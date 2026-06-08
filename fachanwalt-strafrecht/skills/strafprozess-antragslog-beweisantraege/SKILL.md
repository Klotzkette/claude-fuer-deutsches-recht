---
name: strafprozess-antragslog-beweisantraege
description: "Strafprozess Antragslog Beweisantraege im Strafrecht: prüft konkret Antragslog für die Hauptverhandlung, Verteidigung gegen automatisierten biometrischen, Tägliches Strafprozess-Cockpit für Verteidiger, Haft- und Besuchsmanagement für Untersuchungshaft. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Schritt."
---

# Strafprozess Antragslog Beweisantraege

## Arbeitsbereich

**Strafprozess Antragslog Beweisantraege** ordnet den Fall über die tragenden Prüfungslinien: Antragslog für die Hauptverhandlung, Verteidigung gegen automatisierten biometrischen, Tägliches Strafprozess-Cockpit für Verteidiger. Zuerst wird das Feld bestimmt, das die Akte wirklich trägt; ergänzende Felder kommen nur hinzu, wenn sie dieselbe Frist, Zuständigkeit, Beweislast oder denselben Output berühren.
## Prüfungslinien

| Prüfungslinie | Fokus |
| --- | --- |
| `strafprozess-antragslog-beweisantraege-und-widerspruch` | Antragslog für die Hauptverhandlung: verwaltet Beweisanträge, Beweisermittlungsanträge, Widersprüche, § 257-StPO-Erklärungen, Ablehnungsbeschlüsse, Wiederholungsbedarf, Revisionssicherung und taktische Priorität. |
| `strafprozess-biometrischer-internetabgleich-98d-stpo-e` | Verteidigung gegen automatisierten biometrischen Internetabgleich nach dem Regierungsentwurf zu § 98d StPO-E: Rechtsstand prüfen, Akteneinsicht nachfordern, Anordnung, Zweck, Anlasstat, Subsidiarität, Protokollierung, Löschung, KI-VO, Drittbetroffenheit, Trefferqualität, Black-Box-Risiko und Verwertbarkeit angreifen. |
| `strafprozess-cockpit-taegliche-kanzleifuehrung` | Tägliches Strafprozess-Cockpit für Verteidiger: bearbeitet Verfahrensstand, Fristen, Haftlage, Akteneinsicht, offene Anträge, Mandantenkommunikation, Beweisfragen, Termine und nächste Schritte in einer laufend aktualisierbaren Verteidigungsübersicht. |
| `strafprozess-haft-und-besuchsmanagement` | Haft- und Besuchsmanagement für Untersuchungshaft: organisiert Haftbefehl, Haftprüfung, Haftbeschwerde, Akteneinsicht, Besuch, Telefon, Post, Familie, Arbeitgeber, Haftverschonungsplan und Beschleunigungskontrolle. |
| `strafprozess-hv-tagesmappe-und-sitzungsplan` | Hauptverhandlungs-Tagesmappe: erstellt für jeden Sitzungstag Zeitplan, Zeugen- und Beweisprogramm, Einlassungsentscheidung, Fragelisten, Antragsentwürfe, Mandantenbriefing, Pausenstrategie, Protokollnotizen und Nachbereitungsaufgaben. |

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: StGB §§ 13, 22, 23, 25, 32, 35, 46, 47, 56, 57, StPO §§ 100a, 102, 105, 112, 136, 137, 140, 147, 152, 153a, 244, 257c, 261, 264, 265, 267, 304, 341, 344, 349; StPO; StGB — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.
## Prüfungslinien im Detail

## 1. `strafprozess-antragslog-beweisantraege-und-widerspruch`

**Fokus:** Antragslog für die Hauptverhandlung: verwaltet Beweisanträge, Beweisermittlungsanträge, Widersprüche, § 257-StPO-Erklärungen, Ablehnungsbeschlüsse, Wiederholungsbedarf, Revisionssicherung und taktische Priorität.

# Antragslog, Beweisanträge und Widerspruch

## Zweck

In langen Hauptverhandlungen geht der Überblick über Anträge schnell verloren. Dieser Skill führt ein präzises Register: Was wurde gestellt, warum, wie hat das Gericht entschieden, was folgt daraus?

## Antragsregister

```text
Antragslog

Nr.:
Datum/Sitzungstag:
Art: Beweisantrag / Beweisermittlungsantrag / Widerspruch / Erklärung / Befangenheit / Aussetzung
Beweistatsache:
Beweismittel:
Konnex:
Ziel:
Beschluss/Entscheidung:
Reaktion:
Revisionsrelevanz:
Wiedervorlage:
```

## Beweisantrag-Qualität

Prüfe vor Einreichung:

- konkrete Tatsachenbehauptung,
- konkretes Beweismittel,
- Konnex zwischen Beweismittel und Beweistatsache,
- Erheblichkeit für Schuld, Rechtsfolge oder Verfahrensfrage,
- keine unnötige Breite,
- Reihenfolge im Verteidigungsnarrativ.

## Widerspruch/Beanstandung

Bei Verwertungsfragen und Verfahrensfehlern:

- Zeitpunkt festhalten,
- genaue Maßnahme benennen,
- Rechtsgrund oder Verfahrensfehler knapp angeben,
- Entscheidung des Gerichts verlangen,
- Protokollierung kontrollieren.

## Revisionssicherung

Nicht alles ist später heilbar. Deshalb am Sitzungstag prüfen:

- Wurde ein Antrag förmlich gestellt?
- Wurde er beschieden?
- Ist die Begründung dokumentiert?
- Muss eine Erklärung oder Beanstandung folgen?
- Muss der Antrag nach neuer Lage wiederholt oder angepasst werden?

## Output

- `Antragslog`
- `Beweisantrag-Entwurf`
- `Widerspruchsnotiz`
- `Revisionssicherungscheck`
- `Nächster Antrag`

## 2. `strafprozess-biometrischer-internetabgleich-98d-stpo-e`

**Fokus:** Verteidigung gegen automatisierten biometrischen Internetabgleich nach dem Regierungsentwurf zu § 98d StPO-E: Rechtsstand prüfen, Akteneinsicht nachfordern, Anordnung, Zweck, Anlasstat, Subsidiarität, Protokollierung, Löschung, KI-VO, Drittbetroffenheit, Trefferqualität, Black-Box-Risiko und Verwertbarkeit angreifen.

# Biometrischer Internetabgleich im Strafverfahren

## Zweck

Dieser Skill prüft, ob eine Strafakte auf automatisiertem biometrischem Abgleich mit öffentlich zugänglichen Internetdaten beruht oder beruhen könnte. Er ist für Verteidigung, Zeugenbeistand und strafprozessuale Qualitätssicherung gedacht.

Wichtig: § 98d StPO ist nach aktuellem Arbeitsstand als Entwurfsnorm zu behandeln. Vor jeder tragenden Aussage zuerst live prüfen, ob der Entwurf bereits Gesetz geworden ist, ob sich der Wortlaut geändert hat und welche Übergangsregel gilt.

## Sofort-Triage

Frage zuerst:

1. Geht es um Gesicht, Stimme, Gang, Iris, Fingerabdruck, Handgeometrie, Venenstruktur oder ein anderes Identifikationsmerkmal?
2. Stammt das Ausgangsmaterial aus einem Strafverfahren, einer polizeilichen Datei, einem Asservat, einer Lichtbildmappe oder einer Vernehmungs-/Videoakte?
3. Wurde nur manuell im Internet recherchiert oder eine speziell für den Abgleich entwickelte Anwendung eingesetzt?
4. Ging es um Identitätsfeststellung, Aufenthaltsort, Sachverhaltsaufklärung, Fahndung/Vollstreckung oder eine Mischung daraus?
5. Betroffen ist Beschuldigter, Zeuge, Opfer, unbeteiligter Dritter, Berufsgeheimnisträger oder eine größere Personengruppe?
6. Welche Software, welcher Datenbestand, welcher Treffer-Score, welche Schwelle und welche Nachprüfung sind aktenkundig?
7. Gibt es Anordnung, Eilentscheidung, Begründung, Protokoll, Löschvermerk, Benachrichtigung nach § 101 StPO-E oder eine erkennbare Lücke?

## Rechtsstand und Normanker

Live prüfen:

- Regierungsentwurf vom 29.04.2026 / Bundesrat-Drucksache 264/26: §§ 98d, 98e, 101 StPO-E.
- Geltendes Recht bis zum Inkrafttreten: §§ 161, 163 StPO tragen allenfalls manuelle OSINT-Recherche, nicht automatisch schon einen spezialisierten biometrischen Massenabgleich.
- § 98c StPO bleibt der einfache maschinelle Abgleich mit vorhandenen Daten; komplexe verfahrensübergreifende Analyse ist davon nicht ohne Weiteres gedeckt.
- § 147 StPO: vollständige Akteneinsicht in Anordnung, Protokolle, Trefferlisten, technische Dokumentation, Nachprüfungsvermerke und entlastende Null-/Fehltreffer verlangen.
- § 160 Abs. 2 StPO: Entlastendes muss ebenso erhoben und dokumentiert werden.
- § 101 StPO-E: Benachrichtigungspflicht für die Person, deren biometrische Daten aus dem Strafverfahren als Ausgangsmaterial genutzt wurden.
- Datenschutzrecht: JI-Richtlinie (EU) 2016/680, BDSG, besonders sensible biometrische Daten; Zweckbindung, Erforderlichkeit, Löschung und Schutzmaßnahmen.
- KI-VO: Art. 3 Nr. 1, Art. 5, Art. 6 Abs. 2 i.V.m. Anhang III Nr. 1 lit. a, Art. 9 bis 15, Art. 26, Art. 27, Art. 49, Art. 71, Art. 99 prüfen.

## Verteidigungsangriffe

### 1. Maßnahme nicht als Handrecherche tarnen

Trenne sauber:

- Handrecherche mit üblichen Suchmaschinen,
- OSINT-Auswertung ohne spezialisierten biometrischen Abgleich,
- automatisierter biometrischer Abgleich mit Embeddings, Vergleichsdatenbank, Treffer-Score oder KI-Komponente,
- verfahrensübergreifende Datenanalyse.

Wenn eine Anwendung numerische Repräsentationen, Ähnlichkeitsscores, Cluster, Trefferlisten oder Ranking erzeugt, muss die Akte das offenlegen. Der Begriff “öffentlich zugänglich” ersetzt keine Befugnis für automatisierte Erhebung, Umwandlung, Speicherung und Bewertung biometrischer Daten.

### 2. Anlasstat und Verdacht

Angriffspunkte:

- Verdacht nur behauptet, aber nicht durch bestimmte Tatsachen getragen.
- Tat nur von geringer Bedeutung oder bloß formelhaft als “erheblich” bezeichnet.
- Pauschaler Verweis auf § 100a Abs. 2 StPO ohne einzelfallbezogene Schwere.
- Ausgangsdaten stammen aus Bagatellverfahren, Altverfahren oder fremden Verfahren ohne tragfähige Zweckbindung.
- Maßnahme richtet sich faktisch gegen Zeugen oder Dritte, obwohl deren eigenes Fehlverhalten nicht konkretisiert ist.

Arbeitsfrage: Würde die Maßnahme auch dann noch verhältnismäßig wirken, wenn das Gericht die Anzahl der miterfassten Unbeteiligten, die Sensibilität biometrischer Daten und die Möglichkeit späterer Profilbildung ernsthaft einrechnet?

### 3. Zweck überdehnt

Besonders kritisch ist der Einsatz zur allgemeinen Sachverhaltserforschung. Der Skill soll hier nicht nur “zulässig/unzulässig” sagen, sondern den Zweck scharf zuschneiden:

| Zweck | Verteidigungsfrage |
| --- | --- |
| Identität Beschuldigter | Gab es mildere Mittel, etwa Zeugen, Register, bekannte Fotos, Ausweisdaten? |
| Aufenthaltsort Beschuldigter | Ist die Maßnahme wirklich erforderlich oder nur bequem? |
| Zeugenauffindung | Warum darf eine hochintensive Maßnahme gegen Nichtbeschuldigte laufen? |
| Sachverhaltsaufklärung | Droht Profilbildung aus Social-Media-Kontext, Interessen, Kontakten, Orten? |
| Vollstreckung/Fahndung | Ist die konkrete Fahndungslage dokumentiert oder nur routinemäßig behauptet? |

### 4. Subsidiarität ernst nehmen

Die Klausel “wesentlich erschwert oder aussichtslos” darf nicht zur Floskel werden. Verlange aktenkundig:

- Welche herkömmlichen Ermittlungsansätze wurden geprüft?
- Warum reichen Ladung, Befragung, Registerabfrage, Bestandsdaten, Lichtbildvorlage, Umfeldaufklärung oder gezielte Observation nicht?
- Wurde der Einsatz nur gewählt, weil er schneller und bequemer ist?
- Welche Gründe sprechen gegen weniger streubreite Maßnahmen?

Wenn die Begründung nur aus Textbausteinen besteht: als Verhältnismäßigkeits- und Begründungsdefizit markieren.

### 5. Anordnung und Richtervorbehalt

Der Entwurf sieht eine staatsanwaltschaftliche Anordnung und eine Eilkompetenz der Ermittlungspersonen vor. Verteidigerisch prüfen:

- Gibt es überhaupt eine Anordnung?
- Ist sie einzelfallbezogen begründet?
- Wurde Gefahr im Verzug konkret belegt oder nur behauptet?
- Wurde eine spätere Entscheidung fristgerecht herbeigeführt?
- Ist wegen Eingriffsintensität ein Richtervorbehalt verfassungsrechtlich zu fordern?

Im Schriftsatz kann der fehlende Richtervorbehalt nicht mechanisch als “immer tödlich” behandelt werden. Besser: anhand Eingriffsgewicht, Streubreite, Heimlichkeit, Sensibilität der Daten, KI-Einsatz und Drittbetroffenheit verdichten.

### 6. Technische Black-Box aufbrechen

Fordere mindestens:

- Name und Version der Anwendung,
- Anbieter, Betreiber, Betriebsort, Schnittstellen,
- verwendete Datenquellen und Abrufwege,
- ob registrierungs-, genehmigungs- oder entgeltpflichtige Inhalte einbezogen wurden,
- ob Echtzeitdaten, Streams oder Webcam-/Live-Inhalte ausgeschlossen waren,
- Treffer-Schwellenwert, Score, Falschakzeptanz-/Falschrückweisungsrisiko,
- menschliche Nachprüfung und deren Ergebnis,
- Protokolle nach § 98d Abs. 2 StPO-E,
- Löschvermerk nach § 98d Abs. 3 StPO-E,
- technische Dokumentation, Risiko- und Grundrechte-Folgenabschätzung bei KI-Einsatz.

Wenn die Akte nur “Treffer durch Software” enthält, ist sie verteidigungspraktisch unbrauchbar. Das genügt nicht für belastbare Beweiswürdigung.

## KI-VO-Prüfraster

Wenn KI-Komponenten genutzt werden:

1. Ist es ein KI-System nach Art. 3 Nr. 1 KI-VO?
2. Liegt verbotene Echtzeit-Fernidentifizierung vor oder ausdrücklich nur nachträglicher Abgleich?
3. Entsteht durch Scraping/ungezieltes Auslesen eine unzulässige Gesichtserkennungsdatenbank?
4. Hochrisiko-System nach Art. 6 Abs. 2 i.V.m. Anhang III Nr. 1 lit. a?
5. Risikomanagement, Datenqualität, technische Dokumentation, Protokollierung, Transparenz, menschliche Aufsicht, Genauigkeit, Robustheit und Cybersicherheit belegt?
6. Grundrechte-Folgenabschätzung nach Art. 27 KI-VO vorhanden?
7. Wurde das System nur bestimmungsgemäß nach Anbieteranleitung eingesetzt?
8. Können Verteidigung und Gericht die Trefferentstehung nachvollziehen?

## Verwertungsstrategie

Arbeite mehrstufig:

1. **Akteneinsichtsnachforderung**: fehlende Anordnung, Softwaredaten, Protokoll, Löschung, Dokumentation, Score, menschliche Prüfung.
2. **Zwischenangriff im Ermittlungsverfahren**: Einstellung, Löschung, Unterlassung weiterer Nutzung, Beschränkung auf manuelle Nachprüfung.
3. **Hauptverhandlung**: Widerspruch gegen Verwertung rechtzeitig erheben; Sachverständigenbeweis zur Trefferqualität und Methodik beantragen.
4. **Beweiswürdigung**: selbst bei formaler Verwertbarkeit Treffer nur als Ermittlungsansatz behandeln, nicht als Identitätsbeweis.
5. **Revision**: Verfahrensrüge nur mit vollständiger Dokumentation des rechtzeitig erhobenen Widerspruchs und der verletzten Verfahrensnorm.

## Muster: Nachforderung

```text
Wir bitten um vollständige Akteneinsicht in alle Unterlagen zur biometrischen Abgleichmaßnahme:

1. Anordnung einschließlich Begründung, Zweck, Verdachtsgrundlage und Subsidiaritätsprüfung,
2. Bezeichnung, Version und Betreiber der eingesetzten Anwendung,
3. Datenquellen, Abrufwege, Suchparameter, Trefferlisten, Scores und Schwellenwerte,
4. Protokollierung des Einsatzes einschließlich Organisationseinheit und Zeitpunkt,
5. Dokumentation der menschlichen Nachprüfung,
6. Löschvermerk und Zweckbindungsprüfung,
7. Unterlagen zu KI-VO-Konformität, Risikomanagement, Datenqualität und Grundrechte-Folgenabschätzung.

Vor vollständiger Offenlegung kann die Verteidigung weder die Rechtmäßigkeit noch die Beweisbedeutung des behaupteten Treffers prüfen.
```

## Output

- Akteneinsichts- und Nachforderungsantrag.
- Verteidigungsmemo zur Rechtmäßigkeit der Maßnahme.
- Widerspruchs- und Verwertungsangriff für die Hauptverhandlung.
- Fragenkatalog für Polizeizeugen, Sachverständige und IT-Verantwortliche.
- Mandantenbrief in verständlicher Sprache.
- Revisionssicherungsnotiz.

## 3. `strafprozess-cockpit-taegliche-kanzleifuehrung`

**Fokus:** Tägliches Strafprozess-Cockpit für Verteidiger: bearbeitet Verfahrensstand, Fristen, Haftlage, Akteneinsicht, offene Anträge, Mandantenkommunikation, Beweisfragen, Termine und nächste Schritte in einer laufend aktualisierbaren Verteidigungsübersicht.

# Strafprozess-Cockpit für die tägliche Verteidigung

## Zweck

Dieser Skill ist die Schaltzentrale einer Strafakte. Er soll verhindern, dass Fristen, Nachlieferungen, Haftfragen, Beweisanträge, Zusagen der Staatsanwaltschaft oder Mandantenaufträge in E-Mails und Notizen verschwinden.

## Einstieg

Frage nur:

1. Verfahrensstand: Ermittlungsverfahren, Zwischenverfahren, Hauptverfahren, Rechtsmittel, Vollstreckung?
2. Rolle: Verteidigung, Pflichtverteidigung, Zeugenbeistand, Nebenklage, Adhäsion?
3. Gibt es Haft, Durchsuchung, Beschlagnahme, Vermögensarrest oder Führerscheinentzug?
4. Welche Frist oder welcher Termin steht als Nächstes?
5. Liegt Akteneinsicht vollständig vor?

## Cockpit-Felder

```text
Strafprozess-Cockpit

Mandant:
Az. Polizei/StA/Gericht:
Tatvorwurf:
Verfahrensstand:
Haft/Freiheit:
Pflichtverteidigung:
Nächster Termin:
Nächste Frist:
Akteneinsicht:
Offene Anträge:
Offene Beweise:
Mandantenauftrag:
Risikoampel:
Nächster Schritt:
```

## Ampellogik

- **Rot:** Haft, Rechtsmittelfrist, drohende Fristversäumung, HV morgen, unklare Zustellung, drohender Bewährungswiderruf, Durchsuchung/Arrest.
- **Gelb:** Akteneinsicht unvollständig, Nachlieferungen offen, Mandant nicht instruiert, Zeuge unklar, Beweisantrag nicht ausformuliert.
- **Grün:** Fristen notiert, Akte geordnet, Mandant instruiert, nächste Handlung terminiert.

## Täglicher Ablauf

1. Eingangspost scannen: Zustellung, Frist, Termin, Verfügung, Ladung, Beschluss.
2. Fristenbuch aktualisieren: Rechtsmittel, Wiedereinsetzung, Stellungnahmen, Haft, HV.
3. Aktenlog aktualisieren: neue Blätter, neue Sonderbände, digitale Beweise, Asservate.
4. Mandantenlog aktualisieren: letzte Information, offene Rückmeldung, Besuch/Telefonat.
5. Antragslog prüfen: gestellt, beschieden, wiederholen, zurücknehmen, ergänzen.
6. Tagesentscheidung treffen: heute handeln, diese Woche vorbereiten, beobachten.

## Output

Immer liefern:

- `Kurzstatus Akte`
- `Fristen/Wiedervorlagen`
- `Offene Entscheidungen`
- `Nächster anwaltlicher Schritt`
- `Mandanteninfo in 5 Sätzen`

## Quellenregel

StPO-Normen, Fristen und Formanforderungen live prüfen, wenn sie das Ergebnis tragen. Keine Rechtsprechung ohne Gericht, Datum, Aktenzeichen und frei prüfbare Quelle.

## 4. `strafprozess-haft-und-besuchsmanagement`

**Fokus:** Haft- und Besuchsmanagement für Untersuchungshaft: organisiert Haftbefehl, Haftprüfung, Haftbeschwerde, Akteneinsicht, Besuch, Telefon, Post, Familie, Arbeitgeber, Haftverschonungsplan und Beschleunigungskontrolle.

# Haft- und Besuchsmanagement

## Zweck

U-Haft ist Verteidigung unter Zeitdruck. Dieser Skill führt die praktische Seite: Kontakt zum Mandanten, Akteneinsicht, Haftbefehlprüfung, Entlassungsplan, Familie, Arbeitgeber, Fristen und Beschleunigung.

## Sofortliste

1. Haftbefehl vollständig erhalten?
2. Vorführtermin und Belehrung dokumentiert?
3. Verteidigerzugang und Besuchstermin gesichert?
4. Akteneinsicht nach § 147 StPO, insbesondere haftrelevante Informationen, beantragt?
5. Haftgrund: Flucht, Verdunkelung, Wiederholung oder besondere Konstellation?
6. Haftverschonungsplan nach § 116 StPO möglich?
7. Familie/Arbeitgeber/Wohnung nur nach Mandantenfreigabe informieren.

## Rechtsbehelfs- und Organisationsspur

- **Haftprüfung:** § 117 StPO jederzeit als gerichtliche Prüfung von Aufhebung oder Außervollzugsetzung des Haftbefehls.
- **Mündliche Verhandlung:** §§ 118, 118a StPO prüfen, wenn persönliches Gehör, Glaubhaftmachung oder Haftverschonungsplan mündlich besser wirken.
- **Haftbeschwerde:** als Beschwerde nach § 304 StPO einordnen; nicht mit dem Haftprüfungsantrag vermischen.
- **Haftverschonung:** § 116 StPO mit konkretem Sicherungspaket, nicht nur abstrakter Bitte.
- **Sechs-Monats-Kontrolle:** § 121 StPO früh als Wiedervorlage anlegen; Beschleunigungsgebot fortlaufend dokumentieren.
- **Akteneinsicht:** bei Haft § 147 Abs. 2 S. 2 StPO auf haftrelevante Informationen zuspitzen.

## Haftverschonungsplan

Prüfe:

- fester Wohnsitz,
- Arbeit/Ausbildung,
- Familie/Betreuungspflichten,
- Meldeauflagen,
- Kaution,
- Passabgabe,
- Kontaktverbote,
- Therapie/Beratung,
- elektronische Erreichbarkeit,
- Verzicht auf bestimmte Reisen.

## Besuchsnotiz

```text
Haftbesuch

Datum:
JVA:
Mandantenzustand:
Besprochene Punkte:
Aussageverhalten:
Haftverschonungsargumente:
Unterlagen benötigt:
Familienfreigabe:
Nächster Schritt:
```

## Output

- Haftstatus.
- Besuchsleitfaden.
- Haftprüfungs-/Haftbeschwerde-Skizze.
- Haftverschonungsplan.
- Familieninfo.
- Beschleunigungskontrolle.
- Wiedervorlagenliste: Besuch, Akteneinsicht, Haftprüfung/Beschwerde, sechs Monate, nächster Mandantenkontakt.

## 5. `strafprozess-hv-tagesmappe-und-sitzungsplan`

**Fokus:** Hauptverhandlungs-Tagesmappe: erstellt für jeden Sitzungstag Zeitplan, Zeugen- und Beweisprogramm, Einlassungsentscheidung, Fragelisten, Antragsentwürfe, Mandantenbriefing, Pausenstrategie, Protokollnotizen und Nachbereitungsaufgaben.

# Hauptverhandlungs-Tagesmappe und Sitzungsplan

## Zweck

Dieser Skill macht aus einer vorbereiteten Akte eine führbare Hauptverhandlung. Er denkt nicht nur an Rechtsfragen, sondern an den Sitzungstag: Wer kommt wann, was ist zu fragen, was muss beantragt, protokolliert und nachgearbeitet werden?

## Tagesmappe

```text
HV-Tagesmappe

Sitzungstag:
Gericht/Saal:
Beginn:
Besetzung:
Mandant:
Zeugen/Sachverständige:
Beweisthemen:
Anträge vorbereitet:
Dokumente mitbringen:
Mandantenbriefing:
Rote Linien:
Nachbereitung:
```

## Vor Sitzungsbeginn

- Mandant: Schweigen/Einlassung final klären.
- Anwesenheit und Pünktlichkeit sichern.
- Ausweis, Ladung, Vollmacht, Beiordnungsbeschluss, Aktenauszüge.
- Zeugenprogramm und Beweisthemen abgleichen.
- Verständigungs- oder Einstellungsgespräch nur sauber dokumentiert führen.
- Befangenheit/Verfahrenshindernisse vorab prüfen.

## Während der Beweisaufnahme

- Für jeden Zeugen: Beweisthema, erwartete Aussage, Widersprüche, Vorhalte, Risiken.
- Für Sachverständige: Anknüpfungstatsachen, Methodik, Alternativerklärungen, Ergänzungsfragen.
- Nach jeder relevanten Beweiserhebung: Erklärung nach § 257 StPO prüfen.
- Beweisanträge nicht aus dem Bauch stellen; Antragslog nutzen.

## Nach jedem Sitzungstag

- Ergebnisprotokoll erstellen.
- Neue Widersprüche und neue Anträge notieren.
- Mandant knapp informieren.
- Fristen/Termine aktualisieren.
- Revisionssicherung prüfen: Protokoll, Beanstandung, Beschluss, Ablehnung.

## Output

- `HV-Tagesmappe`
- `Zeugen-Frageliste`
- `Antragsmappe`
- `Mandantenbriefing`
- `Nachbereitungsnotiz`
