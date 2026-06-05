---
name: strafverfolgung-beweisbewertung-territorialer
description: "Strafverfolgung Beweisbewertung Territorialer: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Strafverfolgung Beweisbewertung Territorialer

## Arbeitsbereich

Dieser Skill bündelt 4 sachlich verwandte Arbeitsschritte rund um **Strafverfolgung Beweisbewertung Territorialer** im Plugin KI-VO / AI Act-Prüfer. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `strafverfolgung-beweisbewertung-ki-anhang-iii` | KI in Strafverfolgung und Beweisbewertung: Anhang III, Verdachtsgenerierung, Datenanalyse, Encro-/Messenger-Auswertung, Bild-/Audioanalyse, Beweisverwertungsrisiken, Akteneinsicht, Verteidigungsangriffe und Behörden-Governance. |
| `territorialer-anwendungsbereich-art-2` | Nicht-EU-Unternehmen oder Exporteur fragt: Gilt die KI-VO auch für uns obwohl wir außerhalb der EU sind? Art. 2 KI-VO territorialer Anwendungsbereich. Prüfraster: Inverkehrbringen in der EU Nutzung in der EU durch Betreiber Ausgaben die in der EU verwendet werden auch bei Betrieb außerhalb der EU Marktortprinzip. Drittstaaten-Konstellationen und extraterritoriale Wirkung. Output: Anwendbarkeits-Entscheidung mit Begründung. Abgrenzung zu sachlicher-ausschluss-art-2-abs-3-bis-12 (sachliche Ausnahmen) und persoenlicher-anwendungsbereich-rollen-art-3. |
| `training-generativer-modelle-tdm-opt-out` | Training generativer Modelle mit Text, Bild, Musik, Code und Datenbanken: Text-und-Data-Mining, Rechtevorbehalt/Opt-out, Webcrawl, Lizenzpool, Datenherkunft, Beweislast und Risikovermerk fuer Modellanbieter und Unternehmensnutzer. |
| `transparenz-deepfake-synthetic-content-art-50` | Art. 50 KI-VO fuer Chatbots, Deepfakes und synthetische Inhalte: Nutzerhinweis, Medien-/Kunst-/Satire-Ausnahmen, Wasserzeichen, interne Freigabe, Plattformkommunikation und Krisenreaktion bei falscher Kennzeichnung. |

## Arbeitsweg

Im Plugin KI-VO / AI Act-Prüfer gilt für **Strafverfolgung Beweisbewertung Territorialer**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `strafverfolgung-beweisbewertung-ki-anhang-iii`

**Fokus:** KI in Strafverfolgung und Beweisbewertung: Anhang III, Verdachtsgenerierung, Datenanalyse, Encro-/Messenger-Auswertung, Bild-/Audioanalyse, Beweisverwertungsrisiken, Akteneinsicht, Verteidigungsangriffe und Behörden-Governance.

# Strafverfolgung: KI und Beweisbewertung

## Ziel

Der Skill prüft, ob KI-Ergebnisse in Ermittlungsakten, Polizeivermerken oder Beweisanträgen belastbar sind und welche KI-VO- und Prozessrisiken entstehen.

## Normanker

- KI-VO Art. 3 Nr. 1 für die KI-System-Definition; Art. 6 Abs. 2 i. V. m. Anhang III für Hochrisiko-Einstufung.
- Anhang III Nr. 1, 6 und 8 KI-VO gesondert prüfen: Biometrie, Strafverfolgung, Justiz/Prozessentscheidung.
- KI-VO Art. 5 bei verbotenen Praktiken nur als Sperrprüfung, insbesondere biometrische Echtzeit-Fernidentifizierung und manipulative Systeme.
- KI-VO Art. 9 bis 15 für Hochrisiko-Pflichten: Risikomanagement, Datenqualität, technische Dokumentation, Logs, Transparenz, menschliche Aufsicht, Genauigkeit/Robustheit.
- StPO §§ 94 ff., 98, 100a ff., 147, 244, 261 je nach Beweismittel: Sicherstellung/Beschlagnahme, Telekommunikation, Akteneinsicht, Beweisantrag, freie Beweiswürdigung.
- DSGVO/JI-Richtlinie-Umsetzung, BDSG und Landespolizeirecht nur anhand der konkreten Behörde und Datenquelle prüfen.

## Prüfschritte

1. Welche KI-Funktion: Suche, Klassifikation, Übersetzung, Transkription, Gesichtserkennung, Risikoscore, Netzwerkgraph?
2. Wer nutzt sie: Polizei, Staatsanwaltschaft, Gericht, private Dienstleister?
3. Anhang-III-Bezug: Strafverfolgung, Biometrie, Justiz?
4. Datenherkunft: rechtmäßig erhoben, weiterverarbeitet, transformiert?
5. Nachvollziehbarkeit: Modellversion, Parameter, Fehlerrate, Logs?
6. Verteidigung: Akteneinsicht, Sachverständiger, Beweisantrag, Verwertungsverbot?
7. Zweckbestimmung: Wurde ein allgemeines Tool entgegen seiner Zweckbestimmung für Hochrisiko-Strafverfolgung genutzt?
8. Rollen: Anbieter, Betreiber, Importeur, Händler, Behörde und externer IT-Dienstleister nicht vermischen.
9. Aktenklarheit: Ist das KI-Ergebnis Primärbeweis, Ermittlungsanstoß, Übersetzungshilfe oder bloße Sortier-/Priorisierungshilfe?
10. Fair-Trial-Gate: Kann die Verteidigung Methode, Datenbasis, Fehlerquellen und menschliche Kontrollentscheidung tatsächlich angreifen?

## Output

- Behörden-Governance-Vermerk.
- Verteidigungsangriffsmatrix.
- Fragenkatalog für Akteneinsicht.
- Sachverständigenfragen.

## Qualitätsregel

KI-Auswertung ist nicht selbsterklärend. Wenn sie beweisrelevant wird, müssen Methode, Datenbasis und Fehlerquellen in die Akte.

## 2. `territorialer-anwendungsbereich-art-2`

**Fokus:** Nicht-EU-Unternehmen oder Exporteur fragt: Gilt die KI-VO auch für uns obwohl wir außerhalb der EU sind? Art. 2 KI-VO territorialer Anwendungsbereich. Prüfraster: Inverkehrbringen in der EU Nutzung in der EU durch Betreiber Ausgaben die in der EU verwendet werden auch bei Betrieb außerhalb der EU Marktortprinzip. Drittstaaten-Konstellationen und extraterritoriale Wirkung. Output: Anwendbarkeits-Entscheidung mit Begründung. Abgrenzung zu sachlicher-ausschluss-art-2-abs-3-bis-12 (sachliche Ausnahmen) und persoenlicher-anwendungsbereich-rollen-art-3.

# Territorialer Anwendungsbereich — Art. 2 KI-VO

## Zweck

Die KI-VO hat wie die DSGVO eine extraterritoriale Wirkung. Anbieter und Betreiber außerhalb der EU können trotzdem dem Geltungsbereich unterliegen. Dieser Skill klärt, ob die KI-VO auf den geschilderten Sachverhalt anwendbar ist.

## Drei Anknüpfungspunkte nach Art. 2 KI-VO

### Anknüpfungspunkt 1 — Inverkehrbringen oder Inbetriebnahme in der EU (Art. 2 Abs. 1 lit. a)

Die KI-VO gilt für Anbieter, die KI-Systeme oder GPAI-Modelle in der EU in Verkehr bringen oder in Betrieb nehmen, unabhängig davon, ob der Anbieter in der EU oder einem Drittland niedergelassen ist.

**Prüffragen:**
- Wird das System in der EU auf dem Markt angeboten?
- Wird das System erstmals in der EU bereitgestellt (Inverkehrbringen)?
- Wird das System in der EU für seinen Bestimmungszweck eingesetzt (Inbetriebnahme)?

**Ergebnis:** Wenn ja → KI-VO anwendbar.

### Anknüpfungspunkt 2 — Nutzung des Systems in der EU (Art. 2 Abs. 1 lit. b)

Die KI-VO gilt für Betreiber, die KI-Systeme in der EU verwenden, unabhängig vom Sitz des Betreibers.

**Prüffragen:**
- Wird das System von einer in der EU ansässigen Person oder Einrichtung genutzt?
- Werden Entscheidungen auf Basis des Systems in der EU getroffen?

**Ergebnis:** Wenn ja → KI-VO anwendbar für den Betreiber.

### Anknüpfungspunkt 3 — Ausgaben werden in der EU verwendet (Art. 2 Abs. 1 lit. c)

Die KI-VO gilt auch dann, wenn das KI-System außerhalb der EU betrieben wird, aber die Ausgaben (Vorhersagen, Empfehlungen, Entscheidungen) in der EU eingesetzt werden.

**Prüffragen:**
- Betrifft die Ausgabe des Systems Personen in der EU?
- Werden Empfehlungen oder Entscheidungen, die das System erzeugt, auf Personen in der EU angewendet?

**Ergebnis:** Wenn ja → KI-VO anwendbar.

## Drittstaaten-Konstellationen

### Szenario A — Anbieter in USA, Nutzer in Deutschland

Der US-Anbieter unterliegt der KI-VO, wenn er das System in der EU in Verkehr bringt (Art. 2 Abs. 1 lit. a) oder wenn Ausgaben in der EU verwendet werden (Art. 2 Abs. 1 lit. c). Er muss einen Bevollmächtigten in der EU benennen (Art. 22 KI-VO).

### Szenario B — Anbieter in Deutschland, System läuft auf Servern in der Schweiz

Maßgeblich ist nicht der Serverstandort, sondern das Inverkehrbringen. Wenn das System in der EU bereitgestellt wird, gilt die KI-VO.

### Szenario C — Nur Export in Drittstaaten, kein EU-Einsatz

Wenn weder das System in der EU in Verkehr gebracht wird noch Ausgaben in der EU verwendet werden, gilt die KI-VO nicht. Die Beweislast liegt beim Anbieter.

## Ausnahmen vom Anwendungsbereich (Überblick)

Art. 2 Abs. 3 bis 12 KI-VO enthält explizite Ausnahmen. Relevante Ausnahmen werden in `sachlicher-ausschluss-art-2-abs-3-bis-12` vertieft:
- Militärische und nationale Sicherheitszwecke (Abs. 3)
- Behörden von Drittstaaten und internationale Organisationen im Rahmen von Kooperationsabkommen (Abs. 4)
- Forschung und Entwicklung (Abs. 6) — mit Einschränkungen
- Rein persönliche, nicht berufliche Nutzung (Abs. 10)
- Open-Source (Abs. 12) — mit engen Voraussetzungen

## Ergebnis und Routing

- **Territorialer Anwendungsbereich gegeben:** weiter zu `persoenlicher-anwendungsbereich-rollen-art-3` und dann zu `rolle-anbieter-pruefen-art-3-nr-3` oder `rolle-betreiber-pruefen-art-3-nr-4`
- **Territorialer Anwendungsbereich fraglich (Drittstaaten):** Hinweis auf Klärungsbedarf; weiter mit Vorbehalt
- **Kein territorialer Anwendungsbereich:** KI-VO findet keine Anwendung; andere Rechtsordnungen können gelten

---

Hinweis: Keine Rechtsberatung. Mechanische Prüfung anhand vom Nutzer behaupteter Tatsachen. Die KI-VO ist in Auslegung und Konkretisierung dynamisch; Leitlinien der Kommission und Durchführungsrechtsakte sind laufend zu beobachten.

## Aktuelle Rechtsprechung (v14.2)
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zentrale Normen (Paragrafenkette)
- Art. 2 Abs. 1 KI-VO — Anwendungsbereich (EU-Marktplatzierung, EU-Inbetriebnahme, Betreiber in EU)
- Art. 2 Abs. 2 KI-VO — KI-Ausgaben in der EU auch bei Anbieter ausserhalb EU
- Art. 3 Nr. 3/4 KI-VO — Anbieter / Betreiber-Definitionen
- Art. 2 Abs. 3-12 KI-VO — Ausnahmen (Militaer, Forschung, Open Source)

## Triage zu Beginn
1. Ist das KI-System in der EU in Verkehr gebracht oder in Betrieb genommen?
2. Hat der Anbieter Sitz ausserhalb der EU — treffen Ausgaben trotzdem EU-Nutzer?
3. Handelt es sich um ein Hochrisiko-System eines EU-Betreibers (Art. 2 Abs. 1 lit. c)?
4. Liegt eine Ausnahme nach Art. 2 Abs. 3-12 vor (Militaer, Strafverfolgung, Forschung)?
5. Ist ein bevollmaechtigter Vertreter nach Art. 22 KI-VO erforderlich?

## Output-Template — Territorialer Anwendungsbereich
**Adressat:** Pruefer / Rechtsberater — Tonfall: entscheidungsbaum-strukturiert
```
TERRITORIALER ANWENDUNGSBEREICH ART. 2 KI-VO
[DATUM] — System: [SYSTEMNAME] — Anbieter-Sitz: [LAND]

Anwendungsbereich:
☑/☐ Art. 2 Abs. 1 lit. a: Anbieter bringt System in EU in Verkehr
☑/☐ Art. 2 Abs. 1 lit. b: System in Betrieb in EU
☑/☐ Art. 2 Abs. 1 lit. c: Betreiber in EU, Anbieter ausserhalb
☑/☐ Art. 2 Abs. 2: Ausgaben treffen EU-Nutzer

Ausnahme (Art. 2 Abs. 3-12):
☑/☐ Militaerischer Bereich
☑/☐ Ausschliesslich wissenschaftliche Forschung
☑/☐ Open Source (nicht kommerziell)
☑/☐ Sonstiges: [BESCHREIBUNG]

Ergebnis: [KI-VO ANWENDBAR / NICHT ANWENDBAR: Ausnahme Art. 2 Abs. X]
Naechster Schritt: [sachlicher-ausschluss-art-2 / persoenlicher-anwendungsbereich-rollen-art-3]
Geprueft: [NAME], [DATUM]
```

## 3. `training-generativer-modelle-tdm-opt-out`

**Fokus:** Training generativer Modelle mit Text, Bild, Musik, Code und Datenbanken: Text-und-Data-Mining, Rechtevorbehalt/Opt-out, Webcrawl, Lizenzpool, Datenherkunft, Beweislast und Risikovermerk fuer Modellanbieter und Unternehmensnutzer.

# Training generativer Modelle: TDM und Opt-out

## Einsatz

Dieses Fachmodul greift, wenn ein Modell mit fremden Werken, Datenbanken, Bildern, Musik, Code oder Texten trainiert wurde oder wenn ein Unternehmen ein Modell einkauft und die Trainingsdatenrisiken verstehen muss.

## Prüffragen

1. Welche Werkarten: Text, Bild, Musik, Video, Code, Datenbank, wissenschaftliche Publikation?
2. Welche Quelle: Lizenz, eigene Daten, Webcrawl, Kundenupload, Datensatz, öffentliches Archiv?
3. Ist Text- und Data-Mining einschlägig?
4. Gab es einen wirksamen Rechtevorbehalt/Opt-out?
5. Wurde der Opt-out technisch erkannt und respektiert?
6. Können Trainingsdaten oder geschützte Sequenzen im Output reproduziert werden?
7. Gibt es Datenbankherstellerrechte?

## Risikomatrix

| Risiko | Beispiel | Abhilfe |
|---|---|---|
| ungeklärte Lizenz | fremder Bilddatensatz | Datensatz sperren, Lizenz nachziehen |
| Opt-out | maschinenlesbarer Vorbehalt | Crawler-Regel und Sperrprotokoll |
| Memorization | Output kopiert Passagen | Filter, Red-Team, Logging |
| Datenbankrecht | massenhafter Datenbankauszug | Rechteprüfung, Mengenanalyse |

## Output

Erstelle ein Memo mit:

- Datenquellenkarte;
- TDM-/Opt-out-Bewertung;
- Risikostufen;
- Nachforderungsliste an Anbieter;
- Entscheidung: nutzen, nachverhandeln, sperren, ersetzen.

## 4. `transparenz-deepfake-synthetic-content-art-50`

**Fokus:** Art. 50 KI-VO fuer Chatbots, Deepfakes und synthetische Inhalte: Nutzerhinweis, Medien-/Kunst-/Satire-Ausnahmen, Wasserzeichen, interne Freigabe, Plattformkommunikation und Krisenreaktion bei falscher Kennzeichnung.

# Art. 50 KI-VO: Transparenz, Deepfakes, synthetische Inhalte

## Einsatzfälle

- Chatbot im Kundenservice.
- KI-generierte Bilder, Stimmen oder Videos.
- Avatare, Voice Cloning, Bewerbervideos.
- politische Kommunikation, Werbung, Presse, Kunst, Satire.
- automatisierte Textgenerierung für Öffentlichkeit.

## Prüffragen

1. Interagiert eine Person mit einem KI-System?
2. Wird synthetischer Inhalt erzeugt oder verändert?
3. Ist der Inhalt ein Deepfake oder nur KI-unterstützt?
4. Ist Kennzeichnung technisch möglich und zumutbar?
5. Gibt es Ausnahmen oder besondere journalistische/künstlerische Kontexte?
6. Welche Plattformregeln gelten zusätzlich?

## Output

- Kennzeichnungsentscheidung.
- Musterhinweise.
- Freigabeprozess für Marketing/PR.
- Incident-Plan bei falsch oder nicht gekennzeichnetem Material.

## Grundsatz

Kennzeichnung soll informieren, nicht stigmatisieren. Der Hinweis muss dort stehen, wo er für Betroffene wirklich wahrnehmbar ist.
