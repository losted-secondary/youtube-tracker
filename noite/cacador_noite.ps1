# Caçador de Obras — rodada noturna. Roda sozinho (não depende do Claude aberto).
#   powershell -ExecutionPolicy Bypass -File noite\cacador_noite.ps1
# Fases: coleta+descoberta no YouTube -> agente A (nomes + notas) -> ranking+YouTube -> agente B (dossiês) -> HTML
$ErrorActionPreference = "Continue"
$dir = "C:\Users\victo\Desktop\momo-apps\tracker"
$art = Join-Path $dir "artifacts\cacador"
$log = Join-Path $art "noite.log"
Set-Location $dir
$env:PYTHONIOENCODING = "utf-8"
New-Item -ItemType Directory -Force $art | Out-Null

function Log($m) { $l = "[{0}] {1}" -f (Get-Date -Format "dd/MM HH:mm:ss"), $m; Add-Content -Path $log -Value $l -Encoding utf8; Write-Host $l }

function Py($etapa, [string[]]$a) {
    Log "python $($a -join ' ')"
    $saida = Join-Path $art "noite_$etapa.log"
    & python -u cacador_noite.py @a *> $saida
    Log "  -> fim (código $LASTEXITCODE). $(Get-Content $saida -Tail 1)"
}

function Agente($nome, $prompt) {
    Log "agente $nome (codex gpt-6-astra) começou"
    $saida = Join-Path $art "noite_agente_$nome.log"
    $fim = Join-Path $art "noite_agente_$nome.resposta.md"
    Get-Content (Join-Path $dir "noite\$prompt") -Raw -Encoding utf8 |
        & codex --search exec -m gpt-6-astra -c model_reasoning_effort="medium" `
            --dangerously-bypass-approvals-and-sandbox --skip-git-repo-check -C $dir -o $fim - *> $saida
    Log "agente $nome terminou (código $LASTEXITCODE)"
}

function Fila($arq, $campo) {
    $p = Join-Path $art $arq
    if (-not (Test-Path $p)) { return 0 }
    try { return @((Get-Content $p -Raw -Encoding utf8 | ConvertFrom-Json).$campo).Count } catch { return 0 }
}

Log "===== rodada noturna começou ====="
Py "fase1" @("fase1")
for ($i = 1; $i -le 3; $i++) {
    $nomes = Fila "fila_nomes.json" "videos"; $notas = Fila "fila_notas.json" "obras"
    Log "filas: $nomes vídeos sem nome, $notas obras sem nota"
    if ($nomes -eq 0 -and $notas -eq 0) { break }
    if ($i -gt 1 -and $notas -eq 0) { break }       # nome que o agente não achou fica na fila: não insistir
    Agente "A$i" "prompt_a.md"
    Py "fase1_$i" @("fase1")                          # usa os nomes achados -> obras novas podem pedir nota
}
Py "fase2" @("fase2", "80")
Agente "B" "prompt_b.md"
Py "html" @("html")
Log "===== rodada noturna terminou: $art\recomendadas.html ====="
