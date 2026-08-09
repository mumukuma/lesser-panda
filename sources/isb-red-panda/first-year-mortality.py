#!/usr/bin/env python3
"""ISB 2008 血統書：第一年死亡率的地區／年代／園區氣候分組粗算。

用途：支撐 /species/「換毛與健康」節的 sp_health_p2b（氣候不是主導軸）。
資料：同目錄的 ISB-2008-register.csv（2,703 隻，1977–2008）。
世代：只取有確切生日、且生於 2007-12-31 前者（留滿一年觀察窗），n=2,368。
用法：python3 sources/isb-red-panda/first-year-mortality.py

⚠️ 限制（引用數字時務必一起講）：
  - 死亡登錄完整度各地不一，漏報會讓該地「看起來比較好」（中國 24 筆記到 0% 即為鐵證）。
  - 未控制園、胎仔數、母獸經驗、founder 效應；園區氣候分組是依城市手工粗分，非氣象資料。
  - Princée & Glatston 2016 用的是園級氣候變數＋模型，本檔的解析度不足以推翻該文，
    只能說「在地區層級看不到『越熱越糟』的單純關係」。
"""
import csv, re, collections, datetime, os
rows=list(csv.DictReader(open(os.path.join(os.path.dirname(os.path.abspath(__file__)),'ISB-2008-register.csv'))))
datepat=re.compile(r'(\d{1,2} [A-Za-z]{3} \d{4}|~\s*[A-Za-z]{0,3}\s*\d{4}|\?\?\?\?)')
def bi(ev):
    seg=ev.split('|')[0].strip(); m=datepat.search(seg)
    return re.sub(r'\s+',' ',seg[:m.start()].strip()) if m else re.sub(r'\s+',' ',seg[:14].strip())
def pb(s):
    try: return datetime.datetime.strptime((s or '').strip(),'%d %b %Y').date()
    except: return None
def pd_(s):
    try: return datetime.date.fromisoformat((s or '').strip())
    except: return None

JP="HIGASHIIZ SABAE NAGANO HIROSHIMA TOKYOTAMA TOKUYAMA ICHIKAWA TOHOKU_PK HIRAKATA ITOZU OKAYAMA SENDAISHI NISHISONO SHIRAHAMA ASAHIKAWA KUSHIRO_Z NIHONDAIR HIMEHI_SH TOBE ZOORASIA HIGASHI_M MIYAZAK MITO_CHO TOBU KOCHI_NOI CHIBA_SHI KYOTO AKITA ICHIHARA NARA KAWASAKI TOMIOKA ISHIKAWA KOBE_PARK EDOGAWA YOKOHAMA HAMAMATSU OSAKA YUKI KAGAWA KAMI_GUN TOYAMA_Z FUKUOKA IKEDA_ZOO"
NA="KNOXVILLE NZP-WASH NZP-CRC CINCINNAT DENVER COLUMBUS DALLAS NY_BRONX BATTLE_CR SEATTLE LINCOLN_C SANDIEGOZ DETROIT PHILADELP OMAHA SYRACUSE INDIANAPL MILL_MOUN MANHATTAN CALGARY ERIE COLO_SPRG BALTIMORE SIOUX_FAL BUFFALO TORONTO GREENVISC WINNIPEG NASHV_ZOO CLEVELAND CENTRALPK ST_LOUIS SCOTTSBLU SOUTHBEND KANSASCTY LANSING FARGO SACRAMNTO VALLEYZOO MINNESOTA MEMPHIS OKLAHOMA PORTLAND TOLEDO BLOOMINGT BOISE S_BARBARA HOUSTON UTICA FERNDALE OR_WILDLF"
EU="ROTTERDAM MADRID_Z HELSINKI FONTAINE ESKILSTUN AMSTERDAM ANTWERP LISBON BARCELONA LEIPZIG KOLN BUSSOLENG AGRATE RHENEN KREFELD KLEVE COPENHAGE KRISTIANS AALBORG BERLINZOO LA_FRONTI ZURICH DORTMUND HILVARENB BERLIN_TP GORLITZ OVERLOON DRESDEN_Z WARSAW THOIRY AMIENS LODZ DUISBURG ODENSE HANNOVER MUNICH ESTEPONA AUGSBURG EICHBERG EPE PARIS_JP VIENNA LA_PALMYR USTI CAMBRON PRAHA BUDAPEST SALZBURG POZNAN GIVSKUD LA_FLECHE LES_SABLE LA_PLAINE BEAUVAL STUTTGART PEAUGRES HEIDELBRG BOISSIERE POLARPARK WHIPSNADE BELFAST EDINBURGH MARWELL LONDON_RP BURFORD HUNBSTRND BALLAUGH WP_KIRKCU DUBLIN BRISTOL YARMOUTH PAIGNTON CHESTER COLCHESTR HAYLE FOTA SO_LAKES LYMPNE"
OC="ADELAIDE SYDNEY PERTH MOGO MELBOURNE WELLINGTN AUCKLAND YARRALUML"
AF="JOHANSBRG PRETORIA BESTER TRNSV_SNK"
IN="DARJEELIN GANGTOK KANPUR"
CN="SHANGHAI CHENGDU CHINA CHONGQING WUHAN LANCHOW KUNMING SHIH_CHIA GUANGZHOU BEIJING"
REG={}
for grp,names in [('日本',JP),('北美',NA),('歐洲',EU),('大洋洲',OC),('南非',AF),('印度/尼泊爾',IN),('中國',CN)]:
    for n in names.split(): REG[n.replace('_',' ')]=grp

cohort=[]
unmapped=collections.Counter()
for r in rows:
    b=pb(r['birth'])
    if not b or b>datetime.date(2007,12,31): continue
    inst=bi(r['events']); reg=REG.get(inst)
    if not reg: unmapped[inst]+=1; reg='其他/未歸類'
    d=pd_(r['death'])
    died1 = bool(d and (d-b).days<=365)
    cohort.append((reg,b.year,died1,r['taxon'].strip(),inst))
print('cohort n =',len(cohort),' 未歸類',sum(unmapped.values()),'筆／',len(unmapped),'碼')
print('未歸類碼:',', '.join(f'{k}({v})' for k,v in unmapped.most_common(15)))

def rate(sub):
    n=len(sub); d=sum(1 for x in sub if x[2])
    return n,d,(100*d/n if n else float('nan'))

def dec(y): return (y//10)*10
print('\n=== 全球第一年死亡率（依出生年代） ===')
for D in sorted({dec(c[1]) for c in cohort}):
    n,d,p=rate([c for c in cohort if dec(c[1])==D]); print(f'{D}s  n={n:5d}  死={d:4d}  {p:5.1f}%')
print('\n=== 地區 × 年代 ===')
regs=['日本','北美','歐洲','大洋洲','南非','印度/尼泊爾','中國','其他/未歸類']
decs=sorted({dec(c[1]) for c in cohort})
print('地區'.ljust(14)+''.join(f'{D}s'.rjust(14) for D in decs)+'  全期')
for R in regs:
    line=R.ljust(14)
    for D in decs:
        n,d,p=rate([c for c in cohort if c[0]==R and dec(c[1])==D])
        line+=(f'{p:.0f}% (n={n})'.rjust(14) if n else '—'.rjust(14))
    n,d,p=rate([c for c in cohort if c[0]==R])
    line+=f'   {p:.1f}% (n={n})'
    print(line)

print('\n=== 同一飼育文化內部：北美各園依氣候分組 ===')
HOT="DALLAS HOUSTON MEMPHIS OKLAHOMA NASHV_ZOO ST_LOUIS KANSASCTY GREENVISC MANHATTAN"
COLD="MINNESOTA FARGO SIOUX_FAL WINNIPEG CALGARY VALLEYZOO BUFFALO ERIE SYRACUSE UTICA SCOTTSBLU BOISE DENVER COLO_SPRG TORONTO LANSING BATTLE_CR SOUTHBEND CLEVELAND DETROIT SEATTLE PORTLAND OR_WILDLF FERNDALE"
grp={}
for n in HOT.split(): grp[n.replace('_',' ')]='南部濕熱'
for n in COLD.split(): grp[n.replace('_',' ')]='北方/高緯冷涼'
na=[c for c in cohort if c[0]=='北美']
for g in ['南部濕熱','中緯度（其餘）','北方/高緯冷涼']:
    sub=[c for c in na if grp.get(c[4],'中緯度（其餘）')==g]
    n,d,p=rate(sub); print(f'{g:16s} n={n:4d} 死={d:3d}  {p:5.1f}%')
print('\n  2000 年代單獨看：')
for g in ['南部濕熱','中緯度（其餘）','北方/高緯冷涼']:
    sub=[c for c in na if grp.get(c[4],'中緯度（其餘）')==g and c[1]>=2000]
    n,d,p=rate(sub); print(f'  {g:16s} n={n:4d} 死={d:3d}  {p:5.1f}%' if n else f'  {g:16s} n=0')

print('\n=== 日本：北 vs 南 ===')
JPN="ASAHIKAWA KUSHIRO_Z TOHOKU_PK SENDAISHI AKITA NIHONDAIR"
JPS="MIYAZAK FUKUOKA KOCHI_NOI TOBE SHIRAHAMA HIROSHIMA OKAYAMA TOKUYAMA HIMEHI_SH IKEDA_ZOO KAGAWA"
g2={}
for n in JPN.split(): g2[n.replace('_',' ')]='北日本'
for n in JPS.split(): g2[n.replace('_',' ')]='西日本/南日本'
jp=[c for c in cohort if c[0]=='日本']
for g in ['北日本','關東・中部（其餘）','西日本/南日本']:
    sub=[c for c in jp if g2.get(c[4],'關東・中部（其餘）')==g]
    n,d,p=rate(sub); print(f'{g:18s} n={n:4d} 死={d:3d}  {p:5.1f}%')

print('\n=== 亞種（供對照，非本題重點） ===')
for tx in ['fulgens','styani']:
    n,d,p=rate([c for c in cohort if c[3]==tx]); print(f'{tx:8s} n={n:5d} {p:5.1f}%')
