"""Build the public site. Usage: python3 site/build.py -> site/dist/
Home = 'Latest from Levin' feed (feed/latest.json) + topics + papers + companies + profile.
Inner pages = wiki markdown rendered as articles. Private material never ships (see EXCLUDE)."""
import os, re, glob, html, json, shutil, random, markdown, datetime
R=os.path.dirname(os.path.dirname(os.path.abspath(__file__))); D=os.path.join(R,'site','dist')
shutil.rmtree(D,ignore_errors=True); os.makedirs(D); shutil.copytree(os.path.join(R,'site','assets'),os.path.join(D,'assets'))
EXCLUDE={'SCHEMA.md','log.md','README.md','vision.md'}
files=[f for f in glob.glob(R+'/**/*.md',recursive=True) if '/site/' not in f and '/raw/' not in f and '/feed/' not in f and os.path.basename(f) not in EXCLUDE]
name={os.path.basename(f)[:-3]:f for f in files}
E=html.escape
def out(s): return 'wiki-index.html' if s=='index' else s+'.html'
def fm(txt,key):
    m=re.search(rf'^{key}:\s*"?(.*?)"?\s*$',txt,re.M); return m.group(1) if m else None
titles={s:(fm(open(f).read(),'title') or s.replace('-',' ').title()) for s,f in name.items()}
feed=json.load(open(os.path.join(R,'feed','latest.json')))
SITE='Morphospace'
LOGO='''<svg viewBox="0 0 40 40" aria-hidden="true"><defs><radialGradient id="lg" cx="35%" cy="30%"><stop offset="0" stop-color="#3ee6d0"/><stop offset=".55" stop-color="#8b7bff"/><stop offset="1" stop-color="#ff4fa3"/></radialGradient></defs><circle cx="20" cy="20" r="17" fill="url(#lg)"/><circle cx="14" cy="15" r="4" fill="#0b0f1e" opacity=".55"/><circle cx="25" cy="23" r="5" fill="#0b0f1e" opacity=".45"/><circle cx="16" cy="27" r="2.5" fill="#0b0f1e" opacity=".5"/></svg>'''
def nav(cur=''):
    L=[('index.html#latest','Latest'),('index.html#topics','Topics'),('index.html#papers','Papers'),('companies-tracker.html','Companies'),('michael-levin.html','Profile'),('wiki-index.html','All pages')]
    a=''.join(f'<a href="{h}"{" aria-current=page" if cur==t else ""}>{t}</a>' for h,t in L)
    return f'<a class="skip" href="#main">Skip to content</a><div class="wrap"><nav class="top" aria-label="Site"><a class="wm" href="index.html">{LOGO}<span>{SITE.upper()}</span></a><div class="links">{a}</div></nav></div>'
FOOT=f'''<footer><div class="wrap"><p><b>{SITE}</b> is an independent, weekly-updated tracker of the public work of Michael Levin and his lab at Tufts University. It is not affiliated with, reviewed or endorsed by Levin, his lab or Tufts.</p>
<p>Every item links to its original source: YouTube, X, thoughtforms.life, or the paper's DOI. Video quotes come from YouTube captions, and the summaries are our own. Nothing here is medical or investment advice. Feed last checked {E(feed["checked_at"])}.</p></div></footer>'''
def page(title,body,cur='',desc='A weekly tracker of Michael Levin\'s new videos, papers, posts and the companies built on his lab\'s work.'):
    return f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{E(title)}</title><meta name="description" content="{E(desc)}"><meta property="og:title" content="{E(title)}"><meta property="og:description" content="{E(desc)}"><meta name="theme-color" content="#0b0f1e"><link rel="icon" href="data:image/svg+xml,{LOGO.replace('"',"'").replace('#','%23')}"><link rel="stylesheet" href="assets/site.css"></head><body>{nav(cur)}<main id="main">{body}</main>{FOOT}</body></html>'''
def fmtdate(d):
    p=d.split('-'); M=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
    return f'{M[int(p[1])-1]} {int(p[2])}, {p[0]}' if len(p)==3 else f'{M[int(p[1])-1]} {p[0]}'
KL={'video':'Video','paper':'Paper','post':'X post','blog':'Blog'}
def card(it,i):
    k=it['kind']; extra=''
    if k=='paper': extra=f'<span class="tag{" pr" if it.get("status")=="peer-reviewed" else ""}">{"Peer-reviewed" if it.get("status")=="peer-reviewed" else "Preprint"}</span>'
    more=f'<a class="more" href="{out(it["page"])}">Read our summary →</a>' if it.get('page') and it['page'] in name else ''
    note=f'<p class="note">{E(it["note"])}</p>' if it.get('note') and k!='paper' else ''
    hid=' hidden' if i>=12 else ''
    return f'<article class="card k-{k}" data-kind="{k}"{hid}><div class="row"><span class="badge"><i></i>{KL[k]}</span><time datetime="{it["date"]}">{fmtdate(it["date"])}</time></div><h3><a href="{E(it["url"])}" rel="noopener" target="_blank">{E(it["title"])}<span class="skip"> (opens in a new tab)</span></a></h3><div class="src">{E(it["source"])} {extra}{(' · issue '+E(it['issue'])) if it.get('issue') else ''}</div>{note}{more}</article>'
def tissue():
    rnd=random.Random(7); C=['#3ee6d0','#8b7bff','#ff4fa3','#ffc24b']; s=[]
    for y in range(9):
        for x in range(9):
            cx=24+x*44+(22 if y%2 else 0); cy=24+y*40
            if (cx-200)**2+(cy-180)**2>185**2: continue
            r=12+rnd.random()*7; c=rnd.choice(C); d=round(rnd.random()*6,2)
            s.append(f'<circle cx="{cx}" cy="{cy}" r="{r:.1f}" fill="{c}" style="animation-delay:-{d}s"/>')
    return f'<svg class="tissue" viewBox="0 0 400 380" role="img" aria-label="Illustration: a sheet of cells glowing in different colors, like a voltage-dye image of bioelectric patterns">{"".join(s)}</svg>'
# ---------- home ----------
items=feed['items']; cnt={k:sum(1 for i in items if i['kind']==k) for k in KL}
chips='<button class="chip" aria-pressed="true" data-f="all">All</button>'+''.join(f'<button class="chip k-{k}" aria-pressed="false" data-f="{k}"><i></i>{KL[k]+(' posts' if k=='blog' else 's')} <span class="skip">filter</span></button>' for k in KL)
TOPIC_COL={'bioelectricity':'#3ee6d0','regeneration':'#ffc24b','cognition-in-cells':'#8b7bff','xenobots-and-anthrobots':'#ff4fa3','platonic-space-and-ingressing-minds':'#b18cff','ai-and-biology':'#49b6ff','mind-body':'#ff8a5c','control-and-energy':'#7be38b'}
tc=''
for s,c in TOPIC_COL.items():
    t=open(name[s]).read(); body=re.sub(r'^---\n.*?\n---\n','',t,flags=re.S)
    para=next(p.strip() for p in body.split('\n\n') if p.strip() and not p.strip().startswith('#'))
    para=re.sub(r'\[\[([^\]|]+)\|?([^\]]*)\]\]',lambda m:m.group(2) or m.group(1),para)
    short=para if len(para)<170 else para[:para.rfind(' ',0,165)]+'…'
    tc+=f'<a class="topic" style="--c:{c}" href="{out(s)}"><h3>{E(titles[s])}</h3><p>{E(short)}</p></a>'
newp=[i for i in items if i['kind']=='paper'][:8]
newl=''.join(f'<li><a href="{E(p["url"])}" target="_blank" rel="noopener">{E(p["title"])}</a><span class="m">{fmtdate(p["date"])} · {E(p["source"])} · {"Peer-reviewed" if p["status"]=="peer-reviewed" else "Preprint"}</span></li>' for p in newp)
LAND=[("2023","Motile Living Biobots Self-Construct from Adult Human Somatic Progenitor Seed Cells (anthrobots)","Advanced Science","10.1002/advs.202303575"),("2022","Technological Approach to Mind Everywhere (TAME)","Frontiers in Systems Neuroscience","10.3389/fnsys.2022.768201"),("2022","Wearable bioreactor drives long-term limb regeneration in adult frogs","Science Advances","10.1126/sciadv.abj2164"),("2021","Kinematic self-replication in reconfigurable organisms","PNAS","10.1073/pnas.2112672118"),("2021","Bioelectric signaling: Reprogrammable circuits underlying embryogenesis, regeneration, and cancer","Cell","10.1016/j.cell.2021.02.034"),("2020","A scalable pipeline for designing reconfigurable organisms (the first xenobots)","PNAS","10.1073/pnas.1910837117")]
landl=''.join(f'<li><a href="https://doi.org/{d}" target="_blank" rel="noopener">{E(t)}</a><span class="m">{y} · {E(j)} · Peer-reviewed</span></li>' for y,t,j,d in LAND)
COS=[("Morphoceuticals","Co-founded by Levin. Bioelectric drugs for regeneration, built on the 2022 frog-limb work."),("Fauna Systems","Co-founded with Josh Bongard. AI-designed living robots (\u201cbiobots\u201d)."),("Unravel Biosciences","Co-founded. A Wyss Institute spinout doing drug discovery for complex diseases, starting with Rett syndrome."),("Astonishing Labs","Levin is a scientific co-founder. A venture studio whose portfolio includes Anthrobots, Inc.")]
coc=''.join(f'<div class="co"><b>{E(n)}</b><p>{E(d)}</p></div>' for n,d in COS)
home=f'''<div class="wrap"><header class="hero"><div><div class="eyebrow">Updated weekly · last update {fmtdate(feed["updated"])}</div>
<h1 class="big">What's new from <em>Michael Levin's</em> lab, every week.</h1>
<p class="lede">New talks, papers, preprints and posts from the Tufts biologist who studies bioelectricity, regeneration, xenobots and minds in unexpected places. Each one is dated and linked to the source.</p>
<div class="stats"><span class="stat"><b>{cnt["video"]}</b> videos</span><span class="stat"><b>{cnt["paper"]}</b> papers</span><span class="stat"><b>{cnt["post"]}</b> X posts</span><span class="stat"><b>{cnt["blog"]}</b> blog posts</span></div></div>{tissue()}</header>
<section id="latest" aria-labelledby="h-latest"><div class="sh"><div><h2 id="h-latest">Latest from Levin</h2><p class="sub">Newest first, from YouTube, X, his blog and Crossref.</p></div><div class="chips" role="group" aria-label="Filter the feed">{chips}</div></div>
<div class="feed" id="feed">{"".join(card(it,i) for i,it in enumerate(items))}</div><button class="chip showmore" id="more" aria-pressed="false">Show all {len(items)} items</button></section>
<section id="topics" aria-labelledby="h-topics"><div class="sh"><div><h2 id="h-topics">The big ideas</h2><p class="sub">Eight threads that run through his work. Each one links the videos that cover it.</p></div></div><div class="topics">{tc}</div></section>
<section id="papers" aria-labelledby="h-papers"><div class="sh"><div><h2 id="h-papers">Papers</h2><p class="sub">Preprints have not been peer-reviewed yet. Full list on the <a href="https://drmichaellevin.org/publications/" target="_blank" rel="noopener">lab site</a>.</p></div></div>
<div class="two"><div><h3 class="col">New this season</h3><ul class="plist">{newl}</ul></div><div><h3 class="col">Landmark papers</h3><ul class="plist">{landl}</ul></div></div></section>
<section id="companies" aria-labelledby="h-co"><div class="sh"><div><h2 id="h-co">Companies</h2><p class="sub">Companies his lab site lists among his affiliations.</p></div><a class="btn ghost" href="companies-tracker.html">Full tracker, funding and sources →</a></div><div class="cos">{coc}</div>
<p class="callout">As of Oct 16, 2026, none of these companies is publicly traded. This is research, not investment advice.</p></section>
<section id="profile" aria-labelledby="h-pr"><div class="profile"><div class="pcard"><div class="eyebrow">Profile</div><h3 id="h-pr">Michael Levin</h3><ul><li>Vannevar Bush Professor and Distinguished Professor of Biology, Tufts University</li><li>Director, Allen Discovery Center at Tufts</li><li>Co-editor-in-chief, <i>Bioelectricity</i></li></ul><a class="btn" href="michael-levin.html">Full profile</a></div>
<div><h2>Follow the source</h2><ul class="plist"><li><a href="https://drmichaellevin.org/" target="_blank" rel="noopener">drmichaellevin.org</a><span class="m">Lab site: papers, preprints, software, talks</span></li><li><a href="https://www.youtube.com/@drmichaellevin" target="_blank" rel="noopener">YouTube @drmichaellevin</a><span class="m">Talks and lab discussions</span></li><li><a href="https://x.com/drmichaellevin" target="_blank" rel="noopener">X @drmichaellevin</a><span class="m">New preprints, announced first</span></li><li><a href="https://thoughtforms.life" target="_blank" rel="noopener">Forms of life, forms of mind</a><span class="m">His blog</span></li></ul></div></div></section></div>
<script>(()=>{{const cs=[...document.querySelectorAll('.chips .chip')],cards=[...document.querySelectorAll('#feed .card')],more=document.getElementById('more');let f='all',all=false;
function draw(){{let n=0;cards.forEach(c=>{{const ok=f==='all'||c.dataset.kind===f;const show=ok&&(all||f!=='all'||n<12);c.hidden=!show;if(ok)n++}});more.hidden=all||f!=='all'}}
cs.forEach(b=>b.addEventListener('click',()=>{{f=b.dataset.f;cs.forEach(x=>x.setAttribute('aria-pressed',x===b));draw()}}));more.addEventListener('click',()=>{{all=true;draw()}});draw()}})();</script>'''
open(os.path.join(D,'index.html'),'w').write(page(f'{SITE}: the latest from Michael Levin\'s lab, every week',home,'Latest'))
# ---------- article pages ----------
def link(m):
    t,_,label=m.group(1).partition('|'); t=t.strip()
    return f'[{label or titles[t]}]({out(t)})' if t in name else (label or t)
for s,f in name.items():
    body=re.sub(r'^---\n.*?\n---\n','',open(f).read(),flags=re.S)
    body=re.sub(r'\[\[([^\]]+)\]\]',link,body); body=re.sub(r'\s*\^\[[^\]]*\]','',body)
    h=markdown.markdown(body,extensions=['tables'])
    if not re.search(r'<h1',h): h=f'<h1>{E(titles[s])}</h1>'+h
    cur={'companies-tracker':'Companies','michael-levin':'Profile','index':'All pages'}.get(s,'')
    open(os.path.join(D,out(s)),'w').write(page(f'{titles[s]} · {SITE}',f'<div class="wrap"><div class="crumb"><a href="index.html">{SITE}</a> / {E(titles[s])}</div><article class="article">{h}</article></div>',cur))
print(len(name)+1,'pages ->',D)
