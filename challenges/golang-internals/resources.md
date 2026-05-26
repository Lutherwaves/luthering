# Go Internals — Curated Resources

Primary sources first. Cite commit SHAs or version tags when drawing from `src/runtime/*`.

## Anchors (start here)

- https://github.com/emluque/golang-internals-resources — curated index
- https://internals-for-interns.com/posts/understanding-go-runtime/ — accessible runtime overview
- https://antonz.org/go-concurrency/internals/ — concurrency primitives walkthrough
- https://go.dev/ref/mem — official Go memory model (primary)
- https://research.swtch.com/godata — Russ Cox, Go data structures

## By sub-topic

### fundamentals (slices, maps, strings, escape analysis)
- `src/runtime/slice.go`, `src/runtime/string.go`, `src/runtime/map.go` (primary source)
- https://go.dev/blog/slices-intro — slice internals
- https://go.dev/blog/maps — map usage + impl overview
- `go build -gcflags="-m"` — see escape analysis output

### runtime (GMP scheduler, goroutines, channels)
- `src/runtime/proc.go` — `schedule()`, `findrunnable()` (primary source)
- `src/runtime/chan.go` — channel send/recv, sudog queues
- https://rakyll.org/scheduler/ — Jaana Dogan's scheduler intro
- https://www.youtube.com/watch?v=YHRO5WQGh0k — Kavya Joshi, scheduler deep-dive

### gc-allocator (tri-color mark, mcache/mcentral/mheap)
- `src/runtime/mgc.go`, `src/runtime/malloc.go`, `src/runtime/mheap.go` (primary source)
- https://go.dev/doc/gc-guide — official GC guide
- https://tip.golang.org/src/runtime/HACKING.md — runtime hacking notes
- Rick Hudson's GC talks (GopherCon)

### compiler-ssa (parser, AST, SSA)
- `src/go/parser`, `src/go/ast` — front end
- `src/cmd/compile/internal/ssa/README.md` — SSA backend (primary)
- https://github.com/golang/go/tree/master/src/cmd/compile — compiler source
- Keith Randall's SSA talks
