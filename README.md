# Paper Figure Library

个人 CS / AI 论文配图库：积累 **teaser 的叙事与布局**、**architecture 的结构表达**，以及可以直接组合的 **最小 SVG 元素**。

首批收录：**5 个 teaser 范例 · 2 个架构图范例 · 24 个独立元素**。以 Illustrator 编辑为主要使用场景，同时保留 SVG、原始 PDF、原生 AI 和配套素材。

## 从这里开始

| 分类 | 内容 | 入口 |
|---|---|---|
| **Teasers** | 核心想法、方法对比、动机与贡献的视觉概述 | [5 个范例](examples/teasers/README.md) |
| **Architectures** | 模型内部结构、总体框架、模块连接和方法流程 | [2 个范例](examples/architectures/README.md) |
| **Elements** | 模块、数据表示、运算节点、箭头和训练标记 | [24 个独立 SVG](elements/README.md) |
| **全部素材** | 按类别浏览预览、格式、标签和使用状态 | [图文总目录](CATALOG.md) · [JSON 目录](catalog.json) |

| Teaser 示例 | Architecture 示例 |
|---|---|
| [![方法范式对比](examples/teasers/method-comparison/preview.png)](examples/teasers/method-comparison/README.md) | [![多尺度网络架构](examples/architectures/multiscale-network/preview.png)](examples/architectures/multiscale-network/README.md) |

### 最小元素总览

[![24 个最小可复用元素](elements/preview.png)](elements/README.md)

## 首批范例

| 范例 | 可借鉴的表达 | 主文件 |
|---|---|---|
| [Method comparison](examples/teasers/method-comparison/) | 并排比较已有范式与提出的方法 | SVG |
| [Evaluation blind spot](examples/teasers/evaluation-blindspot/) | 用可视化指出评估或观测的盲区 | SVG |
| [CLIP Figure 1](examples/teasers/clip/) | 一个训练阶段、两个应用阶段的层次安排 | SVG + 原 PDF |
| [Neural ODE Figure 1](examples/teasers/neural-ode/) | 离散变换与连续动力学的概念对照 | SVG + 原 PDF |
| [Penrose teaser](examples/teasers/penrose/) | 同一抽象关系在三种几何下的表达 | SVG；实际 Figure 1 的三联图部分 |
| [Multiscale network](examples/architectures/multiscale-network/) | 主干、特征融合和分割输出的架构布局 | 原生 AI，7 个画板 |
| [SAM / LoRA](examples/architectures/sam-lora/) | 总体流程与局部可训练模块的对应 | 原生 AI，2 个画板 |

两个通用 teaser 模板、真实论文图例和绘图教程分别标明类型。主分类按图的主要用途选取；同一条目可以通过标签同时关联 teaser、architecture、pipeline 等用途。

## 使用方式

1. **先看预览与说明**：进入条目目录，了解它的布局、来源和可编辑范围。
2. **打开源文件**：Illustrator 打开 `source.ai` 或 `source.svg`。PDF 转出的 SVG 可能把文字拆成多个对象；论文中的照片仍是嵌入位图。
3. **组合元素**：打开 [all-elements.svg](elements/all-elements.svg) 复制目标元素组，或从 [elements/svg](elements/svg/) 选取单独文件。
4. **在论文项目中修改副本**：替换文字、模型模块、数值与真实实验结果。范例库中的原文件和来源记录保持可追溯。

首批素材已做文件完整性、SVG 自包含性和预览渲染检查，尚未在桌面 Illustrator 中逐项打开。SAM / LoRA 原 AI 含作者本地 PSD 的旧链接，条目说明中列有已收集的配套文件。

## 持续维护

新增范例时，为它建立独立目录，放入源文件、预览、`metadata.json` 和简短的 `README.md`。详细步骤见 [CONTRIBUTING.md](CONTRIBUTING.md)。

在仓库根目录运行：

```bash
python scripts/build_catalog.py
python scripts/validate_library.py
```

原创元素可通过以下命令重新生成；`--render` 额外需要本机安装 Inkscape：

```bash
python scripts/generate_elements.py --render
```

生成器会覆盖同名生成文件；长期修改应同时更新生成器。颜色、线宽与字体参数见 [style-tokens.json](elements/style-tokens.json)。

## 来源与许可

本仓库是私人收集与绘图工作库，**各条素材按自己的来源和许可管理**。没有给第三方素材统一套用开源许可证。

- 两个 CVPR-Figure 模板和 Penrose 素材保留来源仓库的 MIT 许可证。
- CLIP、Neural ODE 保存为论文图例与版式参考；arXiv 的分发许可不等于通用模板授权。
- 两份 Illustrator 教程源文件未发现明确 LICENSE，保留原作者与下载来源。
- `elements/` 为本仓库原创的绘图元素，暂未设置对外再分发许可。

来源 URL、格式转换、嵌入位图、旧链接和文件校验值均记录在对应条目的说明与元数据中。
