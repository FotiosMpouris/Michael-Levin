"""Build the public static site from the wiki markdown. Usage: python3 site/build.py -> site/dist/"""
import os, re, glob, html, shutil, markdown
R=os.path.dirname(os.path.dirname(os.path.abspath(__file__))); D=os.path.join(R,'site','dist')
shutil.rmtree(D,ignore_errors=True); os.makedirs(D)
files=[f for f in glob.glob(R+'/**/*.md',recursive=True) if '/site/' not in f and '/raw/' not in f and os.path.basename(f) not in ('SCHEMA.md','log.md','README.md')]
name={os.path.basename(f)[:-3]:f for f in files}
def out(stem): return 'index.html' if stem=='index' else stem+'.html'
def title_of(txt,stem):
    m=re.search(r'^title:\s*"?(.*?)"?\s*$',txt,re.M); return m.group(1) if m else stem.replace('-',' ').title()
titles={}
for s,f in name.items(): titles[s]=title_of(open(f).read(),s)
CSS='''body{font:17px/1.65 Georgia,serif;color:#1c1c1c;background:#fbfaf7;margin:0}
header{background:#0d1b2a;color:#e8eef5;padding:14px 24px}header a{color:#9fd3ff;margin-right:18px;text-decoration:none;font-family:system-ui,sans-serif;font-size:15px}
header strong{margin-right:28px;font-family:system-ui,sans-serif}main{max-width:820px;margin:0 auto;padding:24px}
h1,h2,h3{font-family:system-ui,sans-serif;color:#0d1b2a}a{color:#0a58a8}blockquote{border-left:3px solid #3a7bd5;margin:14px 0;padding:4px 14px;background:#eef4fb}
table{border-collapse:collapse;font-size:14px;display:block;overflow-x:auto}td,th{border:1px solid #ccd;padding:6px 8px;vertical-align:top}th{background:#e8eef5}
.meta{font-size:13px;color:#667;font-family:system-ui,sans-serif}footer{max-width:820px;margin:30px auto;padding:0 24px 30px;font-size:13px;color:#667;font-family:system-ui,sans-serif}'''
NAV='<header><strong>Michael Levin Research Wiki</strong><a href="index.html">Index</a><a href="whats-new.html">What\'s new</a><a href="companies-tracker.html">Companies</a><a href="vision.html">Why it matters</a></header>'
def link(m):
    t,_,label=m.group(1).partition('|'); t=t.strip()
    if t in name: return f'[{label or titles[t]}]({out(t)})'
    return label or t
for s,f in name.items():
    txt=open(f).read()
    body=re.sub(r'^---\n.*?\n---\n','',txt,flags=re.S)
    body=re.sub(r'\[\[([^\]]+)\]\]',link,body)
    body=re.sub(r'\s*\^\[[^\]]*\]','',body)
    h=markdown.markdown(body,extensions=['tables'])
    page=f'<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{html.escape(titles[s])} — Michael Levin Research Wiki</title><style>{CSS}</style></head><body>{NAV}<main>{h}</main><footer>An independent research wiki tracking the work of Michael Levin and his lab (Tufts University). Not affiliated with Levin or Tufts. Quotes are taken word for word from YouTube auto-captions; summaries are our own. Nothing here is investment or medical advice. Source: <a href="https://github.com/FotiosMpouris/Michael-Levin">github.com/FotiosMpouris/Michael-Levin</a></footer></body></html>'
    open(os.path.join(D,out(s)),'w').write(page)
print(len(name),'pages ->',D)
