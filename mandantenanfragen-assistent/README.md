# mandantenanfragen-assistent

<!-- BEGIN direkt-loslegen (autogen) -->
## Was ist das hier?

Assistent für Anwaltskanzleien zur Erstantwort auf Mandantenanfragen per E-Mail: dankt förmlich übernimmt die Anrede aus der eingehenden E-Mail nennt die telefonische Terminvergabe bittet um Sachverhalt per E-Mail oder bietet eine Telefon-Transkription mit DSGVO-Einwilligungshinweis an.

Dieses Plugin gehört zum Marketplace mit 315 Plugins. Für die Installation nimm das Einzel-ZIP. Ohne Installation genügt zum Einstieg einer der beiden eigenständigen Markdown-Prompts: Schnellstart für den Kernvorgang, Werkstatt für die ausführliche Bearbeitung. Die Prompts ersetzen nicht sämtliche Spezialskills und Hilfsdateien des Plugins.

## Welche Datei wofür? / Which file should I use?

| Bestandteil | Deutsch | English | Wo? / Where? |
| --- | --- | --- | --- |
| Plugin-ZIP | Installiert das vollständige Plugin mit Skills, Referenzen und Hilfsdateien. | Installs the complete plugin with its skills, references and supporting files. | [`mandantenanfragen-assistent.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/paketpflege-20261122-v445.36.9/mandantenanfragen-assistent.zip) |
| Skills | Arbeitsabläufe für einzelne Aufgaben. Wähle bei einem klaren Auftrag den passenden Skill ausdrücklich; die automatische Auswahl ist nicht garantiert. Einzeldownloads enthalten nur die jeweilige Markdown-Datei. | Focused task workflows. Select a known skill explicitly; automatic selection is not guaranteed. An individual download contains only that Markdown file. | [Skill-Liste öffnen / Open skill list](../skills-index/mandantenanfragen-assistent.md) |
| Werkstatt-Prompt | Ausführliche eigenständige Markdown-Datei für komplexe oder mehrstufige Vorgänge. Sie ist kein Skill und nicht im Plugin-ZIP enthalten. | Detailed standalone Markdown file for complex or multi-step matters. It is not a skill and is not included in the plugin ZIP. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=mandantenanfragen-assistent/mandantenanfragen-assistent-werkstatt.md) |
| Schnellstart / Mini-Prompt | Kompakte eigenständige Markdown-Datei für einen schnellen ersten Arbeitsstand. Sie ist kein Skill und nicht im Plugin-ZIP enthalten. | Compact standalone Markdown file for a fast first work product. It is not a skill and is not included in the plugin ZIP. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=mandantenanfragen-assistent/mandantenanfragen-assistent-schnellstart.md) |
| Testakten | Separate Übungsunterlagen in PDF- und Originalformaten; sie werden nicht mit dem Plugin installiert. | Separate practice files in PDF and original formats; they are not installed with the plugin. | [Testakten-Übersicht / Test-file index](../testakten/README.md) |

Links mit „MD herunterladen / Download MD“ starten einen Dateidownload. Navigationslinks zu README- und Übersichtsseiten bleiben dagegen als GitHub-Seiten geöffnet.

Links labelled “MD herunterladen / Download MD” start a file download. Navigation links to README and index pages remain normal GitHub pages.

Die Skill-Liste bildet den Quellbestand ab. Im installierten Paket werden umfangreiche Spezialserien teilweise über einen Fachrouter bei Bedarf geladen und erscheinen dann nicht als eigene auswählbare Skills. Beim manuellen Einsatz eines einzelnen Skills müssen zusätzlich benötigte Referenzen oder Werkzeuge verfügbar sein.

The skill index lists the source collection. In the installed package, some specialist series are accessed through a topic router rather than separate menu entries. A standalone skill may need additional reference files or tools. Choose one entry point, then add only what the matter requires.

Direktnavigation: [30-Sekunden-Start](#in-30-sekunden-starten) · [Startseite](../README.md) · [Plugin-Katalog](../README.md#was-ist-drin) · [Skill-Gesamtübersicht](../SKILLS.md) · [Skills dieses Plugins](../skills-index/mandantenanfragen-assistent.md) · [Plugin-Dateien](.) · [Download-Index](../ASSET_INDEX.md) · [Installation](../INSTALLATION_EINFACH.md) · [Testakten](../testakten/README.md)

## In 30 Sekunden starten

| Ausgangslage | Schnellster Weg |
| --- | --- |
| Plugin installiert | Passenden Fachskill in der [alphabetisch sortierten Skill-Liste](../skills-index/mandantenanfragen-assistent.md) wählen und den untenstehenden Startsatz mit dem Arbeitsordner absenden. |
| Noch keine Installation | Den Schnellstart unten als Markdown herunterladen und mit den Unterlagen in einer freigegebenen Arbeitsoberfläche bereitstellen. |
| Umfangreicher oder mehrstufiger Vorgang | Die Werkstatt laden; sie führt tiefer durch Fachrouten, Gegenposition und Endprodukt. |

Startsatz für mandantenanfragen-assistent:

> Sichte den ausgewählten Ordner intern, ohne seine Inhalte ungefragt aufzulisten. Lies die für den Auftrag tragenden Unterlagen; ergänze die Lektüre gezielt bei offenen Belegfragen. Beginne mit folgendem Arbeitsschritt: einen fachbezogenen Erststand mit Ergebnisrichtung, Kernbeleg und nächstem Dokument. Wenn bereits ein konkretes Dokument verlangt ist, beginne unmittelbar damit. Frage gezielt nach entscheidenden offenen Punkten und arbeite an den unabhängigen Teilen weiter. Verarbeite die Antwort im bestehenden Entwurf; weitere Rückfragen nur bei neuen entscheidenden Lücken.

Bei einem Folgewunsch den bisherigen Aktenstand fortführen. Bereits festgestellte Tatsachen, Berechnungen und Quellen nicht erneut abfragen oder ohne Anlass neu aufbauen.

## Downloads

| Was | Format | Direkt-Download |
| --- | --- | --- |
| Plugin als Komplett-ZIP (Hauptweg) | ZIP | [`mandantenanfragen-assistent.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/paketpflege-20261122-v445.36.9/mandantenanfragen-assistent.zip) |
| Kompakter Prompt (Schnellstart) | Markdown | [`mandantenanfragen-assistent-schnellstart.md`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=mandantenanfragen-assistent/mandantenanfragen-assistent-schnellstart.md) |
| Großer Prompt (Werkstatt) | Markdown | [`mandantenanfragen-assistent-werkstatt.md`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=mandantenanfragen-assistent/mandantenanfragen-assistent-werkstatt.md) |
| Zugeordnete Testakten | PDF / ZIP | [eine zugeordnete Akte](#zugeordnete-testakten) mit Gesamt-PDF, Originaldateien und Einzel-PDFs |

> Marketplace-Hinweis: Dieses Plugin gehört zum Marketplace mit 315 Plugins. Das Sammelpaket [`alle-plugins-megazip.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/alle-plugins-megazip.zip) enthält seinen veröffentlichten Stand, nicht zwingend spätere Einzelpakete. Alle Einzeldateien stehen im [Download-Index](../ASSET_INDEX.md); Werkstatt und Schnellstart bleiben direkte Markdown-Downloads.

## Zugeordnete Testakten

Jede Akte ist getrennt als lesbares Gesamt-PDF, ZIP mit Originaldateien und ZIP mit einzelnen PDFs erreichbar.

> Diese Testakte wurde mit KI generiert und ist ein Experiment. Benutzung auf eigene Verantwortung und eigene Gefahr.
>
> This test case file was generated with AI and is an experiment. Use at your own responsibility and risk.

| Akte | Gesamt-PDF | Originaldateien | Einzel-PDFs |
| --- | --- | --- | --- |
| [Mandantenanfragen Q2/2026 — Kanzlei Roosendaal & Tannenfels, Köln](../testakten/mandantenanfragen-kanzlei-roosendaal-koeln-erstkontakt-q2-2026/README.md) | [Gesamt-PDF](../testakten/mandantenanfragen-kanzlei-roosendaal-koeln-erstkontakt-q2-2026/gesamt-pdf/mandantenanfragen-kanzlei-roosendaal-koeln-erstkontakt-q2-2026_gesamt.pdf) | [`testakte-mandantenanfragen-kanzlei-roosendaal-koeln-erstkontakt-q2-2026.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/grundakten-sammlung-v1.0.0/testakte-mandantenanfragen-kanzlei-roosendaal-koeln-erstkontakt-q2-2026.zip) | [`testakte-mandantenanfragen-kanzlei-roosendaal-koeln-erstkontakt-q2-2026-einzelpdfs.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/akten-v445.35.3/testakte-mandantenanfragen-kanzlei-roosendaal-koeln-erstkontakt-q2-2026-einzelpdfs.zip) |

[Alle Testakten und Fachzuordnungen](../testakten/README.md)
<!-- END direkt-loslegen (autogen) -->

Wenn du das hier öffnest, willst du deinen Fall strukturieren, die einschlägigen Normen prüfen und ein verwertbares Arbeitsprodukt erhalten.
Paketstand: siehe [aktuellen Release](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest).
**Author:** Klotzkette
**Lizenz:** Apache-2.0 OR MIT

---

Der Assistent entwirft für Anwaltskanzleien vollständige Erstantworten auf eingehende E-Mails. Er liest die Anfrage und vorhandene Anlagen zuerst, spricht die anfragende Person an und übernimmt nicht versehentlich den Namen der angeschriebenen Kanzleiperson. Er fragt nur fehlende Unterlagen nach, berücksichtigt berichtete Dringlichkeit und setzt eine bereits beschlossene Mandatsabsage direkt um. Terminvergabe, Mandatsannahme, Fristübernahme und Versand werden nicht durch den Entwurf bewirkt.

Ein Transkriptionsangebot erscheint nur, wenn die Kanzlei diesen Dienst tatsächlich eingerichtet und für den konkreten Einsatz freigegeben hat. Das Plugin stellt keinen Telefondienst bereit; ein Einwilligungstext allein belegt auch keine datenschutzrechtliche Zulässigkeit.

---

## Installation

1. ZIP aus dem Release herunterladen.
2. Plugin-Umgebung öffnen.
3. **Customize → Plugins** bzw. **Personal plugins** öffnen.
4. **Upload plugin** wählen und `mandantenanfragen-assistent.zip` hochladen.
5. Mit einem konkreten Auftrag starten, zum Beispiel: `Beantworte diese Mandantenanfrage: [E-Mail einfügen]`

Nicht das komplette Repository-ZIP hochladen. Das Plugin-ZIP muss im Root direkt `.claude-plugin/plugin.json` und `skills/` enthalten.

---

## Ausgewählte Arbeitswege

Die Auswahl zeigt typische Mandantenanfragen. Alle Skills mit Kurzbeschreibungen und Downloads stehen in der [vollständigen Skill-Liste](../skills-index/mandantenanfragen-assistent.md).

| # | Skill-Name | Beschreibung | Lade-Trigger (Beispiele) |
|---|---|---|---|
| 1 | `anfrage-eingang-parser` | Extrahiert aus der Eingangsmail: Anrede, Name, E-Mail, Kontaktdaten, Sachverhaltsfetzen, Dringlichkeitssignale | "Anfrage auswerten", "E-Mail analysieren", "Kontaktdaten extrahieren" |
| 2 | `anrede-uebernehmen` | Bildet die passende Antwortanrede aus belegtem Absender, Namen und Titel; verwechselt Absender und angeschriebene Kanzleiperson nicht | "Anrede übernehmen", "formelle Anrede", "Titel erkennen" |
| 3 | `erstantwort-generator` | Hauptskill: erstellt die vollständige formelle Erstantwort-Mail mit allen Bausteinen | "Erstantwort schreiben", "Antwortmail erstellen", "Eingangsbestätigung" |
| 4 | `telefon-konfiguration` | Verwaltet Kanzlei-Kontaktdaten (Sekretariat + Transkriptionsservice) aus `kanzlei.json` und setzt sie in Templates ein | "Telefonnummer konfigurieren", "kanzlei.json bearbeiten" |
| 5 | `transkriptionsdienst-erklaerung` | Formuliert den Hinweis auf den automatisierten Transkriptionsservice: Ablauf, Datenschutz, Einwilligungserfordernis | "Transkriptionsservice erklären", "kann nicht schreiben" |
| 6 | `einwilligung-hinweis-datenschutz` | DSGVO-konforme Einwilligungsklausel für die Sprachaufnahme (Art. 6 Abs. 1 lit. a DSGVO, Art. 13 DSGVO) | "DSGVO Einwilligung formulieren", "Datenschutz Transkription" |
| 7 | `mandatsverhaeltnis-hinweis` | Grenzt Eingangsbestätigung, Mandatsannahme und Fristübernahme ab; kein pauschaler Ausschluss gesetzlicher Pflichten | "kein Mandat Hinweis", "Disclaimer Erstanfrage" |
| 8 | `vertraulichkeit-erinnerung` | Verschwiegenheit nach Paragraf 43a Absatz 2 BRAO knüpft an die Berufsausübung an, nicht erst an den Mandatsvertrag | "Schweigepflicht Anwalt", "wann gilt Verschwiegenheit" |
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

Gebührenabgleich vom 16.10.2026: [Paragraf 34 Absatz 1 RVG](https://www.gesetze-im-internet.de/rvg/__34.html) und [Nummer 7008 VV RVG](https://www.gesetze-im-internet.de/rvg/anlage_1.html) wurden amtlich gelesen. Die 190-EUR-Grenze betrifft das erste Beratungsgespräch mit einem Verbraucher ohne Gebührenvereinbarung; sie ist weder ein stets geschuldeter Pauschalpreis noch ein Bruttopreis. Umsatzsteuer soweit anfallend und erstattungsfähige Auslagen sind getrennt zu prüfen. Diese Qualifikation gilt auch für die kurzen Normhinweise in den Fachskills.

Quellenabgleich vom 16.10.2026: [Paragraf 43a Absatz 2 BRAO](https://www.gesetze-im-internet.de/brao/__43a.html) erfasst beruflich bekannt gewordene Informationen und setzt keinen bereits geschlossenen Mandatsvertrag voraus. Vertraulichkeit bei beruflichen Erstanfragen ist deshalb nicht bloß freiwillige Diskretion. [Paragraf 44 BRAO](https://www.gesetze-im-internet.de/brao/__44.html) verlangt die unverzügliche Erklärung einer gewollten Ablehnung; er verpflichtet nicht zur unverzüglichen Annahme. Beide amtlichen Normtexte wurden gelesen. Damit sind weder sämtliche Pflichten im Einzelfall noch die übrigen Berufsrechts- und Datenschutzangaben neu verifiziert.

---

## Lizenz

Apache-2.0 OR MIT — siehe [LICENSE](../LICENSE), [LICENSE-APACHE](../LICENSE-APACHE), [LICENSE-MIT](../LICENSE-MIT)

<!-- BEGIN FACHMODULE-NAVIGATION -->

Das Plugin bietet **10 auswählbare Skills**. Die **59 vollständigen Fachmodule** und ihre Hilfsdateien bleiben in der [Fachbibliothek](FACHMODULE.md) zugänglich. Wählen Sie den Arbeitsweg nach dem gewünschten Ergebnis; er führt zu den passenden Vertiefungen.

<!-- END FACHMODULE-NAVIGATION -->

<!-- BEGIN SKILLS-LOGIC (auto-generated) -->

## Orientierung nach Arbeitslogik

Diese Navigation ordnet die Skills nach typischen Arbeitsschritten. Ein Klick auf einen Skill lädt seine Markdown-Datei; die alphabetische Komplettliste bleibt darunter erhalten.

English: Skills are grouped by typical work phase. Clicking a skill downloads its Markdown file; the complete alphabetical list remains below.

| Arbeitsphase | Typische Skills |
| --- | --- |
| 1. Auftrag und bewährte Fachwerkzeuge | [`einstieg-routing`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=mandantenanfragen-assistent/skills/einstieg-routing/SKILL.md), [`juristischer-argumentationskern`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=mandantenanfragen-assistent/skills/juristischer-argumentationskern/SKILL.md), [`workflow-kaltstart-und-routing`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=mandantenanfragen-assistent/skills/workflow-kaltstart-und-routing/SKILL.md) |
| 2. Auftrag und Adressat | [`auftrag-und-adressat-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=mandantenanfragen-assistent/skills/auftrag-und-adressat-bearbeiten/SKILL.md) |
| 3. Sachverhalt | [`sachverhalt-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=mandantenanfragen-assistent/skills/sachverhalt-bearbeiten/SKILL.md) |
| 4. Normstruktur | [`normstruktur-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=mandantenanfragen-assistent/skills/normstruktur-bearbeiten/SKILL.md) |
| 5. Subsumtion und Gegenprobe | [`subsumtion-und-gegenprobe-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=mandantenanfragen-assistent/skills/subsumtion-und-gegenprobe-bearbeiten/SKILL.md) |
| 6. Arbeitsprodukt | [`arbeitsprodukt-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=mandantenanfragen-assistent/skills/arbeitsprodukt-bearbeiten/SKILL.md) |
| 7. Unterlagen und Quellen auswerten | [`unterlagen-und-quellen-auswerten-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=mandantenanfragen-assistent/skills/unterlagen-und-quellen-auswerten-bearbeiten/SKILL.md) |
| 8. Arbeitsprodukt ausarbeiten und kontrollieren | [`arbeitsprodukt-ausarbeiten-und-kontrollieren-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=mandantenanfragen-assistent/skills/arbeitsprodukt-ausarbeiten-und-kontrollieren-bearbeiten/SKILL.md) |

<!-- END SKILLS-LOGIC (auto-generated) -->

<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Überblick

Automatisch generierte Komplett-Liste aller 10 Skills in diesem Plugin. Jeder Skillname und der Downloadlink laden den unveränderten Inhalt der zugehörigen `SKILL.md` als Markdown-Datei. Der eindeutige Dateiname enthält Plugin und Skill; Beschreibungen stammen aus dem jeweiligen `description`-Feld.

English: Complete list of all 10 skills in this plugin. Both links in each row download the unchanged `SKILL.md` content as a Markdown file with a unique plugin-and-skill filename.

| Skill | Beschreibung | Markdown-Download |
| --- | --- | --- |
| [`arbeitsprodukt-ausarbeiten-und-kontrollieren-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=mandantenanfragen-assistent/skills/arbeitsprodukt-ausarbeiten-und-kontrollieren-bearbeiten/SKILL.md) | Anwaltschaftliche Mandantenanfragen: Arbeitsprodukt ausarbeiten und kontrollieren: Den verlangten Text oder die Berechnung fertigstellen, Gegenposition, Quellenstatus und offene Punkte prüfen und die nächste Handlung erklären. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=mandantenanfragen-assistent/skills/arbeitsprodukt-ausarbeiten-und-kontrollieren-bearbeiten/SKILL.md) |
| [`arbeitsprodukt-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=mandantenanfragen-assistent/skills/arbeitsprodukt-bearbeiten/SKILL.md) | Anwaltschaftliche Mandantenanfragen: Arbeitsprodukt: Kurzvermerk, Gutachten, Schriftsatzkern, Mandantenbrief, Entscheidungsbaum oder Zitierkontrolle vollständig ausformulieren. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=mandantenanfragen-assistent/skills/arbeitsprodukt-bearbeiten/SKILL.md) |
| [`auftrag-und-adressat-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=mandantenanfragen-assistent/skills/auftrag-und-adressat-bearbeiten/SKILL.md) | Anwaltschaftliche Mandantenanfragen: Auftrag und Adressat: Rechtsfrage, gewünschtes Produkt, Empfänger, Frist und Entscheidungsschwelle in einem Satz festlegen. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=mandantenanfragen-assistent/skills/auftrag-und-adressat-bearbeiten/SKILL.md) |
| [`einstieg-routing`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=mandantenanfragen-assistent/skills/einstieg-routing/SKILL.md) | Für Einstieg und Routing: routet Rolle, Frist, Unterlagen und Fachschritt; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. Fachgebiet: mandantenanfragen-assistent. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=mandantenanfragen-assistent/skills/einstieg-routing/SKILL.md) |
| [`juristischer-argumentationskern`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=mandantenanfragen-assistent/skills/juristischer-argumentationskern/SKILL.md) | Mandantenanfrage zum konkreten Antwortentwurf führen. Verarbeitet vorhandene Unterlagen, verbindet entscheidende Fachprüfungen und belegte Quellen, erstellt das beauftragte Ergebnis und führt denselben Vorgang nach neuen Angaben fort. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=mandantenanfragen-assistent/skills/juristischer-argumentationskern/SKILL.md) |
| [`normstruktur-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=mandantenanfragen-assistent/skills/normstruktur-bearbeiten/SKILL.md) | Anwaltschaftliche Mandantenanfragen: Normstruktur: Anspruchsgrundlage oder Prüfungsmaßstab in Tatbestandsmerkmale, Rechtsfolge, Einwendungen und Beweislast zerlegen. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=mandantenanfragen-assistent/skills/normstruktur-bearbeiten/SKILL.md) |
| [`sachverhalt-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=mandantenanfragen-assistent/skills/sachverhalt-bearbeiten/SKILL.md) | Anwaltschaftliche Mandantenanfragen: Sachverhalt: Chronologie, Beteiligte, Dokumentfundstellen, unstreitige Tatsachen, Behauptungen und Lücken sauber trennen. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=mandantenanfragen-assistent/skills/sachverhalt-bearbeiten/SKILL.md) |
| [`subsumtion-und-gegenprobe-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=mandantenanfragen-assistent/skills/subsumtion-und-gegenprobe-bearbeiten/SKILL.md) | Anwaltschaftliche Mandantenanfragen: Subsumtion und Gegenprobe: für jedes Merkmal Tatsache, Beleg, Schluss, stärkstes Gegenargument und Gegenbeweis ausweisen. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=mandantenanfragen-assistent/skills/subsumtion-und-gegenprobe-bearbeiten/SKILL.md) |
| [`unterlagen-und-quellen-auswerten-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=mandantenanfragen-assistent/skills/unterlagen-und-quellen-auswerten-bearbeiten/SKILL.md) | Anwaltschaftliche Mandantenanfragen: Unterlagen und Quellen auswerten: Akte, Belege, Chronologie, Recherche und entscheidende Lücken für den konkreten Fachauftrag nachvollziehbar erschließen. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=mandantenanfragen-assistent/skills/unterlagen-und-quellen-auswerten-bearbeiten/SKILL.md) |
| [`workflow-kaltstart-und-routing`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=mandantenanfragen-assistent/skills/workflow-kaltstart-und-routing/SKILL.md) | Für Kaltstart und Routing: routet Rolle, Frist, Unterlagen und Fachschritt; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. Fachgebiet: mandantenanfragen-assistent. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=mandantenanfragen-assistent/skills/workflow-kaltstart-und-routing/SKILL.md) |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
