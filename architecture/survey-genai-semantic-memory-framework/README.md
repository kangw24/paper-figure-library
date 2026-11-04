# GenAI 语义通信 · 语义记忆与物理信道双路框架

<!-- CATEGORY NAV -->
[Teaser](../../teaser/README.md) · [Architecture](../README.md) · [Element](../../element/README.md) · [总目录](../../CATALOG.md)
<!-- END CATEGORY NAV -->

**Architecture · 原论文 Figure 7 · 2405.20024v2**

![作者原图预览](preview.png)

## 内容与构图

发送端先提取共同知识和变化数据，上路通过两端语义记忆共享知识，下路通过 DJSCC 编解码与无线信道重建数据，最后输出预测。

发送端、上下双路信道、接收端三大区域；生成模型的作用用浅蓝模块统一标示。

解释模型内部结构、处理步骤或数据流，按主要表达用途归入 Architecture。

## 与这次四张参考图的关系

沿 [参考图 1 · 无线感知四场景](../../teaser/survey-genai-wireless-four-scenarios/README.md) · [参考图 2 · Speculative RAG](../../architecture/speculative-rag-draft-verify/README.md) 的表达方式继续检索。

可借鉴的组织关系：

- 用上下通路区分共享知识与传输数据。
- 浅色连通背景标出跨模块语义关系。

## 文件与编辑范围

[作者独立 PDF](original.pdf) · [SVG 转换件](source.svg) · [原始插图定义](figure-inclusion.tex) · [来源与校验记录](metadata.json)

作者独立 PDF 含 54 个绘图对象、26 个文本片段和 5 个嵌入位图对象；保留原有矢量、文字或轮廓。SVG 是 PDF 转换件，文字转轮廓，嵌入图片保持。位图对象数不代表子图数。

PDF 的框线、箭头和原有文字对象或轮廓可按实际对象修改；照片和部分图标仍为位图。桌面 Illustrator 尚未逐项实测。

## 原始出处

- 论文：[Applications of Generative AI (GAI) for Mobile and Wireless Networking: A Survey](https://arxiv.org/abs/2405.20024v2)
- 作者：Vu, Thai-Hoc；Jagatheesaperumal, Senthil Kumar；Nguyen, Minh-Duong；Van Huynh, Nguyen；Kim, Sunghwan；Pham, Quoc-Viet
- [作者项目或仓库](https://arxiv.org/abs/2405.20024v2)
- 所收录版本：`2405.20024v2`，原文 PDF 第 13 页，Figure 7。
- [固定版本 TeX 源码归档](https://arxiv.org/src/2405.20024v2)；原件路径 `Photo/FigureGAIApplication.pdf`。

## 权利与转换记录

所收录 arXiv 版本采用非独占分发许可，该许可不等同第三方重用授权。本条用于私有参考，保留署名与来源；图中第三方插图和照片按原始权利核对。

[原版本许可](https://arxiv.org/licenses/nonexclusive-distrib/1.0/) · [权利记录](RIGHTS.source.txt)

原始文件按原字节保存，转换件另存。

<!-- BEGIN FIGURE LINKS -->
## 关联范例与元素

同论文的其他图：[GenAI × IoT · 分层技术栈与多场景应用](../../teaser/survey-genai-iot-layers-scenes/README.md) · [GenAI 综述 · 演进、生成模型与代表方法拼图](../../teaser/survey-genai-history-model-mosaic/README.md) · [GenAI 网络管理 · 控制面、数据面与切片场景](../../teaser/survey-genai-network-management-scenes/README.md) · [GenAI 无线安全 · 四场景与局部机制并列](../../teaser/survey-genai-wireless-security-four-panels/README.md)

**可搭配的现有元素：** [数据库](../../element/svg/tabler-database.svg) · [编码器块](../../element/svg/rust-encoder.svg) · [解码器块](../../element/svg/rust-decoder.svg) · [分流箭头](../../element/svg/tabler-arrows-split.svg)

这些元素按表达功能关联，并非从本论文原图拆出；来源和许可仍以各元素记录为准。

[范例与元素对照表](../../element/with-examples.md) · [元素分类目录](../../element/README.md)
<!-- END FIGURE LINKS -->
