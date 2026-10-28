#!/usr/bin/env python3
"""Hook PreToolUse (Bash): bloquea comandos destructivos antes de que se ejecuten.
Salida con código 2 => Claude Code cancela la llamada y muestra el motivo a Claude."""
import json, re, sys

PATRONES = [
    (r"\brm\s+-[a-zA-Z]*[rR][a-zA-Z]*f?\s+(/|~|\$HOME|\*)(\s|$)", "rm recursivo sobre /, ~ o *"),
    (r"\bgit\s+push\b.*(--force\b|-f\b)(?!-with-lease)", "git push --force (usa --force-with-lease)"),
    (r"\bgit\s+reset\s+--hard\b", "git reset --hard descarta cambios sin commitear"),
    (r"\bgit\s+clean\s+-[a-zA-Z]*f", "git clean -f borra archivos no versionados"),
    (r"\b(mkfs|fdisk|wipefs)\b|\bdd\s+.*of=/dev/", "operación sobre discos"),
    (r":\(\)\s*\{\s*:\|:&\s*\};:", "fork bomb"),
    (r"\bchmod\s+-R\s+777\b", "chmod -R 777"),
    (r"(curl|wget)[^|]*\|\s*(sudo\s+)?(ba|z)?sh\b", "ejecutar script descargado (curl | sh)"),
    (r"\bDROP\s+(TABLE|DATABASE)\b", "DROP TABLE/DATABASE"),
]

data = json.load(sys.stdin)
cmd = (data.get("tool_input") or {}).get("command", "")
for patron, motivo in PATRONES:
    if re.search(patron, cmd, re.IGNORECASE):
        print(f"Bloqueado por hook de seguridad: {motivo}. "
              "Si de verdad es necesario, pide al usuario que lo ejecute él.", file=sys.stderr)
        sys.exit(2)
sys.exit(0)
