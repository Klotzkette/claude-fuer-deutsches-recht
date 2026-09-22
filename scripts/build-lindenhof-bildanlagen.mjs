#!/usr/bin/env node
import fs from 'node:fs/promises';
import path from 'node:path';
import os from 'node:os';
import { createRequire } from 'node:module';
import { fileURLToPath } from 'node:url';

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const directory = path.join(root, 'testakten/strassennutzung-poller-lieferzufahrt-lindenhof-muenster');
const runtime = await fs.mkdtemp(path.join(os.tmpdir(), 'lindenhof-bildanlagen-'));
await fs.symlink(path.resolve(path.dirname(process.execPath), '../node_modules'), path.join(runtime, 'node_modules'), 'dir');
const require = createRequire(path.join(runtime, 'runtime.cjs'));
const { chromium } = require('playwright');
let browser;
try {
  browser = await chromium.launch({ headless: true,
    ...(process.env.CHROMIUM_EXECUTABLE ? { executablePath: process.env.CHROMIUM_EXECUTABLE } : {}),
  });
  const page = await browser.newPage({ viewport: { width: 980, height: 850 }, deviceScaleFactor: 2 });
  await page.setContent(`<!doctype html><html lang="de"><meta charset="utf-8">
<title>Lindenhof Vorrat: Schlüsselablage</title><style>
*{box-sizing:border-box}body{margin:0;background:#f3f5f4;color:#242c29;font-family:Arial,sans-serif;font-size:15px;line-height:1.45}
header{background:#204d43;color:white;padding:20px 30px;display:flex;justify-content:space-between;align-items:center}
header strong{font-size:21px}header small{display:block;color:#d8e9e1;margin-top:4px}header div:last-child{text-align:right;font-size:13px}
nav{padding:12px 30px;background:#fff;border-bottom:1px solid #d6ded8;color:#59655e}main{padding:25px 30px 30px}
h1{font-size:25px;margin:0 0 5px}h2{font-size:17px;margin:0 0 14px}p{margin:8px 0}.muted{color:#647269;font-size:13px}
.columns{display:grid;grid-template-columns:1.3fr 1fr;gap:26px;margin-top:26px}.sheet{background:white;padding:22px;border:1px solid #d7dfda;border-radius:3px}
.row{display:grid;grid-template-columns:140px 1fr;gap:16px;padding:10px 0;border-bottom:1px solid #e7ece8}.row span{color:#627067;font-size:13px}
.status{color:#23553f;border-left:4px solid #538764;padding:8px 12px;background:#edf4ef;margin-bottom:14px}
.pending{border-left:4px solid #ac7823;background:#fff9ed;color:#685021;padding:10px 12px;margin:14px 0}
table{border-collapse:collapse;width:100%;margin-top:10px;font-size:13px}th{text-align:left;background:#eaf0ec}th,td{padding:10px 8px;border-bottom:1px solid #dce3dd;vertical-align:top}
footer{padding:14px 30px;border-top:1px solid #d6ded8;background:white;color:#647269;font-size:12px}
</style><header><div><strong>Lindenhof Vorrat</strong><small>Betriebsablage · Lindenbogen 18, Münster</small></div><div>Mara Hölscher<small>22.09.2026 · 15:42 Uhr</small></div></header>
<nav>Betrieb / Zufahrt / Schlüssel</nav><main><h1>Schlüsselablage</h1><p class="muted">Vorgang MS-LB-2026-0417 · Stand aus dem Schlüsseljournal</p>
<div class="columns"><section class="sheet"><h2>LB-17 · Poller P1</h2><div class="status">Ausgegeben am 21.08.2026 an Mara Hölscher</div>
<div class="row"><span>Versuchszeitraum</span><div>24.08.2026 bis 15.10.2026</div></div>
<div class="row"><span>Öffnungsfenster</span><div>Montag bis Freitag<br>06:30–10:00 Uhr</div></div>
<div class="row"><span>Nutzung</span><div>Einzelne Lieferfahrten</div></div>
<div class="row"><span>Rückgabe</span><div>16.10.2026 bis 12:00 Uhr,<br>falls keine Folgeregelung erfolgt</div></div>
<p class="muted">Eintrag aus der betrieblichen Ablage. Keine neue Freigabe.</p></section>
<section class="sheet"><h2>Offene Rückmeldungen</h2><div class="pending">LB-18 · Zweitschlüssel beantragt<br>Noch nicht ausgegeben</div>
<div class="row"><span>Beantragtes Fenster</span><div>06:00–18:00 Uhr</div></div>
<div class="row"><span>Ergänzung</span><div>Bis 30.09.2026</div></div>
<div class="row"><span>Besprechung</span><div>06.10.2026 · 09:00 Uhr</div></div>
<p class="muted">Die laufende Schlüsselregelung bleibt in der Ablage getrennt vom beantragten Zugang.</p></section></div>
<h2 style="margin-top:25px">Zugehörige Unterlagen</h2><table><thead><tr><th>Unterlage</th><th>Zeitraum / Bezug</th><th>Ablage</th></tr></thead><tbody>
<tr><td>Schlüsseljournal</td><td>21.08.–22.09.2026</td><td>Betriebsaufzeichnungen</td></tr>
<tr><td>Anhörung</td><td>14.09.2026 · MS-LB-2026-0417</td><td>Eingang Stadt</td></tr></tbody></table>
</main><footer>Lindenhof Vorrat · Interne Betriebsablage · Ausdruck der Bildschirmansicht</footer></html>`);
  await page.screenshot({ path: path.join(directory, '28_schluesselablage_lb17_2026-09-22.png'), fullPage: true });
  const overflow = await page.evaluate(() => document.documentElement.scrollWidth > window.innerWidth);
  if (overflow) throw new Error('Horizontale Überbreite in der Schlüsselablage');
  const chat = await fs.readFile(path.join(directory, '20_chat_fruehdienst_2026-09-04.txt'), 'utf8');
  const records = [...chat.matchAll(/04\.09\.2026 (\d{2}:\d{2}) \| ([^\n]+)\n([^\n]+)/g)];
  if (records.length !== 4) throw new Error('Der Frühdienst-Auszug enthält nicht die erwarteten vier Nachrichten');
  const escape = (value) => value.replaceAll('&', '&amp;').replaceAll('<', '&lt;').replaceAll('>', '&gt;');
  const messages = records.map(([, time, name, body]) => `<article class="${name === 'Mara Hölscher' ? 'own' : 'other'}"><strong>${escape(name)}</strong><p>${escape(body)}</p><time>${time}</time></article>`).join('');
  await page.setViewportSize({ width: 460, height: 890 });
  await page.setContent(`<!doctype html><html lang="de"><meta charset="utf-8"><title>Lindenhof Frühdienst</title><style>
*{box-sizing:border-box}body{margin:0;background:#edf0f3;color:#21252b;font-family:Arial,sans-serif;font-size:15px;line-height:1.5}
.status{padding:11px 21px;background:#fff;display:flex;justify-content:space-between;font-size:12px;font-weight:bold}
header{padding:17px 22px;background:#304765;color:white;font-size:19px;font-weight:bold}header small{display:block;font-size:12px;font-weight:normal;color:#dce5f1;margin-top:3px}
main{padding:16px}.date{text-align:center;color:#586674;font-size:12px;padding:5px 0 15px}
article{max-width:350px;border-radius:5px;background:#fff;padding:13px 15px;margin:0 20px 16px 0;border:1px solid #d9e0e8}
article.own{background:#e1ece3;margin-left:35px;margin-right:0}strong{font-size:13px;color:#435877}p{margin:5px 0 6px}time{display:block;text-align:right;color:#59676b;font-size:11px}
footer{padding:14px 20px;background:#fff;border-top:1px solid #d5dce3;font-size:12px;color:#5e6873}
</style><div class="status"><span>18:06</span><span>21.09.2026</span></div><header>Lindenhof Frühdienst<small>Mara Hölscher · Deniz Arslan</small></header>
<main><div class="date">Freitag, 4. September 2026</div>${messages}</main>
<footer>Ausgewählter Verlauf · Ortszeit Münster<br>Export durch Mara Hölscher am 21.09.2026, 18:06 Uhr<br>Keine Bilder oder Sprachnachrichten im Auszug</footer></html>`);
  await page.screenshot({ path: path.join(directory, '29_chat_fruehdienst_2026-09-04.png'), fullPage: true });
  if (await page.evaluate(() => document.documentElement.scrollWidth > window.innerWidth)) {
    throw new Error('Horizontale Überbreite im Nachrichtenauszug');
  }
  console.log('Zwei Bildanlagen erstellt: Schlüsselablage und identischer Frühdienst-Auszug.');
} finally {
  await browser?.close();
  await fs.rm(runtime, { recursive: true, force: true });
}
