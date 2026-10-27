#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Rebuild source-backed catalogs and GitHub browsing pages."""
import argparse,html,json,re
from pathlib import Path
from validate_library import ROOT,validate
from build_links import load as load_links,build as build_links,figure_links

SECTIONS=[('teaser','teaser','Teaser 范例'),('architecture','architecture','Architecture 范例'),('mechanism','references/mechanisms','机制参考图'),('layout-template','templates/layouts','原生版式模板')]
LABELS={'modules':'网络与模块','data':'数据与文档','operations':'运算与变换','connections':'箭头与连接','training':'训练与标记','devices':'设备与对象','science':'科学与图表','concepts':'概念符号'}
KINDS={'paper-example':'论文范例','tutorial-example':'教材或教程范例','template':'原生模板'}
def write(root,path,text):
 p=root/path;p.parent.mkdir(parents=True,exist_ok=True);p.write_text(text.rstrip()+'\n',encoding='utf-8')
def publication_line(x):
 p=x.get('publication')
 if not p:return ''
 label=p['venue']+' '+str(p['year'])+' · '+{'oral':'Oral','poster':'Poster'}.get(p.get('presentation'),'会议论文，未核实 Oral')
 level=x.get('editability',{}).get('level')
 label+=' · '+{'vector':'矢量结构','vector-and-raster':'矢量 + 原有位图','raster-reference':'整图位图，仅构图参考'}.get(level,'')
 return label.rstrip(' ·')
def build(root):
 examples=[]
 for category,folder,label in SECTIONS:
  lines=['# '+label,'','[回到总目录](../../CATALOG.md)','']
  for path in sorted((root/folder).glob('*/metadata.json')):
   x=json.loads(path.read_text());base=path.parent.relative_to(root).as_posix();x.update(path=base,metadata_path=base+'/metadata.json',readme_path=base+'/README.md',primary_path=base+'/'+x['primary_file'],preview_path=base+'/'+x['preview']);examples.append(x)
   lines+=['## ['+x['title']+']('+x['id']+'/README.md)','','**'+KINDS[x['kind']]+'** · '+x['summary']+('\n\n'+publication_line(x) if publication_line(x) else ''),'','[![预览]('+x['id']+'/'+x['preview']+')]('+x['id']+'/'+x['primary_file']+')','']
  write(root,Path(folder)/'README.md','\n'.join(lines))
 elements=json.loads((root/'element/catalog.json').read_text())['items'];normalized=[]
 for x in elements:normalized.append({**x,'title':x['title_zh'],'category':'element','element_category':x['category'],'kind':'external-element','formats':['svg'],'primary_path':x['svg_path']})
 counts={c:sum(x['category']==c for x in examples+normalized) for c in ['teaser','architecture','element','mechanism','layout-template']}
 figures,element_map,relationships=load_links(root)
 reverse=build_links(root,figures,element_map,relationships)
 readme=root/'README.md'
 if readme.exists():
  content=readme.read_text(encoding='utf-8')
  label='**'+str(counts['teaser'])+' 个 teaser · '+str(counts['architecture'])+' 个 architecture · '+str(counts['element'])+' 个独立 element**'
  content=re.sub(r'\*\*\d+ 个 teaser · \d+ 个 architecture · \d+ 个独立 element\*\*',lambda _:label,content)
  write(root,Path('README.md'),content)
 write(root,Path('catalog.json'),json.dumps({'schema_version':2,'counts':counts,'items':examples+normalized},ensure_ascii=False,indent=2))
 lines=['# 素材总目录','','[Teaser](teaser/README.md) · [Architecture](architecture/README.md) · [Element](element/README.md) · [仓库首页](README.md) · [JSON 来源索引](catalog.json)','','按图的用途分类，会议、年份与 Oral 仅作为条目标签。完整范例与最小元素通过 [Markdown 对照表](element/with-examples.md) 互相连接。','','| 类别 | 数量 | 入口 |','|---|---:|---|']
 for c,f,l in SECTIONS:
  if c in ('teaser','architecture'):lines.append('| '+l+' | '+str(counts[c])+' | [浏览]('+f+'/README.md) |')
 lines+=['| Element 最小可复用元素 | '+str(counts['element'])+' | [按内容与来源浏览](element/README.md) |','','完整机制参考由 Element 页链接，版式母版由 Architecture 页链接，均单独计数。','']
 for c,f,l in SECTIONS:
  if c not in ('teaser','architecture'):continue
  lines+=['## '+l,'']
  if c=='architecture':lines+=['辅助入口：[原生 AI / AIT 版式母版](templates/layouts/README.md)。','']
  for x in examples:
   if x['category']!=c:continue
   lines+=['### ['+x['title']+']('+x['readme_path']+')','',x['summary']+('\n\n'+publication_line(x) if publication_line(x) else ''),'','[<img src="'+x['preview_path']+'" width="760" alt="'+html.escape(x['title'],quote=True)+'">]('+x['primary_path']+')','','来源类型：'+KINDS[x['kind']]+'。许可：'+x['license']['name']+'。','[原文件]('+x['primary_path']+') · [来源记录]('+x['metadata_path']+')','']
 lines+=['## Element','','[![元素选览](element/preview.png)](element/README.md)','','[元素分类目录](element/README.md) · [范例与元素对照表](element/with-examples.md) · [离线检索](element/gallery.html)','','辅助入口：[完整机制参考](references/mechanisms/README.md)。这些完整机制图不计入最小元素数量。','']
 write(root,Path('CATALOG.md'),'\n'.join(lines))
 lines=['# Element · 元素库','','[Teaser](../teaser/README.md) · [Architecture](../architecture/README.md) · [总目录](../CATALOG.md)','','**'+str(len(elements))+' 个独立 SVG**，全部为外部下载或现有原图节点的提取。','','[范例与元素对照表](with-examples.md)：从完整范例找部件，也可从各元素分类页反查关联范例。原图拆件与功能关联分别标明。','','[离线搜索与筛选](gallery.html)（下载仓库后直接打开） · [完整总览 SVG](all-elements.svg) · [逐项来源、许可与署名](catalog.json)','','![元素选览](preview.png)','','## 按内容浏览','','| 分类 | 数量 | 入口 |','|---|---:|---|']
 if (root/'element/vector-parts.json').is_file():
  lines[lines.index('## 按内容浏览'):lines.index('## 按内容浏览')]=['## 论文原图网络部件','','[![DiT、ViT、SD3 原图部件](overviews/paper-parts.png)](overviews/paper-parts.svg)','','注意力、嵌入、归一化、前馈、残差与条件调制等独立节点，保留各自原图及精确提取记录。','']
 for c,l in LABELS.items():
  xs=[x for x in elements if x['category']==c]
  if not xs:continue
  lines.append('| '+l+' | '+str(len(xs))+' | [图文目录](by-category/'+c+'.md) |')
  page=root/'element/by-category'/(c+'.md')
  detail=['# '+l,'','[返回 Element](../README.md) · [Teaser](../../teaser/README.md) · [Architecture](../../architecture/README.md) · [范例与元素对照表](../with-examples.md)','','关联范例按表达功能互链；是否为原图拆件见对照表与元素来源记录。','','| 预览 | 名称与 SVG | 来源与许可 | 关联范例（最多列三项） |','|---|---|---|---|']
  for x in xs:detail.append('| <img src="../../'+x['preview_path']+'" width="140"> | ['+x['title_zh']+'](../../'+x['svg_path']+') | '+x.get('collection',x['source'].get('author',x['source']['kind']))+' · '+x['license']['name']+' | '+(figure_links(page,reverse[x['id']][:3],figures) or '—')+' |')
  write(root,Path('element/by-category')/(c+'.md'),'\n'.join(detail))
 lines+=['','## 按来源浏览','','| 来源 | 数量 | 说明 |','|---|---:|---|']
 sources={}
 for x in elements:sources.setdefault(x.get('collection','原有作者图元'),[]).append(x)
 for i,(name,xs) in enumerate(sources.items()):
  slug='source-'+str(i+1);lines.append('| ['+name+'](by-source/'+slug+'.md) | '+str(len(xs))+' | 保留作者原图或精确提取位置 |')
  detail=['# '+name,'','[返回元素库](../README.md)','','| 预览 | 名称 | 原来源 |','|---|---|---|']
  for x in xs:detail.append('| <img src="../../'+x['preview_path']+'" width="140"> | ['+x['title_zh']+'](../../'+x['svg_path']+') | [出处]('+x['source']['urls'][-1]+') · '+x['license']['name']+' |')
  write(root,Path('element/by-source')/(slug+'.md'),'\n'.join(detail))
 lines+=['','原始下载件不改色、不重画。AI 教程、RUST 等未明确单独图形授权的部件保留为参考，其他素材逐项保留 CC0、CC BY、MIT 等原许可。','完整的卷积、池化与注意力机制图见 [机制参考目录](../references/mechanisms/README.md)，不混入本页的最小元素计数。']
 write(root,Path('element/README.md'),'\n'.join(lines))
 from build_browsing import build as browsing
 browsing(root,elements,LABELS)
 return counts
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--root',type=Path,default=ROOT);root=p.parse_args().root.resolve();errors,_=validate(root)
 if errors:raise SystemExit('\n'.join(errors))
 print('Rebuilt catalog:',build(root))
