// Checks a built lesson game's generator and answer keys independently of the page code.
// usage: node verify_lesson.js games/<slug>.html [runs] [banned-sets.json]
// banned-sets.json (optional, kept outside the repo) is a list of raw data sets that must never come out.
const fs=require('fs'),vm=require('vm');
const [file,runsArg,bannedFile]=process.argv.slice(2),RUNS=+(runsArg||3000);
const src=fs.readFileSync(file,'utf8').match(/<script>([\s\S]*)<\/script>/)[1];
const el=()=>({set innerHTML(v){},get innerHTML(){return''},querySelectorAll:()=>[],classList:{toggle(){}},focus(){}});
const ctx={document:{getElementById:el,querySelector:()=>null,createElement:el,body:{appendChild(){}}},localStorage:{getItem:()=>null,setItem(){}},setInterval(){},setTimeout(){},console,Math,JSON,Date,Number,String,Array,Set,Object,Error,URL:{},Blob:function(){}};
vm.createContext(ctx);vm.runInContext(src.replace(/\nconst (DECK|KINDS|SK)\b/g,'\nvar $1').replace(/\nlet S;/,'\nvar S;'),ctx);
const banned=new Set((bannedFile?JSON.parse(fs.readFileSync(bannedFile,'utf8')):[]).map(v=>v.slice().sort((a,b)=>a-b).join(',')));
let sets=[],fails=[];const og5=ctx.gen5,oga=ctx.genAround;
ctx.gen5=(...a)=>{const v=og5(...a);sets.push(v);return v};ctx.genAround=(...a)=>{const v=oga(...a);sets.push(v);return v};
// independent maths
const mean=v=>v.reduce((a,b)=>a+b,0)/v.length,mad=v=>{const m=mean(v);return Math.round(v.reduce((a,x)=>a+Math.abs(x-m),0)/v.length*1e6)/1e6};
function okProfile(v){return v.length===5&&v.every(Number.isInteger)&&Number.isInteger(mean(v))&&Math.abs(mad(v)*10-Math.round(mad(v)*10))<1e-9&&mad(v)>0}
const F=(m)=>fails.length<20&&fails.push(m);
const kinds=[...new Set(ctx.DECK.map.map(l=>l.kind))];let items=0;
for(let r=0;r<RUNS;r++)for(const k of kinds)for(const solo of [false,true]){sets=[];const e=ctx.KINDS[k](solo);
 for(const v of sets){if(!okProfile(v))F(k+' bad profile '+v);if(banned.has(v.slice().sort((a,b)=>a-b).join(',')))F(k+' produced a banned set '+v)}
 for(const p of e.parts){items++;
  if(p.type==='mc'){const ok=p.choices.filter(c=>c.ok);if(ok.length!==1)F(k+' mc has '+ok.length+' right');if(new Set(p.choices.map(c=>c.t)).size!==p.choices.length)F(k+' duplicate choices');}
  if(p.type==='num'){const V=p.steps||(p.html.match(/class="data">([\d, ]+)</)||[])[1]?.split(',').map(Number);
   if(!V){F(k+' no data');continue}
   const m=mean(V),d=V.map(x=>Math.abs(x-m)),D=d.reduce((a,b)=>a+b,0);
   const want={mean:m,sum:V.reduce((a,b)=>a+b,0),MAD:mad(V),'sum of distances':D};
   p.boxes.forEach(b=>{let w=want[b.label];if(b.label.startsWith('|')){w=Math.abs(+b.label.slice(1).split(' ')[0]-m)}
    if(w===undefined)F(k+' unknown box '+b.label);else if(Math.abs(w-b.ans)>1e-9)F(k+' '+b.label+' key '+b.ans+' expected '+w+' for '+V);
    for(const s of b.slips)if(Math.abs(s.x-b.ans)<1e-9)F(k+' slip equals answer '+b.label+' '+V)})}
  // read/both: check the right choice against the figures shown in the table
  const rows=[...p.html.matchAll(/<tr><th>([^<]+)<\/th><td>([\d.]+)<\/td><td>([\d.]+)<\/td><\/tr>/g)].map(x=>({n:x[1],m:+x[2],v:+x[3]}));
  if(k==='read'){const [a,b]=rows;if(!(a.v>b.v&&a.m<b.m))F('read figures wrong '+JSON.stringify(rows));if(!/more spread out/.test(p.choices.find(c=>c.ok).t))F('read key')}
  if(k==='both'&&rows.length===2){const [a,b]=rows,t=p.choices.find(c=>c.ok).t;const exp=`a ${a.m>b.m?'higher':'lower'} mean and ${a.v>b.v?'more':'less'} variability`;if(t!==exp)F('both key '+t+' vs '+exp)}
  if(k==='both'&&rows.length===4){const best=rows.filter(r=>rows.every(o=>o===r||(r.m>o.m||Math.abs(r.m-o.m)<9)&&true));const hi=rows.slice().sort((x,y)=>y.m-x.m).slice(0,2),pickR=hi.sort((x,y)=>x.v-y.v)[0];
   if(p.choices.find(c=>c.ok).t!==pickR.n)F('both pick key');const lo=rows.slice().sort((x,y)=>x.m-y.m).slice(0,2);if(Math.min(...hi.map(r=>r.m))<=Math.max(...lo.map(r=>r.m)))F('both pick means overlap')}}}
console.log(`${RUNS} runs x ${kinds.length} kinds x 2 paths, ${items} items checked`);
if(fails.length){console.log('FAIL\n'+fails.join('\n'));process.exit(1)}console.log('ok: every set fits the profile, every key matches, no banned set');
