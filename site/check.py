"""Deterministic checks for the wiki + built site. Exit 1 on any ERROR."""
import os,re,glob,sys,urllib.request
R=os.path.dirname(os.path.dirname(os.path.abspath(__file__))); D=R+'/site/dist'; err=0
stems={os.path.basename(f)[:-3] for f in glob.glob(R+'/**/*.md',recursive=True) if '/site/' not in f}
for f in glob.glob(R+'/**/*.md',recursive=True):
    if '/site/' in f or '/raw/' in f: continue
    for t in re.findall(r'\[\[([^\]|]+)',open(f).read()):
        if t.strip() not in stems: print('WARN unresolved wikilink',os.path.relpath(f,R),t)
for f in glob.glob(D+'/*.html'):
    for h in re.findall(r'href="([^"#:]+\.html)"',open(f).read()):
        if not os.path.exists(os.path.join(D,h)): print('ERROR broken local link',os.path.basename(f),h); err+=1
p=open(R+'/entities/michael-levin.md').read()
for u in sorted(set(re.findall(r'\((https?://[^)\s]+)\)',p))):
    try:
        req=urllib.request.Request(u,headers={'User-Agent':'Mozilla/5.0'}); c=urllib.request.urlopen(req,timeout=20).status
    except Exception as e: c=getattr(e,'code',str(e))
    tag='OK' if c==200 else ('WARN' if c in (403,406,429) else 'ERROR')
    if tag=='ERROR': err+=1
    print(tag,c,u)
for w in ['Anthropot','respcecify']:
    if w in p: print('ERROR typo',w); err+=1
# privacy: no personal name on the public site
for f in glob.glob(D+'/**/*',recursive=True):
    if os.path.isfile(f) and f.endswith(('.html','.css','.js')) and re.search(r'(?i)fotios|mpouris',open(f,errors='ignore').read()):
        print('ERROR private name in',os.path.relpath(f,D)); err+=1
if os.path.exists(D+'/vision.html'): print('ERROR vision.html shipped'); err+=1
# feed integrity + links
import json
fd=json.load(open(R+'/feed/latest.json'))
for it in fd['items']:
    if not (it.get('date') and it.get('url') and it.get('kind') in ('video','paper','post','blog') and it.get('title')): print('ERROR bad feed item',it); err+=1
    if re.match(r'\d{4}-\d{2}-\d{2}$',it['date']) and it['date']>fd['updated']: print('ERROR future-dated item',it['url']); err+=1
if '--links' in sys.argv:
    for it in fd['items']:
        u=it['url']
        if u.startswith('https://doi.org/'):  # publishers block bots: verify the DOI is registered instead
            j=json.load(urllib.request.urlopen('https://doi.org/api/handles/'+u[16:],timeout=20)); c=200 if j.get('responseCode')==1 else 404
            print('feed','OK' if c==200 else 'ERROR','doi-registered' if c==200 else 'doi-missing',u); err+=c!=200; continue
        for _ in range(3):
            try: c=urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':'Mozilla/5.0'}),timeout=20).status
            except Exception as e: c=getattr(e,'code',str(e))
            if c==200 or c in (403,404,406,429): break
        tag='OK' if c==200 else ('WARN' if c in (403,406,429) else 'ERROR')
        if tag=='ERROR': err+=1
        print('feed',tag,c,u)
print('ERRORS',err); sys.exit(1 if err else 0)
