# 范例与元素对照

[Teaser](../examples/teasers/README.md) · [Architecture](../examples/architectures/README.md) · [Element](README.md) · [总目录](../CATALOG.md)

由 teaser 看表达思路，由 architecture 看信息流，再沿下列链接选元素。只有来源记录指向该原图的条目，才标作原图拆件。

## 从原图拆出的部件

| 原图 | 已有独立元素 |
|---|---|
| [LightGlue：注意力、动态剪枝与匹配](../examples/architectures/lightglue/README.md) | [Self attention 块](svg/lightglue-self-attention.svg) · [匹配相似度矩阵](svg/lightglue-assignment-matrix.svg) · [残差加法节点](svg/lightglue-residual-add.svg) · [蓝色流程箭头](svg/lightglue-flow-arrow.svg) |
| [多尺度网络总览与模块展开](../examples/architectures/multiscale-network/README.md) | [输入特征层](svg/task5-input-feature.svg) · [多尺度特征堆叠](svg/task5-feature-pyramid.svg) · [多通道彩色张量](svg/task5-rgb-tensor.svg) · [输出特征层](svg/task5-output-feature.svg) · [拼接节点](svg/task5-concat.svg) · [加法节点](svg/task5-add.svg) · [乘法节点](svg/task5-multiply.svg) · [上采样节点](svg/task5-upsample.svg) · [CBR 模块](svg/task5-cbr.svg) · [GAP 模块](svg/task5-gap.svg) · [FC + ReLU 模块](svg/task5-fc-relu.svg) |
| [RUST：编码器、场景表示与位姿分支](../examples/architectures/rust/README.md) | [编码器块](svg/rust-encoder.svg) · [解码器块](svg/rust-decoder.svg) · [特征表示堆叠](svg/rust-feature-stack.svg) · [单层特征块](svg/rust-feature-tile.svg) · [位姿估计模块](svg/rust-pose-estimator.svg) · [右向流程箭头](svg/rust-arrow-right.svg) · [下向流程箭头](svg/rust-arrow-down.svg) |

## 按范例找可搭配元素

本节是表达功能的对应关系，**不表示元素出自所列论文**。各元素保留自己的作者和许可。

### Teaser

| 范例 | 现有元素 |
|---|---|
| [VAR · 从逐 token 到逐尺度生成的范式对照](../examples/teasers/var-paradigm/README.md) | [多尺度特征堆叠](svg/task5-feature-pyramid.svg) · [多通道彩色张量](svg/task5-rgb-tensor.svg) · [拼接节点](svg/task5-concat.svg) · [上采样节点](svg/task5-upsample.svg) · [水平双向箭头](svg/tabler-arrows-right-left.svg) |
| [DPO · RLHF 与直接偏好优化的流程简化](../examples/teasers/dpo-comparison/README.md) | [多用户](svg/tabler-users.svg) · [对话](svg/tabler-message.svg) · [浅层神经网络](svg/towaki-neuralnetwork.svg) · [水平双向箭头](svg/tabler-arrows-right-left.svg) |
| [K-LoRA：主体风格组合与训练范式比较](../examples/teasers/k-lora/README.md) | [图像](svg/tabler-photo.svg) · [锁定](svg/tabler-lock.svg) · [解锁](svg/tabler-lock-open.svg) · [水平双向箭头](svg/tabler-arrows-right-left.svg) |
| [RayDer：数据瓶颈与新训练范式](../examples/teasers/rayder-concept/README.md) | [图像](svg/tabler-photo.svg) · [三维坐标物体](svg/tabler-cube-3d-sphere.svg) · [水平双向箭头](svg/tabler-arrows-right-left.svg) · [锁定](svg/tabler-lock.svg) |
| [Genie · 不同提示生成可交互世界](../examples/teasers/genie-interaction/README.md) | [图像](svg/tabler-photo.svg) · [视频](svg/tabler-video.svg) · [开始](svg/tabler-player-play.svg) · [右箭头](svg/tabler-arrow-right.svg) |
| [VGGT · 多视图输入与统一三维感知能力](../examples/teasers/vggt-capabilities/README.md) | [相机](svg/tabler-camera.svg) · [图像](svg/tabler-photo.svg) · [三维坐标物体](svg/tabler-cube-3d-sphere.svg) |
| [CUT3R · 静态、动态与稀疏照片三类场景](../examples/teasers/cut3r-capabilities/README.md) | [视频](svg/tabler-video.svg) · [图像](svg/tabler-photo.svg) · [相机](svg/tabler-camera.svg) |
| [OrienterNet：用二维地图定位的任务与动机](../examples/teasers/orienternet/README.md) | [地图](svg/tabler-map.svg) · [定位](svg/tabler-map-pin.svg) · [相机](svg/tabler-camera.svg) · [位姿估计模块](svg/rust-pose-estimator.svg) |
| [Uneven Double Refraction：原型与成像能力展示](../examples/teasers/birefractive-rgbd/README.md) | [相机](svg/tabler-camera.svg) · [图像](svg/tabler-photo.svg) · [三维坐标物体](svg/tabler-cube-3d-sphere.svg) |
| [DreamGaussian · 生成能力与优化进程同图展示](../examples/teasers/dreamgaussian-progress/README.md) | [图像](svg/tabler-photo.svg) · [三维坐标物体](svg/tabler-cube-3d-sphere.svg) · [水平双向箭头](svg/tabler-arrows-right-left.svg) · [时钟](svg/tabler-clock.svg) |
| [DECOLLAGE：局部风格控制与三维细化](../examples/teasers/decollage/README.md) | [三维坐标物体](svg/tabler-cube-3d-sphere.svg) · [图像](svg/tabler-photo.svg) · [参数设置](svg/tabler-adjustments.svg) |
| [ShaDDR：粗形状与示例驱动的成果展示](../examples/teasers/shaddr/README.md) | [三维坐标物体](svg/tabler-cube-3d-sphere.svg) · [图像](svg/tabler-photo.svg) · [参数设置](svg/tabler-adjustments.svg) |
| [LightGlue：速度与精度权衡](../examples/teasers/lightglue-tradeoff/README.md) | [散点图符号](svg/tabler-chart-scatter.svg) · [时钟](svg/tabler-clock.svg) · [目标](svg/tabler-target.svg) |

### Architecture

| 范例 | 现有元素 |
|---|---|
| [CUT3R · 持久状态的更新、读取与未见视角推断](../examples/architectures/cut3r-architecture/README.md) | [编码器块](svg/rust-encoder.svg) · [解码器块](svg/rust-decoder.svg) · [特征表示堆叠](svg/rust-feature-stack.svg) · [回环箭头](svg/tabler-arrow-loop-right.svg) · [相机](svg/tabler-camera.svg) |
| [DreamGaussian · 高斯生成、网格提取与纹理细化](../examples/architectures/dreamgaussian-architecture/README.md) | [图像](svg/tabler-photo.svg) · [三维坐标物体](svg/tabler-cube-3d-sphere.svg) · [水平双向箭头](svg/tabler-arrows-right-left.svg) · [时钟](svg/tabler-clock.svg) · [回环箭头](svg/tabler-arrow-loop-right.svg) |
| [Genie · 视频 tokenizer、潜在动作与动力学模型](../examples/architectures/genie-architecture/README.md) | [视频](svg/tabler-video.svg) · [编码器块](svg/rust-encoder.svg) · [特征表示堆叠](svg/rust-feature-stack.svg) · [分流箭头](svg/tabler-arrows-split.svg) |
| [VAR · 多尺度 VQVAE 与 VAR 两阶段训练](../examples/architectures/var-architecture/README.md) | [多尺度特征堆叠](svg/task5-feature-pyramid.svg) · [多通道彩色张量](svg/task5-rgb-tensor.svg) · [拼接节点](svg/task5-concat.svg) · [上采样节点](svg/task5-upsample.svg) · [匹配相似度矩阵](svg/lightglue-assignment-matrix.svg) |
| [LGM · 从文本或图像到三维高斯和网格的流程](../examples/architectures/lgm-pipeline/README.md) | [图像](svg/tabler-photo.svg) · [三维坐标物体](svg/tabler-cube-3d-sphere.svg) · [水平双向箭头](svg/tabler-arrows-right-left.svg) · [时钟](svg/tabler-clock.svg) · [锁定](svg/tabler-lock.svg) · [解锁](svg/tabler-lock-open.svg) |
| [3D Gaussian Splatting · 优化与光栅化双向流程](../examples/architectures/gaussian-splatting-architecture/README.md) | [相机](svg/tabler-camera.svg) · [回环箭头](svg/tabler-arrow-loop-right.svg) · [水平双向箭头](svg/tabler-arrows-right-left.svg) · [图像](svg/tabler-photo.svg) |
| [CLIP Figure 1：训练到零样本预测](../examples/architectures/clip/README.md) | [图像](svg/tabler-photo.svg) · [文本文件](svg/tabler-file-text.svg) · [编码器块](svg/rust-encoder.svg) · [匹配相似度矩阵](svg/lightglue-assignment-matrix.svg) |
| [RayDer：统一 Transformer 的两个使用阶段](../examples/architectures/rayder/README.md) | [编码器块](svg/rust-encoder.svg) · [解码器块](svg/rust-decoder.svg) · [Self attention 块](svg/lightglue-self-attention.svg) · [锁定](svg/tabler-lock.svg) |
| [RUST：编码器、场景表示与位姿分支](../examples/architectures/rust/README.md) | [编码器块](svg/rust-encoder.svg) · [解码器块](svg/rust-decoder.svg) · [特征表示堆叠](svg/rust-feature-stack.svg) · [回环箭头](svg/tabler-arrow-loop-right.svg) · [相机](svg/tabler-camera.svg) |
| [LAV：感知、预测与驾驶控制流程](../examples/architectures/lav/README.md) | [相机](svg/tabler-camera.svg) · [汽车](svg/tabler-car.svg) · [路径](svg/tabler-route.svg) · [特征表示堆叠](svg/rust-feature-stack.svg) |
| [SAM / LoRA 总体流程与 Transformer 模块](../examples/architectures/sam-lora/README.md) | [图像](svg/tabler-photo.svg) · [Self attention 块](svg/lightglue-self-attention.svg) · [锁定](svg/tabler-lock.svg) · [解锁](svg/tabler-lock-open.svg) |
| [DiT · 整体主干与三种条件注入模块](../examples/architectures/dit-architecture/README.md) | [Self attention 块](svg/lightglue-self-attention.svg) · [残差加法节点](svg/lightglue-residual-add.svg) · [匹配相似度矩阵](svg/lightglue-assignment-matrix.svg) · [单层特征块](svg/rust-feature-tile.svg) · [乘法节点](svg/task5-multiply.svg) · [加法节点](svg/task5-add.svg) |
| [SD3 · 双模态主干与 MM-DiT block 展开](../examples/architectures/sd3-mmdit-architecture/README.md) | [Self attention 块](svg/lightglue-self-attention.svg) · [残差加法节点](svg/lightglue-residual-add.svg) · [匹配相似度矩阵](svg/lightglue-assignment-matrix.svg) · [单层特征块](svg/rust-feature-tile.svg) · [拼接节点](svg/task5-concat.svg) · [乘法节点](svg/task5-multiply.svg) · [文本文件](svg/tabler-file-text.svg) |
| [VGGT · 交替注意力主干与多任务输出头](../examples/architectures/vggt-architecture/README.md) | [Self attention 块](svg/lightglue-self-attention.svg) · [残差加法节点](svg/lightglue-residual-add.svg) · [匹配相似度矩阵](svg/lightglue-assignment-matrix.svg) · [单层特征块](svg/rust-feature-tile.svg) · [相机](svg/tabler-camera.svg) |
| [ViT 原论文 · 图像分块、token 序列与编码器展开](../examples/architectures/vit-original-architecture/README.md) | [Self attention 块](svg/lightglue-self-attention.svg) · [残差加法节点](svg/lightglue-residual-add.svg) · [匹配相似度矩阵](svg/lightglue-assignment-matrix.svg) · [单层特征块](svg/rust-feature-tile.svg) · [多通道彩色张量](svg/task5-rgb-tensor.svg) |
| [LGM · 非对称 U-Net 与跨视角注意力](../examples/architectures/lgm-architecture/README.md) | [多尺度特征堆叠](svg/task5-feature-pyramid.svg) · [多通道彩色张量](svg/task5-rgb-tensor.svg) · [拼接节点](svg/task5-concat.svg) · [上采样节点](svg/task5-upsample.svg) · [Self attention 块](svg/lightglue-self-attention.svg) · [相机](svg/tabler-camera.svg) |
| [Instant NGP · 多分辨率哈希编码到 MLP](../examples/architectures/instant-ngp-hash-architecture/README.md) | [匹配相似度矩阵](svg/lightglue-assignment-matrix.svg) · [多尺度特征堆叠](svg/task5-feature-pyramid.svg) · [拼接节点](svg/task5-concat.svg) · [浅层神经网络](svg/towaki-neuralnetwork.svg) |
| [LightGlue：注意力、动态剪枝与匹配](../examples/architectures/lightglue/README.md) | [Self attention 块](svg/lightglue-self-attention.svg) · [残差加法节点](svg/lightglue-residual-add.svg) · [匹配相似度矩阵](svg/lightglue-assignment-matrix.svg) · [单层特征块](svg/rust-feature-tile.svg) |
| [多尺度网络总览与模块展开](../examples/architectures/multiscale-network/README.md) | [多尺度特征堆叠](svg/task5-feature-pyramid.svg) · [多通道彩色张量](svg/task5-rgb-tensor.svg) · [拼接节点](svg/task5-concat.svg) · [上采样节点](svg/task5-upsample.svg) · [CBR 模块](svg/task5-cbr.svg) · [GAP 模块](svg/task5-gap.svg) · [FC + ReLU 模块](svg/task5-fc-relu.svg) |
| [D2L · Transformer 编码器与解码器](../examples/architectures/d2l-transformer/README.md) | [Self attention 块](svg/lightglue-self-attention.svg) · [残差加法节点](svg/lightglue-residual-add.svg) · [匹配相似度矩阵](svg/lightglue-assignment-matrix.svg) · [单层特征块](svg/rust-feature-tile.svg) · [编码器块](svg/rust-encoder.svg) · [解码器块](svg/rust-decoder.svg) |
| [D2L · Vision Transformer](../examples/architectures/d2l-vit/README.md) | [Self attention 块](svg/lightglue-self-attention.svg) · [残差加法节点](svg/lightglue-residual-add.svg) · [匹配相似度矩阵](svg/lightglue-assignment-matrix.svg) · [单层特征块](svg/rust-feature-tile.svg) · [多通道彩色张量](svg/task5-rgb-tensor.svg) |
| [D2L · 编码器—解码器](../examples/architectures/d2l-encoder-decoder/README.md) | [编码器块](svg/rust-encoder.svg) · [解码器块](svg/rust-decoder.svg) · [特征表示堆叠](svg/rust-feature-stack.svg) · [右向流程箭头](svg/rust-arrow-right.svg) |
| [D2L · 带注意力的 Seq2Seq](../examples/architectures/d2l-seq2seq-attention/README.md) | [编码器块](svg/rust-encoder.svg) · [解码器块](svg/rust-decoder.svg) · [Self attention 块](svg/lightglue-self-attention.svg) · [匹配相似度矩阵](svg/lightglue-assignment-matrix.svg) |
| [D2L · ResNet 残差块](../examples/architectures/d2l-resnet-block/README.md) | [多通道彩色张量](svg/task5-rgb-tensor.svg) · [CBR 模块](svg/task5-cbr.svg) · [输出特征层](svg/task5-output-feature.svg) · [ReLU 曲线](svg/bioicons-relu.svg) · [加法节点](svg/task5-add.svg) |
| [D2L · ResNeXt 分组残差块](../examples/architectures/d2l-resnext-block/README.md) | [多通道彩色张量](svg/task5-rgb-tensor.svg) · [CBR 模块](svg/task5-cbr.svg) · [输出特征层](svg/task5-output-feature.svg) · [ReLU 曲线](svg/bioicons-relu.svg) · [拼接节点](svg/task5-concat.svg) |
| [D2L · DenseNet 密集连接块](../examples/architectures/d2l-densenet-block/README.md) | [多通道彩色张量](svg/task5-rgb-tensor.svg) · [CBR 模块](svg/task5-cbr.svg) · [输出特征层](svg/task5-output-feature.svg) · [ReLU 曲线](svg/bioicons-relu.svg) · [拼接节点](svg/task5-concat.svg) |
| [D2L · Inception 并行分支](../examples/architectures/d2l-inception/README.md) | [多通道彩色张量](svg/task5-rgb-tensor.svg) · [CBR 模块](svg/task5-cbr.svg) · [输出特征层](svg/task5-output-feature.svg) · [ReLU 曲线](svg/bioicons-relu.svg) · [拼接节点](svg/task5-concat.svg) · [分流箭头](svg/tabler-arrows-split.svg) |
| [D2L · LeNet](../examples/architectures/d2l-lenet/README.md) | [多通道彩色张量](svg/task5-rgb-tensor.svg) · [CBR 模块](svg/task5-cbr.svg) · [输出特征层](svg/task5-output-feature.svg) · [ReLU 曲线](svg/bioicons-relu.svg) |
| [D2L · AlexNet](../examples/architectures/d2l-alexnet/README.md) | [多通道彩色张量](svg/task5-rgb-tensor.svg) · [CBR 模块](svg/task5-cbr.svg) · [输出特征层](svg/task5-output-feature.svg) · [ReLU 曲线](svg/bioicons-relu.svg) |
| [D2L · VGG](../examples/architectures/d2l-vgg/README.md) | [多通道彩色张量](svg/task5-rgb-tensor.svg) · [CBR 模块](svg/task5-cbr.svg) · [输出特征层](svg/task5-output-feature.svg) · [ReLU 曲线](svg/bioicons-relu.svg) |
| [D2L · 全卷积网络](../examples/architectures/d2l-fcn/README.md) | [多通道彩色张量](svg/task5-rgb-tensor.svg) · [CBR 模块](svg/task5-cbr.svg) · [输出特征层](svg/task5-output-feature.svg) · [ReLU 曲线](svg/bioicons-relu.svg) · [上采样节点](svg/task5-upsample.svg) |
| [D2L · 多层感知机](../examples/architectures/d2l-mlp/README.md) | [浅层神经网络](svg/towaki-neuralnetwork.svg) · [深层神经网络](svg/towaki-deepneuralnetwork.svg) · [FC + ReLU 模块](svg/task5-fc-relu.svg) · [Sigmoid 曲线](svg/bioicons-sigmoid.svg) |
| [D2L · LSTM 内部门控](../examples/architectures/d2l-lstm-3/README.md) | [乘法节点](svg/task5-multiply.svg) · [加法节点](svg/task5-add.svg) · [拼接节点](svg/task5-concat.svg) · [Sigmoid 曲线](svg/bioicons-sigmoid.svg) · [回环箭头](svg/tabler-arrow-loop-right.svg) |
| [D2L · GRU 内部门控](../examples/architectures/d2l-gru-3/README.md) | [乘法节点](svg/task5-multiply.svg) · [加法节点](svg/task5-add.svg) · [Sigmoid 曲线](svg/bioicons-sigmoid.svg) · [回环箭头](svg/tabler-arrow-loop-right.svg) |
| [D2L · 生成对抗网络](../examples/architectures/d2l-gan/README.md) | [深层神经网络](svg/towaki-deepneuralnetwork.svg) · [分流箭头](svg/tabler-arrows-split.svg) · [回环箭头](svg/tabler-arrow-loop-right.svg) · [图像](svg/tabler-photo.svg) |
