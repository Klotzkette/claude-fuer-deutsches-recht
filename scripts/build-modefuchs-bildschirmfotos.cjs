#!/usr/bin/env node
// Die Bildschirmansichten bilden ausschließlich die fallinternen Datensätze ab.
const fs = require('node:fs');
const path = require('node:path');
const { chromium } = require('playwright');

const root = path.resolve(__dirname, '..');
const output = path.join(root, 'testakten/inkasso-zahlungsklage-modefuchs');
const messages = JSON.parse(fs.readFileSync(path.join(__dirname, 'fixtures/modefuchs/korrespondenz.json'), 'utf8'));
const invoice = messages.find(message => message.file === 'Rechnung_April.eml');
const escape = value => value.replaceAll('&', '&amp;').replaceAll('<', '&lt;').replaceAll('>', '&gt;');

const style = `
*{box-sizing:border-box}body{margin:0;color:#24282b;font:16px Arial,sans-serif;background:#f2f3f4;letter-spacing:0}
.window{height:100vh;background:#fff;border:1px solid #abb2b7}.titlebar{height:36px;background:#e2e6e9;padding:8px 18px;font-size:13px;display:flex;justify-content:space-between}
.toolbar{height:66px;display:flex;align-items:center;gap:28px;border-bottom:1px solid #ccd2d5;padding:0 24px;background:#f8f9fa}.brand{font-weight:700;font-size:21px}.search{background:#fff;border:1px solid #bfc7cc;padding:12px 18px;color:#647179;width:500px}
.layout{display:grid;grid-template-columns:240px 1fr;height:calc(100vh - 102px)}nav{background:#f2f4f5;border-right:1px solid #d4d9dc;padding:30px 16px;line-height:1.5}.account{font-size:13px;overflow-wrap:anywhere;margin:0 0 24px}.item{padding:12px 15px;margin:5px 0}.selected{background:#dce9f0;border-left:3px solid #3b718e}.muted{color:#647179}.small{font-size:13px}
main{padding:32px 42px;min-width:0}h1{font-size:25px;margin:0 0 26px}h2{font-size:19px;margin:32px 0 18px}.row{display:flex;align-items:center;justify-content:space-between;gap:24px;padding:21px 0;border-bottom:1px solid #e0e3e5}.label{max-width:700px;line-height:1.6}.select{border:1px solid #aeb9bf;border-radius:3px;padding:11px 17px;min-width:230px;white-space:nowrap;background:#fff}.note{line-height:1.6;max-width:820px;color:#4c565d;margin-top:26px}.check{background:#2b657e;color:#fff;padding:4px 9px;margin-right:9px}.bottom{margin-top:42px;color:#65717a;font-size:13px}.mail-layout{display:grid;grid-template-columns:325px 1fr;height:calc(100vh - 102px)}.mail-list{border-right:1px solid #ccd2d5;background:#fbfcfc}.mail-list h2{font-size:19px;margin:28px 20px}.mail{padding:22px 20px;border-bottom:1px solid #dfe3e5;line-height:1.5}.mail strong{display:block;font-size:15px}.mail span{display:block;font-size:14px;margin-top:5px}.mail.current{background:#e4edf2}.message{padding:29px 32px}.message h1{font-size:21px;margin-bottom:22px;line-height:1.4}.headers{font-size:14px;line-height:1.8;color:#586169}.attachments{display:flex;gap:14px;margin:23px 0}.attachment{border:1px solid #c6cfd4;border-radius:3px;padding:12px;min-width:220px;font-size:13px;line-height:1.7;max-width:45%;overflow-wrap:anywhere}.pdf{font-weight:bold;color:#903e35;font-size:12px}.body{font-size:15px;line-height:1.6;white-space:pre-wrap}.pane{display:grid;grid-template-columns:210px 1fr;height:calc(100vh - 102px)}.pane nav{padding:25px 12px}.pane .account{font-size:12px}.message .body{max-width:820px}.message .small{margin-top:24px}
`;

const frame = (title, content) => `<!doctype html><html lang="de"><meta charset="utf-8"><style>${style}.layout,.pane{height:calc(100vh - 104px)}.mail-layout{height:100%}</style><body><div class="window"><div class="titlebar"><span>${title}</span><span>_ &nbsp; □ &nbsp; ×</span></div><div class="toolbar"><span class="brand">Postfach</span><span class="search">Nachrichten durchsuchen</span><span class="muted">Nachrichten &nbsp;&nbsp; Kontakte &nbsp;&nbsp; Einstellungen</span></div>${content}</div></body></html>`;

const filter = frame('Postfach - Einstellungen | 27.06.2025 18:17', `
<div class="layout"><nav><p class="account">Gottlieb von Altenhausen<br>gottlieb.altenhausen@<wbr>mustermail.de</p><div class="item">Allgemein</div><div class="item">Konto</div><div class="item selected">Sicherheit und Spam</div><div class="item">Nachrichtenregeln</div><div class="item">Speicher</div></nav>
<main><p class="small muted">Einstellungen / Sicherheit und Spam</p><h1>Spamfilter</h1>
<div class="row"><div class="label"><strong>Spamfilter aktiv</strong><br><span class="muted">Eingehende Nachrichten auf unerwünschte Inhalte prüfen</span></div><div><span class="check">✓</span> Aktiv</div></div>
<div class="row"><div class="label"><strong>Unbekannte Absender</strong><br><span class="muted">Nachrichten von Absendern außerhalb Ihrer Kontakte</span></div><div class="select">In den Junk-Ordner &nbsp; ▾</div></div>
<div class="row"><div class="label"><strong>Automatisch löschen</strong><br><span class="muted">Nachrichten im Junk-Ordner entfernen</span></div><div class="select">Nach 10 Tagen &nbsp; ▾</div></div>
<div class="row"><div class="label"><strong>Benachrichtigung über Junk-Nachrichten</strong><br><span class="muted">Zusammenfassung per E-Mail</span></div><div class="select">Aus &nbsp; ▾</div></div>
<h2>Ausnahmen</h2><p class="note">Absender aus Ihren Kontakten werden nicht über die Regel für unbekannte Absender verschoben. Andere Nachrichtenregeln bleiben aktiv.</p>
<div class="row"><span>Zusätzliche erlaubte Absender</span><span class="muted">Keine Einträge</span></div><p class="bottom">Keine ungespeicherten Änderungen &nbsp; | &nbsp; Sitzung: 27.06.2025, 18:17 Uhr</p></main></div>`);

const mailBody = invoice.body.split('\n\nMit freundlichen Grüßen')[0];
const sent = frame('Postfach - Gesendet | 01.07.2025 15:38', `
<div class="pane"><nav><p class="account">ModeFuchs Rechnungswesen<br>rechnungswesen@modefuchs.de</p><div class="item">Posteingang</div><div class="item selected">Gesendet</div><div class="item">Entwürfe</div><div class="item">Archiv</div><div class="item">Papierkorb</div></nav>
<div class="mail-layout"><section class="mail-list"><h2>Gesendet</h2><p class="small muted" style="margin:0 20px 22px">Suche: R-20250406-3098</p>
<div class="mail"><strong>Gottlieb von Altenhausen</strong><span>30.06.2025, 10:12</span><span>Ihre Zahlung zur Rechnung<br>R-20250406-3098</span></div>
<div class="mail"><strong>Gottlieb von Altenhausen</strong><span>20.04.2025, 09:00</span><span>Zahlungserinnerung - Rechnung<br>R-20250406-3098</span></div>
<div class="mail current"><strong>Gottlieb von Altenhausen</strong><span>06.04.2025, 10:18</span><span>R-20250406-3098 | Ihre Rechnung<br>und Versandmitteilung</span><span class="muted">2 Anhänge</span></div></section>
<article class="message"><h1>${escape(invoice.subject)}</h1><div class="headers">Von: ModeFuchs Rechnungswesen &lt;rechnungswesen@modefuchs.de&gt;<br>An: Gottlieb von Altenhausen &lt;gottlieb.altenhausen@mustermail.de&gt;<br>Gesendet: Sonntag, 06.04.2025, 10:18 Uhr</div>
<div class="attachments"><div class="attachment"><span class="pdf">PDF</span><br>04_Rechnung_R-20250406-3098.pdf</div><div class="attachment"><span class="pdf">PDF</span><br>02_Versandbestaetigung_06-04-2025.pdf</div></div>
<div class="body">${escape(mailBody)}</div><p class="small">Mit freundlichen Grüßen<br>ModeFuchs Rechnungswesen</p></article></div></div>`);

async function run() {
  const browser = await chromium.launch({ headless: true, executablePath: process.env.CHROMIUM_PATH || undefined });
  try {
    const page = await browser.newPage({ viewport: { width: 1536, height: 1080 }, deviceScaleFactor: 1 });
    for (const [name, html] of [
      ['Bildschirmfoto_2025-06-27_1817.png', filter],
      ['Bildschirmfoto_Postausgang_20250701.png', sent],
    ]) {
      await page.setContent(html, { waitUntil: 'load' });
      await page.evaluate(() => document.fonts.ready);
      const overflow = await page.evaluate(() => ({
        x: document.documentElement.scrollWidth > innerWidth,
        y: document.documentElement.scrollHeight > innerHeight,
      }));
      if (overflow.x || overflow.y) throw new Error(`Ansicht läuft über: ${name}`);
      await page.screenshot({ path: path.join(output, name), fullPage: true });
      console.log(name);
    }
  } finally { await browser.close(); }
}
run().catch(error => { console.error(error); process.exitCode = 1; });
