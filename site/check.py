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
print('ERRORS',err); sys.exit(1 if err else 0)
