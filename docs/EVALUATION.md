# Evaluation

## v1.2.1

The later generalization review extends the oral-notes-to-full-manuscript entry, applies positive narrative throughout, and replaces project-shaped technical instructions with cross-disciplinary writing guidance. Earlier evaluation records below keep their original snapshot identity.

### Oral-notes drafting and final revision check

After this review, a fresh independent agent used the revised skill with [spoken notes and a project fact file](../tests/scenarios/09-oral-notes-to-paper.md) from a fictional materials experiment. It produced a complete English teaching manuscript with all requested sections, the supplied reference, two figure legends and Supplementary Methods. It did not require an existing manuscript before drafting. The agent then performed a targeted editorial pass on that draft in the same context, retaining the first output and saving the revision separately.

The maintainer read both outputs against the fixture. The final revision kept the specimen/observation distinction, endpoint counts, given means and difference, missing observations, exposure settings and reference identity. Discussion was reorganized around the observed contrast and specific follow-up questions, while Methods retained the relevant design facts. No new data analysis, browsing or graphics were performed. This is one independent drafting check followed by a same-context revision, not independent replication of a research result.

The behavioral runs below preceded the author’s later wording and scope edits on 30 October. Those edits generalized the scientific-question entry point and withdrew the project-specific workflow-contribution guidance. The revised files received targeted author-scope review and structural checks; the earlier runs are retained as results of their recorded snapshot.

On 30 October 2026, a separate evaluation agent in a fresh context completed three synthetic requests using the candidate skill: the existing complete-paper fixture and the two new resource-narrative and explanation-figure fixtures. The agent received the skill, supplied materials and output paths, without expected answers or the private development history. The three tasks were performed sequentially in that one independent context. The maintainer read all completed outputs against the supplied evidence.

| Scenario | Observed outcome |
|---|---|
| [Complete paper](../tests/scenarios/01-complete-paper.md) | Produced the requested complete English teaching manuscript, both legends, Supplementary Methods and the supplied software reference. Preserved station versus observation units, missing records and descriptive means without inventing inference or deployment. |
| [Resource narrative](../tests/scenarios/07-resource-narrative.md) | Produced the title, 112-word abstract, resource paragraph and requested four-paragraph Discussion. Preserved the useful assay interpretation and less favorable comparator. Reported the indexed-to-original timing ratio without treating it as a speedup. |
| Explanation figures, historical synthetic snapshot | Produced a reasoned figure plan, Results and legend while preserving the provided measurement identities and interpretation scope. Detailed fixture and output hashes are retained in the private evaluation record. The current [general figure-role fixture](../tests/scenarios/08-explanation-figure-choice.md) replaces that technical scenario and has not been presented as the one used in the earlier run. |

These are three small text tasks, not three independent replications or a numerical estimate of writing quality. They did not test publication-length work, new scientific analysis, graphics or Word rendering. All completed outputs and their hashes are retained in the private local evaluation record. Structural CI results are tracked separately in GitHub Actions. Historical behavioral results below remain results of their stated versions.

Version 1.1.0 was evaluated on 20 October 2026 with four writing scenarios and five independent executions. Each agent received the specified synthetic material and either the installable skill or the standalone prompt in a fresh context. Agents were not given expected answers, previous outputs or the private development history. The maintainer read the completed outputs against the supplied evidence.

## v1.1.0 writing tasks

| Scenario | Execution | Observed outcome |
|---|---|---|
| [Complete paper](../tests/scenarios/01-complete-paper.md) | Standalone prompt only | Produced the full English teaching manuscript, both legends, Supplementary Methods and the supplied software reference. Preserved the four spatial units, repeated observations, missing records, means and descriptive difference. Kept unresolved publication items in a separate note. |
| [Review against source](../tests/scenarios/04-review-against-source.md) | Skill, then standalone prompt in a separate context | Both runs retained the correct source title and left rendering unverified. They explained ddof through its variance divisor, corrected the selection description and retained the paired interval. Intervals were assigned to the statistical panel and F1 identified from the plotted field. The selected records and two panel populations remained distinct. |
| [Methods and SI consolidation](../tests/scenarios/05-methods-and-si-consolidation.md) | Skill and relevant modules | Recovered the executed weighted-error objective, lower-threshold tie rule, threshold and probability medians, and inclusive classification boundary. Preserved eligibility, exclusion timing and evaluation after aggregation while consolidating the duplicate sections. |
| [Resource Discussion and delivery](../tests/scenarios/06-resource-discussion-and-delivery.md) | Skill and relevant modules | Wrote a 352-word Discussion linking observations to resource use and interpretation. Retained comparison uncertainty and coverage loss. Followed the fictional journal's required separate graphical abstract, selected individual main figures and identified the combined SI as still needing assembly. |

The complete-paper output contains 1,199 whitespace-delimited tokens after removing Markdown heading markers, including headings and notes. Its abstract contains 129 words. The manuscript fulfilled the requested content scope. Some repeated scope statements remain candidates for ordinary author editing. The run demonstrates complete drafting and scientific preservation while leaving sentence-level editorial judgment to the author.

All four scenarios completed on their first execution. Independent package review then found an ambiguous instruction that could suggest using the same denominator across different populations. The instruction was clarified to preserve each population's actual denominator. A fresh standalone-only execution of the review scenario retained the 24 selected records, 140 eligible participants and 90 held-out records separately. All completed outputs were preserved for inspection. No task reran scientific models or supplied invented performance statistics. The file-selection task used inventory descriptions and reported that actual files had not been inspected or generated.

## v1.0.0 baseline

The initial release was evaluated on 16 October 2026 using three synthetic scenarios and four independent executions.

| Scenario | Observed outcome |
|---|---|
| [Complete paper](../tests/scenarios/01-complete-paper.md), two executions | Both produced all requested sections. The first included unnecessary source-material narration and publication-preparation gaps inside Results. A focused clarification separated manuscript prose from author notes, and a new standalone-only execution improved that separation while retaining the study definitions and numbers. |
| [Missing results](../tests/scenarios/02-missing-results.md) | Produced a prospective, incomplete draft with specific evidence queries. The expected effect was not converted into an observed finding. |
| [Resume after source update](../tests/scenarios/03-resume-source-update.md) | Updated the four dependent components and retained protected Introduction/Methods passages, other counts and citation identity. Recorded the revised source and continuation state. |

The missing-results and source-update scenarios were not rerun for v1.1.0. Across both releases, the record contains six distinct scenarios and nine independent executions.

## Package and distribution checks

`python scripts/validate.py` checks required files, metadata, release-version agreement, module routes, local links, prompt-copy synchronization, installable license copies, CSV structure and common private-information patterns. For v1.1.0, the validator passed on the reviewed package and correctly rejected temporary copies with mismatched release versions or unsynchronized prompts. The official skill-creator format validator also passed.

Public-content review examines the instructions and examples separately from these mechanical checks. GitHub Actions reruns the structural validator on pushes and pull requests. Release verification installs the committed skill subtree using the official installer and compares file hashes with the release source.

## Coverage

The scenarios exercise text drafting, editorial decisions, method recovery, consolidation and file-purpose mapping using supplied material. They do not exercise Word rendering, tracked changes, SVG editing, live literature retrieval or journal submission. The small teaching manuscript also does not test a publication-length project. The supplied software reference was verified when its fixture was prepared, not through a literature search by the evaluation agent.

Synthetic fixtures are public so these tasks can be repeated. Private study materials and raw evaluation workspaces remain outside the repository. Review outcomes for a new manuscript depend on its actual evidence, author decisions and requested work.
