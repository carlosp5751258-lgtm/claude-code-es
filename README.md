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

## Tutoriales gratis en español
- [Cómo evitar que Claude Code borre tu proyecto: hooks de seguridad](https://dev.to/carlosp5751258lgtm/como-evitar-que-claude-code-borre-tu-proyecto-hooks-de-seguridad-en-5-minutos-2p0l)
- [Tu primera skill de Claude Code en 10 minutos](https://dev.to/carlosp5751258lgtm/tu-primera-skill-de-claude-code-en-10-minutos-en-espanol-5795)
- [El CLAUDE.md perfecto para proyectos Python](https://dev.to/carlosp5751258lgtm/el-claudemd-perfecto-para-proyectos-python-plantilla-lista-para-copiar-21ka)
- [Hooks en Claude Code: bloquea comandos peligrosos](https://dev.to/carlosp5751258lgtm/hooks-en-claude-code-bloquea-comandos-peligrosos-con-un-script-de-20-lineas-3dln)
- [Cómo pedirle a la IA que depure tu código (sin que adivine)](https://dev.to/carlosp5751258lgtm/como-pedirle-a-la-ia-que-depure-tu-codigo-sin-que-adivine-fdo)
- [Cómo borrar ramas de git ya fusionadas sin miedo](https://dev.to/carlosp5751258lgtm/como-borrar-ramas-de-git-ya-fusionadas-sin-miedo-script-bash-con-dry-run-58ba)
- [Tu primer CI en GitHub Actions con matriz de versiones](https://dev.to/carlosp5751258lgtm/tu-primer-ci-en-github-actions-con-matriz-de-versiones-explicado-en-espanol-3l2h)
- [Valida Conventional Commits con un hook de git en bash](https://dev.to/carlosp5751258lgtm/valida-conventional-commits-con-un-hook-de-git-en-bash-sin-instalar-nada-487l)
- [Dockerfile multi-stage para Go: de 800 MB a menos de 20 MB](https://dev.to/carlosp5751258lgtm/dockerfile-multi-stage-para-go-de-800-mb-a-menos-de-20-mb-32mc)
- [Un CLAUDE.md que Claude Code sí respeta: ejemplo con Terraform](https://dev.to/carlosp5751258lgtm/un-claudemd-que-claude-code-si-respeta-ejemplo-real-con-terraform-1ff1)
- [Crea una skill de Claude Code para migraciones de BD](https://dev.to/carlosp5751258lgtm/crea-una-skill-de-claude-code-para-migraciones-de-base-de-datos-sin-sustos-3j95)
- [Formularios de issues en GitHub](https://dev.to/carlosp5751258lgtm/formularios-de-issues-en-github-deja-de-recibir-reportes-de-error-incompletos-1p8)
