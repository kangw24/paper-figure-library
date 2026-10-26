#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Arrange existing SVG objects and create an offline element browser."""
import copy,json,math,re
from pathlib import Path
import xml.etree.ElementTree as E
NS='http://www.w3.org/2000/svg';E.register_namespace('',NS);E.register_namespace('xlink','http://www.w3.org/1999/xlink')
def compose(root,items,path,cols=6):
 height=max(1,math.ceil(len(items)/cols))*200
 out=E.Element('{'+NS+'}svg',{'viewBox':'0 0 '+str(cols*240)+' '+str(height),'width':str(cols*240),'height':str(height)})
 for i,item in enumerate(items):
  node=copy.deepcopy(E.parse(root/item['svg_path']).getroot());prefix=item['id']+'-';ids={n.get('id'):prefix+n.get('id') for n in node.iter() if n.get('id')};classes={v:prefix+v for n in node.iter() for v in n.get('class','').split()}
  def refs(v):
   if 'url(' not in v:return v
   def remap(match):
    name=match.group(1).strip(chr(34)+chr(39)+' ').lstrip('#')
    return 'url(#'+ids.get(name,name)+')'
   return re.sub(r'url\(([^)]+)\)',remap,v)
  for n in node.iter():
   for k,v in list(n.attrib.items()):
    if k=='id':v=ids[v]
    elif k=='class':v=' '.join(classes[v] for v in v.split())
    else:
     v=refs(v)
     if k.rsplit('}',1)[-1]=='href' and v.startswith('#'):v='#'+ids.get(v[1:],v[1:])
    n.set(k,v)
   if n.tag.rsplit('}',1)[-1]=='style' and n.text:
    n.text=refs(n.text)
    for old,new in classes.items():n.text=re.sub(r'\.'+re.escape(old)+r'\b','.'+new,n.text)
  x=i%cols*240+10;y=i//cols*200+5;node.set('x',str(x));node.set('y',str(y));node.set('width','220');node.set('height','160');out.append(node)
  label=E.SubElement(out,'{'+NS+'}text',{'x':str(x),'y':str(y+180),'font-family':'Arial, sans-serif','font-size':'10','fill':'#222'});label.text=item['id']
 path.parent.mkdir(parents=True,exist_ok=True);E.ElementTree(out).write(path,encoding='utf-8',xml_declaration=True)
 path.write_text('\n'.join(line.rstrip() for line in path.read_text().splitlines())+'\n',encoding='utf-8')
def build(root,items,labels):
 compose(root,items,root/'elements/all-elements.svg')
 for category in labels:
  xs=[x for x in items if x['category']==category]
  if xs:compose(root,xs,root/'elements/overviews'/(category+'.svg'))
 data=[]
 for x in items:data.append({'id':x['id'],'name':x['title_zh'],'en':x.get('title_en',''),'category':x['category'],'collection':x.get('collection','原有作者图元'),'svg':x['svg_path'].removeprefix('elements/'),'preview':x['preview_path'].removeprefix('elements/'),'source':x['source']['urls'][-1],'license':x['license']['name'],'tags':x.get('tags',[]),'attribution':x.get('attribution',x['rights'])})
 payload=json.dumps({'items':data,'labels':labels},ensure_ascii=False).replace('</','<\\/')
 page='''<!doctype html><html lang="zh-CN"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Paper Figure Library · 元素检索</title><style>body{margin:0;font:15px system-ui,sans-serif;background:#f5f6f8;color:#17202d}header{position:sticky;top:0;background:#fffefb;z-index:1;padding:22px 4vw;border-bottom:1px solid #ddd}h1{margin:0 0 8px;font-size:26px}p{color:#526171;margin:6px 0}input,select{padding:11px;border:1px solid #bdc8cf;border-radius:6px;font:inherit;margin:12px 8px 0 0}input{width:min(480px,70vw)}main{padding:24px 4vw;display:grid;grid-template-columns:repeat(auto-fill,minmax(230px,1fr));gap:18px}article{background:white;border:1px solid #dbe0e4;border-radius:8px;padding:16px;display:flex;flex-direction:column;gap:9px}article img{width:100%;height:150px;object-fit:contain}a{color:#235f9a}small{color:#536473;overflow-wrap:anywhere}h2{font-size:17px;margin:2px 0}.links{display:flex;gap:20px}#count{font-weight:600;margin-top:10px}.empty{grid-column:1/-1;padding:40px;text-align:center}</style><header><h1>论文配图 · 元素检索</h1><p>作者原始素材与原图提取部件。下载仓库后可离线使用；每项保留来源、许可和独立 SVG。</p><input id="q" aria-label="搜索" placeholder="搜索中文、英文、模块名，例如 GPU / 张量 / attention"><select id="cat" aria-label="内容分类"><option value="">全部分类</option></select><select id="source" aria-label="素材来源"><option value="">全部来源</option></select><div id="count"></div></header><main id="grid"></main><script id="data" type="application/json">__PAYLOAD__</script><script>
const data=JSON.parse(document.getElementById('data').textContent),items=data.items,q=document.getElementById('q'),cat=document.getElementById('cat'),source=document.getElementById('source'),grid=document.getElementById('grid');
function option(parent,value,label){const o=document.createElement('option');o.value=value;o.textContent=label;parent.append(o)}
for(const c of [...new Set(items.map(x=>x.category))])option(cat,c,data.labels[c]||c);
for(const s of [...new Set(items.map(x=>x.collection))])option(source,s,s);
function draw(){const needle=q.value.trim().toLowerCase(),xs=items.filter(x=>(!cat.value||x.category===cat.value)&&(!source.value||x.collection===source.value)&&(!needle||[x.name,x.en,x.id,...x.tags].join(' ').toLowerCase().includes(needle)));document.getElementById('count').textContent='显示 '+xs.length+' / '+items.length+' 个元素';grid.replaceChildren();
for(const x of xs){const card=document.createElement('article'),img=document.createElement('img'),title=document.createElement('h2'),desc=document.createElement('small'),links=document.createElement('div');img.src=x.preview;img.alt=x.name;img.loading='lazy';title.textContent=x.name;desc.textContent=x.collection+' · '+x.license;links.className='links';for(const [label,url] of [['下载 SVG',x.svg],['原出处',x.source]]){const a=document.createElement('a');a.textContent=label;a.href=url;if(label==='下载 SVG')a.download=x.id+'.svg';else{a.target='_blank';a.rel='noopener noreferrer'}links.append(a)}card.append(img,title,desc,links);grid.append(card)}if(!xs.length){const n=document.createElement('div');n.className='empty';n.textContent='没有匹配的元素。试试英文原名或清除筛选。';grid.append(n)}}
q.addEventListener('input',draw);cat.addEventListener('change',draw);source.addEventListener('change',draw);draw();
</script></html>'''
 (root/'elements/gallery.html').write_text(page.replace('__PAYLOAD__',payload),encoding='utf-8')
