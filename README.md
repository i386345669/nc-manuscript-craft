# NC Manuscript Craft

[中文使用说明](README.zh-CN.md) · [Complete standalone writing prompt](FINAL_PROMPT_ZH.md) · [Skill entry](skills/nc-manuscript-craft/SKILL.md)

An evidence-led writing workflow for complete research manuscripts and precise revision of mature drafts. It makes scientific questions, evidence, interpretation and practical contributions readable while preserving author decisions and technical meaning.

The detailed instructions are in Chinese. Manuscript output follows the requested language. The workflow is oriented toward clear Nature Communications-style writing, but is neither affiliated with a journal nor a promise of acceptance.

## Two ways to use it

### Install as a Codex skill

Ask Codex:

```text
$skill-installer
Install the skill from https://github.com/i386345669/nc-manuscript-craft/tree/main/skills/nc-manuscript-craft
```

Then invoke it in a new turn:

```text
Use $nc-manuscript-craft to write a complete English research manuscript from the supplied results, methods, figures and verified references. Continue through all supported sections and final consistency checks. Preserve scientific meaning and identify any genuine evidence gaps.
```

The installable path is `skills/nc-manuscript-craft`, not the repository root. If a skill with the same name is already installed, back it up and explicitly update it rather than silently overwriting. Use a version tag or commit in the GitHub URL when a fixed release is needed. For local installer script users, the equivalent arguments are `--repo i386345669/nc-manuscript-craft --path skills/nc-manuscript-craft --ref main`.

The skill is instruction-only. It requires no API key or separate MCP service. File creation, browsing, rendering and independent agents depend on the host. Without those capabilities it delivers the supported text and accurately reports unavailable checks.

### Copy a single Markdown prompt

Copy [FINAL_PROMPT_ZH.md](FINAL_PROMPT_ZH.md), add the current project materials and specify the requested outputs. It is self-contained and does not require the installed skill, private history or other module files. A text-only assistant can use it to produce manuscript text.

## What it covers

- A full-manuscript mode with material-readiness branches and explicit completion status.
- Argument, title, abstract, introduction, results, discussion and methods.
- Study-specific handling for observational, experimental, prediction, methods, resource, qualitative and evidence-synthesis work.
- Citation support, legends, supplementary text and requested language synchronization.
- Less formulaic prose and fewer semicolons without losing conditions or citation scope.
- Stable evidence IDs, cross-component dependencies and resumable state for large tasks.
- Actual artifact checks, with clear distinctions between complete text, generated files and verified rendering.

It does not invent data, mechanisms, research chronology, citations or declarations. It does not silently run new analyses, upload unpublished work or submit a paper. It does not estimate AI-detector percentages or journal acceptance probabilities.

## Examples

```text
Use $nc-manuscript-craft. Revise only this Discussion for clearer interpretation and specific literature comparison. Keep the current argument, data and citations. Output English only and explain material changes briefly.
```

```text
Use $nc-manuscript-craft. Audit the supplied results, methods and legends for inconsistent populations, denominators, units and citation support. This is a read-only task.
```

```text
Use $nc-manuscript-craft. Resume from the project state file, check which sources changed and update only dependent manuscript components. Do not restart approved sections.
```

## Repository layout

```text
FINAL_PROMPT_ZH.md                 Self-contained copyable prompt
skills/nc-manuscript-craft/
  SKILL.md                        Concise entry and task routing
  agents/openai.yaml              Codex interface metadata
  references/                     Detailed section and workflow instructions
  assets/                         Optional evidence, state and delivery templates
scripts/validate.py               Local structural and public-content checks
tests/                            Synthetic behavioral fixtures and criteria
docs/                             Scope, evaluation and release notes
```

## Validation

Run `python scripts/validate.py` from the repository root with Python 3.10 or later. The check uses only the standard library. It checks local links, manifest fields, prompt synchronization, template structure and obvious private-path or credential patterns. Semantic behavior requires inspecting actual writing outputs. The public fixtures use invented teaching data and must not be treated as real studies.

See [evaluation scope](docs/EVALUATION.md) for what was actually tested. Package checks and selected tasks do not guarantee error-free writing on every project.

## Attribution and license

Original material is released under the [MIT License](LICENSE). See [third-party attribution](THIRD_PARTY_NOTICES.md) for conceptual influences and applicable MIT notices. No upstream ARS or Leey prompt files are bundled. Links to other projects do not license their content under this repository's MIT terms.

Installation guidance was checked against [official skill documentation](https://learn.chatgpt.com/docs/build-skills). This repository is independent of OpenAI and the named journals.
