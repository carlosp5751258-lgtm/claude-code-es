# Kit Claude Code en español (gratis)

🇬🇧 [Read in English](README.en.md)

Hooks de seguridad, skills, un comando y plantillas CLAUDE.md para que Claude Code trabaje con reglas desde el primer día.

**Gratis y de código abierto (MIT).** Úsalo en tus proyectos y en los de tus clientes.

## Qué incluye

- `hooks/`: bloquea `rm -rf`, `git push --force`, `curl | sh` y la lectura de `.env` o llaves SSH
- `skills/`: revisión de código y commits convencionales
- `comandos/plan.md`: el comando `/plan`
- `plantillas-claude-md/`: Node/TypeScript y Python

## Instalación

```bash
git clone https://github.com/carlosp5751258-lgtm/claude-code-es.git
mkdir -p .claude/hooks .claude/skills .claude/commands
cp claude-code-es/hooks/*.py .claude/hooks/
cp -r claude-code-es/skills/* .claude/skills/
cp claude-code-es/comandos/*.md .claude/commands/
cp -n claude-code-es/hooks/settings.ejemplo.json .claude/settings.json
```

Copia la plantilla de tu stack como `CLAUDE.md` en la raíz del proyecto y reinicia Claude Code. Escribe `/hooks` para comprobar que los hooks están activos.

## ¿Quieres la versión completa?

Esta es la versión gratis y funciona sola. La **versión Pro** añade:

- 6 skills (tests, depuración, documentación, refactor…) y 4 comandos (`/pr`, `/explicar`, `/arreglar-tests`)
- 5 plantillas CLAUDE.md (Next.js, Django y monorepo además de las gratis)
- Hooks de autoformato y aviso de escritorio
- Instalador de un comando que nunca sobrescribe tu configuración

👉 [Ver la versión Pro](https://claudecodees.gumroad.com/l/kit-claude-code-es) · paga lo que quieras desde 3 USD. Comprarla también ayuda a que sigamos publicando recursos gratis.

## Licencia

MIT: puedes usarlo, modificarlo y compartirlo, también en proyectos comerciales. Ver [LICENSE](LICENSE).

---
Parte de **[Ctrl+IA](https://ctrlia.dev/)**: recursos en español para programar con IA. Hecho por Carlos P.
