---
name: einstieg-routing
description: "Für Anwalts-Dashboard Fachanwalt Insolvenz- und Sanierungsrecht: routet Rolle, Frist, Unterlagen und Fachschritt; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt."
---

# Anwalts-Dashboard Fachanwalt Insolvenz- und Sanierungsrecht

> Antragspflicht, Eigenverwaltung, Anfechtung, Restrukturierung: Der Antrag ist ohne schuldhaftes Zögern zu stellen; drei Wochen bei Zahlungsunfähigkeit und sechs Wochen bei Überschuldung sind nur Höchstfristen.
>
> Sie sehen unten die Sofort-Triage. Keine Rückfragen, bis die Tabelle steht. Wenn die Akte 80 % trägt, gehen wir direkt zum Anschluss-Skill — Sie entscheiden, ob.

## Sofort-Triage

| Punkt | Schnellprüfung | Standardquelle / Hilfsweg |
| --- | --- | --- |
| Rolle | Wen vertrete ich? (Mandant · Gegenseite · Mehrere) | Mandantenmail, Vertretungsbestellung |
| Verfahrensstand | Vorprozessual · außergerichtlich · Klage · Rechtsmittel · Vollstreckung | Vorhandene Schriftsätze, Eingangsstempel |
| Eilfrist | **Paragraf 15a Absatz 1 InsO:** Antrag ohne schuldhaftes Zögern, höchstens drei Wochen bei Zahlungsunfähigkeit und sechs Wochen bei Überschuldung. **Paragraf 270d InsO:** Schutzschirm nur bei drohender Zahlungsunfähigkeit oder Überschuldung und fehlender Zahlungsunfähigkeit. | Objektiven Eintritt des Insolvenzgrunds und gerichtliche Bekanntmachungen dokumentieren |
| Hauptanspruch | Antragspflicht §§ 15a, 17 ff. InsO · Anfechtung §§ 129 ff. InsO · GF-Haftung § 64 GmbHG a. F. / § 15b InsO n. F. · Gläubigeranfechtung AnfG außerhalb Insolvenz · Schutzschirm § 270d InsO · Eigenverwaltung § 270 InsO · StaRUG (Stabilisierungs- und Restrukturierungsrahmen). | Sachverhaltsabgleich mit Tatbestandsmerkmalen |
| Zuständigkeit | Insolvenzgericht nach Paragraf 3 InsO bestimmen. Restrukturierungsgericht ist nach Paragraf 34 StaRUG grundsätzlich das Amtsgericht am Sitz eines Oberlandesgerichts; landesrechtliche Konzentration und die örtliche Zuständigkeit nach Paragraf 35 StaRUG aktuell prüfen. Anfechtungsklage gegen Gläubiger: Amts- oder Landgericht nach Zuständigkeit und Streitwert. | Gesetz, Landesverordnung, Register, Gerichtsverzeichnis |

## Risiko-Ampel

- **Frist:** Paragraf 15a InsO verlangt den Antrag ohne schuldhaftes Zögern; drei Wochen ab Zahlungsunfähigkeit und sechs Wochen ab Überschuldung sind nur Höchstfristen. Antrag und Planung der Eigenverwaltung nach Paragraf 270a InsO, vorläufige Anordnung nach Paragraf 270b InsO und Schutzschirm nach Paragraf 270d InsO nur bei erfüllten Voraussetzungen vorbereiten.
- **Beweislage:** 🔴 Zahlungsunfähigkeit § 17 II InsO: 3-Wochen-Liquiditätsstatus. Buchhaltungs- und Bankkontodaten sichern. 🟠 Überschuldung § 19 II InsO: Fortbestehensprognose dokumentieren.
- **Wirtschaftlich:** 🔴 Zahlungen nach Insolvenzreife unter Paragraf 15b InsO einzeln erfassen und nur nach dessen Maßstab fortführen. 🟠 Bei Paragraf 133 InsO den Grundzeitraum von zehn Jahren, den Vierjahreszeitraum für Sicherung oder Befriedigung und die Sonderregeln der Absätze 3 und 4 auseinanderhalten.

## Anschluss-Skills (Router)

| Wenn der Fall trägt … | dann Skill | Erwartung |
| --- | --- | --- |
| Fortbestehensprognose anwerfen | `insanw-fortbestehensprognose-workflow` | Liquiditätsplan 12 Monate, IDW S 11, Beweisdokument |
| Eigenverwaltung / Schutzschirm Paragraf 270d InsO | `insanw-eigenverwaltung-schutzschirm-spezial` | Eigenverwaltungsplanung, Bescheinigung, Planvorlagefrist, Sachwalter |
| **Antragspflicht Paragraf 15a InsO** | `inso-p015a-antragspflicht-bei-juristischen-personen-und-rechtsfa` | unverzüglicher Antrag, Drei-/Sechswochen-Höchstfrist, Organhaftung, Strafrecht |
| Anfechtungsmandat (Gläubiger / Verwalter) | `insanw-anfechtungsmandat-leitfaden` | Tatbestände §§ 129 ff. InsO, Verteidigungsstrategie |
| Konzerninsolvenz / Gruppenkoordination | `insanw-konzerninsolvenz-koordination-spezial` | Gruppen-Gerichtsstand § 3a InsO, Koordinationsverfahren |

## Norm-Radar

- **Paragraf 15a InsO** — Insolvenzantragspflicht ohne schuldhaftes Zögern; höchstens drei Wochen bei Zahlungsunfähigkeit und sechs Wochen bei Überschuldung
- **§ 17 InsO** — Zahlungsunfähigkeit
- **§ 19 InsO** — Überschuldung
- **§ 270 InsO** — Eigenverwaltung; § 270d Schutzschirm
- **Paragraf 133 InsO** — zehnjähriger Grundzeitraum; vier Jahre, wenn die Handlung Sicherung oder Befriedigung gewährt oder ermöglicht; Absatz 3 und 4 gesondert prüfen
- **§ 15b InsO** — Zahlungsverbot nach Insolvenzreife

## Genau eine Rückfrage (nur wenn nötig)

> Stehen wir **vor** der Antragstellung (Beratung GF / Sanierung) oder **nach** Verfahrenseröffnung (Verwalter, Gläubiger, Anfechtung)?

Wenn die Akte die Frage selbst beantwortet, **diese überspringen** und direkt den passenden Anschluss-Skill arbeiten.

## Leitentscheidungs-Anker (Such-Wegweiser, keine fertigen Zitate)

- **Verwertung und Betriebsveräußerung** — Paragrafen 159, 160 und 163 InsO nach Verfahrensstand, Sicherungsrechten, Beschlusslage und dokumentiertem Marktprozess prüfen. Einen Haftungsanker nach Paragraf 60 InsO nur verwenden, wenn Sachverhalt, Pflichtenkreis und tragende Aussage der Entscheidung tatsächlich passen.
- **Vorsatzanfechtung und Bargeschäft** — Paragraphen 133 und 142 InsO tatbestandsbezogen prüfen; erst nach Festlegung von Handlung, Deckungsart, Benachteiligung und Kenntnis die passende Entscheidung des IX. Zivilsenats auswählen.
- **Insolvenzantragspflicht und Zahlungsverbot** — Paragraphen 15a und 15b InsO strikt nach Pflichtigem, Insolvenzgrund, Frist, Zahlung und Privilegierung trennen.
- **Geschäftsveräußerung im Ganzen** — EuGH, Urteil vom 27.11.2003 - C-497/01 (Zita Modes): Übertragung einer selbständigen wirtschaftlichen Einheit, die fortgeführt werden kann. EuGH, Urteil vom 10.11.2011 - C-444/10 (Schriever): Erforderlichkeit mitübertragener Betriebsgrundlagen, insbesondere von Räumen, hängt von Art und Umständen der Tätigkeit ab.

> Diese Anker sind Sucheinstieg. Vor jeder Verwendung in Schriftsatz, Memo oder Mandantenbrief die konkrete Entscheidung in der amtlichen Quelle öffnen und Datum, Aktenzeichen, Randnummer sowie Übertragbarkeit auf den festgestellten Sachverhalt prüfen. Kuratierte Anker-Sammlung in `references/leitentscheidungen-anker.md`.

## Hinweis

Diese Triage ist Ihre Vorbereitung, nicht Ihre Entscheidung. Sie führen das Mandat; der Skill liefert die Karte. Quellenhygiene nach `references/quellenhygiene.md`, Zitierform nach `references/zitierweise.md`. Die Konvention dieses Einstiegs-Dashboards steht in `references/anwalts-dashboard-konvention.md`.
