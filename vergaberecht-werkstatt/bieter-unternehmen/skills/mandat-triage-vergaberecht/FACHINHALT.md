---
name: mandat-triage-vergaberecht
description: 'Vertieft nach dokumentierter Erstinventur die Bieterakte: bestimmt Verfahrensstand, rote Fristen, Angebotsziel, Qualitätsvorteil, Rügepunkt, Beweislücke, Dateiformat und Arbeitsmodul. Nicht für rohe Ordner oder ZIP-Dateien; dort startet der Master-Orchestrator.'
---

# Bieterakte nach Erstinventur rechtlich routen

<!-- BEGIN output-format-block (autogen) -->

## Output-Format (verbindlich)

Schriftart Times New Roman, Schriftgrad 11 pt. Dezimalgliederung 1, 1.1, 1.1.1, 2, 2.1 fortlaufend ohne Lücken, maximal vier Ebenen. Aufzählungen mit Spiegelstrich oder Bullet. Hervorhebung nur durch Kursivsetzung bei Gesetzes- und Aktenzeichenfundstellen, kein Fettdruck, keine Unterstreichung. Vollständige Regeln in [`references/OUTPUT-FORMAT.md`](../../references/OUTPUT-FORMAT.md). Bei abweichenden Vorgaben der Stelle (Portal, Gericht, Kammer) gilt die Stelle.

<!-- END output-format-block (autogen) -->

## Einsatz nach Erstinventur

Dieser Skill folgt auf eine dokumentierte Erstinventur durch den Master-Orchestrator. Er ist nicht der Einstieg für rohe Ordner oder ZIP-Dateien. Er übernimmt die bereits erfassten GAEB-, XML-, Excel-, PDF-, Office-, Portal- und Nachrichtenbestände mit Dateityp, Datum, Absender, Verfahrensbezug und Lesestatus; Originale werden nicht überschrieben.

## Startreihenfolge

1. Vergabegegenstand, Auftraggeber, Aktenzeichen, Los und Verfahren erkennen.
2. Rolle des Unternehmens bestimmen: Bewerber, Bieter, Bestbieter, ausgeschlossener Bieter, Bietergemeinschaft oder Nachunternehmer.
3. Verfahrensstand anhand des jüngsten belastbaren Dokuments bestimmen.
4. Fristen aus Bekanntmachung, Portal, § 134-Information, Rüge, Nichtabhilfe und VK-/OLG-Zustellungen berechnen.
5. Ziel festhalten: Teilnahme, formal vollständiges Angebot, Qualitätsmehrwert, Zuschlag, Abhilfe, Nachprüfung oder Schadensersatz.
6. Lücken benennen und sofort mit vorhandenen Unterlagen weiterarbeiten.

## Rechtsstandsweichen

- Schwellenwert und Regime werden für den Bekanntmachungszeitpunkt live geprüft.
- § 160 Abs. 3 GWB wird je Rügepunkt angewandt; nicht pauschal auf die Akte.
- § 134 GWB beginnt mit Absendung und unterscheidet elektronischen Versand oder Fax von Post.
- § 169 Abs. 1 GWB beginnt erst mit VK-Unterrichtung des Auftraggebers.
- Beschwerde-Rechtsstand: Verfahrensbeginn nach § 187 Abs. 2 GWB belegen. Neuverfahren ab 1. Juli 2026 folgen den neuen §§ 172 und 173 GWB; Altverfahren werden einschließlich Nachprüfung und Beschwerde nach altem Recht beendet.

## Routing

| Befund | primäres Modul | erstes Ergebnis |
|---|---|---|
| Vergabeunterlagen neu | `02-vergabeunterlagen-pruefen` | Unterlagen- und Pflichtenmatrix |
| Angebot zu erstellen | `angebot-in-vorgegebenem-format-erstellen` | Compliance- und Qualitätsplan |
| GAEB, XML, Excel oder PDF | `legacy-systeme-integration` | verlustfreier Import-, Mapping- und Exportplan |
| qualitative Zuschlagschance | `qualitaetsvorsprung-nachweisen` | Preis-Qualitäts- und Belegmatrix |
| erkannter Fehler vor Zuschlag | `ruegeschriftsatz-erstellen` | fristgerechter Rügeentwurf |
| Nichtabhilfe oder akuter Zuschlag | `vergabe-nachpruefung-aussicht` | Go-/Stop-Memo und Schutzstatus |
| VK-Erstantrag | `nachpruefungsantrag-vk` | vollständiger Antrag und Anlagenplan |
| laufendes VK-Verfahren | `nachpruefungsverfahren-vk` | Streitdashboard und nächster Schriftsatz |
| VK-Beschluss | `25-sofortige-beschwerde-olg-paragraf-171` | fristwahrende, zugleich begründete Beschwerde |

Mehrere Module werden nur geladen, wenn ihre Ergebnisse voneinander abhängen. Der Nutzer muss keinen Skillnamen kennen.

## Startbildschirm

Ausgabe in dieser Reihenfolge:

1. Fall in fünf Sätzen.
2. rote Frist mit Beleg oder deutlicher Datenlücke.
3. aktueller Verfahrensstand und Ziel.
4. Dokumentenmatrix mit fehlenden Pflichtunterlagen.
5. gewähltes Routing mit kurzer Begründung.
6. sofort erstelltes erstes Arbeitsprodukt.
7. höchstens fünf priorisierte Rückfragen, nur soweit entscheidungserheblich.

Keine allgemeine Rechtskunde, keine perspektivischen Platzhalter-Skills und keine pauschalen Streitwert- oder Erfolgsaussagen.
