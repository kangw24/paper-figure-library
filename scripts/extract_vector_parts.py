#!/usr/bin/env python3
"""Copy recorded author SVG nodes and keep only their referenced definitions."""
import copy,hashlib,json,re
from pathlib import Path
import xml.etree.ElementTree as E
NS='http://www.w3.org/2000/svg';E.register_namespace('',NS);E.register_namespace('xlink','http://www.w3.org/1999/xlink')
DRAWABLE={'path','use','rect','circle','ellipse','line','polyline','polygon','image','text'}
def tag(node):return node.tag.rsplit('}',1)[-1]
def refs(node):
 found=set()
 for n in node.iter():
  for key,value in n.attrib.items():
   if key.rsplit('}',1)[-1]=='href' and value.startswith('#'):found.add(value[1:])
   found.update(re.findall(r'url\(#([^)]*)\)',value))
 return found
def extract(root):
 manifest=json.loads((root/'element/vector-parts.json').read_text())
 for spec in manifest['specs']:
  data=(root/spec['source_file']).read_bytes();assert hashlib.sha256(data).hexdigest()==spec['source_sha256'],spec['id']
  source=E.fromstring(data);selected={tuple(p) for p in spec['selected_node_paths']};out=copy.deepcopy(source)
  def prune(node,path=()):
   if tag(node)=='defs':return True
   if tag(node) in DRAWABLE:return path in selected
   for i,child in enumerate(list(node)):
    if not prune(child,path+(i,)):node.remove(child)
   return bool(len(node)) or node is out
  prune(out)
  definitions=[n for n in out.iter() if tag(n)=='defs'];index={n.get('id'):n for d in definitions for n in d.iter() if n.get('id')}
  needed=set()
  for node in out:
   if tag(node)!='defs':needed.update(refs(node))
  pending=list(needed)
  while pending:
   key=pending.pop()
   if key not in index:continue
   for ref in refs(index[key])-needed:needed.add(ref);pending.append(ref)
  def prune_defs(node):
   if node.get('id') in needed:return True
   for child in list(node):
    if not prune_defs(child):node.remove(child)
   return bool(len(node))
  for definition in definitions:prune_defs(definition)
  box=spec['viewBox'];out.set('viewBox',' '.join(map(str,box)));out.set('width',str(box[2]));out.set('height',str(box[3]))
  path=root/'element/svg'/(spec['id']+'.svg');E.ElementTree(out).write(path,encoding='utf-8',xml_declaration=True)
  print(spec['id'],len(selected),'nodes',path.stat().st_size,'bytes')
if __name__=='__main__':extract(Path(__file__).resolve().parents[1])
