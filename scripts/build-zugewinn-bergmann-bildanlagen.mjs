#!/usr/bin/env node
import fs from 'node:fs/promises';
import path from 'node:path';
import os from 'node:os';
import { createRequire } from 'node:module';
import { fileURLToPath } from 'node:url';

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const directory = path.join(root, 'testakten/zugewinnausgleich-familie-bergmann-potsdam/bilder');
const runtime = await fs.mkdtemp(path.join(os.tmpdir(), 'bergmann-bildanlagen-'));
await fs.symlink(path.resolve(path.dirname(process.execPath), '../node_modules'), path.join(runtime, 'node_modules'), 'dir');
const require = createRequire(path.join(runtime, 'runtime.cjs'));
const { chromium } = require('playwright');
const browser = await chromium.launch({ headless: true,
  ...(process.env.CHROMIUM_EXECUTABLE ? { executablePath: process.env.CHROMIUM_EXECUTABLE } : {}),
});
const page = await browser.newPage({ viewport: { width: 430, height: 930 }, deviceScaleFactor: 2 });
const style = `
*{box-sizing:border-box}body{margin:0;background:#f2f4f6;color:#20252a;font-family:Arial,sans-serif;font-size:15px}
.status{height:38px;background:#fff;padding:12px 22px;font-weight:bold;display:flex;justify-content:space-between;font-size:13px}
header{padding:21px 24px;background:#164f62;color:white;font-size:19px;font-weight:bold}header span{display:block;font-size:13px;font-weight:normal;margin-top:7px;color:#d7e7ec}
main{padding:24px}h1{font-size:18px;margin:0 0 8px}h2{font-size:15px;margin:28px 0 10px}p{margin:8px 0;line-height:1.5}.muted{color:#566570;font-size:13px}.amount{font-size:32px;margin:12px 0 5px;font-weight:bold}.white{background:#fff;padding:18px;margin:18px -6px}
.row{display:flex;gap:15px;justify-content:space-between;padding:13px 0;border-bottom:1px solid #d8dee2}.row div{max-width:255px}.row small{display:block;color:#596773;font-size:12px;margin-top:6px;line-height:1.4}.row strong{white-space:nowrap;font-size:14px}
footer{padding:14px 22px;position:absolute;bottom:0;background:white;border-top:1px solid #d4dce1;width:100%;font-size:13px;display:flex;justify-content:space-between} .pill{color:#164f62;font-weight:bold;border-bottom:2px solid #164f62;padding-bottom:6px}
`;
async function capture(filename, body) {
  await page.setContent(`<!doctype html><html lang="de"><meta charset="utf-8"><title>Kontoansicht</title><style>${style}</style>${body}</html>`);
  await page.screenshot({ path: path.join(directory, filename), fullPage: true });
}

await fs.mkdir(directory, { recursive: true });
try {
  await capture('KontoKontor_2026-07-08.png', `
<div class="status"><span>19:23</span><span>LTE · 76 %</span></div>
<header>KontoKontor<span>Jonas Bergmann · Kundenkonto KK-41872</span></header>
<main><h1>Vermögensübersicht</h1><p class="muted">08.07.2026 · Kursstand 19:15 Uhr</p>
<div class="amount">3.800,00 EUR</div><p class="muted">Indikativer Wert Ihrer Bestände</p>
<div class="white"><div class="row"><div>Bitcoin<small>BTC · Verwahrung im Kundenkonto</small></div><strong>0,04000000</strong></div>
<div class="row"><div>Kurs je BTC</div><strong>95.000,00 EUR</strong></div><div class="row"><div>EUR-Guthaben</div><strong>0,00 EUR</strong></div></div>
<h2>Letzte Vorgänge</h2><div class="row"><div>Auszahlung an Privatkonto<small>16.06.2026 · KK-A-260616</small></div><strong>1.874,36 EUR</strong></div>
<div class="row"><div>Bitcoin verkauft<small>15.06.2026 · 0,02000000 BTC<br>Gebühr 5,64 EUR · KK-260615-204</small></div><strong>1.880,00 EUR</strong></div>
<p class="muted">Kurswerte können sich bis zur Orderausführung ändern. Der angezeigte Bestand ist keine offene Verkaufsorder.</p></main>
<footer><span class="pill">Übersicht</span><span>Vorgänge</span><span>Dokumente</span><span>Profil</span></footer>`);
  await capture('Havelbogen_2026-07-08.png', `
<div class="status"><span>19:26</span><span>LTE · 75 %</span></div>
<header>Havelbogen Bank<span>Jonas Bergmann · Onlinebanking</span></header>
<main><h1>Privatkonto 4402</h1><p class="muted">Gebuchter Stand · 08.07.2026</p><div class="amount">27.345,64 EUR</div>
<p class="muted">Kontoinhaber: Jonas Bergmann</p><div class="white"><p>Gebuchte Umsätze</p>
<div class="row"><div>Ursula Bergmann<small>06.07.2026 · Hilfe Haushalt und Pflege</small></div><strong>-380,00</strong></div>
<div class="row"><div>Mara Bergmann<small>06.07.2026 · Für Jule und Oskar</small></div><strong>-780,00</strong></div>
<div class="row"><div>Mara und Jonas Bergmann<small>03.07.2026 · Haus und Kinder</small></div><strong>-950,00</strong></div>
<div class="row"><div>Sven Hagedorn<small>03.07.2026 · Miete Feuerbachstraße 9</small></div><strong>-890,00</strong></div>
<div class="row"><div>Bergmann Licht &amp; Planung<small>02.07.2026 · Privatentnahme</small></div><strong>+5.225,00</strong></div></div>
<p class="muted">Anzeige in EUR. Vorgemerkte Zahlungen sind nicht Bestandteil des gebuchten Kontostands.</p></main>
<footer><span class="pill">Konten</span><span>Überweisung</span><span>Postfach</span><span>Service</span></footer>`);
  console.log('Zwei Bildanlagen erstellt: Kontobestand und Kryptobestand vom 08.07.2026.');
} finally {
  await browser.close();
}
