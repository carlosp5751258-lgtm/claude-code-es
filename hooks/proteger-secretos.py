#!/usr/bin/env python3
"""Hook PreToolUse (Read|Edit|Write): impide leer o modificar archivos con secretos."""
import json, re, sys
from pathlib import PurePath

SENSIBLES = [r"(^|/)\.env(\.[\w-]+)?$", r"\.pem$", r"\.key$", r"(^|/)id_(rsa|ed25519|ecdsa)$",
             r"(^|/)\.aws/credentials$", r"(^|/)\.npmrc$", r"(^|/)secrets?\.(json|ya?ml)$"]
PERMITIDOS = [r"\.env\.(example|sample|template)$"]

data = json.load(sys.stdin)
ruta = (data.get("tool_input") or {}).get("file_path", "")
p = PurePath(ruta).as_posix()
if any(re.search(x, p) for x in PERMITIDOS):
    sys.exit(0)
if any(re.search(x, p) for x in SENSIBLES):
    print(f"Bloqueado: '{ruta}' puede contener secretos. Usa un .env.example o pide los valores al usuario.",
          file=sys.stderr)
    sys.exit(2)
sys.exit(0)
