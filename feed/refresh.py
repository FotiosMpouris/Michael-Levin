"""Weekly feed refresh. Pulls YouTube (yt-dlp), Crossref (ORCID) and the thoughtforms.life RSS into feed/latest.json.
It also searches YouTube for new guest appearances (interviews, talks, panels) on other channels and writes them to
feed/guest-candidates.json for review; they reach the public feed only after a check (see feed/UPDATE.md step 3b).
X posts can't be fetched here: the routine adds them with the X tool (see feed/UPDATE.md).
Only source data is written. Existing items are kept, and nothing is invented.
Usage: python3 feed/refresh.py [--dry-run]
       python3 feed/refresh.py --accept VIDEO_ID PAGE_SLUG   (move a checked guest candidate into feed/latest.json)
       python3 feed/refresh.py --reject VIDEO_ID "reason"    (remember a false match so it is never suggested again)
Set YT_COOKIES=/path/to/cookies.txt to pass cookies to yt-dlp (never commit that file)."""
import json,os,re,sys,html,time,glob,subprocess,urllib.request,urllib.parse,datetime
R=os.path.dirname(os.path.dirname(os.path.abspath(__file__))); F=os.path.join(R,'feed','latest.json'); GF=os.path.join(R,'feed','guest-candidates.json')
d=json.load(open(F)); have={i['url'] for i in d['items']}; new=[]
GC=json.load(open(GF)) if os.path.exists(GF) else {'checked':'','pending':[],'rejected':{}}
YT=['yt-dlp']+(['--cookies',os.environ['YT_COOKIES']] if os.environ.get('YT_COOKIES') else [])
def save_guest(): json.dump(GC,open(GF,'w'),indent=1,ensure_ascii=False)
if sys.argv[1:2] in (['--accept'],['--reject']):  # review step for guest candidates; no network
    vid=sys.argv[2]; it=next((c for c in GC['pending'] if c['url'].endswith(vid)),None)
    if not it: sys.exit(f'{vid} is not a pending guest candidate')
    GC['pending'].remove(it)
    if sys.argv[1]=='--reject': GC['rejected'][vid]=sys.argv[3] if len(sys.argv)>3 else 'not a Levin appearance'
    else:
        it['page']=sys.argv[3] if len(sys.argv)>3 else ''; it.pop('match',None)
        d['items']=sorted(d['items']+[it],key=lambda x:x['date'],reverse=True); d['updated']=max(d['updated'],datetime.date.today().isoformat())
        json.dump(d,open(F,'w'),indent=1,ensure_ascii=False)
    save_guest(); print(sys.argv[1][2:]+'ed',vid); sys.exit()
def get(u):
    for k in range(3):
        try: return urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':'Mozilla/5.0'}),timeout=30).read().decode('utf8','ignore')
        except Exception as e: err=e; __import__('time').sleep(3)
    raise err
# YouTube
yt_rss={}
try:
    from zoneinfo import ZoneInfo
    for e in re.findall(r'<entry>(.*?)</entry>',get('https://www.youtube.com/feeds/videos.xml?channel_id=UC3pVafx6EZqXVI2V_Efu2uw'),re.S):
        vid=re.search(r'<yt:videoId>(.*?)</yt:videoId>',e).group(1); pub=re.search(r'<published>(.*?)</published>',e).group(1)
        yt_rss[vid]=(datetime.datetime.fromisoformat(pub).astimezone(ZoneInfo('America/New_York')).date().isoformat(),html.unescape(re.search(r'<title>(.*?)</title>',e).group(1)))
except Exception as e: print('WARN channel RSS failed',e)
ids=subprocess.run(YT+['--flat-playlist','--playlist-end','12','--print','%(id)s','https://www.youtube.com/@drmichaellevin/videos'],capture_output=True,text=True).stdout.split()
for i in ids:
    u=f'https://www.youtube.com/watch?v={i}'
    if u in have: continue
    o=subprocess.run(YT+['--skip-download','--print','%(upload_date)s|%(duration_string)s|%(title)s',u],capture_output=True,text=True).stdout.strip().split('|',2)
    if len(o)==3 and o[0][:2]=='20': new.append(dict(kind='video',date=f'{o[0][:4]}-{o[0][4:6]}-{o[0][6:]}',title=o[2],url=u,source='YouTube @drmichaellevin',note='Duration '+o[1],page=''))
    elif i in yt_rss:  # yt-dlp blocked (bot check / 429): fall back to the channel RSS (published time converted to ET)
        dt,t=yt_rss[i]; new.append(dict(kind='video',date=dt,title=t,url=u,source='YouTube @drmichaellevin',note='',page='',date_basis='channel RSS published, ET'))
    else: print('WARN could not get metadata for video',i)
# Crossref
since=(datetime.date.today()-datetime.timedelta(days=60)).isoformat()
cr=json.loads(get(f'https://api.crossref.org/works?filter=orcid:0000-0001-7292-8084,from-created-date:{since}&sort=created&order=desc&rows=30'))
for w in cr['message']['items']:
    u='https://doi.org/'+w['DOI']
    base=re.sub(r'_v\d+$|\.v\d+$','',w['DOI'])
    if u in have or any(base in x for x in have): continue
    st='preprint' if w.get('type')=='posted-content' else 'peer-reviewed'
    new.append(dict(kind='paper',date=w['created']['date-time'][:10],title=html.unescape(w['title'][0]),url=u,source=html.unescape((w.get('container-title') or [w.get('institution',[{}])[0].get('name','Preprint server') if w.get('institution') else 'Preprint server'])[0]),status=st,authors=', '.join(a.get('family','') for a in w.get('author',[])),note='Peer-reviewed' if st=='peer-reviewed' else 'Preprint, not yet peer-reviewed',date_basis='DOI registered'))
# Blog
lastblog=max([i['date'] for i in d['items'] if i['kind']=='blog'] or ['0'])
rss=get('https://thoughtforms.life/feed/')
for it in re.findall(r'<item>(.*?)</item>',rss,re.S)[:10]:
    g=lambda t:html.unescape((re.search(f'<{t}>(.*?)</{t}>',it,re.S) or [0,''])[1]).replace('<![CDATA[','').replace(']]>','').strip()
    u=g('link')
    if u in have: continue
    dt=datetime.datetime.strptime(g('pubDate')[:16],'%a, %d %b %Y').date().isoformat()
    if dt<=lastblog or 'Nature Photography' in g('title'): continue
    new.append(dict(kind='blog',date=dt,title=g('title').rstrip(':'),url=u,source='thoughtforms.life'))
# Guest appearances on other channels. Kept deliberately simple; every rule is listed here and in feed/UPDATE.md.
OWN='UC3pVafx6EZqXVI2V_Efu2uw'  # his own channel is handled above
QUERIES=['"Michael Levin"','Michael Levin interview','Michael Levin podcast','Michael Levin talk','Michael Levin bioelectricity']
SEARCH='https://www.youtube.com/results?search_query={}&sp=CAISAggE'  # YouTube filters: sort by upload date, uploaded this month
NAME=re.compile(r'\b(michael|mike|dr\.?|prof\.?|professor)\s+levin\b|@drmichaellevin',re.I)  # not just "Levin" (Mark Levin etc.)
CLIP=re.compile(r'#shorts?\b|\bshorts?\b|\bclips?\b|highlights?|compilation|re-?upload|\btrailer\b|\bteaser\b|best of',re.I)
MIN_SECONDS=600  # under about 10 minutes is almost always a clip
SKIP_CHANNELS={}  # channel_id -> reason; add clip or reupload channels here when the review step finds them
def vid_ids_on_site():
    ids={u.split('v=')[-1][:11] for u in have if 'youtube.com/watch' in u}
    for f in glob.glob(os.path.join(R,'videos','*.md')):
        m=re.search(r'^video_id:\s*(\S+)',open(f).read(),re.M); ids|={m.group(1)} if m else set()
    ids|={os.path.basename(f)[11:-4] for f in glob.glob(os.path.join(R,'raw','transcripts','*.txt'))}
    return ids|{c['url'].split('v=')[-1] for c in GC['pending']}|set(GC['rejected'])
norm=lambda t:re.sub(r'[^a-z0-9]+',' ',t.lower()).strip()
titles={norm(i['title']) for i in d['items']}  # same title as an item we already have = reupload
since=(datetime.date.fromisoformat((GC['checked'] or d['updated'])[:10])-datetime.timedelta(days=3)).strftime('%Y%m%d')  # last run, 3-day overlap
seen=vid_ids_on_site(); found={}; guests=[]
for q in QUERIES:
    out=subprocess.run(YT+['--flat-playlist','--playlist-end','40','--print','%(id)s\t%(channel_id)s\t%(duration)s\t%(title)s',SEARCH.format(urllib.parse.quote_plus(q))],capture_output=True,text=True).stdout
    for line in out.splitlines():
        p=line.split('\t',3)
        if len(p)<4 or len(p[0])!=11 or p[0] in seen or p[0] in found: continue
        if p[1]==OWN or p[1] in SKIP_CHANNELS or CLIP.search(p[3]) or norm(p[3]) in titles: continue
        if p[2]!='NA' and float(p[2])<MIN_SECONDS: continue
        found[p[0]]=p[3]
    time.sleep(3)  # YouTube rate-limits fast bursts
for i in list(found)[:30]:  # cap metadata calls per run
    o=subprocess.run(YT+['--skip-download','--print','%(upload_date)s\t%(duration)s\t%(duration_string)s\t%(channel_id)s\t%(channel)s\t%(title)s','--print','%(description)s','--',i],capture_output=True,text=True).stdout
    time.sleep(2)
    head,_,desc=o.partition('\n'); p=head.split('\t',5)
    if len(p)<6 or p[0][:2]!='20': print('WARN could not get metadata for guest candidate',i); continue
    up,dur,durs,cid,ch,t=p
    if up<since or cid==OWN or cid in SKIP_CHANNELS or (dur!='NA' and float(dur)<MIN_SECONDS) or CLIP.search(t) or norm(t) in titles: continue
    if not NAME.search(t+' '+desc): continue
    guests.append(dict(kind='video',date=f'{up[:4]}-{up[4:6]}-{up[6:]}',title=t,url=f'https://www.youtube.com/watch?v={i}',source=f'YouTube · {ch} (Levin as guest)',note='Duration '+durs,page='',appearance='guest',channel=ch,match='title' if NAME.search(t) else 'description'))
for c in guests: print('GUEST CANDIDATE',c['date'],c['channel'],'|',c['title'][:80],'| name in',c['match'])
for n in new: print('NEW',n['kind'],n['date'],n['title'][:90])
if '--dry-run' not in sys.argv and new:
    d['items']=sorted(d['items']+new,key=lambda x:x['date'],reverse=True); d['updated']=datetime.date.today().isoformat()
    d['checked_at']=datetime.datetime.now().strftime('%Y-%m-%d %-I:%M %p ET'); json.dump(d,open(F,'w'),indent=1,ensure_ascii=False)
if '--dry-run' not in sys.argv:
    GC['pending']+=guests; GC['checked']=datetime.date.today().isoformat(); save_guest()
print(len(new),'new items;',len(guests),'new guest candidates;',len(GC['pending']),'pending review in feed/guest-candidates.json')
