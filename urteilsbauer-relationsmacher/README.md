# Urteilsbauer und Relationsmacher

Technischer Plugin-Name: `urteilsbauer-relationsmacher`.

Freistehendes Plugin fuer **Amts-, Land- und Familienrichter sowie Rechtspfleger**. Begleitet von der Aktenintake ueber die Relation und die Beweiswuerdigung mit Richter-Input bis zum fertigen Urteil oder Beschluss inklusive Tenor, Tatbestand, Entscheidungsgruenden, Kosten- und Rechtsmittelbelehrung. Erzeugt am Ende ein DOCX nach § 313 ZPO.

## Direkt-Download

| Plugin | Direkt-Download |
| --- | --- |
| urteilsbauer-relationsmacher | [urteilsbauer-relationsmacher.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/urteilsbauer-relationsmacher.zip) |

## Installation

1. Claude Code oder Claude Desktop/Cowork oeffnen.
2. **Customize Plugins** bzw. **Personal plugins** waehlen.
3. **Install from .zip** und `urteilsbauer-relationsmacher.zip` hochladen.
4. Mit einem konkreten Auftrag starten, zum Beispiel: `Starte die Relation fuer eine Werklohnklage. Akte liegt vor.`

Alternativ via Marketplace:

```
/plugin marketplace add Klotzkette/claude-fuer-deutsches-recht
/plugin install urteilsbauer-relationsmacher@claude-fuer-deutsches-recht
```

Nicht das komplette Repository-ZIP hochladen. Das Plugin-ZIP muss im Root direkt `.claude-plugin/plugin.json` und `skills/` enthalten.

## Testakten

- **Solis Vision X Smartglasses** (Produkthaftung und DSGVO bei smarter Brille, AG/LG-Zivil): [testakten/solis-vision-x-smartglasses/](../testakten/solis-vision-x-smartglasses/) -> [testakte-solis-vision-x-smartglasses.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-solis-vision-x-smartglasses.zip)
- **Schulungsakte Lumen Studios** (Insolvenz- und strafrechtliche Schnittstelle): [testakten/schulungsakte-lumen-studios-insolvenz-strafrecht/](../testakten/schulungsakte-lumen-studios-insolvenz-strafrecht/) -> [testakte-schulungsakte-lumen-studios-insolvenz-strafrecht.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-schulungsakte-lumen-studios-insolvenz-strafrecht.zip)

## Skill-Landkarte

| Skill | Zweck |
| --- | --- |
| `aktenintake-zivil` | Erfasst Parteien, Antraege, Sachverhalt, Streitwert, Anlagen und Lage. |
| `zulaessigkeit-pruefen` | Pruft Statthaftigkeit, Zustaendigkeit, Partei- und Prozessfaehigkeit, Rechtsschutzbeduerfnis. |
| `relation-zivil` | Baut Relation aus Klagegrund und Verteidigung mit Streitstand und Beweislage. |
| `vollrelation-langfassung` | Liefert die ausfuehrliche Vollrelation mit Hilfserwaegungen und Eventualbegruendung. |
| `anspruchsgrundlagen-pruefen` | Identifiziert und subsumiert die einschlaegigen Anspruchsgrundlagen. |
| `kollidierende-agb-pruefen` | Loest AGB-Konflikt nach Restguelitgkeits- und Knock-out-Doktrin. |
| `cisg-pruefen` | Pruft CISG-Anwendbarkeit, Anspruechs- und Aufrechnungslage. |
| `internationales-privatrecht` | Klaert anwendbares Recht nach Rom I/II und nationalem IPR. |
| `incoterms-und-gefahruebergang` | Wendet Incoterms 2020 auf Gefahruebergang und Transportkosten an. |
| `dsgvo-rechtswidriges-produkt` | Beurteilt DSGVO-Verstoesse durch Produkte mit Datenverarbeitung. |
| `familienrichter-spezifika` | Familienrechtliche Besonderheiten: FamFG-Verfahren, Anhoerungspflicht, Vergleichsdruck. |
| `beweisbeschluss-vorbereiten` | Formuliert Beweisthemen, Beweismittel und Beweisanordnung. |
| `beweiswuerdigung-mit-richter-input` | Holt Richter-Input zu Glaubwuerdigkeit ein und baut Beweiswuerdigung. |
| `tatbestand-zivil-schreiben` | Verfasst Tatbestand mit unstreitigem und streitigem Sachverhalt und Antraegen. |
| `entscheidungsgruende-zivil-schreiben` | Baut Entscheidungsgruende mit Subsumtion und juristischer Begruendung. |
| `tenor-bauen-zivil` | Erstellt Tenor mit Hauptsache, Kosten, vorlaeufiger Vollstreckbarkeit. |
| `kostenentscheidung-bauen` | Berechnet Kostenquote nach §§ 91 ff. ZPO inklusive Vergleichswerten. |
| `vorlaeufige-vollstreckbarkeit` | Setzt Sicherheitsleistung und Abwendungsbefugnis nach §§ 708 ff. ZPO. |
| `rechtsmittelbelehrung-zivil` | Erzeugt korrekte Rechtsmittelbelehrung fuer Berufung, Beschwerde, Revision. |
| `beschluss-bauen-zpo` | Baut Beschluesse statt Urteilen, etwa bei einstweiligem Rechtsschutz oder Streitwertfestsetzung. |
| `berufungsfest-pruefen` | Pruft das Urteil auf Berufungsfestigkeit und typische Aufhebungsgruende. |
| `revisionsfest-pruefen` | Pruft Urteil auf revisionsrechtliche Schwachstellen. |
| `dokumente-rendern-urteil-docx` | Rendert das fertige Urteil als DOCX nach § 313 ZPO. |
| `schulung-urteilsbauer` | Trainingsskill zur Einarbeitung neuer Richter und Rechtspfleger. |

## Typische Workflows

- Aktenintake -> Zulaessigkeit -> Relation -> Anspruchsgrundlagen -> Beweisbeschluss.
- Beweiswuerdigung mit Richter-Input -> Tatbestand -> Entscheidungsgruende -> Tenor.
- Kostenentscheidung -> Vorlaeufige Vollstreckbarkeit -> Rechtsmittelbelehrung.
- Berufungs-/Revisionsfestigkeit -> DOCX-Rendering nach § 313 ZPO.

## Haftung

Dieses Plugin ist ein Arbeitswerkzeug fuer die richterliche Praxis. Es ersetzt keine eigene rechtliche Pruefung und keine Beratung durch zugelassene Rechtsanwaelte. Die Verantwortung fuer Tenor, Tatbestand und Entscheidungsgruende bleibt beim Spruchkoerper.
