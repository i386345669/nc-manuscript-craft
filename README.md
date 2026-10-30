# NC Manuscript Craft

v1.2.1 · [Release notes](RELEASE_NOTES_v1.2.1.md)

[中文说明](README.zh-CN.md) · [Complete writing prompt](FINAL_PROMPT_ZH.md) · [Skill entry](skills/nc-manuscript-craft/SKILL.md)

NC Manuscript Craft is a writing skill for research papers. It helps you develop a central argument, write each section from your study materials, and refine mature drafts while keeping the science and the author's voice intact.

Use it for a complete manuscript, a section that needs clearer interpretation, or revisions that need to stay consistent across the main text, legends and supplementary material. The instructions are in Chinese. Choose the manuscript language in your request.

Start with rough spoken notes, project files and your research ideas. The skill helps clarify the scientific question, choose a concrete research focus and complete the manuscript, legends, supplementary material, references and requested submission files. The goal is a complete, polished manuscript suited to the target journal. For polishing, local edits or restructuring, provide the current text or target passage with the relevant context as the editing baseline.

You may state the scientific question directly or develop it from spoken notes and project materials. Use a constructive, contribution-focused voice throughout the title, abstract, manuscript, legends and submission notes. Explain actual work, findings and meaning, and integrate essential conditions and uncertainty as precise facts. The author’s reasoning and voice guide the full paper.

## Start writing

The GitHub installation command below uses the current main branch. Versioned packages and the standalone prompt are available from the [v1.2.1 release](https://github.com/i386345669/nc-manuscript-craft/releases/tag/v1.2.1).

Ask Codex to install the skill:

```text
$skill-installer
Install https://github.com/i386345669/nc-manuscript-craft/tree/main/skills/nc-manuscript-craft
```

In a new turn, provide your materials and describe the writing task:

```text
Use $nc-manuscript-craft to write an English research manuscript from these results, methods, figures and references.
Develop the central argument and complete the sections supported by the materials.
Keep the study's definitions, results and citations accurate, and list any missing facts separately.
Materials: [files or text]
```

You can also copy [FINAL_PROMPT_ZH.md](FINAL_PROMPT_ZH.md) into your assistant and add your materials. It contains the complete writing instructions in one file.

## What it helps with

- **Build the argument.** Identify the main contribution, decide what each section adds, and connect findings to the research question.
- **Write the paper.** Develop the title, abstract, introduction, results, discussion and methods, with support for legends, supplementary text and submission materials when requested.
- **Refine a mature draft.** Improve unclear claims, repetitive paragraph patterns and awkward transitions while preserving effective passages and author decisions.
- **Keep related text aligned.** Check scientific meaning and citation support across sections, figures, tables and requested translations.

Discussion receives particular attention: what was observed, what it means, how it relates to specific earlier work, and which remaining question matters. Paragraphs can differ in length and emphasis because they have different jobs.

## Examples

For a focused revision:

```text
Use $nc-manuscript-craft to revise this Discussion.
Make the contribution and interpretation clearer, and retain the current results and citations.
Keep paragraphs that already work. Explain the important changes briefly.
```

For a comparison before editing:

```text
Use $nc-manuscript-craft to compare these two drafts.
Identify which passages better explain the findings and which better express the contribution.
Recommend a focused revision that combines their strengths.
```

For bilingual work:

```text
Use $nc-manuscript-craft to synchronize the English and Chinese versions of these revised sections.
Preserve the same scientific objects, conditions, quantities and citation roles in natural prose.
```

## Working with your materials

Provide the current draft or research results, relevant figures and methods, and any author decisions that should guide the work. The skill adapts the argument to the study type and the requested scope. Results, interpretations and proposed work retain their respective evidence status throughout editing.

For longer projects, optional templates help track sources and resume unfinished sections. Requested Word, PDF or other file outputs use the tools available in the host environment. Details are in the [complete workflow](skills/nc-manuscript-craft/references/19-complete-manuscript-workflow.md) and [delivery guide](skills/nc-manuscript-craft/references/12-review-delivery.md).

## Explore the writing guidance

- [Argument and positioning](skills/nc-manuscript-craft/references/01-argument-and-positioning.md)
- [Titles and abstracts](skills/nc-manuscript-craft/references/02-title-abstract.md)
- [Discussion and conclusions](skills/nc-manuscript-craft/references/05-discussion-conclusion.md)
- [Voice and precise expression](skills/nc-manuscript-craft/references/11-voice-precision.md)
- [All section guides](skills/nc-manuscript-craft/references/)

For package maintenance, run `python scripts/validate.py` with Python 3.10 or later. [Evaluation notes](docs/EVALUATION.md) describe the checks and writing tasks used to assess the skill.

## License

Released under the [MIT License](LICENSE). [Third-party notices](THIRD_PARTY_NOTICES.md) document the sources and licenses that informed the project.
