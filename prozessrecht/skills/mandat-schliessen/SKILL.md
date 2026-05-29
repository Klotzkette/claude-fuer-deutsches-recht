---
name: mandat-schliessen
description: "Mandat nach Prozessabschluss formal schließen: Kostenfestsetzung, Archivierung, Mandanteninformation. Normen: §§ 103 ff. ZPO, RVG. Prüfraster: Kostenfestsetzungsantrag, Ergebnismitteilung, Handaktenfreigabe. Output: Abschlussbericht Mandat. Abgrenzung: nicht laufende Mandat-Aktualisierung."
---

# Mandat schließen

## Zweck

Strukturierter Abschluss eines Mandats im Portfolio: Ergebnis dokumentieren, Kosten und Honorar abrechnen, Lehren festhalten, Mandat aus dem aktiven Portfolio in den Archivstatus überführen. Der Datensatz bleibt dauerhaft erhalten (Aufbewahrungspflicht § 50 Abs. 1 BRAO: 6 Jahre nach Mandatsende).

## Eingaben

- Mandat-Slug
- Abschlusstyp: `--urteil`, `--vergleich`, `--klagerücknahme`, `--erledigungserklärung`, `--einstellung`, `--sonstiges`
- Ergebnis (kurz): Wer hat gewonnen, was wurde vereinbart, welcher Betrag?

## Ablauf

1. **Abschlusstype und Ergebnis erfassen:**

   | Typ | Relevante Normen |
   |---|---|
   | Urteil (Endurteil) | §§ 300 ff. ZPO; Rechtskraft § 322 ZPO |
   | Anerkenntnisurteil | § 307 ZPO |
   | Versäumnisurteil | §§ 330 ff. ZPO |
   | Vergleich | §§ 794 Abs. 1 Nr. 1, 278 ZPO; vollstreckbar |
   | Klagerücknahme | §§ 269, 270 ZPO; Kostenfolge § 269 Abs. 3 ZPO |
   | Erledigungserklärung | § 91a ZPO; Kostenbeschluss |
   | Einstellung (Strafrecht) | §§ 153, 153a, 170 Abs. 2, 204 StPO |
   | Verfahrensvergleich (Verwaltungsrecht) | § 106 VwGO |

2. **Endexposition berechnen:**
   - Gezahlter Betrag / auferlegte Leistung
   - Kostenfestsetzung (§§ 103 ff. ZPO): eigene Kosten + erstattete / zu erstattende Kosten
   - Vergleich mit ursprünglicher Risikoschätzung (Intake-Wert)

3. **Honorar und Gebühren:**
   - Letzte Abrechnung nach RVG (§ 8 RVG: Fälligkeit mit Mandatsbeendigung)
   - Offene Vorschüsse (§ 9 RVG) zurückerstatten oder verrechnen
   - Fremdgelder abwickeln (§ 43a Abs. 5 BRAO: unverzügliche Weiterleitung)

4. **Lessons Learned:**
   - Was lief gut / schlecht?
   - Prozessführungsempfehlung für künftige vergleichbare Mandate?
   - BGH- oder OLG-Urteile, die im Mandat relevant waren und für spätere Mandate zu merken sind?

5. **Handakte archivieren (§ 50 BRAO):**
   - Handakte für mind. 6 Jahre nach Mandatsende aufbewahren
   - Elektronische Akte: gleichwertige Sicherung (§ 50 Abs. 2 BRAO)
   - Herausgabepflicht auf Verlangen (§ 50 Abs. 3 BRAO)

6. **Portfolio-Log aktualisieren:** Status in `_log.yaml` auf `archiv` setzen; Abschlussdatum, Ergebnis, Endexposition eintragen.

## Quellen und Zitierweise

Verbindlich: `../references/zitierweise.md`.

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Quellenregel: Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff; keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen.
- BRAO § 50 (Aufbewahrungspflicht Handakten: 6 Jahre); § 43a Abs. 5 BRAO (Fremdgelder).
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Ausgabeformat

```
MANDAT-ABSCHLUSS
──────────────────────────────────────
Mandat-Slug:    [slug]
Schließungsdatum: TT.MM.JJJJ
Typ:            [z. B. Vergleich]
MANDATSGEHEIMNIS – § 43a Abs. 2 BRAO

──────────────────────────────────────
ERGEBNIS
──────────────────────────────────────
Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

──────────────────────────────────────
ENDEXPOSITION
──────────────────────────────────────
Eingeklagter Betrag:       EUR XX.XXX
Vergleichszahlung:         EUR XX.XXX
Kostenerstattung:          EUR X.XXX (§§ 103 ff. ZPO)
Ursprüngliche Schätzung:   EUR XX.XXX – EUR XX.XXX

──────────────────────────────────────
LESSONS LEARNED
──────────────────────────────────────
[Freitext]

──────────────────────────────────────
ARCHIVIERUNG
──────────────────────────────────────
Handakte aufzubewahren bis: TT.MM.JJJJ (§ 50 Abs. 1 BRAO: 6 Jahre)
_log.yaml-Status: archiv
```

## Risiken / typische Fehler

- **Aufbewahrungsfrist übersehen:** § 50 Abs. 1 BRAO: mindestens 6 Jahre nach Mandatsende; kürzere Vernichtung ist Berufsrechtsverletzung.
- **Fremdgelder nicht abgewickelt:** § 43a Abs. 5 BRAO – Fremdgelder (Kostenvorschüsse, Schadensersatzbeträge) unverzüglich weiterleiten; Verzögerung kann zur Strafbarkeit führen (§ 266 StGB).
- **Rechtsmittelfrist läuft noch:** Vor dem Schließen prüfen, ob Berufungs- (§ 517 ZPO: 1 Monat) oder Revisionsfrist (§ 548 ZPO: 1 Monat) noch offen ist; Mandat erst nach Eintritt der Rechtskraft schließen oder Mandanten ausdrücklich auf Verzicht hinweisen.
- **Vollstreckungsverjährung:** Vollstreckungstitel verjähren nach § 197 Abs. 1 Nr. 3 BGB in 30 Jahren; Abschluss nicht ohne Dokumentation der Vollstreckungsmaßnahmen.

<!-- AUDIT 27.05.2026
Halluzinierte Referenz geloescht. Keine Ersatzquelle gefunden.
-->
