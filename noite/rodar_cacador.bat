@echo off
rem Cacador de Obras: roda a rodada completa (coleta, YouTube, Astra, dossies) e abre o relatorio.
powershell -NoProfile -ExecutionPolicy Bypass -File "%~dp0cacador_noite.ps1"
start "" "%~dp0..rtifacts\cacadorecomendadas.html"
