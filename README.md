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
5 plantillas CLAUDE.md (Node, Python, Next.js, Django, monorepo), autoformato, notificaciones e instalador. Paga lo que quieras desde 1 USD.

Página del proyecto: https://carlosp5751258-lgtm.github.io/claude-code-es/

Licencia MIT (solo esta versión gratuita).

## Catálogo completo (paga lo que quieras, desde 1 USD)
| Producto | Para qué sirve |
|---|---|
| [Kit Claude Code en Español](https://claudecodees.gumroad.com/l/kit-claude-code-es) | 6 skills, 4 comandos, 5 plantillas CLAUDE.md, hooks e instalador |
| [Guía Claude Code de Cero a Experto (PDF)](https://claudecodees.gumroad.com/l/guia-claude-code) | 30 páginas: CLAUDE.md, permisos, skills, hooks, subagentes, MCP |
| [15 Plantillas CLAUDE.md por Stack](https://claudecodees.gumroad.com/l/plantillas-claude-md) | Go, Rust, Laravel, Rails, Flutter, FastAPI, Terraform y más |
| [Pack 8 Skills Avanzadas](https://claudecodees.gumroad.com/l/skills-avanzadas) | TDD, migraciones, OWASP, rendimiento, a11y, APIs, releases, i18n |
| [100 Prompts para Programadores](https://claudecodees.gumroad.com/l/100-prompts-programadores) | PDF + Markdown + CSV en 10 categorías |
| [Pack GitHub Actions CI](https://claudecodees.gumroad.com/l/github-actions-ci) | 8 workflows comentados |
| [Pack Git Hooks y Pre-commit](https://claudecodees.gumroad.com/l/git-hooks-precommit) | Bloquea secretos, valida commits, tests antes del push |
| [Pack Dockerfiles Optimizados](https://claudecodees.gumroad.com/l/dockerfiles-optimizados) | Node, Next.js, FastAPI, Go + compose |
| [Plantillas de Documentación para GitHub](https://claudecodees.gumroad.com/l/plantillas-docs-github) | README, CONTRIBUTING, SECURITY, issue forms, PR, CHANGELOG |
| [Pack 12 Scripts Bash](https://claudecodees.gumroad.com/l/scripts-bash-devs) | Limpieza, backups, git, puertos, SSL y más |
