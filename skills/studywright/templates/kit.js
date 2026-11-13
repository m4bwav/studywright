// studywright kit: the hero look, the one hero drawing routine, the hero builder and the notes prompt.
// sw.py injects this file into every template, so a hero looks the same in every game.
const Kit=(()=>{const K={still:false};const esc=s=>String(s).replace(/[&<>"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
const LOOK={skin:['#f6d3b3','#e0ac7e','#b9794f','#8a5233','#5c3820'],
 hair:{Black:'#1c1c22',Brown:'#5a3418',Blond:'#e6c35c',Red:'#b8401c',Silver:'#d8dce6',Blue:'#3a7bd5',Pink:'#e56fb0',Green:'#3fae5a'},
 style:['Short','Long','Spiky','Bun','Mohawk','Ponytail','Curly','Bald'],
 outfit:{Teal:'#2bb3a8',Crimson:'#c0304a',Forest:'#3b8a3e',Royal:'#4a5bd8',Gold:'#d9a520',Violet:'#8a4fd0',Charcoal:'#4a4f5a',Sky:'#4aa8e0',Rose:'#e07a9a',Snow:'#e8ecf2'},
 hat:['Class','None','Cap','Crown','Hood','Headband'],
 cape:['None','Crimson','Royal','Gold','Violet','Forest','Charcoal','Snow'],
 face:['Smile','Grin','Serious','Freckles'],
 gear:{Scholar:['Quill','Lantern','Tome'],Ranger:['Bow','Spear','Slingshot'],Knight:['Sword','Hammer','Lance'],Mage:['Staff','Wand','Orb']},
 pet:['None','Owl','Fox','Cat','Dog','Rabbit','Parrot','Turtle','Dragonling','Frog','Robot']};
const PETI={Owl:'🦉',Fox:'🦊',Cat:'🐈',Dragonling:'🐉',Frog:'🐸',Dog:'🐕',Rabbit:'🐇',Parrot:'🦜',Turtle:'🐢',Robot:'🤖'};
const defLook=h=>{const n=[...String(h.name||'Hero')].reduce((a,c)=>a+c.charCodeAt(0),0),pick=(a,k)=>a[(n+k)%a.length];return{skin:pick(LOOK.skin,1),hair:pick(Object.keys(LOOK.hair).slice(0,6),2),style:pick(LOOK.style.slice(0,4),3),outfit:pick(Object.keys(LOOK.outfit).slice(0,7),4),gear:(LOOK.gear[h.cls]||LOOK.gear.Scholar)[0],pet:'None'}};
// One drawing routine for the map, the HUD and the builder, so the hero looks the same everywhere.
// (x,y) is the point between the feet; u is the size of one drawing unit (the hero is about 32 units tall).
function drawHero(c,x,y,u,h,t,walk,face,sx=1,sy=1){const L=h.look||defLook(h),sk=L.skin,hr=LOOK.hair[L.hair]||'#333',of=LOOK.outfit[L.outfit]||'#888',cp=LOOK.outfit[L.cape];
 const sw=walk?Math.sin(t*15):0,bob=walk||K.still?0:Math.sin(t*2.4)*.45,back=face==='u',ex=face==='l'?-1.3:face==='r'?1.3:0;
 const R=(a,b,w,hh,col,r)=>{c.fillStyle=col;if(r&&c.roundRect){c.beginPath();c.roundRect(a,b,w,hh,r);c.fill()}else c.fillRect(a,b,w,hh)};
 const C=(a,b,r,col)=>{c.fillStyle=col;c.beginPath();c.arc(a,b,r,0,7);c.fill()};
 const P=(pts,col)=>{c.fillStyle=col;c.beginPath();pts.forEach((p,i)=>i?c.lineTo(p[0],p[1]):c.moveTo(p[0],p[1]));c.closePath();c.fill()};
 const Ln=(a,b,d,e,col,w)=>{c.strokeStyle=col;c.lineWidth=w;c.lineCap='round';c.beginPath();c.moveTo(a,b);c.lineTo(d,e);c.stroke()};
 c.save();c.translate(x,y);c.scale(u,u);c.fillStyle='#0005';c.beginPath();c.ellipse(0,0,7.5,2.4,0,0,7);c.fill();c.scale(sx,sy);c.translate(0,bob);
 const cape=()=>{if(cp)P([[-5.5,-18],[5.5,-18],[8-sw,-3],[-8-sw,-3]],cp)};
 const gear=()=>{const gx=back?-7.2:7.2,gy=-10-sw*1.2,g=L.gear;
  if(g==='Quill'){Ln(gx,gy,gx+3,gy-9,'#f4f4f4',1.2)}else if(g==='Lantern'){R(gx-2,gy,4,5,'#ffd166',1);Ln(gx,gy,gx,gy-2,'#553',.6)}else if(g==='Tome'){R(gx-2.5,gy-1,5,6.5,'#7a2a2a',.6);R(gx-1.5,gy,3,.8,'#ffd166')}
  else if(g==='Bow'){c.strokeStyle='#8a5a2a';c.lineWidth=1.2;c.beginPath();c.arc(gx-2,gy-3,8,-1.1,1.1);c.stroke();Ln(gx+1.6,gy-10,gx+1.6,gy+4,'#ddd',.4)}
  else if(g==='Spear'){Ln(gx,gy+7,gx,gy-16,'#8a5a2a',1.1);P([[gx-1.8,gy-15],[gx,gy-20],[gx+1.8,gy-15]],'#cfd6e4')}
  else if(g==='Slingshot'){Ln(gx,gy+3,gx,gy-3,'#8a5a2a',1.2);Ln(gx,gy-3,gx-2.5,gy-7,'#8a5a2a',1.2);Ln(gx,gy-3,gx+2.5,gy-7,'#8a5a2a',1.2)}
  else if(g==='Sword'){Ln(gx,gy,gx,gy-15,'#e3e8f4',1.6);Ln(gx-2.6,gy-1,gx+2.6,gy-1,'#b08d3a',1.3)}
  else if(g==='Hammer'){Ln(gx,gy+5,gx,gy-12,'#8a5a2a',1.2);R(gx-3.5,gy-15,7,4,'#9aa0ad',.8)}
  else if(g==='Lance'){P([[gx-1.2,gy+7],[gx,gy-22],[gx+1.2,gy+7]],'#ccd2e2')}
  else if(g==='Staff'){Ln(gx,gy+8,gx,gy-15,'#8a5a2a',1.2);C(gx,gy-16.5,2.4,'#7cf')}
  else if(g==='Wand'){Ln(gx,gy,gx+3,gy-7,'#eee',.9);C(gx+3,gy-7,1.2,'#ffd166')}
  else if(g==='Orb'){C(gx,gy-1,3,'#b388ff');C(gx-.8,gy-1.8,.9,'#fff8')}};
 if(!back)cape();
 R(-4.4,-8,3.6,8-Math.max(0,sw)*2.2,'#2b2f3a',1);R(.8,-8,3.6,8-Math.max(0,-sw)*2.2,'#2b2f3a',1);
 R(-6,-19,12,12,of,3);R(-6,-10.5,12,1.6,'#0004');R(-1,-19,2,8.5,'#fff2');
 R(-8.6,-18+sw,3,8.5,of,1.4);C(-7.1,-9+sw,1.7,sk);R(5.6,-18-sw,3,8.5,of,1.4);C(7.1,-9-sw,1.7,sk);
 gear();C(0,-24.5,6.4,sk);
 const st=L.style,top=()=>{c.fillStyle=hr;c.beginPath();c.arc(0,-25.2,6.7,Math.PI*1.02,-.02*Math.PI);c.closePath();c.fill()};
 if(back){if(st!=='Bald')C(0,-24.8,6.7,hr);else C(0,-24.5,6.4,sk)}
 if(st==='Short'||st==='Bun'||st==='Ponytail'||st==='Long')top();
 if(st==='Long'){R(-7,-26,2.4,10,hr,1);R(4.6,-26,2.4,10,hr,1)}
 if(st==='Bun')C(0,-32.4,2.8,hr);
 if(st==='Ponytail'){R(5,-27,3.4,2.2,hr,1);R(6.6,-27,2.2,9,hr,1)}
 if(st==='Spiky')P([[-6.6,-25],[-6,-32],[-3.4,-28.4],[-1.6,-34],[0,-29],[1.8,-34],[3.4,-28.4],[6,-32],[6.6,-25]],hr);
 if(st==='Mohawk')R(-1.4,-34,2.8,10,hr,1.2);
 if(st==='Curly')[[-5.6,-27],[-3,-30],[0,-31],[3,-30],[5.6,-27],[-6.4,-24],[6.4,-24]].forEach(p=>C(p[0],p[1],2.3,hr));
 if(!back){C(-2.3+ex,-24,1,'#1c1c22');C(2.3+ex,-24,1,'#1c1c22');C(-2+ex,-24.3,.35,'#fff');C(2.6+ex,-24.3,.35,'#fff');const f=L.face||'Smile';
  if(f==='Grin')R(-2+ex,-21.6,4,1.6,'#fff',.7);else if(f==='Serious')Ln(-1.6+ex,-20.8,1.6+ex,-20.8,'#522',.6);else{c.strokeStyle='#522';c.lineWidth=.6;c.beginPath();c.arc(ex,-22,2.2,.25*Math.PI,.75*Math.PI);c.stroke()}
  if(f==='Freckles')[[-3.6,-22.4],[-4.4,-21.6],[3.6,-22.4],[4.4,-21.6]].forEach(p=>C(p[0]+ex,p[1],.35,'#8a4a2a'))}
 const hat=L.hat||'Class',hc=hat==='Class'?h.cls:hat;
 if(hc==='Mage'){P([[-7.5,-28],[0,-41],[7.5,-28]],of);C(0,-41,1.3,'#ffd166');R(-8.5,-29,17,2,of,1)}
 else if(hc==='Knight'){c.fillStyle='#c0c8d8';c.beginPath();c.arc(0,-25.4,7,Math.PI,0);c.closePath();c.fill();R(-7,-26,14,1.6,'#9aa3b8');R(-.8,-36,1.6,5,of)}
 else if(hc==='Ranger'||hc==='Hood'){c.fillStyle=hc==='Hood'?of:'#3a5a2a';c.beginPath();c.arc(0,-25.4,7.4,Math.PI,0);c.closePath();c.fill();c.beginPath();c.moveTo(-3.4,-31.4);c.lineTo(0,-36);c.lineTo(3.4,-31.4);c.closePath();c.fill()}
 else if(hc==='Scholar'){P([[-8,-31],[0,-34.5],[8,-31],[0,-27.5]],'#20222c');R(-4.5,-31,9,3,'#20222c');Ln(6,-31,7,-27,'#ffd166',.6)}
 else if(hc==='Cap'){c.fillStyle=of;c.beginPath();c.arc(0,-26,6.9,Math.PI,0);c.closePath();c.fill();R(back?-9:1,-27.2,8.5,1.8,of,.9)}
 else if(hc==='Crown')P([[-5.5,-29],[-5.5,-35],[-2.8,-32],[0,-36.5],[2.8,-32],[5.5,-35],[5.5,-29]],'#ffd166');
 else if(hc==='Headband')R(-6.6,-28.4,13.2,1.8,of,.6);
 if(back)cape();c.restore()}
function heroCanvas(h,w,hh,u){const cv=document.createElement('canvas');cv.width=w;cv.height=hh;drawHero(cv.getContext('2d'),w/2,hh-6,u,h,0,false,'d');return cv}
const IMG=new Map();function img(h,w=96){const hh=Math.round(w*1.25),key=w+h.cls+JSON.stringify(h.look||h.name);try{if(!IMG.has(key))IMG.set(key,`<img class="avatar" alt="" width="${w}" height="${hh}" src="${heroCanvas(h,w*2,hh*2-8,w*2/40).toDataURL()}">`)}catch(e){return''}return IMG.get(key)}
const CLS={Scholar:'📜',Ranger:'🏹',Knight:'🛡️',Mage:'🔮'};
const TIPS={cls:'Your class gives one special power.',gear:'What your hero carries. It shows on the map.',skin:'Skin tone.',hair:'Hair colour.',style:'Hair style.',face:'Expression.',outfit:'Outfit colour.',hat:'"Class" is the hat that comes with your class.',cape:'A cape flows behind you when you walk.',pet:'A companion that travels with you.'};
if(!document.getElementById('hk-css')){const st=document.createElement('style');st.id='hk-css';st.textContent='.hk{display:flex;gap:16px;flex-wrap:wrap}.hk-pv{text-align:center}.hk-pv canvas{background:radial-gradient(#2b3560,#141a30);border-radius:14px}.hk-o{display:flex;gap:6px;flex-wrap:wrap;margin:4px 0 10px}.hk-o button{padding:6px 10px;font-size:14px;width:auto}.hk-c{display:grid;grid-template-columns:1fr 1fr;gap:8px;margin:6px 0 10px}.hk-sw{display:inline-block;width:16px;height:16px;border-radius:50%;vertical-align:-3px;border:1px solid #0006}.hk button.hk-sel{outline:2px solid #7bd389;background:#2b3560}.hk-t{opacity:.75;font-size:.86em}.hk input{font:inherit;width:100%;padding:10px 12px;border-radius:10px;border:1px solid #36426b;background:#0f1428;color:#e8ecf8}.hk-r{display:flex;gap:8px;flex-wrap:wrap;margin-top:12px}.hk-r button{width:auto}';document.head.appendChild(st)}
let raf=0;
// builder({mount:html=>rootElement, done:({name,cls,look})=>..., back:fn|null, edit:hero|null, perks:{Class:'text'}, sound:{click,coin}, extra:[{label,fn}]})
function builder(o){const edit=o.edit,perks=o.perks||{},snd=o.sound||{},beep=k=>{try{snd[k]&&snd[k]()}catch(e){}};
 const st=edit?{cls:edit.cls,name:edit.name,look:{hat:'Class',cape:'None',face:'Smile',...(edit.look||defLook(edit))}}:{cls:'Ranger',name:'',look:{skin:LOOK.skin[1],hair:'Brown',style:'Short',outfit:'Forest',gear:'Bow',pet:'None',hat:'Class',cape:'None',face:'Smile'}};
 const swatch=(k,v)=>k==='skin'?`<span class="hk-sw" style="background:${v}"></span>`:k==='hair'?`<span class="hk-sw" style="background:${LOOK.hair[v]}"></span> ${v}`:(k==='outfit'||k==='cape')&&LOOK.outfit[v]?`<span class="hk-sw" style="background:${LOOK.outfit[v]}"></span> ${v}`:k==='pet'&&PETI[v]?PETI[v]+' '+v:v;
 const opt=(k,vals,lab)=>`<div class="hk-t"><b>${lab}</b> · ${TIPS[k]}</div><div class="hk-o">${vals.map(v=>`<button data-k="${k}" data-v="${esc(v)}" class="${st.look[k]===v?'hk-sel':''}">${swatch(k,v)}</button>`).join('')}</div>`;
 function draw(){const y=window.scrollY,root=o.mount(`<div class="card"><h1>${edit?'Change your hero':'Create your hero'}</h1><p class="hk-t">This hero is yours in every studywright game: same name, same look, same level and gold.</p>
  <div class="hk"><div class="hk-pv"><canvas data-hk="pv" width="170" height="210"></canvas><div class="hk-t" data-hk="pn"></div><div class="hk-r" style="justify-content:center"><button data-hk="rnd">🎲 Surprise me</button></div></div>
  <div style="flex:1;min-width:260px">${edit?'':'<input type="text" data-hk="hn" maxlength="24" placeholder="Hero name" autocomplete="off" value="'+esc(st.name)+'">'}
  <div class="hk-t" style="margin-top:8px"><b>Class</b> · ${TIPS.cls}</div><div class="hk-c">${Object.keys(CLS).map(c=>`<button data-c="${c}" class="${st.cls===c?'hk-sel':''}" ${edit?'disabled':''}>${CLS[c]} <b>${c}</b>${perks[c]?'<br><span class="hk-t">'+perks[c]+'</span>':''}</button>`).join('')}</div>
  ${opt('gear',LOOK.gear[st.cls],'Weapon or tool')}${opt('outfit',Object.keys(LOOK.outfit),'Outfit')}${opt('hat',LOOK.hat,'Hat')}${opt('cape',LOOK.cape,'Cape')}${opt('skin',LOOK.skin,'Skin')}${opt('hair',Object.keys(LOOK.hair),'Hair colour')}${opt('style',LOOK.style,'Hair style')}${opt('face',LOOK.face,'Face')}${opt('pet',LOOK.pet,'Companion')}
  <div class="hk-r"><button class="go" data-hk="mk">${edit?'Save look ▶':'Create hero ▶'}</button>${o.back?'<button data-hk="bk">Back</button>':''}${(o.extra||[]).map((x,i)=>`<button data-x="${i}">${esc(x.label)}</button>`).join('')}</div></div></div></div>`)||document.body;
  const q=k=>root.querySelector('[data-hk="'+k+'"]'),cvs=q('pv'),pc=cvs.getContext('2d');cancelAnimationFrame(raf);
  const anim=t=>{if(!cvs.isConnected)return;t/=1000;const ph=Math.floor(t/2.2)%4;pc.clearRect(0,0,170,210);drawHero(pc,85,188,4.6,{name:st.name||'Hero',cls:st.cls,look:st.look},t,ph%2===1,['d','r','u','l'][ph]);const pe=PETI[st.look.pet];if(pe){pc.font='30px "Segoe UI Emoji",sans-serif';pc.fillText(pe,8,196)}raf=requestAnimationFrame(anim)};raf=requestAnimationFrame(anim);
  const pn=()=>{q('pn').innerHTML=`<b>${esc(st.name||'Your hero')}</b> the ${st.cls}`};pn();
  if(!edit)q('hn').oninput=e=>{st.name=e.target.value;pn()};
  const redraw=()=>{const sc=root.scrollTop;draw();root.scrollTop=sc;window.scrollTo(0,y)};
  root.querySelectorAll('[data-c]').forEach(b=>b.onclick=()=>{st.cls=b.dataset.c;st.look.gear=LOOK.gear[st.cls][0];beep('click');redraw()});
  root.querySelectorAll('[data-k]').forEach(b=>b.onclick=()=>{st.look[b.dataset.k]=b.dataset.v;beep('click');redraw()});
  root.querySelectorAll('[data-x]').forEach(b=>b.onclick=()=>o.extra[+b.dataset.x].fn());
  q('rnd').onclick=()=>{const pk=a=>a[Math.floor(Math.random()*a.length)];Object.assign(st.look,{skin:pk(LOOK.skin),hair:pk(Object.keys(LOOK.hair)),style:pk(LOOK.style),outfit:pk(Object.keys(LOOK.outfit)),hat:pk(LOOK.hat),cape:pk(LOOK.cape),face:pk(LOOK.face),gear:pk(LOOK.gear[st.cls]),pet:pk(LOOK.pet)});beep('coin');redraw()};
  q('mk').onclick=()=>{const n=(st.name||'').trim();if(!n){const i=q('hn');if(i){i.focus();i.placeholder='Name your hero first'}return}o.done({name:n,cls:st.cls,look:{...st.look}})};
  if(o.back)q('bk').onclick=o.back}
 draw()}
// ---------- every play leaves a log (the JSON record) and a prompt that hands the results to the notes ----------
function notesPrompt(R,fname){const miss=R.first_try_misses||[],a=R.questions_total-miss.length,h=R.hero||{},un=R.unseen||[];
 return `Use the studywright skill to update the study notes with this play.
1. Run "sw.py records" to file the play log ${fname} from Downloads (if the file is missing, use the results below).
2. Update records/INDEX.md, ai-docs/HANDOFF.md and ai-docs/log.md: what was missed, which ideas look shaky, and what the next game should re-test.
3. Tell me in a few lines what to review before the test.

Results: ${R.title} (deck ${R.deck}${R.mode?', '+R.mode+' mode':''}), hero ${h.name||'?'}, ${String(R.finished).slice(0,16).replace('T',' ')} UTC${R.elapsed_sec?', '+Math.round(R.elapsed_sec/60)+' min':''}.
First try: ${R.score_first_try}% (${a} of ${R.questions_total}).${R.deck_total?' Mastered '+R.mastered+' of '+R.deck_total+'. Not reached: '+un.length+(un.length?' ('+[...new Set(un.map(u=>u.topic))].join('; ')+')':'')+'.':''}${R.notes_read?'\nSignposts read: '+(R.notes_read.join(', ')||'none')+'.':''}${R.boss&&!R.boss.skipped?'\nBoss round: '+R.boss.hits+' of '+R.boss.questions+' in time.':''}${R.route?'\nRoute: '+R.route.join(', ')+'.':''}
Missed on the first try:
${miss.map(m=>`- [${m.topic||''}] ${m.q||''}${m.answer?' -> '+m.answer:''}${(m.tries||[]).length?' (answered: '+m.tries.map(t=>'"'+t.given+'" '+(t.ok?'ok':'wrong')).join(', ')+')':''}`).join('\n')||'- nothing'}`}
function copyText(t,btn){const done=()=>{btn.textContent='Copied ✔ Paste it to your AI helper'};const fb=()=>{const ta=document.getElementById('np');ta.focus();ta.select();try{document.execCommand('copy');done()}catch(e){}};try{navigator.clipboard.writeText(t).then(done,fb)}catch(e){fb()}}
function notesHtml(R,fname){return `<h2>For the grown-up: log and notes prompt</h2><p class="hk-t">The play log was saved to Downloads as <b>${esc(fname)}</b>. Copy this prompt and paste it to your AI helper so the study notes get updated with these results.</p><textarea id="np" readonly style="width:100%;height:150px;background:#0f1428;color:#e8ecf8;border:1px solid #36426b;border-radius:10px;padding:8px;font:13px/1.35 ui-monospace,Consolas,monospace">${esc(notesPrompt(R,fname))}</textarea><div class="hk-r"><button class="go" id="cp">📋 Copy the notes prompt</button></div>`}
function notesWire(R,fname){const b=document.getElementById('cp');if(b)b.onclick=()=>copyText(notesPrompt(R,fname),b)}
return Object.assign(K,{LOOK,PETI,defLook,drawHero,heroCanvas,img,builder,notesPrompt,notesHtml,notesWire})})();
