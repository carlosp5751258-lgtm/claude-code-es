---
name: commits-convencionales
description: Genera mensajes de commit siguiendo Conventional Commits a partir de los cambios en stage. Úsala cuando el usuario pida "haz commit", "mensaje de commit" o "commitea esto".
---

# Commits convencionales

1. Lee `git diff --staged` (si está vacío, pregunta qué añadir; no hagas `git add -A` sin permiso).
2. Elige tipo: `feat`, `fix`, `refactor`, `perf`, `test`, `docs`, `build`, `ci`, `chore`.
3. Ámbito opcional = módulo o carpeta principal afectada.
4. Formato:
   ```
   tipo(ámbito): resumen en imperativo, ≤ 72 caracteres

   Por qué se hizo el cambio (no qué: eso ya lo dice el diff).
   BREAKING CHANGE: <solo si rompe compatibilidad>
   ```
5. Si el diff mezcla cambios no relacionados, propone dividirlo en varios commits.
6. Respeta el idioma de los commits previos del repo (`git log --oneline -10`).
