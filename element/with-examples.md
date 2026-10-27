# 范例与元素对照

[Teaser](../teaser/README.md) · [Architecture](../architecture/README.md) · [Element](README.md) · [总目录](../CATALOG.md)

由 teaser 看表达思路，由 architecture 看信息流，再沿下列链接选元素。只有来源记录指向该原图的条目，才标作原图拆件。

## 从原图拆出的部件

| 原图 | 已有独立元素 |
|---|---|
| [DiT · 整体主干与三种条件注入模块](../architecture/dit-architecture/README.md) | [Patchify 图像分块模块](svg/dit-patchify.svg) · [条件嵌入模块](svg/dit-embed.svg) · [DiT block 模块](svg/dit-block.svg) · [线性映射与形状重排](svg/dit-linear-reshape.svg) · [LayerNorm 模块](svg/dit-layer-norm.svg) · [带噪潜变量块](svg/dit-noised-latent.svg) · [时间步条件块](svg/dit-timestep.svg) · [类别条件块](svg/dit-class-condition.svg) · [DiT 多头自注意力模块](svg/dit-self-attention.svg) · [逐位置前馈网络模块](svg/dit-feed-forward.svg) · [条件缩放与平移模块](svg/dit-scale-shift.svg) · [DiT 残差加法节点](svg/dit-residual-add.svg) |
| [LightGlue：注意力、动态剪枝与匹配](../architecture/lightglue/README.md) | [Self attention 块](svg/lightglue-self-attention.svg) · [匹配相似度矩阵](svg/lightglue-assignment-matrix.svg) · [残差加法节点](svg/lightglue-residual-add.svg) · [蓝色流程箭头](svg/lightglue-flow-arrow.svg) |
| [多尺度网络总览与模块展开](../architecture/multiscale-network/README.md) | [输入特征层](svg/task5-input-feature.svg) · [多尺度特征堆叠](svg/task5-feature-pyramid.svg) · [多通道彩色张量](svg/task5-rgb-tensor.svg) · [输出特征层](svg/task5-output-feature.svg) · [拼接节点](svg/task5-concat.svg) · [加法节点](svg/task5-add.svg) · [乘法节点](svg/task5-multiply.svg) · [上采样节点](svg/task5-upsample.svg) · [CBR 模块](svg/task5-cbr.svg) · [GAP 模块](svg/task5-gap.svg) · [FC + ReLU 模块](svg/task5-fc-relu.svg) |
| [RUST：编码器、场景表示与位姿分支](../architecture/rust/README.md) | [编码器块](svg/rust-encoder.svg) · [解码器块](svg/rust-decoder.svg) · [特征表示堆叠](svg/rust-feature-stack.svg) · [单层特征块](svg/rust-feature-tile.svg) · [位姿估计模块](svg/rust-pose-estimator.svg) · [右向流程箭头](svg/rust-arrow-right.svg) · [下向流程箭头](svg/rust-arrow-down.svg) |
| [SD3 · 双模态主干与 MM-DiT block 展开](../architecture/sd3-mmdit-architecture/README.md) | [MM-DiT block 模块](svg/sd3-mmdit-block.svg) · [条件 MLP 模块](svg/sd3-conditioning-mlp.svg) · [图像潜变量分块模块](svg/sd3-patching.svg) · [条件调制模块](svg/sd3-modulation.svg) |
| [ViT 原论文 · 图像分块、token 序列与编码器展开](../architecture/vit-original-architecture/README.md) | [ViT 分类 MLP 头](svg/vit-mlp-head.svg) · [ViT 编码器块](svg/vit-encoder-block.svg) · [类别输出列表](svg/vit-class-output.svg) · [图像块线性投影模块](svg/vit-patch-projection.svg) · [ViT 多头注意力模块](svg/vit-self-attention.svg) · [ViT 归一化模块](svg/vit-norm.svg) · [ViT 前馈 MLP 模块](svg/vit-mlp.svg) · [图像块嵌入模块](svg/vit-embedded-patches.svg) |

## 按范例找可搭配元素

本节是表达功能的对应关系，**不表示元素出自所列论文**。各元素保留自己的作者和许可。

### Teaser

| 范例 | 现有元素 |
|---|---|
| [VAR · 从逐 token 到逐尺度生成的范式对照](../teaser/var-paradigm/README.md) | [多尺度特征堆叠](svg/task5-feature-pyramid.svg) · [多通道彩色张量](svg/task5-rgb-tensor.svg) · [拼接节点](svg/task5-concat.svg) · [上采样节点](svg/task5-upsample.svg) · [水平双向箭头](svg/tabler-arrows-right-left.svg) |
| [DPO · RLHF 与直接偏好优化的流程简化](../teaser/dpo-comparison/README.md) | [多用户](svg/tabler-users.svg) · [对话](svg/tabler-message.svg) · [浅层神经网络](svg/towaki-neuralnetwork.svg) · [水平双向箭头](svg/tabler-arrows-right-left.svg) |
| [K-LoRA：主体风格组合与训练范式比较](../teaser/k-lora/README.md) | [图像](svg/tabler-photo.svg) · [锁定](svg/tabler-lock.svg) · [解锁](svg/tabler-lock-open.svg) · [水平双向箭头](svg/tabler-arrows-right-left.svg) |
| [RayDer：数据瓶颈与新训练范式](../teaser/rayder-concept/README.md) | [图像](svg/tabler-photo.svg) · [三维坐标物体](svg/tabler-cube-3d-sphere.svg) · [水平双向箭头](svg/tabler-arrows-right-left.svg) · [锁定](svg/tabler-lock.svg) |
| [Genie · 不同提示生成可交互世界](../teaser/genie-interaction/README.md) | [图像](svg/tabler-photo.svg) · [视频](svg/tabler-video.svg) · [开始](svg/tabler-player-play.svg) · [右箭头](svg/tabler-arrow-right.svg) |
| [VGGT · 多视图输入与统一三维感知能力](../teaser/vggt-capabilities/README.md) | [相机](svg/tabler-camera.svg) · [图像](svg/tabler-photo.svg) · [三维坐标物体](svg/tabler-cube-3d-sphere.svg) |
| [CUT3R · 静态、动态与稀疏照片三类场景](../teaser/cut3r-capabilities/README.md) | [视频](svg/tabler-video.svg) · [图像](svg/tabler-photo.svg) · [相机](svg/tabler-camera.svg) |
| [OrienterNet：用二维地图定位的任务与动机](../teaser/orienternet/README.md) | [地图](svg/tabler-map.svg) · [定位](svg/tabler-map-pin.svg) · [相机](svg/tabler-camera.svg) · [位姿估计模块](svg/rust-pose-estimator.svg) |
| [Uneven Double Refraction：原型与成像能力展示](../teaser/birefractive-rgbd/README.md) | [相机](svg/tabler-camera.svg) · [图像](svg/tabler-photo.svg) · [三维坐标物体](svg/tabler-cube-3d-sphere.svg) |
| [SAM 2 · 任务、模型与数据引擎三联概念图](../teaser/sam2-task-model-data/README.md) | [视频](svg/tabler-video.svg) · [开始](svg/tabler-player-play.svg) · [回环箭头](svg/tabler-arrow-loop-right.svg) · [ViT 编码器块](svg/vit-encoder-block.svg) |
| [3DETR · 输入点云、注意力与检测结果的对应](../teaser/3detr-attention-teaser/README.md) | [相机](svg/tabler-camera.svg) · [三维坐标物体](svg/tabler-cube-3d-sphere.svg) · [目标](svg/tabler-target.svg) |
| [DreamGaussian · 生成能力与优化进程同图展示](../teaser/dreamgaussian-progress/README.md) | [图像](svg/tabler-photo.svg) · [三维坐标物体](svg/tabler-cube-3d-sphere.svg) · [水平双向箭头](svg/tabler-arrows-right-left.svg) · [时钟](svg/tabler-clock.svg) |
| [DECOLLAGE：局部风格控制与三维细化](../teaser/decollage/README.md) | [三维坐标物体](svg/tabler-cube-3d-sphere.svg) · [图像](svg/tabler-photo.svg) · [参数设置](svg/tabler-adjustments.svg) |
| [ShaDDR：粗形状与示例驱动的成果展示](../teaser/shaddr/README.md) | [三维坐标物体](svg/tabler-cube-3d-sphere.svg) · [图像](svg/tabler-photo.svg) · [参数设置](svg/tabler-adjustments.svg) |
| [LightGlue：速度与精度权衡](../teaser/lightglue-tradeoff/README.md) | [散点图符号](svg/tabler-chart-scatter.svg) · [时钟](svg/tabler-clock.svg) · [目标](svg/tabler-target.svg) |
| [MVSplat · 重建质量、速度与参数量的并列对照](../teaser/mvsplat-comparison/README.md) | [图像](svg/tabler-photo.svg) · [柱状图符号](svg/tabler-chart-bar.svg) · [时钟](svg/tabler-clock.svg) · [多尺度特征堆叠](svg/task5-feature-pyramid.svg) |

### Architecture

| 范例 | 现有元素 |
|---|---|
| [CUT3R · 持久状态的更新、读取与未见视角推断](../architecture/cut3r-architecture/README.md) | [编码器块](svg/rust-encoder.svg) · [解码器块](svg/rust-decoder.svg) · [特征表示堆叠](svg/rust-feature-stack.svg) · [回环箭头](svg/tabler-arrow-loop-right.svg) · [相机](svg/tabler-camera.svg) |
| [DreamGaussian · 高斯生成、网格提取与纹理细化](../architecture/dreamgaussian-architecture/README.md) | [图像](svg/tabler-photo.svg) · [三维坐标物体](svg/tabler-cube-3d-sphere.svg) · [水平双向箭头](svg/tabler-arrows-right-left.svg) · [时钟](svg/tabler-clock.svg) · [回环箭头](svg/tabler-arrow-loop-right.svg) |
| [Genie · 视频 tokenizer、潜在动作与动力学模型](../architecture/genie-architecture/README.md) | [视频](svg/tabler-video.svg) · [编码器块](svg/rust-encoder.svg) · [特征表示堆叠](svg/rust-feature-stack.svg) · [分流箭头](svg/tabler-arrows-split.svg) |
| [VAR · 多尺度 VQVAE 与 VAR 两阶段训练](../architecture/var-architecture/README.md) | [多尺度特征堆叠](svg/task5-feature-pyramid.svg) · [多通道彩色张量](svg/task5-rgb-tensor.svg) · [拼接节点](svg/task5-concat.svg) · [上采样节点](svg/task5-upsample.svg) · [匹配相似度矩阵](svg/lightglue-assignment-matrix.svg) |
| [LGM · 从文本或图像到三维高斯和网格的流程](../architecture/lgm-pipeline/README.md) | [图像](svg/tabler-photo.svg) · [三维坐标物体](svg/tabler-cube-3d-sphere.svg) · [水平双向箭头](svg/tabler-arrows-right-left.svg) · [时钟](svg/tabler-clock.svg) · [锁定](svg/tabler-lock.svg) · [解锁](svg/tabler-lock-open.svg) |
| [3D Gaussian Splatting · 优化与光栅化双向流程](../architecture/gaussian-splatting-architecture/README.md) | [相机](svg/tabler-camera.svg) · [回环箭头](svg/tabler-arrow-loop-right.svg) · [水平双向箭头](svg/tabler-arrows-right-left.svg) · [图像](svg/tabler-photo.svg) |
| [CLIP Figure 1：训练到零样本预测](../architecture/clip/README.md) | [图像](svg/tabler-photo.svg) · [文本文件](svg/tabler-file-text.svg) · [编码器块](svg/rust-encoder.svg) · [匹配相似度矩阵](svg/lightglue-assignment-matrix.svg) |
| [RayDer：统一 Transformer 的两个使用阶段](../architecture/rayder/README.md) | [编码器块](svg/rust-encoder.svg) · [解码器块](svg/rust-decoder.svg) · [Self attention 块](svg/lightglue-self-attention.svg) · [锁定](svg/tabler-lock.svg) |
| [RUST：编码器、场景表示与位姿分支](../architecture/rust/README.md) | [编码器块](svg/rust-encoder.svg) · [解码器块](svg/rust-decoder.svg) · [特征表示堆叠](svg/rust-feature-stack.svg) · [回环箭头](svg/tabler-arrow-loop-right.svg) · [相机](svg/tabler-camera.svg) |
| [LAV：感知、预测与驾驶控制流程](../architecture/lav/README.md) | [相机](svg/tabler-camera.svg) · [汽车](svg/tabler-car.svg) · [路径](svg/tabler-route.svg) · [特征表示堆叠](svg/rust-feature-stack.svg) |
| [SAM / LoRA 总体流程与 Transformer 模块](../architecture/sam-lora/README.md) | [图像](svg/tabler-photo.svg) · [Self attention 块](svg/lightglue-self-attention.svg) · [锁定](svg/tabler-lock.svg) · [解锁](svg/tabler-lock-open.svg) |
| [pixelSplat · 概率深度采样与像素对齐高斯](../architecture/pixelsplat-probabilistic-architecture/README.md) | [匹配相似度矩阵](svg/lightglue-assignment-matrix.svg) · [多通道彩色张量](svg/task5-rgb-tensor.svg) · [相机](svg/tabler-camera.svg) · [浅层神经网络](svg/towaki-neuralnetwork.svg) |
| [BLIP-2 · 冻结图像与语言模型的两阶段桥接](../architecture/blip2-bridge-framework/README.md) | [ViT 编码器块](svg/vit-encoder-block.svg) · [条件嵌入模块](svg/dit-embed.svg) · [锁定](svg/tabler-lock.svg) · [解锁](svg/tabler-lock-open.svg) |
| [DiT · 整体主干与三种条件注入模块](../architecture/dit-architecture/README.md) | [Self attention 块](svg/lightglue-self-attention.svg) · [残差加法节点](svg/lightglue-residual-add.svg) · [匹配相似度矩阵](svg/lightglue-assignment-matrix.svg) · [单层特征块](svg/rust-feature-tile.svg) · [乘法节点](svg/task5-multiply.svg) · [加法节点](svg/task5-add.svg) · [Patchify 图像分块模块](svg/dit-patchify.svg) · [条件嵌入模块](svg/dit-embed.svg) · [DiT block 模块](svg/dit-block.svg) · [线性映射与形状重排](svg/dit-linear-reshape.svg) · [LayerNorm 模块](svg/dit-layer-norm.svg) · [带噪潜变量块](svg/dit-noised-latent.svg) · [时间步条件块](svg/dit-timestep.svg) · [类别条件块](svg/dit-class-condition.svg) · [DiT 多头自注意力模块](svg/dit-self-attention.svg) · [逐位置前馈网络模块](svg/dit-feed-forward.svg) · [条件缩放与平移模块](svg/dit-scale-shift.svg) · [DiT 残差加法节点](svg/dit-residual-add.svg) |
| [SD3 · 双模态主干与 MM-DiT block 展开](../architecture/sd3-mmdit-architecture/README.md) | [Self attention 块](svg/lightglue-self-attention.svg) · [残差加法节点](svg/lightglue-residual-add.svg) · [匹配相似度矩阵](svg/lightglue-assignment-matrix.svg) · [单层特征块](svg/rust-feature-tile.svg) · [拼接节点](svg/task5-concat.svg) · [乘法节点](svg/task5-multiply.svg) · [文本文件](svg/tabler-file-text.svg) · [MM-DiT block 模块](svg/sd3-mmdit-block.svg) · [条件 MLP 模块](svg/sd3-conditioning-mlp.svg) · [图像潜变量分块模块](svg/sd3-patching.svg) · [条件调制模块](svg/sd3-modulation.svg) |
| [VGGT · 交替注意力主干与多任务输出头](../architecture/vggt-architecture/README.md) | [Self attention 块](svg/lightglue-self-attention.svg) · [残差加法节点](svg/lightglue-residual-add.svg) · [匹配相似度矩阵](svg/lightglue-assignment-matrix.svg) · [单层特征块](svg/rust-feature-tile.svg) · [相机](svg/tabler-camera.svg) |
| [ViT 原论文 · 图像分块、token 序列与编码器展开](../architecture/vit-original-architecture/README.md) | [Self attention 块](svg/lightglue-self-attention.svg) · [残差加法节点](svg/lightglue-residual-add.svg) · [匹配相似度矩阵](svg/lightglue-assignment-matrix.svg) · [单层特征块](svg/rust-feature-tile.svg) · [多通道彩色张量](svg/task5-rgb-tensor.svg) · [ViT 分类 MLP 头](svg/vit-mlp-head.svg) · [ViT 编码器块](svg/vit-encoder-block.svg) · [类别输出列表](svg/vit-class-output.svg) · [图像块线性投影模块](svg/vit-patch-projection.svg) · [ViT 多头注意力模块](svg/vit-self-attention.svg) · [ViT 归一化模块](svg/vit-norm.svg) · [ViT 前馈 MLP 模块](svg/vit-mlp.svg) · [图像块嵌入模块](svg/vit-embedded-patches.svg) |
| [LGM · 非对称 U-Net 与跨视角注意力](../architecture/lgm-architecture/README.md) | [多尺度特征堆叠](svg/task5-feature-pyramid.svg) · [多通道彩色张量](svg/task5-rgb-tensor.svg) · [拼接节点](svg/task5-concat.svg) · [上采样节点](svg/task5-upsample.svg) · [Self attention 块](svg/lightglue-self-attention.svg) · [相机](svg/tabler-camera.svg) |
| [Instant NGP · 多分辨率哈希编码到 MLP](../architecture/instant-ngp-hash-architecture/README.md) | [匹配相似度矩阵](svg/lightglue-assignment-matrix.svg) · [多尺度特征堆叠](svg/task5-feature-pyramid.svg) · [拼接节点](svg/task5-concat.svg) · [浅层神经网络](svg/towaki-neuralnetwork.svg) |
| [LightGlue：注意力、动态剪枝与匹配](../architecture/lightglue/README.md) | [Self attention 块](svg/lightglue-self-attention.svg) · [残差加法节点](svg/lightglue-residual-add.svg) · [匹配相似度矩阵](svg/lightglue-assignment-matrix.svg) · [单层特征块](svg/rust-feature-tile.svg) |
| [多尺度网络总览与模块展开](../architecture/multiscale-network/README.md) | [多尺度特征堆叠](svg/task5-feature-pyramid.svg) · [多通道彩色张量](svg/task5-rgb-tensor.svg) · [拼接节点](svg/task5-concat.svg) · [上采样节点](svg/task5-upsample.svg) · [CBR 模块](svg/task5-cbr.svg) · [GAP 模块](svg/task5-gap.svg) · [FC + ReLU 模块](svg/task5-fc-relu.svg) |
| [MVSplat · 多视图匹配、代价体与三维高斯预测](../architecture/mvsplat-architecture/README.md) | [Self attention 块](svg/lightglue-self-attention.svg) · [多尺度特征堆叠](svg/task5-feature-pyramid.svg) · [拼接节点](svg/task5-concat.svg) · [特征表示堆叠](svg/rust-feature-stack.svg) |
| [SAM 2 · 流式编码、记忆注意力与记忆库](../architecture/sam2-memory-architecture/README.md) | [视频](svg/tabler-video.svg) · [DiT 多头自注意力模块](svg/dit-self-attention.svg) · [特征表示堆叠](svg/rust-feature-stack.svg) · [回环箭头](svg/tabler-arrow-loop-right.svg) |
| [LLaVA · 视觉投影与语言 token 的统一输入](../architecture/llava-original-architecture/README.md) | [ViT 编码器块](svg/vit-encoder-block.svg) · [线性映射与形状重排](svg/dit-linear-reshape.svg) · [条件嵌入模块](svg/dit-embed.svg) · [文本文件](svg/tabler-file-text.svg) |
| [BLIP-2 · Q-Former 与三种注意力掩码](../architecture/blip2-qformer-architecture/README.md) | [DiT 多头自注意力模块](svg/dit-self-attention.svg) · [匹配相似度矩阵](svg/lightglue-assignment-matrix.svg) · [逐位置前馈网络模块](svg/dit-feed-forward.svg) · [ViT 编码器块](svg/vit-encoder-block.svg) |
| [3DETR · 点云编码器、查询嵌入与集合预测](../architecture/3detr-architecture/README.md) | [ViT 编码器块](svg/vit-encoder-block.svg) · [DiT 多头自注意力模块](svg/dit-self-attention.svg) · [条件嵌入模块](svg/dit-embed.svg) · [ViT 前馈 MLP 模块](svg/vit-mlp.svg) · [三维坐标物体](svg/tabler-cube-3d-sphere.svg) |
| [D2L · Transformer 编码器与解码器](../architecture/d2l-transformer/README.md) | [Self attention 块](svg/lightglue-self-attention.svg) · [残差加法节点](svg/lightglue-residual-add.svg) · [匹配相似度矩阵](svg/lightglue-assignment-matrix.svg) · [单层特征块](svg/rust-feature-tile.svg) · [编码器块](svg/rust-encoder.svg) · [解码器块](svg/rust-decoder.svg) |
| [D2L · Vision Transformer](../architecture/d2l-vit/README.md) | [Self attention 块](svg/lightglue-self-attention.svg) · [残差加法节点](svg/lightglue-residual-add.svg) · [匹配相似度矩阵](svg/lightglue-assignment-matrix.svg) · [单层特征块](svg/rust-feature-tile.svg) · [多通道彩色张量](svg/task5-rgb-tensor.svg) |
| [D2L · 编码器—解码器](../architecture/d2l-encoder-decoder/README.md) | [编码器块](svg/rust-encoder.svg) · [解码器块](svg/rust-decoder.svg) · [特征表示堆叠](svg/rust-feature-stack.svg) · [右向流程箭头](svg/rust-arrow-right.svg) |
| [D2L · 带注意力的 Seq2Seq](../architecture/d2l-seq2seq-attention/README.md) | [编码器块](svg/rust-encoder.svg) · [解码器块](svg/rust-decoder.svg) · [Self attention 块](svg/lightglue-self-attention.svg) · [匹配相似度矩阵](svg/lightglue-assignment-matrix.svg) |
| [D2L · ResNet 残差块](../architecture/d2l-resnet-block/README.md) | [多通道彩色张量](svg/task5-rgb-tensor.svg) · [CBR 模块](svg/task5-cbr.svg) · [输出特征层](svg/task5-output-feature.svg) · [ReLU 曲线](svg/bioicons-relu.svg) · [加法节点](svg/task5-add.svg) |
| [D2L · ResNeXt 分组残差块](../architecture/d2l-resnext-block/README.md) | [多通道彩色张量](svg/task5-rgb-tensor.svg) · [CBR 模块](svg/task5-cbr.svg) · [输出特征层](svg/task5-output-feature.svg) · [ReLU 曲线](svg/bioicons-relu.svg) · [拼接节点](svg/task5-concat.svg) |
| [D2L · DenseNet 密集连接块](../architecture/d2l-densenet-block/README.md) | [多通道彩色张量](svg/task5-rgb-tensor.svg) · [CBR 模块](svg/task5-cbr.svg) · [输出特征层](svg/task5-output-feature.svg) · [ReLU 曲线](svg/bioicons-relu.svg) · [拼接节点](svg/task5-concat.svg) |
| [D2L · Inception 并行分支](../architecture/d2l-inception/README.md) | [多通道彩色张量](svg/task5-rgb-tensor.svg) · [CBR 模块](svg/task5-cbr.svg) · [输出特征层](svg/task5-output-feature.svg) · [ReLU 曲线](svg/bioicons-relu.svg) · [拼接节点](svg/task5-concat.svg) · [分流箭头](svg/tabler-arrows-split.svg) |
| [D2L · LeNet](../architecture/d2l-lenet/README.md) | [多通道彩色张量](svg/task5-rgb-tensor.svg) · [CBR 模块](svg/task5-cbr.svg) · [输出特征层](svg/task5-output-feature.svg) · [ReLU 曲线](svg/bioicons-relu.svg) |
| [D2L · AlexNet](../architecture/d2l-alexnet/README.md) | [多通道彩色张量](svg/task5-rgb-tensor.svg) · [CBR 模块](svg/task5-cbr.svg) · [输出特征层](svg/task5-output-feature.svg) · [ReLU 曲线](svg/bioicons-relu.svg) |
| [D2L · VGG](../architecture/d2l-vgg/README.md) | [多通道彩色张量](svg/task5-rgb-tensor.svg) · [CBR 模块](svg/task5-cbr.svg) · [输出特征层](svg/task5-output-feature.svg) · [ReLU 曲线](svg/bioicons-relu.svg) |
| [D2L · 全卷积网络](../architecture/d2l-fcn/README.md) | [多通道彩色张量](svg/task5-rgb-tensor.svg) · [CBR 模块](svg/task5-cbr.svg) · [输出特征层](svg/task5-output-feature.svg) · [ReLU 曲线](svg/bioicons-relu.svg) · [上采样节点](svg/task5-upsample.svg) |
| [D2L · 多层感知机](../architecture/d2l-mlp/README.md) | [浅层神经网络](svg/towaki-neuralnetwork.svg) · [深层神经网络](svg/towaki-deepneuralnetwork.svg) · [FC + ReLU 模块](svg/task5-fc-relu.svg) · [Sigmoid 曲线](svg/bioicons-sigmoid.svg) |
| [D2L · LSTM 内部门控](../architecture/d2l-lstm-3/README.md) | [乘法节点](svg/task5-multiply.svg) · [加法节点](svg/task5-add.svg) · [拼接节点](svg/task5-concat.svg) · [Sigmoid 曲线](svg/bioicons-sigmoid.svg) · [回环箭头](svg/tabler-arrow-loop-right.svg) |
| [D2L · GRU 内部门控](../architecture/d2l-gru-3/README.md) | [乘法节点](svg/task5-multiply.svg) · [加法节点](svg/task5-add.svg) · [Sigmoid 曲线](svg/bioicons-sigmoid.svg) · [回环箭头](svg/tabler-arrow-loop-right.svg) |
| [D2L · 生成对抗网络](../architecture/d2l-gan/README.md) | [深层神经网络](svg/towaki-deepneuralnetwork.svg) · [分流箭头](svg/tabler-arrows-split.svg) · [回环箭头](svg/tabler-arrow-loop-right.svg) · [图像](svg/tabler-photo.svg) |
