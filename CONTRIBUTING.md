# 新增与维护素材

仓库保存可编辑源文件、可快速浏览的预览，以及能追溯到作者的来源记录。使用 Python 3.9 或更新版本即可运行维护脚本；不需要第三方 Python 包。

## 选择主分类

| 目录 | 何时放入 | 推荐标签 |
|---|---|---|
| `examples/teasers/<id>/` | 展示核心概念、研究动机、已有方法与本文方法差异、直观结果 | `motivation`、`comparison`、`conceptual` |
| `examples/architectures/<id>/` | 展示网络结构、整体方法框架、数据流程或模块内部连接 | `network`、`framework`、`pipeline` |
| `elements/svg/` | 能独立复制的小元素，例如张量、连接箭头、模块或训练标识 | `tensor`、`arrow`、`module` |

按主要用途选一个主目录，其他用途写入标签。Figure 1 是编号；teaser 是图的用途；架构图也可以承担 teaser 的作用。无需复制同一个源文件到两个目录。

## 新增一个范例

1. 在对应目录下建立小写、连字符命名的子目录，例如 `examples/teasers/my-method-comparison/`。
2. 放入可编辑主文件，如 `source.ai`、`source.svg` 或 `source.pdf`，再放入清晰的 `preview.png`。保留作者原件时使用 `originals/`；图片等配套依赖放入 `assets/`。
3. 复制 [metadata 模板](docs/entry-template.json) 为条目内的 `metadata.json`，填写标题、类型、标签、来源 URL、原文件名称、许可状态、编辑能力、修改记录与日期。模板中的示例值必须替换。
4. 写一份 `README.md`：展示预览，说明这张图适合借鉴什么，链接源文件与作者页面，解释字体、外部链接、位图和转换限制。若有明确许可文件，将原文保存为 `LICENSE.source.txt` 并在元数据中引用。
5. 从仓库根目录运行下列命令。第一条会先校验素材，再重建 [图文目录](CATALOG.md) 与机器可读的 `catalog.json`；第二条可单独复核。

```bash
python scripts/build_catalog.py
python scripts/validate_library.py
```

完成后在本地打开预览和源文件检查画面，再提交新增目录和自动生成的索引。`CATALOG.md` 与根目录 `catalog.json` 是生成结果，修改各条目的元数据即可维护它们。

## 元数据约定

| 字段 | 说明 |
|---|---|
| `id` | 仓库内唯一的小写标识，只用字母、数字与连字符 |
| `category` | `teaser` 或 `architecture`，与所在目录一致 |
| `kind` | `template`、`paper-example`、`tutorial-example` 或 `original-example` |
| `primary_file` / `preview` | 相对于当前条目目录的文件路径 |
| `source` | 作者、项目或论文、具体原文件、来源 URL、获取日期 |
| `license` | 已确认的名称与状态；未见许可证就明确记录未见，不作授权推断 |
| `editability` | 原生格式、矢量对象、可编辑文字、嵌入位图、验证范围 |
| `changes` | 与作者原文件相比做过哪些变更；未修改也写明 |
| `files` | 可选的文件大小与 SHA256 清单，用于发现原件被意外修改 |

首批范例保存了文件校验和。修改这些文件后，校验脚本会报出不一致；请先确认变更符合目的，再更新记录。优先把个人改稿另存为 `adapted/` 内的新文件，并记录修改，不要覆盖保留的作者原件。

## 新增或修改最小元素

统一风格的原创元素由 `scripts/generate_elements.py` 维护，样式见 `elements/style-tokens.json`。修改生成器后重新运行它，更新元素索引和总览 SVG；PNG 总览需按 [元素说明](elements/README.md) 使用 Inkscape 重新渲染。然后运行 `python scripts/build_catalog.py`。

手工新增元素时，在 `elements/svg/` 保存独立 SVG，并向 `elements/catalog.json` 的 `items` 增加对应条目、同步 `count`，更新总览。路径以仓库根目录为基准。外部来源元素要如实记录来源和权利状态，不能沿用原创元素的声明。手工文件也应加入生成器的维护流程，以免后续重建遗漏。

SVG 优先使用直接的形状、路径和文字，保留合理的 `viewBox`。图片依赖应嵌入或明确保留为配套文件；入库的 SVG 需要自包含。不要包含脚本、事件属性、`foreignObject` 或外部样式资源。校验通过后仍应看一次实际渲染，确认字体、箭头和版面没有变化。

## 来源、许可与复用

每个素材遵循其自身的许可与授权情况，仓库不设置覆盖第三方素材的统一许可证。MIT 条目保留原版权及许可声明；论文来源与公开下载的教程文件按实际查得的许可状态记录。作者公开了源文件，并不自动代表可以按 MIT 或 CC0 发布。

“可编辑”描述文件结构，不等于授权范围。SVG 内的照片仍是位图；PDF 转换到 SVG 的文字可能被拆成多个对象；只有真正的 Illustrator 原生文件才标记为原生 AI。没有在桌面 Illustrator 中打开过的文件，应在说明中保留这一验证范围。

## 脚本检查范围

校验覆盖元数据必要字段、唯一 ID、文件路径和非空状态、记录过的 SHA256，以及 SVG 的 XML 结构和外部依赖。它不会打开或执行 AI、PDF、PPTX 中的内容，也不会自动证明版权、语义正确性或桌面软件兼容性。预览与人工检查仍是入库步骤的一部分。
