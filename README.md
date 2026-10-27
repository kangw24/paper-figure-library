# Paper Figure Library

个人 CS / AI 论文配图素材库，按用途分为 **Teaser、Architecture、Element**。收集作者和已有素材库的源文件，用 Markdown 串联完整范例、方法结构与可复用部件。

**16 个 teaser · 42 个 architecture · 341 个独立 element**。

| 分类 | 用来找什么 | 入口 |
|---|---|---|
| **Teaser** | 问题动机、方法差异、核心想法和能力展示 | [按表达目的浏览](teaser/README.md) |
| **Architecture** | 整体流程、网络主干、训练框架和模块展开 | [按结构用途浏览](architecture/README.md) |
| **Element** | 模块、张量、矩阵、运算、箭头和对象等独立 SVG | [按内容分类浏览](element/README.md) |

根目录直接提供三个素材文件夹：

```text
teaser/        动机、概念与能力展示
architecture/  方法流程、网络与模块结构
element/       独立可复用部件
```

会议、年份、Oral 与奖项保留为条目标签。

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

本轮补充 MVSplat、SAM 2、LLaVA、BLIP-2、pixelSplat、3DETR 的 10 张作者原图，并从 DiT、ViT、SD3 架构图提取 24 个独立网络部件。

元素包括作者公开图元、从论文与 task5 原图提取的部件，以及 Tabler、Bioicons、Isoflow 的已有素材。每项保留独立源文件、来源、许可和预览。

## 来源与编辑范围

原始下载的 SVG、AI、AIT 保留原字节；论文 PDF 提取的 SVG 明确记录原文哈希、页码、裁剪坐标与转换步骤。文字可能已转轮廓，照片和渲染图仍为位图。DPO 对照图和 Genie 训练总览明确标为整图位图参考。

每张图的 README 保留选图理由、使用范围和来源记录。完整机制参考通过 Element 页链接，版式母版通过 Architecture 页链接；它们分别计数，不充作最小元素。许可逐项保留，桌面 Illustrator 尚未逐项实测。

## 维护

[完整图文目录](CATALOG.md) · [来源 JSON 索引](catalog.json) · [收录与分类规则](CONTRIBUTING.md)

新增条目后，在 [relationships.json](relationships.json) 补充表达用途、同论文关联和现有元素关联，再更新目录并检查：

    python scripts/build_catalog.py
    python scripts/validate_library.py

[论文原图收录记录](sources/top-conference-2026-10-27.json) · [元素下载记录](sources/expansion-2026-10-25.json) · [原始收录纠正记录](docs/curation-correction.md)
