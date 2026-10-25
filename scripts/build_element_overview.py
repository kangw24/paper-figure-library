#!/usr/bin/env python3
"""Arrange existing SVG components for browsing, preserving their geometry."""
import copy
import json
from pathlib import Path
import re
import xml.etree.ElementTree as ET

ROOT=Path(__file__).resolve().parents[1]
NS='http://www.w3.org/2000/svg'
ET.register_namespace('',NS)
ET.register_namespace('xlink','http://www.w3.org/1999/xlink')
items=json.loads((ROOT/'elements/catalog.json').read_text())['items']
out=ET.Element('{'+NS+'}svg',{'viewBox':'0 0 1440 1040','width':'1440','height':'1040'})
for i,item in enumerate(items):
    node=copy.deepcopy(ET.parse(ROOT/item['svg_path']).getroot())
    prefix=item['id']+'-'
    ids={n.get('id'):prefix+n.get('id') for n in node.iter() if n.get('id')}
    classes={c:prefix+c for n in node.iter() for c in n.get('class','').split()}
    for n in node.iter():
        for k,v in list(n.attrib.items()):
            if k=='id':v=ids[v]
            elif k=='class':v=' '.join(classes[c] for c in v.split())
            else:
                for old,new in ids.items():v=v.replace('url(#'+old+')','url(#'+new+')')
                if k.rsplit('}',1)[-1]=='href' and v.startswith('#'):v='#'+ids.get(v[1:],v[1:])
            n.set(k,v)
        if n.tag.rsplit('}',1)[-1]=='style' and n.text:
            for old,new in classes.items():n.text=re.sub(r'\.'+re.escape(old)+r'\b','.'+new,n.text)
    x=(i%4)*360+15;y=(i//4)*260+15
    node.set('x',str(x));node.set('y',str(y));node.set('width','330');node.set('height','200')
    out.append(node)
    label=ET.SubElement(out,'{'+NS+'}text',{'x':str(x),'y':str(y+225),'font-family':'Arial, sans-serif','font-size':'12','fill':'#222222'})
    label.text=item['id']
ET.ElementTree(out).write(ROOT/'elements/all-elements.svg',encoding='utf-8',xml_declaration=True)
print('Arranged 16 existing components; only labels and layout were added.')
