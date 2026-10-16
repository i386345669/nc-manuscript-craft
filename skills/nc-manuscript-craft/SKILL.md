---
name: nc-manuscript-craft
description: Write complete evidence-led research manuscripts from supplied study materials, or precisely revise mature drafts. Use for full-paper drafting, scientific argument, section writing, citations, legends, supplementary text and requested bilingual synchronization. Preserve scientific meaning and author decisions. Does not silently perform new analyses or predict AI-detector scores or journal acceptance.
metadata:
  version: "1.0.0"
---

# NC Manuscript Craft

从真实研究材料完成论证、写作和交付，也支持成熟稿的定向精修。默认使用清楚、贡献导向的学术表达，少用分号，保护证据与作者声音。名称中的NC说明写作取向，不限制学科，也不承诺某期刊接收。

## 任务与完成约定

先读 [任务与作者决定](references/00-task-and-authority.md)。从当前请求、已有稿件及材料判断目标语言、文章类型、编辑范围和成品。没有明确要求时不要强制双语、投稿信、图件重画或真实修订版。

| 请求 | 应执行的工作 |
|---|---|
| 写完整论文/从材料成稿 | 读取 [完整写作流程](references/19-complete-manuscript-workflow.md)，建立所需交付项，从材料到全部有证据支持的章节。提纲是中间步骤，不作为完成 |
| 建主线/规划框架 | 只完成规划，除非作者同时授权起草 |
| 写某章节 | 读取对应模块并完成该节，核对关联接口 |
| 精修成熟稿 | 以当前基线作最小必要修改，保留有效结构与作者删改 |
| 双语/翻译 | 仅按请求同步语言，核查条件与证据身份 |
| 只读诊断 | 提供可定位问题与建议，不覆盖文件 |
| 文件交付 | 实际生成约定文件并执行可用检查，如实列未验证项 |

完整写作时，按材料决定 `ready_to_write`、`partial_evidence`、`conflicting_sources` 或 `planned_only`。局部缺项只影响依赖部分，继续独立工作。没有完成结果时不编Results，不把预期写成发现。区分内容是否完整、文件是否生成和检查是否完成。

多个任务之间有依赖时连续推进。已授权的起草不强制等待提纲批准，科学含义确需作者决策时提出具体问题并继续其余工作。当前用户指令和科学事实高于本skill默认偏好。

## 始终保留的原则

1. 用一个中心问题组织有主次的贡献，按实际研究类型调整结构。
2. 保护对象、人群、独立单位、测量量、条件、时间、比较、效应尺度、数字、公式、统计家族、技术身份与引文作用。数字相同不等于含义相同。
3. 当前作者决定按范围覆盖旧决定。保留基线，不把作者已删除的修辞换位置恢复，也不无理由重开已确认完成的旧任务。
4. 去反复自辩、审计流水账和空泛拔高，保留改变解释的事实、相反观察、替代解释与方法条件。用准确对象定义表达范围。
5. 成熟稿只改具体问题。保留有作用的研究理由、why-next和we，不以改动比例或工具数量衡量质量。
6. 句段节奏随章节职能变化，术语保持稳定。不虚构预期、失败、意外或前期成果，不故意制造不严谨，不机械添加弱限定。
7. 尽量少用中英文分号。检查英文完整句、逗号拼接、变量大小写、统计归属及联合引文。技术字段和复杂分组可保留必要分隔。
8. 经明确授权可分层显示工程参数，SI保留精确值、单位和定位。统计结果、阈值、区间和公式不随意取整。
9. 文献支持具体命题。近年优先不排除方法、数据和直接先例原文。学习范文的论证动作，不复制事实、经历或结论强度。
10. 图注帮助读图，信息完整但不强制同序。主文与SI执行同样的写作标准，按本次范围同步相关副本。
11. 只报告实际执行过的阅读、检索、独立审查、文件生成和渲染。工具受限时完成可做部分并准确标明状态。
12. 不编造AI检测分数、录用概率或政策认证。声明与实际使用一致。写作不自动授权新增分析、投稿、公开上传或联系他人。

## 按需加载

| 任务 | 模块 |
|---|---|
| 论证、定位、主次 | [01 论证](references/01-argument-and-positioning.md) |
| 标题、摘要 | [02 标题摘要](references/02-title-abstract.md) |
| 问题引导与直接先例 | [03 Introduction](references/03-introduction.md) |
| 发现、设计理由、段落衔接 | [04 Results](references/04-results.md) |
| 解释、具体比较、局限与结尾 | [05 Discussion](references/05-discussion-conclusion.md) |
| 复现、统计与精度 | [06 Methods](references/06-methods-statistics.md) |
| 图证、图注、编辑源与图集 | [07 图件](references/07-figures-legends.md) |
| 补充结果、表注和方法 | [08 SI](references/08-supplementary.md) |
| 按请求中英互译或同步 | [09 双语](references/09-bilingual.md) |
| 从原始研究学习写法 | [10 文献学习](references/10-literature-learning.md) |
| 去防御、节奏、分号 | [11 表达](references/11-voice-precision.md) |
| 审阅、渐进修订、交付核验 | [12 复核交付](references/12-review-delivery.md) |
| 需要简短教学案例 | [13 合成例子](references/13-synthetic-examples.md) |
| 多种编辑工具的职责 | [14 工具协作](references/14-tool-orchestration.md) |
| 公开方法来源和使用边界 | [15 来源](references/15-public-sources.md) |
| 局部、续接等可复制指令 | [16 任务prompt](references/16-prompt-workflows.md) |
| 投稿信和事实声明 | [17 投稿材料](references/17-submission-package.md) |
| 科学支持、题录与编号 | [18 引用](references/18-citations-and-source-use.md) |
| 从材料连续完成全稿 | [19 完整写作](references/19-complete-manuscript-workflow.md) |
| 稳定证据ID、依赖和恢复 | [20 证据状态](references/20-evidence-and-state.md) |
| 不同研究类型的报告重点 | [21 类型适配](references/21-study-types.md) |
| 需要不依赖任何模块的单文件指令 | [22 完整独立prompt](references/22-full-paper-prompt.md) |

仅加载本轮需要的模块，全文任务覆盖所有相关部分。不要让多个工具依次全篇改写。外部技能可用时按实际需要调用，本skill不依赖它们才能执行。

## 状态与交付

复杂全稿任务可使用 [任务卡](assets/task-brief.yaml)、[证据表](assets/evidence-ledger.csv)、[交付表](assets/deliverable-matrix.csv)和[续接状态](assets/project-state.yaml)。简单局部编辑无需搭建这些表。作者有等价记录时直接复用。

论文正文与编辑说明分开。不要将“所提供材料”等来源旁白或未完成检索、渲染、登记号等发表准备事项塞入Results。必要的观察设计、测量身份及科学局限仍准确保留。

逐项检查主张、方法、图表、图注、正文、SI、引用与要求语言的对应。源材料更新时只重新核查其依赖项。原文—改文—理由可使用 [修改记录](assets/change-record.csv)，不强制所有任务输出大表。

最终给出真实成品与简短取舍说明。没有关键结果时交支持范围内的阶段稿，明确缺口，不能冒称可投稿最终稿。需要DOCX/PDF时使用当前工具生成并检查，不能把文本稿叫成已渲染文档。真实tracked接受对应clean、拒绝对应约定基线，公式保持原生结构。没有独立代理时可分轮自检，但准确命名。

按文章类型完成约定组件、关闭必须修复项或明确其影响、无新的实质漂移后停止。不为进一步降低模板感无限改写。
