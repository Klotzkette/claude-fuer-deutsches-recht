---
name: erfuellungsaufwand-buerger-grundbegriff
description: "Erfuellungsaufwand Buerger Grundbegriff: bündelt 2 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Erfuellungsaufwand Buerger Grundbegriff

## Arbeitsbereich

Dieser Skill bündelt 2 sachlich verwandte Arbeitsschritte rund um **Erfuellungsaufwand Buerger Grundbegriff** im Plugin Normenkontrollrat (NKR). Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `nkr-erfuellungsaufwand-buerger-wirtschaft-verwaltung` | Trennt den Erfuellungsaufwand methodisch nach den drei Adressatengruppen Buerger Wirtschaft Verwaltung. Erklaert Spezifika je Gruppe Standard-Zeitwerte Lohnsaetze Bandbreiten und die typischen Falltypen. Mit Mustertabelle fuer die Stellungnahme und Bausteinen zur Plausibilisierung pro Gruppe. |
| `nkr-erfuellungsaufwand-grundbegriff` | Definiert den Grundbegriff Erfuellungsaufwand nach NKRG GGO § 44 und HdR. Trennt den Begriff von benachbarten Konzepten (Buerokratiekosten Vollzugskosten Haushaltskosten Folgekosten Sachkosten). Liefert die Standarddefinition wie sie in jeder NKR-Stellungnahme zugrunde gelegt wird sowie methodische Praezisierungen aus dem Leitfaden. |

## Arbeitsweg

Im Plugin Normenkontrollrat (NKR) gilt für **Erfuellungsaufwand Buerger Grundbegriff**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `nkr-erfuellungsaufwand-buerger-wirtschaft-verwaltung`

**Fokus:** Trennt den Erfuellungsaufwand methodisch nach den drei Adressatengruppen Buerger Wirtschaft Verwaltung. Erklaert Spezifika je Gruppe Standard-Zeitwerte Lohnsaetze Bandbreiten und die typischen Falltypen. Mit Mustertabelle fuer die Stellungnahme und Bausteinen zur Plausibilisierung pro Gruppe.

# NKR-Erfuellungsaufwand fuer Buerger, Wirtschaft und Verwaltung

## Worum geht es konkret

Der Erfuellungsaufwand wird methodisch **separat fuer drei Adressatengruppen** ausgewiesen. Das ist zwingend nach Leitfaden BMI/NKR und Standard in jeder NKR-Stellungnahme.

## Wann dieses Modul hilft / Kaltstart-Fragen

- Stellungnahme-Drafting: Tabellenstruktur
- Ressortentwurf zeigt nur Gesamtsumme
- Diskussion ueber Zuordnung (z.B. Selbstaendige zu Wirtschaft oder Buerger?)

Rueckfrage nur wenn unklar: *"Welche Adressatengruppe steht im Vordergrund — Buerger, Wirtschaft oder Verwaltung?"*

## Rechtlicher und methodischer Rahmen

- **§ 4 NKRG** — Pruefungsgegenstand
- **§ 44 Abs. 4, § 45 GGO** — getrennte Darstellung
- **Leitfaden zur Ermittlung und Darstellung des Erfuellungsaufwands** (BMI / NKR)
- **DESTATIS Zeitwerttabellen** als Datenbasis

## Pruefraster / Schritt fuer Schritt

### Buerger

- **Adressat**: natuerliche Personen in Privatangelegenheiten
- **Aufwand**: Zeitaufwand fuer Antraege, Anzeigen, Belege, Anhoerungen
- **Bewertung**: Zeitkosten (Stand 06/2026 als Bandbreite ca. 28 EUR/h gemaess Leitfaden — vom Anwender mit aktueller Tabelle zu pruefen)
- **Sachkosten**: nur wenn relevant (z.B. Gebuehren, ggf. Notar)
- **Falltypen**: Antrag stellen, Pflicht erfuellen, Anhoerung wahrnehmen
- **Bandbreiten**: stark adressatenabhaengig (Senioren, Migranten, mit/ohne digitale Affinitaet)

### Wirtschaft

- **Adressat**: Unternehmen aller Groessen
- **Aufwand**: Personalkosten plus Sachkosten plus externe Dienstleistungen
- **Bewertung**: branchenbezogene Lohnsaetze gemaess DESTATIS (z.B. ca. 40-50 EUR/h Verwaltung; 60-100 EUR/h hochqualifiziert — laufende Tabellen sind heranzuziehen)
- **Sachkosten**: IT, Material, Gutachten
- **Einmaliger Umstellungsaufwand** vs. laufender Aufwand getrennt
- **KMU-Differenzierung**: KMU ggf. extra ausweisen
- **Falltypen**: Berichtspflicht, Anzeige, Compliance-Prozess, IT-Anpassung, Schulung

### Verwaltung

- **Adressat**: Bund, Land, Kommunen
- **Aufwand**: Personal, IT, Sachmittel; ggf. Gerichte
- **Bewertung**: Vollkostenrechnung Bund / Land / Kommune (Personalkostentabellen BMF / DESTATIS)
- **Investitionen**: einmaliger Investitionsbedarf (z.B. Fachverfahren) separat ausweisen
- **Verteilungsfrage**: welche Ebene traegt? (Konnexitaet, Art. 104a GG)
- **Falltypen**: Antragsbearbeitung, Aufsicht, Sanktion, Beratung, IT-Betrieb

## NKR-Sicht — was triggert eine kritische Stellungnahme

- Gesamtsumme ohne Adressatentrennung
- Buerger-Aufwand "vernachlaessigbar" ohne Begruendung
- Wirtschaft-Aufwand ohne Lohnsatz-Begruendung
- Verwaltung-Aufwand auf "fuer die Verwaltung kostenneutral" gesetzt, obwohl Pflichten neu sind
- Konnexitaetsfrage nicht angesprochen (Pflicht fuer Kommunen)

## Trade-off-Matrix

| Adressat | Zeitwert (Beispiel-Bandbreite) | Hinweis |
|---|---|---|
| Buerger | ca. 28 EUR/h | mit aktueller Leitfaden-Tabelle pruefen |
| Wirtschaft Verwaltung | ca. 40-50 EUR/h | branchenabhaengig |
| Wirtschaft Spezialisten | ca. 60-100 EUR/h | je nach Qualifikation |
| Verwaltung Bund mittlerer Dienst | ca. 50-60 EUR/h | Vollkostenrechnung |
| Verwaltung Bund gehobener Dienst | ca. 65-80 EUR/h | Vollkostenrechnung |

Hinweis: Alle Werte sind Beispiel-Bandbreiten zur Orientierung; verbindlich ist die jeweils aktuelle Lohnkostentabelle des Leitfadens BMI/NKR und die DESTATIS-Personalkostentabelle.

## Mustertexte / Stellungnahme-Bausteine

Tabelle in der Stellungnahme:

| Adressat | einmalig | jaehrlich |
|---|---|---|
| Buerger | [X] Mio EUR | [Y] Mio EUR |
| Wirtschaft | [X] Mio EUR | [Y] Mio EUR |
| davon KMU | [X] Mio EUR | [Y] Mio EUR |
| Verwaltung Bund | [X] Mio EUR | [Y] Mio EUR |
| Verwaltung Laender | [X] Mio EUR | [Y] Mio EUR |
| Verwaltung Kommunen | [X] Mio EUR | [Y] Mio EUR |
| **Gesamt** | **[X] Mio EUR** | **[Y] Mio EUR** |

Bausteine:

- "Der Erfuellungsaufwand fuer Buerger entsteht hauptsaechlich durch [konkrete Pflicht]. Der NKR haelt die zugrundegelegten Fallzahlen fuer plausibel."
- "Der Erfuellungsaufwand fuer die Wirtschaft wird durch [konkrete Pflicht] verursacht. Davon entfallen auf KMU [Anteil]."
- "Der NKR weist darauf hin, dass der Erfuellungsaufwand fuer die kommunale Verwaltung in Hoehe von [X] Mio EUR die Frage der Konnexitaet aufwirft."

## Typische Fehler in Ressort-Entwuerfen

- Nur Gesamtsumme statt aufgeschluesselter Tabelle
- Verwaltung "kostenneutral" trotz neuer Pflichten
- KMU nicht ausgewiesen
- Konnexitaet ignoriert (Pflichten fuer Laender / Kommunen)
- Buerger pauschal "geringfuegig"

## Querverweise

- `nkr-erfuellungsaufwand-grundbegriff`
- `nkr-zeitwerttabelle-und-fallzahlen`
- `nkr-mittelstandsfreundlichkeit-kmu-test`
- `nkr-praktikabilitaet-vollzug-test`
- `legistik-werkstatt/folgenabschaetzung-erfuellungsaufwand`

## Quellen Stand 06/2026

- NKRG vom 14.08.2006 (BGBl. I S. 1866) § 4
- §§ 44 Abs. 4, 45 GGO
- Leitfaden zur Ermittlung und Darstellung des Erfuellungsaufwands (BMI / NKR) inkl. Zeitwerttabellen
- DESTATIS Verdienststrukturerhebung (jeweils aktuelle Ausgabe)
- NKR-Jahresbericht (jeweils aktuelle Ausgabe)
- Live verifizieren ueber [www.destatis.de](https://www.destatis.de) und [www.normenkontrollrat.bund.de](https://www.normenkontrollrat.bund.de)

## 2. `nkr-erfuellungsaufwand-grundbegriff`

**Fokus:** Definiert den Grundbegriff Erfuellungsaufwand nach NKRG GGO § 44 und HdR. Trennt den Begriff von benachbarten Konzepten (Buerokratiekosten Vollzugskosten Haushaltskosten Folgekosten Sachkosten). Liefert die Standarddefinition wie sie in jeder NKR-Stellungnahme zugrunde gelegt wird sowie methodische Praezisierungen aus dem Leitfaden.

# NKR-Erfuellungsaufwand — Grundbegriff

## Worum geht es konkret

Erfuellungsaufwand ist der **zentrale Pruefgegenstand des NKR**. Der Begriff ist gesetzlich verankert (NKRG, GGO) und methodisch im Leitfaden BMI/NKR konkretisiert. Dieser Skill liefert die Standarddefinition und die Abgrenzung zu anderen Kostenbegriffen.

## Wann dieses Modul hilft / Kaltstart-Fragen

- Anfaengerschulung
- Stellungnahme braucht den Grundbegriff im Aufschlag
- Ressort verwechselt Erfuellungsaufwand mit Buerokratiekosten
- Diskussion mit BMF / BRH ueber Abgrenzung

Keine Rueckfrage noetig.

## Rechtlicher und methodischer Rahmen

- **§ 4 NKRG** — Pruefungsgegenstand Erfuellungsaufwand
- **§ 44 GGO** — Gesetzesfolgenabschaetzung
- **§ 45 GGO** — Darstellung in der Begruendung
- **Leitfaden zur Ermittlung und Darstellung des Erfuellungsaufwands** (BMI / NKR)
- **HdR** Teil C

## Standarddefinition

**Erfuellungsaufwand** ist der gesamte messbare zeitliche **und** finanzielle Aufwand, der bei Buergerinnen und Buergern, der Wirtschaft sowie der oeffentlichen Verwaltung durch die **Befolgung** einer bundesrechtlichen Vorschrift entsteht.

Erfuellungsaufwand umfasst alle erforderlichen:

- Tatigkeiten zur Erfuellung einer Pflicht (Antraege, Anzeigen, Berichte, Bauten, Schulungen)
- Anschaffungen (Geraete, Software, Material)
- Dienstleistungen Dritter (Berater, Pruefer, Sachverstaendige)
- internen Prozesse (Schulung, Dokumentation, IT-Anpassung)

## Pruefraster / Schritt fuer Schritt

1. **Pflichtinhalt identifizieren** — welche konkrete Handlung wird angeordnet?
2. **Adressaten bestimmen** — Buerger / Wirtschaft / Verwaltung
3. **Aufwandskomponenten zerlegen**:
 - Zeit (Personalstunden)
 - Sachmittel (Material, IT)
 - Externe Dienstleistungen
4. **Einmalig vs. laufend** trennen
5. **Pro-Fall-Aufwand** ermitteln
6. **Fallzahl** ermitteln (jaehrlich)
7. **Aufwand pro Jahr** berechnen = Fallzahl × Pro-Fall-Aufwand
8. **Aggregation** ueber alle Adressatengruppen
9. **Plausibilisierung** (Vergleich mit Referenzwerten)

## Abgrenzung zu benachbarten Kostenbegriffen

| Begriff | Definition | Wer prueft? |
|---|---|---|
| Erfuellungsaufwand | Aufwand fuer Befolgung der Norm | NKR |
| Buerokratiekosten | Teilmenge: nur Informationspflichten | NKR (historisch) |
| Vollzugskosten | Verwaltungsaufwand bei Behoerden | NKR (Teil von Erfuellungsaufwand) |
| Haushaltskosten | Bundeshaushalt | BMF, BRH |
| Folgekosten | Wirtschaftliche Sekundaereffekte | Wissenschaft, BMF |
| Sachkosten | Anschaffungen | Teil von Erfuellungsaufwand |

## NKR-Sicht — was triggert eine kritische Stellungnahme

- Begriff wird vom Ressort eng (nur Buerokratiekosten) ausgelegt
- Sachmittel oder externe Dienstleistungen werden vergessen
- Schulungs- oder Anpassungsaufwand fehlt
- IT-Investitionen nicht erfasst

## Trade-off-Matrix

| Konstellation | Behandlung |
|---|---|
| Klare gesetzliche Pflicht | Erfuellungsaufwand 100% einrechnen |
| Faktische Pflicht (z.B. Befolgungsdruck) | dokumentieren, ggf. einrechnen |
| Freiwillige Inanspruchnahme | nicht einrechnen, aber transparent machen |
| Sekundaere Wirtschaftsfolgen | nicht Erfuellungsaufwand, ggf. eigener Abschnitt |

## Mustertexte / Stellungnahme-Bausteine

- "Der Erfuellungsaufwand bezeichnet gemaess Leitfaden BMI/NKR den gesamten messbaren Zeitaufwand und die Kosten, die durch Befolgung einer Vorschrift bei Buergern, Wirtschaft und Verwaltung entstehen."
- "Das Vorhaben verursacht nach NKR-Schaetzung einen jaehrlichen Erfuellungsaufwand fuer die Wirtschaft in Hoehe von [X] Mio EUR sowie einen einmaligen Umstellungsaufwand von [Y] Mio EUR."
- "Die Darstellung des Erfuellungsaufwands beschraenkt sich im Ressortentwurf auf Informationspflichten. Der NKR weist darauf hin, dass auch IT-Anpassungs- und Schulungskosten zum Erfuellungsaufwand gehoeren."

## Typische Fehler in Ressort-Entwuerfen

- Begriff "Buerokratiekosten" wird mit "Erfuellungsaufwand" gleichgesetzt
- Sachkosten werden vergessen
- Folgekosten werden eingerechnet, obwohl nicht Erfuellungsaufwand
- "Kein nennenswerter Aufwand" ohne Begruendung

## Querverweise

- `nkr-erfuellungsaufwand-buerger-wirtschaft-verwaltung`
- `nkr-buerokratiekosten-vs-erfuellungsaufwand`
- `nkr-standardkostenmodell-skm`
- `nkr-leitfaden-ermittlung-und-darstellung`
- `legistik-werkstatt/folgenabschaetzung-erfuellungsaufwand`

## Quellen Stand 06/2026

- NKRG vom 14.08.2006 (BGBl. I S. 1866) § 4
- §§ 44, 45 GGO
- Leitfaden zur Ermittlung und Darstellung des Erfuellungsaufwands (BMI / NKR)
- Handbuch der Rechtsfoermlichkeit Teil C
- Live verifizieren ueber [www.normenkontrollrat.bund.de](https://www.normenkontrollrat.bund.de) und [www.bmi.bund.de](https://www.bmi.bund.de)
