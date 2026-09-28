import assert from 'node:assert/strict';
import fs from 'node:fs';
import path from 'node:path';
import vm from 'node:vm';
import {fileURLToPath} from 'node:url';

const root=path.dirname(path.dirname(fileURLToPath(import.meta.url)));
const html=fs.readFileSync(path.join(root,'liquiditaetsplanung/assets/padlet/liquiditaets-padlet.html'),'utf8');
const script=html.match(/<script>([\s\S]*?)<\/script>/)[1].replace(/\binit\(\);\s*$/,'');
const context=vm.createContext({Intl,Date,Number,JSON});
vm.runInContext(script,context);
const base=()=>({
 schemaVersion:2,stichtag:'2026-09-28',bank:0,kasse:0,kkfrei:0,passivaI:0,passivaII:0,vollstaendig:true,
 ein:[{label:'Eingang',w:[0,0,0]}],aus:[{label:'Ausgang',w:[0,0,0]}],indizien:[false,false],
});
let count=0;
function check(name,run){run();count++;console.log(`OK ${name}`);}
check('fehlende Angaben ergeben keine Freigabe',()=>{
 const x=base();x.bank=null;x.vollstaendig=false;const r=context.calculateLiquidity(x);
 assert(r.missing.includes('bank'));assert(r.missing.includes('Abgleich mit Belegen'));
 assert.match(r.result[1],/OFFEN/);assert.notEqual(r.result[0],'ok');
});
check('belegter Nullbetrag bleibt Null; Nenner null ist nicht anwendbar',()=>{
 const r=context.calculateLiquidity(base());assert.equal(r.missing.length,0);assert.equal(r.quote,null);
 assert.equal(r.luecke,0);assert.notEqual(r.result[0],'ok');
});
check('Zufluss in erstem Siebentageabschnitt wird berücksichtigt',()=>{
 const x=base();x.passivaI=100;x.ein[0].w=[100,0,0];x.aus[0].w=[100,0,0];
 const r=context.calculateLiquidity(x);assert.equal(r.aII,100);assert.equal(r.luecke,0);assert.equal(r.liqE[2],0);
});
check('Zahlung auf Altschuld wird nicht nochmals Passiva II',()=>{
 const x=base();x.bank=100;x.passivaI=100;x.aus[0].w=[100,0,0];
 const r=context.calculateLiquidity(x);assert.equal(r.sumP,100);assert.equal(r.pII,0);assert.equal(r.luecke,0);
});
check('nicht eingeplante fällige Schuld bleibt im Status',()=>{
 const x=base();x.passivaI=100;const r=context.calculateLiquidity(x);
 assert.equal(r.liqE[2],0);assert.equal(r.luecke,100);assert.match(r.result[1],/UNTERDECKUNG/);
});
check('neue Fälligkeiten und Eingang in dritter Periode werden symmetrisch erfasst',()=>{
 const x=base();x.bank=40;x.passivaI=70;x.passivaII=50;x.ein[0].w=[10,20,30];
 const r=context.calculateLiquidity(x);assert.equal(r.sumP,120);assert.equal(r.sumAk,100);assert.equal(r.luecke,20);
 assert.equal(r.quote,20/120);
});
check('5-Prozent-Lücke führt nicht zu automatischer Entwarnung',()=>{
 const x=base();x.bank=95;x.passivaI=100;const r=context.calculateLiquidity(x);
 assert.equal(r.quote,0.05);assert.notEqual(r.result[0],'ok');assert.match(r.result[1],/rechtlich prüfen/);
});
check('ein einziges Indiz erhält dieselbe offene Gesamtwürdigung wie mehrere',()=>{
 const x=base();x.indizien=[true,false];const one=context.calculateLiquidity(x);
 x.indizien=[true,true];const two=context.calculateLiquidity(x);
 assert.deepEqual(one.result,two.result);assert.match(one.result[1],/Gesamtwürdigung/);
});
check('ungültige und negative Eingaben werden offengelegt',()=>{
 const x=base();x.stichtag='2026-02-30';x.passivaII=-10;const r=context.calculateLiquidity(x);
 assert(r.missing.includes('gültiger Stichtag'));assert(r.missing.includes('passivaII'));
});
check('späterer Zufluss verdeckt negativen früheren Wochenbestand nicht',()=>{
 const x=base();x.aus[0].w=[100,0,0];x.ein[0].w=[0,0,100];x.passivaII=100;
 const r=context.calculateLiquidity(x);assert.equal(r.liqE[0],-100);assert.equal(r.liqE[2],0);
 assert.notEqual(r.result[0],'ok');
});
check('unbestätigter Altdatenimport darf keine geprüfte Statusrechnung vortäuschen',()=>{
 const x=base();delete x.schemaVersion;delete x.passivaI;delete x.passivaII;
 context.loadState(x);const r=vm.runInContext('calculateLiquidity(state)',context);
 assert(r.missing.includes('passivaI'));assert(r.missing.includes('passivaII'));
 assert(r.missing.includes('Abgleich mit Belegen'));
});
console.log(`${count} Verhaltenstests bestanden.`);
