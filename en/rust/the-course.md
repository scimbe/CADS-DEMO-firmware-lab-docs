---
layout: default
title: What the Rust course covers
lang: en
permalink: /en/rust/the-course/
---

# What the course covers

31 steps in eight modules. The tutor unlocks them in order, so you never have to decide what comes
next. Each step states its learning goal, gives you something to run, and asks you to explain what
happened before it counts the step as understood.

## M0 — Tooling and your first program

The window and the toolchain, not the language. Skipping this module is the single most reliable
way to get stuck in module 1.

| Step | What you do |
|---|---|
| Where you are and what to press first | Get oriented: what this environment is, what is already installed |
| Operating the workbench | The five parts of the window, three ways to run a command, closing a terminal |
| Read a test, then make it pass | Your first `cargo test`, and what a failing test is telling you |
| Predict the output, then run it | Write down what you expect before you run it — the habit the whole course builds on |
| Read a compiler error and repair the file | The compiler as a teaching tool rather than an obstacle |

## M1 — Ownership

| Step | What you do |
|---|---|
| Scope, owner, move | Who owns a value, and when it is dropped |
| Move or clone: which one you actually need | The cost of `clone`, and when it is the wrong reflex |
| Copy types: when assignment is not a move | Why some assignments leave the original usable |
| Ownership across function boundaries | Passing values in and getting them back |

## M2 — References and borrowing

| Step | What you do |
|---|---|
| Borrow instead of taking | Shared references and what they allow |
| Mutable references | One writer, and what the compiler does about it |
| The aliasing rule: readers or one writer | The rule behind half of all borrow-checker errors |
| Slices: a borrow of part of a collection | Views into data without copying it |

## M3 — Structs and enums

| Step | What you do |
|---|---|
| Structs: values that belong together | Modelling data that travels as a unit |
| Enums: one of several shapes | States a value can be in, made explicit |
| `match`: every case, checked | Exhaustiveness, and why the compiler insists on it |
| `if let` and `let … else` | The short forms, and when they read better |

## M4 — Collections

| Step | What you do |
|---|---|
| Vectors: a growable list | Building, indexing and iterating |
| Strings are UTF-8, and that changes things | Bytes, characters, and the traps between them |
| Hash maps and the entry idiom | Counting and grouping without repeated lookups |
| The three collections together | Choosing the right one for a real task |

## M5 — Error handling

| Step | What you do |
|---|---|
| `panic!` is for bugs | The difference between a bug and an expected failure |
| `Result`: failure in the return type | Making failure visible to the caller |
| The `?` operator | Propagating errors without ceremony |
| Your own error type | An error that carries what the caller needs |

## M6 — Generics, traits and lifetimes

| Step | What you do |
|---|---|
| Generics: one function, many types | Writing code once for many types |
| Traits: shared behaviour with a name | Describing what a type can do |
| Trait bounds: asking for exactly what you need | Constraining generics, and reading the error when you do not |
| Lifetimes: how long a borrow is valid | The last piece of the borrow checker |

## M7 — Final project

| Step | What you do |
|---|---|
| Build `wordstat` | A small tool that uses everything above |
| Review your own tool | Judge your own code against criteria you have to apply yourself |

The last step is deliberately an evaluation, not another exercise: you argue for your own design
decisions and defend the trade-offs you made.

## Related

- [Your first session]({{ '/en/rust/first-session/' | relative_url }})
- [When a check will not pass]({{ '/en/rust/when-a-check-fails/' | relative_url }})
- [Rust Tutor docs]({{ '/en/rust/' | relative_url }})
