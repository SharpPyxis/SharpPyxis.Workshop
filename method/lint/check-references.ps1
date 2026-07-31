# check-references.ps1 — every location a workshop cites must resolve.
#
# Run it after renaming or moving anything the framing cites, and at every session close.
#
# Three checks:
#
#  1. LINKS — every markdown link target must resolve. A link is unambiguously a location:
#     it is clickable, and a dangling one sends a reader to a file that is not there.
#
#  2. PREFIXED — backticked tokens starting with a declared prefix must resolve. The prefixes
#     are the structural folders of the layout, passed in by the caller.
#
#  3. RETIRED — names declared retired must not appear anywhere, including outside the framing
#     folder. Paths leak into code comments and dotfile headers, which have no reason to follow
#     the corpus when it moves. This is the migration check.
#
# ⚠ Why checks 1 and 2 are narrow, and must stay narrow. A first version tried to resolve every
# backticked token that "looked like a path". It produced several hundred false failures on a
# real workshop, because almost every such token is an IDENTITY, not a location: a document
# named without its folder, a URL route, a MIME type, a date format, a list of tool names. The
# corpus was already citing by identity — which is the rule (see method/organization.md) — and
# the check punished it. A lint verifies what is declared to be a location; it does not guess.
#
# Exit code 1 if any FAIL.

[CmdletBinding()]
param(
    # The framing folder to check — a workshop's _workspace.
    [Parameter(Mandatory)] [string] $Framing,
    # Extra roots a citation may be relative to, beyond the framing folder, the workshop and
    # the projects root. Typically the workshop's repositories, and the method repository.
    [string[]]  $ExtraRoots = @(),
    # Backtick prefixes that declare a location and must therefore resolve.
    [string[]]  $MustResolvePrefixes = @(),
    # Further folders to sweep for retired names only — a code repository, for instance.
    [string[]]  $AlsoScan = @(),
    # Retired name -> what to write instead.
    [hashtable] $Retired = @{},
    # File name patterns exempt from both resolution checks and from the retired sweep.
    # Archives record what was true then: rewriting them would falsify a record to satisfy a
    # lint, and they are read on explicit demand only, never in the reading chain.
    [string[]]  $Exclude = @()
)

$ErrorActionPreference = 'Stop'
$script:failed = $false

function Report([string]$level, [string]$msg) {
    $color = switch ($level) { 'OK' { 'Green' } 'WARN' { 'Yellow' } 'FAIL' { 'Red' } }
    Write-Host ("[{0,-4}] {1}" -f $level, $msg) -ForegroundColor $color
    if ($level -eq 'FAIL') { $script:failed = $true }
}

$framingRoot  = (Resolve-Path -LiteralPath $Framing).Path
$workshopRoot = Split-Path $framingRoot -Parent
$projectsRoot = Split-Path $workshopRoot -Parent

$roots = @($framingRoot, $workshopRoot, $projectsRoot)
$roots += $ExtraRoots | Where-Object { Test-Path -LiteralPath $_ } | ForEach-Object { (Resolve-Path -LiteralPath $_).Path }

function Test-Resolves([string]$token, [string]$fromDir) {
    $rel = $token -replace '/', [IO.Path]::DirectorySeparatorChar
    if ($rel -match '^([A-Za-z]:|\\)') { return (Test-Path -LiteralPath $rel) }
    foreach ($r in (@($fromDir) + $roots)) {
        if (Test-Path -LiteralPath (Join-Path $r $rel)) { return $true }
    }
    return $false
}

$docs = @(Get-ChildItem -LiteralPath $framingRoot -Recurse -File -Filter '*.md' |
          Where-Object { $d = $_; $d.FullName -notmatch '\\\.git\\' -and
                         -not ($Exclude | Where-Object { $d.Name -like $_ }) })

# --- 1. LINKS ------------------------------------------------------------------------------
$linkCount = 0; $linkBad = 0
foreach ($doc in $docs) {
    $n = 0
    foreach ($line in (Get-Content -LiteralPath $doc.FullName)) {
        $n++
        foreach ($m in [regex]::Matches($line, '\]\(([^)\s]+)\)')) {
            $t = $m.Groups[1].Value
            if ($t -match '^(https?:|mailto:|#)') { continue }
            $t = ($t -split '#')[0]
            if (-not $t) { continue }
            $linkCount++
            if (-not (Test-Resolves $t $doc.DirectoryName)) {
                $linkBad++
                Report FAIL ("lien pendant — {0}:{1} « {2} »" -f $doc.Name, $n, $t)
            }
        }
    }
}
if ($linkBad -eq 0) { Report OK "liens markdown : $linkCount cible(s), toutes résolues" }

# --- 2. PREFIXED ---------------------------------------------------------------------------
if ($MustResolvePrefixes.Count -gt 0) {
    $pfxCount = 0; $pfxBad = 0
    foreach ($doc in $docs) {
        $n = 0
        foreach ($line in (Get-Content -LiteralPath $doc.FullName)) {
            $n++
            foreach ($m in [regex]::Matches($line, '`([^`]+)`')) {
                $t = $m.Groups[1].Value.Trim().TrimEnd('.', ',', ';', ':')
                if ($t -match '\s|[<>*?|"…]') { continue }
                if (-not ($MustResolvePrefixes | Where-Object { $t.StartsWith($_) })) { continue }
                $pfxCount++
                if (-not (Test-Resolves $t $doc.DirectoryName)) {
                    $pfxBad++
                    Report FAIL ("emplacement pendant — {0}:{1} « {2} »" -f $doc.Name, $n, $t)
                }
            }
        }
    }
    if ($pfxBad -eq 0) { Report OK "emplacements préfixés : $pfxCount cité(s), tous résolus" }
}

# --- 3. RETIRED ----------------------------------------------------------------------------
if ($Retired.Count -gt 0) {
    $scan  = @($framingRoot) + @($AlsoScan | Where-Object { Test-Path -LiteralPath $_ })
    $files = @(Get-ChildItem -LiteralPath $scan -Recurse -File -Force |
               Where-Object {
                   $_.FullName -notmatch '\\(\.git|bin|obj|node_modules)\\' -and $_.Length -lt 1mb
               })
    if ($Exclude.Count -gt 0) {
        $files = @($files | Where-Object { $f = $_; -not ($Exclude | Where-Object { $f.Name -like $_ }) })
    }
    $hits = 0
    foreach ($old in $Retired.Keys) {
        # -SimpleMatch takes the pattern literally: escaping it for a regex would make the
        # search look for the backslashes themselves, and the check would silently find less
        # than it should. Observed on the first run — only the token with no special character
        # was reported.
        $found = @(Select-String -LiteralPath $files.FullName -Pattern $old -SimpleMatch -ErrorAction SilentlyContinue)
        foreach ($h in $found) {
            $hits++
            Report FAIL ("nom retiré « {0} » — {1}:{2} → {3}" -f $old, (Split-Path $h.Path -Leaf), $h.LineNumber, $Retired[$old])
        }
    }
    if ($hits -eq 0) { Report OK "noms retirés : aucune occurrence des $($Retired.Count) nom(s) déclaré(s)" }
}

Write-Host ''
if ($script:failed) { Write-Host 'Des contrôles FAIL — corriger avant de committer.' -ForegroundColor Red; exit 1 }
Write-Host 'Renvois sains.' -ForegroundColor Green
