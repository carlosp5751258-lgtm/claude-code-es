---
name: revision-codigo
description: Revisa el diff actual (o una rama) buscando bugs reales, problemas de seguridad y regresiones, y responde en español con hallazgos priorizados. Úsala cuando el usuario pida "revisa mi código", "code review" o "¿está bien este cambio?".
---

# Revisión de código

1. Obtén el diff: `git diff --staged`; si está vacío, `git diff`; si el usuario nombra una rama, `git diff main...<rama>`.
2. Para cada archivo cambiado, lee el contexto suficiente alrededor del cambio (función completa, llamadores).
3. Busca, en este orden:
   - **Correctitud**: casos borde, null/undefined, off-by-one, async sin await, errores tragados.
   - **Seguridad**: inyección (SQL, shell, HTML), secretos en el código, validación de entrada ausente.
   - **Regresiones**: contratos públicos modificados, tests eliminados o debilitados.
4. Descarta lo que no puedas justificar con un escenario concreto. Sin opiniones de estilo salvo que se pidan.
5. Responde con una tabla: `Severidad | Archivo:línea | Problema | Escenario que falla | Arreglo sugerido`.
6. Si no hay hallazgos, dilo claramente; no inventes.
