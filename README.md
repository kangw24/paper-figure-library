# Paper Figure Library

个人 CS / AI 论文配图参考与素材库。收集作者公开的 **teaser 范例**、**architecture 范例** 和 **有出处的最小元素**。

**5 个 teaser · 7 个 architecture（5 个论文方法图 + 2 个 AI 教程）· 16 个外部或原图提取元素**。

| 分类 | 入口 | 内容 |
|---|---|---|
| Teaser | [浏览原图](examples/teasers/README.md) | OrienterNet、RayDer、ShaDDR、K-LoRA、Uneven Double Refraction |
| Architecture | [浏览原图](examples/architectures/README.md) | LightGlue、LAV、RUST、RayDer、CLIP；另保留 2 份原生 AI 教程 |
| 最小元素 | [浏览图元](elements/README.md) | 5 个 CC0 原图元 + 11 个从作者 SVG 提取的现成部件 |
| 全部 | [图文目录](CATALOG.md) · [来源索引](catalog.json) | 每项含原文件、预览和来源记录 |

## Teaser 先看这几张

### [OrienterNet：任务与动机](examples/teasers/orienternet/)

![OrienterNet](examples/teasers/orienternet/preview.png)

### [RayDer：既有数据瓶颈与新范式](examples/teasers/rayder-concept/)

![RayDer](examples/teasers/rayder-concept/preview.png)

### [ShaDDR：输入、风格示例与成果](examples/teasers/shaddr/)

![ShaDDR](examples/teasers/shaddr/preview.png)

## Architecture 示例

[![LightGlue](examples/architectures/lightglue/preview.png)](examples/architectures/lightglue/)

## 图元

[![外部来源图元](elements/preview.png)](elements/README.md)

## 收录规则

- 图形必须有可追溯的外部来源。本仓库只下载、提取、转换、做预览与索引；不自行生成图形充数。
- Teaser 按实际作用判断：用任务、动机、方法差异或成果抓住核心贡献。Figure 1 只是编号。
- Architecture 用于说明模块、连接和数据流。LAV、RUST 的原文件虽名为 teaser.svg，仍按结构内容归入 architecture。
- 保留原始 SVG 字节；提取元素记录原文件哈希与节点位置。SVG 中的图片、轮廓文字和实际文字对象分别标注，不把文件后缀当作完全可编辑的证明。
- 来源许可逐项保存；图片中的地图、照片和论文实验结果保留原权利状态。

## 使用与维护

进入条目查看 PNG 预览，再下载 SVG 或 AI。SVG 可交给 Illustrator 导入；已检查浏览渲染，桌面 Illustrator 尚未逐项实测。原生 AI 教程中的旧链接问题见对应说明。

新增素材参见 [CONTRIBUTING.md](CONTRIBUTING.md)。更新目录并检查完整性：

```bash
python scripts/build_catalog.py
python scripts/validate_library.py
```

[本次来源清单](sources/downloads.json) · [旧库纠正记录](docs/curation-correction.md)
