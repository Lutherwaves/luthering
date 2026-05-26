# Python Internals — Curated Resources

Primary sources first. CPython source at https://github.com/python/cpython. Cite version tags (e.g., v3.13.0) and file paths.

## Anchors (start here)

- https://devguide.python.org/internals/ — official devguide
- https://realpython.com/cpython-source-code-guide/ — source tour
- "CPython Internals" — Anthony Shaw (book, realpython.com/products/cpython-internals-book/)
- https://tenthousandmeters.com/ — "Python behind the scenes" series

## By sub-topic

### fundamentals (PyObject, refcount, object model, dict)
- `Include/object.h`, `Objects/object.c` — PyObject, refcount macros (primary)
- `Objects/dictobject.c` — split/combined dict, open addressing
- `Objects/listobject.c` — list overallocation strategy
- https://docs.python.org/3/c-api/structures.html — C API structures

### bytecode-ceval (dis, ceval.c, frames)
- `Python/ceval.c` — main interpreter loop (primary)
- `Python/compile.c` — AST → bytecode
- `Include/internal/pycore_frame.h` — frame objects (3.11+ zero-cost frames)
- Python `dis` module — run `dis.dis(func)` on anything
- PEP 659 — Specializing Adaptive Interpreter
- https://tenthousandmeters.com/blog/python-behind-the-scenes-4-how-python-bytecode-is-executed/

### gc-gil (cyclic GC, GIL, PEP 703)
- `Python/gc.c` — cyclic GC, generations (primary)
- `Python/ceval_gil.c` — GIL implementation
- PEP 703 — Making the GIL optional
- https://tenthousandmeters.com/blog/python-behind-the-scenes-13-the-gil-and-its-effects-on-python-multithreading/
- https://pythonspeed.com/articles/python-gil/ — Itamar Turner-Trauring

### c-extensions (C API, capsules, buffer protocol)
- https://docs.python.org/3/extending/ — official extending docs
- https://docs.python.org/3/c-api/ — C API reference
- https://pybind11.readthedocs.io/ — pybind11 (higher-level, but source-readable)
- PEP 3118 — Buffer Protocol
