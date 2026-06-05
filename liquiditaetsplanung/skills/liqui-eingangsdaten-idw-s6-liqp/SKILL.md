---
name: liqui-eingangsdaten-idw-s6-liqp
description: "Liqui Eingangsdaten IDW S6 Liqp: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Liqui Eingangsdaten IDW S6 Liqp

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Liqui Eingangsdaten IDW S6 Liqp** im Plugin Liquiditätsplanung. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `liqui-eingangsdaten-checkliste` | Eingangsdaten-Checkliste fuer Liquiditaetsplanung: BWA, OPOS Debitoren/Kreditoren, Kontoauszuege, Steuerkonten, SV-Konten, Personalkosten, Investitionsplanung. Pruefliste Quellen und Vollstaendigkeit. Output: standardisiertes Datentemplate. |
| `idw-s6-integrierte-sanierungsplanung` | Verbindet Liquiditätsvorschau, GuV-Planung und Planbilanz zu einer Sanierungsplanung auf IDW-S-6-Niveau. Prüft Maßnahmenwirkung, Fortbestehensprognose, Sanierungsfähigkeit, Szenarien, Planungsannahmen, Belegregister, kleinere Unternehmen und Übergabe an Bank, Insolvenzverwalter oder Restrukturierungsberater. Output: Planungsanforderung, Annahmenlog, Maßnahmen-Brücke und Sanierungsplanungs-Ampel. |
| `liqp-bankenreporting-leitfaden` | Leitfaden Bankenreporting bei Krise: Anforderungen Hausbank, Konsortium, KfW, Reportingfrequenz, Covenant-Reporting. Pruefraster fuer CFO und Berater. |

## Arbeitsweg

Im Plugin Liquiditätsplanung gilt für **Liqui Eingangsdaten IDW S6 Liqp**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `liqui-eingangsdaten-checkliste`

**Fokus:** Eingangsdaten-Checkliste fuer Liquiditaetsplanung: BWA, OPOS Debitoren/Kreditoren, Kontoauszuege, Steuerkonten, SV-Konten, Personalkosten, Investitionsplanung. Pruefliste Quellen und Vollstaendigkeit. Output: standardisiertes Datentemplate.

# Liqui: Eingangsdaten-Checkliste

## Fachkern: Liqui: Eingangsdaten-Checkliste
- **Spezialgegenstand:** Liqui: Eingangsdaten-Checkliste wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** InsO §§ 17, 18, 19, 15a, StaRUG-Früherkennung, IDW-S-6-/Planungslogik, 3-Wochen- und 13-Wochen-Forecast, Zahlungsstatus und Fortbestehensprognose.
- **Entscheidende Weiche:** Trenne fällige Verbindlichkeiten, liquide Mittel, harte Zahlungszusagen, Planannahmen, Quote/Lücke, Organpflicht und Dokumentationsspur.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


## Fallweichen
Frage zu Beginn nur ab, was fuer den naechsten Schritt unverzichtbar ist. Wenn Material vorliegt, mit dem Material arbeiten und nur eine gezielte Rueckfrage stellen.

1. **Rolle und Ziel:** Wer fragt, welche Rolle, welcher gewuenschte Output (Memo, Schriftsatz, Tabelle, Checkliste)?
2. **Sachverhalt:** Welche unstreitigen Tatsachen liegen vor, was ist streitig, was fehlt noch?
3. **Fristen:** Gibt es Termine, Fristen, eilbeduerftige Schritte?
4. **Unterlagen:** Welche Dokumente, Bescheide, Vertraege, Auszuege liegen vor?
5. **Format:** Wie ausfuehrlich, fuer wen, in welcher Tonalitaet?

## Pruefraster

Der Output muss als verwertbares Arbeitsprodukt aufgebaut sein:

1. **Sachverhalt fixieren** – streitige und unstreitige Tatsachen trennen, Lueckentafel.
2. **Rechtliche Einordnung** - nur einschlaegige Normen, verifizierte Rechtsprechung und frei pruefbare amtliche Quellen; keine Literatur- oder Datenbankfundstellen erfinden.
3. **Pruefung im Gutachtenstil** – Obersatz, Definition, Subsumtion, Zwischenergebnis.
4. **Handlungsempfehlung** – konkret, mit naechstem Schritt, verantwortlicher Person, Frist.

## Plugin-Kontext
Dieses Fachmodul arbeitet den konkreten Schwerpunkt aus, prüft Aktenlage, Normen, Fristen, Belege und Gegenargumente und erzeugt einen unmittelbar nutzbaren nächsten Schritt.

## Output-Module
- Strukturierter Pruefvermerk im Gutachtenstil mit klaren Ueberschriften.
- Tabellen/Checklisten, wo das die Lesbarkeit erhoeht.
- Anschreiben-, Antrags- oder Klageschriftsatz-Geruest, wenn die Aufgabe das verlangt.
- Quellenliste mit Gericht, Datum, Aktenzeichen, frei pruefbarem Link.

## Quellenregel
- Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei pruefbarem Link ausgeben; bei Unsicherheit erst verifizieren oder als zu pruefen markieren.
- Keine Paywall-, Kommentar-, Aufsatz- oder Datenbankfundstelle als tragende Aussage verwenden, wenn sie nicht durch Nutzerquelle oder dokumentierten Live-Zugriff verifiziert ist.
- Keine Kommentar-, Handbuch-, Aufsatz- oder BeckRS-/juris-Blindzitate aus Modellwissen. Literatur nur verwenden, wenn der Nutzer die Quelle bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitskontext dokumentiert ist.
- Annahmen explizit als solche kennzeichnen; keine erfundenen Fundstellen, keine erfundenen Tatsachen, keine erfundenen Behoerdenpraxis-Saetze.

## Was dieser Arbeitsgang nicht macht
- Kein Ersatz fuer eine vollstaendige Mandantenberatung.
- Keine Festlegung des Mandanten ohne dessen ausdrueckliche Entscheidung.
- Keine Bewertung von Tatsachen, die nicht durch Unterlagen oder klare Mandantenangaben gedeckt sind.
- Bei erkennbaren Interessenkonflikten oder Berufsrechtsfragen Hinweis an den fallfuehrenden Anwalt.

## 2. `idw-s6-integrierte-sanierungsplanung`

**Fokus:** Verbindet Liquiditätsvorschau, GuV-Planung und Planbilanz zu einer Sanierungsplanung auf IDW-S-6-Niveau. Prüft Maßnahmenwirkung, Fortbestehensprognose, Sanierungsfähigkeit, Szenarien, Planungsannahmen, Belegregister, kleinere Unternehmen und Übergabe an Bank, Insolvenzverwalter oder Restrukturierungsberater. Output: Planungsanforderung, Annahmenlog, Maßnahmen-Brücke und Sanierungsplanungs-Ampel.

# Integrierte Sanierungsplanung

## Fachkern: Integrierte Sanierungsplanung
- **Spezialgegenstand:** Integrierte Sanierungsplanung wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** InsO §§ 17, 18, 19, 15a, StaRUG-Früherkennung, IDW-S-6-/Planungslogik, 3-Wochen- und 13-Wochen-Forecast, Zahlungsstatus und Fortbestehensprognose.
- **Entscheidende Weiche:** Trenne fällige Verbindlichkeiten, liquide Mittel, harte Zahlungszusagen, Planannahmen, Quote/Lücke, Organpflicht und Dokumentationsspur.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


## Aufgabe

Dieser Skill hebt eine Liquiditätsvorschau auf Sanierungskonzept-Niveau. Er prüft nicht nur, ob in den nächsten Wochen Geld reicht, sondern ob Maßnahmen, Ergebnisplanung, Bilanzplanung und Liquiditätsplanung zusammen ein konsistentes Bild ergeben.

Nutze ihn, wenn ein Unternehmen, eine Bank, ein Insolvenzverwalter, ein Sachwalter, ein Restrukturierungsberater oder ein Gericht nicht nur einen Cash-Forecast, sondern eine tragfähige Sanierungsplanung braucht.

## Wann starten?

- 13-Wochen-Plan ist erstellt, aber Bank verlangt Sanierungskonzept.
- Fortbestehensprognose nach § 19 InsO soll dokumentiert werden.
- StaRUG-, Schutzschirm-, Eigenverwaltungs- oder Insolvenzplanroute steht im Raum.
- Maßnahmenliste existiert, aber ihre finanzielle Wirkung ist unklar.
- Kleine Gesellschaft hat nur BWA, OPOS und Bankauszüge; trotzdem braucht es eine belastbare Planung.

## Eingangsrouting

Wenn nur kurzfristige Zahlungsunfähigkeit geprüft wird, zuerst `liquiditaetsvorschau-3wochen` oder `liquiditaetsvorschau-insolvenzrechtlich`. Wenn daraus ein Sanierungskonzept, eine Bankunterlage oder eine Fortbestehensprognose werden soll, anschließend diesen Skill nutzen.

## Planungsarchitektur

Baue die Planung in vier Ebenen:

1. **Direkte Liquiditätsplanung:** Einzahlungen, Auszahlungen, Linien, freie Liquidität, Engpasswochen.
2. **GuV-Planung:** Umsatz, Rohertrag, Personal, Fixkosten, Zinsen, Steuern, Ergebnis.
3. **Bilanzplanung:** Working Capital, Anlagevermögen, Rückstellungen, Finanzverbindlichkeiten, Eigenkapital.
4. **Maßnahmen- und Annahmenlog:** Jede wesentliche Veränderung mit Quelle, Verantwortlichem, Timing und Risiko.

Alle Ebenen müssen rechnerisch zusammenpassen. Wenn sie nicht passen, ist das Ergebnis eine Lückenliste, nicht eine geschönte Planung.

## Mindesttiefe

- Für akute Krisen: wöchentliche Liquidität für 13 Wochen.
- Für Fortbestehensprognose: mindestens 12 Monate mit belastbarer Liquiditätsreichweite.
- Für Sanierungskonzept: laufendes und folgendes Planjahr regelmäßig monatlich; spätere Jahre können verdichtet werden, wenn die Brücken transparent bleiben.
- Für kleinere Unternehmen: weniger Kontenzeilen sind zulässig, aber GuV, Bilanz und Liquidität müssen trotzdem verknüpft sein.

## Maßnahmen-Brücke

Lege für jede Maßnahme einen Datensatz an:

```yaml
massnahme:
 titel: "[z. B. Standortkonsolidierung / Bankstundung / Kapitalzufuhr]"
 krisenursache: "[welche Ursache wird adressiert?]"
 status: "verbindlich | verhandelt | plausibel | ungeklärt | nicht tragfähig"
 guv-effekt:
 umsatz: "[EUR / Prozent / Monat]"
 kosten: "[EUR / Monat]"
 zinsen_steuern: "[EUR / Monat]"
 liquiditaets-effekt:
 einmalig: "[EUR, Datum]"
 laufend: "[EUR, ab Datum]"
 vorfinanzierungsbedarf: "[EUR]"
 bilanz-effekt:
 eigenkapital: "[EUR]"
 verbindlichkeiten: "[EUR]"
 working_capital: "[EUR]"
 voraussetzungen:
 - "[Beschluss, Vertrag, Finanzierung, Zustimmung]"
 nachweise:
 - "[Datei / Vertrag / Beschluss / Kontoauszug]"
 risiko:
 sensitivitaet: "[was passiert bei Verzug oder Teilwirkung?]"
```

## Sanierungsfähigkeits-Ampel

Bewerte am Ende:

| Ampel | Bedeutung | Konsequenz |
|---|---|---|
| Grün | Liquidität, Ertrag, Bilanz und Maßnahmen tragen auch in plausibler Sensitivität. | Planung kann als Arbeitsstand für Konzept, Bank oder Planroute genutzt werden. |
| Gelb | Basisfall trägt, aber eine tragende Annahme oder Maßnahme ist nicht belegt. | Conditional Go; Datenanforderung und Nachweisfrist ausgeben. |
| Rot | Planung kippt bei naheliegender Abweichung oder beseitigt Krisenursachen nicht. | Keine positive Sanierungsfähigkeit ausgeben; Eskalation zu Insolvenz-/Restrukturierungsberatung. |

## Annahmenlog

Jede wesentliche Annahme braucht:

- Quelle: historische Daten, Vertrag, Auftrag, Managementangabe, Marktbeleg, Steuerbescheid, Bankzusage.
- Plausibilisierung: Vergangenheit, Branchenlogik, Kapazität, Preis-/Mengenbrücke, Gegenparteirisiko.
- Sensitivität: Best/Base/Worst oder mindestens Base/Downside.
- Verantwortlicher: wer aktualisiert und wer entscheidet?
- Wiedervorlage: wann wird die Annahme neu geprüft?

## Spezielle Prüfbereiche

- **Working Capital:** Zahlungsziele, Forderungsausfall, Vorratsaufbau, Lieferantenkredite.
- **Finanzierung:** Linienverfügbarkeit, Kündigungsrechte, Covenants, Tilgungsprofil, Sicherheiten.
- **Steuern und Sozialversicherung:** Fälligkeiten, Rückstände, Stundung, Nebenforderungen.
- **Personal:** Abbaukosten, Kündigungsfristen, Betriebsrat, Insolvenzgeldzeitraum.
- **Investitionen:** Erhaltungs-CapEx nicht mit Null ansetzen, wenn Betrieb sonst ausfällt.
- **Cyber/IT/ESG:** nur dort vertiefen, wo sie für Betrieb, Markt, Finanzierung oder Haftung wesentlich sind.

## Ausgabe

Liefer standardmäßig:

1. **Planungsanforderung** mit Datenliste und Priorität.
2. **Annahmenlog** als Tabelle.
3. **Maßnahmen-Brücke** zwischen Maßnahme, GuV, Bilanz und Liquidität.
4. **Sanierungsplanungs-Ampel** mit Gründen und Stoppern.
5. **Nächster Arbeitsschritt:** Liquiditätsplan aktualisieren, Planbilanz bauen, Maßnahmen belegen, oder insolvenzrechtlich eskalieren.

## Typische Fehler

- Liquiditätsvorschau wird als vollständige Sanierungsplanung verkauft.
- Maßnahmen werden doppelt gezählt: einmal in GuV, einmal im Cashflow.
- Steuern aus Sanierungsmaßnahmen fehlen.
- Working-Capital-Effekt des Wachstums wird ignoriert.
- Planjahr schließt liquiditätsseitig, aber Bilanz stimmt nicht.
- Gesellschafter- oder Bankbeitrag ist nicht verbindlich.
- Kleine Unternehmen werden zu grob geplant, obwohl einzelne Großkunden oder Schlüsselpersonen das Risiko treiben.

## Quellenregel

Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen. Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle ausgeben. Berufsständische Standards als methodischen Maßstab verwenden, nicht als Zitierersatz.

## 3. `liqp-bankenreporting-leitfaden`

**Fokus:** Leitfaden Bankenreporting bei Krise: Anforderungen Hausbank, Konsortium, KfW, Reportingfrequenz, Covenant-Reporting. Pruefraster fuer CFO und Berater.

# LiqP: Bankenreporting

## Fachkern: LiqP: Bankenreporting
- **Spezialgegenstand:** LiqP: Bankenreporting wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** InsO §§ 17, 18, 19, 15a, StaRUG-Früherkennung, IDW-S-6-/Planungslogik, 3-Wochen- und 13-Wochen-Forecast, Zahlungsstatus und Fortbestehensprognose.
- **Entscheidende Weiche:** Trenne fällige Verbindlichkeiten, liquide Mittel, harte Zahlungszusagen, Planannahmen, Quote/Lücke, Organpflicht und Dokumentationsspur.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


## Fallweichen
Frage zu Beginn nur ab, was fuer den naechsten Schritt unverzichtbar ist. Wenn Material vorliegt, mit dem Material arbeiten und nur eine gezielte Rueckfrage stellen.

1. **Rolle und Ziel:** Wer fragt, welche Rolle, welcher gewuenschte Output (Memo, Schriftsatz, Tabelle, Checkliste)?
2. **Sachverhalt:** Welche unstreitigen Tatsachen liegen vor, was ist streitig, was fehlt noch?
3. **Fristen:** Gibt es Termine, Fristen, eilbeduerftige Schritte?
4. **Unterlagen:** Welche Dokumente, Bescheide, Vertraege, Auszuege liegen vor?
5. **Format:** Wie ausfuehrlich, fuer wen, in welcher Tonalitaet?

## Pruefraster

Der Output muss als verwertbares Arbeitsprodukt aufgebaut sein:

1. **Sachverhalt fixieren** - streitige und unstreitige Tatsachen trennen, Lueckentafel.
2. **Rechtliche Einordnung** - einschlaegige Normen, Rechtsprechung BGH/BVerfG/EuGH, Literatur.
3. **Pruefung im Gutachtenstil** - Obersatz, Definition, Subsumtion, Zwischenergebnis.
4. **Handlungsempfehlung** - konkret, mit naechstem Schritt, verantwortlicher Person, Frist.

## Plugin-Kontext
Dieses Fachmodul arbeitet den konkreten Schwerpunkt aus, prüft Aktenlage, Normen, Fristen, Belege und Gegenargumente und erzeugt einen unmittelbar nutzbaren nächsten Schritt.

## Output-Module
- Strukturierter Pruefvermerk im Gutachtenstil mit klaren Ueberschriften.
- Tabellen und Checklisten, wo das die Lesbarkeit erhoeht.
- Anschreiben-, Antrags- oder Klageschriftsatz-Geruest, wenn die Aufgabe das verlangt.
- Quellenliste mit Gericht, Datum, Aktenzeichen, frei pruefbarem Link.

## Quellenregel
- Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei pruefbarem Link (`dejure.org`, `openjur.de`, `bundesgerichtshof.de`, `bundesverfassungsgericht.de`, `curia.europa.eu`).
- Keine Zitate aus `anwalt24.de`. Keine `BeckRS` als alleinige Fundstelle bei tragenden Aussagen.
- Aufsaetze mit Verfasser, Zeitschrift, Jahr, Heft (falls relevant) und Seite.
- Kommentare mit Bearbeiter und Randnummer.
- Annahmen explizit als solche kennzeichnen, keine Erfindungen.

## Was dieser Arbeitsgang nicht macht
- Kein Ersatz fuer eine vollstaendige Mandantenberatung.
- Keine Festlegung des Mandanten ohne dessen ausdrueckliche Entscheidung.
- Keine Bewertung von Tatsachen, die nicht durch Unterlagen oder klare Mandantenangaben gedeckt sind.
- Bei erkennbaren Interessenkonflikten oder Berufsrechtsfragen Hinweis an den fallfuehrenden Anwalt.
