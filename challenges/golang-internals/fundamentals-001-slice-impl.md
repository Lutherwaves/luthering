## Challenge: Build a Toy Slice from Scratch

**Topic:** golang-internals > fundamentals
**Level:** beginner
**Date:** 2026-04-24

**Sources:**
- `src/runtime/slice.go` — https://github.com/golang/go/blob/master/src/runtime/slice.go
- https://research.swtch.com/godata — Russ Cox, Go data structures
- https://go.dev/blog/slices-intro — Go blog, slice internals

## Problem

Implement a minimal `IntSlice` that reproduces Go's slice semantics (header + backing array + growslice) using `unsafe.Pointer` and manual memory allocation. The goal is to *feel* what the language is doing for you. You will **not** use `[]int` internally for your storage — use an `unsafe.Pointer` to a block of ints you manage yourself.

Two artifacts:

1. **Source-reading notes** at `notes/golang-internals/slice-impl.md` — read `runtime.growslice` in `src/runtime/slice.go` and annotate how it decides the new capacity. Cite file + line numbers (at whatever commit SHA you look at — pin it). 8–15 bullets is plenty.

2. **Toy implementation** at `projects/golang-internals/slice-impl/slice.go` with a test file.

## Requirements

- [ ] `IntSlice` struct has exactly three fields: `array unsafe.Pointer`, `len int`, `cap int`.
- [ ] `New(cap int) IntSlice` — allocates a backing array of size `cap` ints, returns a header with `len=0`.
- [ ] `(s IntSlice) Get(i int) int` — bounds-checked (panic on out-of-range, mimicking Go).
- [ ] `(s *IntSlice) Set(i int, v int)` — bounds-checked.
- [ ] `Append(s IntSlice, v int) IntSlice` — value-receiver style like built-in `append`. If `len < cap`, writes in place and returns new header. If `len == cap`, calls your `growslice` and copies.
- [ ] `growslice(oldCap, newLen int) int` — pure function that returns the new capacity. Match Go 1.18+ behavior: double while `oldCap < 256`, otherwise grow toward `1.25x + 3*256/4` style. You don't have to match the `roundupsize` allocator bucketing — just the growth curve.
- [ ] A test file `slice_test.go` with cases that:
  - verify aliasing: two headers sharing an array see each other's writes
  - verify the "append diverges" behavior from the lesson (write through appended header does not mutate the original)
  - verify `growslice` returns the right capacity for inputs like `(4, 5)`, `(8, 9)`, `(256, 257)`, `(1024, 1025)`
- [ ] `go test ./...` passes.

## Hints

- Allocate with `make([]int, cap)` then take `unsafe.Pointer(&backing[0])` — this is a pragmatic way to get a raw pointer without calling `mallocgc`. The teaching point isn't custom allocation; it's the header-vs-storage split.
- Pointer arithmetic: `unsafe.Add(s.array, i*int(unsafe.Sizeof(int(0))))` gets you element `i`.
- `*(*int)(ptr)` reads; `*(*int)(ptr) = v` writes.
- For `Append` on growth: allocate new backing, `copy` via a loop or `runtime.memmove` equivalent (a simple `for` loop is fine).

## Acceptance Criteria

Scored out of 1.0:

- **Correctness (50%)** — struct layout is exactly the three fields; Append/Get/Set behave like Go's built-ins; growslice curve matches intent.
- **Code quality (25%)** — idiomatic Go, clear naming, minimal comments that explain *why* (not *what*).
- **Edge cases (25%)** — bounds checks, `New(0)`, appending to a zero-value `IntSlice{}`, tests that actually prove aliasing/divergence rather than just exercising the API.

## Solution Files

- `projects/golang-internals/slice-impl/slice.go`
- `projects/golang-internals/slice-impl/slice_test.go`
- `notes/golang-internals/slice-impl.md`

When you're done, tell me and I'll review all three.
