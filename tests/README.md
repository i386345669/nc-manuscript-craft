# Behavioral evaluation fixtures

The scenarios contain invented teaching data. They are not scientific evidence and must not be reused as results in a real paper.

Run a scenario in an isolated context with the skill or the standalone prompt and only the indicated material. Do not give the agent the intended answer. Keep generated outputs outside the repository, for example in an ignored `evaluation_outputs/` folder. Preserve the first completed output and inspect its actual scientific meaning.

## Acceptance criteria

1. **Complete paper:** all requested manuscript sections, two legends, the supplied software reference and Supplementary Methods are actually drafted. Counts, units, descriptive interpretation and source attribution remain correct. No invented inferential statistics, mechanisms or deployment claims. English only. It remains clearly a teaching draft, with genuine publication gaps identified.
2. **Missing results:** the expected improvement is not reported as observed. The output completes supported background/design work and identifies the precise missing evidence. No fabricated Results, customary parameters or citations. It does not claim a completed research manuscript or unavailable verification.
3. **Resume/update:** only the dependent estimates change. The protected Introduction and Methods remain verbatim. All four dependencies are updated, with counts, the other-month mean and citation marker retained. A usable state summary records the new source version and actual checks.

These are behavioral criteria, not heading-matching tests. Structural validation alone cannot demonstrate them. See [evaluation report](../docs/EVALUATION.md) for the runs actually completed for the release.
