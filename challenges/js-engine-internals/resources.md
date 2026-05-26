# JS Engine Internals — Curated Resources

V8-focused (also applies conceptually to SpiderMonkey/JavaScriptCore). Primary source: https://github.com/v8/v8.

## Anchors (start here)

- https://v8.dev/blog — official V8 blog (primary)
- https://mathiasbynens.be/notes/shapes-ics — Mathias Bynens, hidden classes + ICs
- https://mrale.ph/ — Vyacheslav Egorov, deep JIT posts
- https://github.com/thlorenz/v8-perf — V8 perf internals index

## By sub-topic

### fundamentals (event loop, microtasks, value representation)
- https://html.spec.whatwg.org/multipage/webappapis.html#event-loops — spec (primary)
- https://v8.dev/blog/pointer-compression — SMI tagging + pointer compression
- https://www.youtube.com/watch?v=cCOL7MC4Pl0 — Jake Archibald, event loop
- https://nodejs.org/en/learn/asynchronous-work/event-loop-timers-and-nexttick — Node.js specifics

### v8-objects (hidden classes, ICs, SMI)
- https://v8.dev/blog/fast-properties — fast properties (primary)
- https://mathiasbynens.be/notes/shapes-ics — shapes + inline caches
- https://v8.dev/blog/react-cliff — real-world deopt case study
- `src/objects/map.h`, `src/objects/js-object.h` in V8 source

### jit-pipeline (Ignition → Sparkplug → Maglev → TurboFan)
- https://v8.dev/blog/ignition-interpreter — Ignition bytecode
- https://v8.dev/blog/sparkplug — Sparkplug baseline JIT
- https://v8.dev/blog/maglev — Maglev mid-tier
- https://v8.dev/docs/turbofan — TurboFan optimizing compiler
- https://mrale.ph/blog/2018/02/03/maybe-you-dont-need-rust-and-wasm-to-speed-up-your-js.html — deopt mechanics

### gc (Scavenger, Mark-Compact, incremental)
- https://v8.dev/blog/trash-talk — GC overview (primary)
- https://v8.dev/blog/orinoco — parallel/concurrent/incremental GC
- https://v8.dev/blog/high-performance-cpp-gc — Oilpan (C++ GC, conceptually similar)
- "The Garbage Collection Handbook" — Jones/Hosking/Moss (book, background theory)
