// Tests the distributed ZIP through file://, not a development server.
import assert from 'node:assert/strict';
import {execFileSync} from 'node:child_process';
import {mkdtemp, writeFile, readFile, mkdir} from 'node:fs/promises';
import {tmpdir} from 'node:os';
import {join, resolve, dirname} from 'node:path';
import {fileURLToPath, pathToFileURL} from 'node:url';

let playwright;
try { playwright = await import(process.env.PLAYWRIGHT_MODULE || 'playwright'); }
catch (error) {
  if (process.env.PLAYWRIGHT_MODULE) throw error;
  playwright = await import(pathToFileURL(join(process.env.HOME, '.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright/index.mjs')).href);
}
const root = resolve(dirname(fileURLToPath(import.meta.url)), '..');
const temp = await mkdtemp(join(tmpdir(), 'grundstueck-website-'));
const python = process.env.PYTHON || 'python3';
const sample = {
  profile: {profile_id:'fixture',name:'Münster',state:'Nordrhein-Westfalen',municipality_code:'05515000',center:[51.9607,7.6261],bounds:[7.45,51.8,7.85,52.1]},
  case_id:'DATEI-42',purpose:'Nachweis für eine Leitungsfläche.',specific_interest:'Prüfung eines gesonderten Nutzungsrechts.',
  sender_organisation:'Änderbare Wasserwerke',recipients:{kataster:'Katasterstelle'},
  selected_parcels:[{municipality:'Münster',municipality_code:'05515000',numerator:'71',flur:'12',official_parcel_reference:'MITGEBRACHT-71',identification_status:'manuell_ergaenzt',geometry:{type:'Point',coordinates:[7.6261,51.9607]}}]
};
await writeFile(join(temp,'case.json'),JSON.stringify(sample));
for (const [name,options] of [['blank',[]],['place',['--case',join(temp,'case.json')]],['case',['--case',join(temp,'case.json'),'--include-case']]]) {
  const zip=join(temp,`${name}.zip`),target=join(temp,name);
  execFileSync(python,[join(root,'app/portable.py'),zip,...options]);
  execFileSync(python,['-c','import sys,zipfile; zipfile.ZipFile(sys.argv[1]).extractall(sys.argv[2])',zip,target]);
}
const browser=await playwright.chromium.launch({headless:true,channel:process.env.PLAYWRIGHT_CHANNEL||'chrome'});
const context=await browser.newContext({viewport:{width:1440,height:1000},acceptDownloads:true});
const page=await context.newPage();
const errors=[], network=[];
page.on('pageerror',error=>errors.push(error.message));
page.on('request',request=>{if(/^https?:/.test(request.url()))network.push(request.url());});
await context.route(/^https?:/,route=>route.abort());
const menu=async id=>{await page.locator('.file-menu summary').click();await page.locator(id).click();};
try {
  await page.goto(pathToFileURL(join(temp,'blank/index.html')).href);
  await page.waitForFunction(()=>!document.getElementById('example').disabled);
  assert.equal(await page.locator('#selection-count').textContent(),'0');
  assert.equal(network.length,0,'Keine versteckten Onlineabrufe beim leeren Start');
  assert.equal(await page.locator('#download-website').isVisible(),false);
  assert.equal(await page.locator('#address-query').isDisabled(),true);
  console.log('OK file:// Erststart mit lokalen Bibliotheken und ohne Server');

  await page.goto(pathToFileURL(join(temp,'place/index.html')).href);
  await page.locator('#prepared-site').click();
  await page.waitForFunction(()=>!document.getElementById('case-fields').disabled);
  assert.equal(await page.locator('#sender_organisation').inputValue(),'');
  assert.equal(await page.locator('#selection-count').textContent(),'0');
  await page.locator('#manual-parcel').click();
  await page.locator('#parcel-numerator').fill('88');
  await page.locator('#parcel-form button[type=submit]').click();
  assert.equal(await page.locator('#selection-count').textContent(),'1');
  await page.locator('#generate-documents').click(); await page.locator('#preview-dialog').waitFor();
  assert.equal(await page.locator('[role=tab]').count(),4);
  await page.locator('[data-close="preview-dialog"]').click();
  console.log('OK vorbereiteter Ort ohne vertrauliche Angaben; Offline-Erfassung und Entwürfe');

  page.once('dialog',dialog=>dialog.accept());
  await page.goto(pathToFileURL(join(temp,'case/index.html')).href);
  assert.equal(await page.locator('#selection-count').textContent(),'0');
  await page.locator('#prepared-site').click();
  await page.waitForFunction(()=>document.getElementById('case_id').value==='DATEI-42');
  await page.locator('#sender_organisation').fill('Geänderte Wasserwerke');
  await page.locator('#specific_interest').fill('Geändertes Interesse mit überprüfbaren Unterlagen.');
  await page.locator('#generate-documents').click(); await page.locator('#preview-dialog').waitFor();
  const frame=page.locator('#document-preview').contentFrame();
  await frame.locator('body').waitFor();
  assert.ok((await frame.locator('body').textContent()).includes('Geänderte Wasserwerke'));
  assert.ok((await frame.locator('body').textContent()).includes('Geändertes Interesse'));
  for (const [button,extension] of [['#export-docx','.docx'],['#export-zip','.zip']]) {
    const ready=page.waitForEvent('download');await page.locator(button).click(); const download=await ready;
    assert.ok(download.suggestedFilename().endsWith(extension));
    const output=join(temp,'export'+extension);await download.saveAs(output);
    const bytes=await readFile(output);assert.equal(bytes.subarray(0,2).toString(),'PK');
    execFileSync(python,['-c','import sys,zipfile; z=zipfile.ZipFile(sys.argv[1]); assert z.testzip() is None; assert "word/document.xml" in z.namelist() if sys.argv[1].endswith(".docx") else len([n for n in z.namelist() if n.endswith(".docx")])==4',output]);
  }
  await page.locator('[data-close="preview-dialog"]').click();
  await menu('#save-case');
  await page.reload();
  assert.equal(await page.locator('#selection-count').textContent(),'0');
  await menu('#restore-case');
  await page.waitForFunction(()=>document.getElementById('sender_organisation').value==='Geänderte Wasserwerke');
  assert.equal(await page.locator('#selection-count').textContent(),'1');
  console.log('OK vier aktualisierte Entwürfe, echte DOCX/ZIP und explizite Wiederherstellung offline');
  const shots=process.env.UI_SCREENSHOTS||join(temp,'screenshots');await mkdir(shots,{recursive:true});
  await page.waitForFunction(()=>!document.getElementById('map-status').textContent.includes('werden geladen'),{},{timeout:20000});
  await page.screenshot({path:join(shots,'portable-desktop.png'),fullPage:true});
  await page.setViewportSize({width:390,height:844});
  assert.equal(await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth),true);
  await page.screenshot({path:join(shots,'portable-mobile.png')});
  assert.deepEqual(errors,[]);
  assert.ok(network.every(url=>!new URL(url).hostname.match(/^(localhost|127\.)/)), 'Kein versteckter lokaler Server');
  console.log(`OK file:// Desktop/Mobil, kein lokaler Server. Ausgaben: ${temp}`);
} finally { await browser.close(); }
