#!/usr/bin/env python3
"""Build Markdown links between figure roles and existing reusable elements."""
import json
import os
import re
from pathlib import Path

MARKER = '<!-- BEGIN FIGURE LINKS -->'
END_MARKER = '<!-- END FIGURE LINKS -->'


def relative(page, target):
    return Path(os.path.relpath(target, page.parent)).as_posix()


def link(page, title, target):
    return '[' + title + '](' + relative(page, target) + ')'


def load(root):
    figures = {}
    for folder in ('teaser', 'architecture'):
        for path in sorted((root / folder).glob('*/metadata.json')):
            item = json.loads(path.read_text(encoding='utf-8'))
            item['_folder'] = path.parent
            item['_relative_folder'] = path.parent.relative_to(root).as_posix()
            figures[item['id']] = item
    elements = {x['id']: x for x in json.loads((root / 'element/catalog.json').read_text())['items']}
    config = json.loads((root / 'relationships.json').read_text())
    errors = []
    grouped = []
    for category, groups in config['groups'].items():
        for group in groups:
            for figure_id in group['figures']:
                grouped.append(figure_id)
                if figure_id not in figures:
                    errors.append('分组引用不存在的范例: ' + figure_id)
                elif figures[figure_id]['category'] != category:
                    errors.append('分组与原分类不一致: ' + figure_id)
    if sorted(grouped) != sorted(figures):
        errors.append('每个 teaser / architecture 必须且只能出现在一个用途分组中')
    for group in config['same_paper']:
        if len(set(group)) < 2:
            errors.append('同论文关联至少需要两个不同范例')
        for figure_id in group:
            if figure_id not in figures:
                errors.append('同论文关联引用不存在的范例: ' + figure_id)
    if set(config['suggested_elements']) != set(figures):
        errors.append('每个范例必须有现有元素关联记录')
    for figure_id, ids in config['suggested_elements'].items():
        for element_id in ids:
            if element_id not in elements:
                errors.append(figure_id + ': 元素不存在: ' + element_id)
        if len(ids) != len(set(ids)):
            errors.append(figure_id + ': 重复元素关联')
    if errors:
        raise ValueError('\n'.join(errors))
    return figures, elements, config


def related(figures, elements, config):
    pairs = {key: [] for key in figures}
    extracted = {key: [] for key in figures}
    reverse = {key: [] for key in elements}
    for group in config['same_paper']:
        for key in group:
            pairs[key].extend(other for other in group if other != key)
    for figure_id, figure in figures.items():
        prefix = figure['_relative_folder'] + '/'
        for element_id, element in elements.items():
            source = element['source']
            if source.get('kind') != 'extracted-existing-vectors':
                continue
            if any(source.get(field, '').startswith(prefix) for field in ('local_original', 'native_original')):
                extracted[figure_id].append(element_id)
        ids = list(dict.fromkeys(extracted[figure_id] + config['suggested_elements'][figure_id]))
        for element_id in ids:
            reverse[element_id].append(figure_id)
    return pairs, extracted, reverse


def element_links(root, page, ids, elements):
    return ' · '.join(link(page, elements[key]['title_zh'], root / elements[key]['svg_path']) for key in ids)


def figure_links(page, ids, figures):
    return ' · '.join(link(page, figures[key]['title'], figures[key]['_folder'] / 'README.md') for key in ids)


def nav(root, page):
    return ' · '.join(link(page, title, root / target) for title, target in (
        ('Teaser', 'teaser/README.md'),
        ('Architecture', 'architecture/README.md'),
        ('Element', 'element/README.md'),
        ('总目录', 'CATALOG.md'),
    ))


def build(root, figures, elements, config):
    pairs, extracted, reverse = related(figures, elements, config)
    for figure_id, figure in figures.items():
        page = figure['_folder'] / 'README.md'
        body = page.read_text(encoding='utf-8')
        body = re.sub(re.escape(MARKER) + r'.*?' + re.escape(END_MARKER) + r'\s*', '', body, flags=re.S)
        body = re.sub(r'^\[顶会精选图文目录\].*\n\n', '', body, flags=re.M)
        heading, rest = body.split('\n', 1)
        # The nav block is regenerated instead of duplicated on subsequent builds.
        rest = re.sub(r'^\s*<!-- CATEGORY NAV -->.*?<!-- END CATEGORY NAV -->\s*', '', rest, flags=re.S)
        body = heading + '\n\n<!-- CATEGORY NAV -->\n' + nav(root, page) + '\n<!-- END CATEGORY NAV -->\n\n' + rest.lstrip()
        lines = [MARKER, '## 关联范例与元素', '']
        if pairs[figure_id]:
            lines += ['同论文的其他图：' + figure_links(page, pairs[figure_id], figures), '']
        if extracted[figure_id]:
            lines += ['**从本图拆出的部件：** ' + element_links(root, page, extracted[figure_id], elements), '']
        suggested = [key for key in config['suggested_elements'][figure_id] if key not in extracted[figure_id]]
        if suggested:
            lines += ['**可搭配的现有元素：** ' + element_links(root, page, suggested, elements), '',
                      '这些元素按表达功能关联，并非从本论文原图拆出；来源和许可仍以各元素记录为准。', '']
        lines += [link(page, '范例与元素对照表', root / 'element/with-examples.md') + ' · ' +
                  link(page, '元素分类目录', root / 'element/README.md'), END_MARKER]
        page.write_text(body.rstrip() + '\n\n' + '\n'.join(lines) + '\n', encoding='utf-8')

    for category, groups in config['groups'].items():
        folder = root / ('teaser' if category == 'teaser' else 'architecture')
        page = folder / 'README.md'
        title = 'Teaser 范例' if category == 'teaser' else 'Architecture 范例'
        lines = ['# ' + title, '', nav(root, page), '',
                 '按图的表达用途浏览。会议、期刊、年份及综述类型保留在条目标签中。', '',
                 '| 表达用途 | 数量 | 入口 |', '|---|---:|---|']
        for group in groups:
            lines.append('| ' + group['title'] + ' | ' + str(len(group['figures'])) + ' | [浏览](#' + group['id'] + ') |')
        for group in groups:
            lines += ['', '<a id="' + group['id'] + '"></a>', '', '## ' + group['title'], '']
            if group.get('description'):
                lines += [group['description'], '']
            for figure_id in group['figures']:
                figure = figures[figure_id]
                detail = figure['_folder'] / 'README.md'
                lines += ['### ' + link(page, figure['title'], detail), '', figure.get('summary', ''), '']
                publication = figure.get('publication')
                if publication:
                    label = publication['venue'] + ' ' + str(publication['year']) + ' · ' + {'oral': 'Oral', 'poster': 'Poster', 'journal-article': '期刊论文', 'preprint': '预印本', 'survey-report': 'STAR 报告'}.get(publication['presentation'], '会议论文；未核实 Oral')
                    if publication.get('article_type') == 'survey':
                        label += ' · 综述'
                    lines += [label, '']
                layout = figure.get('curation', {}).get('panel_layout')
                if layout:
                    lines += ['**子图组织：** ' + layout['summary'] + ' 原论文 Figure ' + str(figure['source']['figure_number']) + '。', '']
                if figure.get('editability', {}).get('level') == 'raster-reference':
                    lines += ['**整图位图，仅构图参考。**', '']
                lines += ['[![预览](' + relative(page, figure['_folder'] / figure['preview']) + ')](' + relative(page, detail) + ')', '']
                refs = [link(page, '说明与源文件', detail)]
                refs += [link(page, '同论文：' + figures[key]['title'], figures[key]['_folder'] / 'README.md') for key in pairs[figure_id]]
                refs += ['[关联元素](' + relative(page, detail) + '#关联范例与元素)']
                lines += [' · '.join(refs), '']
        if category == 'architecture':
            lines += ['## 版式辅助', '', link(page, '原生 AI / AIT 版式母版', root / 'templates/layouts/README.md') + '，作为辅助素材单独计数。', '']
        page.write_text('\n'.join(lines).rstrip() + '\n', encoding='utf-8')

    page = root / 'element/with-examples.md'
    lines = ['# 范例与元素对照', '', nav(root, page), '',
             '由 teaser 看表达思路，由 architecture 看信息流，再沿下列链接选元素。只有来源记录指向该原图的条目，才标作原图拆件。', '',
             '## 从原图拆出的部件', '', '| 原图 | 已有独立元素 |', '|---|---|']
    for key, ids in extracted.items():
        if ids:
            lines.append('| ' + figure_links(page, [key], figures) + ' | ' + element_links(root, page, ids, elements) + ' |')
    lines += ['', '## 按范例找可搭配元素', '',
              '本节是表达功能的对应关系，**不表示元素出自所列论文**。各元素保留自己的作者和许可。', '']
    for category, groups in config['groups'].items():
        lines += ['### ' + ('Teaser' if category == 'teaser' else 'Architecture'), '', '| 范例 | 现有元素 |', '|---|---|']
        for group in groups:
            for key in group['figures']:
                lines.append('| ' + figure_links(page, [key], figures) + ' | ' + element_links(root, page, config['suggested_elements'][key], elements) + ' |')
        lines.append('')
    page.write_text('\n'.join(lines).rstrip() + '\n', encoding='utf-8')
    return reverse
