# Claude Code en Español — Hooks de seguridad gratis 🛡️

Dos hooks que **impiden que Claude Code ejecute comandos destructivos o lea tus secretos**, y una skill de revisión de código en español.

- `bloquear-comandos-peligrosos.py`: frena `rm -rf /`, `git push --force`, `git reset --hard`, `curl | sh`, `DROP TABLE`…
- `proteger-secretos.py`: bloquea la lectura o edición de `.env`, claves `.pem` o SSH y `~/.aws/credentials` (permite `.env.example`).
- `skills/revision-codigo`: code review con hallazgos priorizados por severidad.

## Instalar
```bash
mkdir -p .claude/hooks .claude/skills
cp hooks/*.py .claude/hooks/ && cp -r skills/* .claude/skills/
cp hooks/settings.ejemplo.json .claude/settings.json   # o fusiona la sección "hooks" con la tuya
```

## ¿Quieres el kit completo?
**[Kit Claude Code en Español](https://claudecodees.gumroad.com/l/kit-claude-code-es)**: 6 skills, 4 comandos (`/plan`, `/pr`, `/explicar`, `/arreglar-tests`),
5 plantillas CLAUDE.md (Node, Python, Next.js, Django, monorepo), autoformato, notificaciones e instalador. 9 USD.

Página del proyecto: https://carlosp5751258-lgtm.github.io/claude-code-es/

Licencia MIT (solo esta versión gratuita).
