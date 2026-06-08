# Fachanwalt Insolvenz- und Sanierungsrecht

<!-- BEGIN plugin-sofort-download-section (autogen) -->
## ⬇️ Sofort-Downloads

Direkt-Downloads ohne Umwege. Die URLs sind stabil und zeigen immer auf die aktuelle Version (`latest`-Release).

### Plugin als ZIP

| Inhalt | Download |
| --- | --- |
| **Dieses Plugin** (`fachanwalt-insolvenz-sanierungsrecht`) | [`fachanwalt-insolvenz-sanierungsrecht.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/fachanwalt-insolvenz-sanierungsrecht.zip) |

### Demonstrations-Akten

| Akte | PDF lesen | Akten-ZIP |
| --- | --- | --- |
| **Großbach Druckguss & Präzision GmbH & Co. KG — Schutzschirm und StaRUG-Optionen** (`starug-schutzschirm-grossbach-druckguss-erfurt`) | [Gesamt-PDF lesen](../testakten/starug-schutzschirm-grossbach-druckguss-erfurt/gesamt-pdf/starug-schutzschirm-grossbach-druckguss-erfurt_gesamt.pdf) | [`testakte-starug-schutzschirm-grossbach-druckguss-erfurt.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-starug-schutzschirm-grossbach-druckguss-erfurt.zip) |

<!-- END plugin-sofort-download-section (autogen) -->

Plugin Fachanwalt für Insolvenz- und Sanierungsrecht nach FAO § 14 (idF nach Aufnahme StaRUG-Bereiche). Orientierung, Gläubigerantrag, Restrukturierungsplan StaRUG, Insolvenzanfechtung. Schnittstellen zum Plugin `insolvenzrecht` (operativ) und `steuerrecht-anwalt-und-berater`.

## InsO-Paragraphen-Navigator

Dieses Plugin enthält nun zu jedem aktuell im amtlichen InsO-Wortlaut geführten Paragraphen einen eigenen `inso-p...`-Skill. Der Navigator ist für die tägliche Fachanwaltsarbeit gedacht: Er führt nicht abstrakt durch die Insolvenzordnung, sondern fragt pro Norm nach Rolle, Verfahrensstand, Belegen, Fristen, Rechtsfolge, Gegenargumenten und dem nächsten verwertbaren Arbeitsergebnis.

Besonders hilfreich ist das bei Akten, in denen viele Ebenen gleichzeitig laufen: Eröffnungsantrag, Sicherungsmaßnahmen, Massezuordnung, Anfechtung, Forderungsprüfung, Insolvenzplan, Eigenverwaltung, Verbraucherinsolvenz, Nachlassinsolvenz oder internationales Insolvenzrecht. Weggefallene Vorschriften sind bewusst als Altfassungs- und Übergangsrechtsanker enthalten, damit alte Akten und ältere Rechtsprechung nicht versehentlich auf heutige Fälle übertragen werden.

Vor verbindlichen Aussagen prüft der jeweilige Skill den aktuellen Gesetzeswortlaut und verlangt für Rechtsprechung Gericht, Datum, Aktenzeichen und möglichst eine frei zugängliche amtliche oder gerichtliche Quelle. Literatur- und Datenbankfundstellen werden nicht aus Modellwissen behauptet.

## Installation in Claude Code

1. ZIP herunterladen (Link oben).
2. Claude Code → **Customize Plugins** → **Install from .zip** → Datei wählen.
3. Fertig.

## Enthaltene Skills

| Skill | Zweck |
| --- | --- |
| `fachanwalt-insolvenz-sanierungsrecht-orientierung` | FAO § 14, InsO, StaRUG, EuInsVO, Quellenprüfung. |
| `fachanwalt-insolvenz-sanierungsrecht-glaeubigerantrag` | Gläubigerantrag § 14 InsO, Forderungs- und Insolvenzgrundsglaubhaftmachung. |
| `fachanwalt-insolvenz-sanierungsrecht-restrukturierungsplan` | Restrukturierungsplan StaRUG, Gruppenbildung, gerichtliche Planbestätigung. |
| `fachanwalt-insolvenz-sanierungsrecht-insolvenzanfechtung` | Anfechtungstatbestände §§ 129 ff. InsO (Schenkungs-, Vorsatz-, Deckungsanfechtung). |
| `inso-p001-...` bis `inso-p359-...` | Paragraphen-Navigator zur aktuellen Insolvenzordnung: pro InsO-Norm ein eigener Workflow mit Beleg-, Fristen-, Risiko- und Quellenprüfung. |

## Lizenz

Apache-2.0 OR MIT — Auswahl beim Empfänger.


<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Ueberblick

Automatisch generierte Komplett-Liste aller 55 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `absonderungsrecht-paragraf-50-inso` | Absonderungsrecht § 50 InsO: fachanwaltlicher Spezial-Skill mit Normenanker, Tatsachenmatrix, Beweislast, Fristen, Gegenargumenten und belastbarem Arbeitsprodukt; ohne ungeprüfte Aktenzeichen. |
| `anfechtung-vorsatz-paragraf-133-inso-bgh-ix-zr-65-16` | Vorsatzanfechtung Paragraf 133 InsO mit BGH IX ZR 65/16. |
| `anschluss-routing` | Anschluss-Routing: Einstieg und Routing; klärt Rolle, Ziel, Frist, Aktenlage und den passenden nächsten Fachpfad. |
| `dokumente-intake` | Dokumentenintake: sortiert Dokumente, erkennt Lücken, ordnet Beweiswert und formuliert gezielte Rückfragen. |
| `eigenverwaltung-schutzschirm-paragraf-270b-inso` | Eigenverwaltung Schutzschirm § 270b InsO: fachanwaltlicher Spezial-Skill mit Normenanker, Tatsachenmatrix, Beweislast, Fristen, Gegenargumenten und belastbarem Arbeitsprodukt; ohne ungeprüfte Aktenzeichen. |
| `einstieg-routing` | Einstieg und Routing: Einstieg und Routing; klärt Rolle, Ziel, Frist, Aktenlage und den passenden nächsten Fachpfad. |
| `eroeffnung-fachanwalt-fao-glaeubigerantrag` | Eroeffnung Fachanwalt FAO Glaeubigerantrag im Insolvenz- und Sanierungsrecht: prüft konkret Eroeffnung, Fachanwalt, FAO, Glaeubigerantrag. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Schritt. |
| `fa-inso-sanierung-quellen-edge-case` | Rechtsquellen: Sonderfall und Edge-Case-Prüfung im Insolvenz- und Sanierungsrecht: fachlich vertieftes Modul mit Normenradar (InsO/StaRUG/IDW-S6), Tatbestands-/Beweislastmatrix, Fristen- und Formcheck, Gegenargumenten, Fehlerbremse und d... |
| `fa-schuldschein` | FA Schuldschein im Insolvenz- und Sanierungsrecht im Fachanwalt Insolvenz Sanierungsrecht: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung. Liefert priorisierten Output mit Norm-Pinpoints, Risikoam... |
| `glaeubigerantrag-insolvenzanfechtung` | Glaeubigerantrag Insolvenzanfechtung im Insolvenz- und Sanierungsrecht: prüft konkrete Prüfungslinie für fachanwalt insolvenz sanierungsrecht, Insolvenzanfechtung nach §§ 129-147 InsO fachanwaltlich, Orientierung im Insolvenz- und Sanier... |
| `glaeubigerverhandlung-sanierung-idw-s6-krypto` | Glaeubigerverhandlung Sanierung IDW S6 Krypto im Insolvenz- und Sanierungsrecht: prüft konkret Sanierungs-Verhandlung mit Gläubigern vor und in der, Erstellt und prüft Sanierungskonzepte auf IDW-S-6-Niveau, Prüfungslinie für fachanwalt i... |
| `insanw-eigenverwaltung-konzerninsolvenz` | Inso Insanw Eigenverwaltung Konzerninsolvenz im Insolvenz- und Sanierungsrecht: prüft konkret Spezialfall Eigenverwaltung und Schutzschirmverfahren §§, Spezialfall Konzerninsolvenz §§ 3a ff, Spezialfall Insolvenzanfechtung Zahlungsstrom... |
| `insanw-fortbestehensprognose` | Insanw Fortbestehensprognose im Insolvenz- und Sanierungsrecht: prüft konkret Einstieg, Schnelltriage und Fallrouting im Fachanwalt Insolvenz, Fortbestehensprognose IDW S 11 / S 6, Chronologie und Belegmatrix im Plugin. Liefert priorisie... |
| `insolvenz-insolvenzanfechtung-insolvenzrecht` | Insolvenzanfechtung Insolvenzrecht im Insolvenz- und Sanierungsrecht: prüft konkret Insolvenz, Insolvenzanfechtung, Insolvenzrecht, Krypto. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Schritt. |
| `insolvenzgeld-paragraf-165-sgb-iii` | Insolvenzgeld § 165 sgb iii: fachanwaltlicher Spezial-Skill mit Normenanker, Tatsachenmatrix, Beweislast, Fristen, Gegenargumenten und belastbarem Arbeitsprodukt; ohne ungeprüfte Aktenzeichen. |
| `insolvenzplan-paragraf-217-inso-bgh-ix-zb-66-19` | Insolvenzplan Paragraf 217 InsO mit BGH IX ZB 66/19. |
| `interessen-verwertung-beweislast-starug` | Interessen Verwertung Beweislast Starug im Insolvenz- und Sanierungsrecht: prüft konkret Schnittstellen, Verwertung, StaRUG-Restrukturierungsplan im Detail, Prüft Anfechtungsansprüche und Verteidigungslinien nach §§. Liefert priorisierte... |
| `kommunikation-glaeubiger-p002` | Inso Kommunikation Glaeubiger P002 im Insolvenz- und Sanierungsrecht: prüft konkret Kommunikation mit Glaeubigern im Insolvenz- und, § 2 InsO (Amtsgericht als Insolvenzgericht) im Mandat prüfen, § 3 InsO (Örtliche Zuständigkeit) im Manda... |
| `livecheck-fristennotiz-sanierungsrecht` | Inso Livecheck Fristennotiz Sanierungsrecht im Insolvenz- und Sanierungsrecht: prüft konkret Livecheck, Sanierungsrecht, § 104 InsO (Fixgeschäfte, Finanzleistungen. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächste... |
| `masseunzulaenglichkeit-paragraf-208-inso` | Masseunzulaenglichkeit § 208 InsO: fachanwaltlicher Spezial-Skill mit Normenanker, Tatsachenmatrix, Beweislast, Fristen, Gegenargumenten und belastbarem Arbeitsprodukt; ohne ungeprüfte Aktenzeichen. |
| `output-waehlen` | Output wählen im Insolvenz- und Sanierungsrecht: Diese Output-Weiche für Fachanwalt Insolvenz Sanierungsrecht entscheidet, ob Memo, Antrag, Schriftsatz, Tabelle, Risikoampel, Fragenliste oder Mandantenbrief der richtige nächste Schritt ist. |
| `p001-ziele-p003c-zustandigkeit-p004a` | Inso P001 Ziele P003c Zustandigkeit P004a im Insolvenz- und Sanierungsrecht: prüft konkret § 1 InsO (Ziele des Insolvenzverfahrens) im Mandat prüfen, § 3c InsO (Zuständigkeit für Gruppen-Folgeverfahren) im, § 4a InsO (Stundung der Kosten... |
| `p003d` | Inso P003d im Insolvenz- und Sanierungsrecht im Fachanwalt Insolvenz Sanierungsrecht: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel u... |
| `p003e-unternehmensgruppe-p004b` | Inso P003e Unternehmensgruppe P004b im Insolvenz- und Sanierungsrecht: prüft konkret § 3e InsO (Unternehmensgruppe) im Mandat prüfen, § 4b InsO (Rückzahlung und Anpassung der gestundeten, § 4c InsO (Aufhebung der Stundung) im Mandat prüf... |
| `p004-anwendbarkeit-p036-unpfandbare` | Inso P004 Anwendbarkeit P036 Unpfandbare im Insolvenz- und Sanierungsrecht: prüft konkret Red-Team Qualitygate im Plugin, § 4 InsO (Anwendbarkeit der Zivilprozeßordnung) im Mandat, § 36 InsO (Unpfändbare Gegenstände) im Mandat prüfen, Sc... |
| `p020-auskunfts-p021-anordnung-p022` | Inso P020 Auskunfts P021 Anordnung P022 im Insolvenz- und Sanierungsrecht: prüft konkret § 20 InsO (Auskunfts- und Mitwirkungspflicht im, § 21 InsO (Anordnung vorläufiger Maßnahmen) im Mandat prüfen, § 22 InsO (Rechtsstellung des vorläuf... |
| `p040-unterhaltsanspruche-p041-nicht-p042` | Inso P040 Unterhaltsanspruche P041 Nicht P042 im Insolvenz- und Sanierungsrecht: prüft konkret § 40 InsO (Unterhaltsansprüche) im Mandat prüfen, § 41 InsO (Nicht fällige Forderungen) im Mandat prüfen, § 42 InsO (Auflösend bedingte Forder... |
| `p054-kosten-p088-vollstreckung-p095` | Inso P054 Kosten P088 Vollstreckung P095 im Insolvenz- und Sanierungsrecht: prüft konkret § 54 InsO (Kosten des Insolvenzverfahrens) im Mandat prüfen, § 88 InsO (Vollstreckung vor Verfahrenseröffnung) im Mandat, § 95 InsO (Eintritt der A... |
| `p061-nichterfullung-p062-verjahrung-p063` | Inso P061 Nichterfullung P062 Verjahrung P063 im Insolvenz- und Sanierungsrecht: prüft konkret § 61 InsO (Nichterfüllung von Masseverbindlichkeiten) im, § 62 InsO (Verjährung) im Mandat prüfen, § 63 InsO (Vergütung des Insolvenzverwalter... |
| `p083-erbschaft-p084-auseinandersetzung` | Inso P083 Erbschaft P084 Auseinandersetzung im Insolvenz- und Sanierungsrecht: prüft konkret § 83 InsO (Erbschaft, § 84 InsO (Auseinandersetzung einer Gesellschaft oder, § 85 InsO (Aufnahme von Aktivprozessen) im Mandat prüfen, § 86 InsO... |
| `p092-gesamtschaden-p093-personliche-p227` | Inso P092 Gesamtschaden P093 Personliche P227 im Insolvenz- und Sanierungsrecht: prüft konkret § 92 InsO (Gesamtschaden) im Mandat prüfen, § 93 InsO (Persönliche Haftung der Gesellschafter) im, § 227 InsO (Haftung des Schuldners) im Mand... |
| `p109-schuldner-p110-p111-verausserung` | Inso P109 Schuldner P110 P111 Verausserung im Insolvenz- und Sanierungsrecht: prüft konkret § 109 InsO (Schuldner als Mieter oder Pächter) im Mandat, § 110 InsO (Schuldner als Vermieter oder Verpächter) im, § 111 InsO (Veräußerung des Mi... |
| `p126` | Inso P126 im Insolvenz- und Sanierungsrecht im Fachanwalt Insolvenz Sanierungsrecht: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel un... |
| `p134-unentgeltliche-p135` | Inso P134 Unentgeltliche P135 im Insolvenz- und Sanierungsrecht: prüft konkret § 134 InsO (Unentgeltliche Leistung) im Mandat prüfen, § 135 InsO (Gesellschafterdarlehen) im Mandat prüfen, § 136 InsO (Stille Gesellschaft) im Mandat prüfen... |
| `p139-eroffnungsantrag-p147` | Inso P139 Eroffnungsantrag P147 im Insolvenz- und Sanierungsrecht: prüft konkret § 139 InsO (Berechnung der Fristen vor dem, § 147 InsO (Rechtshandlungen nach Verfahrenseröffnung) im, § 157 InsO (Entscheidung über den Fortgang des Verfah... |
| `p155-steuerrecht-erstgespraech` | Inso P155 Steuerrecht Erstgespraech im Insolvenz- und Sanierungsrecht: prüft konkret § 155 InsO (Handels- und steuerrechtliche Rechnungslegung), Steuerrecht, Strukturierter Erstgespraechsleitfaden für Insolvenz- und, Fachanwaltlicher Fac... |
| `p159-verwertung-p160-besonders-p161` | Inso P159 Verwertung P160 Besonders P161 im Insolvenz- und Sanierungsrecht: prüft konkret § 159 InsO (Verwertung der Insolvenzmasse) im Mandat prüfen, § 160 InsO (Besonders bedeutsame Rechtshandlungen) im, § 161 InsO (Vorläufige Untersag... |
| `p180-zustandigkeit-p181-umfang-p182` | Inso P180 Zustandigkeit P181 Umfang P182 im Insolvenz- und Sanierungsrecht: prüft konkret § 180 InsO (Zuständigkeit für die Feststellung) im Mandat, § 181 InsO (Umfang der Feststellung) im Mandat prüfen, § 182 InsO (Streitwert) im Mandat... |
| `p203-anordnung-p204-rechtsmittel-p205` | Inso P203 Anordnung P204 Rechtsmittel P205 im Insolvenz- und Sanierungsrecht: prüft konkret § 203 InsO (Anordnung der Nachtragsverteilung) im Mandat, § 204 InsO (Rechtsmittel) im Mandat prüfen, § 205 InsO (Vollzug der Nachtragsverteilung... |
| `p223a-gruppeninterne-p224-rechte-p225` | Inso P223a Gruppeninterne P224 Rechte P225 im Insolvenz- und Sanierungsrecht: prüft konkret § 223a InsO (Gruppeninterne Drittsicherheiten) im Mandat, § 224 InsO (Rechte der Insolvenzgläubiger) im Mandat prüfen, § 225 InsO (Rechte der nac... |
| `p242-schriftliche-p243-abstimmung-p244` | Inso P242 Schriftliche P243 Abstimmung P244 im Insolvenz- und Sanierungsrecht: prüft konkret § 242 InsO (Schriftliche Abstimmung) im Mandat prüfen, § 243 InsO (Abstimmung in Gruppen) im Mandat prüfen, § 244 InsO (Erforderliche Mehrheiten... |
| `p260-uberwachung-p261-aufgaben-p262` | Inso P260 Uberwachung P261 Aufgaben P262 im Insolvenz- und Sanierungsrecht: prüft konkret § 260 InsO (Überwachung der Planerfüllung) im Mandat prüfen, § 261 InsO (Aufgaben und Befugnisse des, § 262 InsO (Anzeigepflicht des Insolvenzverwa... |
| `p270f-anordnung-p270g-eigenverwaltung` | Inso P270f Anordnung P270g Eigenverwaltung im Insolvenz- und Sanierungsrecht: prüft konkret § 270f InsO (Anordnung der Eigenverwaltung) im Mandat prüfen, § 270g InsO (Eigenverwaltung bei gruppenangehörigen, § 271 InsO (Nachträgliche Anor... |
| `p279-gegenseitige-p336-vertrag-p043` | Inso P279 Gegenseitige P336 Vertrag P043 im Insolvenz- und Sanierungsrecht: prüft konkret § 279 InsO (Gegenseitige Verträge) im Mandat prüfen, § 336 InsO (Vertrag über einen unbeweglichen Gegenstand) im, § 43 InsO (Haftung mehrerer Perso... |
| `p290-versagung-p291-weggefallen-p292` | Inso P290 Versagung P291 Weggefallen P292 im Insolvenz- und Sanierungsrecht: prüft konkret § 290 InsO (Versagung der Restschuldbefreiung) im Mandat, § 291 InsO ist im aktuellen Normtext weggefallen, Altakten, Übe. Liefert priorisierten O... |
| `p308-annahme-p309-ersetzung-p310-kosten` | Inso P308 Annahme P309 Ersetzung P310 Kosten im Insolvenz- und Sanierungsrecht: prüft konkret § 308 InsO (Annahme des Schuldenbereinigungsplans) im, § 309 InsO (Ersetzung der Zustimmung) im Mandat prüfen, § 310 InsO (Kosten) im Mandat pr... |
| `p335-grundsatz-p337-arbeitsverhaltnis` | Inso P335 Grundsatz P337 Arbeitsverhaltnis im Insolvenz- und Sanierungsrecht: prüft konkret § 335 InsO (Grundsatz) im Mandat prüfen, § 337 InsO (Arbeitsverhältnis) im Mandat prüfen, § 338 InsO (Aufrechnung) im Mandat prüfen, § 339 InsO (... |
| `p359-schriftsatzkern-substantiierung` | Inso P359 Schriftsatzkern Substantiierung im Insolvenz- und Sanierungsrecht: prüft konkret § 359 InsO (Verweisung auf das Einführungsgesetz) im Mandat, Substantiierter Schriftsatzkern für Insolvenzantrag, Anfechtungsklage, StaRUG-Re. Lie... |
| `quellen-livecheck` | Rechtsquellen-Livecheck: Quellenprüfung; Normenstand, Rechtsprechung, Behördenpraxis und Zitierfähigkeit werden vor einer tragenden Aussage verifiziert. |
| `restschuldbefreiung-paragraf-287-inso-bgh-ix-zb-25-18` | Restschuldbefreiung Verkuerzte Verfahrensdauer Paragraf 287 InsO. |
| `scheme-of-arrangement` | Scheme of Arrangement: fachanwaltlicher Spezial-Skill mit Normenanker, Tatsachenmatrix, Beweislast, Fristen, Gegenargumenten und belastbarem Arbeitsprodukt; ohne ungeprüfte Aktenzeichen. |
| `starug-quellenkarte` | Starug Quellenkarte: Quellenprüfung; Normenstand, Rechtsprechung, Behördenpraxis und Zitierfähigkeit werden vor einer tragenden Aussage verifiziert. |
| `ueberschuldung-paragraf-19-inso-bgh-ii-zr-129-16` | Ueberschuldung Paragraf 19 InsO mit BGH II ZR 129/16. |
| `unterlagen-luecken` | Unterlagen und Lücken: sortiert Dokumente, erkennt Lücken, ordnet Beweiswert und formuliert gezielte Rückfragen. |
| `zahlungsunfaehigkeit-paragraf-17-inso-bgh-ix-zb-25-17` | Zahlungsunfaehigkeit Paragraf 17 InsO mit BGH IX ZB 25/17. |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
