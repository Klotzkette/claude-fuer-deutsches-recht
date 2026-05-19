---
name: takedown-anweisung
description: >
  Abmahnungsunterstützung und Meldeverfahren bei Urheberrechtsverletzungen im
  Internet — Notice-and-Take-Down nach §§ 7 ff. TMG/DDG, DSA Art. 16
  Meldeverfahren, Störerhaftung und Gegendarstellung. Lädt bei der Erstellung
  einer Meldung an einen Hostprovider, der Triagierung einer eingegangenen
  Meldung oder der Formulierung einer Gegendarstellung.
language: de
triggers:
  - "Take-Down Meldung"
  - "Notice and Take Down Deutschland"
  - "Hostprovider Haftung"
  - "DSA Meldung"
  - "Störerhaftung"
  - "Urheberrechtsverletzung Internet"
  - "Plattform Meldeverfahren"
  - "Gegenvorstellung Meldung"
  - "§ 7 TMG DDG Haftung"
---

# Notice-and-Take-Down / Meldeverfahren

## Zweck

Diese Skill deckt drei Handlungsmodi ab:

- `--senden` — Meldung an einen Hostprovider nach §§ 7 ff. TMG/DDG (Notice-and-Take-Down) sowie ggf. DSA Art. 16 formulieren
- `--reagieren` — eingegangene Meldung triagieren: Entfernen / Gegenvorstellung / Verhandeln / Ignorieren
- `--gegenvorstellung` — Gegenvorstellung an die Plattform nach eigenem gutem Glauben formulieren

Kein Modus sendet automatisch. Die Skill entwirft; der Rechtsanwalt prüft und versendet.

Hinweis: Dieser Skill ersetzt keine anwaltliche Beratung im konkreten Einzelfall.

## Eingaben

Befehlsargument:
- `--senden` + Kontext oder Pfad zur Meldungsunterlage
- `--reagieren` + Pfad zur oder eingefügte eingegangene Meldung
- `--gegenvorstellung` + Kontext
- (kein Argument) → fragen: „Sollen wir eine Meldung senden, auf eine eingegangene reagieren oder eine Gegenvorstellung formulieren?"

## Rechtlicher Rahmen

### Kernvorschriften

**Haftung des Hostproviders / Vermittlerdienstleister:**
- **§ 7 Abs. 1 DDG / § 7 Abs. 1 TMG (§ 10 TMG a.F.)** — Kein Hostprovider ist verpflichtet, gespeicherte Inhalte zu überwachen; erst nach Kenntnis von konkreter Rechtsverletzung entsteht Handlungspflicht (Reaktionspflicht nach BGH-Rspr.)
- **§ 10 DDG / § 10 TMG** — Haftungsprivileg für Hostprovider: Haftung erst bei Kenntnis und Nichtentfernen nach Hinweis (Notice-and-Take-Down-Mechanismus)
- **Art. 16 DSA (Digital Services Act, EU 2022/2065)** — Meldeverfahren für Plattformen mit mehr als 45 Mio. monatlichen Nutzern in der EU; einheitliches Meldeformular-Format; Reaktionspflicht; Beschwerdemechanismus
- **Art. 17 DSA** — Begründungspflicht der Plattform bei Inhaltsmoderation; Gegenvorstellungsrecht
- **§ 97 UrhG** — Unterlassungs- und Schadensersatzanspruch bei Urheberrechtsverletzung; Grundlage für Abmahnung

**Störerhaftung:**
- Störerhaftung: Wer willentlich und adäquat kausal zur Rechtsverletzung eines Dritten beiträgt, haftet als Störer auf Unterlassung (nicht Schadensersatz). Prüfungspflichten müssen zumutbar sein.
- **§ 8 DDG** — Durchleitungsdienstleister: kein Haftungsprivileg-Verlust bei bloßer Durchleitung; keine Überwachungspflicht

**NetzDG / weitere:**
- **§§ 1–3 NetzDG** — Plattformpflichten bei Hassrede und sonstigen strafbaren Inhalten; spezialgesetzliche Entfernungspflicht unabhängig vom allgemeinen Notice-and-Take-Down

### Leitentscheidungen

- BGH, Urt. v. 11.03.2004 – I ZR 304/01, BGHZ 158, 236 Rn. 42 (Internet-Versteigerung I) — Grundlegend: Störerhaftung des Online-Marktplatzes; zumutbare Prüfungspflichten; Haftung erst nach Hinweis auf konkrete Rechtsverletzung
- BGH, Urt. v. 30.04.2020 – I ZR 115/16, GRUR 2020, 738 Rn. 55 (YouTube / Uploaded) — Haftung von Hostprovider für Urheberrechtsverletzungen; Reaktionspflicht nach qualifiziertem Hinweis; kein generelles Overblocking
- BGH, Urt. v. 12.07.2012 – I ZR 18/11, GRUR 2013, 370 Rn. 28 (Alone in the Dark) — Take-Down bei Filesharing; Zumutbarkeit der Prüfungspflicht
- BGH, Urt. v. 22.07.2010 – I ZR 139/08, GRUR 2011, 152 (Rolex/Stiftung Warentest) — Störerhaftung; Abmahnungserfordernis vor gerichtlichem Vorgehen; Wiederholungsgefahr
- EuGH, Urt. v. 22.06.2021 – C-682/18, C-683/18, GRUR 2021, 1054 (YouTube/Cyando) — Kommunikation an die Öffentlichkeit; Kenntnis und Kontrolle als Haftungsvoraussetzung für Plattformen

### Kommentare

- Köhler, in: Köhler/Bornkamm/Feddersen, UWG, 43. Aufl. 2025, § 8 Rn. 2.1 (Unterlassungsanspruch; Störerhaftung)
- Leistner/Ohst, in: Schricker/Loewenheim, UrhG, 6. Aufl. 2020, § 97 Rn. 1 (Unterlassung und Schadensersatz)
- Hoffmann, in: Spindler/Schuster, Recht der elektronischen Medien, 4. Aufl. 2023, § 10 TMG Rn. 1 (Hostprovider-Haftung, Notice-and-Take-Down)
- Martini, in: BeckOK InfoMedienR, 44. Ed. (Stand 01.05.2025), Art. 16 DSA Rn. 1 (Meldeverfahren nach Digital Services Act)

## Ablauf

### Modus `--senden`: Meldung an Hostprovider / Plattform

#### Schritt 1: Geschütztes Werk identifizieren

> Um eine Meldung zu formulieren, werden folgende Angaben benötigt:
>
> - **Bezeichnung / Beschreibung des Werkes** — was ist es (Software, Bild, Text, Video, Audio)?
> - **Rechtsinhaber** — wem gehören die Rechte? Eigentümer, ausschließlicher Nutzungsrechtinhaber, oder Auftraggeber nach § 69b UrhG (Arbeitnehmer-Softwarewerk)?
> - **Nachweis der Rechtsinhaberschaft** — Urheberschaft, Lizenz, Auftrag
> - **Frühere Lizenzen** — wurde die beanstandete Nutzung jemals gestattet (Vertrag, Creative-Commons-Lizenz, stillschweigende Erlaubnis)?

Rechtsinhaberschaft und Verfügungsberechtigung sind die ersten Punkte, die ein Hostprovider und ein Gericht prüfen.

#### Schritt 2: Verletzungsmaterial und Fundort identifizieren

> - **Plattform / Diensteanbieter** — YouTube, Instagram, GitHub, Amazon, ein Webhoster etc.
> - **URL(s)** — konkrete, direkte Links zum beanstandeten Inhalt
> - **Beschreibung** — was ist die Verletzung (identische Kopie, wesentlich ähnlich, abgeleitetes Werk ohne Lizenz)?
> - **Beweissicherung** — Screenshot mit sichtbarer URL und Zeitstempel; ggf. Web-Archivierung (archive.org)

§ 97 UrhG und das Notice-and-Take-Down-System verlangen hinreichend genaue Bezeichnung, damit der Diensteanbieter den Inhalt auffinden und beurteilen kann.

#### Schritt 3: Zulässigkeitsprüfung (Freie Nutzung, Schranken)

Vor der Meldung sind Urheberrechtsschranken zu prüfen. Eine Meldung auf schrankengemäße Nutzungen schädigt den Diensteanbieter und kann Schadensersatzansprüche (§ 826 BGB, § 97a Abs. 4 UrhG analog) auslösen.

Prüfen nach §§ 44a ff. UrhG:

- **§ 51 UrhG — Zitat:** Kritik, Rezension, wissenschaftliche Auseinandersetzung — legitim, wenn Zitatzweck erkennbar und Umfang verhältnismäßig
- **§ 49 UrhG — Presseprivileg:** Übernahme von Tagesaktualitäten; eng begrenzt
- **§ 44a UrhG — Vorübergehende Vervielfältigungen:** Technisch-funktionale Zwischenspeicherung
- **§ 60a ff. UrhG — Bildung und Wissenschaft:** Unterricht, Wissenschaft, öffentliche Einrichtungen; begrenzt
- **§ 24 UrhG — Freie Benutzung (aufgehoben):** Seit 7.6.2021 durch Unionsrecht ersetzt; Parodie, Karikatur, Pastiche jetzt über § 51a UrhG

Wenn Schrankennutzung **wahrscheinlich oder zweifelhaft**: Entwurf stoppen, an Rechtsanwalt verweisen. Eine Meldung auf geschützte Meinungsäußerungen ist das genaue Szenario, das zu einer Gegenreaktion berechtigt.

#### Schritt 4: Guter Glaube und Vertretungsberechtigung

- Ist der Nutzer der Rechtsinhaber oder von ihm bevollmächtigt?
- Wurde die Nutzung direkt geprüft (nicht nur aus zweiter Hand)?
- Wurden bestehende Lizenzen und Gestattungen überprüft?

Wenn ja auf alle Punkte: Guter Glaube ist begründbar.

#### Schritt 5: Meldung formulieren

Erforderliche Elemente (nach BGH-Rspr. und DSA Art. 16):

1. **Identifikation der Rechtsinhaberin** — Name, Adresse, E-Mail; Bevollmächtigter falls zutreffend
2. **Bezeichnung des geschützten Werkes** — Titel, Typ, ggf. Registrierungsnummer (Urheberrecht entsteht formfrei nach § 7 UrhG; Registrierung ist kein Anspruchsvoraussetzung)
3. **Genaue Fundort-URL(s)** des beanstandeten Inhalts
4. **Beschreibung der Verletzung** — worin konkret die Verletzung besteht
5. **Erklärung guten Glaubens** — keine Berechtigung der Nutzung durch Inhaber, seinen Bevollmächtigten oder das Gesetz
6. **Genauigkeitserklärung** — Angaben sind nach bestem Wissen zutreffend
7. **Bitte um Entfernung**

DSA Art. 16 Plattformen: Meldung über das behördlich bereitgestellte Formular oder den plattformeigenen Meldepfad einreichen. Plattform ist zur Bestätigung und Begründung verpflichtet (Art. 17 DSA).

#### Schritt 6: Warnhinweis vor Versand

```
┌─────────────────────────────────────────────────────────────┐
│  VOR DEM VERSAND DIESER MELDUNG                             │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  Eine Notice-and-Take-Down-Meldung hat unmittelbare         │
│  rechtliche Wirkung. Unberechtigt eingereichte Meldungen    │
│  können Schadensersatzansprüche des Diensteanbieters        │
│  oder des betroffenen Nutzers auslösen (§§ 823, 826 BGB;   │
│  Art. 17 Abs. 8 DSA für Missbrauch des Meldeverfahrens).   │
│                                                             │
│  Vor dem Versand bestätigen:                                │
│                                                             │
│    1. Sie sind Rechtsinhaber oder bevollmächtigt.           │
│    2. Die beanstandete Nutzung ist nicht gestattet —        │
│       Lizenzen, Schranken und Gestattungen wurden           │
│       geprüft.                                              │
│    3. Schranken (§§ 44a ff. UrhG, insb. Zitat § 51,        │
│       Parodie § 51a) sind nicht einschlägig.                │
│    4. Die versendende Person hat Genehmigung gemäß          │
│       Mandatsprofil.                                        │
│                                                             │
│  Genehmigung gemäß Mandatsprofil: [Genehmigende Person]    │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### Modus `--reagieren`: Eingegangene Meldung triagieren

Der eigene Inhalt wurde von einer Plattform entfernt oder ein Diensteanbieter hat eine Meldung übermittelt.

#### Schritt 1: Meldung lesen

Extrahieren:

- **Absender** — Entität, Unterzeichner, ggf. anwaltliche Vertretung
- **Diensteanbieter** — welche Plattform hat informiert?
- **Beanstandetes Werk** — was behauptet der Absender als sein Recht?
- **Unser Inhalt** — welche URL(s) / welcher Inhalt wurde beanstandet?
- **Datum** der Meldung und ggf. Entfernung
- **Formelle Vollständigkeit** — enthält die Meldung alle erforderlichen Elemente? (Fehler erhöhen die Möglichkeit einer Gegenvorstellung)

#### Schritt 2: Bewertung

- **Liegt eine Lizenz vor?** Vertraglich, stillschweigend, Creative Commons, vorherige Einigung
- **Greift eine Schranke?** Zitat (§ 51 UrhG), Parodie/Pastiche (§ 51a UrhG), Bildung (§ 60a ff. UrhG)
- **Hat die Meldung formelle Mängel?** Fehlende Elemente, fehlende Genehmigungserklärung, unklare Rechtsinhaberschaft? Mangelhafte Meldungen sind keine ordnungsgemäßen Meldungen; die Plattform darf trotzdem handeln — aber das Durchsetzungsrisiko des Absenders steigt.
- **Hat die Plattform ordnungsgemäß reagiert?** Wurde uns nach Art. 17 DSA eine Begründung übermittelt?
- **Absender-Glaubwürdigkeit:** Wiederholte Meldungen auf vergleichbare Inhalte? Erkennbares Muster von Overblocking?

#### Schritt 3: Vier Optionen präsentieren

**A — Entfernung akzeptieren**
- Wenn: Meldung berechtigt oder Aufwand des Widerspruchs unverhältnismäßig
- Abwägung: Inhalt bleibt offline; SEO-Effekt; Sperren-Konto-Risiko bei Plattformen mit Wiederholungssystem
- Nächster Schritt: Vorgang dokumentieren; keine Gegenvorstellungs-Frist versäumen

**B — Gegenvorstellung einlegen**
- Wenn: guter Glaube, dass Inhalt rechtmäßig war — Lizenz, Schranke, fehlendes Eigentumsrecht des Absenders
- Abwägung: Inhalt bleibt gesperrt bis Plattform entscheidet; bei DSA: Beschwerdemechanismus (Art. 20) und außergerichtliche Beilegung (Art. 21) verfügbar; Eskalationsrisiko
- Nächster Schritt: `/gewerblicher-rechtsschutz:takedown-anweisung --gegenvorstellung`

**C — Absender direkt kontaktieren**
- Wenn: Spielraum für einvernehmliche Lösung (Lizenzierung, Namensnennung, Teilentfernung)
- Abwägung: Inhalt bleibt gesperrt während der Gespräche; Vertraulichkeit von Verhandlungen beachten (§ 278 ZPO-Analogie)
- Nächster Schritt: Anschreiben an Absender; Gegenvorstellung bis Einigung zurückstellen

**D — Ignorieren / auf anderem Weg verfolgen**
- Wenn: Schaden gering, kein Interesse an Gerichtsstand-Einräumung, Absender separat adressieren
- Abwägung: Inhalt bleibt gesperrt; § 97 UrhG kann ggf. beim Absender selbst geltend gemacht werden bei unberechtigter Meldung

Empfehlung mit zwei Sätzen Begründung.

#### Schritt 4: Triagierungsvermerk schreiben

```markdown
[ARBEITSERGEBNIS-KOPFZEILE]

# Eingegangene Meldung — Triagierung

**Kurzzeichen:** [kurzzeichen]
**Eingegangen:** [JJJJ-MM-TT]
**Plattform:** [Name]

## Die Meldung

**Absender:** [Entität, Unterzeichner, Anwaltsbüro falls vorhanden]
**Beanstandetes Werk:** [Titel, Beschreibung]
**Unser Inhalt:** [URLs / Identifikatoren]
**Datum der Entfernung:** [JJJJ-MM-TT]
**Formelle Vollständigkeit der Meldung:** [ja / nein — fehlende Elemente auflisten]

## Bewertung

**Lizenz / Genehmigungscheck:** [Ergebnis]
**Schrankenprüfung (§§ 51, 51a, 60a ff. UrhG):** [Ergebnis — jede Schranke + Schluss; `[SME VERIFIZIEREN]`]
**Formelle Mängel der Meldung:** [Liste oder keine]
**DSA-Begründung durch Plattform:** [erhalten / nicht erhalten]
**Absender-Glaubwürdigkeit:** [Einschätzung]

## Optionen

### A. Entfernung akzeptieren
### B. Gegenvorstellung
### C. Absender kontaktieren
### D. Ignorieren

**Empfehlung:** [A/B/C/D] — [zwei Sätze] — `[SME VERIFIZIEREN: Anwalt bestätigt vor Ausführung]`

## Fristen

- **Beschwerdefrist DSA Art. 20:** 6 Monate nach Entscheidung der Plattform
- **Außergerichtliche Beilegung DSA Art. 21:** Verfügbar bei nicht-gütlicher Einigung
- **Vertragliche Fristen mit Plattform:** [prüfen]

## Sofortmaßnahmen

- [ ] Beweissicherung des beanstandeten Inhalts durchgeführt — [ja/nein]
- [ ] Geschäftliche Auswirkung bewertet — [ja/nein]
- [ ] Mandat im Verlaufsprotokoll erfasst — [ja/nein/TBD]
- [ ] Rechtsanwalt beauftragt — [wer]
```

### Modus `--gegenvorstellung`: Gegenvorstellung an Plattform

#### Schritt 1: Voraussetzungen prüfen

- Inhalt wurde aufgrund einer Meldung (nicht aufgrund von AGB-Verstoß) entfernt
- Es besteht guter Glaube, dass die Entfernung unberechtigt war (Lizenz, Schranke, fehlende Rechtsinhaberschaft des Absenders)
- Entscheidung wurde bewusst getroffen — nicht reaktiv

#### Schritt 2: Gegenvorstellung formulieren

Erforderliche Elemente:

1. **Identifikation des betroffenen Inhalts** — URL des entfernten Inhalts
2. **Erklärung des guten Glaubens** — Inhalt war rechtmäßig, weil: [Lizenz / Schranke / fehlendes Recht des Absenders]
3. **Begründung** — konkrete Darlegung
4. **Antrag auf Wiederherstellung**
5. **Kontaktdaten**

Bei DSA-Plattformen: Beschwerdemechanismus nach Art. 20 DSA nutzen; ggf. außergerichtliche Streitbeilegung nach Art. 21 DSA.

#### Schritt 3: Warnhinweis vor Versand

```
┌─────────────────────────────────────────────────────────────┐
│  VOR DEM VERSAND DIESER GEGENVORSTELLUNG                    │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  Eine Gegenvorstellung bestreitet die Berechtigung          │
│  der ursprünglichen Meldung und kann den Absender zu        │
│  rechtlichen Schritten veranlassen.                         │
│                                                             │
│  • Bei Eskalation durch den Absender: Klage auf             │
│    Unterlassung oder Schadensersatz nach § 97 UrhG          │
│    möglich.                                                 │
│                                                             │
│  • DSA Art. 20: Beschwerde bei Plattform möglich.           │
│    Art. 21: Außergerichtliche Streitbeilegung verfügbar.    │
│                                                             │
│  Vor dem Versand bestätigen:                                │
│    1. Guter Glaube besteht — Lizenz, Schranke oder          │
│       fehlendes Recht des Absenders ist konkret             │
│       benennbar.                                            │
│    2. Anwalt hat diese Gegenvorstellung vor dem             │
│       Versand geprüft.                                      │
│    3. Genehmigung gemäß Mandatsprofil liegt vor.            │
│                                                             │
│  Genehmigung gemäß Mandatsprofil: [Genehmigende Person]    │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

## Ausgabeformat

- `--senden`: Meldungsentwurf (Klartext, zum Einreichen über plattformeigenen Meldepfad oder per E-Mail an Diensteanbieter). Im Chat zur Überprüfung zeigen, bevor auf Disk gespeichert.
- `--reagieren`: Triagierungsvermerk mit Arbeitsergebnis-Kopfzeile; privilegiert und vertraulich.
- `--gegenvorstellung`: Gegenvorstellungsentwurf (Klartext). Im Chat zur Überprüfung zeigen.

Abschlusssatz (in-Chat-Vorschau): *„Dies ist ein Entwurf zur anwaltlichen Prüfung, kein versandfertiges Schreiben. Ein Rechtsanwalt prüft, bearbeitet und übernimmt fachliche Verantwortung vor dem Versand."*

## Beispiel

**Eingabe:** `/gewerblicher-rechtsschutz:takedown-anweisung --senden` — Fotograf meldet unerlaubte Nutzung seines Fotos auf einer Nachrichtenwebsite.

**Auszug Meldungsentwurf:**

> An: [Name Diensteanbieter / Hostprovider]
> Betreff: Meldung einer Urheberrechtsverletzung nach § 7 Abs. 2 DDG
>
> Sehr geehrte Damen und Herren,
>
> ich bin Rechtsinhaber / bevollmächtigte Vertreterin für folgendes urheberrechtlich geschütztes Werk:
> Fotografie „[Bildtitel]", aufgenommen am [Datum], Urheber [Name] (§ 7 UrhG).
>
> Dieses Werk wird auf Ihrer Plattform ohne Genehmigung genutzt unter:
> [URL]
>
> Die Nutzung ist weder durch mich noch durch Dritte gestattet. Schranken nach §§ 44a ff. UrhG greifen nach Prüfung nicht ein. Ich bitte um unverzügliche Entfernung des genannten Inhalts.
>
> Ich erkläre nach bestem Wissen und Gewissen, dass die vorstehenden Angaben zutreffend sind und ich berechtigt bin, im Namen des Rechtsinhabers zu handeln.
>
> [Kontaktdaten / Unterschrift]

## Risiken und typische Fehler

- **Schrankenprüfung versäumen:** Meldungen auf zitiergeschützte Kritik, Parodien oder Unterrichtsmaterial sind unzulässig und können Gegenansprüche auslösen.
- **Unklare Rechtsinhaberschaft:** Meldung ohne Nachweis der Berechtigung scheitert beim Hostprovider und erzeugt Haftungsrisiken.
- **DSA-Pflichten übersehen:** Große Plattformen (Very Large Online Platforms nach Art. 33 DSA) sind zu förmlichen Reaktionen und Begründungen verpflichtet; diese Pflichten können eingefordert werden.
- **Gegenvorstellung ohne Anwaltsrat:** Die Gegenvorstellung bestreitet die Meldung; eine unbegründete Gegenvorstellung kann zur eigenen Unterlassungsklage führen.
- **NetzDG-Spezialregeln vergessen:** Bei Hassrede und strafbaren Inhalten gelten §§ 1–3 NetzDG mit eigenem Melde- und Entfernungsregime.

## Quellenpflicht

Alle Aussagen zu Haftung, Schranken und Verfahren müssen belegbar sein:

- **Gesetze:** §§ 7, 10 DDG (entspr. TMG); §§ 51, 51a, 97 UrhG; Art. 16, 17, 20, 21 DSA; §§ 1–3 NetzDG
- **Rechtsprechung:** mindestens eine BGH-Entscheidung zur Hostprovider-Haftung oder Störerhaftung (BGH BGHZ 158, 236 oder BGH GRUR 2020, 738)
- **Kommentar:** Spindler/Schuster eMedienR oder Köhler/Bornkamm/Feddersen UWG mit § und Randnummer
- Modellannahmen als `[Modellwissen — verifizieren]` kennzeichnen.
