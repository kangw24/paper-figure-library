#!/usr/bin/env python3
"""Download pinned external sources without altering or executing their contents."""
import argparse,concurrent.futures,hashlib,json
from pathlib import Path
from urllib.request import Request,urlopen

def main():
 p=argparse.ArgumentParser(description=__doc__)
 p.add_argument('--manifest',type=Path,default=Path('sources/expansion-2026-10-25.json'))
 p.add_argument('--out',type=Path,required=True)
 args=p.parse_args();out=args.out.resolve();raw=json.loads(args.manifest.read_text())
 records=raw['downloads'] if isinstance(raw,dict) else raw
 def fetch(item):
  target=(out/item['file']).resolve()
  if not target.is_relative_to(out):raise ValueError('Source path escapes output directory')
  with urlopen(Request(item['url'],headers={'User-Agent':'PaperFigureLibrary/1.0'}),timeout=45) as response:data=response.read(50*1024*1024)
  if item.get('sha256') and hashlib.sha256(data).hexdigest()!=item['sha256']:raise ValueError('SHA256 mismatch: '+item['file'])
  if item.get('blob_sha') and hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()!=item['blob_sha']:raise ValueError('Upstream Git blob mismatch')
  target.parent.mkdir(parents=True,exist_ok=True);target.write_bytes(data);return item['file']
 with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
  for i,_ in enumerate(pool.map(fetch,records),1):
   if i%25==0 or i==len(records):print(str(i)+' / '+str(len(records)))
if __name__=='__main__':main()
