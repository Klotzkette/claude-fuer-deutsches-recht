# mandantenanfragen-assistent

<!-- BEGIN direkt-loslegen (autogen) -->
## Was ist das hier?

Assistent für Anwaltskanzleien zur Erstantwort auf Mandantenanfragen per E-Mail: dankt förmlich übernimmt die Anrede aus der eingehenden E-Mail nennt die telefonische Terminvergabe bittet um Sachverhalt per E-Mail oder bietet eine Telefon-Transkription mit DSGVO-Einwilligungshinweis an.

Dieses Plugin gehört zum Marketplace mit 235 Plugins für deutsches Recht. Es bündelt die zugehörigen Skills, Prüfraster, Vorlagen und Arbeitsroutinen in einem installierbaren Plugin-ZIP. Die zwei Markdown-Prompts sind vollwertige Ein-Datei-Starts für den Fall, dass kein Plugin-Setup genutzt werden soll: Werkstatt für den ausführlichen Arbeitsmodus, Schnellstart für den kompakten Einstieg.

Direktnavigation: [30-Sekunden-Start](#in-30-sekunden-starten) · [Startseite](../README.md) · [Plugin-Katalog](../README.md#was-ist-drin) · [Skill-Gesamtübersicht](../SKILLS.md) · [Skills dieses Plugins](../skills-index/mandantenanfragen-assistent.md) · [Plugin-Dateien](.) · [Download-Index](../ASSET_INDEX.md) · [Testakten](../testakten/README.md)

## In 30 Sekunden starten

| Ausgangslage | Schnellster Weg |
| --- | --- |
| Plugin installiert | Passenden Fachskill aus der Skill-Liste wählen und den untenstehenden Startsatz mit dem Arbeitsordner absenden. |
| Noch keine Installation | Den Schnellstart als Markdown laden und zusammen mit den Unterlagen öffnen. |
| Umfangreicher oder mehrstufiger Vorgang | Die Werkstatt laden; sie führt tiefer durch Fachrouten, Gegenposition und Endprodukt. |

Startsatz für mandantenanfragen-assistent:

> Lies zuerst alle Dateien im ausgewählten Ordner. Bearbeite den Vorgang mit diesem Fachgebiet und liefere als Erstes Subsumtionszeile: Normmerkmal, Definition, Tatsache, Aktenfund, Schluss, Gegenargument, Beweislast und Zwischenergebnis. Wenn bereits ein konkretes Dokument verlangt ist, beginne unmittelbar damit. Frage nur einmal gebündelt nach, falls der nächste fachliche Schritt sonst falsch wäre; arbeite im Übrigen mit sichtbar markierten Lücken weiter.

Bei einem Folgewunsch den bisherigen Aktenstand fortführen. Bereits festgestellte Tatsachen, Berechnungen und Quellen nicht erneut abfragen oder ohne Anlass neu aufbauen.

## Downloads

| Was | Format | Direkt-Download |
| --- | --- | --- |
| Plugin als Komplett-ZIP (Hauptweg) | ZIP | [`mandantenanfragen-assistent.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/mandantenanfragen-assistent.zip) |
| Kompakter Prompt (Schnellstart) | Markdown | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/mandantenanfragen-assistent/mandantenanfragen-assistent-schnellstart.md" download><code>mandantenanfragen-assistent-schnellstart.md</code></a> |
| Großer Prompt (Werkstatt) | Markdown | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/mandantenanfragen-assistent/mandantenanfragen-assistent-werkstatt.md" download><code>mandantenanfragen-assistent-werkstatt.md</code></a> |
| Zugeordnete Testakten | PDF / ZIP | [eine zugeordnete Akte](#zugeordnete-testakten) mit Gesamt-PDF, Originaldateien und Einzel-PDFs |

> Marketplace-Hinweis: Dieses Plugin gehört zum Marketplace mit 235 Plugins. Wer alle Plugins auf einmal will, nimmt [`alle-plugins-megazip.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/alle-plugins-megazip.zip). Alle Einzeldateien stehen im [Download-Index](../ASSET_INDEX.md); Werkstatt und Schnellstart bleiben direkte Markdown-Downloads.

## Zugeordnete Testakten

Jede Akte ist getrennt als lesbares Gesamt-PDF, ZIP mit Originaldateien und ZIP mit einzelnen PDFs erreichbar.

| Akte | Gesamt-PDF | Originaldateien | Einzel-PDFs |
| --- | --- | --- | --- |
| [Mandantenanfragen Q2/2026 — Kanzlei Roosendaal & Tannenfels, Köln](../testakten/mandantenanfragen-kanzlei-roosendaal-koeln-erstkontakt-q2-2026/README.md) | [Gesamt-PDF](../testakten/mandantenanfragen-kanzlei-roosendaal-koeln-erstkontakt-q2-2026/gesamt-pdf/mandantenanfragen-kanzlei-roosendaal-koeln-erstkontakt-q2-2026_gesamt.pdf) | [`testakte-mandantenanfragen-kanzlei-roosendaal-koeln-erstkontakt-q2-2026.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-mandantenanfragen-kanzlei-roosendaal-koeln-erstkontakt-q2-2026.zip) | [`testakte-mandantenanfragen-kanzlei-roosendaal-koeln-erstkontakt-q2-2026-einzelpdfs.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-mandantenanfragen-kanzlei-roosendaal-koeln-erstkontakt-q2-2026-einzelpdfs.zip) |

[Alle Testakten und Fachzuordnungen](../testakten/README.md)
<!-- END direkt-loslegen (autogen) -->

Wenn du das hier öffnest, willst du deinen Fall strukturieren, die einschlägigen Normen prüfen und ein verwertbares Arbeitsprodukt erhalten.
**Version:** 439.0.0
**Author:** Klotzkette
**Lizenz:** Apache-2.0 OR MIT

---

Assistent für Anwaltskanzleien zur automatisierten Erstantwort auf eingehende Mandantenanfragen per E-Mail. Das Plugin dankt formell für die Anfrage, übernimmt die exakte Anrede aus der eingehenden Mail, weist auf die telefonische Terminvergabe hin und bittet um eine Sachverhaltszusammenfassung per E-Mail. Für Personen, die nicht schreiben können oder möchten, bietet es einen automatisierten Transkriptionsservice an — mit DSGVO-konformem Einwilligungshinweis.

---

## Installation

1. ZIP aus dem Release herunterladen.
2. Plugin-Umgebung öffnen.
3. **Customize Plugins** bzw. **Personal plugins** öffnen.
4. **Install from .zip** wählen und `mandantenanfragen-assistent.zip` hochladen.
5. Mit einem konkreten Auftrag starten, zum Beispiel: `Beantworte diese Mandantenanfrage: [E-Mail einfügen]`

Nicht das komplette Repository-ZIP hochladen. Das Plugin-ZIP muss im Root direkt `.claude-plugin/plugin.json` und `skills/` enthalten.

---

## Skills-Übersicht (15 Skills)

| # | Skill-Name | Beschreibung | Lade-Trigger (Beispiele) |
|---|---|---|---|
| 1 | `anfrage-eingang-parser` | Extrahiert aus der Eingangsmail: Anrede, Name, E-Mail, Kontaktdaten, Sachverhaltsfetzen, Dringlichkeitssignale | "Anfrage auswerten", "E-Mail analysieren", "Kontaktdaten extrahieren" |
| 2 | `anrede-uebernehmen` | Übernimmt die EXAKTE Anrede aus der Eingangsmail; Heuristiken für Titel, Doppelnamen, Adelsprädikat, kirchliche Titel, Ehepaar | "Anrede übernehmen", "formelle Anrede", "Titel erkennen" |
| 3 | `erstantwort-generator` | Hauptskill: erstellt die vollständige formelle Erstantwort-Mail mit allen Bausteinen | "Erstantwort schreiben", "Antwortmail erstellen", "Eingangsbestätigung" |
| 4 | `telefon-konfiguration` | Verwaltet Kanzlei-Kontaktdaten (Sekretariat + Transkriptionsservice) aus `kanzlei.json` und setzt sie in Templates ein | "Telefonnummer konfigurieren", "kanzlei.json bearbeiten" |
| 5 | `transkriptionsdienst-erklaerung` | Formuliert den Hinweis auf den automatisierten Transkriptionsservice: Ablauf, Datenschutz, Einwilligungserfordernis | "Transkriptionsservice erklären", "kann nicht schreiben" |
| 6 | `einwilligung-hinweis-datenschutz` | DSGVO-konforme Einwilligungsklausel für die Sprachaufnahme (Art. 6 Abs. 1 lit. a DSGVO, Art. 13 DSGVO) | "DSGVO Einwilligung formulieren", "Datenschutz Transkription" |
| 7 | `mandatsverhaeltnis-hinweis` | Formuliert den Disclaimer: kein Mandatsverhältnis, keine Rechtsberatung, keine Pflichten der Kanzlei | "kein Mandat Hinweis", "Disclaimer Erstanfrage" |
| 8 | `vertraulichkeit-erinnerung` | Hinweis auf anwaltliche Schweigepflicht § 43a Abs. 2 BRAO — gilt erst ab Mandatsbegründung | "Schweigepflicht Anwalt", "wann gilt Verschwiegenheit" |
| 9 | `folgekorrespondenz-vorbereiten` | Erstellt Skeleton-Eintrag für CRM/Akte: Name, Mail, Telefon, Anliegen, Dringlichkeit, Konfliktcheck-Status | "CRM Eintrag erstellen", "Akte anlegen" |
| 10 | `spam-und-massen-anfrage-filter` | Erkennt Spam-Muster: 419-Scams, Massen-Anfragen, Phishing, Recruiter-Mails; kennzeichnet zur Aussortierung | "Spam prüfen", "verdächtige Anfrage", "Scam-Mail" |
| 11 | `dringlichkeitsmarker` | Erkennt Fristen und Eile-Signale; setzt Stufe HOCH/MITTEL/NIEDRIG; bei HOCH: Sofortanruf des Anwalts erforderlich | "Dringlichkeit prüfen", "Frist erkannt", "Eilbedarf" |
| 12 | `konfliktcheck-vorab` | Hinweis auf Konfliktcheck-Pflicht (§ 43a Abs. 4 BRAO, § 3 BORA); instruiert Sekretariat, Gegenseite vor Terminvergabe zu erfragen | "Konfliktcheck", "Interessenkonflikt prüfen" |
| 13 | `mehrsprachige-antwort` | Erkennt Sprache der Anfrage (DE/EN/FR/IT) und schaltet Erstantwort in die entsprechende Sprache um | "Antwort auf Englisch", "mehrsprachige Erstantwort" |
| 14 | `muster-erstantwort` | Vorlage-Skill mit drei vollständigen Musterschreiben (Standard, nur Vorname, Transkriptionsservice-Modus) für Copy-paste | "Musterschreiben zeigen", "Vorlage Erstantwort" |

---

## Beispiel-Prompt

```
Ich habe soeben diese E-Mail erhalten. Bitte erstelle eine formelle Erstantwort:

Von: Dr. Klaus-Dieter Müller-Strauss <kdms@example.de>
Betreff: Frage zur fristlosen Kündigung meines Angestellten

Sehr geehrte Damen und Herren,

mein Name ist Dr. Klaus-Dieter Müller-Strauss, ich führe ein kleines
Unternehmen im Bereich Maschinenbau. Ich möchte einem meiner Mitarbeiter
fristlos kündigen wegen grober Pflichtverletzung. Was muss ich beachten?

Mit freundlichen Grüßen
Dr. Klaus-Dieter Müller-Strauss
```

Das Plugin extrahiert automatisch die Anrede, prüft auf Dringlichkeit und Spam und erstellt die vollständige Erstantwort — einschließlich aller berufsrechtlichen Hinweise.

---

## Konfiguration (kanzlei.json)

Legen Sie im Plugin-Verzeichnis eine Datei `kanzlei.json` an:

```json
{
  "kanzlei": {
    "name": "[KANZLEI-NAME]",
    "adresse": {
      "strasse": "[STRASSE UND HAUSNUMMER]",
      "plz": "[POSTLEITZAHL]",
      "ort": "[ORT]"
    },
    "telefon_sekretariat": "[SEKRETARIATS-TELEFON]",
    "telefon_transkription": "[TRANSKRIPTIONS-TELEFON]",
    "erreichbarkeit": "[Z.B. Mo-Fr 09:00-17:00 Uhr]",
    "email_kanzlei": "[KANZLEI-E-MAIL]",
    "unterzeichnende_ra": "[VORNAME NACHNAME, Rechtsanwalt/Rechtsanwaeltin]"
  }
}
```

---

## Musterschreiben

Vollständig ausformulierte Musterschreiben für drei Szenarien (mit Anrede, ohne klare Anrede, Transkriptionsservice-Variante) finden Sie in:

[references/musteranschreiben.md](references/musteranschreiben.md)

---

## Rechtliche Hinweise

Dieses Plugin ist ein Hilfswerkzeug für Anwaltskanzleien. Es ersetzt nicht die Prüfung durch einen zugelassenen Rechtsanwalt. Alle generierten Texte sind Vorschläge — die abschließende Prüfung und Freigabe jeder Erstantwort liegt beim Sekretariat und der verantwortlichen Rechtsanwältin bzw. dem verantwortlichen Rechtsanwalt.

Das Plugin enthält keine Rechtsberatung. Alle Musterschreiben sind unverbindliche Formulierungshilfen.

Berufsrechtliche Grundlagen: §§ 43 ff. BRAO, §§ 1 ff. BORA, RVG, DSGVO.

---

## Lizenz

Apache-2.0 OR MIT — siehe [LICENSE](../LICENSE), [LICENSE-APACHE](../LICENSE-APACHE), [LICENSE-MIT](../LICENSE-MIT)


<!-- BEGIN SKILLS-LOGIC (auto-generated) -->

## Orientierung nach Arbeitslogik

Diese Navigation ordnet die Skills nach typischen Arbeitsschritten. Die alphabetische Komplettliste bleibt darunter erhalten.

| Arbeitsphase | Typische Skills |
| --- | --- |
| 1. Einstieg und Fallrouting | [`anfrage-eingang-parser`](skills/anfrage-eingang-parser/SKILL.md), [`anschluss-routing`](skills/anschluss-routing/SKILL.md), [`anwaltskanzleien-erstpruefung-und-mandatsziel`](skills/anwaltskanzleien-erstpruefung-und-mandatsziel/SKILL.md), [`dokumente-intake`](skills/dokumente-intake/SKILL.md), [`e-mail-erstantwort-und-terminrouting`](skills/e-mail-erstantwort-und-terminrouting/SKILL.md), [`einstieg-routing`](skills/einstieg-routing/SKILL.md), [`manda-erstkontakt-triagebogen-bauleiter`](skills/manda-erstkontakt-triagebogen-bauleiter/SKILL.md), [`manda-mandatsablehnung-rechtsschutz`](skills/manda-mandatsablehnung-rechtsschutz/SKILL.md), [`mandantenanfragen-anfrage-eingang-anrede`](skills/mandantenanfragen-anfrage-eingang-anrede/SKILL.md), [`mandatsverhaeltnis-hinweis`](skills/mandatsverhaeltnis-hinweis/SKILL.md), [`start-chronologie-fristen`](skills/start-chronologie-fristen/SKILL.md), [`workflow-kaltstart-und-routing`](skills/workflow-kaltstart-und-routing/SKILL.md) |
| 2. Unterlagen, Sachverhalt und Quellen | [`eingehenden-quellenkarte`](skills/eingehenden-quellenkarte/SKILL.md), [`einwilligung-hinweis-datenschutz`](skills/einwilligung-hinweis-datenschutz/SKILL.md), [`ma-erstvermerk-mandantenakte`](skills/ma-erstvermerk-mandantenakte/SKILL.md), [`mail-dokumentenmatrix-und-lueckenliste`](skills/mail-dokumentenmatrix-und-lueckenliste/SKILL.md), [`nennt-sachverhalt-telefon`](skills/nennt-sachverhalt-telefon/SKILL.md), [`quellen-livecheck`](skills/quellen-livecheck/SKILL.md), [`sachverhalt-formular-portal-und-einreichung`](skills/sachverhalt-formular-portal-und-einreichung/SKILL.md), [`spezial-eingehenden-livequellen-und-rechtsprechungscheck`](skills/spezial-eingehenden-livequellen-und-rechtsprechungscheck/SKILL.md), [`transkription-beweislast-und-darlegungslast`](skills/transkription-beweislast-und-darlegungslast/SKILL.md), [`unterlagen-luecken`](skills/unterlagen-luecken/SKILL.md), [`workflow-chronologie-und-belegmatrix`](skills/workflow-chronologie-und-belegmatrix/SKILL.md), [`workflow-unterlagen-lueckenliste`](skills/workflow-unterlagen-lueckenliste/SKILL.md) |
| 3. Prüfung, Anspruch und Subsumtion | [`folgekorrespondenz-vorbereiten-konfliktcheck`](skills/folgekorrespondenz-vorbereiten-konfliktcheck/SKILL.md), [`juristischer-argumentationskern`](skills/juristischer-argumentationskern/SKILL.md), [`konfliktcheck-vorab`](skills/konfliktcheck-vorab/SKILL.md), [`ma-konfliktcheck-konzern`](skills/ma-konfliktcheck-konzern/SKILL.md), [`manda-erstgespraechsleitfaden-checkliste`](skills/manda-erstgespraechsleitfaden-checkliste/SKILL.md), [`workflow-fristen-und-risikoampel`](skills/workflow-fristen-und-risikoampel/SKILL.md) |
| 5. Verfahren, Behörde und Gericht | [`einwilligungshinweis-fristennotiz-und-naechster-schritt`](skills/einwilligungshinweis-fristennotiz-und-naechster-schritt/SKILL.md), [`foermlich-behoerden-gericht-und-registerweg`](skills/foermlich-behoerden-gericht-und-registerweg/SKILL.md) |
| 6. Ergebnis, Schreiben und Kommunikation | [`erstantwort-foermlich-mail`](skills/erstantwort-foermlich-mail/SKILL.md), [`erstantwort-generator`](skills/erstantwort-generator/SKILL.md), [`mandantenkommunikation-redteam`](skills/mandantenkommunikation-redteam/SKILL.md), [`mehrsprachige-antwort-muster-erstantwort-spam`](skills/mehrsprachige-antwort-muster-erstantwort-spam/SKILL.md), [`muster-erstantwort`](skills/muster-erstantwort/SKILL.md), [`output-waehlen`](skills/output-waehlen/SKILL.md), [`telefon-mandantenkommunikation-entscheidungsvorlage`](skills/telefon-mandantenkommunikation-entscheidungsvorlage/SKILL.md) |
| 7. Kontrolle, Qualität und Gegenprüfung | [`bietet-fehlerkatalog`](skills/bietet-fehlerkatalog/SKILL.md), [`spezial-bietet-red-team-und-qualitaetskontrolle`](skills/spezial-bietet-red-team-und-qualitaetskontrolle/SKILL.md), [`workflow-redteam-qualitygate`](skills/workflow-redteam-qualitygate/SKILL.md) |
| 8. Spezialmodule und Schnittstellen | [`anrede-anwaltskanzleien-bittet`](skills/anrede-anwaltskanzleien-bittet/SKILL.md), [`anrede-uebernehmen`](skills/anrede-uebernehmen/SKILL.md), [`bittet-internationaler-bezug-und-schnittstellen`](skills/bittet-internationaler-bezug-und-schnittstellen/SKILL.md), [`dankt-dsgvo-sonderfall-e-mail`](skills/dankt-dsgvo-sonderfall-e-mail/SKILL.md), [`dringlichkeitsmarker-einwilligung-hinweis`](skills/dringlichkeitsmarker-einwilligung-hinweis/SKILL.md), [`dsgvo-sonderfall-und-edge-case`](skills/dsgvo-sonderfall-und-edge-case/SKILL.md), [`ma-aufnahmegespraech-leitfaden`](skills/ma-aufnahmegespraech-leitfaden/SKILL.md), [`ma-einfuehrung-erstkontakt`](skills/ma-einfuehrung-erstkontakt/SKILL.md), [`ma-mandant-manda-erstgespraechsleitfaden`](skills/ma-mandant-manda-erstgespraechsleitfaden/SKILL.md), [`manda-rechtsschutz-eintrittsanfrage-spezial`](skills/manda-rechtsschutz-eintrittsanfrage-spezial/SKILL.md), [`spam-und-massen-anfrage-filter`](skills/spam-und-massen-anfrage-filter/SKILL.md), [`telefon-konfiguration`](skills/telefon-konfiguration/SKILL.md), [`telefonische-terminvergabe-interessen`](skills/telefonische-terminvergabe-interessen/SKILL.md), [`terminvergabe-mehrparteien-konflikt-und-interessen`](skills/terminvergabe-mehrparteien-konflikt-und-interessen/SKILL.md), [`transkriptionsdienst-erklaerung`](skills/transkriptionsdienst-erklaerung/SKILL.md), [`uebernimmt-telefon-konfiguration`](skills/uebernimmt-telefon-konfiguration/SKILL.md), [`vertraulichkeit-erinnerung`](skills/vertraulichkeit-erinnerung/SKILL.md) |

<!-- END SKILLS-LOGIC (auto-generated) -->

<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Überblick

Automatisch generierte Komplett-Liste aller 59 Skills in diesem Plugin. Jeder Skillname öffnet die zugehörige `SKILL.md`; Beschreibungen stammen aus deren `description`-Feld.

| Skill | Beschreibung |
| --- | --- |
| [`anfrage-eingang-parser`](skills/anfrage-eingang-parser/SKILL.md) | Wenn es um Anfrage-Eingang-Parser in mandantenanfragen-assistent geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`anrede-anwaltskanzleien-bittet`](skills/anrede-anwaltskanzleien-bittet/SKILL.md) | Wenn es um Anrede: Verhandlung, Vergleich und Eskalation in mandantenanfragen-assistent geht: entwickelt Verhandlungsziel, Vergleichskorridor und Eskalationspfad; liefert eine Verhandlungs- oder Eskalationslinie mit Optionen. |
| [`anrede-uebernehmen`](skills/anrede-uebernehmen/SKILL.md) | Wenn es um Anrede-Übernehmen in mandantenanfragen-assistent geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`anschluss-routing`](skills/anschluss-routing/SKILL.md) | Wenn es um Anschluss-Routing in mandantenanfragen-assistent geht: klärt Rolle, Ziel, Frist, Unterlagen und den passenden nächsten Fachskill; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und nächstem Schritt. |
| [`anwaltskanzleien-erstpruefung-und-mandatsziel`](skills/anwaltskanzleien-erstpruefung-und-mandatsziel/SKILL.md) | Wenn es um Anwaltskanzleien: Erstprüfung, Rollenklärung und Mandatsziel in mandantenanfragen-assistent geht: klärt Rolle, Ziel, Frist, Unterlagen und den passenden nächsten Fachskill; liefert eine Fristen- und Risikoampel mit Sofortschri... |
| [`bietet-fehlerkatalog`](skills/bietet-fehlerkatalog/SKILL.md) | Wenn es um Bietet Fehlerkatalog in mandantenanfragen-assistent geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`bittet-internationaler-bezug-und-schnittstellen`](skills/bittet-internationaler-bezug-und-schnittstellen/SKILL.md) | Wenn es um Bittet: Internationaler Bezug und Schnittstellen in mandantenanfragen-assistent geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`dankt-dsgvo-sonderfall-e-mail`](skills/dankt-dsgvo-sonderfall-e-mail/SKILL.md) | Wenn es um Dankt: Risikoampel, Gegenargumente und Verteidigungslinien in mandantenanfragen-assistent geht: zerlegt Ergebnis, Frist, Zuständigkeit, Beweislast und Gegenposition; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`dokumente-intake`](skills/dokumente-intake/SKILL.md) | Wenn es um Dokumentenintake in mandantenanfragen-assistent geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`dringlichkeitsmarker-einwilligung-hinweis`](skills/dringlichkeitsmarker-einwilligung-hinweis/SKILL.md) | Wenn es um Dringlichkeitsmarker in mandantenanfragen-assistent geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`dsgvo-sonderfall-und-edge-case`](skills/dsgvo-sonderfall-und-edge-case/SKILL.md) | Wenn es um DSGVO: Sonderfall und Edge-Case-Prüfung in mandantenanfragen-assistent geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`e-mail-erstantwort-und-terminrouting`](skills/e-mail-erstantwort-und-terminrouting/SKILL.md) | Wenn es um E-Mail-Erstantwort, Terminrouting und Mandatsannahmehinweis in mandantenanfragen-assistent geht: klärt Rolle, Ziel, Frist, Unterlagen und den passenden nächsten Fachskill; liefert eine Schnittstellenkarte mit Kollisions-, Zust... |
| [`eingehenden-quellenkarte`](skills/eingehenden-quellenkarte/SKILL.md) | Wenn es um Eingehenden Quellenkarte in mandantenanfragen-assistent geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert eine Tatbestands- oder Anspruchsmatrix mit Gegenargumenten. |
| [`einstieg-routing`](skills/einstieg-routing/SKILL.md) | Wenn es um Einstieg und Routing in mandantenanfragen-assistent geht: klärt Rolle, Ziel, Frist, Unterlagen und den passenden nächsten Fachskill; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`einwilligung-hinweis-datenschutz`](skills/einwilligung-hinweis-datenschutz/SKILL.md) | Wenn es um Einwilligung-Hinweis-Datenschutz in mandantenanfragen-assistent geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`einwilligungshinweis-fristennotiz-und-naechster-schritt`](skills/einwilligungshinweis-fristennotiz-und-naechster-schritt/SKILL.md) | Wenn es um Einwilligungshinweis: Fristennotiz und nächster Schritt in mandantenanfragen-assistent geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`erstantwort-foermlich-mail`](skills/erstantwort-foermlich-mail/SKILL.md) | Wenn es um Erstantwort: Tatbestandsmerkmale, Beweisfragen und Beleglage in mandantenanfragen-assistent geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Beweislast- und Substantiierungsmatrix. |
| [`erstantwort-generator`](skills/erstantwort-generator/SKILL.md) | Wenn es um Erstantwort-Generator in mandantenanfragen-assistent geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und nächstem Schritt. |
| [`foermlich-behoerden-gericht-und-registerweg`](skills/foermlich-behoerden-gericht-und-registerweg/SKILL.md) | Wenn es um Foermlich: Behörden-, Gerichts- oder Registerweg in mandantenanfragen-assistent geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`folgekorrespondenz-vorbereiten-konfliktcheck`](skills/folgekorrespondenz-vorbereiten-konfliktcheck/SKILL.md) | Wenn es um Folgekorrespondenz-Vorbereiten in mandantenanfragen-assistent geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und nächstem Schritt. |
| [`juristischer-argumentationskern`](skills/juristischer-argumentationskern/SKILL.md) | Schaltet sich ein, wenn in Mandantenanfragen Assistent ein juristisches Arbeitsprodukt tragfähig begründet werden muss; verbindet konkrete Aktenfundstellen mit Tatbestandsmerkmal, Beweislast, stärkster Gegenposition und Rechtsfolge. |
| [`konfliktcheck-vorab`](skills/konfliktcheck-vorab/SKILL.md) | Wenn es um Konfliktcheck-Vorab in mandantenanfragen-assistent geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`ma-aufnahmegespraech-leitfaden`](skills/ma-aufnahmegespraech-leitfaden/SKILL.md) | Wenn es um Aufnahmegespraechs-Leitfaden in mandantenanfragen-assistent geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und nächstem Sch... |
| [`ma-einfuehrung-erstkontakt`](skills/ma-einfuehrung-erstkontakt/SKILL.md) | Wenn es um Erstkontakt: Typen in mandantenanfragen-assistent geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`ma-erstvermerk-mandantenakte`](skills/ma-erstvermerk-mandantenakte/SKILL.md) | Wenn es um Erstvermerk Mandantenakte in mandantenanfragen-assistent geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und nächstem Schritt. |
| [`ma-konfliktcheck-konzern`](skills/ma-konfliktcheck-konzern/SKILL.md) | Wenn es um Konfliktcheck im Konzern in mandantenanfragen-assistent geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigkeits- und Nachweisfragen. |
| [`ma-mandant-manda-erstgespraechsleitfaden`](skills/ma-mandant-manda-erstgespraechsleitfaden/SKILL.md) | Wenn es um Mandant mit Betreuung in mandantenanfragen-assistent geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`mail-dokumentenmatrix-und-lueckenliste`](skills/mail-dokumentenmatrix-und-lueckenliste/SKILL.md) | Wenn es um Mail: Dokumentenmatrix, Lückenliste und Nachforderung in mandantenanfragen-assistent geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Dokumentenmatrix mit Nachforderungsliste. |
| [`manda-erstgespraechsleitfaden-checkliste`](skills/manda-erstgespraechsleitfaden-checkliste/SKILL.md) | Wenn es um Manda: Erstgespraechsleitfaden in mandantenanfragen-assistent geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Dokumentenmatrix mit Nachforderungsliste. |
| [`manda-erstkontakt-triagebogen-bauleiter`](skills/manda-erstkontakt-triagebogen-bauleiter/SKILL.md) | Wenn es um Manda: Triagebogen Erstkontakt in mandantenanfragen-assistent geht: klärt Rolle, Ziel, Frist, Unterlagen und den passenden nächsten Fachskill; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`manda-mandatsablehnung-rechtsschutz`](skills/manda-mandatsablehnung-rechtsschutz/SKILL.md) | Wenn es um Manda: Mandatsablehnung COI in mandantenanfragen-assistent geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und nächstem Schr... |
| [`manda-rechtsschutz-eintrittsanfrage-spezial`](skills/manda-rechtsschutz-eintrittsanfrage-spezial/SKILL.md) | Wenn es um Manda: RS-Eintrittsanfrage in mandantenanfragen-assistent geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und nächstem Schritt. |
| [`mandantenanfragen-anfrage-eingang-anrede`](skills/mandantenanfragen-anfrage-eingang-anrede/SKILL.md) | Wenn es um Mandantenanfragen: Fristen, Form, Zuständigkeit und Rechtsweg in mandantenanfragen-assistent geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`mandantenkommunikation-redteam`](skills/mandantenkommunikation-redteam/SKILL.md) | Wenn es um Mandantenkommunikation in mandantenanfragen-assistent geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert eine Mandantennachricht oder Entscheidungsvorlage. |
| [`mandatsverhaeltnis-hinweis`](skills/mandatsverhaeltnis-hinweis/SKILL.md) | Wenn es um Mandatsverhältnis-Hinweis in mandantenanfragen-assistent geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`mehrsprachige-antwort-muster-erstantwort-spam`](skills/mehrsprachige-antwort-muster-erstantwort-spam/SKILL.md) | Wenn es um Mehrsprachige-Antwort in mandantenanfragen-assistent geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`muster-erstantwort`](skills/muster-erstantwort/SKILL.md) | Wenn es um Muster-Erstantwort in mandantenanfragen-assistent geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`nennt-sachverhalt-telefon`](skills/nennt-sachverhalt-telefon/SKILL.md) | Wenn es um Nennt: Zahlen, Schwellenwerte und Berechnung in mandantenanfragen-assistent geht: rechnet Schwellen, Beträge, Varianten und Kontrollannahmen durch; liefert eine Berechnungstabelle mit Schwellen, Annahmen und Kontrollfragen. |
| [`output-waehlen`](skills/output-waehlen/SKILL.md) | Wenn es um Output wählen in mandantenanfragen-assistent geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`quellen-livecheck`](skills/quellen-livecheck/SKILL.md) | Wenn es um Rechtsquellen-Livecheck in mandantenanfragen-assistent geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert eine Tatbestands- oder Anspruchsmatrix mit Gegenargumenten. |
| [`sachverhalt-formular-portal-und-einreichung`](skills/sachverhalt-formular-portal-und-einreichung/SKILL.md) | Wenn es um Sachverhalt: Formular, Portal und Einreichungslogik in mandantenanfragen-assistent geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`spam-und-massen-anfrage-filter`](skills/spam-und-massen-anfrage-filter/SKILL.md) | Wenn es um Spam-und-Massen-Anfrage-Filter in mandantenanfragen-assistent geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`spezial-bietet-red-team-und-qualitaetskontrolle`](skills/spezial-bietet-red-team-und-qualitaetskontrolle/SKILL.md) | Wenn es um Bietet: Red-Team und Qualitätskontrolle in mandantenanfragen-assistent geht: zerlegt Ergebnis, Frist, Zuständigkeit, Beweislast und Gegenposition; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`spezial-eingehenden-livequellen-und-rechtsprechungscheck`](skills/spezial-eingehenden-livequellen-und-rechtsprechungscheck/SKILL.md) | Wenn es um Eingehenden: Livequellen- und Rechtsprechungscheck in mandantenanfragen-assistent geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`start-chronologie-fristen`](skills/start-chronologie-fristen/SKILL.md) | Wenn es um Mandantenanfragen-Assistent — Allgemein in mandantenanfragen-assistent geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Chronologie mit Belegmatrix und Widerspruchsliste. |
| [`telefon-konfiguration`](skills/telefon-konfiguration/SKILL.md) | Wenn es um Telefon-Konfiguration in mandantenanfragen-assistent geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`telefon-mandantenkommunikation-entscheidungsvorlage`](skills/telefon-mandantenkommunikation-entscheidungsvorlage/SKILL.md) | Wenn es um Telefon: Mandantenkommunikation und Entscheidungsvorlage in mandantenanfragen-assistent geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`telefonische-terminvergabe-interessen`](skills/telefonische-terminvergabe-interessen/SKILL.md) | Wenn es um Telefonische: Compliance-Dokumentation und Aktenvermerk in mandantenanfragen-assistent geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und näch... |
| [`terminvergabe-mehrparteien-konflikt-und-interessen`](skills/terminvergabe-mehrparteien-konflikt-und-interessen/SKILL.md) | Wenn es um Terminvergabe: Mehrparteienkonflikt und Interessenmatrix in mandantenanfragen-assistent geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`transkription-beweislast-und-darlegungslast`](skills/transkription-beweislast-und-darlegungslast/SKILL.md) | Wenn es um Transkription: Beweislast, Darlegungslast und Substantiierung in mandantenanfragen-assistent geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`transkriptionsdienst-erklaerung`](skills/transkriptionsdienst-erklaerung/SKILL.md) | Wenn es um Transkriptionsdienst-Erklärung in mandantenanfragen-assistent geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`uebernimmt-telefon-konfiguration`](skills/uebernimmt-telefon-konfiguration/SKILL.md) | Wenn es um Uebernimmt: Schriftsatz-, Brief- und Memo-Bausteine in mandantenanfragen-assistent geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und... |
| [`unterlagen-luecken`](skills/unterlagen-luecken/SKILL.md) | Wenn es um Unterlagen und Lücken in mandantenanfragen-assistent geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`vertraulichkeit-erinnerung`](skills/vertraulichkeit-erinnerung/SKILL.md) | Wenn es um Sekretariat muss wissen ab wann die Anwaltsschwiegepflicht gilt in mandantenanfragen-assistent geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`workflow-chronologie-und-belegmatrix`](skills/workflow-chronologie-und-belegmatrix/SKILL.md) | Wenn es um Chronologie und Belegmatrix in mandantenanfragen-assistent geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Chronologie mit Belegmatrix und Widerspruchsliste. |
| [`workflow-fristen-und-risikoampel`](skills/workflow-fristen-und-risikoampel/SKILL.md) | Wenn es um Fristen- und Risikoampel in mandantenanfragen-assistent geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`workflow-kaltstart-und-routing`](skills/workflow-kaltstart-und-routing/SKILL.md) | Wenn es um Kaltstart und Routing in mandantenanfragen-assistent geht: klärt Rolle, Ziel, Frist, Unterlagen und den passenden nächsten Fachskill; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`workflow-redteam-qualitygate`](skills/workflow-redteam-qualitygate/SKILL.md) | Wenn es um Red-Team Qualitygate in mandantenanfragen-assistent geht: zerlegt Ergebnis, Frist, Zuständigkeit, Beweislast und Gegenposition; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`workflow-unterlagen-lueckenliste`](skills/workflow-unterlagen-lueckenliste/SKILL.md) | Wenn es um Unterlagen- und Lückenliste in mandantenanfragen-assistent geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Dokumentenmatrix mit Nachforderungsliste. |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
