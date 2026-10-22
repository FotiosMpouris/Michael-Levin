"""Weekly feed refresh. Pulls YouTube (yt-dlp), Crossref (ORCID) and the thoughtforms.life RSS into feed/latest.json.
X posts can't be fetched here: the routine adds them with the X tool (see feed/UPDATE.md).
Only source data is written. Existing items are kept, and nothing is invented.
Usage: python3 feed/refresh.py [--dry-run]"""
import json,os,re,sys,html,subprocess,urllib.request,datetime
R=os.path.dirname(os.path.dirname(os.path.abspath(__file__))); F=os.path.join(R,'feed','latest.json')
d=json.load(open(F)); have={i['url'] for i in d['items']}; new=[]
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
ids=subprocess.run(['yt-dlp','--flat-playlist','--playlist-end','12','--print','%(id)s','https://www.youtube.com/@drmichaellevin/videos'],capture_output=True,text=True).stdout.split()
for i in ids:
    u=f'https://www.youtube.com/watch?v={i}'
    if u in have: continue
    o=subprocess.run(['yt-dlp','--skip-download','--print','%(upload_date)s|%(duration_string)s|%(title)s',u],capture_output=True,text=True).stdout.strip().split('|',2)
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
for n in new: print('NEW',n['kind'],n['date'],n['title'][:90])
if '--dry-run' not in sys.argv and new:
    d['items']=sorted(d['items']+new,key=lambda x:x['date'],reverse=True); d['updated']=datetime.date.today().isoformat()
    d['checked_at']=datetime.datetime.now().strftime('%Y-%m-%d %-I:%M %p ET'); json.dump(d,open(F,'w'),indent=1,ensure_ascii=False)
print(len(new),'new items')
