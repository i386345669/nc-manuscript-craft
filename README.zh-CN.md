# NC Manuscript Craft

v1.2.1 · [更新说明](RELEASE_NOTES_v1.2.1.md)

[English](README.md) · [完整写作 Prompt](FINAL_PROMPT_ZH.md) · [技能入口](skills/nc-manuscript-craft/SKILL.md)

这是一套用于科研论文写作的技能，帮助你把研究材料组织成清楚的中心论证，完成各个章节，并对成熟稿做有针对性的修订。写作围绕研究实际发现、读者需要理解的问题，以及作者希望保留的判断展开。

可以用它从材料起草全稿，修改一段解释不够充分的 Discussion，或同步正文、图注和补充材料中的相关变化。详细指令使用中文，稿件语言由你的任务要求决定。

你可以从口述稿、完整项目文件和自己的逻辑框架开始。技能会协助梳理科学问题、选择具体研究切入点，持续完成正文、图注、补充材料、引用和约定的投稿文件，以目标期刊要求的完整成熟论文为交付目标。润色、局部修改或重构时，使用当前正文或目标段落及必要上下文作为编辑基线，按本轮范围处理。

科学问题可以由你直接提出，也可以从口述与项目材料中共同提炼。全程采用正向性叙述，以实际研究、发现和意义推进标题、摘要、正文、图注和投稿说明。研究条件与不确定性通过准确事实表达，作者的判断与自然的行文贯穿全稿。

## 开始使用

下面的 GitHub 安装命令使用主分支中的当前版本。也可从 [v1.2.1 Release](https://github.com/i386345669/nc-manuscript-craft/releases/tag/v1.2.1) 获取版本包和独立 Prompt。

在 Codex 中发送：

```text
$skill-installer
请安装 https://github.com/i386345669/nc-manuscript-craft/tree/main/skills/nc-manuscript-craft
```

安装后，在新一轮对话中附上材料并说明写作任务：

```text
请使用 $nc-manuscript-craft，根据这些结果、方法、图表和参考资料完成英文论文。
确定中心论证，完成材料所支持的各个章节。
准确保留研究定义、结果与引文，将需要补充的事实单独列出。
材料：【文件或正文】
```

也可以将 [FINAL_PROMPT_ZH.md](FINAL_PROMPT_ZH.md) 整体复制给助手，再附上研究材料。这个文件包含完整的写作指令。

## 它能帮助你做什么

- **建立论证。** 找出主要贡献，明确各节增加了什么认识，将发现与研究问题连接起来。
- **完成论文。** 撰写标题、摘要、引言、结果、讨论和方法，并按需处理图注、补充材料与投稿材料。
- **精修成熟稿。** 改善含混的主张、重复的段落结构和不自然的衔接，保留已经有效的文字与作者决定。
- **同步相关内容。** 核对章节、图表及所需译文之间的科学含义和引文支持关系。

Discussion 的重点是解释实际观察到了什么、这些发现意味着什么，以及它们与具体研究怎样相接。有必要继续区分解释时，再提出相应的研究问题。段落的长短与详略随内容变化。

## 常用任务

定向精修：

```text
请使用 $nc-manuscript-craft 修改这段 Discussion。
把贡献和结果解释写得更清楚，保留现有结果与引用。
已经有效的段落保持原文，并简要说明重要修改。
```

比较两个版本：

```text
请使用 $nc-manuscript-craft 比较这两个版本。
判断哪些段落更好地解释了发现，哪些更清楚地表达了贡献。
提出结合两版长处的局部修订方案。
```

双语同步：

```text
请使用 $nc-manuscript-craft 同步这些修订段落的中英文版本。
用自然的表达保留同一研究对象、条件、数量和引用作用。
```

## 准备哪些材料

提供当前稿件或已完成结果、相关图表和方法，以及需要保留的作者判断。技能会根据研究类型与本轮范围组织写作，持续区分研究结果、结果解释与未来计划的证据身份。

长篇任务可以使用配套模板记录来源和未完成章节，便于接续工作。需要 Word、PDF 等文件时，调用所在环境提供的工具生成和检查。详细流程见[完整写作](skills/nc-manuscript-craft/references/19-complete-manuscript-workflow.md)与[交付指南](skills/nc-manuscript-craft/references/12-review-delivery.md)。

## 按需深入

- [论证主线与定位](skills/nc-manuscript-craft/references/01-argument-and-positioning.md)
- [标题与摘要](skills/nc-manuscript-craft/references/02-title-abstract.md)
- [Discussion 与结尾](skills/nc-manuscript-craft/references/05-discussion-conclusion.md)
- [作者声音与精确表达](skills/nc-manuscript-craft/references/11-voice-precision.md)
- [全部章节指南](skills/nc-manuscript-craft/references/)

维护技能时，可使用 Python 3.10 或以上版本运行 `python scripts/validate.py`。[测试说明](docs/EVALUATION.md)记录具体检查范围及用于评估技能的写作任务。

## 许可

本仓库采用 [MIT 许可](LICENSE)。项目参考来源及相关许可见[第三方说明](THIRD_PARTY_NOTICES.md)。
