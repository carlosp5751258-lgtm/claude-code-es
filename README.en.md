# Claude Code Starter Kit (free)

🇪🇸 [Leer en español](README.md)

Security hooks, skills, a command and CLAUDE.md templates so Claude Code works with rules from day one.

**Free and open source (MIT).** Use it in your projects and your clients' projects. The files are commented in Spanish.

## What's included

- `hooks/`: blocks `rm -rf`, `git push --force`, `curl | sh` and reading `.env` files or SSH keys
- `skills/`: code review and conventional commits
- `comandos/plan.md`: the `/plan` command
- `plantillas-claude-md/`: Node/TypeScript and Python

## Installation

```bash
git clone https://github.com/carlosp5751258-lgtm/claude-code-es.git
mkdir -p .claude/hooks .claude/skills .claude/commands
cp claude-code-es/hooks/*.py .claude/hooks/
cp -r claude-code-es/skills/* .claude/skills/
cp claude-code-es/comandos/*.md .claude/commands/
cp -n claude-code-es/hooks/settings.ejemplo.json .claude/settings.json
```

Copy the template for your stack as `CLAUDE.md` in the project root and restart Claude Code. Type `/hooks` to check that the hooks are active.

## Want the full version?

This is the free version and it works on its own. The **Pro version** adds:

- 6 skills (tests, debugging, documentation, refactoring…) and 4 commands (`/pr`, `/explicar`, `/arreglar-tests`)
- 5 CLAUDE.md templates (Next.js, Django and monorepo on top of the free ones)
- Auto-format and desktop notification hooks
- One-command installer that never overwrites your configuration

👉 [See the Pro version](https://claudecodees.gumroad.com/l/kit-claude-code-es) · pay what you want from 3 USD. Buying it also helps us keep publishing free resources.

## License

MIT: you can use, modify and share it, including in commercial projects. See [LICENSE](LICENSE).

---
Part of **[Ctrl+IA](https://ctrlia.dev/en/)**: resources for coding with AI. Made by Carlos P.
