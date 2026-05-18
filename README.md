# Klotzkette German Legal Skills

> Deutsche Rechtsfähigkeiten für die anwaltliche Praxis – Skills, Sub-Agenten, Hooks und Cookbooks für die Beratung in deutschen Kanzleien. Mit verbindlicher **BGH-Zitierweise** und ausdrücklicher Berücksichtigung des hohen Stellenwerts von **Kommentaren und Aufsätzen** im civil law.

Diese Sammlung lässt sich u. a. in Claude Code, Claude Desktop und vergleichbaren Skill-fähigen KI-Umgebungen einsetzen. Inspiriert von und adaptiert nach Anthropics offenem Projekt `claude-for-legal`, vollständig auf das deutsche Recht und die Arbeitsweise deutscher Kanzleien zugeschnitten.

## Was ist drin?

Plugins (in Claude-Code-Terminologie) für die wichtigsten Rechtsgebiete der deutschen Beratungspraxis:

| Plugin | Beschreibung |
| --- | --- |
| [`arbeitsrecht`](./arbeitsrecht) | Individual- und Kollektivarbeitsrecht – Kündigung, Aufhebungsvertrag, Abmahnung, Anhörung Betriebsrat, KSchG-Klage, internationale Entsendungen |
| [`datenschutzrecht`](./datenschutzrecht) | DSGVO, BDSG, TTDSG, Auskunft, Datenpanne, AVV |
| [`gesellschaftsrecht`](./gesellschaftsrecht) | GmbH, AG, Personengesellschaften, M&A, Due Diligence, Gesellschafterbeschluss, Handelsregister |
| [`gewerblicher-rechtsschutz`](./gewerblicher-rechtsschutz) | Marke, Design, Patent, Urheberrecht, UWG-Abmahnung |
| [`jurastudium`](./jurastudium) | Werkzeuge für Studium und Referendariat |
| [`kanzlei-builder-hub`](./kanzlei-builder-hub) | Werkzeuge zum Bauen eigener kanzleiinterner Skills |
| [`ki-governance`](./ki-governance) | EU-KI-VO, KI-Inventar, AIA, Vendor Review |
| [`produktrecht`](./produktrecht) | Produktrecht, AGB, Impressum, PAngV, Marketing-Claims |
| [`prozessrecht`](./prozessrecht) | Zivil-, Straf- und Verwaltungsprozess, Mahnverfahren, einstweilige Verfügung, Zwangsvollstreckung, Verkehrsunfall |
| [`rechtsberatungsstelle`](./rechtsberatungsstelle) | Pro-Bono-Beratungsstellen, Mandantenakte, Mandantenbrief |
| [`regulatorisches-recht`](./regulatorisches-recht) | Aufsichtsrecht, KWG, GwG, EnWG, TKG, Inkasso/RDG, UStVA, DORA-IKT-Vertragsprüfung |
| [`steuerberatung`](./steuerberatung) | BWA-/SuSa-/Bilanz-Krisenprüfung (§§ 17, 19 InsO, § 102 StaRUG), rollierende Liquiditätsvorschau 13/26/52 Wochen mit Ampel und Fortführungsprognose nach IDW S 6/S 11. Mit kompletter Beispielakte (Edelholz Manufaktur Berlin GmbH). |
| [`vertragsrecht`](./vertragsrecht) | NDA, SaaS-/MSA-Review, Lieferanten-AGB, Renewal-Tracking |

Zusätzlich:
- [`managed-agent-cookbooks`](./managed-agent-cookbooks) – wiederverwendbare Vorlagen für Multi-Agent-Workflows.
- [`references/zitierweise.md`](./references/zitierweise.md) – die **verbindliche** deutsche Zitierweise (BGH-Stil), die alle Skills einhalten.
- [`references/methodik-deutsches-recht.md`](./references/methodik-deutsches-recht.md) – Methodenlehre, Anspruchsgrundlagenreihenfolge, Beweislast, Fristen.

## Schnellstart

1. Repository klonen oder als ZIP herunterladen.
2. In einer Skill-fähigen KI-Umgebung als Marketplace einbinden, z. B.:

   ```bash
   /plugin marketplace add Klotzkette/claude-fuer-deutsches-recht
   /plugin install arbeitsrecht
   /plugin install vertragsrecht
   ```

3. Optional Marketplace lokal vorlegen:

   ```bash
   /plugin marketplace add /pfad/zu/claude-fuer-deutsches-recht
   ```

Details siehe [`QUICKSTART.md`](./QUICKSTART.md).

## Was ist anders als am US-Original?

Diese Adaption ist **kein** einfaches Übersetzungsprojekt. Sie berücksichtigt die strukturellen Unterschiede des deutschen Rechts:

| Aspekt | USA | Deutschland (dieses Repository) |
| --- | --- | --- |
| Bindungswirkung von Urteilen | stare decisis (vertikal bindend) | grundsätzlich **keine** Bindung (Ausn.: § 31 BVerfGG) |
| Pre-Trial Discovery | umfassend | **gibt es nicht**; nur eng begrenzte §§ 142, 144 ZPO |
| Stellenwert von Kommentaren | gering | **zentral**, oft tragend – jeder Skill belegt mit Bearbeiter, Kommentar, Auflage, Norm, Rn. |
| Stellenwert von Aufsätzen | gering | hoch, insbesondere bei neuen Rechtsfragen |
| Zitierweise | Bluebook | BGH-/Beck-Stil – verbindlich in [`references/zitierweise.md`](./references/zitierweise.md) |
| Due Diligence | mit Discovery | mit Q&A, Datenraum, anwaltlicher Sachverhaltsaufklärung |
| Kündigungsschutz | at-will (Ausn.) | Regelfall (KSchG ab 6 Monate / >10 AN) |

Außerdem ergänzt: über 20 Skills zu typisch deutschen Themen, die im Original fehlen, u. a.:

- **Kündigungsschutzklage** nach § 4 KSchG (3-Wochen-Frist)
- **Mahnbescheid** §§ 688 ff. ZPO
- **Einstweilige Verfügung & Schutzschrift**
- **Aufhebungsvertrag** inkl. Sperrzeit-Prüfung
- **Anhörung des Betriebsrats** § 102 BetrVG
- **Verkehrsunfall**-Abwicklung
- **UWG-Abmahnung** und **Urheberrechts-Abmahnung**
- **AGB-Prüfung** §§ 305 ff. BGB
- **Widerruf im Fernabsatz** §§ 312g, 355 BGB
- **GmbH-Gründung** und **Handelsregisteranmeldung**
- **DSGVO-Auskunft** Art. 15 DSGVO und **Datenpanne** Art. 33/34 DSGVO
- **Umsatzsteuer-Voranmeldung** und Korrektur nach § 153 AO
- **Inkasso** nach RDG / § 43d BRAO
- **DORA-IKT-Vertragsprüfung** (VO (EU) 2022/2554) mit Tabular Review, EUR-Lex-Live-Snapshot und Klausel-Patch-Liste
- **Markenanmeldung** beim DPMA
- **Impressumspflicht** §§ 5, 6 DDG
- **PAngV-Prüfung**

Eine vollständige Übersicht steht in [`references/rechtsgebiete-uebersicht.md`](./references/rechtsgebiete-uebersicht.md).

## Verbindliche Zitierweise

Jeder Skill verweist auf [`references/zitierweise.md`](./references/zitierweise.md). Die Kernregeln in Kurzfassung:

- **Urteile:** `BGH, Urt. v. 13.07.2022 – VIII ZR 317/21, NJW 2022, 2754 Rn. 21.`
- **Beschlüsse:** `BVerfG, Beschl. v. 06.11.2019 – 1 BvR 16/13, BVerfGE 152, 152 Rn. 78 – "Recht auf Vergessen I".`
- **Kommentare:** `Ernst, in: MüKoBGB, 9. Aufl. 2022, § 280 Rn. 154.`
- **BeckOK:** `Sutschet, in: BeckOK BGB, 70. Ed. (Stand 01.02.2025), § 311 Rn. 45.`
- **Aufsätze:** `Grigoleit, NJW 2020, 1873 (1876).`

Pflicht: Datum + Aktenzeichen + Fundstelle + Randnummer bei Rspr.; Bearbeiter + Werk + Auflage + Norm + Rn. bei Kommentaren.

## Hinweise zur Nutzung

- Dieses Repository ersetzt **keine** anwaltliche Beratung. Es liefert Werkzeuge und Vorlagen für Juristinnen und Juristen.
- Skills greifen ausschließlich auf den Datenraum des jeweiligen Mandats zu. Mandantengeheimnis (§ 43a Abs. 2 BRAO, § 203 StGB) ist zu wahren.
- Bei jeder Nutzung von LLM-Ausgaben: **Quellen verifizieren**. Halluzinationsrisiko ist real, insbesondere bei Rechtsprechung mit "passend klingenden" Aktenzeichen.
- Geld- und Sicherungsleistungen (z. B. Mahnbescheid, einstweilige Verfügung) sind fristgebunden – die Skills berechnen Fristen, aber die anwaltliche Kontrolle bleibt.

## Lizenz

Apache License, Version 2.0 – siehe [`LICENSE`](./LICENSE) und [`NOTICE`](./NOTICE).

Die ursprüngliche Vorlage `claude-for-legal` von Anthropic steht unter der MIT-Lizenz; diese Adaption erweitert, ersetzt und ergänzt die ursprünglichen Inhalte und wird unter der oben genannten Lizenz veröffentlicht.

## Mitwirken

Beiträge willkommen – siehe [`CONTRIBUTING.md`](./CONTRIBUTING.md).
