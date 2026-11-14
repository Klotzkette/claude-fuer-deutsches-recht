---
name: mandat-schliessen
description: "Für Mandat schließen: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt."
---

# Mandat schließen

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: nur die Fristen des konkreten Rechtsgebiets und der Akte verwenden; Widerspruch, Klage, Einspruch, Rechtsmittel, Verjährung, Verwirkung, Rüge-, Anzeige-, Anmelde- und Ausschlussfristen strikt trennen und nie aus einem anderen Fachgebiet übernehmen.
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Eingaben

- Mandat-Slug
- Abschlusstyp: `--urteil`, `--vergleich`, `--klagerücknahme`, `--erledigungserklärung`, `--einstellung`, `--sonstiges`
- Ergebnis (kurz): Wer hat gewonnen, was wurde vereinbart, welcher Betrag?

## Ablauf

1. **Abschlusstype und Ergebnis erfassen:**

 | Typ | Relevante Normen |
 |---|---|
 | Urteil (Endurteil) | Paragrafen 300 ff. ZPO; Rechtskraft Paragraf 322 ZPO |
 | Anerkenntnisurteil | Paragraf 307 ZPO |
 | Versäumnisurteil | Paragrafen 330 ff. ZPO |
 | Vergleich | Paragrafen 794 Abs. 1 Nr. 1, 278 ZPO; vollstreckbar |
 | Klagerücknahme | Paragrafen 269, 270 ZPO; Kostenfolge Paragraf 269 Abs. 3 ZPO |
 | Erledigungserklärung | Paragraf 91a ZPO; Kostenbeschluss |
 | Kostenfeststellungsklage nach erledigter Hauptsache | Paragrafen 263, 264 Nr. 2, 256 ZPO; Paragrafen 280, 286 BGB |
 | Einstellung (Strafrecht) | Paragrafen 153, 153a, 170 Abs. 2, 204 StPO |
 | Verfahrensvergleich (Verwaltungsrecht) | Paragraf 106 VwGO |

Vor jeder Klagerücknahme oder Erledigungserklärung ist bei Zahlung, Aufrechnung, dauernder Einrede, Unmöglichkeit oder Wegfall des Rechtsschutzbedürfnisses die Zeitachse zu prüfen. War die Gegenseite bei Klageeinreichung in Verzug, kann die Umstellung auf Feststellung der materiellen Kostenerstattungspflicht als Verzugsschaden strategisch besser sein als Paragraf 91a ZPO oder Paragraf 269 Abs. 3 Satz 3 ZPO. Dann den Skill `kostenfeststellungsklage-verzugsschaden-erledigung` nutzen und die Entscheidung in der Handakte begründen.

2. **Endexposition berechnen:**
 - Gezahlter Betrag / auferlegte Leistung
 - Kostenfestsetzung (Paragrafen 103 ff. ZPO): eigene Kosten + erstattete / zu erstattende Kosten
 - Vergleich mit ursprünglicher Risikoschätzung (Intake-Wert)

3. **Honorar und Gebühren:**
 - Letzte Abrechnung nach RVG (Paragraf 8 RVG: Fälligkeit mit Mandatsbeendigung)
 - Offene Vorschüsse (Paragraf 9 RVG) zurückerstatten oder verrechnen
 - Fremdgelder abwickeln (Paragraf 43a Abs. 5 BRAO: unverzügliche Weiterleitung)

4. **Lessons Learned:**
 - Was lief gut / schlecht?
 - Prozessführungsempfehlung für künftige vergleichbare Mandate?
 - BGH- oder OLG-Urteile, die im Mandat relevant waren und für spätere Mandate zu merken sind?

5. **Handakte archivieren (Paragraf 50 BRAO):**
 - Handakte für mind. 6 Jahre nach Mandatsende aufbewahren
 - Elektronische Akte: gleichwertige Sicherung (Paragraf 50 Abs. 2 BRAO)
 - Herausgabepflicht auf Verlangen (Paragraf 50 Abs. 3 BRAO)

6. **Portfolio-Log aktualisieren:** Status in `_log.yaml` auf `archiv` setzen; Abschlussdatum, Ergebnis, Endexposition eintragen.

## Quellen und Zitierweise

Verbindlich: `../references/zitierweise.md`.

- Quellenregel: Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff; keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen.
- BRAO Paragraf 50 (Aufbewahrungspflicht Handakten: 6 Jahre); Paragraf 43a Abs. 5 BRAO (Fremdgelder).

## Ausgabeformat

```
MANDAT-ABSCHLUSS
──────────────────────────────────────
Mandat-Slug: [slug]
Schließungsdatum: TT.MM.JJJJ
Typ: [z. B. Vergleich]
MANDATSGEHEIMNIS – Paragraf 43a Abs. 2 BRAO

──────────────────────────────────────
ERGEBNIS
──────────────────────────────────────
Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

──────────────────────────────────────
ENDEXPOSITION
──────────────────────────────────────
Eingeklagter Betrag: EUR XX.XXX
Vergleichszahlung: EUR XX.XXX
Kostenerstattung: EUR X.XXX (Paragrafen 103 ff. ZPO)
Ursprüngliche Schätzung: EUR XX.XXX – EUR XX.XXX

──────────────────────────────────────
LESSONS LEARNED
──────────────────────────────────────
[Freitext]

──────────────────────────────────────
ARCHIVIERUNG
──────────────────────────────────────
Handakte aufzubewahren bis: TT.MM.JJJJ (Paragraf 50 Abs. 1 BRAO: 6 Jahre)
_log.yaml-Status: archiv
```

<!-- BEGIN ausformulierungspflicht (autogen) -->
> **Ausformulierungspflicht und Formatstandard.** Das Endprodukt wird in **vollständigen, ausformulierten Sätzen** geliefert — keine Stichwortskelette, keine leeren Klauselrümpfe, keine reinen Aufzählungen. Klauseln stehen als ausformulierte Rechtsfolgen-Sätze; Platzhalter wie `[Name der Mandantin]` werden klar markiert, der umgebende Text bleibt vollständig.
>
> **Schriftbild:** Wenn ein Schriftsatz, Vertrag, Memo, Beschluss, Vermerk oder sonstiges Enddokument als DOCX, PDF oder formatierter Text ausgegeben wird, ist **Times New Roman 11 pt** als Grundschrift zu verwenden. Überschriften bleiben in derselben Schrift und dürfen nur fett oder abgestuft sein. Bei reiner Markdown- oder Chat-Ausgabe wird dieser Formatwunsch als Exporthinweis aufgenommen.
>
> **Nummerierung:** Gliederung ausschließlich dezimal (`1`, `1.1`, `1.1.1` und so weiter). Keine römischen Ziffern, keine Buchstaben- oder Mischgliederung.
<!-- END ausformulierungspflicht (autogen) -->

## Risiken / typische Fehler

- **Aufbewahrungsfrist übersehen:** Paragraf 50 Abs. 1 BRAO: mindestens 6 Jahre nach Mandatsende; kürzere Vernichtung ist Berufsrechtsverletzung.
- **Fremdgelder nicht abgewickelt:** Paragraf 43a Abs. 5 BRAO – Fremdgelder (Kostenvorschüsse, Schadensersatzbeträge) unverzüglich weiterleiten; Verzögerung kann zur Strafbarkeit führen (Paragraf 266 StGB).
- **Rechtsmittelfrist läuft noch:** Vor dem Schließen prüfen, ob Berufungs- (Paragraf 517 ZPO: 1 Monat) oder Revisionsfrist (Paragraf 548 ZPO: 1 Monat) noch offen ist; Mandat erst nach Eintritt der Rechtskraft schließen oder Mandanten ausdrücklich auf Verzicht hinweisen.
- **Vollstreckungsverjährung:** Vollstreckungstitel verjähren nach Paragraf 197 Abs. 1 Nr. 3 BGB in 30 Jahren; Abschluss nicht ohne Dokumentation der Vollstreckungsmaßnahmen.
- **Erledigungsfalle bei Zahlung nach Klageeinreichung:** Nicht automatisch erledigen oder zurücknehmen. Zuerst prüfen, ob die Kosten des Klageverfahrens wegen Verzugs nach Paragrafen 280, 286 BGB als materieller Schaden feststellbar sind.

> Quellenregel: Entscheidungen nur nach Prüfung einer amtlichen oder frei zugänglichen Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage ausgeben.
