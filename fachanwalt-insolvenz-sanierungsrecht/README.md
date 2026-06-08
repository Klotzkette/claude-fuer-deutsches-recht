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
| `anfechtung-vorsatz-paragraf-133-inso-bgh-ix-zr-65-16` | Anfechtung Vorsatz Paragraf 133 InsO BGH Ix Zr 65 16: fachanwaltlicher Spezialskill mit Normenanker, Fristen-/Zustaendigkeitscheck, Beweisfragen, Rechtsprechungshygiene und direkt nutzbarem Arbeitsprodukt. |
| `anschluss-routing` | Anschluss-Routing für Fachanwalt Insolvenz- und Sanierungsrecht: wählt den nächsten Spezial-Skill nach Engpass (§ 15a InsO 3 Wochen Antragspflicht, Insolvenzantrag, Sanierungskonzept IDW S6, Plan), dokumentiert Router-Entscheidung mit Be... |
| `dokumente-intake` | Dokumentenintake für Fachanwalt Insolvenz- und Sanierungsrecht: sortiert Insolvenzantrag, Sanierungskonzept IDW S6, Plan, prüft Datum, Absender, Frist und Beweiswert (Bilanz, Liquiditätsplan); markiert Lücken; berücksichtigt Mandatsgehei... |
| `eigenverwaltung-schutzschirm-paragraf-270b-inso` | Eigenverwaltung Schutzschirm § 270b InsO: fachanwaltlicher Spezial-Skill mit Normenanker, Tatsachenmatrix, Beweislast, Fristen, Gegenargumenten und belastbarem Arbeitsprodukt; ohne ungeprüfte Aktenzeichen. |
| `einstieg-routing` | Einstieg, Triage und Routing für Fachanwalt Insolvenz- und Sanierungsrecht: ordnet Rolle (Schuldnerunternehmen, Geschäftsführung (Haftung!), Insolvenzverwalter), markiert Frist (§ 15a InsO 3 Wochen Antragspflicht), wählt Norm (InsO, StaR... |
| `eroeffnung-fachanwalt-fao-glaeubigerantrag` | Eroeffnung Fachanwalt FAO Glaeubigerantrag im Insolvenz- und Sanierungsrecht: prüft konkret Eroeffnung, Fachanwalt, FAO, Glaeubigerantrag. |
| `fa-inso-sanierung-quellen-edge-case` | Rechtsquellen: Sonderfall und Edge-Case-Prüfung im Insolvenz- und Sanierungsrecht: fachlich vertieftes Modul mit Normenradar (InsO/StaRUG/IDW-S6), Tatbestands-/Beweislastmatrix, Fristen- und Formcheck, Gegenargumenten, Fehlerbremse und d... |
| `fa-schuldschein` | FA Schuldschein im Insolvenz- und Sanierungsrecht im Fachanwalt Insolvenz Sanierungsrecht. |
| `glaeubigerantrag-insolvenzanfechtung` | Glaeubigerantrag Insolvenzanfechtung im Insolvenz- und Sanierungsrecht: prüft konkrete Prüfungslinie für fachanwalt insolvenz sanierungsrecht, Insolvenzanfechtung nach §§ 129-147 InsO fachanwaltlich, Orientierung im Insolvenz- und Sanier... |
| `glaeubigerverhandlung-sanierung-idw-s6-krypto` | Glaeubigerverhandlung Sanierung IDW S6 Krypto im Insolvenz- und Sanierungsrecht: prüft konkret Sanierungs-Verhandlung mit Gläubigern vor und in der, Erstellt und prüft Sanierungskonzepte auf IDW-S-6-Niveau, Prüfungslinie für fachanwalt i... |
| `insanw-eigenverwaltung-konzerninsolvenz` | Inso Insanw Eigenverwaltung Konzerninsolvenz im Insolvenz- und Sanierungsrecht: prüft konkret Spezialfall Eigenverwaltung und Schutzschirmverfahren §§, Spezialfall Konzerninsolvenz §§ 3a ff, Spezialfall Insolvenzanfechtung Zahlungsstrom... |
| `insanw-fortbestehensprognose` | Insanw Fortbestehensprognose im Insolvenz- und Sanierungsrecht: prüft konkret Einstieg, Schnelltriage und Fallrouting im Fachanwalt Insolvenz, Fortbestehensprognose IDW S 11 / S 6, Chronologie und Belegmatrix im Plugin. |
| `inso-1-ziele-3c-zustaendigkeit-4a` | Inso P001 Ziele P003c Zustandigkeit P004a im Insolvenz- und Sanierungsrecht: prüft konkret § 1 InsO (Ziele des Insolvenzverfahrens) im Mandat prüfen, § 3c InsO (Zuständigkeit für Gruppen-Folgeverfahren) im, § 4a InsO (Stundung der Kosten... |
| `inso-109-110-111-veraeusserung` | Inso P109 Schuldner P110 P111 Verausserung im Insolvenz- und Sanierungsrecht: prüft konkret § 109 InsO (Schuldner als Mieter oder Pächter) im Mandat, § 110 InsO (Schuldner als Vermieter oder Verpächter) im, § 111 InsO (Veräußerung des Mi... |
| `inso-126-pruefungstermin` | Inso P126 im Insolvenz- und Sanierungsrecht im Fachanwalt Insolvenz Sanierungsrecht. |
| `inso-134-135-unentgeltliche-leistung` | Inso P134 Unentgeltliche P135 im Insolvenz- und Sanierungsrecht: prüft konkret § 134 InsO (Unentgeltliche Leistung) im Mandat prüfen, § 135 InsO (Gesellschafterdarlehen) im Mandat prüfen, § 136 InsO (Stille Gesellschaft) im Mandat prüfen... |
| `inso-139-147-eroeffnungsantrag` | Inso P139 Eroffnungsantrag P147 im Insolvenz- und Sanierungsrecht: prüft konkret § 139 InsO Berechnung der Fristen vor dem, § 147 InsO Rechtshandlungen nach Verfahrenseröffnung im, § 157 InsO Entscheidung über den Fortgang des Verfahrens... |
| `inso-155-steuerrecht-erstgespraech` | Inso P155 Steuerrecht Erstgespraech im Insolvenz- und Sanierungsrecht: prüft konkret § 155 InsO (Handels- und steuerrechtliche Rechnungslegung), Steuerrecht, Strukturierter Erstgespraechsleitfaden für Insolvenz- und, Fachanwaltlicher Fac... |
| `inso-159-160-161-verwertung` | Inso P159 Verwertung P160 Besonders P161 im Insolvenz- und Sanierungsrecht: prüft konkret § 159 InsO (Verwertung der Insolvenzmasse) im Mandat prüfen, § 160 InsO (Besonders bedeutsame Rechtshandlungen) im, § 161 InsO (Vorläufige Untersag... |
| `inso-180-181-182-anfechtung` | Inso P180 Zustandigkeit P181 Umfang P182 im Insolvenz- und Sanierungsrecht: prüft konkret § 180 InsO (Zuständigkeit für die Feststellung) im Mandat, § 181 InsO (Umfang der Feststellung) im Mandat prüfen, § 182 InsO (Streitwert) im Mandat... |
| `inso-20-auskunft-21-anordnung-22` | Inso P020 Auskunfts P021 Anordnung P022 im Insolvenz- und Sanierungsrecht: prüft konkret § 20 InsO Auskunfts- und Mitwirkungspflicht im, § 21 InsO Anordnung vorläufiger Maßnahmen im Mandat prüfen, § 22 InsO Rechtsstellung des vorläufigen... |
| `inso-203-204-205-anordnung` | Inso P203 Anordnung P204 Rechtsmittel P205 im Insolvenz- und Sanierungsrecht: prüft konkret § 203 InsO (Anordnung der Nachtragsverteilung) im Mandat, § 204 InsO (Rechtsmittel) im Mandat prüfen, § 205 InsO (Vollzug der Nachtragsverteilung... |
| `inso-223a-224-225-gruppe` | Inso P223a Gruppeninterne P224 Rechte P225 im Insolvenz- und Sanierungsrecht: prüft konkret § 223a InsO (Gruppeninterne Drittsicherheiten) im Mandat, § 224 InsO (Rechte der Insolvenzgläubiger) im Mandat prüfen, § 225 InsO (Rechte der nac... |
| `inso-242-243-244-abstimmung` | Inso P242 Schriftliche P243 Abstimmung P244 im Insolvenz- und Sanierungsrecht: prüft konkret § 242 InsO (Schriftliche Abstimmung) im Mandat prüfen, § 243 InsO (Abstimmung in Gruppen) im Mandat prüfen, § 244 InsO (Erforderliche Mehrheiten... |
| `inso-260-261-262-ueberwachung` | Inso P260 Uberwachung P261 Aufgaben P262 im Insolvenz- und Sanierungsrecht: prüft konkret § 260 InsO Überwachung der Planerfüllung im Mandat prüfen, § 261 InsO Aufgaben und Befugnisse des, § 262 InsO Anzeigepflicht des Insolvenzverwalter... |
| `inso-270f-270g-eigenverwaltung` | Inso P270f Anordnung P270g Eigenverwaltung im Insolvenz- und Sanierungsrecht: prüft konkret § 270f InsO Anordnung der Eigenverwaltung im Mandat prüfen, § 270g InsO Eigenverwaltung bei gruppenangehörigen, § 271 InsO Nachträgliche Anordnun... |
| `inso-279-336-43-vertraege` | Inso P279 Gegenseitige P336 Vertrag P043 im Insolvenz- und Sanierungsrecht: prüft konkret § 279 InsO (Gegenseitige Verträge) im Mandat prüfen, § 336 InsO (Vertrag über einen unbeweglichen Gegenstand) im, § 43 InsO (Haftung mehrerer Perso... |
| `inso-290-291-292-versagung-rsb` | Inso P290 Versagung P291 Weggefallen P292 im Insolvenz- und Sanierungsrecht: prüft konkret § 290 InsO (Versagung der Restschuldbefreiung) im Mandat, § 291 InsO ist im aktuellen Normtext weggefallen, Altakten, Übe. |
| `inso-308-309-310-plan-annahme` | Inso P308 Annahme P309 Ersetzung P310 Kosten im Insolvenz- und Sanierungsrecht: prüft konkret § 308 InsO (Annahme des Schuldenbereinigungsplans) im, § 309 InsO (Ersetzung der Zustimmung) im Mandat prüfen, § 310 InsO (Kosten) im Mandat pr... |
| `inso-335-337-arbeitsverhaeltnis` | Inso P335 Grundsatz P337 Arbeitsverhaltnis im Insolvenz- und Sanierungsrecht: prüft konkret § 335 InsO (Grundsatz) im Mandat prüfen, § 337 InsO (Arbeitsverhältnis) im Mandat prüfen, § 338 InsO (Aufrechnung) im Mandat prüfen, § 339 InsO (... |
| `inso-359-schriftsatzkern` | Inso P359 Schriftsatzkern Substantiierung im Insolvenz- und Sanierungsrecht: prüft konkret § 359 InsO (Verweisung auf das Einführungsgesetz) im Mandat, Substantiierter Schriftsatzkern für Insolvenzantrag, Anfechtungsklage, StaRUG-Re. |
| `inso-3d-gruppen-gerichtsstand` | Inso P003d im Insolvenz- und Sanierungsrecht im Fachanwalt Insolvenz Sanierungsrecht. |
| `inso-3e-unternehmensgruppe-4b` | Inso P003e Unternehmensgruppe P004b im Insolvenz- und Sanierungsrecht: prüft konkret § 3e InsO Unternehmensgruppe im Mandat prüfen, § 4b InsO Rückzahlung und Anpassung der gestundeten, § 4c InsO Aufhebung der Stundung im Mandat prüfen, §... |
| `inso-4-anwendbarkeit-36-unpfaendbare` | Inso P004 Anwendbarkeit P036 Unpfandbare im Insolvenz- und Sanierungsrecht: prüft konkret Red-Team Qualitygate im Plugin, § 4 InsO (Anwendbarkeit der Zivilprozeßordnung) im Mandat, § 36 InsO (Unpfändbare Gegenstände) im Mandat prüfen, Sc... |
| `inso-40-unterhalt-41-nicht-42` | Inso P040 Unterhaltsanspruche P041 Nicht P042 im Insolvenz- und Sanierungsrecht: prüft konkret § 40 InsO (Unterhaltsansprüche) im Mandat prüfen, § 41 InsO (Nicht fällige Forderungen) im Mandat prüfen, § 42 InsO (Auflösend bedingte Forder... |
| `inso-54-kosten-88-vollstreckung-95` | Inso P054 Kosten P088 Vollstreckung P095 im Insolvenz- und Sanierungsrecht: prüft konkret § 54 InsO (Kosten des Insolvenzverfahrens) im Mandat prüfen, § 88 InsO (Vollstreckung vor Verfahrenseröffnung) im Mandat, § 95 InsO (Eintritt der A... |
| `inso-61-63-erfuellung-verjaehrung` | Inso P061 Nichterfullung P062 Verjahrung P063 im Insolvenz- und Sanierungsrecht: prüft konkret § 61 InsO (Nichterfüllung von Masseverbindlichkeiten) im, § 62 InsO (Verjährung) im Mandat prüfen, § 63 InsO (Vergütung des Insolvenzverwalter... |
| `inso-83-84-erbschaft-auseinandersetzung` | Inso P083 Erbschaft P084 Auseinandersetzung im Insolvenz- und Sanierungsrecht: prüft konkret § 83 InsO Erbschaft, § 84 InsO Auseinandersetzung einer Gesellschaft oder, § 85 InsO Aufnahme von Aktivprozessen im Mandat prüfen, § 86 InsO Auf... |
| `inso-92-93-227-haftung-gesamtschaden` | Inso P092 Gesamtschaden P093 Personliche P227 im Insolvenz- und Sanierungsrecht: prüft konkret § 92 InsO Gesamtschaden im Mandat prüfen, § 93 InsO Persönliche Haftung der Gesellschafter im, § 227 InsO Haftung des Schuldners im Mandat prü... |
| `insolvenz-insolvenzanfechtung-insolvenzrecht` | Insolvenzanfechtung Insolvenzrecht im Insolvenz- und Sanierungsrecht: prüft konkret Insolvenz, Insolvenzanfechtung, Insolvenzrecht, Krypto. |
| `insolvenzgeld-paragraf-165-sgb-iii` | Insolvenzgeld § 165 sgb iii: fachanwaltlicher Spezial-Skill mit Normenanker, Tatsachenmatrix, Beweislast, Fristen, Gegenargumenten und belastbarem Arbeitsprodukt; ohne ungeprüfte Aktenzeichen. |
| `insolvenzplan-paragraf-217-inso-bgh-ix-zb-66-19` | Insolvenzplan Paragraf 217 InsO BGH Ix Zb 66 19: fachanwaltlicher Spezialskill mit Normenanker, Fristen-/Zustaendigkeitscheck, Beweisfragen, Rechtsprechungshygiene und direkt nutzbarem Arbeitsprodukt. |
| `interessen-verwertung-beweislast-starug` | Interessen Verwertung Beweislast Starug im Insolvenz- und Sanierungsrecht: prüft konkret Schnittstellen, Verwertung, StaRUG-Restrukturierungsplan im Detail, Prüft Anfechtungsansprüche und Verteidigungslinien nach §§. |
| `kommunikation-glaeubiger-p002` | Inso Kommunikation Glaeubiger P002 im Insolvenz- und Sanierungsrecht: prüft konkret Kommunikation mit Glaeubigern im Insolvenz- und, § 2 InsO (Amtsgericht als Insolvenzgericht) im Mandat prüfen, § 3 InsO (Örtliche Zuständigkeit) im Manda... |
| `livecheck-fristennotiz-sanierungsrecht` | Inso Livecheck Fristennotiz Sanierungsrecht im Insolvenz- und Sanierungsrecht: prüft konkret Livecheck, Sanierungsrecht, § 104 InsO Fixgeschäfte, Finanzleistungen. |
| `masseunzulaenglichkeit-paragraf-208-inso` | Masseunzulaenglichkeit § 208 InsO: fachanwaltlicher Spezial-Skill mit Normenanker, Tatsachenmatrix, Beweislast, Fristen, Gegenargumenten und belastbarem Arbeitsprodukt; ohne ungeprüfte Aktenzeichen. |
| `output-waehlen` | Output-Wahl für Fachanwalt Insolvenz- und Sanierungsrecht: stimmt Adressat (Schuldnerunternehmen, Geschäftsführung (Haftung!), Insolvenzverwalter), Frist (§ 15a InsO 3 Wochen Antragspflicht) und Form auf den Zweck ab — typische Outputs:... |
| `quellen-livecheck` | Quellen-Live-Check für Fachanwalt Insolvenz- und Sanierungsrecht: prüft Normen (InsO, StaRUG, InsVV) gegen amtliche Datenbank, Rechtsprechung mit Gericht-Datum-Az-Rn; nutzt Insolvenzgericht (AG) und Quellenhygiene nach references/quellen... |
| `restschuldbefreiung-paragraf-287-inso-bgh-ix-zb-25-18` | Restschuldbefreiung Paragraf 287 InsO BGH Ix Zb 25 18: fachanwaltlicher Spezialskill mit Normenanker, Fristen-/Zustaendigkeitscheck, Beweisfragen, Rechtsprechungshygiene und direkt nutzbarem Arbeitsprodukt. |
| `scheme-of-arrangement` | Scheme of Arrangement: fachanwaltlicher Spezial-Skill mit Normenanker, Tatsachenmatrix, Beweislast, Fristen, Gegenargumenten und belastbarem Arbeitsprodukt; ohne ungeprüfte Aktenzeichen. |
| `starug-quellenkarte` | Starug Quellenkarte: Quellenprüfung; Normenstand, Rechtsprechung, Behördenpraxis und Zitierfähigkeit werden vor einer tragenden Aussage verifiziert. |
| `ueberschuldung-paragraf-19-inso-bgh-ii-zr-129-16` | Ueberschuldung Paragraf 19 InsO BGH Ii Zr 129 16: fachanwaltlicher Spezialskill mit Normenanker, Fristen-/Zustaendigkeitscheck, Beweisfragen, Rechtsprechungshygiene und direkt nutzbarem Arbeitsprodukt. |
| `unterlagen-luecken` | Lücken- und Beschaffungsliste für Fachanwalt Insolvenz- und Sanierungsrecht: trennt fehlende Tatsachen von fehlenden Belegen (Insolvenzantrag, Sanierungskonzept IDW S6, Plan), nennt pro Lücke Beweisthema, Beschaffungsweg (Insolvenzgerich... |
| `zahlungsunfaehigkeit-paragraf-17-inso-bgh-ix-zb-25-17` | Zahlungsunfaehigkeit Paragraf 17 InsO BGH Ix Zb 25 17: fachanwaltlicher Spezialskill mit Normenanker, Fristen-/Zustaendigkeitscheck, Beweisfragen, Rechtsprechungshygiene und direkt nutzbarem Arbeitsprodukt. |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
