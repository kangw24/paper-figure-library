# Paper Figure Library

个人 CS / AI 论文配图素材库，按用途分为 **Teaser、Architecture、Element**。收集作者和已有素材库的源文件，用 Markdown 串联完整范例、方法结构与可复用部件。

**76 个 teaser · 56 个 architecture · 341 个独立 element**。

| 分类 | 用来找什么 | 入口 |
|---|---|---|
| **Teaser** | 问题动机、核心想法、能力展示、领域全景与演进 | [按表达目的浏览](teaser/README.md) |
| **Architecture** | 整体流程、网络主干、训练框架和模块展开 | [按结构用途浏览](architecture/README.md) |
| **Element** | 模块、张量、矩阵、运算、箭头和对象等独立 SVG | [按内容分类浏览](element/README.md) |

根目录直接提供三个素材文件夹：

```text
teaser/        动机、概念、能力展示与领域全景
architecture/  方法流程、网络与模块结构
element/       独立可复用部件
```

会议、期刊、年份、综述类型、Oral 与奖项保留为条目标签。

AI4PDE 综述图：[Fig.1：领域定位、方法与应用全景](teaser/survey-ai-pde-scope-map/README.md) · [Fig.2：物理／数据条件下的方法对照](teaser/survey-ai-pde-physics-data-paradigms/README.md)。两项均保留作者原始 PDF 和 SVG 转换件。

相近的概念总览与方法对照：[PDE 物理—数据连续谱](teaser/survey-pde-physics-data-continuum/README.md)、[物理知识的五种融入方式](teaser/survey-physics-knowledge-five-paradigms/README.md)、[知识来源—表示—融入位置](teaser/survey-informed-ml-knowledge-map/README.md)、[数据与先验知识双路径](teaser/survey-informed-ml-information-flow/README.md)、[PIML 三维分类全景](teaser/survey-piml-three-axis-landscape/README.md)。

其他相近构图：[机器人学习的三路先验对照](teaser/survey-robot-physics-three-routes/README.md)、[六类方法面板](teaser/survey-robot-physics-six-families/README.md)、[数据—模型—优化流程](teaser/survey-piml-data-model-optimization/README.md)、[PBDL 领域位置与方法空间](teaser/pbdl-field-method-space/README.md)。前两项提供矢量结构，后两项为作者／出版商原始位图参考。

本次补充：[六面板神经方法总览](teaser/survey-biomedical-six-methods/README.md)提供作者独立 PDF 与 SVG；[导数—方程—残差](teaser/survey-piml-equations-residuals/README.md)、[优化过程的多子图全景](teaser/survey-piml-optimization-landscape/README.md)和[物理—学习四范式对照](teaser/survey-dynamics-physics-learning-spectrum/README.md)保留作者原始 PNG／JPEG，作为构图参考。

综述与综合报告的概念图、领域地图和发展脉络从 [全景目录](teaser/README.md#landscape) 浏览。优先看 [AI4Science 领域圆环](teaser/survey-ai4science-domain-wheel/README.md)、[3D／4D 世界模型全景](teaser/survey-3d4d-world-overview/README.md)、[3D 表示与生成范式](teaser/survey-3d-representation-generators/README.md)，以及 [世界模型能力递进](teaser/survey-world-model-capability-ladder/README.md)。范式对照还可看 [图基础模型](teaser/survey-graph-foundation-paradigm/README.md)。

多子图综述优先看 [主题与应用总览](teaser/README.md#multi-panel)：[21 种图像编辑任务](teaser/survey-instruction-editing-task-gallery/README.md)、[神经场的 5 类技术＋6 类应用](teaser/survey-neural-fields-multipanel/README.md)，以及 [Neural Rendering 场景拼图](teaser/survey-neural-rendering-2020-gallery/README.md)。前两项保留作者独立 PDF 并提供 SVG；神经渲染拼图原件为整张 JPEG。

可编辑的多区综述图还包括：[五类科研活动总览](teaser/survey-ai4research-five-activities/README.md)、[七类学科应用](teaser/survey-ai4research-seven-domains/README.md)、[科学数据构建全景](teaser/survey-scillm-data-construction/README.md)、[十二场景仿真时间线](teaser/survey-diffsim-twelve-scenes/README.md)。均提供作者独立 PDF 和 SVG 转换件，原有位图保留其属性。

## 沿着范例找素材

1. 在 [Teaser](teaser/README.md) 找表达思路，例如 VAR 的范式对照、Genie 的交互概念、DreamGaussian 的优化过程。
2. 从条目中的“同论文的其他图”进入 [Architecture](architecture/README.md)，看信息流、主干和局部模块。
3. 沿“关联范例与元素”选择 [Element](element/README.md)，或打开 [范例与元素对照表](element/with-examples.md) 对照查找。元素分类页也能反查关联范例。

例如：[VAR teaser](teaser/var-paradigm/README.md) → [VAR architecture](architecture/var-architecture/README.md) → [多尺度特征堆叠](element/svg/task5-feature-pyramid.svg)。最后一个是库中功能相近的现有元素，来源是 task5 教程。

[LightGlue architecture](architecture/lightglue/README.md) 则直接链接到从该原图拆出的 [注意力块](element/svg/lightglue-self-attention.svg)、[匹配矩阵](element/svg/lightglue-assignment-matrix.svg) 等部件。两种关联在页面里分别说明。

## Element 快速入口

| 内容 | 入口 |
|---|---|
| 网络、张量、特征图与模块 | [网络与模块](element/by-category/modules.md) · [数据与文档](element/by-category/data.md) |
| 箭头、分支、汇合和弯曲连接 | [箭头与连接](element/by-category/connections.md) |
| 运算、冻结与训练标记 | [运算与变换](element/by-category/operations.md) · [训练与标记](element/by-category/training.md) |
| 相机、GPU、服务器与设备 | [设备与对象](element/by-category/devices.md) |
| 范例到元素、元素到范例 | [Markdown 对照表](element/with-examples.md) |
| 离线搜索 | 下载仓库后打开 [gallery.html](element/gallery.html) |

已收录 MVSplat、SAM 2、LLaVA、BLIP-2、pixelSplat、3DETR 的 10 张作者原图，并从 DiT、ViT、SD3 架构图提取 24 个独立网络部件。

元素包括作者公开图元、从论文与 task5 原图提取的部件，以及 Tabler、Bioicons、Isoflow 的已有素材。每项保留独立源文件、来源、许可和预览。

## 来源与编辑范围

原始下载的 SVG、AI、AIT 保留原字节；综述条目优先保留作者 TeX 归档中的独立 PDF 原件及插图定义，记录固定版本、归档哈希与成员路径。PDF 中的原文本对象保留，附带 SVG 的文字转为轮廓。3DGS 母图的章节与引文编号由原论文 LaTeX 叠加，独立文件保留作者的编号空槽。CRFM 报告同时保留论文实际嵌入的 PNG 与作者归档中的矢量配套 PDF，注明版本对应关系。

从整篇论文 PDF 摘取的 SVG 另记录原文哈希、页码、裁剪坐标与转换步骤。照片和渲染图仍为位图。DPO 对照图和 Genie 训练总览明确标为整图位图参考。

每张图的 README 保留选图理由、使用范围和来源记录。完整机制参考通过 Element 页链接，版式母版通过 Architecture 页链接；它们分别计数，不充作最小元素。许可逐项保留，桌面 Illustrator 尚未逐项实测。

## 科研制图 Skill

[scientific-figure-workflow](skills/scientific-figure-workflow/SKILL.md) 总结了本项目从选参考、科学机制复审、紧凑排版、配色与 TeX，到 Illustrator 原生交付和汇报 PPT 的完整流程。附七份详细参考、图形简报与修订记录模板、只读 SVG 结构预检工具。区分通用原则、个人偏好与本次 AI4PDE 案例，不改变素材库收录规则。

## 维护

[完整图文目录](CATALOG.md) · [来源 JSON 索引](catalog.json) · [收录与分类规则](CONTRIBUTING.md)

新增条目后，在 [relationships.json](relationships.json) 补充表达用途、同论文关联和现有元素关联，再更新目录并检查：

    python scripts/build_catalog.py
    python scripts/validate_library.py

[可编辑综述图收录记录](sources/survey-editable-2026-10-28.json) · [方法面板与优化图收录记录](sources/physics-overviews-3-2026-10-28.json) · [后续物理学习图收录记录](sources/physics-overviews-2-2026-10-27.json) · [物理与知识融合图收录记录](sources/physics-overviews-2026-10-27.json) · [AI4PDE 图收录记录](sources/ai-pde-review-2026-10-27.json) · [多子图综述收录记录](sources/survey-panels-2026-10-27.json) · [综述原图收录记录](sources/survey-figures-2026-10-27.json) · [领域全景扩充记录](sources/survey-rich-2026-10-27.json) · [论文原图收录记录](sources/top-conference-2026-10-27.json) · [元素下载记录](sources/expansion-2026-10-25.json) · [原始收录纠正记录](docs/curation-correction.md)
