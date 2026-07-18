[CmdletBinding()]
param(
    [switch]$KeepAux
)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'

$ProjectRoot = Split-Path -Parent $PSScriptRoot
$SourceDir = Join-Path $ProjectRoot 'notes\teaching'
$OutputDir = Join-Path $ProjectRoot 'output\teaching'
$TempDir = Join-Path $ProjectRoot 'tmp\teaching_latex'
$MiKTeXBin = 'D:\application\miktex\miktex\bin\x64'
$XeLaTeX = Join-Path $MiKTeXBin 'xelatex.exe'
$JobName = 'EL_model_teaching_note_zh'
$SourceFile = '.\EL_model_teaching_note_zh.tex'

if (-not (Test-Path -LiteralPath $XeLaTeX)) {
    throw "Required MiKTeX executable not found: $XeLaTeX"
}

New-Item -ItemType Directory -Force -Path $OutputDir, $TempDir | Out-Null
$env:TEMP = $TempDir
$env:TMP = $TempDir

$XeLaTeXArgs = @(
    '-interaction=nonstopmode'
    '-halt-on-error'
    '-file-line-error'
    "--job-name=$JobName"
    '--output-directory=../../output/teaching'
    $SourceFile
)

Push-Location $SourceDir
try {
    for ($Pass = 1; $Pass -le 3; $Pass++) {
        & $XeLaTeX @XeLaTeXArgs
        if ($LASTEXITCODE -ne 0) {
            throw "XeLaTeX pass $Pass failed with exit code $LASTEXITCODE."
        }
    }
}
finally {
    Pop-Location
}

$PdfPath = Join-Path $OutputDir "$JobName.pdf"
if (-not (Test-Path -LiteralPath $PdfPath)) {
    throw "Expected PDF was not created: $PdfPath"
}

if (-not $KeepAux) {
    $AuxiliarySuffixes = @(
        '.aux'
        '.fdb_latexmk'
        '.fls'
        '.log'
        '.out'
        '.synctex.gz'
        '.toc'
    )

    foreach ($Suffix in $AuxiliarySuffixes) {
        $AuxiliaryPath = Join-Path $OutputDir "$JobName$Suffix"
        if (Test-Path -LiteralPath $AuxiliaryPath) {
            Remove-Item -LiteralPath $AuxiliaryPath -Force
        }
    }
}

Write-Output "Built $PdfPath"
