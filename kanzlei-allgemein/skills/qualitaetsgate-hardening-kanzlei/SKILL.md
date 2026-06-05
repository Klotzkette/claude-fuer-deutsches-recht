---
name: qualitaetsgate-hardening-kanzlei
description: "Qualitaetsgate Hardening Kanzlei: bündelt 2 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Qualitaetsgate Hardening Kanzlei

## Arbeitsbereich

Dieser Skill bündelt 2 sachlich verwandte Arbeitsschritte rund um **Qualitaetsgate Hardening Kanzlei** im Plugin Kanzlei-Allgemein. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `kanzlei-allgemein-qualitaetsgate-hardening` | Haertet Kanzlei-Outputs mit mehrstufigen Qualitaetsgates für Anfaenger und Profis. Anwendungsfall Schriftsatz Vertrag oder beA-Versand soll vor Abgang auf Substanz Vollständigkeit und Haftungsrisiken geprüft werden. Normen § 51 BRAO Haftung § 43a BRAO Berufspflichten § 130a ZPO formelle Anforderungen. Prüfraster Substanz Beweise Anlagen Fristen Zuständigkeit Anträge Vollmacht Datenschutz Zitate Versandweg Rechnung offene Risiken. Output Qualitaetsgate-Bericht mit Ampelstatus Maengelliste und Freigabeentscheidung. Abgrenzung zu versand-vor-check (unmittelbarer Pre-Check) und kanzlei-allgemein-schreibcanvas. |
| `kanzlei-allgemein-schreibcanvas` | Bietet ein freies Schreib-Canvas für Schriftsaetze Briefe Rechnungen beA-Nachrichten und Mandantenkommunikation. Anwendungsfall Anwalt will einen Entwurf strukturieren oder schwache Stellen in einem laufenden Text aufdecken lassen. Prüfraster Tatsachenvortrag Beweisangebote Anträge Normen Fristen Stilsicherheit juristischer Substanzcheck. Output Kommentierter Entwurf mit Verbesserungsvorschlaegen zu Tatsachen Beweisen Anträgen Normen naechsten Schritten. Abgrenzung zu kanzlei-allgemein-schriftsatz-turbo (Schnellerstellung) und kanzlei-allgemein-qualitaetsgate-hardening. |

## Arbeitsweg

Im Plugin Kanzlei-Allgemein gilt für **Qualitaetsgate Hardening Kanzlei**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `kanzlei-allgemein-qualitaetsgate-hardening`

**Fokus:** Haertet Kanzlei-Outputs mit mehrstufigen Qualitaetsgates für Anfaenger und Profis. Anwendungsfall Schriftsatz Vertrag oder beA-Versand soll vor Abgang auf Substanz Vollständigkeit und Haftungsrisiken geprüft werden. Normen § 51 BRAO Haftung § 43a BRAO Berufspflichten § 130a ZPO formelle Anforderungen. Prüfraster Substanz Beweise Anlagen Fristen Zuständigkeit Anträge Vollmacht Datenschutz Zitate Versandweg Rechnung offene Risiken. Output Qualitaetsgate-Bericht mit Ampelstatus Maengelliste und Freigabeentscheidung. Abgrenzung zu versand-vor-check (unmittelbarer Pre-Check) und kanzlei-allgemein-schreibcanvas.

# Qualitätsgate und Hardening


## Triage zu Beginn
1. Welches Produkttyp soll geprueft werden: Klage, Replik, Antrag, Vertrag, Mandantenbrief, Rechnung oder beA-Versand?
2. Soll der Schnellcheck (nur rote Risiken), Normal- oder Profi-Modus (Taktik, Gegner-Argument, Kosten) eingesetzt werden?
3. Gibt es eine laufende Frist, die den Pruefumfang begrenzt?
4. Soll das Qualitaetsgate-Protokoll als Aktenbestandteil gespeichert werden?

## Aktuelle Rechtsprechung
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zentrale Normen
- § 43 BRAO — Sorgfaltspflicht: Qualitaetssicherung als Grundpflicht vor jedem Ausgang
- § 130 ZPO — Inhalt von Schriftsaetzen: Antraege und Begruendung muessen vollstaendig sein
- § 253 Abs. 2 ZPO — Klageschrift: Vollstaendigkeitspflicht bei Antraegen und Tatsachen
- § 51 BRAO — Haftung bei erkennbar lueckenhaftem oder fehlerhaftem Schriftsatz

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Zweck

Dieser Skill ist die letzte und wiederholbare Prüfstation für Kanzlei-Outputs. Er soll Anfänger auffangen und Profis nicht ausbremsen. Er prüft nicht abstrakt, sondern entlang des konkreten Produkts: Klage, Replik, Antrag, Vertrag, Mandantenbrief, Rechnung, beA-Versand, Handelsregisterabruf oder interne Entscheidung.

## Moduswahl

Zu Beginn anbieten:

1. `Schnellcheck`: nur rote Risiken und fehlende Pflichtpunkte.
2. `Normal`: Substanz, Beweise, Anlagen, Fristen, Versand.
3. `Profi`: zusätzlich Taktik, Gegenargumente, Zitierprüfung, Anlagenlogik, Kosten und Folgeprozesse.

## Allgemeine Gates

- Ziel und Adressat klar.
- Akte und Aktenzeichen korrekt.
- Sachverhalt mit Datum, Beteiligten und Quelle.
- Rechtliche Grundlage benannt.
- Antrag oder gewünschtes Ergebnis konkret.
- Beweis- und Glaubhaftmachungsmittel zugeordnet.
- Anlagen nummeriert und erwähnt.
- Fristen und Zustellung geprüft.
- Vollmacht, Signatur und Vertretung geprüft.
- Datenschutz und Mandatsgeheimnis geprüft.
- Kosten, Rechnung oder Zeitnarrativ vorgemerkt.
- Versandweg und Protokoll vorbereitet.
- Offene Risiken sichtbar.

## Stop-, Warn- und Durchlauf-Logik

Das Gate darf nicht alles gleich behandeln. Immer eine Einstufung ausgeben:

- `STOPP`: Ausgabe oder Versand wäre fachlich, fristlich, berufsrechtlich oder technisch gefährlich. Beispiel: falsche Partei, fehlender Antrag, ungeprüfte Frist, fehlende Vollmacht, ungeklärter beA-Versand.
- `WARNUNG`: Entwurf ist nutzbar, aber mit sichtbarem Risiko. Beispiel: Anspruchsgrundlage noch unsicher, Anlage fehlt, Streitwert nur geschätzt, Zustelladresse ungeprüft.
- `DURCHLAUF`: Output ist für den gewählten Arbeitsstand plausibel. Offene Punkte sind dokumentiert und nicht versandkritisch.

Für das Kommandocenter zusätzlich mappen:

- `STOPP` = Ampel `ROT`.
- `WARNUNG` = Ampel `GELB`.
- `DURCHLAUF` = Ampel `GRÜN`.

Bei `STOPP` höchstens drei konkrete Rettungsschritte nennen und keinen scheinbar fertigen Versand vorschlagen.

## Produktspezifische Pflichtgates

### Klage, Replik, Antrag

- Antrag vollstreckungsfähig oder bewusst als Entwurf markiert.
- Zuständigkeit, Frist und Streitwert geprüft.
- Rubrum mit Partei, Rechtsform, Vertreter und Anschrift geprüft.
- Anspruchsgrundlage, Tatsachen, Subsumtion und Beweise getrennt.
- Darlegungs- und Beweislast geprüft.
- Anlagen im Text erwähnt und im Anlagenverzeichnis geführt.
- Bei Replik: jeder erhebliche Gegenvortrag einzeln beantwortet.
- beA-Dateien, Signatur, Vollmacht und Versandprotokoll geprüft.

### Vertrag

- Parteien und Vertretung gegen Handelsregister oder Aktenquelle geprüft.
- Leistung, Gegenleistung, Fälligkeit und Laufzeit konkret.
- Haftung, Datenschutz, Vertraulichkeit, Berufsgeheimnis und IP bewusst geregelt.
- Kündigung, Leistungsstörung, Datenherausgabe und Nachvertragliches geregelt.
- Anlagen und Rangfolge der Vertragsdokumente festgelegt.
- Verhandlungspunkte und rote Linien sichtbar.

### Rechnung, E-Rechnung und Buchhaltung

- Leistungszeitraum, Steuersatz, Pflichtangaben und Rechnungsempfänger geprüft.
- GoBD-Änderungsprotokoll angelegt.
- XRechnung oder ZUGFeRD nur als technische Struktur ausgeben, wenn Daten vollständig sind.
- Zahlung, offener Posten und Konto-Matching vorbereitet.

## Anfänger-Auffangmodus

Wenn der Nutzer unsicher oder unsortiert arbeitet:

- Nicht bremsen.
- Erst eine brauchbare Struktur erzeugen.
- Fehlendes als kleine Checkliste darstellen.
- Maximal drei nächste Schritte anbieten.
- Formulierungsbausteine statt langer Theorie liefern.

## Profi-Modus

Wenn der Entwurf bereits gut ist:

- Gegenargumente antizipieren.
- Darlegungs- und Beweislast prüfen.
- Antragsfassung zuspitzen.
- Anlagenreihenfolge und Querverweise prüfen.
- Kosten- und Fristrisiken markieren.
- Stil verdichten.

## Ausgabeformat

Immer kurz und handlungsorientiert:

1. Status: `STOPP`, `WARNUNG` oder `DURCHLAUF`.
2. Die drei wichtigsten Befunde.
3. Nächste konkrete Schritte.
4. Offene Fragen, nur soweit nötig.
5. Verweis auf den passenden Folge-Skill.

## Ausgabe

`assets/templates/qualitaetsgate-checkliste.md` verwenden.

## 2. `kanzlei-allgemein-schreibcanvas`

**Fokus:** Bietet ein freies Schreib-Canvas für Schriftsaetze Briefe Rechnungen beA-Nachrichten und Mandantenkommunikation. Anwendungsfall Anwalt will einen Entwurf strukturieren oder schwache Stellen in einem laufenden Text aufdecken lassen. Prüfraster Tatsachenvortrag Beweisangebote Anträge Normen Fristen Stilsicherheit juristischer Substanzcheck. Output Kommentierter Entwurf mit Verbesserungsvorschlaegen zu Tatsachen Beweisen Anträgen Normen naechsten Schritten. Abgrenzung zu kanzlei-allgemein-schriftsatz-turbo (Schnellerstellung) und kanzlei-allgemein-qualitaetsgate-hardening.

# Schreib-Canvas


## Triage zu Beginn
1. Welcher Dokumenttyp soll im Canvas erstellt werden: Klage, Replik, Mandantenbrief, Notiz, beA-Nachricht?
2. Gibt es Tatsachenluecken oder fehlende Beweisangebote im bisherigen Entwurf?
3. Sollen Rechtsgrundlagen automatisch vorgeschlagen oder manuell eingefuegt werden?
4. Ist eine Frist einzuhalten, die den Schreibprozess zeitlich begrenzt?

## Aktuelle Rechtsprechung
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zentrale Normen
- § 130 ZPO — Inhalt von Schriftsaetzen: Vollstaendigkeit von Antraegen und Tatsachen
- § 253 Abs. 2 Nr. 2 ZPO — Bestimmtheitsgrundsatz beim Klageantrag
- § 138 ZPO — Wahrheitspflicht und Erklaerungslast: Tatsachen muessen vollstaendig und wahrheitsgemass sein
- § 43 BRAO — Sorgfaltspflicht: Canvas-Pruefung als Teil anwaltlicher Dokumentenerstellung

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Zweck

Dieser Skill stellt ein Arbeitsbrett für Entwürfe bereit: links der Rohtext, rechts Hinweise, darunter offene Tatsachen, Beweise, Fristen, Anlagen, Versand- und Abrechnungspunkte. Das Canvas soll beim Schreiben helfen, ohne ständig zu stören.

## Canvas-Bereiche

- Rohtext.
- Verbesserter Vorschlag.
- Tatsachenlücken.
- Beweisangebote.
- Rechtsgrundlagen.
- Anträge und Tenor.
- Anlagen.
- Fristen.
- Versandweg.
- Zeitnarrativ.
- Rechnungs- oder Kostenfolge.

## Interventionen

Nur intervenieren, wenn:

- ein Text juristisch unsubstantiiert wirkt,
- ein Antrag fehlt,
- ein Beweisangebot fehlt,
- eine Frist oder ein EB berührt ist,
- beA-Versand naheliegt,
- eine Rechnung oder E-Rechnung naheliegt,
- die Sprache unprofessionell, zu scharf oder zu unklar ist,
- Anlagen erwähnt, aber nicht beigefügt sind.

## Hilfston

Formulierungen:

- `Ich glaube, hier fehlt noch der konkrete Tatsachenkern. Wollen wir Datum, Beteiligte und Beweisangebot ergänzen?`
- `Der Satz ist verständlich, aber für das Gericht noch zu abstrakt. Ich würde ihn so nachschärfen: ...`
- `Das ist schon verwendbar. Für den beA-Versand sollten wir noch Anlagen und Signatur prüfen.`
- `Aus diesem Arbeitsschritt kann ich ein Zeitnarrativ vorbereiten.`

## Arbeitsweise

1. Entwurf aufnehmen.
2. Textsorte erkennen.
3. Ziel und Adressat klären.
4. Substanzcheck durchführen.
5. Verbesserungsvorschlag danebenstellen.
6. Offene Punkte als kleine Aufgaben erfassen.
7. Nach Freigabe an Output, Fristen, Zeit oder Rechnung übergeben.
8. Bei Klage, Replik, Antrag oder gerichtlichem Schriftsatz an `kanzlei-allgemein-schriftsatz-turbo` übergeben.
9. Bei Vertrag, Termsheet oder Klauselwunsch an `kanzlei-allgemein-vertragsentwurf` übergeben.
10. Vor Ausgabe `kanzlei-allgemein-qualitaetsgate-hardening` nutzen.

## Ausgabe

`assets/templates/schreibcanvas.md` verwenden.
