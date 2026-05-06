# Contributing to Philosophy.execute()

We welcome contributions! Here's how to add a new spec:

## What makes a good spec?

1. **Rooted in tradition** — Connect to actual philosophical lineage (doesn't have to be ancient, but should have history)
2. **Solves a real decision problem** — "Be virtuous" isn't a spec. "How to decide when two virtues conflict" is.
3. **Formalizable** — Can you express it as logic? If not, it might be too abstract for this project.
4. **Worked examples** — Show the spec in action on real scenarios
5. **Honest about limitations** — Where does the formalization break down?

## Submission format

Create a new file in `specs/your-principle-name.md` with:

```markdown
# Your Principle Name

**Principle:** One-line summary

**Tradition:** Where this comes from

**The Ancient Version:** How it was originally stated

**The Problem:** Why the simple version is insufficient

## Formal Specification
(Pseudocode)

## Plain Language
(What it actually means)

## Worked Example
(Real scenario using the spec)

## Edge Cases & Limitations
(Where it breaks down)

## Why This Matters
(For humans, for AI, for both)

## References
(Sources, similar ideas, related specs)
```

## Submission process

1. Fork the repo
2. Create your spec in `specs/`
3. Add at least one example in `examples/`
4. Open a PR with clear description
5. We'll discuss edge cases, refine formalization
6. Merge when consensus is reached

## What we're NOT looking for

- Self-help maxims without philosophical grounding
- Pure abstractions with no decision application
- Specs that are just "do the right thing" reworded
- Anything that can't handle edge cases

## Discussion

Have thoughts on an existing spec? Open an issue tagged `discussion`.

Found a limitation? Open an issue tagged `edge-case`.

Want to debate formalization? That's what the discussions/ folder is for.

## License

By contributing, you agree to release your work under MIT license.