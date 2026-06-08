# mandantenanfragen-assistent

<!-- BEGIN plugin-sofort-download-section (autogen) -->
## ⬇️ Sofort-Downloads

Direkt-Downloads ohne Umwege. Die URLs sind stabil und zeigen immer auf die aktuelle Version (`latest`-Release).

### Plugin als ZIP

| Inhalt | Download |
| --- | --- |
| **Dieses Plugin** (`mandantenanfragen-assistent`) | [`mandantenanfragen-assistent.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/mandantenanfragen-assistent.zip) |

### Demonstrations-Akten

| Akte | PDF lesen | Akten-ZIP |
| --- | --- | --- |
| **Mandantenanfragen Q2/2026 — Kanzlei Roosendaal & Tannenfels, Köln** (`mandantenanfragen-kanzlei-roosendaal-koeln-erstkontakt-q2-2026`) | [Gesamt-PDF lesen](../testakten/mandantenanfragen-kanzlei-roosendaal-koeln-erstkontakt-q2-2026/gesamt-pdf/mandantenanfragen-kanzlei-roosendaal-koeln-erstkontakt-q2-2026_gesamt.pdf) | [`testakte-mandantenanfragen-kanzlei-roosendaal-koeln-erstkontakt-q2-2026.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-mandantenanfragen-kanzlei-roosendaal-koeln-erstkontakt-q2-2026.zip) |

<!-- END plugin-sofort-download-section (autogen) -->

**Version:** 3.2.1
**Author:** Klotzkette
**Lizenz:** Apache-2.0 OR MIT

---

Assistent für Anwaltskanzleien zur automatisierten Erstantwort auf eingehende Mandantenanfragen per E-Mail. Das Plugin dankt formell für die Anfrage, übernimmt die exakte Anrede aus der eingehenden Mail, weist auf die telefonische Terminvergabe hin und bittet um eine Sachverhaltszusammenfassung per E-Mail. Für Personen, die nicht schreiben können oder möchten, bietet es einen automatisierten Transkriptionsservice an — mit DSGVO-konformem Einwilligungshinweis.

---

## Installation

1. ZIP aus dem Release herunterladen.
2. Claude Code oder Claude Desktop/Cowork öffnen.
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


<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Ueberblick

Automatisch generierte Komplett-Liste aller 54 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `anfrage-eingang-parser` | Sekretariat oder Anwalt erhielt E-Mail-Anfrage eines potentiellen Mandanten und will sie schnell strukturiert auswerten. E-Mail-Parser Kanzlei. Prüfraster: Anrede Name Absender E-Mail-Adresse Telefon Sachverhaltsfetzen Stichwörter dringl... |
| `anrede-anwaltskanzleien-bittet` | Anrede: Verhandlung, Vergleich und Eskalation im Plugin mandantenanfragen assistent im Mandantenanfragen Assistent. |
| `anrede-uebernehmen` | Antwort-E-Mail soll mit exakt richtiger Anrede des potentiellen Mandanten beginnen ohne Fehler bei Titeln oder Doppelnamen. Anredekonventionen Kanzlei. Prüfraster: Titel (Dr. Prof. Mag.) Doppelnamen Adelspraeifikate kirchliche Titel Komp... |
| `anschluss-routing` | Anschluss-Routing für Mandantenanfragen-Assistent: wählt den nächsten Spezial-Skill nach Engpass (Unverzügliche Antwort, Mandantenmail, Kanzleiprofil, Honorarinfo), dokumentiert Router-Entscheidung mit Begründung. |
| `anwaltskanzleien-erstpruefung-und-mandatsziel` | Anwaltskanzleien: Erstprüfung, Rollenklärung und Mandatsziel im Plugin mandantenanfragen assistent im Mandantenanfragen Assistent. |
| `bietet-fehlerkatalog` | Bietet Fehlerkatalog: Fehlerbremse; prüft Fristen, Zuständigkeit, Beweislast, Quellen und taktische Risiken vor Abgabe oder Versand. |
| `bittet-internationaler-bezug-und-schnittstellen` | Bittet: Internationaler Bezug und Schnittstellen im Plugin mandantenanfragen assistent im Mandantenanfragen Assistent. |
| `dankt-dsgvo-sonderfall-e-mail` | Dankt: Risikoampel, Gegenargumente und Verteidigungslinien im Plugin mandantenanfragen assistent im Mandantenanfragen Assistent. |
| `dokumente-intake` | Dokumentenintake für Mandantenanfragen-Assistent: sortiert Mandantenmail, Kanzleiprofil, Honorarinfo, prüft Datum, Absender, Frist und Beweiswert (Urkunden, Zeugen); markiert Lücken; berücksichtigt Mandatsgeheimnis § 43a BRAO. |
| `dringlichkeitsmarker-einwilligung-hinweis` | Eingehende Mandantenanfrage enthaelt möglicherweise Fristenproblem oder dringenden Handlungsbedarf. Dringlichkeitscheck Kanzlei-Intake. Prüfraster: Signale Hauptverhandlung naechste Woche Kündigungsfrist Zwangsvollstreckung Insolvenzantr... |
| `dsgvo-sonderfall-und-edge-case` | DSGVO: Sonderfall und Edge-Case-Prüfung im Plugin mandantenanfragen assistent im Mandantenanfragen Assistent. |
| `e-mail-erstantwort-und-terminrouting` | E-Mail-Erstantwort, Terminrouting und Mandatsannahmehinweis: führt schnell durch Sachverhalt, Rechtsgrundlagen, Belege, Risiken und erzeugt einen verwertbaren nächsten Output im Mandantenanfragen Assistent. |
| `eingehenden-quellenkarte` | Eingehenden Quellenkarte: Quellenprüfung; Normenstand, Rechtsprechung, Behördenpraxis und Zitierfähigkeit werden vor einer tragenden Aussage verifiziert. |
| `einstieg-routing` | Einstieg, Triage und Routing für Mandantenanfragen-Assistent: ordnet Rolle (Mandant, Anwalt, Sekretariat), markiert Frist (Unverzügliche Antwort), wählt Norm (BRAO § 43 Sachlichkeit, BORA) und Zuständigkeit (zuständige Stelle), leitet zu... |
| `einwilligung-hinweis-datenschutz` | Kanzlei bietet telefonischen Transkriptionsservice an und muss DSGVO-konforme Einwilligung einholen. Art. 6 Abs. 1 lit. a DSGVO Art. 13 DSGVO Informationspflicht. Prüfraster: Rechtsgrundlage Einwilligung Informationspflicht Hinweis kein... |
| `einwilligungshinweis-fristennotiz-und-naechster-schritt` | Einwilligungshinweis: Fristennotiz und nächster Schritt im Plugin mandantenanfragen assistent im Mandantenanfragen Assistent. |
| `erstantwort-foermlich-mail` | Erstantwort: Tatbestandsmerkmale, Beweisfragen und Beleglage im Plugin mandantenanfragen assistent im Mandantenanfragen Assistent. |
| `erstantwort-generator` | Sekretariat oder Anwalt muss professionelle Erstantwort-E-Mail an potentiellen Mandanten senden. Hauptskill Erstantwort-E-Mail. Prüfraster: Dank für Anfrage exakte Anrede Terminvergabe-Hinweis Transkriptionsservice mit DSGVO-Einwilligung... |
| `foermlich-behoerden-gericht-und-registerweg` | Foermlich: Behörden-, Gerichts- oder Registerweg im Plugin mandantenanfragen assistent im Mandantenanfragen Assistent. |
| `folgekorrespondenz-vorbereiten-konfliktcheck` | Nach Eingang einer Anfrage muss Sekretariat CRM-Eintrag und Akte anlegen. CRM-Eintrag Kanzlei-Intake. Prüfraster: Name Mail Telefon Anliegen-Stichwort Dringlichkeit Datum Sprachkennung Konfliktcheck-Status. Output: Skeleton-Eintrag für C... |
| `konfliktcheck-vorab` | Sekretariat soll vor Terminvergabe Interessenkonflikt prüfen. § 43a Abs. 4 BRAO § 3 BORA Interessenkonflikt-Check. Prüfraster: Gegenseite und Beteiligte erfragen Datenbankabgleich bestehende Mandate. Output: Konfliktcheck-Anweisung und A... |
| `ma-aufnahmegespraech-leitfaden` | Aufnahmegespraechsleitfaden Mandant: Sachverhalt, Eilbedarf, Ziel, Bereits eingeleitete Schritte, Andere beauftragte Anwaelte, Konflikte, Vergueng. Strukturierte Fragen und typische Stolpersteine. Mustertext zur Mandatsbestaetigung im Ma... |
| `ma-einfuehrung-erstkontakt` | Erstkontakt-Typen einfuehrend: Telefon, E-Mail, Webformular, Walk-in, Empfehlung. Pro Typ: Risiken, Dokumentation, Datenschutz, Naechster Schritt. Routing-Logik und Eskalation bei sensiblen Faellen im Mandantenanfragen Assistent. |
| `ma-erstvermerk-mandantenakte` | Erstvermerk für die Mandantenakte: Pflichtangaben (Mandant, Sachverhalt, Eilbedarf, Ziel, Honorar, naechster Schritt), interne Hinweise (Konflikte, sensible Punkte). Format und Aufbewahrung in der Akte im Mandantenanfragen Assistent. |
| `ma-konfliktcheck-konzern` | Spezialfall Konfliktcheck im Konzern: Mandat für Tochter eines bestehenden Mandanten, gegenlaeufige Interessen, Chinese Walls, Information Barriers. Pruefraster und Mustertexte für Einwilligungen und Hinweis an Mandant im Mandantenanfrag... |
| `ma-mandant-manda-erstgespraechsleitfaden` | Spezialfall Mandant mit gesetzlicher Betreuung oder Vorsorgevollmacht: Pruefen der Vertretungsmacht, Einwilligungsfaehigkeit, Schweigepflicht gegenueber Betreuer, Beauftragung nur für den Aufgabenkreis. Mustertexte und Pruefraster. Route... |
| `mail-dokumentenmatrix-und-lueckenliste` | Mail: Dokumentenmatrix, Lückenliste und Nachforderung im Plugin mandantenanfragen assistent im Mandantenanfragen Assistent. |
| `manda-erstgespraechsleitfaden-checkliste` | Checkliste Erstgespraechsleitfaden: Sachverhaltserhebung, Ziel des Mandanten, vorhandene Unterlagen, Erfolgsaussicht offen erlaeutern, Honorar. Mustertext Folgeschreiben Mandant im Mandantenanfragen Assistent. |
| `manda-erstkontakt-triagebogen-bauleiter` | Bauleiter Triagebogen Erstkontakt: Mandantendaten, COI-Pruefung, Rechtsschutzversicherung, Eilbeduerftigkeit, RVG-Hinweis. Pruefraster für Sekretariat und Anwalt im Mandantenanfragen Assistent. |
| `manda-mandatsablehnung-rechtsschutz` | Spezialfall Mandatsablehnung und COI-Kommunikation: berufsrechtliche Hinweise § 43a BRAO, Schweigepflicht, Ablehnungsschreiben ohne offene Konflikte. Pruefraster für Risk-and-Compliance im Mandantenanfragen Assistent. |
| `manda-rechtsschutz-eintrittsanfrage-spezial` | Spezialfall Rechtsschutzversicherung-Eintrittsanfrage: Deckungsanfrage, Stichentscheid, Mustertext für Auseinandersetzung mit Rechtsschutzversicherer. Pruefraster Mandant und Anwalt im Mandantenanfragen Assistent. |
| `mandantenanfragen-anfrage-eingang-anrede` | Mandantenanfragen: Fristen, Form, Zuständigkeit und Rechtsweg im Plugin mandantenanfragen assistent im Mandantenanfragen Assistent. |
| `mandantenkommunikation-redteam` | Mandantenkommunikation: übersetzt das Ergebnis in eine klare Nachricht mit Entscheidungspunkten, Risiken und nächsten Schritten im Mandantenanfragen Assistent. |
| `mandatsverhaeltnis-hinweis` | Antwortmail muss klar machen dass noch kein Mandatsverhältnis besteht und keine Rechtsberatung erfolgt. § 43 BRAO Haftungsabgrenzung Erstanfrage. Prüfraster: Beantwortung der Anfrage = keine Rechtsberatung kein Mandatsverhältnis kein Pfl... |
| `mehrsprachige-antwort-muster-erstantwort-spam` | Mandantenanfrage kam auf Englisch Franzoesisch oder Italienisch und Antwort soll in derselben Sprache erfolgen. Mehrsprachige Erstantwort Kanzlei. Prüfraster: Sprache erkennen Anredekonventionen Schlussformeln Datenschutzhinweise in Ziel... |
| `muster-erstantwort` | Kanzlei benoetigt fertige ausfuellbare Vorlage für die Erstantwort auf Mandantenanfragen. Template Erstantwort. Prüfraster: Platzhalter KANZLEI-NAME SEKRETARIATS-TELEFON TRANSKRIPTIONS-TELEFON UNTERZEICHNENDE-RA. Drei Varianten Standard... |
| `nennt-sachverhalt-telefon` | Nennt: Zahlen, Schwellenwerte und Berechnung im Plugin mandantenanfragen assistent im Mandantenanfragen Assistent. |
| `output-waehlen` | Output-Wahl für Mandantenanfragen-Assistent: stimmt Adressat (Mandant, Anwalt, Sekretariat), Frist (Unverzügliche Antwort) und Form auf den Zweck ab — typische Outputs: Antwortentwurf, Empfangsbestätigung, Rückfrage-Vorschlag. |
| `quellen-livecheck` | Quellen-Live-Check für Mandantenanfragen-Assistent: prüft Normen (BRAO § 43 Sachlichkeit, BORA) gegen amtliche Datenbank, Rechtsprechung mit Gericht-Datum-Az-Rn; nutzt zuständige Stelle und Quellenhygiene nach references/quellenhygiene.md. |
| `sachverhalt-formular-portal-und-einreichung` | Sachverhalt: Formular, Portal und Einreichungslogik im Plugin mandantenanfragen assistent im Mandantenanfragen Assistent. |
| `spam-und-massen-anfrage-filter` | Sekretariat hat Anfrage erhalten die verdaechtig ausschaut. Spam-Erkennung Kanzlei-Eingang. Prüfraster: Spam Werbung 419-Scams automatisierte Recruiter-Mails Massen-Mandantenanfragen Phishing. Output: Spam-Einschaetzung mit Empfehlung Au... |
| `start-chronologie-fristen` | Einstieg, Schnelltriage und Fallrouting im Mandantenanfragen Assistent-Plugin. Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken und Wunsch-Output ab, schlägt passende Fachmodule aus diesem Plugin vor und führt in einen klaren Arbeitsplan.... |
| `telefon-konfiguration` | Kanzlei muss Telefonnummern für Sekretariat und Transkriptionsservice in den Antwort-Templates hinterlegen. Konfigurationsverwaltung Kanzlei-Nummern. Prüfraster: kanzlei.json Sekretariatsnummer Transkriptionsnummer Lesen und Setzen der P... |
| `telefon-mandantenkommunikation-entscheidungsvorlage` | Telefon: Mandantenkommunikation und Entscheidungsvorlage im Plugin mandantenanfragen assistent im Mandantenanfragen Assistent. |
| `telefonische-terminvergabe-interessen` | Telefonische: Compliance-Dokumentation und Aktenvermerk im Plugin mandantenanfragen assistent im Mandantenanfragen Assistent. |
| `terminvergabe-mehrparteien-konflikt-und-interessen` | Terminvergabe: Mehrparteienkonflikt und Interessenmatrix im Plugin mandantenanfragen assistent im Mandantenanfragen Assistent. |
| `transkription-beweislast-und-darlegungslast` | Transkription: Beweislast, Darlegungslast und Substantiierung im Plugin mandantenanfragen assistent im Mandantenanfragen Assistent. |
| `transkriptionsdienst-erklaerung` | Mandant kann seinen Fall nicht schriftlich schildern und soll stattdessen anrufen. Transkriptionsservice Erklärung in Erstantwort. Prüfraster: Telefonnummer Ablauf des Anrufs Verarbeitungshinweis DSGVO-Einwilligung Kein-Mandat-Hinweis. O... |
| `uebernimmt-telefon-konfiguration` | Uebernimmt: Schriftsatz-, Brief- und Memo-Bausteine im Plugin mandantenanfragen assistent im Mandantenanfragen Assistent. |
| `unterlagen-luecken` | Lücken- und Beschaffungsliste für Mandantenanfragen-Assistent: trennt fehlende Tatsachen von fehlenden Belegen (Mandantenmail, Kanzleiprofil, Honorarinfo), nennt pro Lücke Beweisthema, Beschaffungsweg (zuständige Stelle), Frist und Ersat... |
| `vertraulichkeit-erinnerung` | Vertraulichkeit Erinnerung im Mandantenanfragen-Triage im Mandantenanfragen Assistent. |
| `workflow-chronologie-und-belegmatrix` | Chronologie und Belegmatrix: macht aus unordentlichem Material eine Timeline mit Belegstellen und offenen Widersprüchen im Mandantenanfragen Assistent. |
| `workflow-fristen-und-risikoampel` | Fristen- und Risikoampel: macht eine Sofortampel für Frist, Zuständigkeit, Haftung, Eilbedarf und fehlende Unterlagen im Mandantenanfragen Assistent. |
| `workflow-redteam-qualitygate` | Red-Team Qualitygate: prüft das Ergebnis auf Halluzinationen, Fristenfehler, Zuständigkeit, Quellen, Beweise und Ton im Mandantenanfragen Assistent. |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
