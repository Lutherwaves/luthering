# TypeScript Internals — Curated Resources

Primary source: https://github.com/microsoft/TypeScript. Cite version tags when referencing.

## Anchors (start here)

- https://basarat.gitbook.io/typescript/overview — Basarat's TS compiler internals handbook (primary)
- https://github.com/microsoft/TypeScript/wiki/Architectural-Overview — official architecture
- https://github.com/microsoft/TypeScript-Compiler-Notes — MS-maintained compiler notes
- Anders Hejlsberg TSConf talks (YouTube)

## By sub-topic

### fundamentals (structural typing, widening/narrowing, inference)
- https://www.typescriptlang.org/docs/handbook/2/narrowing.html — narrowing
- https://www.typescriptlang.org/docs/handbook/type-compatibility.html — structural compat
- https://github.com/microsoft/TypeScript/wiki/FAQ — ground truth for common questions

### compiler-pipeline (scanner → parser → binder → checker → emitter)
- `src/compiler/scanner.ts` — tokenizer
- `src/compiler/parser.ts` — AST construction
- `src/compiler/binder.ts` — symbol tables, control flow graph
- `src/compiler/checker.ts` — THE type checker (60k+ lines; start with `checkSourceFile`)
- `src/compiler/emitter.ts` — JS emission
- Basarat's compiler chapter covers each phase in order

### type-system (conditional, variance, mapped, distributive)
- https://www.typescriptlang.org/docs/handbook/2/conditional-types.html
- https://www.typescriptlang.org/docs/handbook/2/mapped-types.html
- https://github.com/microsoft/TypeScript/pull/21316 — conditional types PR (history + reasoning)
- https://github.com/type-challenges/type-challenges — apply it hands-on

### tooling (language service, incremental, project refs)
- `src/services/` — language service (LSP-ish API)
- https://github.com/microsoft/TypeScript/wiki/Using-the-Language-Service-API
- https://www.typescriptlang.org/docs/handbook/project-references.html
- https://github.com/microsoft/TypeScript/wiki/Performance — incremental build internals
