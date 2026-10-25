# CLIP Figure 1：训练到零样本预测

![预览](preview.png)

真实论文 Figure 1：左侧为图文对比预训练，右侧依次为用类别文本构建分类器、零样本预测。适合借鉴“一个训练阶段 + 两个使用阶段”的信息层级。

## 可编辑文件

- **主文件：[source.svg](source.svg)**
- [结构化元数据](metadata.json)

配套原始文件与许可：

- [`originals/main-diagrams.pdf`](originals/main-diagrams.pdf)

## 借鉴什么

借鉴左大右小的三阶段布局、输入与表示的对应关系、阶段编号和颜色复用。本文原图归入论文参考范例；为自己的论文重绘时替换模型、文字与样本图，并按实际使用情况保留引用。

## 打开与编辑

在 Illustrator 中使用“文件 → 打开”选择 `source.svg`，按需要取消编组并另存自己的工作副本。SVG 可另外用 Inkscape 打开；AI 预览来自其 PDF 兼容层。

- 文字通过 PDF 转换保留为文字对象，但可能被拆成多个字符或文本块。
- 样本照片仍是嵌入位图；不能当作可编辑矢量图形。
- 字体表现依赖本地字体；尚未在桌面 Illustrator 中打开验证。

## 来源

- https://arxiv.org/abs/2103.00020
- https://arxiv.org/src/2103.00020

原始文件名：`main-diagrams.pdf`。

## 许可与使用范围

**arXiv non-exclusive distribution license**。arXiv 的非独占分发许可不是通用自由复用许可证。本条目作为私人研究与版式参考保存，不能据此推定可以自由再分发或直接复用论文图片。

## 整理时做了什么

- 从作者 arXiv 源包原样提取 main-diagrams.pdf。
- 用 PyMuPDF 导出 SVG，text_as_path=False，以保留文字对象。
- 本条目仅复制、重命名已有 SVG、原始 PDF 和预览。

收录日期：2026-10-25。主文件与所有随附二进制文件的 SHA256 记录在 `metadata.json`。

