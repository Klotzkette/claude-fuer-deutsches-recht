---
name: takedown-anweisung-unterlassungsverlangen
description: "Takedown Anweisung Unterlassungsverlangen: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Takedown Anweisung Unterlassungsverlangen

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Takedown Anweisung Unterlassungsverlangen** im Plugin Gewerblicher Rechtsschutz. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `takedown-anweisung` | Rechteinhaber findet urheberrechtsverletzende Inhalte online oder erhielt selbst eine Meldung als Hostprovider. Notice-and-Take-Down §§ 7 ff. TMG/DDG DSA Art. 16. Prüfraster: Meldung an Hostprovider Stoererhaftung DSA Meldeformular Gegendarstellung. Output: Meldungs-Entwurf oder Gegendarstellungs-Schriftsatz. Abgrenzung zu abmahnung-urheberrecht (klassische Abmahnung) und verletzungs-triage. |
| `unterlassungsverlangen` | Schutzrechtsinhaber will Verletzung abmahnen oder hat selbst Abmahnung erhalten. Abmahnung Unterlassung MarkenG PatG UrhG UWG. Prüfraster: Abmahnungsentwurf modifizierte Unterlassungserklärung Streitwert Kostenansatz RVG oder Reaktions-Optionsmemo bei erhaltener Abmahnung. Output: Abmahnungsschreiben oder Optionsmemo mit Risikobewertung. Abgrenzung zu schutzschrift-eilverfuegung (Praeventiv) und verletzungs-triage (Eingangsentscheidung). |
| `verletzungs-triage` | Mandant sieht IP-Verletzung oder hat Verletzungsschreiben erhalten und fragt: Was ist zu tun? Verletzungs-Triage gewerblicher Rechtsschutz. Prüfraster: Marke § 14 MarkenG Patent § 9 PatG Urheber § 97 UrhG Wettbewerb § 8 UWG Entscheidungsempfehlung Ignorieren/informelles Schreiben/Abmahnung/eV/Klage. Output: Entscheidungs-Memo mit Empfehlung und naechstem Schritt. Abgrenzung zu unterlassungsverlangen (Abmahnung selbst) und mandat-triage-gewerblicher-rechtsschutz. |

## Arbeitsweg

Im Plugin Gewerblicher Rechtsschutz gilt für **Takedown Anweisung Unterlassungsverlangen**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `takedown-anweisung`

**Fokus:** Rechteinhaber findet urheberrechtsverletzende Inhalte online oder erhielt selbst eine Meldung als Hostprovider. Notice-and-Take-Down §§ 7 ff. TMG/DDG DSA Art. 16. Prüfraster: Meldung an Hostprovider Stoererhaftung DSA Meldeformular Gegendarstellung. Output: Meldungs-Entwurf oder Gegendarstellungs-Schriftsatz. Abgrenzung zu abmahnung-urheberrecht (klassische Abmahnung) und verletzungs-triage.

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
- (kein Argument) → fragen: "Sollen wir eine Meldung senden, auf eine eingegangene reagieren oder eine Gegenvorstellung formulieren?"

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

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

### Kommentare

- Köhler, in: Köhler/Bornkamm/Feddersen, UWG, 43. Aufl. 2025, § 8 Rn. 2.1 (Unterlassungsanspruch; Störerhaftung)
- Leistner/Ohst, in: Schricker/Löwenheim, UrhG, 6. Aufl. 2020, § 97 Rn. 1 (Unterlassung und Schadensersatz)
- Quellenregel: Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff; keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen.

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
│ VOR DEM VERSAND DIESER MELDUNG │
├─────────────────────────────────────────────────────────────┤
│ │
│ Eine Notice-and-Take-Down-Meldung hat unmittelbare │
│ rechtliche Wirkung. Unberechtigt eingereichte Meldungen │
│ können Schadensersatzansprüche des Diensteanbieters │
│ oder des betroffenen Nutzers auslösen (§§ 823, 826 BGB; │
│ Art. 17 Abs. 8 DSA für Missbrauch des Meldeverfahrens). │
│ │
│ Vor dem Versand bestätigen: │
│ │
│ 1. Sie sind Rechtsinhaber oder bevollmächtigt. │
│ 2. Die beanstandete Nutzung ist nicht gestattet — │
│ Lizenzen, Schranken und Gestattungen wurden │
│ geprüft. │
│ 3. Schranken (§§ 44a ff. UrhG, insb. Zitat § 51, │
│ Parodie § 51a) sind nicht einschlägig. │
│ 4. Die versendende Person hat Genehmigung gemäß │
│ Mandatsprofil. │
│ │
│ Genehmigung gemäß Mandatsprofil: [Genehmigende Person] │
│ │
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
│ VOR DEM VERSAND DIESER GEGENVORSTELLUNG │
├─────────────────────────────────────────────────────────────┤
│ │
│ Eine Gegenvorstellung bestreitet die Berechtigung │
│ der ursprünglichen Meldung und kann den Absender zu │
│ rechtlichen Schritten veranlassen. │
│ │
│ • Bei Eskalation durch den Absender: Klage auf │
│ Unterlassung oder Schadensersatz nach § 97 UrhG │
│ möglich. │
│ │
│ • DSA Art. 20: Beschwerde bei Plattform möglich. │
│ Art. 21: Außergerichtliche Streitbeilegung verfügbar. │
│ │
│ Vor dem Versand bestätigen: │
│ 1. Guter Glaube besteht — Lizenz, Schranke oder │
│ fehlendes Recht des Absenders ist konkret │
│ benennbar. │
│ 2. Anwalt hat diese Gegenvorstellung vor dem │
│ Versand geprüft. │
│ 3. Genehmigung gemäß Mandatsprofil liegt vor. │
│ │
│ Genehmigung gemäß Mandatsprofil: [Genehmigende Person] │
│ │
└─────────────────────────────────────────────────────────────┘
```

## Ausgabeformat

- `--senden`: Meldungsentwurf (Klartext, zum Einreichen über plattformeigenen Meldepfad oder per E-Mail an Diensteanbieter). Im Chat zur Überprüfung zeigen, bevor auf Disk gespeichert.
- `--reagieren`: Triagierungsvermerk mit Arbeitsergebnis-Kopfzeile; privilegiert und vertraulich.
- `--gegenvorstellung`: Gegenvorstellungsentwurf (Klartext). Im Chat zur Überprüfung zeigen.

Abschlusssatz (in-Chat-Vorschau): *"Dies ist ein Entwurf zur anwaltlichen Prüfung, kein versandfertiges Schreiben. Ein Rechtsanwalt prüft, bearbeitet und übernimmt fachliche Verantwortung vor dem Versand."*

## Beispiel

**Eingabe:** `/gewerblicher-rechtsschutz:takedown-anweisung --senden` — Fotograf meldet unerlaubte Nutzung seines Fotos auf einer Nachrichtenwebsite.

**Auszug Meldungsentwurf:**

> An: [Name Diensteanbieter / Hostprovider]
> Betreff: Meldung einer Urheberrechtsverletzung nach § 7 Abs. 2 DDG
>
> Sehr geehrte Damen und Herren,
>
> ich bin Rechtsinhaber / bevollmächtigte Vertreterin für folgendes urheberrechtlich geschütztes Werk:
> Fotografie "[Bildtitel]", aufgenommen am [Datum], Urheber [Name] (§ 7 UrhG).
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
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- **Kommentar:** Spindler/Schuster eMedienR oder Köhler/Bornkamm/Feddersen UWG mit § und Randnummer
- Modellannahmen als `[Modellwissen — verifizieren]` kennzeichnen.

## Triage-Fragen vor Takedown

Bevor der Takedown ausgeloest wird, klaere:
1. Liegt eine klare Rechtsverletzung vor oder handelt es sich um Kritik/Parodie/Satire (urheberrechtliche Schranke)?
2. Ist der Rechteinhaber klar identifiziert und ist der Einreicher zur Meldung berechtigt?
3. Ist die Plattform eine Very Large Online Platform (VLOP) nach DSA Art. 33 (Pflicht zu foermlicehem Notice-and-Action-Verfahren)?
4. Wurde das NetzDG geprueft (§§ 1-3 NetzDG) fuer strafbare Inhalte mit eigenen Loeschfristen?

## Aktuelle Rechtsprechung

> Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

> Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

> **DSA (EU) 2022/2065, Art. 16/17 (Digital Services Act):** Hosting-Dienstleister muessen wirksame und zugaengliche Melde- und Abhilfemechanismen einrichten; bei VLOP gelten verstaerkte Transparenz- und Reaktionspflichten; Verstoss kann zu Bussgeldern bis 6 % des globalen Jahresumsatzes fuehren.

<!-- AUDIT 27.05.2026: Bundle 032 Halluzinations-Reparatur
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
-->

## 2. `unterlassungsverlangen`

**Fokus:** Schutzrechtsinhaber will Verletzung abmahnen oder hat selbst Abmahnung erhalten. Abmahnung Unterlassung MarkenG PatG UrhG UWG. Prüfraster: Abmahnungsentwurf modifizierte Unterlassungserklärung Streitwert Kostenansatz RVG oder Reaktions-Optionsmemo bei erhaltener Abmahnung. Output: Abmahnungsschreiben oder Optionsmemo mit Risikobewertung. Abgrenzung zu schutzschrift-eilverfuegung (Praeventiv) und verletzungs-triage (Eingangsentscheidung).

# Abmahnung

Zwei Modi. Einen wählen:

- `/gewerblicher-rechtsschutz:abmahnung-urheberrecht --senden` – Abmahnungsentwurf kalibriert auf die Durchsetzungsstrategie der Kanzlei. Genehmigungsgate läuft vor Versand.
- `/gewerblicher-rechtsschutz:abmahnung-urheberrecht --empfangen` – Eingehende Abmahnung triagieren. Erzeugt ein Optionen-Memo mit Empfehlung.

## Zweck

Abmahnungen nach deutschem Recht dienen der Geltendmachung von Unterlassungsansprüchen wegen Marken- (§ 14 MarkenG), Urheber- (§ 97 Abs. 1 UrhG), Patent- (§ 139 PatG), Design- (§ 42 DesignG) oder Wettbewerbsverstößen (§ 8 UWG). Die ordnungsgemäß formulierte Abmahnung unterbricht die Wiederholungsgefahr, schafft Kostenerstattungsansprüche (§ 13 UWG; § 97a UrhG) und ist Voraussetzung für einen Antrag auf einstweilige Verfügung.

## Eingaben

- Kanzleiprofil (Durchsetzungsstrategie, Genehmigungsmatrix) – automatisch geladen
- Rechtsgrundlage des Verstoßes (Marke, Urheber, Patent, Design, UWG)
- Konkrete Verletzungshandlung mit Beschreibung und Beweisen (URLs, Screenshots, Fotos)
- Registernummer des verletzten Schutzrechts (falls eingetragen)
- Gegner: Name, Anschrift, Vertreter (falls bekannt)
- Gewünschte Frist zur Reaktion (Standard: 10–14 Tage, kürzer bei dringendem Eilbedarf)
- Streitwertvorgabe (falls vorhanden) oder Antrag auf Schätzung

## Ablauf – Sendemodus

### 1. Kanzleiprofil lesen
Durchsetzungsstrategie und Genehmigungsmatrix laden. Enthält das Profil `[PLATZHALTER]`, stoppen und auf `gewerblicher-rechtsschutz-kaltstart-interview` hinweisen.

### 2. Verletzung rechtlich einordnen

Gegenstand bestimmen:

**Markenrecht (§ 14 MarkenG):**
- Kennzeichen: eingetragene Marke, Benutzungsmarke, geschäftliche Bezeichnung
- Verletzungsform: Identität (§ 14 Abs. 2 Nr. 1), Verwechslungsgefahr (§ 14 Abs. 2 Nr. 2), Rufausnutzung/-beeinträchtigung bekannter Marken (§ 14 Abs. 2 Nr. 3)
- Prüfung: Benutzung im geschäftlichen Verkehr, für Waren/Dienstleistungen, ohne Zustimmung
- Benutzungsschonfrist: eingetragene Marke muss 5 Jahre ernsthaft benutzt sein (§ 26 MarkenG), sonst Einrede nach § 25 MarkenG
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

**Urheberrecht (§ 97 Abs. 1 UrhG):**
- Schutzvoraussetzungen: persönliche geistige Schöpfung (§ 2 Abs. 2 UrhG); keine Neuheitsprüfung
- Verletzungshandlungen: Vervielfältigung (§ 16 UrhG), Verbreitung (§ 17 UrhG), öffentliche Zugänglichmachung (§ 19a UrhG)
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

**Wettbewerbsrecht (§ 8 Abs. 1 UWG):**
- Unlautere geschäftliche Handlung: §§ 3 ff. UWG; Beispiele: Irreführung (§ 5 UWG), Anschwärzung (§ 4 Nr. 2 UWG), vergleichende Werbung (§ 6 UWG), unzumutbare Belästigung (§ 7 UWG)
- Mitbewerber, Verbraucherverbände, qualifizierte Einrichtungen (§ 8 Abs. 3 UWG) anspruchsberechtigt
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

**Patentrecht (§ 139 PatG):**
- Patentanspruch muss in Kraft sein, nicht nichtig
- Verletzungshandlungen: § 9 PatG (Herstellung, Anbieten, Inverkehrbringen, Gebrauch, Einfuhr)
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

### 3. Abmahnschreiben formulieren

**Pflichtbestandteile einer wirksamen Abmahnung** (§ 13 Abs. 2 UWG; § 97a Abs. 2 UrhG; allg. Zivilrecht):

1. Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
2. **Bezeichnung des verletzten Rechts** – einschließlich Registernummer bei eingetragenen Rechten
3. **Unterlassungsaufforderung** – klar und bestimmt (§ 253 Abs. 2 Nr. 2 ZPO analog)
4. **Beifügen einer vorformulierten modifizierten Unterlassungserklärung** mit Vertragsstrafe
5. **Fristsetzung** – in der Regel 10–14 Tage; bei Eilbedarf kürzer (3–5 Tage); starre Fristen sind problematisch wenn sie faktisch unerreichbar sind
6. **Kostenhinweis** – Ankündigung der Geltendmachung von Abmahnkosten nach §§ 13, 14 UWG; § 97a Abs. 1 UrhG; RVG

**Modifizierte Unterlassungserklärung:**
- Abgabe einer unmodifizierten strafbewehrten UE beseitigt Wiederholungsgefahr; modifizierte UE mit zu niedriger Vertragsstrafe oder eingeschränktem Umfang dagegen nicht
- Empfohlene Formulierung: "... verpflichte mich, es bei Meidung einer für jeden Fall der Zuwiderhandlung zu zahlenden angemessenen Vertragsstrafe, deren Höhe vom Gläubiger nach billigem Ermessen festgesetzt und im Streitfall vom zuständigen Gericht überprüft wird (sog. Hamburger Brauch), zu unterlassen, ..."
- Hamburger Brauch vorzugswürdig gegenüber Festbetrag, um spätere Streitigkeiten über Strafhöhe zu vermeiden
- Geografischer und sachlicher Umfang muss dem abgemahnten Verstoß entsprechen
- Frist für UE-Abgabe ausdrücklich nennen

### 4. Streitwert berechnen

Streitwert bestimmt Gerichtskostenvorschuss und RVG-Gebühren:

| Verletzungsart | Typische Streitwertbandbreite (OLG-Rspr.) |
|---|---|
| Markenrecht (eingetragene Marke, kommerziell) | 25.000 – 150.000 € |
| Markenrecht (Benutzungsmarke, lokal) | 10.000 – 50.000 € |
| Urheberrecht (professionelles Werk) | 6.000 – 50.000 € |
| Urheberrecht (Lichtbild § 72 UrhG) | 3.000 – 10.000 € |
| UWG (Wettbewerbsverstoß, mittelständisch) | 10.000 – 100.000 € |
| Patent (kommerziell bedeutend) | 250.000 – 2.000.000 € |

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

### 5. Kostenerstattungsanspruch berechnen (RVG)

Abmahnkosten nach § 13 Abs. 3 UWG (bei UWG-Abmahnungen) oder allgemeinen Grundsätzen (§§ 683, 670 BGB) sind erstattungsfähig:

- Gegenstandswert: Streitwert der Abmahnung
- Gebühr: 1,3-fache Geschäftsgebühr (Nr. 2300 VV RVG) ggf. erhöht
- Zzgl. Auslagenpauschale (Nr. 7002 VV RVG): 20 € (max. 20 % der Gebühren)
- Zzgl. Umsatzsteuer (§ 19a UStG beachten, falls USt-pflichtig)

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

### 6. Pre-Delivery-Gate

Vor dem Versand prüfen:
- [ ] Verletzung ausreichend dokumentiert? (Screenshots mit Datum, URL-Angabe, Notarstaat bei Bedarf)
- [ ] Registernummer des Schutzrechts verifiziert und in Kraft?
- [ ] Benutzungsschonfrist (§ 26 MarkenG) geprüft?
- [ ] UE-Formulierung vollständig und angemessen umfangreich?
- [ ] Streitwert anwaltlich plausibilisiert?
- [ ] Genehmiger aus Kanzleiprofil informiert?
- [ ] Mandant über mögliche Gegensanktionen (§ 8c UWG: missbräuchliche Abmahnung, Schadensersatz) informiert?

**Missbrauchsprüfung (§ 8c UWG):** Indizien für missbräuchliche Abmahnung: überwiegend Gebührengenerierung; Gläubiger hat zahlreiche gleichartige Verletzungen abgemahnt; Streitwert unverhältnismäßig; Frist unangemessen kurz. Missbräuchliche Abmahnung löst Schadensersatzpflicht des Abmahnenden aus (§ 8c Abs. 2 UWG); Freistellungsanspruch des Abgemahnten.

## Ablauf – Empfangsmodus

### 1. Abmahnung aufnehmen und Frist notieren
Datum des Zugangs und gesetzte Frist sofort vermerken. Frist für UE-Abgabe und ggf. einstweilige Verfügung bestimmen (EV ohne vorherige Abmahnung üblich; nach Fristablauf droht Hauptsacheverfahren).

### 2. Formelle Wirksamkeitsprüfung
Prüfen: Ist die Abmahnung hinreichend bestimmt? Enthält sie das verletzte Recht und die konkrete Verletzungshandlung? Ist die UE beigefügt? Eine formell unwirksame Abmahnung begründet keinen Kostenerstattungsanspruch und kann Rückschlüsse auf die Durchsetzungsabsicht erlauben.

### 3. Handlungsoptionen-Memo

| Option | Beschreibung | Wann passend |
|---|---|---|
| **A) UE-Abgabe (unmodifiziert)** | Strafbewehrte UE in vorgeschlagenem Umfang abgeben | Verletzung eindeutig, Umfang angemessen, keine Gegenwehr sinnvoll |
| **B) Modifizierte UE** | Eigene UE mit eingeschränktem Umfang / niedrigerer Vertragsstrafe anbieten | Verletzung teilweise bestreitbar, Umfang zu weit, Verhandlungsspielraum |
| **C) Negative Feststellungsklage** | Rechtshängigkeitssperre durch NFL (§ 256 ZPO) | Abmahnung offensichtlich unbegründet, Zermürbungsversuch |
| **D) Widerspruch / Abweisung** | Abmahnung zurückweisen, ggf. Gegenansprüche anmelden | § 8c UWG-Missbrauch wahrscheinlich, fehlende Aktivlegitimation |
| **E) Verhandlung** | Ohne UE verhandeln, Vergleich anstreben | Starkes Interesse beider Seiten an Lösung, kommerzieller Kontext |

## Quellen und Zitierweise

Zitierweise nach `../references/zitierweise.md`.

**Wichtige Normen:** §§ 8, 12, 13, 14 UWG; § 97 Abs. 1, § 97a, § 139 UrhG; §§ 14, 26 MarkenG; § 139 PatG; § 42 DesignG.

**Leitentscheidungen:**
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

- Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen zitieren. Literatur nur nutzen, wenn der Nutzer die Quelle bereitstellt oder ein lizenzierter Live-Zugriff sie verifiziert.
- Köhler, in: Köhler/Bornkamm/Feddersen, UWG, 43. Aufl. 2025, § 8 Rn. 1.1 ff.
- Ingerl/Rohnke, MarkenG, 3. Aufl. 2010, § 14 Rn. 345 ff. (vor. auf BGH-Rspr. aktualisieren).
- Dreier/Schulze, UrhG, 7. Aufl. 2022, § 97a Rn. 12 ff.

## Ausgabeformat

**Sendemodus:** Abmahnschreiben als vollständiger Briefentwurf (Briefkopf, Datum, Empfänger, Betreff, Sachverhalt, Rechtslage, Forderungen, Fristangabe, Anlagen-Verzeichnis: modifizierte UE) + separater Prüfvermerk.

**Empfangsmodus:** Optionen-Memo mit Zusammenfassung der Abmahnung, Fristnotiz, Risikoeinschätzung je Option (Ampel 🔴/🟠/🟡/🟢), Empfehlung und Entscheidungsbaum.

## Beispiel (Sendemodus – Markenrechtliche Abmahnung)

> **Sachverhalt:** Mandant ist Inhaber der deutschen Wortmarke "NORDBLATT" (DPMA-Reg.-Nr. 30 2019 012 345, eingetragen für Kl. 25), registriert seit 2019. Dritter bietet auf einer Verkaufsplattform Oberbekleidung unter der Bezeichnung "NORDBLATT" an.

**Rechtliche Einordnung (Gutachtenstil):**

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

*Benutzungsschonfrist:* Die Marke ist seit 2019 eingetragen; die Fünfjahresfrist (§ 26 Abs. 5 MarkenG) läuft ab 2024; ernsthafte Benutzung durch Mandant zu dokumentieren. `[prüfen]`

*Unterlassungsanspruch:* Es besteht Wiederholungsgefahr (tatsächliche Verletzungshandlung); Unterlassungsanspruch aus § 14 Abs. 5 MarkenG gegeben.

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

*Kosten:* 1,3-Geschäftsgebühr aus 50.000 € nach Nr. 2300 VV RVG = 1.641,40 € zzgl. 20 € Auslagenpauschale = 1.661,40 € zzgl. MwSt.

## Risiken / typische Fehler

- **Zu knappe Frist:** Fristen unter 3 Tagen können als unangemessen gelten und die Wiederholungsgefahr nicht wirksam beseitigen; bei bekannter Urlaubszeit oder Auslandssitz verlängern.
- **Unklarer Unterlassungsgegenstand:** Die abgemahnte Handlung muss vollstreckungstauglich beschrieben sein; andernfalls kann ein Unterlassungstitel nicht vollstreckt werden (§ 890 ZPO).
- **Missbräuchlichkeit (§ 8c UWG):** Serielle Abmahnungen mit primärem Kostenerzielungszweck sind missbräuchlich und begründen Schadensersatzpflichten; Massenfälle vorab auf Missbrauchsrisiko prüfen.
- **Benutzungsschonfrist (§ 26 MarkenG):** Unterlassene Prüfung gefährdet das gesamte Abmahnungsverfahren, wenn der Verletzer die Einrede erhebt.
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- **Kein Versand ohne Freigabe:** Das Plugin sendet keine Abmahnung; es entwirft und wartet auf Genehmigung durch den konfigurierten Genehmiger.

## Triage-Fragen vor Unterlassungsverlangen

Bevor das Unterlassungsverlangen formuliert wird, klaere:
1. Liegt Wiederholungsgefahr (tatsaechliche Verletzung) oder nur Erstbegehungsgefahr vor?
2. Ist die abgemahnte Handlung vollstreckungstauglich beschreibbar (§ 890 ZPO — keine vagen Formulierungen)?
3. Wurde die Unterlassungserklaerung ausreichend strafbewehrt (Hamburger Brauch vs. feste Vertragsstrafe)?
4. Ist die Dringlichkeitsfrist fuer eine spaetere einstweilige Verfuegung gewahrt (BGH: max. 4-6 Wochen nach Kenntniserlangung)?

## Aktuelle Rechtsprechung

> Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

> Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

> Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Audit-Hinweis (27.05.2026)

Im Halluzinations-Audit 2026-05-27 wurden in diesem Skill folgende
Aktenzeichen geprueft und korrigiert:
- BGH I ZR 153/16 (WRONG_TOPIC: tatsaechlich "19% MwSt. GESCHENKT" — irrefuehrende Werbung, nicht Unterlassungserklaerung-Praezision): ersetzt durch verifizierte Entscheidung BGH I ZR 82/99 vom 31.05.2001 (Weit-Vor-Winter-Schluss-Verkauf), GRUR 2002, 180 (Quelle: dejure.org/2001,536)

## 3. `verletzungs-triage`

**Fokus:** Mandant sieht IP-Verletzung oder hat Verletzungsschreiben erhalten und fragt: Was ist zu tun? Verletzungs-Triage gewerblicher Rechtsschutz. Prüfraster: Marke § 14 MarkenG Patent § 9 PatG Urheber § 97 UrhG Wettbewerb § 8 UWG Entscheidungsempfehlung Ignorieren/informelles Schreiben/Abmahnung/eV/Klage. Output: Entscheidungs-Memo mit Empfehlung und naechstem Schritt. Abgrenzung zu unterlassungsverlangen (Abmahnung selbst) und mandat-triage-gewerblicher-rechtsschutz.

# Verletzungs-Triage

## Zweck

Strukturierte Erstbewertung einer möglichen Schutzrechtsverletzung. Der Skill klärt, welches Recht verletzt sein könnte, bewertet den kommerziellen und rechtlichen Schweregrad und empfiehlt die verhältnismäßige Reaktion auf einer fünfstufigen Skala: von "Ignorieren" bis "Sofortklage". Die Empfehlung wird kalibriert an der im Kanzleiprofil hinterlegten Durchsetzungsstrategie.

## Eingaben

- Beschreibung der möglichen Verletzungshandlung (mit Beweismitteln: URLs, Screenshots, Produktbeschreibungen, Werbematerial)
- Art des eigenen Schutzrechts (falls bekannt: Registernummer)
- Identität der gegnerischen Partei (falls bekannt)
- Kommerzieller Kontext (Wettbewerber, Trittbrettfahrer, gutgläubiger Dritter)
- Zeitpunkt der Entdeckung
- Marktsituation (Marktanteile, wirtschaftlicher Schaden schätzungsweise)

## Ablauf

### 1. Rechtsgrundlage identifizieren

Zunächst bestimmen, welches Recht verletzt sein könnte:

#### Markenrecht (§ 14 MarkenG)

**Verletzungsformen:**
- § 14 Abs. 2 Nr. 1: Doppelidentität (identisches Zeichen + identische Waren/DL)
- § 14 Abs. 2 Nr. 2: Verwechslungsgefahr (ähnliches Zeichen + ähnliche Waren/DL)
- § 14 Abs. 2 Nr. 3: Bekannte Marke, Rufausnutzung/-beeinträchtigung

**Checkliste Markenrechtsverletzung:**
- [ ] Handelt der Verletzer im geschäftlichen Verkehr?
- [ ] Benutzt er das Zeichen für Waren oder Dienstleistungen?
- [ ] Fehlt die Zustimmung des Markeninhabers?
- [ ] Ist die Marke schutzfähig und nicht durch Einreden (Benutzungsschonfrist § 26 MarkenG, Verfalls § 53 MarkenG) gefährdet?
- [ ] Greift keine Schranke (§§ 20–26 MarkenG: beschreibende Benutzung, rein dekorative Benutzung)?

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

#### Patentrecht (§ 9 PatG)

**Verletzungshandlungen:**
- § 9 Satz 2 Nr. 1: Herstellen, Anbieten, Inverkehrbringen, Gebrauchen, Einführen oder Besitzen des patentierten Erzeugnisses
- § 9 Satz 2 Nr. 2: Anbieten/Liefern von Mitteln zur Benutzung der Erfindung (mittelbare Patentverletzung, § 10 PatG)
- § 9 Satz 2 Nr. 3: Verfahrenspatentverletzung

**Checkliste Patentverletzung:**
- [ ] Patent in Kraft (Jahresgebühren, keine Nichtigerklärung)?
- [ ] Alle Merkmale des Hauptanspruchs im Verletzungsgegenstand?
- [ ] Äquivalenzprüfung erforderlich? (BGH – "Pemetrexed")
- [ ] Schranken (§§ 11, 12 PatG: Privatbenutzung, Vorbenützungsrecht)?

#### Urheberrecht (§ 97 Abs. 1 UrhG)

**Verletzungshandlungen:** Vervielfältigung (§ 16), Verbreitung (§ 17), öffentliche Zugänglichmachung (§ 19a), Bearbeitung ohne Zustimmung (§ 23).

**Checkliste Urheberrechtsverletzung:**
- [ ] Werk urheberrechtlich schutzfähig (§ 2 UrhG, persönliche geistige Schöpfung)?
- [ ] Urheber/Rechteinhaber identifiziert?
- [ ] Schutzfrist nicht abgelaufen (70 Jahre nach Tod des Urhebers, § 64 UrhG)?
- [ ] Keine Schranke (§§ 44a ff. UrhG: Zitat, Karikaturl Parodik)?
- [ ] Nachweis der Verletzung ausreichend (z. B. Hash-Vergleich bei Filesharing)?

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

#### Wettbewerbsrecht (§ 8 UWG)

**Verletzungshandlungen:** Unlautere geschäftliche Handlungen gem. §§ 3 ff. UWG (Irreführung § 5, Anschwärzung § 4 Nr. 2, Imitation § 4 Nr. 3, vergleichende Werbung § 6, aggressive Praktiken § 4a, unzumutbare Belästigung § 7).

**Checkliste UWG-Verstoß:**
- [ ] Geschäftliche Handlung?
- [ ] Unlauterkeit nachweisbar?
- [ ] Mitbewerber, qualifizierte Einrichtung oder Verbraucherschutzverband anspruchsberechtigt (§ 8 Abs. 3 UWG)?
- [ ] Besondere Gefahr des Leistungsschutzes nach § 4 Nr. 3 UWG (konkrete Nachahmung)?

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

### 2. Schwere der Verletzung bewerten

**Faktoren:**

| Faktor | Erhöht Schwere | Vermindert Schwere |
|---|---|---|
| Kommerzieller Schaden | Konkreter Umsatzverlust nachweisbar | Kein messbarer Schaden |
| Vorsatz | Bewusstes Kopieren, Wiederholungstäter | Gutgläubig, einmaliger Verstoß |
| Reichweite | Bundesweite oder internationale Verbreitung | Lokal begrenzt |
| Wettbewerbssituation | Direkter Wettbewerber | Randmarkt, kein direkter Wettbewerber |
| Zeitkritizität | Weihnachtsgeschäft, Produkteinführung | Kein Zeitdruck |
| Beweissituation | Klare Verletzung dokumentiert | Verletzung bestreitbar |

### 3. Handlungsoptionen

| Option | Beschreibung | Geeignet wenn |
|---|---|---|
| **A) Ignorieren / Beobachten** | Aktenvermerk; Beobachtung; kein aktives Vorgehen | Geringfügig, kein kommerzieller Schaden, defensiver Mandant |
| **B) Informelles Schreiben** | Freundliche Kontaktaufnahme ohne Anwaltsbrief; Aufforderung zur Unterlassung ohne Vertragsstrafe | Gutgläubiger Dritter; Erstkontakt sinnvoll; Beziehungserhalt |
| **C) Abmahnung** | Förmliche Abmahnung mit modifizierter Unterlassungserklärung und Kostenerstattungsanspruch | Klare Verletzung; ausgewogene/offensive Strategie; Kostenerstattung gewünscht |
| **D) Einstweilige Verfügung** | Antrag auf EV ohne vorherige Abmahnung (Dringlichkeit); oder nach fruchtlosem Fristablauf | Eilbedürftigkeit; drohende Messepräsenz; laufende Verletzung mit steigendem Schaden |
| **E) Hauptsacheklage** | Klage auf Unterlassung, Schadensersatz, Auskunft | Schwere Verletzung; Abmahnung erfolglos; hoher Streitwert; Grundsatzklärung |

**Dringlichkeitsprüfung für einstweilige Verfügung:**
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- EV-Antrag muss schlüssig und mit eidesstattlichen Versicherungen gestützt sein
- Vollziehungsfrist: EV muss innerhalb 1 Monat zugestellt werden (§ 929 Abs. 2 ZPO)

### 4. Strategische Einschätzung

**Kostenrisiko:**
Streitwert und voraussichtliche Kosten (beide Seiten) grob schätzen:
- OLG-Verfahren Markenrecht: oft 5.000–30.000 € Anwaltskosten je Seite
- LG-Hauptsacheklage Patent: oft 50.000–200.000 €+ je Seite
- EV-Verfahren: i. d. R. günstiger, aber Abschlussschreiben folgt

**Gegenmaßnahmen-Risiko:**
- Kann Gegner Widerklage auf Nichtigkeit (Patent) oder Löschung (Marke) erheben?
- Gegenseitige Verletzungsansprüche?
- Reputationsrisiko bei öffentlichem Streit?

### 5. Empfehlung

Durchsetzungsstrategie aus Kanzleiprofil anwenden und klare Empfehlung formulieren (A–E), mit Begründung und Vorbehalt für anwaltliche Letztentscheidung.

## Quellen und Zitierweise

Zitierweise nach `../references/zitierweise.md`.

**Normen:** §§ 14, 15 MarkenG; §§ 9, 10, 139 PatG; §§ 97, 97a UrhG; §§ 3, 8 UWG; §§ 935–945 ZPO (EV); § 256 ZPO (NFL).

**Leitentscheidungen:**
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

- Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen zitieren. Literatur nur nutzen, wenn der Nutzer die Quelle bereitstellt oder ein lizenzierter Live-Zugriff sie verifiziert.
- Köhler, in: Köhler/Bornkamm/Feddersen, UWG, 43. Aufl. 2025, § 8 Rn. 1.100 ff.
- Ingerl/Rohnke, MarkenG, 3. Aufl. 2010, § 14 Rn. 345 ff.
- Dreier/Schulze, UrhG, 7. Aufl. 2022, § 97 Rn. 10 ff.
- Schricker/Löwenheim, UrhG, 6. Aufl. 2020, § 97 Rn. 42 ff.

## Ausgabeformat

**Triage-Memo:**
1. Sachverhaltsdarstellung (2–3 Sätze)
2. Rechtliche Einordnung (je Anspruchsgrundlage: Kurze Prüfung)
3. Schwerbewertung (Ampel: 🔴/🟠/🟡/🟢)
4. Handlungsoptionen A–E mit Vor-/Nachteilen
5. Empfehlung (kalibriert an Kanzleiprofil)
6. Entscheidungsbaum

## Risiken / typische Fehler

- **EV-Dringlichkeit verpassen:** Frist von 1 Monat ab Kenntnis läuft schnell ab; sofort nach Entdeckung handeln.
- **Beweis nicht sichern:** Screenshots, archivierte Webseiten (Wayback Machine, web.archive.org), notarielle Protokolle sofort nach Entdeckung anfertigen; Beweise könnten sonst verschwinden.
- **Gegenangriff nicht einkalkulieren:** Besonders bei Patentverfahren besteht erhebliches Nichtigkeitsrisiko; bei Marken Löschungsantrag möglich.
- **Missbrauchsrisiko § 8c UWG:** Serielle Abmahnungen mit primärem Gebührenerzielungszweck sind missbräuchlich; anwaltliche Prüfung des Gesamtbilds erforderlich.
- **Verjährung beachten:** § 20 MarkenG (3 Jahre), § 141 PatG (3 Jahre), § 102 UrhG (3 Jahre), § 11 UWG (6 Monate ab Kenntnis / 3 Jahre absolut); `[Modellwissen – prüfen]`.

<!-- AUDIT 27.05.2026: Bundle 032 Halluzinations-Reparatur
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
-->
