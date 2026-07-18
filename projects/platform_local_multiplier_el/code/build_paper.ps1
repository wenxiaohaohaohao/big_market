[CmdletBinding()]
param(
    [switch]$KeepAux
)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'

$ProjectRoot = Split-Path -Parent $PSScriptRoot
$PaperDir = Join-Path $ProjectRoot 'paper'
$OutputDir = Join-Path $ProjectRoot 'output'
$TempDir = Join-Path $ProjectRoot 'tmp\latex'
$MiKTeXBin = 'D:\application\miktex\miktex\bin\x64'
$PdfLaTeX = Join-Path $MiKTeXBin 'pdflatex.exe'
$BibTeX = Join-Path $MiKTeXBin 'bibtex.exe'

foreach ($Executable in @($PdfLaTeX, $BibTeX)) {
    if (-not (Test-Path -LiteralPath $Executable)) {
        throw "Required MiKTeX executable not found: $Executable"
    }
}

New-Item -ItemType Directory -Force -Path $OutputDir, $TempDir | Out-Null
$env:TEMP = $TempDir
$env:TMP = $TempDir

$MainPdfArgs = @(
    '-interaction=nonstopmode'
    '-halt-on-error'
    '-file-line-error'
    '--job-name=paper'
    '--output-directory=../output'
    './main.tex'
)

$SupplementPdfArgs = @(
    '-interaction=nonstopmode'
    '-halt-on-error'
    '-file-line-error'
    '--job-name=supplement'
    '--output-directory=../output'
    './supplement.tex'
)

Push-Location $PaperDir
try {
    & $PdfLaTeX @MainPdfArgs
    if ($LASTEXITCODE -ne 0) {
        throw "First pdfLaTeX pass failed with exit code $LASTEXITCODE."
    }

    & $BibTeX '../output/paper'
    if ($LASTEXITCODE -ne 0) {
        throw "BibTeX failed with exit code $LASTEXITCODE."
    }

    & $PdfLaTeX @MainPdfArgs
    if ($LASTEXITCODE -ne 0) {
        throw "Second pdfLaTeX pass failed with exit code $LASTEXITCODE."
    }

    & $PdfLaTeX @MainPdfArgs
    if ($LASTEXITCODE -ne 0) {
        throw "Final pdfLaTeX pass failed with exit code $LASTEXITCODE."
    }

    & $PdfLaTeX @SupplementPdfArgs
    if ($LASTEXITCODE -ne 0) {
        throw "First supplement pdfLaTeX pass failed with exit code $LASTEXITCODE."
    }

    & $PdfLaTeX @SupplementPdfArgs
    if ($LASTEXITCODE -ne 0) {
        throw "Final supplement pdfLaTeX pass failed with exit code $LASTEXITCODE."
    }
}
finally {
    Pop-Location
}

$PdfPath = Join-Path $OutputDir 'paper.pdf'
if (-not (Test-Path -LiteralPath $PdfPath)) {
    throw "Expected PDF was not created: $PdfPath"
}
$SupplementPdfPath = Join-Path $OutputDir 'supplement.pdf'
if (-not (Test-Path -LiteralPath $SupplementPdfPath)) {
    throw "Expected supplement PDF was not created: $SupplementPdfPath"
}

if (-not $KeepAux) {
    $AuxiliarySuffixes = @(
        '.aux'
        '.bbl'
        '.blg'
        '.fdb_latexmk'
        '.fls'
        '.log'
        '.out'
        '.run.xml'
        '.synctex.gz'
        '.toc'
    )

    foreach ($Stem in @('paper', 'supplement')) {
        foreach ($Suffix in $AuxiliarySuffixes) {
            $AuxiliaryPath = Join-Path $OutputDir ("$Stem$Suffix")
            if (Test-Path -LiteralPath $AuxiliaryPath) {
                Remove-Item -LiteralPath $AuxiliaryPath -Force
            }
        }
    }

    $AccidentalSourceLog = Join-Path $PaperDir 'paper.log'
    if (Test-Path -LiteralPath $AccidentalSourceLog) {
        Remove-Item -LiteralPath $AccidentalSourceLog -Force
    }
}

Write-Output "Built $PdfPath"
Write-Output "Built $SupplementPdfPath"
