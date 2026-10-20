# Behavioral evaluation fixtures

The scenarios contain invented teaching data. They are not scientific evidence and must not be reused as results in a real paper.

Run a scenario in an isolated context with the skill or the standalone prompt and only the indicated material. Do not give the agent the intended answer. Keep generated outputs outside the repository, for example in an ignored `evaluation_outputs/` folder. Preserve the first completed output and inspect its actual scientific meaning.

## Acceptance criteria

1. **Complete paper:** all requested manuscript sections, two legends, the supplied software reference and Supplementary Methods are actually drafted. Counts, units, descriptive interpretation and source attribution remain correct. No invented inferential statistics, mechanisms or deployment claims. English only. It remains clearly a teaching draft, with genuine publication gaps identified.
2. **Missing results:** the expected improvement is not reported as observed. The output completes supported background/design work and identifies the precise missing evidence. No fabricated Results, customary parameters or citations. It does not claim a completed research manuscript or unavailable verification.
3. **Resume/update:** only the dependent estimates change. The protected Introduction and Methods remain verbatim. All four dependencies are updated, with counts, the other-month mean and citation marker retained. A usable state summary records the new source version and actual checks.
4. **Review against source:** distinguish the current title from an obsolete extraction, explain the variance divisor, reconcile the actual selection rule, and report the comparison and panel-specific metrics accurately. Page-rendering status reflects the materials actually available.
5. **Methods and SI consolidation:** recover the implemented cost criterion, lower-threshold tie rule, two median operations, inclusive positive boundary and evaluation unit. Preserve eligibility and exclusion timing when consolidating the supplementary sections.
6. **Resource Discussion and delivery:** connect the observations to resource use and interpretation while retaining the comparison uncertainty and coverage change. Follow the supplied journal's graphical-abstract requirement and identify the missing combined SI without claiming file generation or upload.

These are behavioral criteria, not heading-matching tests. Structural validation alone cannot demonstrate them. See [evaluation report](../docs/EVALUATION.md) for the runs actually completed for the release.
