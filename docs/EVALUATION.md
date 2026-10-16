# Evaluation scope and observed results

The initial public package was evaluated on 16 October 2026 using three synthetic teaching scenarios and four independent executions. These checks assess observable drafting behavior, not journal acceptance, AI-detector scores or correctness on every future manuscript.

## Behavioral checks

Each evaluator received one scenario and either the standalone prompt alone or the installable skill. Evaluators used a fresh task context and were not given the intended answer, previous outputs or suspected failure. The maintainer inspected the resulting text rather than relying only on an evaluator's self-report.

| Scenario | Input and execution | Observed outcome |
|---|---|---|
| [Complete paper](../tests/scenarios/01-complete-paper.md) | Standalone prompt only, supplied synthetic monitoring results and one software reference. Executed twice in separate contexts | Both runs produced a full English teaching manuscript with abstract, Introduction, Results, Discussion, Methods, supplementary methods, reference and two figure legends. The final run preserved the supplied counts, means and difference without inventing inferential statistics or deployment efficacy |
| [Missing results](../tests/scenarios/02-missing-results.md) | Skill plus a planned experiment and an expected effect, with no observed results | Produced a clearly incomplete, prospective draft and specific author queries. Did not turn the expected effect into a finding or invent replicates, statistical tests, p values or citations |
| [Resume after a source update](../tests/scenarios/03-resume-source-update.md) | Skill plus an existing draft, protected passages and a revised authoritative source | Updated the four dependent components: abstract, Results, table and legend. Preserved unrelated counts, the other mean, citation numbering and protected Introduction/Methods text. Recorded the revised source and continuation state |

The first complete-paper run included unnecessary source-material narration and publication-preparation gaps inside Results. This led to a focused clarification separating manuscript prose from author notes. A second standalone-only execution improved this separation and completed the requested manuscript. Ordinary editorial judgment is still needed: for example, a prototype's absent usability evaluation could be moved from Results to limitations depending on the article's purpose. No further rewrite was required to satisfy the scientific-preservation and full-delivery criteria tested here.

The final complete-paper draft contained 1,154 whitespace-delimited tokens including headings and notes, with a 130-word abstract. Length is reported to make the observed output concrete, not as a manuscript-length target. The fixtures intentionally describe a small teaching study and do not test a publication-length biomedical manuscript.

## Package checks

`python scripts/validate.py` checks required files, metadata, routed references, local links, prompt-copy synchronization, installable license copies, CSV structure and several obvious private-information patterns. The official skill-creator validator separately checks the skill entry's format. These checks do not prove scientific meaning or discover every possible confidential detail.

Release verification also installs the committed skill subtree from GitHub using the official skill-installer and compares its files with the release source. This checks distribution and packaging rather than manuscript quality. The repository's CI reruns the structural validator on pushes and pull requests.

## Limits

- Three scenarios cannot establish general reliability across disciplines, languages, study designs or long projects.
- The behavioral fixtures do not exercise Word rendering, tracked changes, editable SVG reconstruction, real database access, reference searches or manuscript submission. Instructions for those tasks are not equivalent to successful execution.
- The supplied software reference was checked during fixture preparation. The evaluation agent did not independently verify it through a live literature search.
- All example research details are synthetic. Private development conversations, unpublished research files and raw evaluation workspaces are excluded from this repository.
- Review the actual manuscript, data and declarations before use. Neither passing checks nor polished prose certifies submission readiness.
