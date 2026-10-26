#!/usr/bin/env python3
"""Reproduce existing-node SVG extractions without drawing new geometry."""
import copy
import hashlib
import json
from pathlib import Path
import xml.etree.ElementTree as ET

ROOT=Path(__file__).resolve().parents[1]
NS='http://www.w3.org/2000/svg'
ET.register_namespace('',NS)
ET.register_namespace('xlink','http://www.w3.org/1999/xlink')
for spec in json.loads((ROOT/'elements/extraction-specs.json').read_text())['specs']:
    source=ROOT/spec['source']
    assert hashlib.sha256(source.read_bytes()).hexdigest()==spec['source_sha256'],source
    parent=ET.parse(source).getroot()
    for index in spec['parent_child_indices']:parent=parent[index]
    box=spec['viewBox']
    out=ET.Element('{'+NS+'}svg',{'viewBox':' '.join(map(str,box)),'width':str(box[2]),'height':str(box[3])})
    for index in spec['selected_child_indices']:out.append(copy.deepcopy(parent[index]))
    for node in out.iter():
        if node.get('id')=='Layer-1':node.attrib.pop('id')
    ET.ElementTree(out).write(ROOT/'elements/svg'/(spec['id']+'.svg'),encoding='utf-8',xml_declaration=True)
print('Copied existing source nodes for 11 components; no geometry generated.')

# Additional exact-node extractions from the original task5 artboard SVG export.
extra=ROOT/'elements/task5-extractions.json'
if extra.is_file():
    data=json.loads(extra.read_text())
    source=ET.parse(ROOT/data['source']).getroot()
    for spec in data['specs']:
        box=spec['viewBox']
        out=ET.Element('{'+NS+'}svg',{'viewBox':' '.join(map(str,box)),'width':str(box[2]),'height':str(box[3])})
        out.append(copy.deepcopy(source[0]))
        for chain in spec['selected_node_paths']:
            parent=out
            original=source
            for index in chain[:-1]:
                original=original[index]
                node=ET.SubElement(parent,original.tag,original.attrib)
                parent=node
            parent.append(copy.deepcopy(original[chain[-1]]))
        ET.ElementTree(out).write(ROOT/'elements/svg'/(spec['id']+'.svg'),encoding='utf-8',xml_declaration=True)
    print('Copied '+str(len(data['specs']))+' additional task5 components from recorded source node paths.')
