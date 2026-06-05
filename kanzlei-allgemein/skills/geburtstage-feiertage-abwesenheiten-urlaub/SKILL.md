---
name: geburtstage-feiertage-abwesenheiten-urlaub
description: "Geburtstage Feiertage Abwesenheiten Urlaub: bündelt 2 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Geburtstage Feiertage Abwesenheiten Urlaub

## Arbeitsbereich

Dieser Skill bündelt 2 sachlich verwandte Arbeitsschritte rund um **Geburtstage Feiertage Abwesenheiten Urlaub** im Plugin Kanzlei-Allgemein. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `geburtstage-feiertage` | Pflegt einen Mandanten- und Geschäftspartner-Geburtstagsverteiler. Reminders einige Tage vor dem Tag. Vorlagen für kurze persoenliche Glueckwunsch-E-Mail (formell-warm). Bei Geschäftspartnern auch Firmenjubilaeen. Geburtstagsverteiler getrennt von Mandantenfaellen — Pflege als Geschäftspartnerstamm. Datenschutz beachten Art. 6 Abs. 1 lit. f DSGVO berechtigtes Interesse Geburtstagsglueckwunsch zulässig; Widerspruchsrecht Mandant beachten. |
| `kanzlei-allgemein-abwesenheiten-urlaub` | Verwaltung von Abwesenheiten in der Kanzlei — Urlaub Krankmeldung Elternzeit Pflegezeit Fortbildung. Anwendungsfall Anwalt oder Mitarbeiter meldet Urlaub oder Krankheit und Kanzlei muss Vertretung für Fristen beA Postlauf Mandantenkommunikation sicherstellen. Normen § 7 BUrlG Resturlaub § 16 BEEG Elternzeit § 3 PflegeZG Kurzpflegezeit Art. 6 DSGVO Diagnosedaten. Prüfraster Überschneidungen Fristencheck beA-Abdeckung Postlauf-Vertretung Teamkonflikt. Output Urlaubsplan Vertretungsregelung Abwesenheitsregister Eskalationsprotokoll Schnittstelle Lohn-SV. Abgrenzung zu Lohn-SV-Skill und Kanzleikalender. |

## Arbeitsweg

Im Plugin Kanzlei-Allgemein gilt für **Geburtstage Feiertage Abwesenheiten Urlaub**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `geburtstage-feiertage`

**Fokus:** Pflegt einen Mandanten- und Geschäftspartner-Geburtstagsverteiler. Reminders einige Tage vor dem Tag. Vorlagen für kurze persoenliche Glueckwunsch-E-Mail (formell-warm). Bei Geschäftspartnern auch Firmenjubilaeen. Geburtstagsverteiler getrennt von Mandantenfaellen — Pflege als Geschäftspartnerstamm. Datenschutz beachten Art. 6 Abs. 1 lit. f DSGVO berechtigtes Interesse Geburtstagsglueckwunsch zulässig; Widerspruchsrecht Mandant beachten.

# Geburtstage und Feiertage


## Triage zu Beginn
1. Liegt eine Einwilligung des Empfaengers vor, oder wird auf berechtigtes Interesse (Art. 6 Abs. 1 lit. f DSGVO) gestuetzt?
2. Sollen postalische Karten, E-Mails oder digitale Nachrichten versandt werden?
3. Gibt es einen Widerspruch (Art. 21 DSGVO) einzelner Empfaenger zu beruecksichtigen?
4. Betrifft der Versand Verbraucher (strenger Datenschutz) oder Geschaeftskunden?

## Aktuelle Rechtsprechung
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zentrale Normen
- Art. 6 Abs. 1 lit. f DSGVO — Berechtigtes Interesse als Rechtsgrundlage fuer Mandantenpflege-Kontakte
- Art. 21 DSGVO — Widerspruchsrecht: muss ohne Schranken moeglich sein
- Art. 5 Abs. 1 lit. c DSGVO — Datensparsamkeit: nur notwendige Daten speichern
- § 7 UWG — Unzumutbare Belaestigung bei Werbung ohne Einwilligung

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Pflege des Verteilers

### Quellen

- Mandantenstammdaten aus `mandantenakte-anlegen`.
- Geschäftspartner (Steuerberater Notar Sachverständige Kollegen).
- Eingangsbedingung: ausdrückliche oder konkludente Einwilligung des Empfängers.

### Datenmodell

```yaml
- name: Mueller, Hans
 geburtstag: 1972-08-15
 funktion: Geschäftsführer Mueller GmbH (Mandant Aktenkreis 2026/0042)
 ansprache: foermlich # foermlich / vornamen / locker
 versandweg: e-mail
 e-mail: hmueller@mueller-gmbh.de
 vorlauf-tage: 2
 letzte-glueckwuensche: 2025-08-14
 widerspruch-eingelegt: false
```

### Datenschutz

- **Art. 6 Abs. 1 lit. f DSGVO** berechtigtes Interesse — Mandantenpflege ist allgemein zulässig.
- **Widerspruchsrecht** beachten — auf Widerspruch hin Eintrag deaktivieren.
- **Information bei Mandatsbeginn** (Datenschutzhinweis Art. 13 DSGVO) auf mögliche Glückwunschsendungen.
- **Verarbeitungsverzeichnis** nach Art. 30 DSGVO ergänzen.

## Tagesbrief-Integration

Im `sekretariats-tagesbrief` morgens Eintrag:

```
Heute / in den nächsten Tagen Geburtstag:
- 22.05.2026 Hans Mueller, Geschäftsführer Mueller GmbH — Glückwunsch vorbereiten
- 24.05.2026 RA Dr. Schulz, Kollege Kanzlei XYZ — kurze Mail
```

## Vorlagen

### Förmlich

```
Betreff: Herzliche Glückwünsche zum Geburtstag

Sehr geehrter Herr [Nachname],

zu Ihrem heutigen Geburtstag übermittle ich Ihnen meine besten persoenlichen
Glückwünsche. Ich wünsche Ihnen vor allem Gesundheit Zufriedenheit und
Erfolg im neuen Lebensjahr.

Mit freundlichen Grüßen
[Anwalt]
```

### Vertraut (langjaehriger Geschäftspartner)

```
Betreff: Alles Gute zum Geburtstag

Lieber [Vorname],

zu Ihrem heutigen Geburtstag herzliche Glückwünsche. Vielen Dank für die
gute und vertrauensvolle Zusammenarbeit im vergangenen Jahr.

Beste Grüße aus der Kanzlei
[Anwalt]
```

## Firmenjubiläen

- Erfassung des Gründungsdatums (Handelsregister) bei juristischen Personen als Mandanten.
- 10 25 50 75 100 Jahre als Schwellen.
- Bei runder Jahreszahl: persönliche Glückwunschkarte zusätzlich zur E-Mail.

## Feiertagsversand

- Weihnachten: siehe Skill `weihnachtskarten`.
- Ostern Neujahr: optional je nach Kanzlei.

## Sicherheits-Check

- Vor Versand: Empfänger noch aktiv? Lebt noch? Mandat nicht beendet im Streit?
- Bei Streit beendeten Mandaten: Eintrag manuell deaktivieren oder löschen.

## Audit

- Letzte Versendung dokumentiert (vermeidet Doppelversand und ermöglicht Auswertung).
- Bei Widerspruch unverzueglich löschen oder anonymisieren (DSGVO Art. 17).

## Ausgabe

- Aktualisierter Geburtstagsverteiler.
- Tagesbrief-Eintrag.
- Versand-E-Mails als Entwurf zur Freigabe.

## 2. `kanzlei-allgemein-abwesenheiten-urlaub`

**Fokus:** Verwaltung von Abwesenheiten in der Kanzlei — Urlaub Krankmeldung Elternzeit Pflegezeit Fortbildung. Anwendungsfall Anwalt oder Mitarbeiter meldet Urlaub oder Krankheit und Kanzlei muss Vertretung für Fristen beA Postlauf Mandantenkommunikation sicherstellen. Normen § 7 BUrlG Resturlaub § 16 BEEG Elternzeit § 3 PflegeZG Kurzpflegezeit Art. 6 DSGVO Diagnosedaten. Prüfraster Überschneidungen Fristencheck beA-Abdeckung Postlauf-Vertretung Teamkonflikt. Output Urlaubsplan Vertretungsregelung Abwesenheitsregister Eskalationsprotokoll Schnittstelle Lohn-SV. Abgrenzung zu Lohn-SV-Skill und Kanzleikalender.

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
- Genehmigen mit Auflage (z.B. "Vertretung muss von Mandant XY bestätigt werden")
- Rueckfrage (z.B. "Wer vertritt im Mandat 123?")
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
| Person | Art | Anfang | Ende | Vertretung | Status |
|--------|-------------|------------|------------|-----------------|----------|
| RA Mueller | Urlaub | 01.07.2026 | 14.07.2026 | RA Schmidt, RAin Weber (Mandat 312) | genehmigt |
| RAin Weber | Krank | 15.06.2026 | offen | RA Mueller | laufend |
| ReFa Bauer | Bildung | 03.09.2026 | 04.09.2026 | ReFa Klein | genehmigt |
```

Vorlage unter `assets/templates/abwesenheiten-register.md`.

## 7) Datenschutz

- **Diagnose-Daten nicht erfassen.** Im Personalakten-Eintrag genuegt Zeitraum.
- **AU-Bescheinigung** ist personenbezogenes Gesundheitsdatum Art. 9 DSGVO — gesonderte Aufbewahrung.
- **Mandanten erfahren keine Diagnose.** Es genuegt: "RA Mueller ist erkrankt, Vertretung übernimmt RA Schmidt."
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


## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.
