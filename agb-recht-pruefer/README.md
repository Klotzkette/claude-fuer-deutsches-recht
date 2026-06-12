# AGB-Recht-Prüfer

<!-- BEGIN plugin-sofort-download-section (autogen) -->

## ⬇️ Sofort-Downloads

Direkt-Downloads ohne Umwege. Die URLs sind stabil und zeigen immer auf die aktuelle Version (`latest`-Release).

### Plugin als ZIP

| Inhalt | Download |
| --- | --- |
| **Dieses Plugin** (`agb-recht-pruefer`) | [`agb-recht-pruefer.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/agb-recht-pruefer.zip) |

### Demonstrations-Akten

| Akte | PDF lesen | Akten-ZIP |
| --- | --- | --- |
| **BGB BT — Smart-Kühlschrank, digitale Elemente und Reparaturblockade** (`bgb-bt-smart-kuehlschrank-digital-repair-koeln`) | [Gesamt-PDF lesen](../testakten/bgb-bt-smart-kuehlschrank-digital-repair-koeln/gesamt-pdf/bgb-bt-smart-kuehlschrank-digital-repair-koeln_gesamt.pdf) | [`testakte-bgb-bt-smart-kuehlschrank-digital-repair-koeln.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-bgb-bt-smart-kuehlschrank-digital-repair-koeln.zip) |
| **Akte Nordstern MedTech Vertrieb - Provision, Buchauszug und Ausgleich** (`handelsvertreterrecht-provisionsausgleich-nordstern-medtech`) | [Gesamt-PDF lesen](../testakten/handelsvertreterrecht-provisionsausgleich-nordstern-medtech/gesamt-pdf/handelsvertreterrecht-provisionsausgleich-nordstern-medtech_gesamt.pdf) | [`testakte-handelsvertreterrecht-provisionsausgleich-nordstern-medtech.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-handelsvertreterrecht-provisionsausgleich-nordstern-medtech.zip) |
| **Akte Vellbruck Robotics GmbH — Roboterflotte AtlasCare / LumaMove / Werkbank C7** (`robotikrecht-roboterflotte-vellbruck-muenchen`) | [Gesamt-PDF lesen](../testakten/robotikrecht-roboterflotte-vellbruck-muenchen/gesamt-pdf/robotikrecht-roboterflotte-vellbruck-muenchen_gesamt.pdf) | [`testakte-robotikrecht-roboterflotte-vellbruck-muenchen.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-robotikrecht-roboterflotte-vellbruck-muenchen.zip) |

<!-- END plugin-sofort-download-section (autogen) -->

Gigantisches Plugin für deutsches AGB-Recht: Prüfen, Entwerfen, Redlinen, Verhandeln, Rollout und Streitverteidigung von Allgemeinen Geschäftsbedingungen in allen praktischen Varianten.

Das Plugin ist bewusst zweigleisig gebaut:

- **AGB prüfen:** Klauseln zerlegen, Einbeziehung und Transparenz prüfen, §§ 305 bis 310 BGB sauber anwenden, Risiko bewerten, bessere Fassung vorschlagen.
- **AGB entwerfen:** Geschäftsmodell verstehen, Klauselfamilien auswählen, sichere oder bewusst risikobehaftete Fassungen erzeugen, Rollout und Nachweisfähigkeit mitdenken.

## Start

```text
/agb-recht-prüfer:allgemein
```

Der Einstieg fragt zuerst nicht zwanzig Dinge ab, sondern klärt die wichtigste Weiche: **prüfen oder entwerfen?** Danach routet er in passende Spezialskills, etwa Verbraucher-AGB, B2B-AGB, Online-Checkout, Preisanpassung, Haftung, Laufzeit, UKlaG, Redline oder konkrete Branchenbedingungen.

## Arbeitsweise

1. Klausel und Vertragstyp erfassen.
2. AGB-Eigenschaft und Einbeziehung prüfen.
3. Überraschung, Mehrdeutigkeit und Transparenz klären.
4. Inhaltskontrolle nach §§ 307 bis 309 BGB und Besonderheiten nach § 310 BGB.
5. Rechtsfolge, Rückabwicklung, UKlaG-/Prozessrisiko prüfen.
6. Bessere Klausel entwerfen: sicher, balanced oder aggressiv mit Warnlabel.
7. Rollout, Versionierung, Nachweisbarkeit und Fachbereichskommunikation erledigen.

## Live-Quellen

Das Plugin soll bei tragenden Aussagen immer die aktülle amtliche Fassung auf **Gesetze im Internet** prüfen, insbesondere BGB §§ 305 bis 310 und UKlaG. Siehe [`references/QUELLEN.md`](./references/QUELLEN.md).

## Typische Ergebnisse

| Bedarf | Ergebnis |
| --- | --- |
| Fremde AGB schnell prüfen | Klauselampel, Risikobegründung, Redline-Kommentar |
| Eigene AGB neu entwerfen | Klauselarchitektur, sichere Fassungen, Fallbacks |
| B2C-Rollout vorbereiten | Checkout-/Einbeziehungscheck, Versionierung, Kundenkommunikation |
| B2B-Verhandlung führen | Playbook mit Must-have, Fallback, No-Go und Argumenten |
| Abmahnung erhalten | Fristenscan, UKlaG-Risiko, modifizierte Unterlassungserklärung |
| Management informieren | kurze Legal Note mit Risiko, Optionen und Empfehlung |

## Enthaltene Skills

Die vollständige Skill-Liste wird automatisch am Ende dieser README aktualisiert.

## Lizenz

Apache-2.0 OR MIT — Auswahl beim Empfänger.


<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Überblick

Automatisch generierte Komplett-Liste aller 302 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `abmahnung-reagieren` | Output- und Streit-Skill für Abmahnung Reagieren: macht aus der AGB-Prüfung verwertbare Redlines, Entwürfe, Playbooks, Abmahnreaktionen oder Entscheidungsunterlagen. |
| `abnahme-testing` | Klausel-Fachmodul für Abnahme Testing: prüft, redlined und entwirft die Klausel mit Risikoampel, Verbraucher-/B2B-Unterscheidung und praxistauglicher Ersatzfassung. |
| `abtretung-adversarial-test` | Klausel-Fachmodul für Abtretung: prüft, redlined und entwirft die Klausel mit Risikoampel, Verbraucher-/B2B-Unterscheidung und praxistauglicher Ersatzfassung im AGB-Recht. |
| `adversarial-test-agb` | Output- und Streit-Skill für Adversarial Test AGB: macht aus der AGB-Prüfung verwertbare Redlines, Entwürfe, Playbooks, Abmahnreaktionen oder Entscheidungsunterlagen. |
| `aenderungsvorbehalt-308` | Norm- und Dogmatik-Skill für Änderungsvorbehalt 308: prüft die AGB-Kontrolle quellenstreng entlang BGB §§ 305 bis 310 und ordnet Rechtsfolge, Risiko und bessere Fassung. |
| `agb-abtretung` | Klausel-Fachmodul für Abtretung: prüft, redlined und entwirft die Klausel mit Risikoampel, Verbraucher-/B2B-Unterscheidung und praxistauglicher Ersatzfassung. |
| `agb-anwaltsvertrag-allg-mandatsbedingungen` | AGB im Anwaltsvertrag und Allgemeine Mandatsbedingungen. Skill klaert die AGB-rechtliche Prüfung typischer Mandatsbedingungen Verguetungsklauseln Verzugsregelungen Verschwiegenheit Auflagen RVG-konforme Honorarvereinbarungen und Sonderv... |
| `agb-anwaltsvertrag-und-allg-mandatsbedingungen` | AGB im Anwaltsvertrag und Allgemeine Mandatsbedingungen. Skill klaert die AGB-rechtliche Prüfung typischer Mandatsbedingungen Verguetungsklauseln Verzugsregelungen Verschwiegenheit Auflagen RVG-konforme Honorarvereinbarungen und Sonderv... |
| `agb-arbeitnehmerueberlassung-aueg` | AGB bei Arbeitnehmerueberlassung (AUeG). Skill klaert die AGB-rechtliche Prüfung der Standardvertraege zwischen Verleiher Entleiher und Leiharbeitnehmer Equal-Pay-Klauseln Branchenzuschlaege Verleihbarkeitsausschluss Vertragsstrafe bei... |
| `agb-auditrechte` | Klausel-Fachmodul für Auditrechte: prüft, redlined und entwirft die Klausel mit Risikoampel, Verbraucher-/B2B-Unterscheidung und praxistauglicher Ersatzfassung. |
| `agb-begriff-vorformuliert-305` | Norm- und Dogmatik-Skill für AGB Begriff Vorformuliert 305: prüft die AGB-Kontrolle quellenstreng entlang BGB §§ 305 bis 310 und ordnet Rechtsfolge, Risiko und bessere Fassung. |
| `agb-bei-digitalen-produkten-327f-update` | AGB bei digitalen Produkten und § 327f BGB Update-Pflicht. Skill vertieft die AGB-rechtliche Behandlung von Update-Klauseln Aktualisierungspflichten Funktionsanpassungen sowie das Verhältnis zur Hauptleistungspflicht. Aktuelle BGH-Folge... |
| `agb-bei-iso-vertraegen-international` | AGB bei internationalen ISO-Vertraegen. Skill behandelt die AGB-rechtliche Prüfung internationaler Vertragsmuster ICC FIDIC ISDA AIA und ihre Anpassung an deutsches Recht. Klaert die Wechselwirkung mit Rom-I und ordre public. Behandelt... |
| `agb-bei-kreditvertraegen-verbraucherdarlehen` | AGB bei Verbraucherdarlehensvertraegen. Skill behandelt AGB im Kontext der §§ 491 ff. BGB Vorvertragliche Information Widerrufsrecht effektiver Jahreszins Sondervorschriften zu Restschuldversicherung Bearbeitungsentgelt Bearbeitungsgebue... |
| `agb-bei-plattformnutzung-app-stores` | AGB bei Plattformnutzung App Stores Apple Google Steam Amazon. Skill klaert die AGB-rechtlichen Kontrollfaktoren der Standardvertraege Marktstellung und Marktmacht (Art. 102 AEUV) sowie das Verhältnis zur P2B-Verordnung. Behandelt aktue... |
| `agb-bei-vereinen-und-verbaenden` | AGB bei Vereinen und Verbaenden. Skill klaert die AGB-rechtliche Prüfung von Vereinsbeitrittsbedingungen Beitragsregelungen Ausschlussklauseln und Vereinsstrafen. Behandelt das Spannungsverhaeltnis zwischen Vereinsautonomie (Art. 9 GG)... |
| `agb-bei-versicherungsvertraegen-vvg` | AGB-Kontrolle bei Versicherungsvertraegen (VVG). Skill behandelt das Spannungsverhaeltnis zwischen den Allgemeinen Versicherungsbedingungen (AVB) und § 307 BGB. Klaert das Transparenzgebot Risikoausschluesse Obliegenheitsverletzungen San... |
| `agb-bonitaetspruefung-score-klauseln` | Klausel-Fachmodul für Bonitätsprüfung: prüft, redlined und entwirft die Klausel mit Risikoampel, Verbraucher-/B2B-Unterscheidung und praxistauglicher Ersatzfassung. |
| `agb-eigentumsvorbehalt-b2b-b2c` | Klausel-Fachmodul für Eigentumsvorbehalt: prüft, redlined und entwirft die Klausel mit Risikoampel, Verbraucher-/B2B-Unterscheidung und praxistauglicher Ersatzfassung. |
| `agb-entwurf-kaltstart` | Einstiegs- und Prüfungslinie für AGB Entwurf Kaltstart: sortiert Ziel, Rolle, Dokumente, Normenstand, AGB-Risiko und nächsten Output schnell und anfängertauglich. |
| `agb-exklusivitaet` | Klausel-Fachmodul für Exklusivität: prüft, redlined und entwirft die Klausel mit Risikoampel, Verbraucher-/B2B-Unterscheidung und praxistauglicher Ersatzfassung. |
| `agb-formulararbeitsvertrag-305ff-bgb` | Branchen-Fachmodul für Formulararbeitsvertrag: prüft typische AGB-Risiken des Vertragstyps und erzeugt Klauselarchitektur, Red Flags und bessere Bedingungen. |
| `agb-fuer-vereinsausschluss-und-haftung` | AGB-Klauseln zum Vereinsausschluss und zur Haftung im Verein. Skill klaert die AGB-rechtliche Prüfung von Ausschlussklauseln in Vereinssatzungen und Beitrittsformularen das Verhältnis zur Vereinsautonomie und das gerichtliche Prüfrast... |
| `agb-gerichtsstand` | Klausel-Fachmodul für Gerichtsstand: prüft, redlined und entwirft die Klausel mit Risikoampel, Verbraucher-/B2B-Unterscheidung und praxistauglicher Ersatzfassung. |
| `agb-haftung-erfuellungsgehilfen` | AGB-Haftung für Erfuellungsgehilfen. Skill klaert die AGB-rechtliche Behandlung von Haftungsausschluessen für Erfuellungsgehilfen (§ 278 BGB) und die Wechselwirkung mit § 309 Nr. 7 BGB. Behandelt die BGH-Linie zur unwirksamen Pauschalfre... |
| `agb-im-arbeitsvertrag-310-abs-4-vertieft` | Arbeitsvertrags-AGB nach § 310 Abs. 4 BGB. Skill vertieft die AGB-Kontrolle im Arbeitsrecht: Anwendbarkeit der §§ 305 ff. BGB auf vorformulierte Arbeitsvertragsklauseln Sonderregeln für Tarifvertraege und Betriebsvereinbarungen. Behandel... |
| `agb-im-bankvertrag-sparkassen-und-banken` | AGB-Kontrolle im Bankvertrag. Skill behandelt die Banken-AGB Sparkassen-AGB und Allgemeinen Geschäftsbedingungen der Volks- und Raiffeisenbanken Klauseln zu Entgelten Änderungen einseitige Vertragsanpassung BGH-Linie zu Gebührenklausel... |
| `agb-im-bauvertrag-vob-b-2024` | AGB-Kontrolle der VOB-B im Bauvertrag. Skill klaert die BGH-Linie zur AGB-rechtlichen Behandlung der VOB-B insgesamt und einzelner Klauseln. Behandelt das Privileg der VOB-B unter § 310 Abs. 1 BGB Erlass des § 308 und § 309 BGB bei volls... |
| `agb-im-konzernverbund` | AGB im Konzernverbund. Skill behandelt die AGB-rechtliche Prüfung von Konzernvereinbarungen Service-Level-Agreements zwischen Mutter und Tochter sowie Standardklauseln bei konzerninternen Vertraegen. Aktuelle Themen: Cash-Pooling Cross-... |
| `agb-im-leasingvertrag-fortwirkung` | AGB im Leasingvertrag. Skill klaert AGB-Klauseln in Operating- und Finance-Leasing Verteilung der Sach- und Rechtsgefahr Maengelhaftungs-Drittinanspruchnahme (Drittabtretungsmodell BGH) Restwertabrechnung Andienung Mehrkilometerregelung.... |
| `agb-im-mietrecht-wohnraum-vs-gewerbe` | AGB im Mietrecht: Wohnraum- und Gewerberaummiete. Skill differenziert die AGB-rechtliche Behandlung typischer Mietklauseln Schoenheitsreparaturen Quotenklauseln Endrenovierung Mieterhoehungsvereinbarungen Versetzungsklauseln Anpassungskl... |
| `agb-in-kapitalanlagen-effektenhandel` | AGB im Kapitalanlage- und Effektenhandel. Skill klaert die AGB-rechtliche Prüfung der Allgemeinen Geschäftsbedingungen für Wertpapiergeschaefte (Sonderbedingungen) der Spar- und Tagesgeldbedingungen sowie der Anforderungen aus MiFID II... |
| `agb-indexierung` | Klausel-Fachmodul für Indexierung: prüft, redlined und entwirft die Klausel mit Risikoampel, Verbraucher-/B2B-Unterscheidung und praxistauglicher Ersatzfassung. |
| `agb-kardinalpflichten-haftungsbegrenzung` | Klausel-Fachmodul für Kardinalpflichten: prüft, redlined und entwirft die Klausel mit Risikoampel, Verbraucher-/B2B-Unterscheidung und praxistauglicher Ersatzfassung. |
| `agb-konzernklausel-datenaustausch-haftung` | Klausel-Fachmodul für Konzernklausel: prüft, redlined und entwirft die Klausel mit Risikoampel, Verbraucher-/B2B-Unterscheidung und praxistauglicher Ersatzfassung. |
| `agb-lagerbedingungen-haftung-pflichten` | Branchen-Fachmodul für Lagerbedingungen: prüft typische AGB-Risiken des Vertragstyps und erzeugt Klauselarchitektur, Red Flags und bessere Bedingungen. |
| `agb-leasingvertrag-fortwirkung-schiedsklausel` | AGB im Leasingvertrag. Skill klaert AGB-Klauseln in Operating- und Finance-Leasing Verteilung der Sach- und Rechtsgefahr Maengelhaftungs-Drittinanspruchnahme (Drittabtretungsmodell BGH) Restwertabrechnung Andienung Mehrkilometerregelung.... |
| `agb-mindestabnahme-bezugspflichten` | Klausel-Fachmodul für Mindestabnahme: prüft, redlined und entwirft die Klausel mit Risikoampel, Verbraucher-/B2B-Unterscheidung und praxistauglicher Ersatzfassung. |
| `agb-mitwirkungspflichten-leistungsstoerung` | Klausel-Fachmodul für Mitwirkungspflichten: prüft, redlined und entwirft die Klausel mit Risikoampel, Verbraucher-/B2B-Unterscheidung und praxistauglicher Ersatzfassung. |
| `agb-preisanpassung-energie-stromgvv-gasgvv` | AGB-Preisanpassung Energieversorgung StromGVV GasGVV. Skill klaert die rechtlichen Anforderungen an Preisanpassungsklauseln in Energielieferungsvertraegen Grundversorgung (StromGVV GasGVV) und Sonderkundenvertraege. Behandelt EuGH-Linie... |
| `agb-pruefung-kaltstart` | Einstiegs- und Prüfungslinie für AGB Prüfung Kaltstart: sortiert Ziel, Rolle, Dokumente, Normenstand, AGB-Risiko und nächsten Output schnell und anfängertauglich. |
| `agb-rechtswahl` | Klausel-Fachmodul für Rechtswahl: prüft, redlined und entwirft die Klausel mit Risikoampel, Verbraucher-/B2B-Unterscheidung und praxistauglicher Ersatzfassung. |
| `agb-rechtswahl-schweizer-recht-rom-i` | Rechtswahl Schweizer Recht in AGB als Versuch dem deutschen AGB-Recht zu entkommen. Skill klaert Rom-I-VO Art. 3 freie Rechtswahl Art. 6 zwingender Verbraucherschutz Art. 9 Eingriffsnormen sowie die Prüfung ob §§ 305-310 BGB internation... |
| `agb-referenznennung-werbung-zustimmung` | Klausel-Fachmodul für Referenznennung: prüft, redlined und entwirft die Klausel mit Risikoampel, Verbraucher-/B2B-Unterscheidung und praxistauglicher Ersatzfassung. |
| `agb-reisebedingungen-pauschalreise` | Branchen-Fachmodul für Reisebedingungen: prüft typische AGB-Risiken des Vertragstyps und erzeugt Klauselarchitektur, Red Flags und bessere Bedingungen. |
| `agb-risikoklassifizierung-ampel` | Einstiegs- und Prüfungslinie für AGB Risikoklassifizierung Ampel: sortiert Ziel, Rolle, Dokumente, Normenstand, AGB-Risiko und nächsten Output schnell und anfängertauglich. |
| `agb-ruegeobliegenheit-377hgb` | Klausel-Fachmodul für Rügeobliegenheit: prüft, redlined und entwirft die Klausel mit Risikoampel, Verbraucher-/B2B-Unterscheidung und praxistauglicher Ersatzfassung. |
| `agb-schiedsgericht-verbraucher-b2b` | Klausel-Fachmodul für Schiedsgericht: prüft, redlined und entwirft die Klausel mit Risikoampel, Verbraucher-/B2B-Unterscheidung und praxistauglicher Ersatzfassung. |
| `agb-schiedsklausel-opt-out-deutsches-recht` | Schiedsklausel als Opt-out aus dem deutschen AGB-Recht: BGH-Linie zur Wirksamkeit von Schiedsvereinbarungen in AGB. Prüfraster: § 1031 ZPO Schriftform New York Convention 1958 Bruessel-Ia-VO 1215/2012 Art. 25 sowie ordre-public-Vorbehal... |
| `agb-sicherungsrechte-abtretung-pfand` | Klausel-Fachmodul für Sicherungsrechte: prüft, redlined und entwirft die Klausel mit Risikoampel, Verbraucher-/B2B-Unterscheidung und praxistauglicher Ersatzfassung. |
| `agb-subunternehmer-einsatz-haftung` | Klausel-Fachmodul für Subunternehmer: prüft, redlined und entwirft die Klausel mit Risikoampel, Verbraucher-/B2B-Unterscheidung und praxistauglicher Ersatzfassung. |
| `agb-transparenzgebot-307-abs-1-satz-2` | AGB Transparenzgebot § 307 Abs. 1 Satz 2 BGB. Skill arbeitet die BGH-Linie zum Transparenzgebot aus Bestimmtheitserfordernis Verstaendlichkeit Vorhersehbarkeit der Klauselwirkung und Schutz vor verschachtelten Verweisen. Behandelt typisc... |
| `agb-und-242-bgb-eingriffsnorm` | Diskussion um § 242 BGB als Eingriffsnorm im Sinne Art. 9 Rom-I-VO. Skill problematisiert die in der Literatur vereinzelt vertretene These das gesamte AGB-Recht greife international durch weil § 242 BGB ein verbindlicher Grundsatz von Tr... |
| `agb-und-cookie-einwilligung-dsgvo` | AGB und Cookie-Einwilligung nach DSGVO und TTDSG / TDDDG. Skill klaert die Wechselwirkung von AGB-rechtlichen Klauseln und datenschutzrechtlicher Einwilligung Anforderungen an die Einwilligung Differenzierung notwendige Cookies und optio... |
| `agb-und-ipr-art-6-rom-i-verbraucher` | AGB und IPR Art. 6 Rom-I-VO Verbraucherschutz. Skill vertieft die IPR-rechtliche Prüfung der AGB bei Verbrauchervertraegen mit internationalem Bezug. Klaert die Voraussetzungen der ausgerichteten Taetigkeit nach Art. 6 Abs. 1 Buchst. b... |
| `agb-vereinsbedingungen-mitgliedschaft` | Branchen-Fachmodul für Vereinsbedingungen: prüft typische AGB-Risiken des Vertragstyps und erzeugt Klauselarchitektur, Red Flags und bessere Bedingungen. |
| `agb-verjaehrungsverkuerzung-maengel` | Klausel-Fachmodul für Verjährungsverkürzung: prüft, redlined und entwirft die Klausel mit Risikoampel, Verbraucher-/B2B-Unterscheidung und praxistauglicher Ersatzfassung. |
| `agb-versionierung-aenderungshistorie` | Einstiegs- und Prüfungslinie für AGB Versionierung Änderungshistorie: sortiert Ziel, Rolle, Dokumente, Normenstand, AGB-Risiko und nächsten Output schnell und anfängertauglich. |
| `agb-vertragsstrafe-309-nr-6` | AGB-Vertragsstrafe nach § 309 Nr. 6 BGB. Skill vertieft die AGB-rechtliche Behandlung von Vertragsstrafen im B2C und B2B. Klaert Hoechstgrenzen Abgrenzung zu pauschalierten Schadensersatz Sondervorschriften im Arbeitsvertrag (§ 310 Abs.... |
| `agb-werkleistung-vob-b-aktuell` | AGB im Werkvertragsrecht VOB-B in aktueller Fassung. Skill behandelt die VOB-B-Klauseln zur Maengelhaftung Abnahme Sicherheitsleistung und Änderungsanordnung Klausel-für-Klausel-Wirksamkeitspruefung gegen § 307 BGB. BGH-Aktuelles zu §§... |
| `agentur-marketing-agb` | Branchen-Fachmodul für Agentur Marketing AGB: prüft typische AGB-Risiken des Vertragstyps und erzeugt Klauselarchitektur, Red Flags und bessere Bedingungen. |
| `annahmefrist-leistungsfrist-308` | Norm- und Dogmatik-Skill für Annahmefrist Leistungsfrist 308: prüft die AGB-Kontrolle quellenstreng entlang BGB §§ 305 bis 310 und ordnet Rechtsfolge, Risiko und bessere Fassung. |
| `app-agb` | Branchen-Fachmodul für App AGB: prüft typische AGB-Risiken des Vertragstyps und erzeugt Klauselarchitektur, Red Flags und bessere Bedingungen. |
| `arbeitsrecht-agb-310-abs4` | Norm- und Dogmatik-Skill für Arbeitsrecht AGB 310 Abs. 4: prüft die AGB-Kontrolle quellenstreng entlang BGB §§ 305 bis 310 und ordnet Rechtsfolge, Risiko und bessere Fassung. |
| `arbeitsrecht-agb-architekten-ingenieur` | Norm- und Dogmatik-Skill für Arbeitsrecht AGB 310 Abs. 4: prüft die AGB-Kontrolle quellenstreng entlang BGB §§ 305 bis 310 und ordnet Rechtsfolge, Risiko und bessere Fassung im AGB-Recht. |
| `architekten-ingenieur-agb` | Branchen-Fachmodul für Architekten Ingenieur AGB: prüft typische AGB-Risiken des Vertragstyps und erzeugt Klauselarchitektur, Red Flags und bessere Bedingungen. |
| `auditrechte` | Klausel-Fachmodul für Auditrechte: prüft, redlined und entwirft die Klausel mit Risikoampel, Verbraucher-/B2B-Unterscheidung und praxistauglicher Ersatzfassung im AGB-Recht. |
| `aufrechnung-zurueckbehaltung-309` | Norm- und Dogmatik-Skill für Aufrechnung Zurückbehaltung 309: prüft die AGB-Kontrolle quellenstreng entlang BGB §§ 305 bis 310 und ordnet Rechtsfolge, Risiko und bessere Fassung. |
| `automatische-verlaengerung` | Klausel-Fachmodul für Automatische Verlängerung: prüft, redlined und entwirft die Klausel mit Risikoampel, Verbraucher-/B2B-Unterscheidung und praxistauglicher Ersatzfassung. |
| `avv-agb-b2b-harte-b2c-b2b2c-backup` | Branchen-Fachmodul für AVV und AGB Schnittstelle: prüft typische AGB-Risiken des Vertragstyps und erzeugt Klauselarchitektur, Red Flags und bessere Bedingungen im AGB-Recht. |
| `avv-und-agb-schnittstelle` | Branchen-Fachmodul für AVV und AGB Schnittstelle: prüft typische AGB-Risiken des Vertragstyps und erzeugt Klauselarchitektur, Red Flags und bessere Bedingungen. |
| `b2b-harte-fassung` | Output- und Streit-Skill für B2B Harte Fassung: macht aus der AGB-Prüfung verwertbare Redlines, Entwürfe, Playbooks, Abmahnreaktionen oder Entscheidungsunterlagen. |
| `b2c-b2b-b2b2c-rollencheck` | Einstiegs- und Prüfungslinie für B2C B2B B2B2C Rollencheck: sortiert Ziel, Rolle, Dokumente, Normenstand, AGB-Risiko und nächsten Output schnell und anfängertauglich. |
| `backup-datenverlust` | Klausel-Fachmodul für Backup Datenverlust: prüft, redlined und entwirft die Klausel mit Risikoampel, Verbraucher-/B2B-Unterscheidung und praxistauglicher Ersatzfassung. |
| `bank-agb` | Branchen-Fachmodul für Bank AGB: prüft typische AGB-Risiken des Vertragstyps und erzeugt Klauselarchitektur, Red Flags und bessere Bedingungen. |
| `bankvertrag-sparkassen-bauvertrag-vob` | AGB-Kontrolle im Bankvertrag. Skill behandelt die Banken-AGB Sparkassen-AGB und Allgemeinen Geschäftsbedingungen der Volks- und Raiffeisenbanken Klauseln zu Entgelten Änderungen einseitige Vertragsanpassung BGH-Linie zu Gebührenklausel... |
| `battle-forms-bau-vob-beweislast-zugang` | Norm- und Dogmatik-Skill für Battle of Forms AGB Kollision: prüft die AGB-Kontrolle quellenstreng entlang BGB §§ 305 bis 310 und ordnet Rechtsfolge, Risiko und bessere Fassung im AGB-Recht. |
| `battle-of-forms-agb-kollision` | Norm- und Dogmatik-Skill für Battle of Forms AGB Kollision: prüft die AGB-Kontrolle quellenstreng entlang BGB §§ 305 bis 310 und ordnet Rechtsfolge, Risiko und bessere Fassung. |
| `bau-vob-agb` | Branchen-Fachmodul für Bau VOB/B AGB: prüft typische AGB-Risiken des Vertragstyps und erzeugt Klauselarchitektur, Red Flags und bessere Bedingungen. |
| `begriff-vorformuliert-digitalen-produkten-iso` | Norm- und Dogmatik-Skill für AGB Begriff Vorformuliert 305: prüft die AGB-Kontrolle quellenstreng entlang BGB §§ 305 bis 310 und ordnet Rechtsfolge, Risiko und bessere Fassung im AGB-Recht. |
| `beweislast-und-zugang-309` | Norm- und Dogmatik-Skill für Beweislast und Zugang 309: prüft die AGB-Kontrolle quellenstreng entlang BGB §§ 305 bis 310 und ordnet Rechtsfolge, Risiko und bessere Fassung. |
| `bewertung-rezensionen` | Klausel-Fachmodul für Bewertung Rezensionen: prüft, redlined und entwirft die Klausel mit Risikoampel, Verbraucher-/B2B-Unterscheidung und praxistauglicher Ersatzfassung. |
| `bildungs-kurs-agb` | Branchen-Fachmodul für Bildungs Kurs AGB: prüft typische AGB-Risiken des Vertragstyps und erzeugt Klauselarchitektur, Red Flags und bessere Bedingungen. |
| `blue-pencil-board-agb-bonitaetspruefung-bonus` | Blue-Pencil-Test und geltungserhaltende Reduktion in AGB-Vertraegen. Skill arbeitet die Methodik aus wann eine teilbare Klausel durch Streichung in einen wirksamen Restbestand zerfaellt und wann dies ausgeschlossen ist. Behandelt die BGH... |
| `blue-pencil-und-geltungserhaltende-reduktion` | Blue-Pencil-Test und geltungserhaltende Reduktion in AGB-Vertraegen. Skill arbeitet die Methodik aus wann eine teilbare Klausel durch Streichung in einen wirksamen Restbestand zerfaellt und wann dies ausgeschlossen ist. Behandelt die BGH... |
| `board-brief-agb` | Output- und Streit-Skill für Board Brief AGB: macht aus der AGB-Prüfung verwertbare Redlines, Entwürfe, Playbooks, Abmahnreaktionen oder Entscheidungsunterlagen. |
| `bonitaetspruefung` | Klausel-Fachmodul für Bonitätsprüfung: prüft, redlined und entwirft die Klausel mit Risikoampel, Verbraucher-/B2B-Unterscheidung und praxistauglicher Ersatzfassung im AGB-Recht. |
| `bonus-rabatt` | Klausel-Fachmodul für Bonus Rabatt: prüft, redlined und entwirft die Klausel mit Risikoampel, Verbraucher-/B2B-Unterscheidung und praxistauglicher Ersatzfassung. |
| `business-summary-agb` | Output- und Streit-Skill für Business Summary AGB: macht aus der AGB-Prüfung verwertbare Redlines, Entwürfe, Playbooks, Abmahnreaktionen oder Entscheidungsunterlagen. |
| `change-request` | Klausel-Fachmodul für Change Reqüst: prüft, redlined und entwirft die Klausel mit Risikoampel, Verbraucher-/B2B-Unterscheidung und praxistauglicher Ersatzfassung. |
| `change-request-clickwrap-beweisakte-cloud` | Klausel-Fachmodul für Change Reqüst: prüft, redlined und entwirft die Klausel mit Risikoampel, Verbraucher-/B2B-Unterscheidung und praxistauglicher Ersatzfassung im AGB-Recht. |
| `clickwrap-beweisakte` | Output- und Streit-Skill für Clickwrap Beweisakte: macht aus der AGB-Prüfung verwertbare Redlines, Entwürfe, Playbooks, Abmahnreaktionen oder Entscheidungsunterlagen. |
| `cloud-hosting-agb` | Branchen-Fachmodul für Cloud Hosting AGB: prüft typische AGB-Risiken des Vertragstyps und erzeugt Klauselarchitektur, Red Flags und bessere Bedingungen. |
| `compliance-sanktionen` | Klausel-Fachmodul für Compliance Sanktionen: prüft, redlined und entwirft die Klausel mit Risikoampel, Verbraucher-/B2B-Unterscheidung und praxistauglicher Ersatzfassung. |
| `consulting-agb` | Branchen-Fachmodul für Consulting AGB: prüft typische AGB-Risiken des Vertragstyps und erzeugt Klauselarchitektur, Red Flags und bessere Bedingungen. |
| `crowdfunding-agb` | Branchen-Fachmodul für Crowdfunding AGB: prüft typische AGB-Risiken des Vertragstyps und erzeugt Klauselarchitektur, Red Flags und bessere Bedingungen. |
| `crypto-exchange-agb` | Branchen-Fachmodul für Crypto Exchange AGB: prüft typische AGB-Risiken des Vertragstyps und erzeugt Klauselarchitektur, Red Flags und bessere Bedingungen. |
| `crypto-exchange-darlehen-finanzierung` | Branchen-Fachmodul für Crypto Exchange AGB: prüft typische AGB-Risiken des Vertragstyps und erzeugt Klauselarchitektur, Red Flags und bessere Bedingungen im AGB-Recht. |
| `darlehen-finanzierung-agb` | Branchen-Fachmodul für Darlehen Finanzierung AGB: prüft typische AGB-Risiken des Vertragstyps und erzeugt Klauselarchitektur, Red Flags und bessere Bedingungen. |
| `datenexport-portabilitaet` | Klausel-Fachmodul für Datenexport Portabilität: prüft, redlined und entwirft die Klausel mit Risikoampel, Verbraucher-/B2B-Unterscheidung und praxistauglicher Ersatzfassung. |
| `datenschutzverweise-agb` | Klausel-Fachmodul für Datenschutzverweise AGB: prüft, redlined und entwirft die Klausel mit Risikoampel, Verbraucher-/B2B-Unterscheidung und praxistauglicher Ersatzfassung. |
| `definitionen-glossar-agb` | Output- und Streit-Skill für Definitionen Glossar AGB: macht aus der AGB-Prüfung verwertbare Redlines, Entwürfe, Playbooks, Abmahnreaktionen oder Entscheidungsunterlagen. |
| `deutsch-englisch-agb` | Output- und Streit-Skill für Deutsch Englisch AGB: macht aus der AGB-Prüfung verwertbare Redlines, Entwürfe, Playbooks, Abmahnreaktionen oder Entscheidungsunterlagen. |
| `deutsch-englisch-digitale-inhalte-handbuch` | Output- und Streit-Skill für Deutsch Englisch AGB: macht aus der AGB-Prüfung verwertbare Redlines, Entwürfe, Playbooks, Abmahnreaktionen oder Entscheidungsunterlagen im AGB-Recht. |
| `digitale-inhalte-services` | Branchen-Fachmodul für Digitale Inhalte Services: prüft typische AGB-Risiken des Vertragstyps und erzeugt Klauselarchitektur, Red Flags und bessere Bedingungen. |
| `dokumentation-handbuch` | Klausel-Fachmodul für Dokumentation Handbuch: prüft, redlined und entwirft die Klausel mit Risikoampel, Verbraucher-/B2B-Unterscheidung und praxistauglicher Ersatzfassung. |
| `dokumentenfamilie-rangfolge` | Einstiegs- und Prüfungslinie für Dokumentenfamilie Rangfolge: sortiert Ziel, Rolle, Dokumente, Normenstand, AGB-Risiko und nächsten Output schnell und anfängertauglich. |
| `ecommerce-shop-agb` | Branchen-Fachmodul für Ecommerce Shop AGB: prüft typische AGB-Risiken des Vertragstyps und erzeugt Klauselarchitektur, Red Flags und bessere Bedingungen. |
| `eigentumsvorbehalt-einbeziehung-hinweis` | Klausel-Fachmodul für Eigentumsvorbehalt: prüft, redlined und entwirft die Klausel mit Risikoampel, Verbraucher-/B2B-Unterscheidung und praxistauglicher Ersatzfassung im AGB-Recht. |
| `einbeziehung-hinweis-kenntnisnahme-305` | Norm- und Dogmatik-Skill für Einbeziehung Hinweis Kenntnisnahme 305: prüft die AGB-Kontrolle quellenstreng entlang BGB §§ 305 bis 310 und ordnet Rechtsfolge, Risiko und bessere Fassung. |
| `einbeziehung-online-clickwrap-browsewrap` | Norm- und Dogmatik-Skill für Einbeziehung Online Clickwrap Browsewrap: prüft die AGB-Kontrolle quellenstreng entlang BGB §§ 305 bis 310 und ordnet Rechtsfolge, Risiko und bessere Fassung. |
| `einkaufsbedingungen-b2b` | Branchen-Fachmodul für Einkaufsbedingungen B2B: prüft typische AGB-Risiken des Vertragstyps und erzeugt Klauselarchitektur, Red Flags und bessere Bedingungen. |
| `einstweilige-verfuegung-agb` | Output- und Streit-Skill für Einstweilige Verfügung AGB: macht aus der AGB-Prüfung verwertbare Redlines, Entwürfe, Playbooks, Abmahnreaktionen oder Entscheidungsunterlagen. |
| `energieversorgung-agb` | Branchen-Fachmodul für Energieversorgung AGB: prüft typische AGB-Risiken des Vertragstyps und erzeugt Klauselarchitektur, Red Flags und bessere Bedingungen. |
| `energieversorgung-agb-entgelt-nebenkosten` | Branchen-Fachmodul für Energieversorgung AGB: prüft typische AGB-Risiken des Vertragstyps und erzeugt Klauselarchitektur, Red Flags und bessere Bedingungen im AGB-Recht. |
| `entgelt-nebenkosten-service-fees` | Klausel-Fachmodul für Entgelt Nebenkosten Service Fees: prüft, redlined und entwirft die Klausel mit Risikoampel, Verbraucher-/B2B-Unterscheidung und praxistauglicher Ersatzfassung. |
| `ergaenzende-vertragsauslegung-bei-agb-luecken` | Ergaenzende Vertragsauslegung bei AGB-Luecken. Skill klaert die BGH-Linie zur Lueckenfuellung wenn AGB-Klauseln unwirksam sind. Behandelt das Verhältnis von § 306 Abs. 2 BGB Gesetzesrecht und ergaenzender Vertragsauslegung sowie die Gre... |
| `erganzende-vertragsauslegung-agb-luecke` | Norm- und Dogmatik-Skill für Erganzende Vertragsauslegung AGB Lücke: prüft die AGB-Kontrolle quellenstreng entlang BGB §§ 305 bis 310 und ordnet Rechtsfolge, Risiko und bessere Fassung. |
| `exklusivitaet` | Klausel-Fachmodul für Exklusivität: prüft, redlined und entwirft die Klausel mit Risikoampel, Verbraucher-/B2B-Unterscheidung und praxistauglicher Ersatzfassung im AGB-Recht. |
| `factoring-agb` | Branchen-Fachmodul für Factoring AGB: prüft typische AGB-Risiken des Vertragstyps und erzeugt Klauselarchitektur, Red Flags und bessere Bedingungen. |
| `feedback-rechte` | Klausel-Fachmodul für Feedback Rechte: prüft, redlined und entwirft die Klausel mit Risikoampel, Verbraucher-/B2B-Unterscheidung und praxistauglicher Ersatzfassung. |
| `fiktive-erklaerung-zustimmung-308` | Norm- und Dogmatik-Skill für Fiktive Erklärung Zustimmung 308: prüft die AGB-Kontrolle quellenstreng entlang BGB §§ 305 bis 310 und ordnet Rechtsfolge, Risiko und bessere Fassung. |
| `fitnessstudio-agb` | Branchen-Fachmodul für Fitnessstudio AGB: prüft typische AGB-Risiken des Vertragstyps und erzeugt Klauselarchitektur, Red Flags und bessere Bedingungen. |
| `fitnessstudio-agb-force-majeure-formvorgaben` | Branchen-Fachmodul für Fitnessstudio AGB: prüft typische AGB-Risiken des Vertragstyps und erzeugt Klauselarchitektur, Red Flags und bessere Bedingungen im AGB-Recht. |
| `force-majeure-hoehere-gewalt` | Klausel-Fachmodul für Force Majeure Höhere Gewalt: prüft, redlined und entwirft die Klausel mit Risikoampel, Verbraucher-/B2B-Unterscheidung und praxistauglicher Ersatzfassung. |
| `formulararbeitsvertrag-haendlervertrag-agb` | Branchen-Fachmodul für Formulararbeitsvertrag: prüft typische AGB-Risiken des Vertragstyps und erzeugt Klauselarchitektur, Red Flags und bessere Bedingungen im AGB-Recht. |
| `formvorgaben-anzeigen-erklaerungen-309` | Norm- und Dogmatik-Skill für Formvorgaben Anzeigen Erklärungen 309: prüft die AGB-Kontrolle quellenstreng entlang BGB §§ 305 bis 310 und ordnet Rechtsfolge, Risiko und bessere Fassung. |
| `forschung-entwicklung-agb` | Branchen-Fachmodul für Forschung Entwicklung AGB: prüft typische AGB-Risiken des Vertragstyps und erzeugt Klauselarchitektur, Red Flags und bessere Bedingungen. |
| `fragebogen-agb-automation` | Output- und Streit-Skill für Fragebogen AGB Automation: macht aus der AGB-Prüfung verwertbare Redlines, Entwürfe, Playbooks, Abmahnreaktionen oder Entscheidungsunterlagen. |
| `franchise-agb` | Branchen-Fachmodul für Franchise AGB: prüft typische AGB-Risiken des Vertragstyps und erzeugt Klauselarchitektur, Red Flags und bessere Bedingungen. |
| `franchise-agb-gaming-garantie-beschaffenheit` | Branchen-Fachmodul für Franchise AGB: prüft typische AGB-Risiken des Vertragstyps und erzeugt Klauselarchitektur, Red Flags und bessere Bedingungen im AGB-Recht. |
| `gaming-agb` | Branchen-Fachmodul für Gaming AGB: prüft typische AGB-Risiken des Vertragstyps und erzeugt Klauselarchitektur, Red Flags und bessere Bedingungen. |
| `garantie-beschaffenheit` | Klausel-Fachmodul für Garantie Beschaffenheit: prüft, redlined und entwirft die Klausel mit Risikoampel, Verbraucher-/B2B-Unterscheidung und praxistauglicher Ersatzfassung. |
| `gerichtsstand` | Klausel-Fachmodul für Gerichtsstand: prüft, redlined und entwirft die Klausel mit Risikoampel, Verbraucher-/B2B-Unterscheidung und praxistauglicher Ersatzfassung im AGB-Recht. |
| `gesellschaftsrechtliche-satzungen-agb` | Norm- und Dogmatik-Skill für Gesellschaftsrechtliche Satzungen AGB Abgrenzung: prüft die AGB-Kontrolle quellenstreng entlang BGB §§ 305 bis 310 und ordnet Rechtsfolge, Risiko und bessere Fassung. |
| `gesellschaftsrechtliche-satzungen-agb-abgrenzung` | Norm- und Dogmatik-Skill für Gesellschaftsrechtliche Satzungen AGB Abgrenzung: prüft die AGB-Kontrolle quellenstreng entlang BGB §§ 305 bis 310 und ordnet Rechtsfolge, Risiko und bessere Fassung im AGB-Recht. |
| `gesetzliches-leitbild-abweichung-307` | Norm- und Dogmatik-Skill für Gesetzliches Leitbild Abweichung 307: prüft die AGB-Kontrolle quellenstreng entlang BGB §§ 305 bis 310 und ordnet Rechtsfolge, Risiko und bessere Fassung. |
| `gesetzliches-leitbild-gewahrleistung` | Norm- und Dogmatik-Skill für Gesetzliches Leitbild Abweichung 307: prüft die AGB-Kontrolle quellenstreng entlang BGB §§ 305 bis 310 und ordnet Rechtsfolge, Risiko und bessere Fassung im AGB-Recht. |
| `gewahrleistung-ausschluss` | Klausel-Fachmodul für Gewährleistung Ausschluss: prüft, redlined und entwirft die Klausel mit Risikoampel, Verbraucher-/B2B-Unterscheidung und praxistauglicher Ersatzfassung. |
| `gewerbemiete-agb` | Branchen-Fachmodul für Gewerbemiete AGB: prüft typische AGB-Risiken des Vertragstyps und erzeugt Klauselarchitektur, Red Flags und bessere Bedingungen. |
| `haendlervertrag-agb` | Branchen-Fachmodul für Haendlervertrag AGB: prüft typische AGB-Risiken des Vertragstyps und erzeugt Klauselarchitektur, Red Flags und bessere Bedingungen. |
| `haftung-grobe-fahrlaessigkeit-vorsatz` | Klausel-Fachmodul für Haftung Grobe Fahrlaessigkeit Vorsatz: prüft, redlined und entwirft die Klausel mit Risikoampel, Verbraucher-/B2B-Unterscheidung und praxistauglicher Ersatzfassung. |
| `haftung-indirekte-schaeden` | Klausel-Fachmodul für Haftung Indirekte Schaeden: prüft, redlined und entwirft die Klausel mit Risikoampel, Verbraucher-/B2B-Unterscheidung und praxistauglicher Ersatzfassung. |
| `haftung-leben-koerper-gesundheit-309` | Norm- und Dogmatik-Skill für Haftung Leben Koerper Gesundheit 309: prüft die AGB-Kontrolle quellenstreng entlang BGB §§ 305 bis 310 und ordnet Rechtsfolge, Risiko und bessere Fassung. |
| `haftung-sanktionen-grobe-fahrlaessigkeit` | Klausel-Fachmodul für Compliance Sanktionen: prüft, redlined und entwirft die Klausel mit Risikoampel, Verbraucher-/B2B-Unterscheidung und praxistauglicher Ersatzfassung im AGB-Recht. |
| `haftungscap-summe` | Klausel-Fachmodul für Haftungscap Summe: prüft, redlined und entwirft die Klausel mit Risikoampel, Verbraucher-/B2B-Unterscheidung und praxistauglicher Ersatzfassung. |
| `handelsvertreter-agb` | Branchen-Fachmodul für Handelsvertreter AGB: prüft typische AGB-Risiken des Vertragstyps und erzeugt Klauselarchitektur, Red Flags und bessere Bedingungen. |
| `indexierung` | Klausel-Fachmodul für Indexierung: prüft, redlined und entwirft die Klausel mit Risikoampel, Verbraucher-/B2B-Unterscheidung und praxistauglicher Ersatzfassung im AGB-Recht. |
| `individualabrede-305b` | Norm- und Dogmatik-Skill für Individualabrede 305b: prüft die AGB-Kontrolle quellenstreng entlang BGB §§ 305 bis 310 und ordnet Rechtsfolge, Risiko und bessere Fassung. |
| `individualabrede-305b-individualklage` | Norm- und Dogmatik-Skill für Individualabrede 305b: prüft die AGB-Kontrolle quellenstreng entlang BGB §§ 305 bis 310 und ordnet Rechtsfolge, Risiko und bessere Fassung im AGB-Recht. |
| `individualklage-verteidigung` | Output- und Streit-Skill für Individualklage Verteidigung: macht aus der AGB-Prüfung verwertbare Redlines, Entwürfe, Playbooks, Abmahnreaktionen oder Entscheidungsunterlagen. |
| `inhaltskontrolle-307-generalklausel` | Norm- und Dogmatik-Skill für Inhaltskontrolle 307 Generalklausel: prüft die AGB-Kontrolle quellenstreng entlang BGB §§ 305 bis 310 und ordnet Rechtsfolge, Risiko und bessere Fassung. |
| `insolvenzverkauf-agb` | Branchen-Fachmodul für Insolvenzverkauf AGB: prüft typische AGB-Risiken des Vertragstyps und erzeugt Klauselarchitektur, Red Flags und bessere Bedingungen. |
| `ip-nutzungsrechte` | Klausel-Fachmodul für IP Nutzungsrechte: prüft, redlined und entwirft die Klausel mit Risikoampel, Verbraucher-/B2B-Unterscheidung und praxistauglicher Ersatzfassung. |
| `ipr-art-versionierung-aenderungshistorie` | AGB und IPR Art. 6 Rom-I-VO Verbraucherschutz. Skill vertieft die IPR-rechtliche Prüfung der AGB bei Verbrauchervertraegen mit internationalem Bezug. Klaert die Voraussetzungen der ausgerichteten Taetigkeit nach Art. 6 Abs. 1 Buchst. b... |
| `kaltstart-triage` | Einstiegs- und Prüfungslinie für Allgemein: sortiert Ziel, Rolle, Dokumente, Normenstand, AGB-Risiko und nächsten Output schnell und anfängertauglich. |
| `kardinalpflichten` | Klausel-Fachmodul für Kardinalpflichten: prüft, redlined und entwirft die Klausel mit Risikoampel, Verbraucher-/B2B-Unterscheidung und praxistauglicher Ersatzfassung im AGB-Recht. |
| `ki-output-nutzung` | Klausel-Fachmodul für KI Output Nutzung: prüft, redlined und entwirft die Klausel mit Risikoampel, Verbraucher-/B2B-Unterscheidung und praxistauglicher Ersatzfassung. |
| `ki-service-agb` | Branchen-Fachmodul für KI Service AGB: prüft typische AGB-Risiken des Vertragstyps und erzeugt Klauselarchitektur, Red Flags und bessere Bedingungen. |
| `ki-service-kollisionsrecht-ipr-konto` | Branchen-Fachmodul für KI Service AGB: prüft typische AGB-Risiken des Vertragstyps und erzeugt Klauselarchitektur, Red Flags und bessere Bedingungen im AGB-Recht. |
| `klausel-checkliste-self-service` | Output- und Streit-Skill für Klausel Checkliste Self Service: macht aus der AGB-Prüfung verwertbare Redlines, Entwürfe, Playbooks, Abmahnreaktionen oder Entscheidungsunterlagen. |
| `klausel-entwerfen-aggressiv` | Output- und Streit-Skill für Klausel Entwerfen Aggressiv: macht aus der AGB-Prüfung verwertbare Redlines, Entwürfe, Playbooks, Abmahnreaktionen oder Entscheidungsunterlagen. |
| `klausel-entwerfen-balanced` | Output- und Streit-Skill für Klausel Entwerfen Balanced: macht aus der AGB-Prüfung verwertbare Redlines, Entwürfe, Playbooks, Abmahnreaktionen oder Entscheidungsunterlagen. |
| `klausel-entwerfen-low-risk` | Output- und Streit-Skill für Klausel Entwerfen Low Risk: macht aus der AGB-Prüfung verwertbare Redlines, Entwürfe, Playbooks, Abmahnreaktionen oder Entscheidungsunterlagen. |
| `klausel-entwerfen-low-risk-klauselbibliothek` | Output- und Streit-Skill für Klausel Entwerfen Balanced: macht aus der AGB-Prüfung verwertbare Redlines, Entwürfe, Playbooks, Abmahnreaktionen oder Entscheidungsunterlagen im AGB-Recht. |
| `klauselbibliothek-aufbau` | Einstiegs- und Prüfungslinie für Klauselbibliothek Aufbau: sortiert Ziel, Rolle, Dokumente, Normenstand, AGB-Risiko und nächsten Output schnell und anfängertauglich. |
| `klauselinventar-und-scope` | Einstiegs- und Prüfungslinie für Klauselinventar und Scope: sortiert Ziel, Rolle, Dokumente, Normenstand, AGB-Risiko und nächsten Output schnell und anfängertauglich. |
| `klauselvarianten-vergleich` | Output- und Streit-Skill für Klauselvarianten Vergleich: macht aus der AGB-Prüfung verwertbare Redlines, Entwürfe, Playbooks, Abmahnreaktionen oder Entscheidungsunterlagen. |
| `klauselverbote-308-systematik` | Norm- und Dogmatik-Skill für Klauselverbote 308 Systematik: prüft die AGB-Kontrolle quellenstreng entlang BGB §§ 305 bis 310 und ordnet Rechtsfolge, Risiko und bessere Fassung. |
| `klauselverbote-309-systematik` | Norm- und Dogmatik-Skill für Klauselverbote 309 Systematik: prüft die AGB-Kontrolle quellenstreng entlang BGB §§ 305 bis 310 und ordnet Rechtsfolge, Risiko und bessere Fassung. |
| `klauselverbote-systematik` | Norm- und Dogmatik-Skill für Klauselverbote 308 Systematik: prüft die AGB-Kontrolle quellenstreng entlang BGB §§ 305 bis 310 und ordnet Rechtsfolge, Risiko und bessere Fassung im AGB-Recht. |
| `kollisionsrecht-ipr-agb` | Einstiegs- und Prüfungslinie für Kollisionsrecht IPR AGB: sortiert Ziel, Rolle, Dokumente, Normenstand, AGB-Risiko und nächsten Output schnell und anfängertauglich. |
| `konto-kuendigung-sperre` | Klausel-Fachmodul für Konto Kündigung Sperre: prüft, redlined und entwirft die Klausel mit Risikoampel, Verbraucher-/B2B-Unterscheidung und praxistauglicher Ersatzfassung. |
| `konzernklausel` | Klausel-Fachmodul für Konzernklausel: prüft, redlined und entwirft die Klausel mit Risikoampel, Verbraucher-/B2B-Unterscheidung und praxistauglicher Ersatzfassung im AGB-Recht. |
| `kuendigung-aus-wichtigem-grund` | Klausel-Fachmodul für Kündigung Aus Wichtigem Grund: prüft, redlined und entwirft die Klausel mit Risikoampel, Verbraucher-/B2B-Unterscheidung und praxistauglicher Ersatzfassung. |
| `kuendigung-ordentlich` | Klausel-Fachmodul für Kündigung Ordentlich: prüft, redlined und entwirft die Klausel mit Risikoampel, Verbraucher-/B2B-Unterscheidung und praxistauglicher Ersatzfassung. |
| `kuendigungsfiktion-und-nachfrist-308` | Norm- und Dogmatik-Skill für Kündigungsfiktion und Nachfrist 308: prüft die AGB-Kontrolle quellenstreng entlang BGB §§ 305 bis 310 und ordnet Rechtsfolge, Risiko und bessere Fassung. |
| `kurzfristige-preiserhoehung-309` | Norm- und Dogmatik-Skill für Kurzfristige Preiserhöhung 309: prüft die AGB-Kontrolle quellenstreng entlang BGB §§ 305 bis 310 und ordnet Rechtsfolge, Risiko und bessere Fassung. |
| `kurzfristige-preiserhoehung-lieferfrist` | Norm- und Dogmatik-Skill für Kurzfristige Preiserhöhung 309: prüft die AGB-Kontrolle quellenstreng entlang BGB §§ 305 bis 310 und ordnet Rechtsfolge, Risiko und bessere Fassung im AGB-Recht. |
| `lagerbedingungen-laufzeit-verlaengerung` | Branchen-Fachmodul für Lagerbedingungen: prüft typische AGB-Risiken des Vertragstyps und erzeugt Klauselarchitektur, Red Flags und bessere Bedingungen im AGB-Recht. |
| `laufzeit-verlaengerung-309` | Norm- und Dogmatik-Skill für Laufzeit Verlängerung 309: prüft die AGB-Kontrolle quellenstreng entlang BGB §§ 305 bis 310 und ordnet Rechtsfolge, Risiko und bessere Fassung. |
| `leasing-agb` | Branchen-Fachmodul für Leasing AGB: prüft typische AGB-Risiken des Vertragstyps und erzeugt Klauselarchitektur, Red Flags und bessere Bedingungen. |
| `legal-note-redline-output` | Einstiegs- und Prüfungslinie für Legal Note Redline Output: sortiert Ziel, Rolle, Dokumente, Normenstand, AGB-Risiko und nächsten Output schnell und anfängertauglich. |
| `leistungsaenderung-produktupdate` | Klausel-Fachmodul für Leistungsänderung Produktupdate: prüft, redlined und entwirft die Klausel mit Risikoampel, Verbraucher-/B2B-Unterscheidung und praxistauglicher Ersatzfassung. |
| `lieferfrist-teillieferung` | Klausel-Fachmodul für Lieferfrist Teillieferung: prüft, redlined und entwirft die Klausel mit Risikoampel, Verbraucher-/B2B-Unterscheidung und praxistauglicher Ersatzfassung. |
| `liquidated-damages` | Klausel-Fachmodul für Liquidated Damages: prüft, redlined und entwirft die Klausel mit Risikoampel, Verbraucher-/B2B-Unterscheidung und praxistauglicher Ersatzfassung. |
| `logistik-spedition-agb` | Branchen-Fachmodul für Logistik Spedition AGB: prüft typische AGB-Risiken des Vertragstyps und erzeugt Klauselarchitektur, Red Flags und bessere Bedingungen. |
| `logistik-spedition-maengelrechte` | Branchen-Fachmodul für Logistik Spedition AGB: prüft typische AGB-Risiken des Vertragstyps und erzeugt Klauselarchitektur, Red Flags und bessere Bedingungen im AGB-Recht. |
| `maengelrechte-309` | Norm- und Dogmatik-Skill für Mängelrechte 309: prüft die AGB-Kontrolle quellenstreng entlang BGB §§ 305 bis 310 und ordnet Rechtsfolge, Risiko und bessere Fassung. |
| `mahngebuehren-und-zinsanpassung-agb` | Mahngebuehren und Zinsanpassungsklauseln in AGB. Skill klaert wie hoch Mahngebuehren in AGB sein dürfen Differenzierung erste zweite dritte Mahnung sowie die Wechselwirkung zum Verzugsschaden (§ 280 II 286 BGB). Behandelt automatische Z... |
| `mandanteninterview-agb` | Einstiegs- und Prüfungslinie für Mandanteninterview AGB: sortiert Ziel, Rolle, Dokumente, Normenstand, AGB-Risiko und nächsten Output schnell und anfängertauglich. |
| `mandantenmail-agb` | Output- und Streit-Skill für Mandantenmail AGB: macht aus der AGB-Prüfung verwertbare Redlines, Entwürfe, Playbooks, Abmahnreaktionen oder Entscheidungsunterlagen. |
| `marketplace-agb` | Branchen-Fachmodul für Marketplace AGB: prüft typische AGB-Risiken des Vertragstyps und erzeugt Klauselarchitektur, Red Flags und bessere Bedingungen. |
| `marketplace-agb-mediation-escalation` | Branchen-Fachmodul für Marketplace AGB: prüft typische AGB-Risiken des Vertragstyps und erzeugt Klauselarchitektur, Red Flags und bessere Bedingungen im AGB-Recht. |
| `massenschaden-datenmodell` | Output- und Streit-Skill für Massenschaden Datenmodell: macht aus der AGB-Prüfung verwertbare Redlines, Entwürfe, Playbooks, Abmahnreaktionen oder Entscheidungsunterlagen. |
| `massenschaden-datenmodell-rechtsabteilung` | Output- und Streit-Skill für Massenschaden Datenmodell: macht aus der AGB-Prüfung verwertbare Redlines, Entwürfe, Playbooks, Abmahnreaktionen oder Entscheidungsunterlagen im AGB-Recht. |
| `mediation-escalation` | Klausel-Fachmodul für Mediation Escalation: prüft, redlined und entwirft die Klausel mit Risikoampel, Verbraucher-/B2B-Unterscheidung und praxistauglicher Ersatzfassung. |
| `medizinische-leistungen-agb` | Branchen-Fachmodul für Medizinische Leistungen AGB: prüft typische AGB-Risiken des Vertragstyps und erzeugt Klauselarchitektur, Red Flags und bessere Bedingungen. |
| `mehrdeutigkeit-305c2` | Norm- und Dogmatik-Skill für Mehrdeutigkeit 305c2: prüft die AGB-Kontrolle quellenstreng entlang BGB §§ 305 bis 310 und ordnet Rechtsfolge, Risiko und bessere Fassung. |
| `mehrsprachige-agb-check` | Einstiegs- und Prüfungslinie für Mehrsprachige AGB Check: sortiert Ziel, Rolle, Dokumente, Normenstand, AGB-Risiko und nächsten Output schnell und anfängertauglich. |
| `mindestabnahme-mitwirkungspflichten` | Klausel-Fachmodul für Mindestabnahme: prüft, redlined und entwirft die Klausel mit Risikoampel, Verbraucher-/B2B-Unterscheidung und praxistauglicher Ersatzfassung im AGB-Recht. |
| `mitwirkungspflichten` | Klausel-Fachmodul für Mitwirkungspflichten: prüft, redlined und entwirft die Klausel mit Risikoampel, Verbraucher-/B2B-Unterscheidung und praxistauglicher Ersatzfassung im AGB-Recht. |
| `msa-rahmenvertrag` | Branchen-Fachmodul für MSA Rahmenvertrag: prüft typische AGB-Risiken des Vertragstyps und erzeugt Klauselarchitektur, Red Flags und bessere Bedingungen. |
| `nacherfuellung-vorrang` | Klausel-Fachmodul für Nacherfüllung Vorrang: prüft, redlined und entwirft die Klausel mit Risikoampel, Verbraucher-/B2B-Unterscheidung und praxistauglicher Ersatzfassung. |
| `nda-standardbedingungen` | Branchen-Fachmodul für NDA Standardbedingungen: prüft typische AGB-Risiken des Vertragstyps und erzeugt Klauselarchitektur, Red Flags und bessere Bedingungen. |
| `negative-feststellung-agb` | Output- und Streit-Skill für Negative Feststellung AGB: macht aus der AGB-Prüfung verwertbare Redlines, Entwürfe, Playbooks, Abmahnreaktionen oder Entscheidungsunterlagen. |
| `non-solicitation` | Klausel-Fachmodul für Non Solicitation: prüft, redlined und entwirft die Klausel mit Risikoampel, Verbraucher-/B2B-Unterscheidung und praxistauglicher Ersatzfassung. |
| `non-solicitation-norm-live-open-source` | Klausel-Fachmodul für Non Solicitation: prüft, redlined und entwirft die Klausel mit Risikoampel, Verbraucher-/B2B-Unterscheidung und praxistauglicher Ersatzfassung im AGB-Recht. |
| `norm-live-check-gesetze-im-internet` | Einstiegs- und Prüfungslinie für Norm Live Check Gesetze Im Internet: sortiert Ziel, Rolle, Dokumente, Normenstand, AGB-Risiko und nächsten Output schnell und anfängertauglich. |
| `open-source-komponenten` | Klausel-Fachmodul für Open Source Komponenten: prüft, redlined und entwirft die Klausel mit Risikoampel, Verbraucher-/B2B-Unterscheidung und praxistauglicher Ersatzfassung. |
| `parking-mobility-agb` | Branchen-Fachmodul für Parking Mobility AGB: prüft typische AGB-Risiken des Vertragstyps und erzeugt Klauselarchitektur, Red Flags und bessere Bedingungen. |
| `plain-language-politur` | Output- und Streit-Skill für Plain Language Politur: macht aus der AGB-Prüfung verwertbare Redlines, Entwürfe, Playbooks, Abmahnreaktionen oder Entscheidungsunterlagen. |
| `plattform-online-gate-rollout-rangfolge` | Einstiegs- und Prüfungslinie für Plattform und Online Checkout: sortiert Ziel, Rolle, Dokumente, Normenstand, AGB-Risiko und nächsten Output schnell und anfängertauglich im AGB-Recht. |
| `plattform-und-online-checkout` | Einstiegs- und Prüfungslinie für Plattform und Online Checkout: sortiert Ziel, Rolle, Dokumente, Normenstand, AGB-Risiko und nächsten Output schnell und anfängertauglich. |
| `plattformnutzung-app-vereinen-verbaenden` | AGB bei Plattformnutzung App Stores Apple Google Steam Amazon. Skill klaert die AGB-rechtlichen Kontrollfaktoren der Standardvertraege Marktstellung und Marktmacht (Art. 102 AEUV) sowie das Verhältnis zur P2B-Verordnung. Behandelt aktue... |
| `preisanpassung-klausel` | Klausel-Fachmodul für Preisanpassung Klausel: prüft, redlined und entwirft die Klausel mit Risikoampel, Verbraucher-/B2B-Unterscheidung und praxistauglicher Ersatzfassung. |
| `product-counsel-feedback-rechte-annahmefrist` | Output- und Streit-Skill für Product Counsel Workflow: macht aus der AGB-Prüfung verwertbare Redlines, Entwürfe, Playbooks, Abmahnreaktionen oder Entscheidungsunterlagen im AGB-Recht. |
| `product-counsel-workflow` | Output- und Streit-Skill für Product Counsel Workflow: macht aus der AGB-Prüfung verwertbare Redlines, Entwürfe, Playbooks, Abmahnreaktionen oder Entscheidungsunterlagen. |
| `quality-gate-vor-rollout` | Output- und Streit-Skill für Quality Gate Vor Rollout: macht aus der AGB-Prüfung verwertbare Redlines, Entwürfe, Playbooks, Abmahnreaktionen oder Entscheidungsunterlagen. |
| `rangfolge-sprache` | Klausel-Fachmodul für Rangfolge Sprache: prüft, redlined und entwirft die Klausel mit Risikoampel, Verbraucher-/B2B-Unterscheidung und praxistauglicher Ersatzfassung. |
| `rechtsabteilung-change-control-klauseln` | Rechtsabteilungs-Fachmodul für Change-Control-Klauseln im Konzernvertrag: Einseitige Leistungs- und Prozessänderungen werden in komplexen Konzern-Frameworks auf Zumutbarkeit und Governance geprüft. Mit Normen, Rechtsprechungsanker, Beleg... |
| `rechtsabteilung-change-vertragsstrafe` | Rechtsabteilungs-Fachmodul für Change-Control-Klauseln im Konzernvertrag: Einseitige Leistungs- und Prozessänderungen werden in komplexen Konzern-Frameworks auf Zumutbarkeit und Governance geprüft. Mit Normen, Rechtsprechungsanker, Beleg... |
| `rechtsabteilung-haftungsdeckel-daten-ki` | Rechtsabteilungs-Fachmodul für Haftungsdeckel für Daten- und KI-Schäden: Liability Caps bei Software, Daten, KI und Outsourcing werden so geprüft, dass Kardinalpflichten und Personenschäden nicht versehentlich abgeschnitten werden. Mit N... |
| `rechtsabteilung-haftungsdeckel-fuer-daten-und-ki-schaeden` | Rechtsabteilungs-Fachmodul für Haftungsdeckel für Daten- und KI-Schäden: Liability Caps bei Software, Daten, KI und Outsourcing werden so geprüft, dass Kardinalpflichten und Personenschäden nicht versehentlich abgeschnitten werden. Mit N... |
| `rechtsabteilung-preisanpassung` | Rechtsabteilungs-Fachmodul für Preisanpassung bei Dauerverträgen nach Energiekosten-Schock: Preisgleitklauseln werden nach Anlass, Parameter, Transparenz, Kündigungsrecht und Mitteilungsmechanik bewertet. Mit Normen, Rechtsprechungsanker... |
| `rechtsabteilung-preisanpassung-bei-dauervertraegen-nach-energiek` | Rechtsabteilungs-Fachmodul für Preisanpassung bei Dauerverträgen nach Energiekosten-Schock: Preisgleitklauseln werden nach Anlass, Parameter, Transparenz, Kündigungsrecht und Mitteilungsmechanik bewertet. Mit Normen, Rechtsprechungsanker... |
| `rechtsabteilung-vertragsstrafe-einheitspreis` | Rechtsabteilungs-Fachmodul für Vertragsstrafe in Einheitspreis- und Lieferverträgen: Rechtsabteilungen prüfen, ob Bezugsgrößen der Vertragsstrafe die tatsächlich beauftragte Leistung überschießen. Mit Normen, Rechtsprechungsanker, Belegm... |
| `rechtsabteilung-vertragsstrafe-in-einheitspreis-und-liefervertra` | Rechtsabteilungs-Fachmodul für Vertragsstrafe in Einheitspreis- und Lieferverträgen: Rechtsabteilungen prüfen, ob Bezugsgrößen der Vertragsstrafe die tatsächlich beauftragte Leistung überschießen. Mit Normen, Rechtsprechungsanker, Belegm... |
| `rechtsabteilung-zustimmungsfiktion-bank-agb` | Rechtsabteilungs-Fachmodul für Zustimmungsfiktion nach Bank-AGB-Urteil: Klauseln, die Schweigen oder bloße Weiternutzung als Zustimmung behandeln, werden für Preis- und Leistungsänderungen in B2C und B2B auseinandergenommen. Mit Normen,... |
| `rechtsabteilung-zustimmungsfiktion-nach-bank-agb-urteil` | Rechtsabteilungs-Fachmodul für Zustimmungsfiktion nach Bank-AGB-Urteil: Klauseln, die Schweigen oder bloße Weiternutzung als Zustimmung behandeln, werden für Preis- und Leistungsänderungen in B2C und B2B auseinandergenommen. Mit Normen,... |
| `rechtsfolge-306-kein-blue-pencil` | Norm- und Dogmatik-Skill für Rechtsfolge 306 Kein Blü Pencil: prüft die AGB-Kontrolle quellenstreng entlang BGB §§ 305 bis 310 und ordnet Rechtsfolge, Risiko und bessere Fassung. |
| `rechtsfolge-kein-rechtsfolgen-rueckabwicklung` | Norm- und Dogmatik-Skill für Rechtsfolge 306 Kein Blü Pencil: prüft die AGB-Kontrolle quellenstreng entlang BGB §§ 305 bis 310 und ordnet Rechtsfolge, Risiko und bessere Fassung im AGB-Recht. |
| `rechtsfolgen-rueckabwicklung-agb` | Norm- und Dogmatik-Skill für Rechtsfolgen Rückabwicklung AGB: prüft die AGB-Kontrolle quellenstreng entlang BGB §§ 305 bis 310 und ordnet Rechtsfolge, Risiko und bessere Fassung. |
| `rechtswahl` | Klausel-Fachmodul für Rechtswahl: prüft, redlined und entwirft die Klausel mit Risikoampel, Verbraucher-/B2B-Unterscheidung und praxistauglicher Ersatzfassung im AGB-Recht. |
| `rechtswahl-schweizer-risikoklassifizierung` | Rechtswahl Schweizer Recht in AGB als Versuch dem deutschen AGB-Recht zu entkommen. Skill klaert Rom-I-VO Art. 3 freie Rechtswahl Art. 6 zwingender Verbraucherschutz Art. 9 Eingriffsnormen sowie die Prüfung ob §§ 305-310 BGB internation... |
| `red-team-gegneransicht-agb` | Einstiegs- und Prüfungslinie für Red Team Gegneransicht AGB: sortiert Ziel, Rolle, Dokumente, Normenstand, AGB-Risiko und nächsten Output schnell und anfängertauglich. |
| `redline-kommentar-agb` | Output- und Streit-Skill für Redline Kommentar AGB: macht aus der AGB-Prüfung verwertbare Redlines, Entwürfe, Playbooks, Abmahnreaktionen oder Entscheidungsunterlagen. |
| `referenznennung` | Klausel-Fachmodul für Referenznennung: prüft, redlined und entwirft die Klausel mit Risikoampel, Verbraucher-/B2B-Unterscheidung und praxistauglicher Ersatzfassung im AGB-Recht. |
| `reisebedingungen-reseller-agb-risk-acceptance` | Branchen-Fachmodul für Reisebedingungen: prüft typische AGB-Risiken des Vertragstyps und erzeugt Klauselarchitektur, Red Flags und bessere Bedingungen im AGB-Recht. |
| `reseller-agb` | Branchen-Fachmodul für Reseller AGB: prüft typische AGB-Risiken des Vertragstyps und erzeugt Klauselarchitektur, Red Flags und bessere Bedingungen. |
| `risk-acceptance-memo` | Output- und Streit-Skill für Risk Acceptance Memo: macht aus der AGB-Prüfung verwertbare Redlines, Entwürfe, Playbooks, Abmahnreaktionen oder Entscheidungsunterlagen. |
| `rollout-mail-bestandskunden` | Output- und Streit-Skill für Rollout Mail Bestandskunden: macht aus der AGB-Prüfung verwertbare Redlines, Entwürfe, Playbooks, Abmahnreaktionen oder Entscheidungsunterlagen. |
| `rollout-monitoring-agb` | Einstiegs- und Prüfungslinie für Rollout Monitoring AGB: sortiert Ziel, Rolle, Dokumente, Normenstand, AGB-Risiko und nächsten Output schnell und anfängertauglich. |
| `ruegeobliegenheit-saas-agb-schiedsgericht` | Klausel-Fachmodul für Rügeobliegenheit: prüft, redlined und entwirft die Klausel mit Risikoampel, Verbraucher-/B2B-Unterscheidung und praxistauglicher Ersatzfassung im AGB-Recht. |
| `saas-agb` | Branchen-Fachmodul für SaaS AGB: prüft typische AGB-Risiken des Vertragstyps und erzeugt Klauselarchitektur, Red Flags und bessere Bedingungen. |
| `salvatorische-klausel` | Klausel-Fachmodul für Salvatorische Klausel: prüft, redlined und entwirft die Klausel mit Risikoampel, Verbraucher-/B2B-Unterscheidung und praxistauglicher Ersatzfassung. |
| `salvatorische-klausel-grenzen-rspr` | Salvatorische Klausel: Grenzen und Wirkung. Skill klaert die BGH-Linie zu Salvatorischen Klauseln in AGB-Vertraegen Wirkung der Klausel auf die Unwirksamkeit einzelner Bestimmungen Wechselwirkung mit § 306 BGB. Behandelt Sondervarianten... |
| `schadenspauschale-309` | Norm- und Dogmatik-Skill für Schadenspauschale 309: prüft die AGB-Kontrolle quellenstreng entlang BGB §§ 305 bis 310 und ordnet Rechtsfolge, Risiko und bessere Fassung. |
| `schiedsgericht` | Klausel-Fachmodul für Schiedsgericht: prüft, redlined und entwirft die Klausel mit Risikoampel, Verbraucher-/B2B-Unterscheidung und praxistauglicher Ersatzfassung im AGB-Recht. |
| `schriftform-textform` | Klausel-Fachmodul für Schriftform Textform: prüft, redlined und entwirft die Klausel mit Risikoampel, Verbraucher-/B2B-Unterscheidung und praxistauglicher Ersatzfassung. |
| `security-incidents` | Klausel-Fachmodul für Security Incidents: prüft, redlined und entwirft die Klausel mit Risikoampel, Verbraucher-/B2B-Unterscheidung und praxistauglicher Ersatzfassung. |
| `sicherungsrechte-sla-service-social-media` | Klausel-Fachmodul für Sicherungsrechte: prüft, redlined und entwirft die Klausel mit Risikoampel, Verbraucher-/B2B-Unterscheidung und praxistauglicher Ersatzfassung im AGB-Recht. |
| `sla-service-credits` | Klausel-Fachmodul für SLA Service Credits: prüft, redlined und entwirft die Klausel mit Risikoampel, Verbraucher-/B2B-Unterscheidung und praxistauglicher Ersatzfassung. |
| `social-media-agb` | Branchen-Fachmodul für Social Media AGB: prüft typische AGB-Risiken des Vertragstyps und erzeugt Klauselarchitektur, Red Flags und bessere Bedingungen. |
| `softwarelizenz-agb` | Branchen-Fachmodul für Softwarelizenz AGB: prüft typische AGB-Risiken des Vertragstyps und erzeugt Klauselarchitektur, Red Flags und bessere Bedingungen. |
| `sperrung-suspendierung` | Klausel-Fachmodul für Sperrung Suspendierung: prüft, redlined und entwirft die Klausel mit Risikoampel, Verbraucher-/B2B-Unterscheidung und praxistauglicher Ersatzfassung. |
| `steuern-umsatzsteuer` | Klausel-Fachmodul für Steürn Umsatzsteür: prüft, redlined und entwirft die Klausel mit Risikoampel, Verbraucher-/B2B-Unterscheidung und praxistauglicher Ersatzfassung. |
| `steuern-umsatzsteuer-stummer-upload` | Klausel-Fachmodul für Steürn Umsatzsteür: prüft, redlined und entwirft die Klausel mit Risikoampel, Verbraucher-/B2B-Unterscheidung und praxistauglicher Ersatzfassung im AGB-Recht. |
| `stummer-upload-agb-dokumente` | Einstiegs- und Prüfungslinie für Stummer Upload AGB Dokumente: sortiert Ziel, Rolle, Dokumente, Normenstand, AGB-Risiko und nächsten Output schnell und anfängertauglich. |
| `subscription-abonnement` | Branchen-Fachmodul für Subscription Abonnement: prüft typische AGB-Risiken des Vertragstyps und erzeugt Klauselarchitektur, Red Flags und bessere Bedingungen. |
| `subscription-box-agb` | Branchen-Fachmodul für Subscription Box AGB: prüft typische AGB-Risiken des Vertragstyps und erzeugt Klauselarchitektur, Red Flags und bessere Bedingungen. |
| `subunternehmer` | Klausel-Fachmodul für Subunternehmer: prüft, redlined und entwirft die Klausel mit Risikoampel, Verbraucher-/B2B-Unterscheidung und praxistauglicher Ersatzfassung im AGB-Recht. |
| `support-response-telekommunikation-agb` | Klausel-Fachmodul für Support Response Times: prüft, redlined und entwirft die Klausel mit Risikoampel, Verbraucher-/B2B-Unterscheidung und praxistauglicher Ersatzfassung im AGB-Recht. |
| `support-response-times` | Klausel-Fachmodul für Support Response Times: prüft, redlined und entwirft die Klausel mit Risikoampel, Verbraucher-/B2B-Unterscheidung und praxistauglicher Ersatzfassung. |
| `telekommunikation-agb` | Branchen-Fachmodul für Telekommunikation AGB: prüft typische AGB-Risiken des Vertragstyps und erzeugt Klauselarchitektur, Red Flags und bessere Bedingungen. |
| `transparenzgebot-307` | Norm- und Dogmatik-Skill für Transparenzgebot 307: prüft die AGB-Kontrolle quellenstreng entlang BGB §§ 305 bis 310 und ordnet Rechtsfolge, Risiko und bessere Fassung. |
| `ueberraschende-klausel-305c` | Norm- und Dogmatik-Skill für Überraschende Klausel 305c: prüft die AGB-Kontrolle quellenstreng entlang BGB §§ 305 bis 310 und ordnet Rechtsfolge, Risiko und bessere Fassung. |
| `uklag-unterlassung-verbandsklage` | Norm- und Dogmatik-Skill für UKlaG Unterlassung Verbandsklage: prüft die AGB-Kontrolle quellenstreng entlang BGB §§ 305 bis 310 und ordnet Rechtsfolge, Risiko und bessere Fassung. |
| `unterlassungserklaerung-modifizieren` | Output- und Streit-Skill für Unterlassungserklärung Modifizieren: macht aus der AGB-Prüfung verwertbare Redlines, Entwürfe, Playbooks, Abmahnreaktionen oder Entscheidungsunterlagen. |
| `unternehmerverkehr-310-abs1` | Norm- und Dogmatik-Skill für Unternehmerverkehr 310 Abs. 1: prüft die AGB-Kontrolle quellenstreng entlang BGB §§ 305 bis 310 und ordnet Rechtsfolge, Risiko und bessere Fassung. |
| `unternehmerverkehr-abs1-schnellcheck-user` | Norm- und Dogmatik-Skill für Unternehmerverkehr 310 Abs. 1: prüft die AGB-Kontrolle quellenstreng entlang BGB §§ 305 bis 310 und ordnet Rechtsfolge, Risiko und bessere Fassung im AGB-Recht. |
| `unternehmerverkehr-schnellcheck` | Einstiegs- und Prüfungslinie für Unternehmerverkehr Schnellcheck: sortiert Ziel, Rolle, Dokumente, Normenstand, AGB-Risiko und nächsten Output schnell und anfängertauglich. |
| `user-content-moderation` | Klausel-Fachmodul für User Content Moderation: prüft, redlined und entwirft die Klausel mit Risikoampel, Verbraucher-/B2B-Unterscheidung und praxistauglicher Ersatzfassung. |
| `vdug-abhilfeklage-agb-schnittstelle` | Norm- und Dogmatik-Skill für VDuG Abhilfeklage AGB Schnittstelle: prüft die AGB-Kontrolle quellenstreng entlang BGB §§ 305 bis 310 und ordnet Rechtsfolge, Risiko und bessere Fassung. |
| `verbraucherbesonderheiten-310-abs3` | Norm- und Dogmatik-Skill für Verbraucherbesonderheiten 310 Abs. 3: prüft die AGB-Kontrolle quellenstreng entlang BGB §§ 305 bis 310 und ordnet Rechtsfolge, Risiko und bessere Fassung. |
| `verbraucherfreundliche-fassung` | Output- und Streit-Skill für Verbraucherfreundliche Fassung: macht aus der AGB-Prüfung verwertbare Redlines, Entwürfe, Playbooks, Abmahnreaktionen oder Entscheidungsunterlagen. |
| `verbraucherfreundliche-fassung-verbraucherschutz` | Output- und Streit-Skill für Verbraucherfreundliche Fassung: macht aus der AGB-Prüfung verwertbare Redlines, Entwürfe, Playbooks, Abmahnreaktionen oder Entscheidungsunterlagen im AGB-Recht. |
| `verbraucherschutz-schnellcheck` | Einstiegs- und Prüfungslinie für Verbraucherschutz Schnellcheck: sortiert Ziel, Rolle, Dokumente, Normenstand, AGB-Risiko und nächsten Output schnell und anfängertauglich. |
| `vereinsbedingungen` | Branchen-Fachmodul für Vereinsbedingungen: prüft typische AGB-Risiken des Vertragstyps und erzeugt Klauselarchitektur, Red Flags und bessere Bedingungen im AGB-Recht. |
| `verfuegbarkeit-wartungsfenster` | Klausel-Fachmodul für Verfügbarkeit Wartungsfenster: prüft, redlined und entwirft die Klausel mit Risikoampel, Verbraucher-/B2B-Unterscheidung und praxistauglicher Ersatzfassung. |
| `vergaberechtliche-vertragsbedingungen` | Branchen-Fachmodul für Vergaberechtliche Vertragsbedingungen: prüft typische AGB-Risiken des Vertragstyps und erzeugt Klauselarchitektur, Red Flags und bessere Bedingungen. |
| `vergaberechtliche-vertragsbedingungen-vertragsstrafe` | Branchen-Fachmodul für Vergaberechtliche Vertragsbedingungen: prüft typische AGB-Risiken des Vertragstyps und erzeugt Klauselarchitektur, Red Flags und bessere Bedingungen im AGB-Recht. |
| `verhandlungs-playbook-agb` | Output- und Streit-Skill für Verhandlungs Playbook AGB: macht aus der AGB-Prüfung verwertbare Redlines, Entwürfe, Playbooks, Abmahnreaktionen oder Entscheidungsunterlagen. |
| `verjaehrungsverkuerzung-verkaufsbedingungen` | Klausel-Fachmodul für Verjährungsverkürzung: prüft, redlined und entwirft die Klausel mit Risikoampel, Verbraucher-/B2B-Unterscheidung und praxistauglicher Ersatzfassung im AGB-Recht. |
| `verkaufsbedingungen-b2b` | Branchen-Fachmodul für Verkaufsbedingungen B2B: prüft typische AGB-Risiken des Vertragstyps und erzeugt Klauselarchitektur, Red Flags und bessere Bedingungen. |
| `versicherung-avb` | Branchen-Fachmodul für Versicherung Avb: prüft typische AGB-Risiken des Vertragstyps und erzeugt Klauselarchitektur, Red Flags und bessere Bedingungen. |
| `versicherungsvertraegen-vvg-agb` | AGB-Kontrolle bei Versicherungsvertraegen (VVG). Skill behandelt das Spannungsverhaeltnis zwischen den Allgemeinen Versicherungsbedingungen (AVB) und § 307 BGB. Klaert das Transparenzgebot Risikoausschluesse Obliegenheitsverletzungen San... |
| `versionsdiff-agb` | Output- und Streit-Skill für Versionsdiff AGB: macht aus der AGB-Prüfung verwertbare Redlines, Entwürfe, Playbooks, Abmahnreaktionen oder Entscheidungsunterlagen. |
| `vertragsstrafe-309` | Norm- und Dogmatik-Skill für Vertragsstrafe 309: prüft die AGB-Kontrolle quellenstreng entlang BGB §§ 305 bis 310 und ordnet Rechtsfolge, Risiko und bessere Fassung. |
| `vertraulichkeit-klausel` | Klausel-Fachmodul für Vertraulichkeit Klausel: prüft, redlined und entwirft die Klausel mit Risikoampel, Verbraucher-/B2B-Unterscheidung und praxistauglicher Ersatzfassung. |
| `vollmacht-vertretung` | Klausel-Fachmodul für Vollmacht Vertretung: prüft, redlined und entwirft die Klausel mit Risikoampel, Verbraucher-/B2B-Unterscheidung und praxistauglicher Ersatzfassung. |
| `vorkasse-abschlag-sicherheit` | Klausel-Fachmodul für Vorkasse Abschlag Sicherheit: prüft, redlined und entwirft die Klausel mit Risikoampel, Verbraucher-/B2B-Unterscheidung und praxistauglicher Ersatzfassung. |
| `vorkasse-abschlag-wartung-maintenance-website` | Klausel-Fachmodul für Vorkasse Abschlag Sicherheit: prüft, redlined und entwirft die Klausel mit Risikoampel, Verbraucher-/B2B-Unterscheidung und praxistauglicher Ersatzfassung im AGB-Recht. |
| `wartung-maintenance` | Branchen-Fachmodul für Wartung Maintenance: prüft typische AGB-Risiken des Vertragstyps und erzeugt Klauselarchitektur, Red Flags und bessere Bedingungen. |
| `website-update-check` | Output- und Streit-Skill für Website Update Check: macht aus der AGB-Prüfung verwertbare Redlines, Entwürfe, Playbooks, Abmahnreaktionen oder Entscheidungsunterlagen. |
| `wesentliche-rechte-pflichten-307` | Norm- und Dogmatik-Skill für Wesentliche Rechte Pflichten 307: prüft die AGB-Kontrolle quellenstreng entlang BGB §§ 305 bis 310 und ordnet Rechtsfolge, Risiko und bessere Fassung. |
| `widerruf-umfeld-agb` | Klausel-Fachmodul für Widerruf Umfeld AGB: prüft, redlined und entwirft die Klausel mit Risikoampel, Verbraucher-/B2B-Unterscheidung und praxistauglicher Ersatzfassung. |
| `wohnraummiete-agb` | Branchen-Fachmodul für Wohnraummiete AGB: prüft typische AGB-Risiken des Vertragstyps und erzeugt Klauselarchitektur, Red Flags und bessere Bedingungen. |
| `wohnraummiete-agb-zahlungsdienste` | Branchen-Fachmodul für Wohnraummiete AGB: prüft typische AGB-Risiken des Vertragstyps und erzeugt Klauselarchitektur, Red Flags und bessere Bedingungen im AGB-Recht. |
| `zahlungsdienste-agb` | Branchen-Fachmodul für Zahlungsdienste AGB: prüft typische AGB-Risiken des Vertragstyps und erzeugt Klauselarchitektur, Red Flags und bessere Bedingungen. |
| `zahlungsmittel-chargeback` | Klausel-Fachmodul für Zahlungsmittel Chargeback: prüft, redlined und entwirft die Klausel mit Risikoampel, Verbraucher-/B2B-Unterscheidung und praxistauglicher Ersatzfassung. |
| `zahlungsverzug-mahnkosten` | Klausel-Fachmodul für Zahlungsverzug Mahnkosten: prüft, redlined und entwirft die Klausel mit Risikoampel, Verbraucher-/B2B-Unterscheidung und praxistauglicher Ersatzfassung. |

<!-- END SKILLS-OVERVIEW (auto-generated) -->

<!-- BEGIN megaprompt-und-vorlagen (autogen) -->
## Experimentell: dieses Plugin auch ohne Claude Code

### Megaprompt (alle Kern-Skills in einer Datei)

Das Plugin gibt es zusaetzlich als **single-file Megaprompt** — ein experimentelles Markdown, das die wichtigsten Skills in einer einzigen Datei buendelt. Drop das in einen Chat ohne Claude-Code-Integration; der Agent erhaelt damit die gebuendelten Skill-Anweisungen.

- **Direkt-Download**: [`agb-recht-pruefer.md`](https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/testakten/megaprompts/agb-recht-pruefer.md) (27 KB)
- Im Repo: [`testakten/megaprompts/agb-recht-pruefer.md`](../testakten/megaprompts/agb-recht-pruefer.md)

*Keine Haftung, keine Gewaehr — Megaprompts sind eine Best-Effort-Kompression, kein vollwertiger Plugin-Ersatz.*

### Formatvorlagen (Markdown + ODT)

Sofort verwendbare Vorlagen (Times Roman 11pt, A4, mit Disclaimer und Feldern in [Klammern]). Markdown zum Lesen / Anpassen, ODT zum Bearbeiten in LibreOffice/Word.

| Vorlage | Markdown | ODT |
| --- | --- | --- |
| Agb Prüfraster Klauselrisiko Paragraf 307 Bgb | [`.md`](https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/testakten/formatvorlagen-paradebeispiele/agb-recht-pruefer/agb-pruefraster-klauselrisiko-paragraf-307-bgb.md) | [`.odt`](https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/testakten/formatvorlagen-paradebeispiele/agb-recht-pruefer/agb-pruefraster-klauselrisiko-paragraf-307-bgb.odt) |

*Experimentelle KI-Vorlagen — keine Haftung. Vor Verwendung im Mandat anwaltlich prüfen und an konkreten Fall anpassen.*

<!-- END megaprompt-und-vorlagen (autogen) -->
