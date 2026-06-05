---
name: bericht-abfallnachweis-nachwv-api-zugang
description: "Bericht Abfallnachweis Nachwv API Zugang: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Bericht Abfallnachweis Nachwv API Zugang

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Bericht Abfallnachweis Nachwv API Zugang** im Plugin Berichtspflichten Erlediger. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `bericht-abfallnachweis-nachwv-krwg` | Abfallrechtliche Nachweise: gefährliche Abfälle, eANV, Register, Entsorgungsnachweise, Begleitscheine und Abfallbilanz. |
| `bericht-api-portal-zugang-rollen` | Behördenportale/API-Zugänge: ELSTER, IDEV, LUCID, ear, BAFA, DEHSt, Bundesbank, Rollen, Vertreter und Offboarding. |
| `bericht-arbeitsschutz-unterweisung-nachweise` | Unterweisung, Gefährdungsbeurteilung, Betriebsanweisung, Prüfnachweise und Behördenkontrolle. |

## Arbeitsweg

Im Plugin Berichtspflichten Erlediger gilt für **Bericht Abfallnachweis Nachwv API Zugang**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `bericht-abfallnachweis-nachwv-krwg`

**Fokus:** Abfallrechtliche Nachweise: gefährliche Abfälle, eANV, Register, Entsorgungsnachweise, Begleitscheine und Abfallbilanz.

# Abfallnachweis und Entsorgung

## Einsatz

Für Betriebe mit Bau-, Chemie-, Werkstatt- oder Produktionsabfällen.

## Norm- und Quellenanker

- KrWG §§ 49, 50 für Register- und Nachweispflichten; KrWG § 3 für Grundbegriffe und gefährliche Abfälle.
- NachwV für Entsorgungsnachweis, Sammelentsorgungsnachweis, Begleitschein, Übernahmeschein und elektronisches Nachweisverfahren.
- AVV für Abfallschlüssel und gefährliche Kennzeichnung; LAGA M 27 und Landesvollzug für praktische eANV-Fragen live prüfen.
- AbfVerbrG/Verordnung (EG) Nr. 1013/2006 gesondert prüfen, sobald Abfälle grenzüberschreitend verbracht werden.

## Arbeitsfragen

1. Welche Abfallschlüssel wurden vergeben, und warum passt der Schlüssel zu Herkunft, Zusammensetzung und Analyse?
2. Gefährlich, POP-haltig, mineralisch, Bauabfall, Chemieabfall, Elektroaltgerät oder Verpackung?
3. Wer ist Erzeuger, Besitzer, Beförderer, Sammler, Makler, Händler, Entsorger?
4. Welcher Nachweisweg: Entsorgungsnachweis, Sammelnachweis, Begleitschein, Übernahmeschein, Register?
5. Ist eANV erforderlich, sind Signaturen/Zugänge vorhanden, und stimmen Mengen mit Wiegescheinen/Rechnungen?

## Output

Abfallregister-Check mit AVV-Schlüssel, Gefährlichkeit, Beteiligtenrolle, Nachweisart, eANV-Status, Entsorgergenehmigung, Mengenabgleich und Aufbewahrung.

## Red Flags

- falscher AVV-Schlüssel
- Entsorgergenehmigung ungeprüft
- Begleitschein fehlt
- "Nicht gefährlich" behauptet, obwohl Analyse oder Herkunft das Gegenteil nahelegt
- Makler/Händler eingeschaltet, aber Verantwortlichkeit des Erzeugers wird fälschlich abgehakt
- Grenzüberschreitende Verbringung ohne Notifizierungsprüfung

## Arbeitsstil

Berichtspflichten werden wie kleine Verfahren behandelt: Rechtsgrundlage lesen, Pflichtenträger und Schwelle prüfen, Datenquelle sichern, nur erforderliche Daten melden, Vier-Augen-Freigabe dokumentieren, Versandnachweis ablegen.

## Qualitätsregel

Keine Rechtsprechung aus Modellwissen zitieren. Wenn eine Entscheidung gebraucht wird: Gericht, Entscheidungsform, Datum, Aktenzeichen und frei zugängliche Quelle verifizieren. Normen und Behördenportale vor Abgabe live prüfen.

## 2. `bericht-api-portal-zugang-rollen`

**Fokus:** Behördenportale/API-Zugänge: ELSTER, IDEV, LUCID, ear, BAFA, DEHSt, Bundesbank, Rollen, Vertreter und Offboarding.

# Portale, APIs und Rollen sicher verwalten

## Einsatz

Für Unternehmen mit vielen Meldeportalen.

## Norm- und Quellenanker

Fachportalregeln; DSGVO; IT-Sicherheit; Vollmachtsrecht.

## Arbeitsfragen

1. Welche Portale?
2. Wer hat Zugriff?
3. Welche Vertretung/Offboarding?

## Output

Portalzugangsregister und Rechteplan.

## Red Flags

- Ex-Mitarbeiteraccount aktiv
- 2FA fehlt
- private E-Mail

## Arbeitsstil

Berichtspflichten werden wie kleine Verfahren behandelt: Rechtsgrundlage lesen, Pflichtenträger und Schwelle prüfen, Datenquelle sichern, nur erforderliche Daten melden, Vier-Augen-Freigabe dokumentieren, Versandnachweis ablegen.

## Qualitätsregel

Keine Rechtsprechung aus Modellwissen zitieren. Wenn eine Entscheidung gebraucht wird: Gericht, Entscheidungsform, Datum, Aktenzeichen und frei zugängliche Quelle verifizieren. Normen und Behördenportale vor Abgabe live prüfen.

## 3. `bericht-arbeitsschutz-unterweisung-nachweise`

**Fokus:** Unterweisung, Gefährdungsbeurteilung, Betriebsanweisung, Prüfnachweise und Behördenkontrolle.

# Arbeitsschutz-Unterweisungen nachweisen

## Einsatz

Für Handwerk, Produktion und Büro mit Arbeitsschutzpflichten.

## Norm- und Quellenanker

- ArbSchG §§ 5, 6, 12 für Gefährdungsbeurteilung, Dokumentation und Unterweisung.
- BetrSichV für Arbeitsmittel, Prüfungen, befähigte Personen und Explosionsschutz, wenn Maschinen/Anlagen betroffen sind.
- GefStoffV für Gefahrstoffverzeichnis, Betriebsanweisung, Exposition und Unterweisung bei Chemikalien, Asbest, Lösemitteln, Reinigern.
- DGUV-Vorschriften/Regeln als Praxismaßstab; nicht als Gesetz zitieren, aber als konkretisierende Arbeitsschutzlogik nutzen.

## Arbeitsfragen

1. Welche Tätigkeit, welcher Arbeitsplatz, welche Personengruppe: Büro, Werkstatt, Baustelle, Lager, Minderjährige, Schwangere, Leiharbeit, Fremdfirmen?
2. Welche Gefährdungsbeurteilung liegt zugrunde, und wann wurde sie zuletzt aktualisiert?
3. Welche Unterweisung ist erforderlich: Erstunterweisung, jährliche Wiederholung, Anlassunterweisung nach Unfall/neuer Maschine/neuem Stoff?
4. Welche Betriebsanweisungen, Prüfprotokolle und Qualifikationsnachweise gehören dazu?
5. Wie werden digitale Unterweisungen, Verständnisfragen, Nachfragen und Nachunterweisungen dokumentiert?

## Output

Unterweisungs- und Nachweisordner mit Gefährdung, Rechtsgrundlage, Teilnehmerkreis, Inhalt, Sprache, Datum, Prüfer/Freigeber, Wiederholungsfrist und Unfall-/Behördenbezug.

## Red Flags

- Unterschriftenliste ohne Inhalt
- neue Mitarbeiter vergessen
- Prüffristen fehlen
- Unterweisung in deutscher Sprache, obwohl Beschäftigte sie nicht verstehen
- Fremdfirmen und Leiharbeitnehmer fallen durch das Raster
- Unfall passiert und die passende Gefährdungsbeurteilung ist nicht aktualisiert

## Arbeitsstil

Berichtspflichten werden wie kleine Verfahren behandelt: Rechtsgrundlage lesen, Pflichtenträger und Schwelle prüfen, Datenquelle sichern, nur erforderliche Daten melden, Vier-Augen-Freigabe dokumentieren, Versandnachweis ablegen.

## Qualitätsregel

Keine Rechtsprechung aus Modellwissen zitieren. Wenn eine Entscheidung gebraucht wird: Gericht, Entscheidungsform, Datum, Aktenzeichen und frei zugängliche Quelle verifizieren. Normen und Behördenportale vor Abgabe live prüfen.
