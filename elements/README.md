# 最小可复用元素库

首批 **24 个独立 SVG 元素**，用于快速搭建 teaser、模型架构和方法流程。每个元素保留普通矢量形状与可编辑文字，使用统一的蓝、绿、橙配色。

![24 个元素总览](preview.png)

- [打开可编辑总览 all-elements.svg](all-elements.svg)：在一张画布上选取所需元素。
- [浏览独立 SVG 文件](svg/)：每个文件仅包含一个元素，画布均为 `240 × 160`。
- [查看机器可读目录](catalog.json)：包括名称、标签、文件路径、来源和编辑说明。
- [查看样式参数](style-tokens.json)：颜色、字体、线宽、画布和圆角。

## 按内容选取

| 类别 | 元素 | 常见用途 |
|---|---|---|
| 模块 | [通用模块](svg/module-block.svg)、[编码器](svg/encoder.svg)、[解码器](svg/decoder.svg)、[MLP](svg/mlp.svg)、[注意力](svg/attention.svg) | 组成模型结构或计算流程 |
| 数据 | [特征张量](svg/tensor-stack.svg)、[矩阵](svg/matrix.svg)、[Token 序列](svg/token-sequence.svg)、[图像占位块](svg/image-tile.svg)、[隐变量向量](svg/latent-vector.svg)、[样本点云](svg/sample-cloud.svg) | 表示输入、特征、中间表示和输出分布 |
| 运算 | [加法节点](svg/sum-node.svg)、[拼接节点](svg/concat-node.svg)、[损失函数](svg/loss.svg) | 表示残差、特征融合和训练目标 |
| 连接 | [实线箭头](svg/arrow-solid.svg)、[虚线箭头](svg/arrow-dashed.svg)、[双向箭头](svg/arrow-bidirectional.svg)、[跳跃连接](svg/skip-connection.svg) | 表示数据流、辅助路径、交互和旁路 |
| 训练 | [冻结参数](svg/frozen-badge.svg)、[可训练参数](svg/trainable-badge.svg)、[参数共享](svg/shared-weights.svg) | 表示微调范围、更新状态和共享参数 |
| 科学与动力学 | [时间推进](svg/time-rollout.svg)、[物理约束](svg/physics-constraint.svg)、[分布映射](svg/distribution-map.svg) | AI4PDE、动力系统、生成模型的概念示意 |

## 在 Illustrator 中使用

1. 打开一个独立 SVG，或打开 `all-elements.svg` 后选择目标元素组。
2. 复制到论文图稿，按需要取消编组、调整模块宽度和连接路径。
3. 直接编辑文字、填充与描边。箭头尖端为独立多边形；拉长箭头时，分别移动尖端和线段末端可避免箭头头部被拉伸。
4. 替换图像占位块、Token 名称、张量维度、函数名称及示意数据，使其与论文方法一致。

独立元素的背景透明，总览背景为白色。文字使用 `Arial, Helvetica, sans-serif`；本机字体替换可能改变字宽。文件采用简单路径、矩形、圆和文本，不包含外部图片、脚本、复杂滤镜或 SVG `<use>` 引用。

点云、隐变量数值和分布轮廓是绘图占位示意，不代表实验结果；注意力元素中的 `Attn(Q, K, V)` 是函数标签，请根据实际方法改写。

## 维护与重新生成

在仓库根目录执行：

```bash
python scripts/generate_elements.py
```

生成 SVG、JSON 目录和样式参数只依赖 Python 标准库。如果已安装 Inkscape，可同时生成 PNG 总览：

```bash
python scripts/generate_elements.py --render
```

生成器会检查 XML 格式、`viewBox`、脚本与外部引用。初始版本已用 Inkscape 渲染并检查总览；尚未在 Illustrator 桌面版逐项验证。

**生成命令会覆盖本目录内同名生成文件。** 长期修改建议同步到生成器；临时改稿可先把所需元素复制到自己的项目目录。

新增元素时，保持独立 SVG 自包含，并补充 `catalog.json` 中的分类、标签、来源与编辑说明。当前目录由生成器维护：应在 `create_items()` 中登记新元素，再运行上述命令更新目录。

## 来源与使用状态

这些元素于 2026-10-25 为本仓库原创绘制，没有从第三方论文图中描摹或拆取。它们用于仓库所有者的个人科研绘图与修改复用，当前未设置对外再分发的开源许可。此说明仅适用于本目录的原创元素，不改变仓库其他范例各自的许可和署名要求。
