---
layout: default
title: What the JavaScript course covers
lang: en
permalink: /en/javascript/the-course/
---

# What the course covers

31 steps in eight modules. The tutor unlocks them in order, so you never have to decide what comes
next. Each step states its learning goal, gives you something to run, and asks you to explain what
happened before it counts the step as understood. No prior programming experience is assumed.

## M0 — Tooling

The window and the runtime, not the language. Skipping this module is the single most reliable way
to get stuck in module 1.

| Step | What you do |
|---|---|
| Operating the interface | The five parts of the window, three ways to run a command, closing a terminal |
| Your first run | Running a file with Node, and what the prompt coming back means |
| Reading a test | What a failing assertion tells you, and why red is the normal starting state |
| Modules, exports and imports | Why a missing export stops a whole test file from loading |
| Predict before you run | Write down what you expect first — the habit the whole course builds on |

## M1 — Values and types

| Step | What you do |
|---|---|
| `let`, `const` and the temporal dead zone | Where a name exists, and where it only looks as if it does |
| Types and what `typeof` will not tell you | The type system's honest and dishonest answers |
| Coercion, `+` and the value that equals nothing | Why `+` sometimes adds and sometimes joins |
| `==` against `===`, and the one case `===` gets wrong | The comparison rules, including the exception |

## M2 — Control flow and error handling

| Step | What you do |
|---|---|
| `if`, `else` and a switch that falls through | Branching, and the missing `break` |
| Truthy, falsy and the defaults that eat your values | Why `0` and `""` disappear where you did not expect it |
| `try`, `catch`, `finally` and who gets the error | Where an error goes when you do not catch it |
| Error objects and an error class of your own | Errors that carry what the caller needs |

## M3 — Loops and iteration

| Step | What you do |
|---|---|
| `for` and `while`, and which one fits | Choosing a loop by what you actually know in advance |
| Off by one, and the error it hands you | The classic mistake, and how the output betrays it |
| `for…of` against `for…in` | Values against keys, and the bug the confusion causes |
| `break`, `continue` and a labelled exit | Leaving a loop deliberately |

## M4 — Functions and closures

| Step | What you do |
|---|---|
| Declarations, expressions and when a name exists | Hoisting, in the only form that matters in practice |
| Default and rest parameters | Functions that take what they are given |
| Closures, and what a loop variable captures | The classic closure trap, run rather than described |
| Arrow functions and losing `this` | Two function forms, and the difference that bites |

## M5 — Objects and arrays

| Step | What you do |
|---|---|
| Objects, references and copying | Who else holds the thing you just changed |
| Reading through levels that may not exist | Optional chaining instead of a chain of guards |
| Arrays, `length` and who owns the data | Mutating in place against producing something new |
| `map`, `filter`, `reduce` and a sort that lies | The transformations, and the default sort's surprise |

## M6 — Asynchrony

| Step | What you do |
|---|---|
| Promises, and what a pending value is | A value that is not there yet |
| `async`, `await` and the missing `await` | The mistake that produces a promise where you wanted a result |
| Errors that arrive late | Failures that no `try` around the call will catch |
| Sequential or concurrent, and what a caller must learn | Choosing deliberately, and documenting the choice |

## M7 — Capstone project

| Step | What you do |
|---|---|
| Designing the report tool | Decide the structure before writing the code |
| Building the report tool, and testing it yourself | Implement it, and invent your own test cases |

The last step asks you to write the tests, not just pass them: you have to decide what is worth
checking, which is a different skill from making a given test go green.

## Related

- [Your first session]({{ '/en/javascript/first-session/' | relative_url }})
- [When a check will not pass]({{ '/en/javascript/when-a-check-fails/' | relative_url }})
- [JavaScript Tutor docs]({{ '/en/javascript/' | relative_url }})
