// Glossary word cards (sw.py build injects this only when the deck has a `glossary`).
// Hover, tap or focus a marked word for its card. The reader picks plain or original wording; saved per browser.
const GL=(()=>{const idx=new Map(),RK='studywright:gloss-register';
const key=s=>s.toLowerCase().replace(/\s+/g,' ').trim();
for(const e of (DECK.glossary||[]))for(const t of [e.term,...(e.aliases||[])])if(t&&!idx.has(key(t)))idx.set(key(t),e);
// longest phrase up to 4 words wins; a final word ending in s also tries the singular (same rule as sw.py gloss_find)
function find(text){const ws=[...text.matchAll(/[A-Za-z][A-Za-z'-]*/g)],out=[];
 for(let i=0;i<ws.length;){let hit=null;
  for(let n=Math.min(4,ws.length-i);n>0&&!hit;n--){const a=ws[i],b=ws[i+n-1],seg=text.slice(a.index,b.index+b[0].length);
   if(n>1&&!/^[A-Za-z'-]+(\s+[A-Za-z'-]+)*$/.test(seg))continue;
   const k=key(seg);let e=idx.get(k);if(!e&&/[^s]s$/.test(k))e=idx.get(k.slice(0,-1));
   if(e)hit={start:a.index,end:b.index+b[0].length,entry:e,n}}
  if(hit){out.push(hit);i+=hit.n}else i++}
 return out}
let reg='plain';try{reg=localStorage.getItem(RK)||'plain'}catch(e){}
const text=e=>reg==='plain'?(e.plain||e.def):(e.def||e.plain);
if(typeof document==='undefined'||!document.createTreeWalker||!idx.size)return{find,text};
const st=document.createElement('style');st.textContent=`.sw-gl{border-bottom:2px dotted currentColor;cursor:help}.sw-gl:focus{outline:2px solid #7aa2ff;outline-offset:2px}
.sw-gcard{position:fixed;z-index:9999;max-width:300px;box-sizing:border-box;padding:10px 12px;border-radius:10px;background:#1b2233;color:#eef;font:15px/1.4 system-ui,sans-serif;box-shadow:0 6px 24px #0008;opacity:0;pointer-events:none;transition:opacity .15s}
.sw-gcard.on{opacity:1}.sw-gcard b{display:block;margin-bottom:4px}
.sw-greg{position:fixed;right:8px;bottom:8px;z-index:9998;font:13px system-ui,sans-serif;padding:6px 10px;border-radius:8px;border:1px solid #fff4;background:#1b2233;color:#eef;cursor:pointer}
@media (prefers-reduced-motion:reduce){.sw-gcard{transition:none}}`;document.head.appendChild(st);
const card=document.createElement('div');card.className='sw-gcard';card.id='sw-gcard';card.setAttribute('role','tooltip');
const btn=document.createElement('button');btn.className='sw-greg';btn.dataset.nogloss='1';
const label=()=>{btn.textContent=reg==='plain'?'Word help: Plain, easier to read':'Word help: Original, as written';btn.title='Switch how word cards are worded'};
let cur=null;
function show(el){cur=el;const e=idx.get(el.dataset.k);card.innerHTML='';const b=document.createElement('b');b.textContent=e.term;card.append(b,document.createTextNode(text(e)));
 const vw=innerWidth,vh=innerHeight;card.style.width=Math.min(300,vw-16)+'px';card.style.left='0';card.style.top='0';card.classList.add('on');
 const r=el.getBoundingClientRect(),h=card.offsetHeight,w=card.offsetWidth;
 let top=r.top-h-8>=8?r.top-h-8:r.bottom+8;top=Math.max(8,Math.min(top,vh-h-8));
 const left=Math.max(8,Math.min(r.left+r.width/2-w/2,vw-w-8));card.style.left=left+'px';card.style.top=top+'px';el.setAttribute('aria-describedby','sw-gcard')}
function hide(){if(cur)cur.removeAttribute('aria-describedby');cur=null;card.classList.remove('on')}
btn.onclick=()=>{reg=reg==='plain'?'original':'plain';try{localStorage.setItem(RK,reg)}catch(e){}label();if(cur)show(cur)};
const SKIP='script,style,textarea,input,select,button,option,.sw-gl,.sw-gcard,[data-nogloss]';
function walk(root){if(root.nodeType===3){mark(root);return}if(root.nodeType!==1||root.closest(SKIP))return;
 const tw=document.createTreeWalker(root,NodeFilter.SHOW_TEXT),ns=[];while(tw.nextNode())ns.push(tw.currentNode);ns.forEach(mark)}
function mark(n){const p=n.parentElement;if(!p||!n.isConnected||p.closest(SKIP))return;const hits=find(n.data);if(!hits.length)return;
 const f=document.createDocumentFragment();let at=0;
 for(const h of hits){f.append(n.data.slice(at,h.start));const s=document.createElement('span');s.className='sw-gl';s.tabIndex=0;
  s.dataset.k=key(h.entry.term);s.textContent=n.data.slice(h.start,h.end);f.append(s);at=h.end}
 f.append(n.data.slice(at));n.replaceWith(f)}
const glOf=t=>t&&t.closest?t.closest('.sw-gl'):null;
document.addEventListener('mouseover',ev=>{const g=glOf(ev.target);if(g)show(g)});
document.addEventListener('mouseout',ev=>{const g=glOf(ev.target);if(g&&g===cur&&!g.contains(ev.relatedTarget)&&document.activeElement!==g)hide()});
document.addEventListener('focusin',ev=>{const g=glOf(ev.target);if(g)show(g)});
document.addEventListener('focusout',ev=>{if(ev.target===cur)hide()});
document.addEventListener('click',ev=>{const g=glOf(ev.target);if(g){ev.stopPropagation();if(!g.contains(document.activeElement))g.focus();show(g)}else if(ev.target!==btn)hide()},true);
document.addEventListener('keydown',ev=>{if(ev.key==='Escape')hide();const g=glOf(ev.target);if(g&&(ev.key==='Enter'||ev.key===' ')){ev.preventDefault();show(g)}});
addEventListener('scroll',hide,true);addEventListener('resize',hide);
function start(){document.body.append(card,btn);label();walk(document.body);
 new MutationObserver(ms=>{for(const m of ms){if(m.type==='characterData')mark(m.target);else m.addedNodes.forEach(walk)}}).observe(document.body,{childList:true,subtree:true,characterData:true})}
document.readyState==='loading'?document.addEventListener('DOMContentLoaded',start):start();
return{find,text,show,hide}})();
