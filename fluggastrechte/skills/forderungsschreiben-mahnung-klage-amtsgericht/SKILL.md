---
name: forderungsschreiben-mahnung-klage-amtsgericht
description: "Forderungsschreiben Mahnung Klage Amtsgericht: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Forderungsschreiben Mahnung Klage Amtsgericht

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Forderungsschreiben Mahnung Klage Amtsgericht** im Plugin Fluggastrechte (VO 261/2004). Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `forderungsschreiben-mahnung` | Zweite Stufe nach Ablauf der Frist aus dem ersten Forderungsschreiben oder nach erfolgloser Reaktion der Airline. Setzt Nachfrist (typisch zehn Tage) bezieht sich auf die erste Forderung weist Verzugszinsen aus und droht konkret SOEP-Schlichtung oder Klage zum Amtsgericht. Bei Reaktion der Airline mit Standardausreden Verweis auf den Skill `airline-standardausreden-prüfen` zur Konfrontation mit Pinpoint auf EuGH-Rechtsprechung. |
| `klage-amtsgericht-fluggast` | Prüffeld für klage amtsgericht fluggast: prüft Normtext, Nutzerangaben, Fristen, Belege und verifizierte Rechtsprechung mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle. |
| `pauschalreise-statt-flug-pruefen` | Pauschalreise gegen Flug-Einzelbuchung: Reiseveranstalterhaftung nach §§ 651a ff. BGB, Pauschalreise-RL EU 2015 2302. Minderung, Schadensersatz, Ruecktritt. Verhaeltnis zur VO 261 (kumulativ moeglich, Anrechnung nach BGH). Pruefraster ob Pauschalreise vorliegt. |

## Arbeitsweg

Im Plugin Fluggastrechte (VO 261/2004) gilt für **Forderungsschreiben Mahnung Klage Amtsgericht**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `forderungsschreiben-mahnung`

**Fokus:** Zweite Stufe nach Ablauf der Frist aus dem ersten Forderungsschreiben oder nach erfolgloser Reaktion der Airline. Setzt Nachfrist (typisch zehn Tage) bezieht sich auf die erste Forderung weist Verzugszinsen aus und droht konkret SOEP-Schlichtung oder Klage zum Amtsgericht. Bei Reaktion der Airline mit Standardausreden Verweis auf den Skill `airline-standardausreden-prüfen` zur Konfrontation mit Pinpoint auf EuGH-Rechtsprechung.

# Forderungsschreiben — Mahnung (zweite Stufe)

## Voraussetzung

Erstes Forderungsschreiben aus Skill `forderungsschreiben-erste-stufe` ist versendet — Frist ist abgelaufen oder Airline hat ablehnend reagiert.

## Struktur

```
Betreff: Mahnung — Forderung Ausgleichszahlung gemäß Art. 7 VO (EG)
 Nr. 261/2004 — Flug [Flugnummer] vom [Datum]
 Buchungscode [PNR]
 Mein voriges Schreiben vom [Datum erste Stufe]

Sehr geehrte Damen und Herren,

Sie haben auf mein Schreiben vom [Datum] [nicht reagiert / ablehnend
geantwortet]. Die hierin gestellten Forderungen sind weiterhin offen.

Zu Ihrer ablehnenden Begründung [bei Ablehnung]:

 "[Zitat Airline-Begründung]"

Diese Begründung verfaengt nicht. Bei [technischer Defekt / Streik der
eigenen Mitarbeiter / Crew-Engpass / sonstige Standardausrede] handelt es
sich nach ständiger EuGH-Rechtsprechung regelmäßig NICHT um
außergewöhnliche Umstaende im Sinn des Art. 5 Abs. 3 VO 261/2004:

 Bei technischem Defekt: EuGH, Urt. v. 22.12.2008, C-549/07 (Wallentin-Hermann) — technische Defekte sind grundsaetzlich Teil der normalen Tätigkeit eines Luftfahrtunternehmens.
 [Volltext und Randnummer vor Versand in curia.europa.eu aufrufen
 und passende Aktenzeichen-Linie ergaenzen — z.B. bei Streik der
 eigenen Mitarbeiter EuGH-Linie, bei Personalmangel C-405/23
 (16.5.2024), bei Vorverlegung C-394/23 (9.1.2025).]

Die Beweislast für außergewöhnliche Umstaende und für die Ergreifung
aller zumutbaren Maßnahmen liegt bei Ihnen.

Ich setze hiermit eine letzte Frist zur Zahlung des offenen Betrags von

 [Gesamtbetrag] EUR
 zuzueglich Verzugszinsen seit [Datum erste Frist + 1] in Höhe von
 5 Prozentpunkten über dem Basiszinssatz gemäß § 288 Abs. 1 BGB

bis spaetestens [Datum + 10 Tage].

Sollten Sie die Zahlung nicht fristgerecht leisten werde ich:

 a) die Schlichtungsstelle für den öffentlichen Personenverkehr SOEP
 anrufen — kostenfrei für Verbraucher,
 b) anschliessend Klage zum zuständigen Amtsgericht erheben.

Im Klagefall werden Sie zudem die Gerichtskosten Anwaltskosten und alle
ueberfälligen Verzugszinsen zu tragen haben. Die sachliche Zuständigkeit
des Amtsgerichts ergibt sich aus § 23 Nr. 1 GVG bei Streitwerten bis
zehntausend Euro (i. d. F. seit 01.01.2026). Die oertliche Zuständigkeit
ergibt sich aus § 29 ZPO i.V.m. Art. 7 Nr. 1 lit. b VO (EU) 1215/2012
(Brüssel-Ia) wahlweise am Abflughafen oder am
Zielflughafen oder aus § 13 ZPO Ihrem Sitz / Niederlassung in Deutschland.

Mit freundlichen Grüßen

[Unterschrift]
[Name]
```

## Standard-Gegenargumente

Wenn die Airline mit einer typischen Begründung argumentiert siehe Skill
`airline-standardausreden-pruefen` — dort sind die EuGH-Pinpoints aufgelistet:

| Airline-Begründung | Kerngegenargument | Rspr. (offene Quelle curia.europa.eu) |
|---|---|---|
| "Technischer Defekt" | nicht außergewöhnlich | EuGH C-549/07 (Wallentin-Hermann, 22.12.2008) |
| "Crew-Engpass" | nicht außergewöhnlich | st. Rspr. — Teil normalen Betriebs |
| "Streik eigener Mitarbeiter" | nicht außergewöhnlich | EuGH-Linie zum Personal — konkrete Aktenzeichen in curia.europa.eu vor Versand verifizieren |
| "Vorverlegung um wenige Stunden" | bei mehr als 1 h: Annullierung | EuGH C-394/23 (9.1.2025); C-146/20 u.a. (21.12.2021) |
| "Sie haben uns nicht innerhalb von 30 Tagen informiert" | VO 261/2004 sieht keine solche Frist vor | Verjährung drei Jahre § 195 BGB |
| "Sie haben Umbuchung akzeptiert" | Akzeptanz schließt Ausgleichsanspruch nicht aus | EuGH ständig |
| "Sie haben Voucher erhalten" | wenn nicht ausdrücklich als Ausgleichszahlung gewidmet — kein Ausschluss | st. Rspr. |
| "Vorflug aus Vortag verspätet" | regelmäßig nicht außergewöhnlich (Kette aus Routine-Folge) | st. Rspr. EuGH |

## Versand

- **Einschreiben mit Rückschein** wie Erststufe.
- Parallel **E-Mail an Kundenservice** mit Bezugnahme auf die erste Mahnung.

## Nächster Schritt

- Bei weiterer Untätigkeit: **SOEP-Schlichtungsverfahren** oder **Klage** zum Amtsgericht.
- SOEP-Verfahren ist kostenfrei und oft erfolgreich. Voraussetzung: keine anhängige Klage.
- Klage als letzter Schritt — Skill `klage-amtsgericht-fluggast`.

## Ausgabe

- `mahnung-zweite-stufe-<datum>.docx` und PDF.
- Eintrag im Tagesplan — Reaktionsfrist gesetzt.

## Anlagen-Übergabe

Unmittelbar nach Erstellung des Schreibens den Skill `fluggastrechte-anlagen-bauen` aufrufen.

Übergabe-Schema:

```yaml
schriftsatz: mahnung-zweite-stufe-<datum>.docx
rohbelege_verzeichnis: <fall>/belege/
ausgabeverzeichnis: <fall>/anlagen/
bundle: true
schriftgrad_stempel: 12
schrift_stempel: Arial-Bold
bezeichnung: "Anlage K"
```

Wichtig: Die Mahnung nimmt regelmäßig dieselben Anlagen wie das Erstschreiben in Bezug **plus** das erste Forderungsschreiben selbst und ggf. die Antwort der Airline. Vor Übergabe sicherstellen, dass im Schriftsatz alle benötigten Anlagen mit "Anlage K N" benannt sind — der Skill zieht die Reihenfolge aus dem Text.

## Zentrale Anspruchsgrundlagen & Normen

- Art. 7 VO (EG) Nr. 261/2004 — Ausgleichszahlung 250/400/600 EUR je nach Distanz
- Art. 5 Abs. 3 VO (EG) Nr. 261/2004 — Entlastungsbeweis aussergewoehnliche Umstaende (Beweislast Airline)
- § 286 Abs. 1 BGB — Verzug bei fruchtlosem Fristablauf
- § 288 Abs. 1 BGB — Verzugszinsen 5 Prozentpunkte ueber Basiszinssatz
- § 195 BGB — Regelmaessige Verjährungsfrist drei Jahre
- § 199 Abs. 1 BGB — Verjährungsbeginn Schluss des Jahres der Kenntnis

## Aktuelle Rechtsprechung (Stand Mai 2026; offene Quelle curia.europa.eu)

- EuGH, Urt. v. 19.11.2009, C-402/07 und C-432/07 (Sturgeon u.a.) — 3-Stunden-Schwelle
- EuGH, Urt. v. 22.12.2008, C-549/07 (Wallentin-Hermann) — techn. Defekt kein außergewöhnlicher Umstand
- EuGH, Urt. v. 26.2.2013, C-11/11 (Folkerts) — Endziel-Verspätung Anschlussflüge
- EuGH, Urt. v. 9.1.2025, C-394/23 — Vorverlegung als Annullierung
- EuGH, Urt. v. 13.6.2025, C-411/23 — versteckter Konstruktionsfehler Triebwerk
- EuGH, Urt. v. 16.10.2025, C-399/24 — Blitzschlag

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Triage vor Mahnung — Checkliste

1. Erste Stufe versendet und Frist abgelaufen? → Datum prüfen (typisch 14 Tage nach Erstschreiben)
2. Airline hat ablehnend geantwortet? → Antwort-Text kopieren und in Mahnung zitieren
3. Airline hat gar nicht geantwortet? → Hinweis auf Untätigkeit formulieren
4. Anspruch noch nicht verjährt? → § 195/199 BGB: drei Jahre ab Jahresende des Flugjahres
5. SOEP-Schlichtung bereits beantragt? → falls ja, Klage erst nach Abschluss

## Adressat & Tonfall

Adressat: Airline-Kundendienst / Rechtsabteilung — Tonfall scharf-fristsetzend, aber sachlich-juristisch; keine persoenlichen Vorwuerfe

## 2. `klage-amtsgericht-fluggast`

**Fokus:** Prüffeld für klage amtsgericht fluggast: prüft Normtext, Nutzerangaben, Fristen, Belege und verifizierte Rechtsprechung mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle.

# Klage zum Amtsgericht (Fluggastrechte)

## Disclaimer (Schlüsselstelle)

Eine Klage ist ein Rechtsschriftsatz mit Konsequenzen (Gerichtskosten Streitwert-Risiko Auslagen). Vor Einreichung Beweislage prüfen — auf konkrete Vorhalt-Antworten der Airline reagieren können. Bei komplexen Fällen anwaltliche Hilfe einholen — Rechtsschutzversicherung prüfen.

## Voraussetzungen

- **Schriftform** des Klageantrags (§ 253 ZPO).
- **Klagepartei** ist der Anspruchsteller (jeder Passagier eigener Anspruch — Streitgenossenschaft möglich nach § 60 ZPO).
- **Beklagte** ausführendes Luftfahrtunternehmen.
- **Streitwert** Summe der Anspruechen aller Passagiere; bis zehntausend Euro AG-Zuständigkeit.

## Sachliche Zuständigkeit

- **§ 23 Nr. 1 GVG i. d. F. seit 01.01.2026** Amtsgericht bei Streitwerten bis **zehntausend Euro**.
- Über zehntausend Euro Landgericht (§ 71 GVG).
- Bei Fluggastrechten über drei Personen mit 600-EUR-Anspruechen Schwelle erreichbar — prüfen.

## Örtliche Zuständigkeit

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

- **Abflugflughafen** oder
- **Zielflughafen** der streitigen Flugstrecke

erhoben werden. Subsidiaer

- **Sitz / Niederlassung der Airline** in Deutschland (§§ 12 13 17 ZPO).

Bei Pauschalreise mit Reiseveranstalter als Beklagter zusätzlich der **Wohnsitz des Reiseveranstalters**.

## Klagestruktur

### 1. Rubrum

```
An das Amtsgericht [Ort des Abflughafens / Zielflughafens / Niederlassung]

In Sachen
 [Hauptkläger] und weitere Kläger (siehe Anlage)
 - vertreten durch [Hauptkläger] aufgrund Vollmacht

 gegen

 [Airline-Name]
 vertreten durch [gesetzlicher Vertreter / Niederlassungsleiter Deutschland]
 [Adresse]

erhebe ich Klage und beantrage:
```

### 2. Anträge

```
1. Die Beklagte wird verurteilt an den Kläger zu 1 [Name]
 [Betrag] EUR nebst Verzugszinsen in Höhe von 5 Prozentpunkten über dem
 Basiszinssatz seit [Datum Frist erste Mahnung + 1] zu zahlen.

2. Die Beklagte wird verurteilt an den Kläger zu 2 [Name]
 [Betrag] EUR nebst Zinsen wie zu 1.

3. Die Beklagte wird verurteilt an den Kläger zu 3 [Name minderjährig]
 vertreten durch die Erziehungsberechtigten [Name]
 [Betrag] EUR nebst Zinsen wie zu 1.

4. Die Beklagte traegt die Kosten des Rechtsstreits.

5. Das Urteil ist vorlaeufig vollstreckbar (§ 708 Nr. 11 ZPO).
```

### 3. Streitwert

```
Streitwert: [Summe der Einzelanspruechen]
```

### 4. Sachverhalt

```
1. Die Klagepartei buchte am [Datum] bei der Beklagten die Beforderung
 gemäß Buchungscode [PNR] auf dem Flug [Flugnummer] am [Datum] von
 [Abflughafen] nach [Zielflughafen] in Economy.
 Beweis: Buchungsbestätigung, Anlage K1

2. Die Klagepartei meldete sich am Tag des Flugs rechtzeitig zum
 Check-in. Sie hatte ein gültiges Ticket und alle Reisedokumente.
 Beweis: Boardingpaesse, Anlage K2

3. Der Flug wurde durch die Beklagte [annulliert / mit X Stunden
 Verspätung durchgeführt / die Befoerderung wurde verweigert].
 Beweis: Stoerungsmitteilung der Beklagten, Anlage K3

4. [Bei Annullierung mit Ersatzflug:] Die Beklagte bot Ersatzflug
 [Flugnummer] am [Datum] an, mit dem die Klagepartei das Endziel
 [X] Stunden verspätet erreichte.
 Beweis: Ersatz-Boardingpaesse, Anlage K4

5. [Falls Auslagen entstanden:] Aufgrund der Annullierung musste die
 Klagepartei [Hotel Verpflegung Telefon] in Höhe von [Y] EUR
 aufwenden.
 Beweis: Belege, Anlage K5

6. Mit Schreiben vom [Datum] forderte die Klagepartei die Beklagte
 zur Zahlung auf [Erste Stufe]; mit Schreiben vom [Datum]
 zur Zahlung nochmals [Mahnung].
 Beweis: Forderungs- und Mahnschreiben mit Einschreiben-Rückschein,
 Anlagen K6 K7

7. Die Beklagte zahlte nicht.
```

### 5. Rechtliche Würdigung

```
1. Anspruchsgrundlage: Art. 7 VO (EG) Nr. 261/2004.

2. Anwendungsbereich: Der Flug erfüllt die Voraussetzungen des Art. 3
 Abs. 1 VO 261/2004 (Abflug aus einem EU-Mitgliedstaat).

3. Tatbestand: Der Flug wurde
 [bei Annullierung] gemäß Art. 5 VO 261/2004 annulliert. Der
 urspruengliche Flug fand nicht statt; der Ersatzflug am [Datum] erfolgte
 mit gravierender Änderung.

 [bei Verspätung] Der Flug erreichte das Endziel mit [X] Stunden
 Verspätung. Nach EuGH, Urt. v. 19.11.2009, C-402/07 und C-432/07
 (Sturgeon u.a. — Quelle: curia.europa.eu) sowie EuGH, Urt. v.
 23.10.2012, C-581/10 und C-629/10 (Nelson u.a. — curia.europa.eu)
 entsteht bei mehr als drei Stunden Endzielverspätung ein
 Ausgleichsanspruch wie bei Annullierung.

 [bei Anschlussflug] Maßgeblich ist die Endzielverspätung gemäß EuGH,
 Urt. v. 26.2.2013, C-11/11 (Folkerts — curia.europa.eu) und EuGH,
 Urt. v. 31.5.2018, C-537/17 (Wegener — curia.europa.eu).

4. Distanz: Die Grosskreisdistanz [Abflug zu Endziel] betraegt [X] km.
 Dies entspricht der Stufe [1/2/3] des Art. 7 VO 261/2004.

5. Höhe des Anspruchs: [250 / 400 / 600] EUR pro Passagier;
 bei [3] Passagieren [Gesamtbetrag] EUR.

6. Keine Befreiung wegen außergewöhnlicher Umstaende (Art. 5 Abs. 3
 VO 261/2004). Die Beklagte hat sich auf [Begründung der Airline]
 berufen. Dies verfaengt aus folgenden Gründen nicht:

 Technische Defekte sind nach EuGH, Urt. v. 22.12.2008, C-549/07
 (Wallentin-Hermann — curia.europa.eu), regelmäßig nicht als
 außergewöhnliche Umstaende einzuordnen, weil sie Teil der normalen
 Ausübung der Tätigkeit des Luftfahrtunternehmens sind.

 [bei Streik] Streiks der eigenen Mitarbeiter (auch wilde Streiks)
 stellen nach st. Rspr. des EuGH keinen außergewöhnlichen Umstand
 dar. Volltext und konkretes Aktenzeichen vor Versand in
 curia.europa.eu aufrufen und mit Randnummer einsetzen.

 [bei Personalmangel Flughafen] EuGH, Urt. v. 16.5.2024, C-405/23
 (curia.europa.eu) — Personalmangel beim eigenen Bodenpersonal ist
 nicht außergewöhnlich; nur ausnahmsweise bei drittverantwortetem
 Engpass.

 [bei versteckter Konstruktionsfehler] EuGH, Urt. v. 13.6.2025,
 C-411/23 (curia.europa.eu) — versteckter Konstruktionsfehler im
 Triebwerk kann außergewöhnlicher Umstand sein, auch wenn die
 Airline vorab informiert war; zumutbare Maßnahmen bleiben darzulegen.

 [bei Blitzschlag] EuGH, Urt. v. 16.10.2025, C-399/24 (curia.europa.eu).

 Die Beweislast für außergewöhnliche Umstaende und für die
 Ergreifung aller zumutbaren Maßnahmen liegt bei der Beklagten.

7. Verzug: Mit Ablauf der mit Schreiben vom [Datum] gesetzten Zahlungsfrist
 trat Verzug ein (§ 286 Abs. 1 BGB). Verzugszinsen gemäß § 288 Abs. 1
 BGB.

8. Sachliche Zuständigkeit Amtsgericht (§ 23 Nr. 1 GVG bis zehntausend
 Euro, Streitwertgrenze seit 1.1.2026). Oertliche Zuständigkeit
 wahlweise am Abflug- oder Zielflughafen (§ 29 ZPO i.V.m. Art. 7
 Nr. 1 lit. b VO (EU) 1215/2012 — Brüssel-Ia) oder am Sitz der
 Beklagten (§§ 12, 17 ZPO).
```

### 6. Beweisangebote

```
Beweise:
 Urkundenbeweis durch beigefuegte Anlagen K1 bis K7.
 Parteivernehmung der Klagepartei zum Verlauf vor Ort.
 Im Bestreitensfall: Auskunft des Flughafens [Name] über tatsächliche
 Abflug- und Ankunftszeiten (Anregung gerichtlicher Beiziehung).
```

### 7. Anlagen

```
K1 Buchungsbestätigung
K2 Boardingpaesse
K3 Stoerungsmitteilung der Airline
K4 Ersatzboardingpaesse (sofern vorhanden)
K5 Belege zu Auslagen
K6 Forderungsschreiben vom [Datum] mit Einschreiben-Rückschein
K7 Mahnschreiben vom [Datum] mit Einschreiben-Rückschein
K8 Vollmachten der Mitreisenden
```

### 8. Unterschrift

```
[Ort, Datum]
[Name (und ggf. Initialen aller Kläger oder Vollmachtsverweis)]
```

## Anwaltszwang

- **Kein Anwaltszwang** vor dem Amtsgericht (§ 78 ZPO e contrario).
- Selbstvertretung möglich aber rechtliche Risiken vorhanden — vor Klage Skill `airline-standardausreden-pruefen` nutzen.

## Versandweg

- **Schriftlich** per Post oder zur Niederschrift.
- **Elektronisch** wenn Mandant beA/EGVP-Zugang hat — für Privatpersonen üblicherweise nicht.

## Streitgenossenschaft

- **Mehrere Passagiere** können als Streitgenossen klagen (§ 60 ZPO).
- Eine Klageschrift für alle — separate Anträge je Kläger.
- Vollmacht der Mitreisenden erforderlich (Skill `vollmacht-familienmitglieder`).

## Ausgabe

- `klage-fluggast-<datum>.docx` und PDF.
- Anlagenkonvolut (siehe nächste Sektion).
- Streitwert- und Kostenberechnung.
- Hinweis zur Gerichtswahl Abflughafen / Zielflughafen / Niederlassungssitz.

## Anlagen-Übergabe

Unmittelbar nach Erstellung der Klageschrift den Skill `fluggastrechte-anlagen-bauen` aufrufen — ohne ordnungsgemäßes Anlagenkonvolut ist die Klage nicht einreichungsfähig.

Übergabe-Schema:

```yaml
schriftsatz: klage-fluggast-<datum>.docx
rohbelege_verzeichnis: <fall>/belege/
ausgabeverzeichnis: <fall>/anlagen/
bundle: true # Pflicht — beA verlangt geschlossenes PDF
schriftgrad_stempel: 12
schrift_stempel: Arial-Bold
bezeichnung: "Anlage K"
```

beA-Konvention:

- Anlagen werden im beA als separate PDFs eingereicht, jeweils mit Stempel oben rechts in Arial 12 FETT.
- Dateiname ohne Umlaute und ohne Leerzeichen: `Anlage_K_1.pdf`, `Anlage_K_2.pdf`, …
- Reihenfolge muss der Erwähnung im Schriftsatz entsprechen — der Skill `fluggastrechte-anlagen-bauen` erzwingt dies.
- Sammel-PDF `Schriftsatz_mit_Anlagen.pdf` zusätzlich erzeugen für eigenes Aktenexemplar.

## Hinweise

- Vor Klage bei kleineren Anspruechen Schlichtungsstelle Luftverkehr (SOEP) versuchen — kostenfrei und meist erfolgreich.
- Bei Erfolg keine Verjährungshemmung allein durch SOEP-Verfahren — Verjährungsprüfung beachten (drei Jahre § 195 BGB).

## Zentrale Anspruchsgrundlagen & Normen

- Art. 7 VO (EG) Nr. 261/2004 — Ausgleichszahlung 250/400/600 EUR je nach Distanzklasse
- Art. 5 Abs. 1 lit. c VO (EG) Nr. 261/2004 — Annullierung; Art. 6 VO — Verspaetung
- Art. 5 Abs. 3 VO (EG) Nr. 261/2004 — Befreiung nur bei aussergewoehnlichen Umstaenden (Beweislast Airline)
- § 23 Nr. 1 GVG (i.d.F. seit 01.01.2026) — sachliche Zustaendigkeit Amtsgericht bis 10.000 EUR
- §§ 12, 13, 17 ZPO — oertliche Zustaendigkeit allgemein
- § 253 ZPO — Klageerhebung Schriftform, Mindestinhalt Klageschrift
- § 60 ZPO — Streitgenossenschaft mehrerer Passagiere
- §§ 286, 288 BGB — Verzug und Verzugszinsen
- § 195, § 199 Abs. 1 BGB — Verjährung drei Jahre

## Aktuelle Rechtsprechung (Stand Mai 2026; Volltext jeweils in curia.europa.eu prüfen)

- EuGH, Urt. v. 19.11.2009, C-402/07 und C-432/07 (Sturgeon u.a.) — 3-Stunden-Schwelle
- EuGH, Urt. v. 23.10.2012, C-581/10 und C-629/10 (Nelson u.a.) — Bestätigung
- EuGH, Urt. v. 22.12.2008, C-549/07 (Wallentin-Hermann) — technischer Defekt
- EuGH, Urt. v. 26.2.2013, C-11/11 (Folkerts) — Endziel-Verspätung Anschlussflüge
- EuGH, Urt. v. 31.5.2018, C-537/17 (Wegener) — einheitliche Buchung Drittstaat
- EuGH, Urt. v. 4.5.2017, C-315/15 (Pesková) — Vogelschlag
- EuGH, Urt. v. 21.12.2021, C-146/20, C-188/20, C-196/20 — Vorverlegung als Annullierung
- EuGH, Urt. v. 16.5.2024, C-405/23 — Personalmangel Flughafen
- EuGH, Urt. v. 9.1.2025, C-394/23 — Vorverlegung bestätigend
- EuGH, Urt. v. 13.6.2025, C-411/23 — versteckter Konstruktionsfehler
- EuGH, Urt. v. 16.10.2025, C-399/24 — Blitzschlag

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Triage vor Klageerhebung

1. Schlichtung versucht? → SOEP-Verfahren erst ausschoepfen (kostenfrei); danach Klage
2. Verjährung geprueft? → drei Jahre ab Jahresende des Flugjahres (§ 195 i.V.m. § 199 BGB)
3. Streitwert berechnet? → bei > 10.000 EUR Landgericht (§ 71 GVG) + Anwaltszwang § 78 ZPO
4. Beweismittel vollstaendig? → Boardingpaesse, Buchungsbestaetigung, Stoerungsbestaetigung, Mahnschreiben
5. Richtige Beklagte? → ausfuehrendes Luftfahrtunternehmen (nicht Reiseveranstalter), Art. 2 lit. b VO 261/2004
6. Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Adressat & Tonfall

Adressat: Amtsgericht am gewaehlten Gerichtsstand — Tonfall sachlich-juristisch; Schriftsatz ohne Anwaltszwang trotzdem klar strukturiert nach § 253 ZPO-Mindestinhalt (Parteien, Antrag, Begruendung, Beweisangebote)

## 3. `pauschalreise-statt-flug-pruefen`

**Fokus:** Pauschalreise gegen Flug-Einzelbuchung: Reiseveranstalterhaftung nach §§ 651a ff. BGB, Pauschalreise-RL EU 2015 2302. Minderung, Schadensersatz, Ruecktritt. Verhaeltnis zur VO 261 (kumulativ moeglich, Anrechnung nach BGH). Pruefraster ob Pauschalreise vorliegt.

# Pauschalreise gegen Einzelflug

## Spezialwissen: Pauschalreise gegen Einzelflug
- **Spezialgegenstand:** Pauschalreise gegen Einzelflug / pauschalreise statt flug pruefen. Der Skill löst diese konkrete Lage und darf nicht in allgemeines Routing ausweichen.
- **Normen-/Quellenanker:** BGB, RL, EU, VO, BGH.
- **Entscheidende Weiche:** Aus dem Sachverhalt sind Tatbestandsmerkmal, Zuständigkeit, Frist, Beweislast, Ermessen/Wertung und Rechtsfolge getrennt herauszuarbeiten; offene Tatsachen werden als offen markiert.
- **Arbeitsprodukt:** Erzeuge eine fallbezogene Matrix `Norm / Tatsache / Beleg / Gegenargument / Risiko / nächster Schritt` plus einen direkt verwendbaren Baustein für Vermerk, Schreiben, Antrag, Schriftsatz oder Entscheidungsvorlage.


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
2. **Rechtliche Einordnung** - einschlaegige Normen, zustaendige Stellen, Verfahrensart, Darlegungs-/Beweislast und nur verifizierte Rechtsprechung.
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
- Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei pruefbarem Link ausgeben; bei Unsicherheit erst verifizieren oder als zu pruefen markieren.
- Keine Paywall-, Kommentar-, Aufsatz- oder Datenbankfundstelle als tragende Aussage verwenden, wenn sie nicht durch Nutzerquelle oder dokumentierten Live-Zugriff verifiziert ist.
- Keine Kommentar-, Handbuch-, Aufsatz- oder BeckRS-/juris-Blindzitate aus Modellwissen. Literatur nur verwenden, wenn der Nutzer die Quelle bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitskontext dokumentiert ist.
- Annahmen explizit als solche kennzeichnen; keine erfundenen Fundstellen, keine erfundenen Tatsachen, keine erfundenen Behoerdenpraxis-Saetze.

## Was dieser Arbeitsgang nicht macht
- Kein Ersatz fuer eine vollstaendige Mandantenberatung.
- Keine Festlegung des Mandanten ohne dessen ausdrueckliche Entscheidung.
- Keine Bewertung von Tatsachen, die nicht durch Unterlagen oder klare Mandantenangaben gedeckt sind.
- Bei erkennbaren Interessenkonflikten oder Berufsrechtsfragen Hinweis an den fallfuehrenden Anwalt.
