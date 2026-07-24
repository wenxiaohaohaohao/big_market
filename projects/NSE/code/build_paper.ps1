$ErrorActionPreference = "Stop"

$ProjectRoot = Split-Path -Parent $PSScriptRoot
$PaperDir = Join-Path $ProjectRoot "paper"
$OutputDir = Join-Path $ProjectRoot "output"
$TempRoot = Join-Path $ProjectRoot "tmp"
$BuildDir = Join-Path $TempRoot "latex"
$XeLaTeX = "D:\application\miktex\miktex\bin\x64\xelatex.exe"

New-Item -ItemType Directory -Force -Path $OutputDir, $BuildDir | Out-Null

$env:TEMP = $TempRoot
$env:TMP = $TempRoot

if (-not (Test-Path -LiteralPath $XeLaTeX)) {
    throw "MiKTeX xelatex was not found at $XeLaTeX"
}

Push-Location $PaperDir
try {
    & $XeLaTeX -interaction=nonstopmode -halt-on-error `
        -jobname=NSE_draft -output-directory="$BuildDir" "main.tex"
    if ($LASTEXITCODE -ne 0) {
        throw "First XeLaTeX pass failed with exit code $LASTEXITCODE"
    }

    & $XeLaTeX -interaction=nonstopmode -halt-on-error `
        -jobname=NSE_draft -output-directory="$BuildDir" "main.tex"
    if ($LASTEXITCODE -ne 0) {
        throw "Second XeLaTeX pass failed with exit code $LASTEXITCODE"
    }

    $BuiltPdf = Join-Path $BuildDir "NSE_draft.pdf"
    $FinalPdf = Join-Path $OutputDir "NSE_draft.pdf"
    $PendingPdf = Join-Path $OutputDir "NSE_draft_pending.pdf"

    try {
        Copy-Item -LiteralPath $BuiltPdf -Destination $FinalPdf -Force
        if (Test-Path -LiteralPath $PendingPdf) {
            Remove-Item -LiteralPath $PendingPdf -Force
        }
        $PublishedPdf = $FinalPdf
    }
    catch [System.IO.IOException] {
        Copy-Item -LiteralPath $BuiltPdf -Destination $PendingPdf -Force
        Write-Warning "NSE_draft.pdf is open. Wrote the new build to NSE_draft_pending.pdf."
        $PublishedPdf = $PendingPdf
    }

    Copy-Item -LiteralPath (Join-Path $BuildDir "NSE_draft.log") `
        -Destination (Join-Path $OutputDir "NSE_draft.log") -Force
}
finally {
    Pop-Location
}

Write-Host "Built $PublishedPdf"
