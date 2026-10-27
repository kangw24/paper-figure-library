# VAR · 从逐 token 到逐尺度生成的范式对照

<!-- CATEGORY NAV -->
[Teaser](../README.md) · [Architecture](../../architecture/README.md) · [Element](../../element/README.md) · [总目录](../../CATALOG.md)
<!-- END CATEGORY NAV -->

**NeurIPS 2024 · Oral · 原论文 Figure 2**

![原图预览](preview.png)

## 为什么收这张图

同一张图比较语言自回归、图像逐 token 生成和逐尺度生成，核心差异直接表现为生成顺序与尺度变化。

概念与范式对照 teaser，原论文编号为 Figure 2。

## 可以借鉴

- 保持对照项的视觉语法一致
- 用空间展开表达粗到细过程
- 把新范式分配更大的视觉面积

## 文件与编辑范围

[主文件](source.svg) · [单图 PDF](figure.pdf) · [来源与校验记录](metadata.json)

原 PDF 的几何路径与线条保留，SVG 文字转为轮廓；照片、三维渲染与原有位图部件仍为嵌入图片。

SVG 是原论文图形的提取转换件，未取得作者原生 AI 工程。不同 PDF 阅读器或 Illustrator 对字体、透明度的导入可能有差异。

## 原始出处

- 论文：[Visual Autoregressive Modeling: Scalable Image Generation via Next-Scale Prediction](https://arxiv.org/abs/2404.02905)
- 作者：Tian, Keyu, Jiang, Yi, Yuan, Zehuan, Peng, Bingyue, Wang, Liwei
- [作者项目或代码](https://github.com/FoundationVision/VAR)
- [会议与展示身份依据](https://neurips.cc/virtual/2024/oral/97960)
- PDF 第 2 页，Figure 2；截取坐标见 metadata.json。

## 权利与修改记录

arXiv 原文声明 CC0 1.0；仍保留论文来源和修改记录，第三方素材以其原声明为准。

原文许可声明：https://creativecommons.org/publicdomain/zero/1.0/

只提取、裁剪与转换原图；没有重新绘制。

<!-- BEGIN FIGURE LINKS -->
## 关联范例与元素

同论文的其他图：[VAR · 多尺度 VQVAE 与 VAR 两阶段训练](../../architecture/var-architecture/README.md)

**可搭配的现有元素：** [多尺度特征堆叠](../../element/svg/task5-feature-pyramid.svg) · [多通道彩色张量](../../element/svg/task5-rgb-tensor.svg) · [拼接节点](../../element/svg/task5-concat.svg) · [上采样节点](../../element/svg/task5-upsample.svg) · [水平双向箭头](../../element/svg/tabler-arrows-right-left.svg)

这些元素按表达功能关联，并非从本论文原图拆出；来源和许可仍以各元素记录为准。

[范例与元素对照表](../../element/with-examples.md) · [元素分类目录](../../element/README.md)
<!-- END FIGURE LINKS -->
