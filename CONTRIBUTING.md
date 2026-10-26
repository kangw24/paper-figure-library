# 收录与维护

只收集有真实外部来源的素材，不用 agent 自绘图元或生成的占位模板填充库。

1. 优先找论文作者项目页、作者仓库与作者提供的源文件。下载前先看图及其论文或项目语境。
2. 按图的用途分 teaser / architecture；不能仅按 Figure 1 或文件名分类。
3. 每个条目保留 source.svg 或 source.ai、preview.png、metadata.json、README.md。记录固定版本 URL、上游路径、SHA256、许可证据、位图数量与文字可编辑情况。
4. 原始下载件不重绘。需要从图中拆部件时，保留完整原图，记录节点位置与画布范围。已有节点可提取，不重新仿画。
5. `elements/catalog.json` 的 source.kind 只能是 external-download 或 extracted-existing-vectors。RUST 的参考部件不代表已取得自由再分发授权；许可状态必须保留。
6. 用 `python scripts/build_catalog.py` 更新索引；`python scripts/validate_library.py` 检查文件、哈希、来源与 SVG 引用。实际查看预览后才能标记 visual_reviewed。

`elements/extraction-specs.json` 保存精确提取位置，`scripts/extract_elements.py` 可以重新提取；这只复制原有 SVG 节点，不生成新几何。

扩充后，完整机制参考图放 references/mechanisms，版式母版放 templates/layouts；两者分别计数。元素页按内容和来源分组，完整画板与完整架构图不能当作一个最小图元凑数。

原 AIT 可能只有提示文字的 PDF 层。遇到这种情况保留原生文件，改用原作者配套 PDF 或官方网页预览，并在元数据明确注明。预览文件变更后更新对应文件哈希。
