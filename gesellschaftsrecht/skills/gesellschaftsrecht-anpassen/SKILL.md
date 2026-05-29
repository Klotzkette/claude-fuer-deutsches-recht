---
name: gesellschaftsrecht-anpassen
description: 'Geführte Anpassung des gesellschaftsrechtlichen Praxisprofils — einzelne Einstellung ändern, ohne das vollständige Ersteinrichtungs-Interview neu durchzuführen. Risikoprofil, Eskalationskontakte, aktive Module (M&A / Governance / Kapitalmarkt / Gesellschaftsverwaltung), Wesentlichkeitsschwellen, Beschlussformat oder Mandatsworkspace-Pfade anpassen. Lädt, wenn der Nutzer "Profil ändern", "Konfiguration aktualisieren", "Einstellung anpassen" oder vergleichbare Formulierungen verwendet.'

---

# Praxisprofil anpassen

## Triage zu Beginn

Vor der Profilanpassung klaeren:

1. **Profil vorhanden?** Existiert eine CLAUDE.md mit abgeschlossenem Kaltstart-Interview? Falls nicht: `gesellschaftsrecht-kaltstart-interview` zuerst ausfuehren.
2. **Was soll geaendert werden?** Ein Abschnitt (Wesentlichkeitsschwelle, Modul, Risikoprofil, Person) oder mehrere Abschnitte? — Pro Durchlauf nur eine Aenderung.
3. **Modul-Aktivierung?** Wird ein bisher inaktives Modul aktiviert (z.B. Kapitalmarkt)? Dann sind Folge-Einrichtungsfragen zu stellen.
4. **Rechtsrelevante Aenderung?** Betrifft die Aenderung Normschwellen (z.B. Wesentlichkeitsschwelle M&A) oder Verfahrensregeln (z.B. Beschlussformat)? Dann rechtliche Downstream-Konsequenz erklaeren.
5. **Downstream-Wirkung?** Welche anderen Skills werden von der Aenderung beeinflusst? (Tabelle der konfigurierbaren Bereiche zeigen)

## Zweck

Der Nutzer möchte eine einzelne Einstellung im Praxisprofil ändern — ein Risikoprofil, einen Eskalationskontakt, einen Modulschalter, ein Ausgabeformat — ohne das vollständige Ersteinrichtungs-Interview zu wiederholen und ohne YAML manuell zu bearbeiten.

## Eingaben

- Aktuelle CLAUDE.md (Praxisebene) und ggf. Unternehmensprofil
- Beschreibung der gewünschten Änderung (Freitext oder Abschnittsbenennung)
- Bei modulspezifischen Änderungen: ggf. neue Seed-Dokumente

## Rechtlicher Rahmen

Das Praxisprofil bildet den rechtlichen Rahmen der vom Nutzer betreuten Mandate ab. Änderungen an Wesentlichkeitsschwellen, Modulen oder Eskalationslogiken haben unmittelbare Auswirkungen auf sämtliche Skill-Ausgaben.

Relevante Vorschriften je Bereich (Referenz für Konsistenzprüfung):
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Mitbestimmung: MitbestG, DrittelbG — eine Moduländerung, die ein mitbestimmungspflichtiges Unternehmen betrifft, ist zu flaggen
- Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen zitieren. Literatur nur nutzen, wenn der Nutzer die Quelle bereitstellt oder ein lizenzierter Live-Zugriff sie verifiziert.
- Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen zitieren. Literatur nur nutzen, wenn der Nutzer die Quelle bereitstellt oder ein lizenzierter Live-Zugriff sie verifiziert.

## Ablauf

### Schritt 1: Praxisprofil lesen

CLAUDE.md und Unternehmensprofil lesen. Falls das Plugin-Profil nicht existiert oder noch `[PLATZHALTER]`-Werte enthält:

> Sie haben die Ersteinrichtung noch nicht abgeschlossen. Führen Sie zunächst `/gesellschaftsrecht:gesellschaftsrecht-kaltstart-interview` aus — die Anpassungsfunktion setzt ein bestehendes Praxisprofil voraus.

### Schritt 2: Anpassungsübersicht zeigen

Liste der konfigurierbaren Bereiche mit aktuellen Werten:

- **Unternehmen / Wer Sie sind** — Name, Branche, Rechtsform, Sitz, Tätigkeitssetting *(gemeinsam genutzt über alle Plugins — Änderungen wirken in `unternehmens-profil.md`)*
- **Aktive Module** — welche von M&A, Governance/Beschlussfassung, Kapitalmarkt, Gesellschaftsverwaltung aktiv sind. Ein- und Ausschalten ändert, welche Skills Setup-Hinweise einblenden.
- **Risikoprofil** — konservativ / ausgewogen / progressiv; Bedeutung für Due-Diligence-Wesentlichkeit und Offenlegungsumfang
- **Personen** — Transaktionsteam, verantwortlicher Geschäftsführer/Vorstand, Gesellschaftsverwaltungsverantwortlicher, Eskalationskette
- **M&A-Modul** — Wesentlichkeitsschwellen (Vertragswert, Mitarbeiteranzahl, Umsatz), zugelassene VDR-Plattformen, KI-Massenreview-Vertrauensstufe, Briefing-Turnus des Transaktionsteams
- **Governance-Modul** — Hausbeschlussformat, bevorzugte Unterzeichner, Ausschussstruktur, Notaranforderungen
- **Kapitalmarkt-Modul** — Berichterstattungskalender, BaFin-Meldepflichten, Hauptversammlungs-Turnus
- **Gesellschaftsverwaltungs-Modul** — Gesellschaftstabelle, Registerführung, Jahresabschluss-Pflichten
- **Ablauf** — Mandatsworkspaces, Schließungscheckliste, VDR-Pfad
- **Integrationen** — Box / Intralinks / Datasite / Handelsregister / Datenraum-Status und Fallbacks

### Schritt 3: Änderungswunsch erfragen

> Was möchten Sie anpassen? Wählen Sie einen Abschnitt, oder beschreiben Sie die Änderung in eigenen Worten.

### Schritt 4: Änderung durchführen

Aktuellen Wert zeigen, neuen Wert abfragen, Downstream-Auswirkungen erläutern, bestätigen, in die Konfiguration schreiben.

Beispiele:
- *Wesentlichkeitsschwelle 250.000 EUR → 500.000 EUR:* "`/Due-Diligence-Extraktion` und `/Material-Vertragsverzeichnis` verwenden künftig 500.000 EUR als Grenzwert. Bestehende Findings bleiben unverändert; bei rückwirkender Anwendung bitte neu ausführen."
- *Kapitalmarkt-Modul aktivieren:* "Beim nächsten Aufruf eines kapitalmarktrechtlichen Skills werden Sie nach Berichterstattungskalender und BaFin-Pflichten gefragt."
- *KI-Massenreview-Vertrauen "jede Zeile prüfen" → "10 % Stichprobe":* "`/KI-Tool-Übergabe` prüft künftig eine 10 %-Stichprobe statt jeder Extraktion."

### Schritt 5: Änderungen an Unternehmensprofil

Bei Änderungen an Unternehmensname, Branche, Sitz, Tätigkeitssetting, Rechtsform: in `unternehmens-profil.md` schreiben und hinweisen:

> Diese Änderung betrifft alle Plugins — jedes Plugin, das Ihren Jurisdiktionsbereich liest, sieht ab sofort [neuer Wert].

### Schritt 6: Abschluss

> Fertig. Ihre nächste Ausgabe spiegelt die Änderung wider. Weitere Anpassungen? Sie können `/gesellschaftsrecht:gesellschaftsrecht-anpassen` jederzeit erneut aufrufen.

## Ausgabeformat

- Bestaetigung der Aenderung mit Vorher-/Nachher-Wert
- Hinweis auf betroffene Skills
- Ggf. Inkonsistenzwarnung (s. u.)

## Output-Template

**Adressat:** Praxis-Nutzer / Kanzlei-intern — Tonfall: sachlich-bestaedigend, handlungsanleitend

```
PROFILANPASSUNG GESELLSCHAFTSRECHT
Datum: [TT.MM.JJJJ]
Geaenderter Abschnitt: [ABSCHNITTSNAME]

--- AENDERUNG ---
VORHER: [ALTER WERT]
NACHHER: [NEUER WERT]

--- BETROFFENE SKILLS ---
Diese Aenderung wirkt auf folgende Skills:
- [SKILL 1]: [BESCHREIBUNG DER AUSWIRKUNG]
- [SKILL 2]: [BESCHREIBUNG DER AUSWIRKUNG]
Rueckwirkende Anwendung auf bestehende Daten: [NEIN / NUR AUF ANFRAGE]

--- INKONSISTENZ-PRUEFUNG ---
[KEIN KONFLIKT ERKANNT]
oder:
Konflikt erkannt: [BESCHREIBUNG] — Empfehlung: [HANDLUNGSHINWEIS]

--- BESTAEIGUNG ---
Praxisprofil gespeichert. Naechste Ausgabe verwendet den neuen Wert.
Weitere Anpassungen: `/gesellschaftsrecht:gesellschaftsrecht-anpassen` erneut aufrufen.
```

## Rote Schwellen

- **Wesentlichkeitsschwelle M&A auf null oder sehr niedrig gesetzt** — alle Vertraege werden als wesentlich geflaggt; DD-Tools werden unbrauchbar; Wert ueberdenken.
- **Modul deaktiviert, obwohl aktive Mandate dieses Modul nutzen** — laufende Mandate koennen Skills nicht mehr laden; erst nach Abschluss aller Mandate in diesem Bereich deaktivieren.
- **Schutzfunktionen (\"pruefen\"-Flags, Quellenhinweise) entfernt** — haftungsrechtliches Risiko; vor Entfernung Trade-off ausfuehrlich erklaeren.
- **Mehrere Abschnitte in einem Durchlauf geaendert** — Downstream-Konflikte schwer nachverfolgbar; eine Aenderung pro Durchlauf.

## Beispiel

**Szenario:** Wesentlichkeitsschwelle für Vertragsreview von 100.000 EUR auf 250.000 EUR erhöhen.

Ausgabe: "Wesentlichkeitsschwelle geändert: 100.000 EUR → 250.000 EUR. `/Due-Diligence-Extraktion` und `/Material-Vertragsverzeichnis` wenden den neuen Wert an. Bestehende Findings bleiben unverändert."

## Risiken und typische Fehler

- **Abschnitte löschen.** Wenn der Nutzer etwas "entfernen" möchte, Wert auf `[Nicht konfiguriert]` setzen und Auswirkung erläutern.
- **Interne Inkonsistenz ignorieren.** Wenn die Änderung das Profil inkonsistent macht (z.B. Kapitalmarkt-Modul deaktiviert + "BaFin-Kontakt" in Eskalationsmatrix; oder konservatives Risikoprofil + sehr hohe Schwellenwerte), Spannung flaggen.
- **Schutzfunktionen degradieren.** Das `[überprüfen]`-Flag, Quellenangaben auf abgerufenen Dokumenten und `[verifizieren]`-Tags auf zitierten Entscheidungen sind inhaltlich tragende Elemente — Trade-off vor Entfernung erläutern.
- **Mehrere Änderungen gleichzeitig.** Eine Änderung pro Durchlauf, kein Re-Interview.

## Quellenpflicht

Bei Änderungen, die rechtliche Schwellenwerte oder Verfahrensregeln betreffen:
- Einschlägige Norm zitieren: `§ 48 Abs. 2 GmbHG`, `Art. 17 Abs. 1 MAR`
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen zitieren. Literatur nur nutzen, wenn der Nutzer die Quelle bereitstellt oder ein lizenzierter Live-Zugriff sie verifiziert.

Hinweis: Dieser Skill ersetzt keine anwaltliche Beratung im konkreten Einzelfall.
