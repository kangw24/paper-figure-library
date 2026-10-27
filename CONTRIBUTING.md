# 收录与维护

只收集有真实外部来源的素材，不用 agent 自绘图元或生成的占位模板填充库。

实体目录固定为根目录下的 `teaser/`、`architecture/`、`element/`，不再嵌套一层 examples。三类通过 README 与 `relationships.json` 互链。

1. 优先找论文作者项目页、作者仓库与作者提供的源文件。下载前先看图及其论文或项目语境。
2. 按图的用途分 teaser / architecture；不能仅按 Figure 1 或文件名分类。
3. 每个条目保留 source.svg 或 source.ai、preview.png、metadata.json、README.md。记录固定版本 URL、上游路径、SHA256、许可证据、位图数量与文字可编辑情况。
4. 原始下载件不重绘。需要从图中拆部件时，保留完整原图，记录节点位置与画布范围。已有节点可提取，不重新仿画。
5. `element/catalog.json` 的 source.kind 只能是 external-download 或 extracted-existing-vectors。RUST 的参考部件不代表已取得自由再分发授权；许可状态必须保留。
6. 用 `python scripts/build_catalog.py` 更新索引；`python scripts/validate_library.py` 检查文件、哈希、来源与 SVG 引用。实际查看预览后才能标记 visual_reviewed。

`element/extraction-specs.json` 保存精确提取位置，`scripts/extract_elements.py` 可以重新提取；这只复制原有 SVG 节点，不生成新几何。

扩充后，完整机制参考图放 references/mechanisms，版式母版放 templates/layouts；两者分别计数。元素页按内容和来源分组，完整画板与完整架构图不能当作一个最小图元凑数。

原 AIT 可能只有提示文字的 PDF 层。遇到这种情况保留原生文件，改用原作者配套 PDF 或官方网页预览，并在元数据明确注明。预览文件变更后更新对应文件哈希。


## 论文图的分类与来源

- 按图的作用分类：teaser 表达概念、差异或核心能力；architecture / framework 解释方法内部结构。Figure 1 编号本身不决定类别。
- Oral 标签必须指向会议官网、作者项目页或官方代码仓库中的明确声明。奖项、候选奖、Poster、Spotlight、Oral 分开记录，不能互相推定。
- 先逐页看图再选，写清它的构图或信息表达为什么值得借鉴。普通样例拼图不自动收成 teaser。
- PDF 摘图记录原文 URL 与 SHA256、页码、图号、裁剪坐标和转换步骤。提供 SVG 时说明文字是否为轮廓，以及哪些部分本来就是位图。
- 作者本身只提供整张位图时，标为 `raster-reference`，保留真实图片；不将图片包在 SVG 中宣称可编辑。
- 提取后同时检查原 PDF 裁剪、单图 PDF 和 SVG 的显示，特别核对底部标签、透明图片及边框。PDF 字体的边界框可能大于可见字形，删除外围正文时要保留文字边距再裁剪。
- 会议、年份、Oral 和奖项只作为条目标签，不单独建立会议文件夹或精选集合。来源批次记录保留在 sources，不作为浏览分类。
- Teaser、Architecture、Element 三类通过各自 README 和条目 README 互链。同一论文的多张图互链；元素必须区分“从该原图拆出”和“功能相近的现有素材”。
- 在 `relationships.json` 维护按表达用途的二级分组、同论文关联及现有元素关联；分组覆盖每个范例且不重复。实际拆件关系从元素的 `source.local_original` / `source.native_original` 读取，不手工伪造。
- 运行目录生成器后会更新两类范例目录、各条目的关联段落、Element 分类页和 `element/with-examples.md`。不要只修改生成出的 Markdown 而漏改关联记录。

## 综述原图

- 先按实际用途区分概念场景、领域全景、时间线、谱系和分类路线图；综述中的统一框架与模块分解仍放 Architecture。图号与具体子类型写入元数据。
- 综述放在现有根目录分类中，使用 `survey` 标签和 `publication.article_type: survey`，不另建 survey 实体文件夹。期刊年份和所收录 arXiv 修订版本分别记录，不给期刊综述套 Oral 标签。
- 作者 TeX 归档中的独立 PDF 优先原样保存。记录固定版本的归档 URL、SHA256、成员路径与原件 SHA256，并保留原始插图定义；转换 SVG 的文字轮廓与原有位图须单独说明。
- 个别作者会在 LaTeX 中叠加章节、引文或子图编号，独立 PDF 中预留空槽。保留原件并在条目显著说明，不能悄悄补字后宣称是原文件。
- 时间线、增长曲线与谱系图是对应版本的历史快照，不能因今天收录而暗示其中内容已更新到今天。


`element/vector-parts.json` 记录从论文 SVG 提取的精确节点路径，`scripts/extract_vector_parts.py` 可在不重绘的情况下重新提取。完整机制图与版式模板继续作为辅助资料，从相应类别页链接。
