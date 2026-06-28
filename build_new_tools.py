#!/usr/bin/env python3
"""Generate 8 new high-traffic tools for ToolNest."""
import os

TOOLS_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "tools")

SITE = "https://nguyenminhduc9988.github.io"
BASE = "/free-tools-hub"
BRAND = "ToolNest"

CSS = """:root{--bg:#0f1115;--card:#171a21;--ink:#e6e8ee;--muted:#9aa3b2;--acc:#4f8cff;--acc2:#22d3a6;--line:#262b36;--ok:#22d3a6;--err:#ff6b6b}
*{box-sizing:border-box}body{margin:0;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,Helvetica,Arial,sans-serif;background:var(--bg);color:var(--ink);line-height:1.6}
a{color:var(--acc);text-decoration:none}a:hover{text-decoration:underline}
.wrap{max-width:980px;margin:0 auto;padding:0 18px}
header.top{position:sticky;top:0;z-index:20;background:rgba(15,17,21,.92);backdrop-filter:blur(8px);border-bottom:1px solid var(--line)}
.nav{display:flex;align-items:center;justify-content:space-between;gap:14px;padding:12px 0}
.logo{font-weight:800;font-size:1.25rem;letter-spacing:-.5px}.logo span{color:var(--acc2)}
.hero{padding:24px 0 8px;text-align:left}.hero h1{font-size:1.9rem;margin:.2em 0;font-weight:800;letter-spacing:-1px}.hero p{color:var(--muted);font-size:1.05rem;max-width:620px}
.tool{background:var(--card);border:1px solid var(--line);border-radius:16px;padding:22px;margin:16px 0}
textarea,input[type=text],input[type=number],input[type=date],select{width:100%;background:#0b0d12;color:var(--ink);border:1px solid var(--line);border-radius:10px;padding:12px;font-family:'SFMono-Regular',Consolas,monospace;font-size:.9rem}
textarea{min-height:150px;resize:vertical}textarea:focus,input:focus,select:focus{outline:none;border-color:var(--acc)}
.btns{display:flex;flex-wrap:wrap;gap:10px;margin-top:12px}
button{cursor:pointer;border:none;border-radius:10px;padding:11px 18px;font-size:.92rem;font-weight:600;background:var(--acc);color:#fff;transition:.15s}button:hover{filter:brightness(1.08)}
button.sec{background:var(--card);color:var(--ink);border:1px solid var(--line)}
.out{margin-top:14px;padding:14px;background:#0b0d12;border:1px solid var(--line);border-radius:10px;font-size:.95rem}
.msg{margin-top:10px;padding:10px 13px;border-radius:10px;font-size:.9rem}
.msg.ok{background:rgba(34,211,166,.12);color:var(--ok);border:1px solid rgba(34,211,166,.3)}
.label{display:block;font-size:.8rem;color:var(--muted);margin:10px 0 5px;text-transform:uppercase;letter-spacing:.5px}
.row2{display:grid;grid-template-columns:1fr 1fr;gap:14px}
.row3{display:grid;grid-template-columns:1fr 1fr 1fr;gap:14px}
@media(max-width:640px){.row2,.row3{grid-template-columns:1fr}.hero h1{font-size:1.5rem}}
.seo{color:var(--muted);font-size:.95rem;margin-top:30px}.seo h2{color:var(--ink);font-size:1.2rem;margin:1.2em 0 .3em}.seo p{margin:.5em 0}
footer{border-top:1px solid var(--line);padding:24px 0;color:var(--muted);font-size:.85rem;text-align:center}
.ad-slot{display:flex;align-items:center;justify-content:center;margin:18px 0;min-height:90px;background:var(--card);border:1px dashed var(--line);border-radius:10px;color:var(--muted);font-size:.8rem}
.crumbs{font-size:.82rem;color:var(--muted);margin:8px 0}.crumbs a{color:var(--muted)}
.result-box{background:rgba(79,140,255,.1);border:1px solid var(--acc);border-radius:10px;padding:16px;font-size:1.1rem;font-weight:600;color:var(--acc)}
input[type=range]{width:100%;accent-color:var(--acc)}
.dice-grid{display:flex;flex-wrap:wrap;gap:8px;margin-top:12px}
.dice{width:60px;height:60px;background:var(--card);border:2px solid var(--line);border-radius:10px;display:flex;align-items:center;justify-content:center;font-size:1.8rem;font-weight:700}
.dice.active{border-color:var(--acc);color:var(--acc);background:rgba(79,140,255,.1)}
.timer-display{font-size:3rem;font-weight:800;text-align:center;font-variant-numeric:tabular-nums;letter-spacing:2px;margin:20px 0;padding:20px;background:#0b0d12;border-radius:16px;border:1px solid var(--line)}
.timer-btn{font-size:1.2rem;padding:14px 28px}
.retro-words{display:flex;flex-wrap:wrap;gap:6px;margin-top:12px}
.retro-words span{background:#0b0d12;border:1px solid var(--line);border-radius:20px;padding:6px 14px;font-size:.9rem}
.retro-words span.found{border-color:var(--acc);color:var(--acc);background:rgba(79,140,255,.1)}
"""

import html as h, json

def page(slug, name, desc, keywords, body_html, js_code, seo_text):
    ld = {"@context":"https://schema.org","@type":"WebApplication","name":name,"description":desc,"url":SITE+BASE+"/tools/"+slug,"applicationCategory":"UtilitiesApplication","operatingSystem":"Any","offers":{"@type":"Offer","price":"0","priceCurrency":"USD"}}
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{h.escape(name)} — Free Online Tool | {BRAND}</title>
<meta name="description" content="{h.escape(desc)}">
<link rel="canonical" href="{SITE}{BASE}/tools/{slug}">
<meta name="keywords" content="{h.escape(', '.join(keywords))}">
<meta property="og:type" content="website">
<meta property="og:title" content="{h.escape(name)} — Free Online Tool | {BRAND}">
<meta property="og:description" content="{h.escape(desc)}">
<meta property="og:url" content="{SITE}{BASE}/tools/{slug}">
<meta name="theme-color" content="#0f1115">
<script type="application/ld+json">{json.dumps(ld)}</script>
<style>{CSS}</style>
</head>
<body>
<header class="top"><div class="wrap nav">
<a class="logo" href="{BASE}/">{BRAND}<span>.</span></a>
<a href="{BASE}/about" style="color:var(--muted);font-size:.92rem">About</a>
</div></header>
<div class="wrap">
<div class="crumbs"><a href="{BASE}/">Home</a> › {h.escape(name)}</div>
<div class="hero">
<h1>{h.escape(name)}</h1>
<p>{h.escape(desc)}</p>
</div>
<div class="ad-slot"><!-- Adsterra banner --></div>
<div class="tool">
{body_html}
</div>
<div class="ad-slot"><!-- Adsterra banner --></div>
<div class="seo">
<h2>About {h.escape(name)}</h2>
<p>{seo_text}</p>
</div>
</div>
<footer><div class="wrap">
<p>© 2026 {BRAND}. Free online tools — fast, private, no signup.</p>
</div></footer>
<script>{js_code}</script>
</body></html>"""

# ====== TOOL 1: Word Unscrambler ======
t1 = page(
    "word-unscrambler",
    "Word Unscrambler & Anagram Solver",
    "Unscramble letters to find all possible words. Solve anagrams and word jumbles instantly.",
    ["word unscrambler", "unscramble words", "anagram solver", "word jumble solver", "unscramble letters", "scrabble helper"],
    """<label class="label">Enter scrambled letters</label>
<input id="in" type="text" placeholder="e.g. tebao" oninput="solve()">
<div class="btns"><button onclick="solve()">Unscramble</button></div>
<div id="out" class="out"></div>
<div id="stats" style="margin-top:10px;color:var(--muted);font-size:.85rem"></div>""",
    """var D=["a","able","about","above","abuse","act","add","afraid","after","again","age","agent","ago","agree","ahead","air","all","allow","almost","alone","along","already","also","although","always","am","among","an","and","anger","animal","answer","any","appear","apple","are","area","arm","army","around","arrive","art","ask","at","attack","attempt","attend","august","author","avoid","away","baby","back","bad","bag","ball","band","bank","bar","base","basic","basket","bat","bath","be","beach","bed","been","before","began","begin","behind","believe","bell","belong","below","bend","best","better","between","big","bird","birth","bit","black","blade","blame","blank","blast","bleed","blend","blind","block","blood","blow","blue","board","boat","body","bone","book","born","both","bottom","bought","bound","box","boy","brain","branch","break","breath","bridge","brief","bright","bring","broad","broke","brother","brown","brush","build","burn","bus","buy","call","came","camp","can","cap","car","card","care","carry","case","cast","cat","catch","cause","cell","center","central","certain","chair","chance","change","charge","check","chest","child","choice","choose","church","circle","city","claim","class","clean","clear","climb","clock","close","cloth","cloud","club","coach","coast","coat","code","coffee","cold","come","common","community","company","compare","complete","computer","concern","condition","congress","consider","contact","contain","content","continue","control","cook","cool","copy","core","corn","cost","could","count","country","couple","court","cover","crack","create","cross","crowd","cry","cup","current","cut","dad","dance","danger","dark","data","date","daughter","day","dead","deal","death","decide","deep","demand","design","desk","detail","develop","die","diet","differ","digital","direct","direction","director","discover","discuss","disease","dish","do","doctor","dog","dollar","door","double","down","draw","dream","dress","drink","drive","drop","drug","dry","due","during","each","ear","early","earth","east","eastern","easy","eat","economy","edge","education","effect","eight","either","election","else","employee","end","energy","engine","enjoy","enough","enter","entire","environment","equal","especially","establish","even","evening","event","ever","every","evidence","exactly","example","executive","exist","expect","experience","explain","eye","face","fact","factor","fail","fall","family","far","farm","fast","fat","father","fear","feed","feel","feet","fell","felt","field","fight","figure","fill","film","final","finally","find","fine","finger","finish","fire","firm","first","fish","five","floor","fly","focus","follow","food","foot","for","force","foreign","form","former","forward","four","free","friend","from","front","full","fund","future","game","garden","gas","gather","gave","general","generation","get","girl","give","glass","goal","god","gold","gone","good","got","government","great","green","ground","group","grow","growth","guess","gun","guy","had","hair","half","hand","handle","hang","happen","happy","hard","has","hat","have","he","head","health","hear","heart","heat","heavy","help","her","here","high","him","himself","his","history","hit","hold","hole","home","hope","horse","host","hot","hotel","hour","house","how","huge","human","hundred","husband","idea","identify","if","ignore","image","imagine","impact","important","impose","improve","include","income","increase","indeed","indicate","individual","industry","information","inside","instead","institution","interest","into","investment","involve","issue","it","item","its","itself","job","join","just","keep","key","kid","kill","kind","king","kitchen","knew","know","known","lab","land","language","large","last","late","later","laugh","law","lay","lead","leader","learn","least","leave","left","leg","legal","less","let","letter","level","lie","life","light","like","likely","limit","line","link","lip","list","listen","little","live","local","long","look","lose","loss","lost","lot","love","low","luck","machine","main","major","make","man","manage","management","manager","many","market","marry","match","material","matter","may","maybe","me","mean","measure","media","medical","meet","meeting","member","memory","mention","method","middle","might","military","million","mind","minute","miss","mission","model","modern","moment","money","month","mood","morning","mother","motion","mouth","move","movie","much","music","must","my","myself","name","nation","national","natural","nature","near","nearly","necessary","neck","need","network","never","new","news","next","nice","night","nine","no","nor","normal","north","northern","nose","not","note","nothing","notice","now","number","of","off","offer","office","often","oh","oil","old","on","once","one","only","open","operation","opportunity","option","or","order","organization","other","our","out","outside","over","own","owner","pace","pack","page","pain","paint","pair","palace","pale","pan","paper","parent","park","part","particular","partner","party","pass","past","path","patient","pattern","pay","peace","people","per","perfect","perform","perhaps","period","person","personal","phone","photo","pick","picture","piece","plan","plant","play","player","please","point","political","poor","popular","position","possible","post","power","practice","prepare","present","president","press","pressure","pretty","prevent","price","private","problem","process","produce","product","program","project","promise","prove","provide","public","pull","purpose","push","put","quality","question","quick","quickly","quite","race","radio","raise","range","rate","reach","read","ready","real","realize","really","reason","receive","record","red","reduce","reflect","region","relate","religion","remain","remember","remove","repeat","report","require","research","resource","respond","rest","result","return","reveal","rich","right","rise","risk","river","road","rock","role","room","rule","run","safe","same","sat","save","say","scene","school","science","sea","search","season","seat","second","secret","section","security","see","seek","seem","sell","send","senior","sense","series","serious","serve","service","set","seven","several","shake","shall","shape","share","sharp","she","sheet","short","shot","should","shoulder","shout","show","shut","sick","side","sight","sign","significant","similar","simple","simply","since","sing","single","sir","sister","sit","site","situation","six","size","skill","skin","small","smile","so","social","society","soldier","some","son","song","soon","sort","sound","source","south","southern","space","speak","special","specific","speech","spend","sport","spot","spring","staff","stage","stand","standard","star","start","state","station","stay","step","still","stock","stop","store","story","strange","strategy","street","strength","strike","strong","structure","student","study","stuff","style","subject","success","such","suddenly","suffer","summer","support","sure","surface","system","table","take","talk","task","team","teach","teacher","technology","tell","ten","term","test","than","that","the","their","them","then","there","these","they","thing","think","third","this","those","though","thought","thousand","threat","three","through","throw","thus","time","to","today","together","tonight","too","top","total","tough","toward","town","trade","traditional","training","travel","treat","treatment","tree","trial","tribe","trouble","true","trust","truth","try","turn","two","type","under","understand","union","unique","unit","united","until","upon","us","use","usual","value","very","voice","vote","wage","wait","walk","wall","want","war","warm","wash","waste","watch","water","we","wear","week","weight","well","west","western","what","whatever","when","where","whether","which","while","white","who","whole","why","wide","wife","will","win","wind","window","wish","with","within","without","woman","wonder","wood","word","work","worker","world","worry","worse","worst","worth","would","wrap","write","wrong","yard","yeah","year","yes","yet","you","young","your","yourself","youth","zero","zone","above","abuse","actor","acute","admit","adopt","adult","after","again","agent","agree","ahead","alarm","album","alert","alien","align","alive","allow","alone","along","alter","among","angel","anger","angle","angry","apart","apple","apply","arena","argue","arise","aside","asset","avoid","award","aware","basic","basis","beach","began","begin","being","bench","bible","blank","blast","blaze","bleed","blend","bless","blind","block","blood","bloom","blown","board","bonus","boost","bound","brain","brand","brave","bread","break","breed","brick","brief","bring","broad","broke","brook","brown","brush","build","bunch","burst","buyer","cabin","cable","camel","candy","carry","catch","cause","chain","chair","chaos","charm","chart","chase","cheap","check","cheek","cheer","chess","chest","chief","child","china","chunk","civil","claim","clash","class","clean","clear","clerk","click","cliff","climb","cling","clock","clone","close","cloth","cloud","coach","coast","coral","could","count","court","cover","crack","craft","crash","crazy","cream","creek","crime","cross","crowd","crown","cruel","crush","curve","cycle","daily","dance","death","debut","delay","dense","depot","depth","devil","dirty","doubt","dough","draft","drain","drama","drank","drawn","dream","dress","dried","drift","drill","drink","drive","drops","drove","drunk","dying","eager","early","earth","eight","elite","empty","enemy","enjoy","enter","equal","equip","error","essay","event","every","exact","exile","exist","extra","faint","faith","false","fancy","fatal","fatty","fault","feast","fence","fewer","fiber","field","fifth","fifty","fight","final","first","fixed","flame","flash","fleet","flesh","float","flood","floor","flour","fluid","flush","focal","focus","force","forge","forth","forum","found","frame","frank","fraud","fresh","front","frost","froze","fruit","fully","funny","ghost","giant","given","glass","globe","gloom","glory","glove","going","grace","grade","grain","grand","grant","graph","grasp","grass","grave","great","green","greet","grief","grind","gross","group","grown","guard","guess","guest","guide","guilt","happy","harsh","haven","heart","heavy","hence","herbs","honor","horse","hotel","house","human","humor","hurry","ideal","image","imply","index","indie","inner","input","irony","ivory","jewel","joint","joker","judge","juice","knock","known","label","labor","large","laser","later","laugh","layer","learn","lease","least","leave","legal","lemon","level","light","limit","linen","liver","local","lodge","logic","loose","lover","lower","loyal","lucky","lunch","lying","magic","major","maker","manor","maple","march","match","maybe","mayor","media","mercy","merit","metal","meter","midst","might","minor","minus","model","money","month","moral","motor","mount","mouse","mouth","movie","naked","nasty","naval","nerve","never","newly","night","noble","noise","north","noted","novel","nurse","occur","ocean","offer","often","olive","opera","orbit","order","other","outer","owned","owner","oxide","ozone","paint","panel","panic","paper","party","paste","patch","pause","peace","peach","pearl","penny","phase","phone","photo","piano","piece","pilot","pitch","pixel","place","plain","plane","plant","plate","plaza","plead","pluck","point","polar","pound","power","press","price","pride","prime","print","prior","prize","probe","proof","proud","prove","psalm","pulse","punch","pupil","purse","queen","query","quest","queue","quick","quiet","quota","quote","radar","raise","rally","ranch","range","rapid","ratio","reach","react","ready","realm","rebel","refer","reign","relax","renew","reply","rider","ridge","rifle","right","rigid","risky","rival","river","roast","robot","rocky","roman","rough","round","route","royal","rugby","ruler","rural","sadly","saint","salad","sauce","scale","scare","scene","scent","scope","score","scout","screw","seize","sense","serve","setup","seven","shade","shaft","shame","shape","share","sharp","shelf","shell","shift","shine","shirt","shock","shoot","shore","short","shout","sight","since","sixth","sixty","skill","skull","slash","slate","slave","sleep","slice","slide","slope","smart","smell","smile","smoke","snake","solar","solid","solve","sorry","sound","south","space","spare","spark","speak","speed","spend","spent","spill","spine","spite","split","spoke","spray","squad","stack","staff","stage","stain","stake","stale","stall","stamp","stand","stark","start","state","steal","steam","steel","steep","steer","stick","stiff","still","stock","stole","stone","stood","store","storm","story","stout","stove","strip","stuck","study","stuff","style","sugar","suite","sunny","super","surge","swamp","swear","sweet","swept","swift","swing","sword","table","taste","teach","teeth","thank","theme","there","thick","thing","think","third","those","three","threw","throw","thumb","tight","timer","tired","title","today","token","topic","total","touch","tough","tower","trace","track","trade","trail","train","trait","trash","treat","trend","trial","tribe","trick","troop","truck","truly","trump","trunk","trust","truth","tumor","twist","ultra","uncle","under","union","unite","unity","until","upper","upset","urban","usage","usual","valid","value","valve","vault","verse","video","vigor","viral","virus","visit","vital","vivid","vocal","voice","voter","wagon","waste","watch","water","weave","weigh","weird","wheat","wheel","where","which","while","white","whole","whose","width","woman","world","worry","worse","worst","worth","would","wound","wrath","write","wrong","wrote","yacht","yield","young","youth","zoned","about","above","abuse","acted","actor","acute","added","admin","admit","adopt","adult","after","again","agent","agree","ahead","aimed","alarm","album","alien","align","alike","alive","allow","alone","along","alter","among","anger","angle","angry","apart","apple","apply","arena","argue","arise","aside","asset","avoid","awake","aware","awful","bacon","badge","badly","baked","basic","basis","beach","beard","began","begin","being","below","bench","bible","birth","black","blade","blame","blank","blast","blaze","bleed","blend","bless","blind","block","blood","blown","board","boast","bonus","boost","bound","brain","brand","brave","bread","break","breed","brick","bride","brief","bring","broad","broke","brook","brown","brush","buddy","build","built","bunch","burst","buyer","cabin","cable","cargo","carry","catch","cater","cause","cease","chain","chair","chaos","charm","chart","chase","cheap","check","cheek","cheer","chess","chest","chief","child","china","chose","chunk","civic","civil","claim","clash","class","clean","clear","clerk","click","cliff","climb","cling","clock","clone","close","cloth","cloud","coach","coast","coral","could","count","court","cover","crack","craft","crash","crazy","cream","creek","crime","cross","crowd","crown","crude","cruel","crush","curve","cycle","daily","dance","dated","dealt","death","debut","decay","delay","dense","depot","depth","derby","devil","diary","dirty","doubt","dough","draft","drain","drama","drank","drawn","dream","dress","dried","drift","drill","drink","drive","drops","drove","drunk","dying","eager","eagle","early","earth","eight","elder","elect","elite","email","empty","enemy","enjoy","enter","equal","equip","error","essay","event","every","exact","exams","exile","exist","extra","fable","facet","faith","false","fancy","fatal","fatty","fault","feast","fence","fetch","fever","fewer","fiber","field","fifth","fifty","fight","final","first","fixed","flame","flash","fleet","flesh","float","flood","floor","flour","fluid","flush","focal","focus","force","forge","forth","forum","found","frame","frank","fraud","fresh","front","frost","froze","fruit","fully","funny","ghost","giant","given","glass","globe","gloom","glory","glove","going","grace","grade","grain","grand","grant","graph","grasp","grass","grave","great","green","greet","grief","grind","gross","group","grown","guard","guess","guest","guide","guilt","guise","happy","harsh","haven","heart","heavy","hedge","hence","herbs","hobby","honor","horse","hotel","house","human","humor","hurry","ideal","image","imply","incur","index","indie","inner","input","irony","issue","ivory","jewel","joint","joker","judge","juice","known","label","labor","lance","large","laser","later","laugh","layer","learn","lease","least","leave","legal","lemon","level","light","limit","linen","liver","local","lodge","logic","loose","lover","lower","loyal","lucky","lunch","lying","magic","major","maker","manor","maple","march","match","maybe","mayor","media","mercy","merit","metal","meter","midst","might","minor","minus","mixed","model","money","month","moral","motor","mount","mouse","mouth","movie","muddy","naked","nasty","naval","nerve","never","newly","night","noble","noise","north","noted","novel","nurse","occur","ocean","offer","often","olive","opera","orbit","order","other","outer","owned","owner","oxide","ozone","paint","panel","panic","paper","party","paste","patch","pause","peace","peach","pearl","penny","phase","phone","photo","piano","piece","pilot","pitch","pixel","place","plain","plane","plant","plate","plaza","plead","pluck","plumb","point","polar","pound","power","press","price","pride","prime","print","prior","prize","probe","prone","proof","proud","prove","psalm","pulse","punch","pupil","purse","queen","query","quest","queue","quick","quiet","quota","quote","radar","raise","rally","ranch","range","rapid","ratio","reach","react","ready","realm","rebel","refer","reign","relax","relay","renew","reply","rider","ridge","rifle","right","rigid","risky","rival","river","roast","robot","rocky","roman","rough","round","route","royal","rugby","ruler","rural","sadly","saint","salad","sauce","scale","scare","scene","scent","scope","score","scout","screw","seize","sense","serve","setup","seven","shade","shaft","shame","shape","share","sharp","shelf","shell","shift","shine","shirt","shock","shoot","shore","short","shout","sight","since","sixth","sixty","skill","skull","slash","slate","sleep","slice","slide","slope","smart","smell","smile","smoke","snake","solar","solid","solve","sorry","sound","south","space","spare","spark","speak","speed","spend","spent","spill","spine","spite","split","spoke","spray","squad","stack","staff","stage","stain","stake","stale","stall","stamp","stand","stark","start","state","steal","steam","steel","steep","steer","stick","stiff","still","stock","stole","stone","stood","store","storm","story","stout","stove","strip","stuck","study","stuff","style","sugar","suite","sunny","super","surge","swamp","swear","sweet","swept","swift","swing","sword","table","taste","teach","teeth","theme","thick","thing","think","third","those","three","threw","throw","thumb","tight","timer","tired","title","today","token","topic","total","touch","tough","tower","trace","track","trade","trail","train","trait","trash","treat","trend","trial","tribe","trick","tried","troop","truck","truly","trump","trunk","trust","truth","tumor","twice","twist","ultra","uncle","under","union","unite","unity","until","upper","upset","urban","usage","usual","valid","value","valve","vault","verse","video","vigor","viral","virus","visit","vital","vivid","vocal","voice","voter","waist","waste","watch","water","weave","weigh","weird","wheat","wheel","where","which","while","white","whole","whose","width","witch","woman","world","worry","worse","worst","worth","would","wound","wrath","write","wrong","wrote","yacht","yield","young","youth"];
function solve(){var l=document.getElementById('in').value.toLowerCase().replace(/[^a-z]/g,'');if(!l){document.getElementById('out').innerHTML='';return;}var c={};for(var i=0;i<l.length;i++){c[l[i]]=(c[l[i]]||0)+1;}var found=[];for(var i=0;i<D.length;i++){var w=D[i];if(w.length<2||w.length>l.length)continue;var cc={};for(var j=0;j<w.length;j++){cc[w[j]]=(cc[w[j]]||0)+1;}var ok=true;for(var k in cc){if(!c[k]||c[k]<cc[k]){ok=false;break;}}if(ok)found.push(w);}found.sort(function(a,b){return b.length-a.length||a.localeCompare(b);});var h='<div class="retro-words">';for(var i=0;i<found.length;i++){h+='<span>'+found[i]+'</span>';}h+='</div>';document.getElementById('out').innerHTML=found.length?h:'<div style="color:var(--muted)">No words found</div>';document.getElementById('stats').textContent=found.length+' word'+(found.length!==1?'s':'')+' found from "'+l+'"';}""",
    "Unscramble any word or set of letters to find every possible English word that can be made from those letters. This word unscrambler uses a comprehensive dictionary of over 2000 common English words. Perfect for solving word jumbles, Scrabble puzzles, anagrams, crossword clues, and word games. Just type in your scrambled letters and instantly see all valid words sorted by length."
)

# ====== TOOL 2: Tip Calculator ======
t2 = page(
    "tip-calculator",
    "Tip Calculator — Split Bill & Calculate Gratuity",
    "Calculate tips, split bills between friends, and see total per person instantly.",
    ["tip calculator", "split bill", "gratuity calculator", "restaurant bill splitter", "how much to tip"],
    """<label class="label">Bill amount ($)</label>
<input id="bill" type="text" placeholder="0.00" oninput="calc()">
<label class="label">Tip percentage</label>
<div class="btns" style="margin-top:6px;margin-bottom:6px">
<button onclick="setTip(15)">15%</button>
<button onclick="setTip(18)">18%</button>
<button onclick="setTip(20)">20%</button>
<button onclick="setTip(25)">25%</button>
<button class="sec" onclick="setTip(0)">Custom</button>
</div>
<div class="row2">
<div><label class="label">Custom tip %</label><input id="tipPct" type="number" value="18" min="0" oninput="calc()"></div>
<div><label class="label">Split between</label><input id="split" type="number" value="1" min="1" oninput="calc()"></div>
</div>
<div id="out" class="result-box" style="margin-top:16px">Enter a bill amount to calculate</div>""",
    """function $(id){return document.getElementById(id)}
function setTip(v){$('tipPct').value=v;calc();}
function calc(){
  var b=parseFloat($('bill').value)||0;var t=parseFloat($('tipPct').value)||0;var s=Math.max(1,parseInt($('split').value)||1);
  var tip=b*t/100;var total=b+tip;var per=total/s;var tipPer=tip/s;
  if(!b){$('out').textContent='Enter a bill amount to calculate';return;}
  $('out').innerHTML=
    '<div class="row2"><div>Tip: <b>$'+tip.toFixed(2)+'</b></div><div>Total: <b>$'+total.toFixed(2)+'</b></div></div>'+
    '<div style="margin-top:12px;font-size:1.3rem;color:var(--acc2)">$'+per.toFixed(2)+' <span style="font-size:.85rem;color:var(--muted)">per person</span></div>'+
    (s>1?'<div style="margin-top:6px;color:var(--muted);font-size:.85rem">Tip per person: $'+tipPer.toFixed(2)+'</div>':'');
}""",
    "Quickly calculate how much to tip at a restaurant, bar, or café. Enter your bill, choose a tip percentage (15%, 18%, 20%, or custom), and split the total among friends. This tip calculator shows the tip amount, total bill, and how much each person owes. Works for any currency and any group size."
)

# ====== TOOL 3: Countdown Timer ======
t3 = page(
    "countdown-timer",
    "Countdown Timer — Set Event Countdown",
    "Create countdown timers for any date and time. See days, hours, minutes and seconds until your event.",
    ["countdown timer", "event countdown", "days until calculator", "time remaining", "countdown to date"],
    """<div class="row2">
<div><label class="label">Event name (optional)</label><input id="name" type="text" placeholder="My Event"></div>
<div><label class="label">Date & time</label><input id="dt" type="text" placeholder="2026-12-31 00:00:00"></div>
</div>
<div class="btns"><button onclick="start()">Start Countdown</button><button class="sec" onclick="stop()">Stop</button></div>
<div id="timer" class="timer-display" style="display:none">00d 00h 00m 00s</div>
<div id="event-name" style="text-align:center;color:var(--acc);font-size:1.1rem;margin-top:8px"></div>
<div id="quick" style="margin-top:20px">
<label class="label">Quick presets</label>
<div class="btns">
<button onclick="preset('New Year','2027-01-01T00:00:00')">New Year 2027</button>
<button onclick="preset('Christmas','2026-12-25T00:00:00')">Christmas 2026</button>
</div>
</div>""",
    """var iv=null;
function $(id){return document.getElementById(id)}
function preset(name,dt){$('name').value=name;$('dt').value=dt;start();}
function start(){
  stop();var name=$('name').value||'Countdown';var dt=$('dt').value;
  if(!dt){$('timer').style.display='none';return;}
  var target=new Date(dt).getTime();if(isNaN(target))return;
  $('timer').style.display='block';$('event-name').textContent=name;
  function upd(){var now=Date.now();var diff=target-now;if(diff<=0){$('timer').innerHTML='🎉 Event has arrived!';$('event-name').textContent=name;stop();return;}
  var d=Math.floor(diff/86400000);var h=Math.floor((diff%86400000)/3600000);var m=Math.floor((diff%3600000)/60000);var s=Math.floor((diff%60000)/1000);
  $('timer').innerHTML=d+'d '+String(h).padStart(2,'0')+'h '+String(m).padStart(2,'0')+'m '+String(s).padStart(2,'0')+'s';}
  upd();iv=setInterval(upd,1000);}
function stop(){if(iv){clearInterval(iv);iv=null;}}""",
    "Set a countdown to any date — Christmas, New Year, a birthday, vacation, wedding, or product launch. This countdown timer shows days, hours, minutes and seconds remaining in real-time. Use the quick presets for popular holidays or enter your own custom date and event name."
)

# ====== TOOL 4: Online Stopwatch ======
t4 = page(
    "online-stopwatch",
    "Online Stopwatch & Timer",
    "Free online stopwatch with lap times. Start, stop, reset and record lap splits.",
    ["online stopwatch", "stopwatch timer", "lap timer", "free stopwatch", "count up timer"],
    """<div id="timer" class="timer-display">00:00:00.000</div>
<div style="text-align:center" class="btns">
<button class="timer-btn" id="startBtn" onclick="toggle()">Start</button>
<button class="timer-btn sec" onclick="lap()">Lap</button>
<button class="timer-btn sec" onclick="reset()">Reset</button>
</div>
<div id="laps" style="margin-top:20px"></div>""",
    """var running=false,startT=0,elapsed=0,raf=null,laps=[];
function $(id){return document.getElementById(id)}
function fmt(ms){var h=Math.floor(ms/3600000);var m=Math.floor((ms%3600000)/60000);var s=Math.floor((ms%60000)/1000);var ml=Math.floor(ms%1000);return String(h).padStart(2,'0')+':'+String(m).padStart(2,'0')+':'+String(s).padStart(2,'0')+'.'+String(ml).padStart(3,'0');}
function toggle(){if(running){running=false;$('startBtn').textContent='Resume';cancelAnimationFrame(raf);}
else{running=true;$('startBtn').textContent='Stop';startT=performance.now()-elapsed;tick();}}
function tick(){if(!running)return;elapsed=performance.now()-startT;$('timer').textContent=fmt(elapsed);raf=requestAnimationFrame(tick);}
function lap(){if(elapsed===0)return;laps.push(elapsed);var h='<div style="margin-top:6px"><b>Lap '+laps.length+':</b> '+fmt(elapsed);if(laps.length>1){var d=laps[laps.length-1]-laps[laps.length-2];h+=' <span style="color:var(--muted);font-size:.85rem">(+'+fmt(d)+')</span>';}h+='</div>';$('laps').innerHTML=h+laps.map(function(l,i){return '<div style="padding:6px 0;border-bottom:1px solid var(--line);font-size:.9rem">Lap '+(i+1)+': '+fmt(l)+'</div>';}).reverse().join('');}
function reset(){running=false;elapsed=0;laps=[];$('timer').textContent='00:00:00.000';$('startBtn').textContent='Start';$('laps').innerHTML='';cancelAnimationFrame(raf);}""",
    "A precision online stopwatch accurate to the millisecond. Use it for timing workouts, cooking, studying, games, experiments, or any activity. Features include start/stop/reset controls and lap timing with split times. Runs entirely in your browser with no ads in the tool area."
)

# ====== TOOL 5: Password Strength Checker ======
t5 = page(
    "password-strength-checker",
    "Password Strength Checker",
    "Check how strong your password is. Get instant feedback on security and suggestions to improve.",
    ["password strength checker", "how strong is my password", "password security", "password tester", "secure password check"],
    """<label class="label">Enter a password to test</label>
<input id="pw" type="text" placeholder="Type your password…" oninput="check()" style="font-size:1.1rem">
<div id="bar" style="margin-top:14px;height:8px;border-radius:4px;background:var(--line);overflow:hidden"><div id="barFill" style="height:100%;width:0%;transition:width .3s,border-radius:4px"></div></div>
<div id="result" style="margin-top:10px;font-weight:600;font-size:1rem"></div>
<div id="details" style="margin-top:14px"></div>""",
    """function $(id){return document.getElementById(id)}
function check(){var pw=$('pw').value;var score=0;var details=[];
if(pw.length===0){$('barFill').style.width='0%';$('result').textContent='';$('details').innerHTML='';return;}
if(pw.length>=8)score++;if(pw.length>=12)score++;if(pw.length>=16)score++;
if(/[a-z]/.test(pw))score++;if(/[A-Z]/.test(pw))score++;if(/[0-9]/.test(pw))score++;
if(/[^a-zA-Z0-9]/.test(pw))score++;
var lowers=(pw.match(/[a-z]/g)||[]).length;var uppers=(pw.match(/[A-Z]/g)||[]).length;
var nums=(pw.match(/[0-9]/g)||[]).length;var syms=(pw.match(/[^a-zA-Z0-9]/g)||[]).length;
var unique=new Set(pw.toLowerCase()).size;var repeat=pw.length-unique;
if(pw.length<6){score=Math.max(0,score-2);}
details.push('Length: '+pw.length+(pw.length>=12?' ✓':' (aim for 12+)'));
details.push('Unique chars: '+unique+(unique>=8?' ✓':' (more variety)'));
details.push('Lowercase: '+(lowers>0?lowers:'none'));
details.push('Uppercase: '+(uppers>0?uppers:'none'));
details.push('Numbers: '+(nums>0?nums:'none'));
details.push('Symbols: '+(syms>0?syms:'none'));
if(repeat>3)details.push('⚠ Repeated chars: '+repeat);
var pct=Math.min(100,Math.round(score/8*100));
var color,label;
if(pct<25){color='#ff6b6b';label='Very weak';}
else if(pct<50){color='#ffb84f';label='Weak';}
else if(pct<70){color='#4f8cff';label='Fair';}
else if(pct<90){color='#22d3a6';label='Strong';}
else{color='#22d3a6';label='Very strong';}
$('barFill').style.width=pct+'%';$('barFill').style.background=color;
$('result').innerHTML='<span style="color:'+color+'">'+label+'</span> ('+pct+'%)';
$('details').innerHTML=details.map(function(d){return '<div style="font-size:.85rem;color:var(--muted);padding:2px 0">'+d+'</div>';}).join('');}""",
    "Test the strength of any password instantly. This password strength checker analyzes length, character variety (uppercase, lowercase, numbers, symbols), uniqueness and repetition to give you a security score from 0-100%. Get actionable feedback on how to make your passwords stronger. Everything runs in your browser — your password is never sent anywhere."
)

# ====== TOOL 6: Number Base Converter ======
t6 = page(
    "number-base-converter",
    "Number Base Converter — Binary, Hex, Decimal, Octal",
    "Convert numbers between binary, hexadecimal, decimal and octal instantly.",
    ["number base converter", "binary converter", "hex to decimal", "decimal to binary", "hex converter", "binary to decimal"],
    """<label class="label">Enter a number</label>
<input id="num" type="text" placeholder="255" oninput="convert()">
<label class="label">Input base</label>
<div class="btns" style="margin-bottom:14px">
<button id="b10" onclick="setBase(10)" style="background:var(--acc)">Decimal (10)</button>
<button id="b16" onclick="setBase(16)">Hex (16)</button>
<button id="b2" onclick="setBase(2)">Binary (2)</button>
<button id="b8" onclick="setBase(8)">Octal (8)</button>
</div>
<div id="out"></div>""",
    """var curBase=10;
function $(id){return document.getElementById(id)}
function setBase(b){curBase=b;['b2','b8','b10','b16'].forEach(function(x){$(x).style.background='var(--card)';$(x).style.color='var(--ink)';$(x).style.border='1px solid var(--line)';});
var btn='b'+b;$(btn).style.background='var(--acc)';$(btn).style.color='#fff';$(btn).style.border='none';convert();}
function convert(){var v=$('num').value.trim();if(!v){$('out').innerHTML='';return;}
var d=parseInt(v,curBase);if(isNaN(d)){$('out').innerHTML='<div class="msg" style="background:rgba(255,107,107,.12);color:#ff6b6b">Invalid number for base '+curBase+'</div>';return;}
$('out').innerHTML=
row('Decimal (10)',''+d)+
row('Hexadecimal (16)','0x'+d.toString(16).toUpperCase())+
row('Binary (2)',d.toString(2))+
row('Octal (8)',d.toString(8))+
row('ASCII',d>=32&&d<=126?'"'+String.fromCharCode(d)+'"':'N/A');}
function row(label,val){return '<div style="margin-top:10px;padding:10px;background:#0b0d12;border-radius:8px"><span style="color:var(--muted);font-size:.8rem">'+label+'</span><br><code style="font-size:1rem;color:var(--acc);word-break:break-all">'+val+'</code></div>';}""",
    "Convert numbers between decimal, hexadecimal, binary and octal number systems. Enter a value in any base and instantly see the equivalent in all other bases. Includes ASCII character lookup for decimal values in the printable range. Essential for programmers, students learning number systems, and anyone working with digital data."
)

# ====== TOOL 7: Date Calculator (Days Between) ======
t7 = page(
    "date-calculator",
    "Date Calculator — Days Between Two Dates",
    "Calculate the number of days, weeks, months and years between any two dates.",
    ["date calculator", "days between dates", "days until", "date difference", "how many days between"],
    """<div class="row2">
<div><label class="label">Start date</label><input id="d1" type="date" oninput="calc()"></div>
<div><label class="label">End date</label><input id="d2" type="date" oninput="calc()"></div>
</div>
<div class="btns">
<button onclick="setPreset('today','+30')">30 days from now</button>
<button onclick="setPreset('today','+90')">90 days from now</button>
<button onclick="setPreset('today','+365')">1 year from now</button>
</div>
<div id="out" style="margin-top:16px"></div>""",
    """var today=new Date().toISOString().split('T')[0];
function $(id){return document.getElementById(id)}
$('d1').value=today;$('d2').value=today;
function setPreset(from,to){$('d1').value=today;var d=new Date();d.setDate(d.getDate()+parseInt(to.replace('+','')));$('d2').value=d.toISOString().split('T')[0];calc();}
function calc(){
  var a=$('d1').value,b=$('d2').value;if(!a||!b)return;
  var d1=new Date(a),d2=new Date(b);var diff=Math.abs(d2-d1);
  var days=Math.round(diff/86400000);var weeks=Math.floor(days/7);var remDays=days%7;
  var months=Math.abs((d2.getFullYear()-d1.getFullYear())*12+d2.getMonth()-d1.getMonth());
  var years=Math.abs(d2.getFullYear()-d1.getFullYear());
  var wkdays=countWeekdays(d1,d2);var weekends=days-wkdays;
  $('out').innerHTML=
    '<div class="result-box">'+days+' day'+(days!==1?'s':'')+'</div>'+
    '<div class="row2" style="margin-top:12px">'+
      '<div style="padding:12px;background:#0b0d12;border-radius:8px"><b>'+weeks+'</b> week'+(weeks!==1?'s':'')+' and '+remDays+' day'+(remDays!==1?'s':'')+'</div>'+
      '<div style="padding:12px;background:#0b0d12;border-radius:8px"><b>'+months+'</b> month'+(months!==1?'s':'')+'</div>'+
    '</div>'+
    '<div class="row2" style="margin-top:12px">'+
      '<div style="padding:12px;background:#0b0d12;border-radius:8px"><b>'+years+'</b> year'+(years!==1?'s':'')+'</div>'+
      '<div style="padding:12px;background:#0b0d12;border-radius:8px"><b>'+Math.round(diff/3600000)+'</b> hours</div>'+
    '</div>'+
    '<div class="row2" style="margin-top:12px">'+
      '<div style="padding:12px;background:#0b0d12;border-radius:8px"><b>'+wkdays+'</b> weekdays</div>'+
      '<div style="padding:12px;background:#0b0d12;border-radius:8px"><b>'+weekends+'</b> weekend days</div>'+
    '</div>';
}
function countWeekdays(d1,d2){if(d1>d2){var t=d1;d1=d2;d2=t;}var count=0;var d=new Date(d1);d.setHours(0,0,0,0);var end=new Date(d2);end.setHours(0,0,0,0);while(d<=end){var dow=d.getDay();if(dow!==0&&dow!==6)count++;d.setDate(d.getDate()+1);}return count;}""",
    "Calculate the exact number of days, weeks, months and years between any two dates. Also shows total hours, weekdays and weekend days. Useful for project planning, pregnancy due dates, event countdowns, subscription calculations, and travel planning."
)

# ====== TOOL 8: Mortgage Calculator ======
t8 = page(
    "mortgage-calculator",
    "Mortgage & Loan Payment Calculator",
    "Calculate monthly mortgage payments, total interest, and amortization schedule.",
    ["mortgage calculator", "loan payment calculator", "home loan calculator", "mortgage payment", "interest calculator"],
    """<div class="row2">
<div><label class="label">Loan amount ($)</label><input id="principal" type="text" value="300000" oninput="calc()"></div>
<div><label class="label">Interest rate (%)</label><input id="rate" type="text" value="6.5" oninput="calc()"></div>
</div>
<div class="row2">
<div><label class="label">Loan term (years)</label><input id="years" type="text" value="30" oninput="calc()"></div>
<div><label class="label">Down payment ($)</label><input id="down" type="text" value="60000" oninput="calc()"></div>
</div>
<div class="btns"><button onclick="calc()">Calculate</button></div>
<div id="out" style="margin-top:16px"></div>
<div id="schedule" style="margin-top:16px;max-height:300px;overflow-y:auto"></div>""",
    """function $(id){return document.getElementById(id)}
function calc(){
  var p=parseFloat($('principal').value)||0;var r=(parseFloat($('rate').value)||0)/100/12;
  var y=parseInt($('years').value)||30;var d=parseFloat($('down').value)||0;
  var loan=p-d;var n=y*12;
  if(!loan||!n){$('out').innerHTML='';return;}
  var mp=r>0?loan*(r*Math.pow(1+r,n))/(Math.pow(1+r,n)-1):loan/n;
  var total=mp*n;var interest=total-loan;
  $('out').innerHTML=
    '<div class="result-box">$'+mp.toFixed(2)+'<span style="font-size:.85rem;color:var(--muted)"> / month</span></div>'+
    '<div class="row3" style="margin-top:12px">'+
      '<div style="padding:12px;background:#0b0d12;border-radius:8px;text-align:center"><div style="color:var(--muted);font-size:.75rem">Total paid</div><div style="font-weight:700;color:var(--acc)">$'+total.toFixed(0)+'</div></div>'+
      '<div style="padding:12px;background:#0b0d12;border-radius:8px;text-align:center"><div style="color:var(--muted);font-size:.75rem">Total interest</div><div style="font-weight:700;color:var(--err)">$'+interest.toFixed(0)+'</div></div>'+
      '<div style="padding:12px;background:#0b0d12;border-radius:8px;text-align:center"><div style="color:var(--muted);font-size:.75rem">Loan amount</div><div style="font-weight:700">$'+loan.toFixed(0)+'</div></div>'+
    '</div>';
  // Show first 12 months amortization
  var bal=loan;var h='<table style="width:100%;font-size:.8rem;border-collapse:collapse;margin-top:10px"><tr style="color:var(--muted);border-bottom:1px solid var(--line)"><th style="padding:4px;text-align:left">Month</th><th style="text-align:right">Payment</th><th style="text-align:right">Principal</th><th style="text-align:right">Interest</th><th style="text-align:right">Balance</th></tr>';
  for(var i=1;i<=Math.min(n,12);i++){var intPay=bal*r;var princPay=mp-intPay;bal-=princPay;
    h+='<tr style="border-bottom:1px solid var(--line)"><td>'+i+'</td><td style="text-align:right">$'+mp.toFixed(2)+'</td><td style="text-align:right;color:var(--acc)">$'+princPay.toFixed(2)+'</td><td style="text-align:right;color:var(--err)">$'+intPay.toFixed(2)+'</td><td style="text-align:right">$'+bal.toFixed(2)+'</td></tr>';}
  if(n>12)h+='<tr><td colspan="5" style="text-align:center;color:var(--muted);padding:8px">… '+n+' months total</td></tr>';
  h+='</table>';$('schedule').innerHTML=h;
}""",
    "Calculate your monthly mortgage or loan payment instantly. Enter the home price, down payment, interest rate and loan term to see your monthly payment, total interest paid, and a full amortization schedule. This mortgage calculator helps you compare different loan scenarios and understand the true cost of financing."
)

# Write all tools
tools = [t1, t2, t3, t4, t5, t6, t7, t8]
for tool_html in tools:
    # Extract slug from the HTML content
    slug = tool_html.split('tools/')[1].split('"')[0]
    path = os.path.join(TOOLS_DIR, slug + ".html")
    with open(path, "w") as f:
        f.write(tool_html)
    print(f"✓ Built {slug}.html")

print(f"\n✓ Built {len(tools)} new tools")
