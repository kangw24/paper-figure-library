# LGM · 非对称 U-Net 与跨视角注意力

<!-- CATEGORY NAV -->
[Teaser](../../teasers/README.md) · [Architecture](../README.md) · [Element](../../../elements/README.md) · [总目录](../../../CATALOG.md)
<!-- END CATEGORY NAV -->

**ECCV 2024 · Oral · 原论文 Figure 3**

![原图预览](preview.png)

## 为什么收这张图

把多视图输入、相机射线编码、U-Net、三维融合和监督闭环放在一张图里；顶部局部放大说明跨视角交互。

网络内部结构与训练监督主图。

## 可以借鉴

- 层级条块表达 U-Net 深度与分辨率变化
- 局部放大解释创新模块
- 用虚线闭环连接新视角监督

## 文件与编辑范围

[主文件](source.svg) · [单图 PDF](figure.pdf) · [来源与校验记录](metadata.json)

原 PDF 的几何路径与线条保留，SVG 文字转为轮廓；照片、三维渲染与原有位图部件仍为嵌入图片。

SVG 是原论文图形的提取转换件，未取得作者原生 AI 工程。不同 PDF 阅读器或 Illustrator 对字体、透明度的导入可能有差异。

## 原始出处

- 论文：[LGM: Large Multi-View Gaussian Model for High-Resolution 3D Content Creation](https://arxiv.org/abs/2402.05054)
- 作者：Tang, Jiaxiang, Chen, Zhaoxi, Chen, Xiaokang, Wang, Tengfei, Zeng, Gang, Liu, Ziwei
- [作者项目或代码](https://me.kiui.moe/lgm/)
- [会议与展示身份依据](https://me.kiui.moe/lgm/)
- PDF 第 6 页，Figure 3；截取坐标见 metadata.json。

## 权利与修改记录

arXiv 标注的是授予 arXiv 的非独占分发许可，不是第三方图形重用许可。本条用于个人私有参考，改编或公开再用需核对原权利。

原文许可声明：https://arxiv.org/licenses/nonexclusive-distrib/1.0/

只提取、裁剪与转换原图；没有重新绘制。

<!-- BEGIN FIGURE LINKS -->
## 关联范例与元素

同论文的其他图：[LGM · 从文本或图像到三维高斯和网格的流程](../lgm-pipeline/README.md)

**可搭配的现有元素：** [多尺度特征堆叠](../../../elements/svg/task5-feature-pyramid.svg) · [多通道彩色张量](../../../elements/svg/task5-rgb-tensor.svg) · [拼接节点](../../../elements/svg/task5-concat.svg) · [上采样节点](../../../elements/svg/task5-upsample.svg) · [Self attention 块](../../../elements/svg/lightglue-self-attention.svg) · [相机](../../../elements/svg/tabler-camera.svg)

这些元素按表达功能关联，并非从本论文原图拆出；来源和许可仍以各元素记录为准。

[范例与元素对照表](../../../elements/with-examples.md) · [元素分类目录](../../../elements/README.md)
<!-- END FIGURE LINKS -->
