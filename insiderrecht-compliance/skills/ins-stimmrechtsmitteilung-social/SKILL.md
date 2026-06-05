---
name: ins-stimmrechtsmitteilung-social
description: "Ins 040 Stimmrechtsmitteilung, Ins 042 Social Media Leak: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nächsten belastbaren Output."
---

# Ins 040 Stimmrechtsmitteilung, Ins 042 Social Media Leak

## Arbeitsbereich

Dieser Skill bündelt **Ins 040 Stimmrechtsmitteilung, Ins 042 Social Media Leak** zu einem konkreten Arbeitsgang. Starte mit dem Modul, das die Tatsachen der Akte trägt; weitere Module nur hinzunehmen, wenn sie dieselbe Frist, Zuständigkeit, Beweislast oder denselben Output betreffen.

## Arbeitsmodule

| Arbeitsmodul | Fokus |
| --- | --- |
| `ins-040-stimmrechtsmitteilung` | Koordiniert Stimmrechtsmitteilungen nach §§ 33 ff. WpHG mit MAR-Insiderrecht: Schwellenberechnungen, Meldefristen und Insider-Trading-Risiken bei Paketkauf. |
| `ins-042-social-media-leak` | Reagiert auf Social-Media-Leaks (Twitter/X, LinkedIn, Reddit): Kursrelevanz-Bewertung, Ad-hoc-Pflicht, Nichtoeffentlichkeit und forensische Dokumentation. |

## Arbeitsweg

Für **Ins 040 Stimmrechtsmitteilung, Ins 042 Social Media Leak** zuerst das Arbeitsmodul wählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Im Plugin `insiderrecht-compliance` bleiben Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschter Output getrennt; Module nur kombinieren, wenn dieselbe Akte mehrere dieser Punkte trägt. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Arbeitsmodule im Detail

## 1. `ins-040-stimmrechtsmitteilung`

**Fokus:** Koordiniert Stimmrechtsmitteilungen nach §§ 33 ff. WpHG mit MAR-Insiderrecht: Schwellenberechnungen, Meldefristen und Insider-Trading-Risiken bei Paketkauf.

# Stimmrechtsmitteilungen (§§ 33 ff. WpHG) und Insiderrecht

## Rechtlicher Rahmen

Stimmrechtsmitteilungen nach §§ 33 ff. WpHG (Umsetzung der Transparenzrichtlinie) sind zwar
keine MAR-Pflichten, aber in der Praxis eng mit dem Insiderrecht verzahnt: Der Paketkauf,
der eine Meldeschwelle auslöst, kann auf Basis von Insiderinformationen erfolgen (Art. 14 MAR-
Verstoß). Umgekehrt kann das Überschreiten einer Meldeschwelle selbst eine Insiderinformation
für den Emittenten darstellen (Art. 7 MAR).

Rechtsgrundlagen:
- §§ 33–47 WpHG: https://www.gesetze-im-internet.de/wphg/__33.html
- Art. 7, 14 MAR: https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32014R0596
- Transparenzrichtlinie (EU) 2013/50: https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32013L0050
- BaFin-Emittentenleitfaden: https://www.bafin.de/dok/8252648

## Ziel dieses Skills

Dieser Skill koordiniert Stimmrechtsmitteilungs-Pflichten mit MAR-Insiderrecht und stellt
sicher, dass Paketerwerbe und Meldungen rechtskonform ablaufen.

## Arbeitsprogramm

### Schritt 1 – Stimmrechtsmitteilungs-Pflichten (§§ 33 ff. WpHG)

- Meldeschwellen: 3 %, 5 %, 10 %, 15 %, 20 %, 25 %, 30 %, 50 %, 75 %
- Meldepflichtig: Aktionäre und Personen, denen Stimmrechte zugerechnet werden
- Frist: 4 Handelstage nach Erreichen, Überschreiten oder Unterschreiten einer Schwelle
- Inhalt: DVO (EU) 2015/761-konformes Formular

### Schritt 2 – MAR-Insiderrecht beim Paketkauf

- Hat der Käufer beim Erwerb des Aktienpakets Insiderinformationen genutzt?
- Insiderinformationen können sein: nicht-öffentliche Prognoseabweichungen, M&A-Pläne,
 regulatory actions – Informationen aus einer Due Diligence über den Emittenten
- Safe Harbour: Unternehmensinterne Entscheidung, strategische Beteiligung aufzubauen,
 stellt allein noch keine Insiderinformation über den Emittenten dar

### Schritt 3 – Stimmrechtsmitteilung als Insiderinformation

- Das Überschreiten einer Meldeschwelle durch einen Großaktionär kann für den Emittenten
 eine Insiderinformation sein (z. B. überraschende 10 %-Beteiligung eines Aktivisten)
- Emittent hat keine eigenständige Meldepflicht, aber ggf. Ad-hoc-Pflicht nach Art. 17 MAR
- Timing: Ad-hoc-Pflicht entsteht, wenn Emittent von der Beteiligung offiziell informiert wird

### Schritt 4 – Acting in Concert

- Koordinierter Erwerb mehrerer Aktionäre kann zur Zurechnung von Stimmrechten führen
- Gleichzeitig: Koordination auf Basis gemeinsamer Insiderinformationen = Art. 14 MAR-Risiko
- Abgrenzung: Legitime Abstimmung im Rahmen von HV-Aktivismus vs. unzulässiges Insider-Tipping

### Schritt 5 – Dokumentation und Meldefristen

- Alle Schwellenberechnungen mit Zeitstempel dokumentieren
- Meldung an BaFin und Emittent innerhalb von 4 Handelstagen (§ 40 WpHG)
- Veröffentlichung durch Emittent nach Eingang der Meldung
- Bei Fehler oder Nachmeldung: Korrekturmeldung mit Erklärung

## Red-Team-Fragen

- Hat der Käufer beim Paketkauf Insiderinformationen genutzt?
- Wurde die Stimmrechtsmitteilung fristgerecht und im korrekten Format eingereicht?
- Hat der Emittent die Beteiligung als Insiderinformation qualifiziert und ggf. eine
 Ad-hoc-Mitteilung veröffentlicht?
- Gibt es Hinweise auf Acting-in-Concert mit anderen Aktionären?

## Ausgabeformat

Erzeuge:
1. Stimmrechtsschwellen-Übersicht (Schwelle × Meldepflicht × Frist)
2. MAR-Insiderrecht-Check für Paketkäufer
3. Emittenten-Ad-hoc-Prüfprotokoll (bei überraschender Beteiligung)
4. Stimmrechtsmeldungs-Formular (DVO-konform)

Belege ausschließlich mit: eur-lex.europa.eu, gesetze-im-internet.de, bafin.de, dejure.org.

## 2. `ins-042-social-media-leak`

**Fokus:** Reagiert auf Social-Media-Leaks (Twitter/X, LinkedIn, Reddit): Kursrelevanz-Bewertung, Ad-hoc-Pflicht, Nichtoeffentlichkeit und forensische Dokumentation.

# Social-Media-Leak – Insiderrecht und Ad-hoc-Reaktion

## Rechtlicher Rahmen

Die Verbreitung von Insiderinformationen über Social Media (Twitter/X, LinkedIn, Reddit,
Telegram, WhatsApp-Gruppen) kann die Nichtöffentlichkeit der Information aufheben und die
Ad-hoc-Pflicht nach Art. 17 MAR aktivieren. Nicht jede Social-Media-Meldung hebt die
Nichtöffentlichkeit auf – Gerüchte, Spekulationen oder einzelne Tweets ohne substanzielle
Verbreitung genügen i.d.R. nicht. Die BaFin überwacht Social Media auf Marktmissbrauch.

Rechtsgrundlagen:
- Art. 7 MAR (Nichtöffentlichkeit): https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32014R0596
- Art. 17 Abs. 7 MAR (Leak): https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32014R0596
- BaFin-Emittentenleitfaden: https://www.bafin.de/dok/8252648

## Ziel dieses Skills

Dieser Skill bewertet Social-Media-Leaks auf ihre insiderrechtliche Relevanz und steuert
die Compliance-Reaktion einschließlich Ad-hoc-Entscheidung und forensischer Sicherung.

## Arbeitsprogramm

### Schritt 1 – Inhaltsanalyse des Leaks

- Welche Information wurde veröffentlicht?
- Ist die Information präzise und kursrelevant (Art. 7 MAR)?
- Stammt die Information von einer Person mit Insiderkenntnissen oder ist es Spekulation?
- Verbreitung: Wie viele Follower/Views hat der Post? Wurde er von Qualitätsjournalisten
 aufgegriffen?

### Schritt 2 – Nichtöffentlichkeits-Bewertung

- Nichtöffentlichkeit ist aufgehoben, wenn die Information einer breiten Öffentlichkeit
 zugänglich ist und von ihr zur Kenntnis genommen werden kann
- Ein einzelner Tweet ohne Verbreitung genügt nicht
- Aber: Wenn Mainstream-Medien berichten (Reuters, Bloomberg, FAZ): Öffentlichkeit hergestellt
- Grenzfall: Nischenforum, kleiner Telegram-Kanal → Compliance-Entscheidung mit Zeitstempel

### Schritt 3 – Ad-hoc-Entscheidung

- Ist die Nichtöffentlichkeit aufgehoben? → Ad-hoc-Pflicht prüfen
- Lief ein Aufschub? → Aufschub endet bei Vertraulichkeitsverlust (Art. 17 Abs. 7 MAR)
- Entscheidung dokumentieren: Mit welcher Begründung wurde veröffentlicht oder nicht veröffentlicht?

### Schritt 4 – Forensische Dokumentation

- Sofortige Sicherung des Social-Media-Beitrags (Screenshot, URL, Zeitstempel)
- Identifikation des Accounts (anonym? Mitarbeiter-Account?)
- Netzwerkanalyse: Wer hatte Zugang zur Insiderinformation?
- Insiderlisten-Abgleich: Wer kommt als Quelle des Leaks in Frage?

### Schritt 5 – BaFin und Strafanzeige

- Proaktive BaFin-Meldung (Marktüberwachung)
- Strafanzeige gegen unbekannte Person (§ 119 WpHG) erwägen
- Koordination mit IT-Forensik und externer Kanzlei

## Red-Team-Fragen

- Wurde die Nichtöffentlichkeits-Bewertung sorgfältig und zeitnah vorgenommen?
- Wurde die Entscheidung, nicht zu veröffentlichen (falls getroffen), dokumentiert?
- Wurden Beweise zeitnah gesichert (Social-Media-Beiträge verschwinden)?
- Ist der Leak intern untersucht worden?

## Ausgabeformat

Erzeuge:
1. Leak-Bewertungsbogen (Inhalt × Verbreitung × Nichtöffentlichkeit × Ad-hoc-Pflicht)
2. Ad-hoc-Entscheidungsprotokoll (mit Begründung)
3. Forensische Dokumentation (Screenshot-Vorlage mit Zeitstempel)
4. BaFin-Meldungsschreiben

Belege ausschließlich mit: eur-lex.europa.eu, bafin.de, gesetze-im-internet.de, dejure.org.

## Weitere Hinweise

Besondere Situation: Ein Mitarbeiter postet kursrelevante Informationen auf dem eigenen
LinkedIn-Profil. Hier greifen neben MAR auch das Arbeitsrecht (Nebenpflichten aus dem
Arbeitsvertrag, § 241 Abs. 2 BGB) und ggf. das Berufsrecht. Compliance sollte Social-Media-
Guidelines haben, die Mitarbeitern ausdrücklich verbieten, nicht-öffentliche
Unternehmensinformationen zu posten. Verstöße können arbeitsrechtliche Konsequenzen haben
(Abmahnung, Kündigung) und müssen mit der MAR-Compliance-Reaktion koordiniert werden.

Weitere Quellen:
- Art. 17 Abs. 7 MAR: https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32014R0596
- BaFin-Emittentenleitfaden: https://www.bafin.de/dok/8252648
