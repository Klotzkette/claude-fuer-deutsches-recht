---
name: ins-vorstandswechsel-dividenden
description: "Ins 029 Vorstandswechsel, Ins 030 Dividenden Nderung: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nächsten belastbaren Output."
---

# Ins 029 Vorstandswechsel, Ins 030 Dividenden Nderung

## Arbeitsbereich

Dieser Skill bündelt **Ins 029 Vorstandswechsel, Ins 030 Dividenden Nderung** zu einem konkreten Arbeitsgang. Starte mit dem Modul, das die Tatsachen der Akte trägt; weitere Module nur hinzunehmen, wenn sie dieselbe Frist, Zuständigkeit, Beweislast oder denselben Output betreffen.

## Arbeitsmodule

| Arbeitsmodul | Fokus |
| --- | --- |
| `ins-029-vorstandswechsel` | Prueft Insiderrecht bei Vorstandswechseln: Zeitpunkt der Insiderinformation, Ad-hoc-Pflicht, Abberufung vs. Ruecktritt und Vertraulichkeitspflichten. |
| `ins-030-dividenden-nderung` | Prueft Insiderinformations-Entstehung bei Dividendenaenderungen: Vorstandsvorschlag, AR-Billigung, Kapitalmarktkonsensus-Abweichung und Ad-hoc-Pflicht. |

## Arbeitsweg

Für **Ins 029 Vorstandswechsel, Ins 030 Dividenden Nderung** zuerst das Arbeitsmodul wählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Im Plugin `insiderrecht-compliance` bleiben Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschter Output getrennt; Module nur kombinieren, wenn dieselbe Akte mehrere dieser Punkte trägt. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Arbeitsmodule im Detail

## 1. `ins-029-vorstandswechsel`

**Fokus:** Prueft Insiderrecht bei Vorstandswechseln: Zeitpunkt der Insiderinformation, Ad-hoc-Pflicht, Abberufung vs. Ruecktritt und Vertraulichkeitspflichten.

# Vorstandswechsel – Insiderrecht und Ad-hoc-Pflicht

## Rechtlicher Rahmen

Ein Wechsel in der Unternehmensführung (CEO, CFO, andere Vorstandsmitglieder) ist typischerweise
eine kursrelevante Insiderinformation. Die Insiderinformation entsteht nicht erst mit dem
Beschluss des Aufsichtsrats, sondern kann bereits früher vorliegen (Geltl/Daimler-Test). Bei
Abberufung oder einvernehmlicher Aufhebung des Anstellungsvertrags ist besondere Sorgfalt geboten.

Rechtsgrundlagen:
- Art. 7, 17 MAR: https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32014R0596
- EuGH C-19/11 (Geltl/Daimler): https://curia.europa.eu/juris/document/document.jsf?docid=123755
- §§ 84, 93, 116 AktG: https://www.gesetze-im-internet.de/aktg/__84.html
- BaFin-Emittentenleitfaden: https://www.bafin.de/dok/8252648

## Ziel dieses Skills

Dieser Skill bestimmt den Entstehungszeitpunkt der Insiderinformation bei Vorstandswechseln,
prüft den Ad-hoc-Zeitpunkt und stellt Vertraulichkeit während der Entscheidungsphase sicher.

## Arbeitsprogramm

### Schritt 1 – Frühzeitige Insiderinformation bei Vorstandswechseln

- Geltl/Daimler-Test anwenden: Ab wann ist der Wechsel als hinreichend wahrscheinlich anzusehen?
- Typische Trigger für frühzeitige Insiderinformation:
 - AR-Präsidium hat Abberufungsentscheidung in principle getroffen
 - Einvernehmliche Aufhebungsverhandlungen sind fortgeschritten
 - Nachfolger ist identifiziert und hat Verhandlungen aufgenommen
- Dokumentiere frühestmöglichen Zeitpunkt

### Schritt 2 – AR-Beschluss als definierter Zeitpunkt

- Spätester Entstehungszeitpunkt der Insiderinformation: AR-Beschluss
- Ad-hoc-Pflicht: Unverzüglich nach AR-Beschluss
- Ausnahme: Wenn Nachfolge noch nicht geklärt und Vollständigkeit für die Ad-hoc fehlt
 (Zwischenmitteilung möglich, die nur Abgang meldet)

### Schritt 3 – Aufschub-Möglichkeiten

- Legitimes Interesse am Aufschub: In der Praxis selten, da Wechsel selbst
 keine laufenden Verhandlungen darstellt
- Ausnahme: Wenn Wechsel mit wesentlicher Strategie-Neuausrichtung verknüpft ist,
 kann Aufschub bis zur Vollständigkeit gerechtfertigt sein (restriktiv)
- Vertraulichkeit während AR-Beratung: Normal-Standard der AR-Verschwiegenheitspflicht
 (§ 116 AktG) reicht für die AR-Phase

### Schritt 4 – Inhalt der Ad-hoc-Mitteilung

- Name des ausscheidenden Vorstandsmitglieds, Funktion, Datum des Ausscheidens
- Wenn bekannt: Nachfolger, Datum des Antritts, kurze Kurzbiographie
- Ggf. Grund des Wechsels (wenn wesentlich)
- Wenn Nachfolge noch nicht geregelt: Interimsregelung nennen

### Schritt 5 – Eigengeschäfte und Directors' Dealings

- Ausscheidendes Vorstandsmitglied: Hat es Eigengeschäfte zwischen Beginn der
 Abberufungsverhandlungen und Ad-hoc getätigt? → Art. 14 MAR-Prüfung
- Neuer CEO: Directors'-Dealings-Registrierung ab Dienstantritt
- Abfindung: Meldepflichtige Transaktion nach Art. 19 MAR?

## Red-Team-Fragen

- Wurde der frühestmögliche Insiderinformationszeitpunkt dokumentiert?
- Wurden Eigengeschäfte des ausscheidenden Vorstandsmitglieds im kritischen Zeitraum geprüft?
- Ist die Ad-hoc vollständig (Name, Funktion, Datum, Nachfolge)?
- Wurden AR-Mitglieder auf Insiderstatus während der Beratungsphase hingewiesen?

## Ausgabeformat

Erzeuge:
1. Zeitstrahl Insiderinformations-Entstehung → AR-Beschluss → Ad-hoc
2. Ad-hoc-Entwurf Vorstandswechsel
3. Eigengeschäfts-Prüfprotokoll für ausscheidendes Vorstandsmitglied
4. AR-Verschwiegenheitsinstruktion für die Beratungsphase

Belege ausschließlich mit: eur-lex.europa.eu, curia.europa.eu, gesetze-im-internet.de,
bafin.de, bgh.de, dejure.org.

## 2. `ins-030-dividenden-nderung`

**Fokus:** Prueft Insiderinformations-Entstehung bei Dividendenaenderungen: Vorstandsvorschlag, AR-Billigung, Kapitalmarktkonsensus-Abweichung und Ad-hoc-Pflicht.

# Dividendenänderung – Insiderrecht und Ad-hoc-Pflicht

## Rechtlicher Rahmen

Eine signifikante Dividendenerhöhung oder -kürzung (oder Ausfall der Dividende) ist typischerweise
kursrelevant und kann eine Insiderinformation begründen. Die Insiderinformation entsteht nicht
erst mit dem HV-Beschluss, sondern kann bereits beim Vorstandsvorschlag oder AR-Billigung vorliegen.
Maßgeblich ist die Abweichung vom Analystenkonsensus.

Rechtsgrundlagen:
- Art. 7, 17 MAR: https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32014R0596
- §§ 58, 174 AktG: https://www.gesetze-im-internet.de/aktg/__58.html
- BaFin-Emittentenleitfaden: https://www.bafin.de/dok/8252648

## Ziel dieses Skills

Dieser Skill bestimmt den Entstehungszeitpunkt der Insiderinformation bei Dividendenänderungen
und stellt die rechtzeitige Ad-hoc-Veröffentlichung sicher.

## Arbeitsprogramm

### Schritt 1 – Kursrelevanz-Einschätzung

- Analyse des Analystenkonsensus: Welche Dividende erwartet der Markt?
- Abweichung von der eigenen bisherigen Dividendenpolitik
- Wesentlichkeitsschwelle: Keine feste Prozentregel; BaFin-Emittentenleitfaden nennt
 erhebliche Unterschreitung als Indikator
- Dividendenausfall: Stets kursrelevant, wenn bisher Dividende gezahlt wurde

### Schritt 2 – Entstehungszeitpunkt der Insiderinformation

- Vorstandsbeschluss zum Dividendenvorschlag: Typischer Zeitpunkt
- AR-Billigung des Vorschlags: Spätestens ab hier ist die Insiderinformation präzise
- Früherer Zeitpunkt möglich: Wenn bereits im Vorstand klar entschieden wurde und
 AR-Zustimmung praktisch sicher

### Schritt 3 – Aufschub-Prüfung

- Kein Standard-Aufschub für Dividendenankündigungen
- Möglicher Aufschub: Wenn Dividendenentscheidung mit wesentlicher Unternehmens-
 transaktion verknüpft ist (z. B. Sanierung, M&A)
- Praxis: Dividendenänderungen werden i.d.R. als Teil des Jahresabschluss-Termins
 koordiniert (Jahresabschluss-Saison)

### Schritt 4 – Koordination mit Jahresabschluss

- Wird der Jahresabschluss gleichzeitig veröffentlicht?
- Dann: Dividendeninfo als Teil der Jahresabschluss-Ad-hoc oder separater Announcement?
- Beachte: Wenn die Dividende erheblich von Konsensus abweicht und Jahresabschluss
 erst in 2 Wochen kommt: Separate Ad-hoc jetzt erforderlich

### Schritt 5 – Eigengeschäfte und Directors' Dealings

- PDMRs, die zwischen Vorstandsbeschluss und Ad-hoc Aktien kaufen (antizipierte
 Dividendenerhöhung) oder verkaufen (antizipierter -ausfall): Art. 14 MAR-Prüfung
- HV-Beschluss: Offizielle Bestätigung der Dividende, i.d.R. nicht mehr kursrelevant
 (bereits bekannt durch Ad-hoc)

## Red-Team-Fragen

- Wurde der Analystenkonsensus als Kursrelevanz-Benchmark herangezogen?
- Liegt ein früherer Entstehungszeitpunkt als AR-Billigung vor?
- Wurden Eigengeschäfte von PDMRs zwischen Beschluss und Ad-hoc geprüft?
- Wurde bei Dividendenausfall sofort veröffentlicht (nicht erst zum Jahresabschluss)?

## Ausgabeformat

Erzeuge:
1. Kursrelevanz-Analyse (Konsensus-Abweichung, Wesentlichkeitsbewertung)
2. Zeitstrahl Entstehung → Beschluss → Ad-hoc
3. Ad-hoc-Entwurf Dividendenänderung
4. PDMR-Eigengeschäfts-Check im kritischen Zeitraum

Belege ausschließlich mit: eur-lex.europa.eu, gesetze-im-internet.de, bafin.de, dejure.org.

## Weitere Hinweise

Bei Dividendenankündigungen von REIT-Strukturen oder dividend-orientierten Emittenten
(z. B. Infrastruktur-Gesellschaften) ist die Kursrelevanz besonders hoch, weil Anleger
primär wegen des Dividenden-Einkommens investieren. Jede Abweichung von der kommunizierten
Dividendenpolitik wird als wesentlicher Eingriff in die Anlagebasis gewertet. Compliance
muss in solchen Fällen eine noch niedrigere Wesentlichkeitsschwelle anwenden.

Weitere Quellen:
- Art. 7 MAR: https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32014R0596
- BaFin-Emittentenleitfaden: https://www.bafin.de/dok/8252648
