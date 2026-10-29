# CLAUDE.md — Proyecto Node.js + TypeScript

## Comandos
- Instalar: `npm ci`
- Desarrollo: `npm run dev`
- Tests: `npm test` (un archivo: `npx vitest run ruta/al/archivo.test.ts`)
- Tipos: `npx tsc --noEmit`
- Lint: `npm run lint -- --fix`

## Convenciones
- TypeScript estricto: nada de `any`. Si no se conoce el tipo, usa `unknown` y estréchalo.
- Imports absolutos desde `src/` (alias `@/`).
- Errores: lanza clases propias que extiendan `Error`; nunca strings.
- Las funciones async siempre se `await`-ean o se devuelven; nada de promesas flotantes.

## Flujo de trabajo
1. Antes de editar, lee el test existente del módulo.
2. Tras cada cambio: `npx tsc --noEmit && npm test`.
3. No toques `package-lock.json` a mano.

## No hacer
- No añadir dependencias sin preguntar.
- No desactivar reglas de ESLint con comentarios.
