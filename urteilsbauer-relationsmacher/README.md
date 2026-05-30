# Urteilsbauer und Relationsmacher

Technischer Plugin-Name: `urteilsbauer-relationsmacher`.

Freistehendes Plugin für **Amts-, Land- und Familienrichter sowie Rechtspfleger**. Begleitet von der Aktenintake über die Relation und die Beweiswürdigung mit Richter-Input bis zum fertigen Urteil oder Beschluss inklusive Tenor, Tatbestand, Entscheidungsgründen, Kosten- und Rechtsmittelbelehrung. Erzeugt am Ende ein DOCX nach § 313 ZPO.

## Direkt-Download

| Plugin | Direkt-Download |
| --- | --- |
| urteilsbauer-relationsmacher | [urteilsbauer-relationsmacher.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/urteilsbauer-relationsmacher.zip) |

## Installation

1. Claude Code oder Claude Desktop/Cowork öffnen.
2. **Customize Plugins** bzw. **Personal plugins** wählen.
3. **Install from .zip** und `urteilsbauer-relationsmacher.zip` hochladen.
4. Mit einem konkreten Auftrag starten, zum Beispiel: `Starte die Relation fuer eine Werklohnklage. Akte liegt vor.`

Alternativ via Marketplace:

```
/plugin marketplace add Klotzkette/claude-fuer-deutsches-recht
/plugin install urteilsbauer-relationsmacher@claude-fuer-deutsches-recht
```

Nicht das komplette Repository-ZIP hochladen. Das Plugin-ZIP muss im Root direkt `.claude-plugin/plugin.json` und `skills/` enthalten.

## Arbeitsakten

- **Solis Vision X Smartglasses** (Produkthaftung und DSGVO bei smarter Brille, AG/LG-Zivil): [testakten/solis-vision-x-smartglasses/](../testakten/solis-vision-x-smartglasses/) -> [testakte-solis-vision-x-smartglasses.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-solis-vision-x-smartglasses.zip)
- **LUMEN Studios** (Insolvenz- und strafrechtliche Schnittstelle): [testakten/lumen-studios-insolvenz-strafverfahren/](../testakten/lumen-studios-insolvenz-strafverfahren/) -> [testakte-lumen-studios-insolvenz-strafverfahren.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-lumen-studios-insolvenz-strafverfahren.zip)

## Skill-Landkarte

| Skill | Zweck |
| --- | --- |
| `aktenintake-zivil` | Erfasst Parteien, Anträge, Sachverhalt, Streitwert, Anlagen und Lage. |
| `zulaessigkeit-pruefen` | Pruft Statthaftigkeit, Zuständigkeit, Partei- und Prozessfähigkeit, Rechtsschutzbedürfnis. |
| `relation-zivil` | Baut Relation aus Klagegrund und Verteidigung mit Streitstand und Beweislage. |
| `vollrelation-langfassung` | Liefert die ausführliche Vollrelation mit Hilfserwaegungen und Eventualbegründung. |
| `anspruchsgrundlagen-pruefen` | Identifiziert und subsumiert die einschlaegigen Anspruchsgrundlagen. |
| `kollidierende-agb-pruefen` | Loest AGB-Konflikt nach Restguelitgkeits- und Knock-out-Doktrin. |
| `cisg-pruefen` | Pruft CISG-Anwendbarkeit, Anspruechs- und Aufrechnungslage. |
| `internationales-privatrecht` | Klärt anwendbares Recht nach Rom I/II und nationalem IPR. |
| `incoterms-und-gefahruebergang` | Wendet Incoterms 2020 auf Gefahrübergang und Transportkosten an. |
| `dsgvo-rechtswidriges-produkt` | Beurteilt DSGVO-Verstöße durch Produkte mit Datenverarbeitung. |
| `familienrichter-spezifika` | Familienrechtliche Besonderheiten: FamFG-Verfahren, Anhörungspflicht, Vergleichsdruck. |
| `beweisbeschluss-vorbereiten` | Formuliert Beweisthemen, Beweismittel und Beweisanordnung. |
| `beweiswuerdigung-mit-richter-input` | Holt Richter-Input zu Glaubwürdigkeit ein und baut Beweiswürdigung. |
| `tatbestand-zivil-schreiben` | Verfasst Tatbestand mit unstreitigem und streitigem Sachverhalt und Anträgen. |
| `entscheidungsgruende-zivil-schreiben` | Baut Entscheidungsgründe mit Subsumtion und juristischer Begründung. |
| `tenor-bauen-zivil` | Erstellt Tenor mit Hauptsache, Kosten, vorläufiger Vollstreckbarkeit. |
| `kostenentscheidung-bauen` | Berechnet Kostenquote nach §§ 91 ff. ZPO inklusive Vergleichswerten. |
| `vorlaeufige-vollstreckbarkeit` | Setzt Sicherheitsleistung und Abwendungsbefugnis nach §§ 708 ff. ZPO. |
| `rechtsmittelbelehrung-zivil` | Erzeugt korrekte Rechtsmittelbelehrung für Berufung, Beschwerde, Revision. |
| `beschluss-bauen-zpo` | Baut Beschlüsse statt Urteilen, etwa bei einstweiligem Rechtsschutz oder Streitwertfestsetzung. |
| `berufungsfest-pruefen` | Pruft das Urteil auf Berufungsfestigkeit und typische Aufhebungsgründe. |
| `revisionsfest-pruefen` | Pruft Urteil auf revisionsrechtliche Schwachstellen. |
| `dokumente-rendern-urteil-docx` | Rendert das fertige Urteil als DOCX nach § 313 ZPO. |
| `schulung-urteilsbauer` | Trainingsskill zur Einarbeitung neuer Richter und Rechtspfleger. |

## Typische Workflows

- Aktenintake -> Zulässigkeit -> Relation -> Anspruchsgrundlagen -> Beweisbeschluss.
- Beweiswürdigung mit Richter-Input -> Tatbestand -> Entscheidungsgründe -> Tenor.
- Kostenentscheidung -> Vorläufige Vollstreckbarkeit -> Rechtsmittelbelehrung.
- Berufungs-/Revisionsfestigkeit -> DOCX-Rendering nach § 313 ZPO.

## Haftung

Dieses Plugin ist ein Arbeitswerkzeug für die richterliche Praxis. Es ersetzt keine eigene rechtliche Prüfung und keine Beratung durch zugelassene Rechtsanwälte. Die Verantwortung für Tenor, Tatbestand und Entscheidungsgründe bleibt beim Spruchkoerper.


<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Ueberblick

Automatisch generierte Komplett-Liste aller 25 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `aktenintake-zivil` | Eingehende Zivilakte vor erster Prüfung strukturieren: Richter oder Referendar erhalt neue Akte und muss Überblick gewinnen. Normen: § 313 ZPO (Urteilsinhalt), § 286 ZPO (freie Beweiswürdigung), § 139 ZPO (richterliche Hinweispflicht). P... |
| `allgemein` | Einstieg, Schnelltriage und Workflow-Routing im Urteilsbauer Relationsmacher-Plugin. Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken und Wunsch-Output ab, schlägt passende Spezial-Skills aus diesem Plugin vor und führt in einen klaren Ar... |
| `anspruchsgrundlagen-pruefen` | Anspruchsgrundlagen identifizieren und Prüfungsreihenfolge bestimmen: Richter oder Kandidat muss Anspruchskonkurrenz lösen. Normen: §§ 433 ff., 280 ff., 812 ff., 823 ff. BGB; HGB; CISG; GmbHG; StVG; ProdHG; IPR Rom-I/II. Prüfraster: Reih... |
| `berufungsfest-pruefen` | Fertiges Urteil gegen häufigste Aufhebungsgründe selbst prüfen: Richter will vor Urteilsversand Aufhebungsrisiken minimieren. Normen: § 529 ZPO (Tatsachenfeststellung Berufung), § 546 ZPO (Rechtsverletzung), § 547 Nr. 6 ZPO (Begründungsm... |
| `beschluss-bauen-zpo` | Zivilrechtliche Beschluesse erstellen: PKH, Streitwert, Beweis, Hinweis nach § 139 ZPO, Kostenfestsetzung, Versaeumnis, Erledigung. Normen: §§ 127 und 329 und 358 ff. sowie 139 und 103 ff. ZPO. Prüfraster: Unterschied Beschluss/Urteil (B... |
| `beweisbeschluss-vorbereiten` | Beweisbeschluss nach § 359 ZPO vorbereiten: Richter bestimmt Beweisaufnahme nach muendlicher Verhandlung. Normen: § 359 ZPO (Inhalt Beweisbeschluss), § 286 ZPO (Beweislast), §§ 373 ff. ZPO (Zeugen), §§ 402 ff. ZPO (Sachverständige). Prüf... |
| `beweiswuerdigung-mit-richter-input` | Strukturierte Beweiswürdigung nach § 286 ZPO schreiben: Richter hat Beweise erhoben und will Entscheidungsgründe-Abschnitt verfassen. Normen: § 286 ZPO (freie Beweiswürdigung), § 261 ZPO (Beweislast), §§ 414 ff. ZPO (Sachverständige). Pr... |
| `cisg-pruefen` | UN-Kaufrecht (CISG) auf Anwendbarkeit und Eingreifen prüfen: Internationaler Kaufvertrag mit Auslandsbezug und Vertragsstreit. Normen: CISG Art. 1-6 (Anwendungsbereich), Art. 25 (wesentliche Vertragsverletzung), Art. 35 (Vertragsmäßigkei... |
| `dokumente-rendern-urteil-docx` | Zivilurteil als DOCX im offiziellen Gerichtslayout rendern: Richter oder Referendar will fertiges Urteil als Dokument ausgeben. Normen: § 313 ZPO (Urteilsinhalt und -form). Prüfraster: Gerichtslayout (Aktenzeichen, Gerichtsbezeichnung, I... |
| `dsgvo-rechtswidriges-produkt` | Produkt aus dem Ausland auf DSGVO-Rechtswidrigkeit prüfen: Richter oder Anwalt muss beurteilen ob Smartglasses oder IoT-Produkt DSGVO-konform ist. Normen: Art. 3 DSGVO (räumlicher Anwendungsbereich), Art. 5 Abs. 1 lit. c (Datensparsamkei... |
| `entscheidungsgruende-zivil-schreiben` | Entscheidungsgründe eines Zivilurteils im Urteilsstil schreiben: Richter hat Beweise erhoben und muss Begründung formulieren. Normen: § 313 Abs. 3 ZPO (Entscheidungsgründe), § 286 ZPO. Prüfraster: Urteilsstil (kein Gutachtenstil), Obersa... |
| `familienrichter-spezifika` | FamFG-Spezifika für Familienrichter anwenden: Richter am Familiengericht muss Beschluss statt Urteil abfassen. Normen: § 38 FamFG (Beschluss), § 137 FamFG (Verbund- und Folgesachen), § 1697a BGB (Kindeswohlprüfung), FamFG §§ 58 ff. (Besc... |
| `incoterms-und-gefahruebergang` | Incoterms-Klausel und Gefahruebergang in internationalem Kaufvertrag prüfen: Streit über Transportschaden oder Lieferpflicht. Normen: Incoterms 2020 (FOB, CIF, EXW, DAP, DDP), CISG Art. 31 und 67 ff. (Gefahruebergang). Prüfraster: Einsch... |
| `internationales-privatrecht` | Anwendbares Recht bei grenzüberschreitenden Vertraegen und Delikten bestimmen: Auslandsbezug im Prozess erfordert IPR-Prüfung. Normen: Rom-I-VO (vertragliche Schuldverhältnisse), Rom-II-VO (außervertragliche), Art. 4 ff. EGBGB (autonomes... |
| `kollidierende-agb-pruefen` | Kollidierende AGB im B2B-Verkehr (Battle of the Forms) lösen: Kaufvertrag mit beiderseitigen AGB und widerspruechen. Normen: §§ 305-310 BGB (AGB-Recht B2B), CISG Art. 19 (Annahme mit Abweichungen). Prüfraster: Last-Shot-Doctrine, Knock-o... |
| `kostenentscheidung-bauen` | Kostenentscheidung nach §§ 91 ff. ZPO erstellen: Richter muss Kostenquote und -grundentscheidung formulieren. Normen: § 91 ZPO (vollständiges Obsiegen), § 92 ZPO (teilweises Obsiegen), § 100 ZPO (mehrere Beklagte), § 101 ZPO (Streitgenos... |
| `rechtsmittelbelehrung-zivil` | Workflow-Skill zu rechtsmittelbelehrung zivil. Nutzt Normtext, Nutzerangaben und verifizierte Quellen; Rechtsprechung nur nach Live-Pruefung mit Gericht, Datum und Aktenzeichen. |
| `relation-zivil` | Zivilrechtliche Relation nach klassischer Relationstechnik erstellen: Referendar oder Richter erstellt Entscheidungsunterlage vor Urteilsabfassung. Normen: §§ 253 ff. und 286 und 313 ZPO. Prüfraster: Sachbericht, Streitgegenstand, Zuläss... |
| `revisionsfest-pruefen` | Prüfung gegen Aufhebung in der Revision: absolute Revisionsgründe Paragraf 547 ZPO Revisionszulassung Paragraf 543 ZPO grundsaetzliche Bedeutung Rechtsfortbildung Sicherung einheitlicher Rechtsprechung. Begründungstiefe Beweiswürdigung V... |
| `schulung-urteilsbauer` | Schulungs-Trainerleitfaden für Plugin urteilsbauer-relationsmacher: Ausbilder plant Schulungstag für Proberichter, Assessoren oder Rechtspfleger. Normen: §§ 313 und 286 und 529 ZPO (Lernziele). Prüfraster: Lernziele, Stundenplan (1 Tag o... |
| `tatbestand-zivil-schreiben` | Tatbestand eines Zivilurteils nach § 313 Abs. 2 ZPO schreiben: Richter muss den Prozessstoff sachlich und knapp wiedergeben. Normen: § 313 Abs. 2 ZPO (Tatbestand-Anforderungen), § 314 ZPO (Beweiskraft des Tatbestands). Prüfraster: Einlei... |
| `tenor-bauen-zivil` | Tenor eines Zivilurteils konstruieren: Richter muss Hauptsache-Entscheidung, Kosten und Vollstreckbarkeit klar tenorieren. Normen: §§ 91 ff. ZPO (Kosten), §§ 708-720a ZPO (vorlaeufige Vollstreckbarkeit), § 511 ZPO (Berufungszulassung), B... |
| `vollrelation-langfassung` | Vollständige Relation im Schulstandard für Referendar-/Assessorprüfung ausformulieren: Kandidat benoetigt Langfassung mit gutachterlichem Stil. Normen: §§ 253 ff. und 286 und 313 ZPO. Prüfraster: Sachbericht, Auslegung Streitgegenstand,... |
| `vorlaeufige-vollstreckbarkeit` | Anordnung zur vorlaeufigen Vollstreckbarkeit nach §§ 708-720a ZPO bestimmen: Richter muss die richtige Vollstreckbarkeitsermaechtigungs-Formel formulieren. Normen: § 709 ZPO (Sicherheitsleistung 110%), § 711 ZPO (Schutzantrag Schuldner),... |
| `zulaessigkeit-pruefen` | Zulässigkeit der Zivilklage systematisch prüfen: Richter oder Referendar prüft Prüfstation Zulässigkeit. Normen: § 13 GVG (Rechtsweg), EuGVVO Bruessel Ia (internationale Zuständigkeit), §§ 12 ff. ZPO (örtliche Zuständigkeit), § 23 GVG (s... |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
