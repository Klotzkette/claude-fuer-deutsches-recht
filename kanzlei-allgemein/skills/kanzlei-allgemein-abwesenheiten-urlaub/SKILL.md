---
name: kanzlei-allgemein-abwesenheiten-urlaub
description: "Verwaltet Urlaub Krankmeldungen Fehlzeiten Vertretung Kalenderabstimmung Resturlaub Teamabdeckung. Mit Ablauf fuer Urlaubsantrag Krankmeldung Elternzeit Pflegezeit. Pruefliste Fristen beA Postlauf Mandantenkommunikation Vertretungsregelung. Datenschutz bei Diagnose-Daten. Abwesenheitsregister-Template Eskalation bei Konflikten. Schnittstelle Lohn-SV."
---

# Abwesenheiten, Urlaub, Krankheit

## Zweck

Dieser Skill verwaltet alle Formen der Abwesenheit in einer Kanzlei — von Erholungsurlaub über Krankmeldung bis zu Elternzeit. Er achtet darauf, dass **Fristen, beA-Eingaenge, Postlauf, Mandantenkommunikation und Gerichtstermine** auch in der Abwesenheit abgedeckt bleiben. Verstöße koennen zu Wiedereinsetzung Paragraf 233 ZPO, Haftungsrisiken Paragraf 280 BGB und berufsrechtlichen Folgen (Paragraf 43a BRAO) führen.

## 1) Abwesenheitsarten

| Art | Anlass | Vorlauf | Vertretung erforderlich |
|---|---|---|---|
| Erholungsurlaub | jaehrlicher Anspruch BUrlG | meist 4-6 Wochen | ja |
| Sonderurlaub | persönliche Anlaesse (Heirat, Todesfall) | sofort | ja, soweit möglich |
| Bildungsurlaub | Bildungsfreistellungsgesetze der Länder | 6-8 Wochen Vorlauf | ja |
| Krankheit (AU) | Krankheit mit AU-Bescheinigung | sofort | ja, ad hoc |
| Kind krank | Paragraf 45 SGB V | sofort | ja, ad hoc |
| Mutterschutz | Paragraf 3 MuSchG | nach Bekanntwerden Schwangerschaft | langfristig, Stoppschild |
| Elternzeit | Paragraf 16 BEEG | 7 Wochen vor Beginn | langfristig, Stoppschild |
| Pflegezeit | Paragraf 3 PflegeZG | 10 Tage vor Beginn | langfristig, Stoppschild |
| Fortbildung | bezahlt oder unbezahlt | mit Beleg | ja |
| Homeoffice | mobile Arbeit | je nach Vereinbarung | nicht zwingend, aber Kalenderabstimmung |
| Überstundenausgleich | Zeitkonto | kurzfristig | ja |
| Unbezahlter Urlaub | Sondervereinbarung | je nach Anlass | ja |

## 2) Ablauf Urlaubsantrag

### Schritt 1 — Anfrage erfassen

- Person (mit Funktion)
- Zeitraum (Anfang, Ende, Werktage)
- Anlass (nicht zwingend, aber bei Bildungsurlaub Pflicht)

### Schritt 2 — Resturlaub und Überschneidungen prüfen

- Resturlaub aus dem Vorjahr (Paragraf 7 III BUrlG: Übertrag bis 31.03.)
- Aktueller Urlaubsanspruch des Jahres
- Bereits genehmigter Urlaub
- Überschneidungen mit anderen Teammitgliedern

### Schritt 3 — Operative Prüfung

- **Fristen**: Welche Fristen laufen im Antrags-Zeitraum?
- **Gerichtstermine**: Termine wahrnehmen müssen
- **beA-Eingaenge**: Wer leert das beA-Postfach?
- **Postlauf**: Wer holt die Post ab und sortiert?
- **Telefon**: Wer ist erreichbar?
- **Mandantenkommunikation**: Welche Mandate haben Kommunikationsbedarf?

### Schritt 4 — Vertretung vorschlagen

- Konkret benannte Person je Mandat
- Doppelvertretung bei kritischen Mandaten
- Vertretung dokumentiert (Mandanten-Brief, beA-Mandatsanzeige)

### Schritt 5 — Entscheidung

- Genehmigen
- Genehmigen mit Auflage (z.B. „Vertretung muss von Mandant XY bestätigt werden")
- Rueckfrage (z.B. „Wer vertritt im Mandat 123?")
- Alternativer Zeitraum vorschlagen
- Ablehnen (mit Begründung — selten, meist nur bei Termin-Kollision)

### Schritt 6 — Kalender pflegen

- Kanzlei-Kalender aktualisieren
- Abwesenheitsregister aktualisieren
- Out-of-Office-Mail eingerichtet
- beA-Vertretung Paragraf 31a BRAO eingerichtet

## 3) Ablauf Krankmeldung

### Schritt 1 — Aufnahme

- Wer hat krank gemeldet?
- Wann?
- Voraussichtliche Rückkehr?
- AU-Bescheinigung vorhanden (Paragraf 5 EFZG: nach 3 Tagen Pflicht, Tarif/Arbeitsvertrag oft früher)

### Schritt 2 — Ad-hoc-Vertretung

- Welche Termine in den nächsten Tagen?
- Welche Fristen in der laufenden Woche?
- beA-Eingang täglich prüfen lassen
- Telefon-Umleitung

### Schritt 3 — Lohn/SV-Hinweis

- Bei Krankheit > 6 Wochen: Hinweis an Lohnbuchhaltung
- Anschluss-Skill: `kanzlei-allgemein-lohn-sv`

### Schritt 4 — Datenschutz

- **Diagnose nicht erfassen**, außer für Krankengeld-Antrag erforderlich
- AU-Bescheinigung beinhaltet keinen Befund — das ist gesetzlich so
- Bei eAU (elektronische AU): keine Papier-Bescheinigung mehr beim AG, sondern Abruf bei der Kasse Paragraf 109 SGB IV

## 4) Vertretungsregelung — Prüfliste

- [ ] **Vertretung benannt** je laufendem Mandat?
- [ ] **Mandanten benachrichtigt**, soweit Vertretung Außenwirkung hat?
- [ ] **beA-Vertretung** eingerichtet Paragraf 31a III BRAO?
- [ ] **Out-of-Office-Mail** eingerichtet (mit Vertretung-Hinweis)?
- [ ] **Telefon-Umleitung** oder Vertretung am Telefon?
- [ ] **Postzustellung**: wer leert das Postfach?
- [ ] **Fristen-Kalender** an Vertretung weitergegeben?
- [ ] **Schlüssel/Zugang** zu Akten, soweit erforderlich?

## 5) Eskalation bei Konflikten

| Konflikt | Mechanismus |
|---|---|
| Urlaubswunsch kollidiert mit Gerichtstermin | Termin priorisieren; ggf. Verlegungsantrag |
| Zwei Mitarbeiter wollen gleichen Zeitraum | Vorrang nach Antragseingang, sonst Abwaegung Familie/Kinder |
| Wiederholte Kurzkrankmeldungen | Personalgespräch; ggf. BEM Paragraf 167 II SGB IX bei > 6 Wochen pro Jahr |
| Geplante Elternzeit | Stoppschild — Personalplanung mindestens 6 Monate vor Mutterschutzbeginn |
| Kurzfristige Krankmeldung am Tag eines Gerichtstermins | Sofort-Vertretung organisieren; Termin nur in dringendsten Fällen verlegen |

## 6) Abwesenheitsregister-Template

```
| Person | Art         | Anfang     | Ende       | Vertretung      | Status   |
|--------|-------------|------------|------------|-----------------|----------|
| RA Mueller | Urlaub  | 01.07.2026 | 14.07.2026 | RA Schmidt, RAin Weber (Mandat 312) | genehmigt |
| RAin Weber | Krank   | 15.06.2026 | offen      | RA Mueller       | laufend  |
| ReFa Bauer | Bildung | 03.09.2026 | 04.09.2026 | ReFa Klein       | genehmigt |
```

Vorlage unter `assets/templates/abwesenheiten-register.md`.

## 7) Datenschutz

- **Diagnose-Daten nicht erfassen.** Im Personalakten-Eintrag genuegt Zeitraum.
- **AU-Bescheinigung** ist personenbezogenes Gesundheitsdatum Art. 9 DSGVO — gesonderte Aufbewahrung.
- **Mandanten erfahren keine Diagnose.** Es genuegt: „RA Mueller ist erkrankt, Vertretung übernimmt RA Schmidt."
- **Vertretungsanzeige** an Mandanten nur mit Mandantenbezug, nicht generell.

## 8) Typische Fehler

1. **Vertretung nicht im beA hinterlegt.** Folge: Zustellungen kommen nicht an, Frist-Versaeumung.
2. **Out-of-Office-Mail ohne Vertretung.** Mandanten warten, Frust und ggf. Haftung.
3. **Gerichtstermin in Urlaub übersehen.** Folge: Saeumnis Paragraf 330 ZPO, Wiedereinsetzung Paragraf 233 ZPO nur bei Verschuldensfreiheit.
4. **Bildungsurlaub-Antrag zu spaet.** Bundesländer-Fristen 6-8 Wochen.
5. **Krankheit über 6 Wochen nicht an Lohnbuchhaltung gemeldet.** Folge: falsche Lohnabrechnung, Krankengeld-Verzug.
6. **Diagnose in Personalakte.** DSGVO-Verstoß.
7. **Elternzeit-Anzeige ohne 7-Wochen-Vorlauf.** Folge: Beginn verschiebt sich.

## 9) Schnittstellen

- `kanzlei-allgemein-lohn-sv` — bei Krankheit > 6 Wochen, Mutterschutz, Elternzeit
- `kanzlei-allgemein-hr-personal` — Personalakte, Resturlaubs-Konto, Vertragsfragen
- `kanzlei-allgemein-fristen-monitor` — Fristen-Vertretung während Abwesenheit
- `kanzlei-allgemein-kanzleikalender` — Termin-Vertretung und Kalender-Synchronisation
- `kanzlei-allgemein-bea-journal` — beA-Vertretung Paragraf 31a III BRAO
- `kanzlei-allgemein-postlauf` — Postzustellung und -bearbeitung während Abwesenheit
- `kanzlei-allgemein-output-versand` — Vertretungsanzeige in der Mandanten-Korrespondenz
