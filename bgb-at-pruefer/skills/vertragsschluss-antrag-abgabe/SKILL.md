---
name: vertragsschluss-antrag-abgabe
description: "Vertragsschluss Antrag Abgabe: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Vertragsschluss Antrag Abgabe

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Vertragsschluss Antrag Abgabe** im Plugin Bgb At Pruefer. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `vertragsschluss-antrag-annahme` | Klausurfall zum Vertragsschluss durch Antrag und Annahme nach §§ 145 bis 156 BGB: Bindungswirkung des Antrags, Erlöschungsgründe, Annahmefrist unter An- und Abwesenden, verspätete und abgeänderte Annahme sowie Zeitpunkt des Vertragsschlusses. Output: vollständiger Subsumtionspfad. |
| `abgabe-willenserklaerung` | Klausurfall zur Abgabe einer Willenserklärung nach §§ 116 ff. BGB: willentliche Entäußerung unter Anwesenden und Abwesenden, Botenproblematik, E-Mail und Plattform-Postfach, Widerruf vor Abgabe. Output: Gutachtenstil-Lösung mit Subsumtionsraster. |
| `invitatio-ad-offerendum-und-werbung` | Klausurfall zur Abgrenzung von Angebot und invitatio ad offerendum nach §§ 145 bis 147 BGB: Werbung im Schaufenster und Online-Shop als bloße Aufforderung zur Angebotsabgabe, verbindliche Preisauszeichnung, automatisierte Bestellbestätigung. Output: Subsumtionsraster und Gutachtenstil. |

## Arbeitsweg

Im Plugin Bgb At Pruefer gilt für **Vertragsschluss Antrag Abgabe**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `vertragsschluss-antrag-annahme`

**Fokus:** Klausurfall zum Vertragsschluss durch Antrag und Annahme nach §§ 145 bis 156 BGB: Bindungswirkung des Antrags, Erlöschungsgründe, Annahmefrist unter An- und Abwesenden, verspätete und abgeänderte Annahme sowie Zeitpunkt des Vertragsschlusses. Output: vollständiger Subsumtionspfad.

# Vertragsschluss — Antrag und Annahme §§ 145 bis 156 BGB

## Mandantenfall

- Angebot per Brief abgegeben — Käufer nimmt nach zwei Wochen an; Frist abgelaufen?
- Annahme mit Änderung des Preises — gilt dies als neues Angebot oder als (abgeänderte) Annahme?
- Klausurkonstellation: Anbieter stirbt nach Abgabe des Angebots, bevor der Empfänger annimmt.

## Erste Schritte

1. Antrag bestimmen: Vollständiges, auf Vertragsschluss gerichtetes Angebot mit Rechtsbindungswillen.
2. Bindungswirkung nach § 145 BGB: Antragende ist an das Angebot gebunden, solange Annahmefrist läuft.
3. Erlöschen des Antrags: § 146 BGB — Ablehnung oder nicht rechtzeitige Annahme.
4. Annahmefrist: § 147 BGB — unter Anwesenden sofort, unter Abwesenden angemessene Postlaufzeit.
5. Verspätete Annahme: § 149 BGB — gilt als neues Angebot; Antragender kann sofort annehmen.
6. Abgeänderte Annahme: § 150 Abs. 2 BGB — gilt als Ablehnung verbunden mit neuem Antrag.

## Rechtsrahmen

- § 145 BGB: Bindungswirkung des Antrags — Antragender ist grundsätzlich gebunden.
- § 146 BGB: Erlöschen des Antrags bei Ablehnung oder nicht rechtzeitiger Annahme.
- § 147 BGB: Annahmefrist — unter Anwesenden sofort, unter Abwesenden angemessene Zeit.
- § 149 BGB: Verspätete Annahme — gilt dem Antragenden gegenüber als neues Angebot.
- § 150 Abs. 2 BGB: Abgeänderte Annahme — gilt als Ablehnung und neues Angebot.

## Prüfraster

1. Antrag vollständig: Alle essentialia negotii enthalten und Rechtsbindungswille erkennbar?
2. Antrag zugegangen: § 130 BGB — Zeitpunkt des Zugangs beim Empfänger.
3. Annahmefrist nach § 147 BGB: Unter Anwesenden sofort, unter Abwesenden wie lange?
4. Annahme innerhalb der Frist zugegangen: Zeitpunkt dokumentiert?
5. Verspätete Annahme nach § 149 BGB: Antragender muss unverzüglich ablehnen, sonst gilt Vertrag?
6. Abgeänderte Annahme nach § 150 Abs. 2 BGB: Änderung wesentlich oder unwesentlich?
7. Tod oder Geschäftsunfähigkeit des Antragenden: § 130 Abs. 2 BGB — Antrag bleibt grundsätzlich wirksam.

## Typische Fallstricke

- Verspätete Annahme ist kein Vertragsschluss, sondern neues Angebot — Antragender muss annehmen.
- Abgeänderte Annahme, auch bei geringfügiger Änderung, gilt als Ablehnung und neues Angebot.
- § 130 Abs. 2 BGB: Tod des Antragenden nach Abgabe hindert Wirksamkeit nicht — häufig falsch gelöst.
- Kaufmännisches Bestätigungsschreiben kann Vertragsinhalt nachträglich modifizieren.

## Output

- Gutachtenstil-Abschnitt zum Vertragsschluss nach §§ 145 bis 156 BGB
- Zeitstrahl: Antrag-Abgabe → Antrag-Zugang → Annahme-Frist → Annahme-Zugang → Vertragsschluss
- Prüfampel: Vertrag geschlossen / Annahmefrist abgelaufen / abgeänderte Annahme als neues Angebot
- Klausurlösungsskizze mit verspäteter und abgeänderter Annahme

## Quellen

- [§ 145 BGB — gesetze-im-internet.de](https://www.gesetze-im-internet.de/bgb/__145.html)
- [§ 147 BGB — gesetze-im-internet.de](https://www.gesetze-im-internet.de/bgb/__147.html)
- [§ 150 BGB — gesetze-im-internet.de](https://www.gesetze-im-internet.de/bgb/__150.html)
- [dejure.org § 145 BGB](https://dejure.org/gesetze/BGB/145.html)
- [dejure.org § 150 BGB](https://dejure.org/gesetze/BGB/150.html)

## Vertiefung

### Annahmefrist-Berechnung

§ 147 Abs. 2 BGB: Die angemessene Frist umfasst Bearbeitungszeit für das Angebot, Postlaufzeit
hin und zurück sowie eine kurze Überlegungszeit. Bei Angeboten per E-Mail ist die Frist kürzer
als bei Briefangeboten, weil die Übermittlungszeit kürzer ist.

### Vertragsschluss im internationalen Handel

Bei grenzüberschreitenden Verträgen kann das UN-Kaufrecht (CISG) anwendbar sein, das eigene
Regeln für Angebot und Annahme enthält. Das CISG kennt kein Abstraktionsprinzip — wichtig für
den internationalen BGB-AT-Vergleich.

### Klausur-Checkliste Vertragsschluss

- Antrag vollständig mit allen essentialia negotii?
- Zugangszeitpunkt des Antrags nach § 130 BGB bestimmt?
- Annahmefrist nach § 147 BGB berechnet?
- Annahme innerhalb der Frist zugegangen?
- Verspätete Annahme (§ 149 BGB) oder abgeänderte Annahme (§ 150 Abs. 2 BGB) als neues Angebot?

## 2. `abgabe-willenserklaerung`

**Fokus:** Klausurfall zur Abgabe einer Willenserklärung nach §§ 116 ff. BGB: willentliche Entäußerung unter Anwesenden und Abwesenden, Botenproblematik, E-Mail und Plattform-Postfach, Widerruf vor Abgabe. Output: Gutachtenstil-Lösung mit Subsumtionsraster.

# Abgabe der Willenserklärung — Tatbestand und Zeitpunkt

## Mandantenfall

- Mandant verschickt eine Kündigung per E-Mail, zieht sie kurz danach zurück — war die Erklärung schon abgegeben?
- Arbeitgeber beauftragt einen Boten mit der Übermittlung eines Vertragsangebots; Bote verliert den Brief — Abgabe oder nicht?
- Klausurkonstellation: Online-Bestellung wird durch Autofill-Fehler abgesendet, bevor Nutzer bestätigt.

## Erste Schritte

1. Feststellen, ob eine empfangsbedürftige oder nicht empfangsbedürftige Willenserklärung vorliegt.
2. Willentliche Entäußerung: Hat der Erklärende die Erklärung bewusst in Richtung Empfänger auf den Weg gebracht?
3. Botenstellung bestimmen: Erklärungsbote (Risiko des Erklärenden), Empfangsbote (Risiko des Empfängers).
4. Bei elektronischer Übermittlung: Verlassen des Machtbereichs des Absenders prüfen (E-Mail-Server).
5. Widerruf vor Abgabe (§ 130 Abs. 1 S. 2 BGB analog) von Widerruf nach Zugang abgrenzen.
6. Ergebnis im Gutachtenstil: Norm — Tatbestandsmerkmal — Subsumtion — Rechtsfolge.

## Rechtsrahmen

- § 130 BGB: Zugang unter Abwesenden; Wirksamkeit der Willenserklärung ab Zugang.
- §§ 116 ff. BGB: Allgemeine Vorschriften zur Willenserklärung und ihren Mängeln.
- § 120 BGB: Haftung bei Übermittlungsfehlern durch Boten oder Übermittlungseinrichtung.
- § 164 BGB: Handeln im fremden Namen; abzugrenzen vom Boten ohne eigene Willenserklärung.
- § 242 BGB: Treu und Glauben — Empfänger kann sich nicht auf Nichtzugang berufen, wenn er ihn vereitelt hat.

## Prüfraster

1. Empfangsbedürftige oder formfreie, nicht empfangsbedürftige Willenserklärung?
2. Willentliche Entäußerung in Richtung des Empfängers bejaht oder verneint?
3. Boteneigenschaft: Erklärungsbote oder Empfangsbote — wer trägt das Übermittlungsrisiko?
4. Bei digitaler Übermittlung: Verlassen des Machtbereichs des Absenders (Outbox-Zeitstempel)?
5. Widerruf: Ist er dem Empfänger vor oder gleichzeitig mit der Erklärung zugegangen?
6. Abgabe bei Anwesenden: Akustisches Wahrnehmen nach eingeschränkter Vernehmungstheorie?
7. Rechtsfolge: Zeitpunkt der Abgabe bestimmt Beginn von Fristen und Bindungswirkung.

## Typische Fallstricke

- Abgabe und Zugang werden in Klausuren häufig vermengt; beide müssen separat geprüft werden.
- Boten-Fehler: Verlust durch Erklärungsboten trifft den Erklärenden, Verlust durch Empfangsboten trifft den Empfänger.
- Bei Autofill oder technischen Fehlern: Fehlendes Erklärungsbewusstsein kann Abgabe verhindern.
- Widerruf muss gleichzeitig oder früher zugehen, nicht nur gleichzeitig abgesendet werden.

## Output

- Gutachtenabschnitt zur Abgabe mit vollständiger Subsumtion
- Kurztriage mit Prüfampel: Abgabe bejaht / verneint / offen
- Rückfragenliste zu fehlenden Tatsachen (Zeitstempel, Botenweg, technisches Protokoll)
- Schriftsatzbaustein für streitigen Abgabezeitpunkt

## Quellen

- [§ 130 BGB — gesetze-im-internet.de](https://www.gesetze-im-internet.de/bgb/__130.html)
- [§ 116 BGB — gesetze-im-internet.de](https://www.gesetze-im-internet.de/bgb/__116.html)
- [§ 120 BGB — gesetze-im-internet.de](https://www.gesetze-im-internet.de/bgb/__120.html)
- [dejure.org § 130 BGB](https://dejure.org/gesetze/BGB/130.html)
- [dejure.org § 116 BGB](https://dejure.org/gesetze/BGB/116.html)

## Vertiefung

### Dogmatische Einordnung

Die Abgabe ist zeitlich und begrifflich vom Zugang (§ 130 BGB) zu trennen. Sie markiert den Zeitpunkt,
ab dem die Erklärung dem Erklärenden endgültig nicht mehr gehört. Für die Bindungswirkung des Antrags
(§ 145 BGB) kommt es auf die Abgabe, für die Wirksamkeit der Willenserklärung auf den Zugang an.

### Besonderheiten bei digitalen Erklärungen

Bei E-Mail-Kommunikation verlässt die Erklärung den Machtbereich des Absenders mit dem Absendevorgang
(Klick auf „Senden"). Die eingeschränkte Vernehmungstheorie, die der BGH für Erklärungen unter
Anwesenden anwendet, gilt hier nicht. Plattform-Nachrichten (z.B. Messenger-Dienste) gelten in der
Machtbereich-Lehre als vergleichbar mit E-Mail, solange der Absender keinen Rückholmechanismus hat.

### Klausur-Checkliste Abgabe

- Wurde die Erklärung willentlich nach außen gegeben?
- War der Weg zum Empfänger erkennbar und gewollt?
- Liegt ein Boten- oder Vertreter-Mittlerverhältnis vor?
- Bestand eine Kontrollmöglichkeit bis zum letzten Moment?
- Ist Widerruf noch möglich (gleichzeitig mit Zugang)?

## 3. `invitatio-ad-offerendum-und-werbung`

**Fokus:** Klausurfall zur Abgrenzung von Angebot und invitatio ad offerendum nach §§ 145 bis 147 BGB: Werbung im Schaufenster und Online-Shop als bloße Aufforderung zur Angebotsabgabe, verbindliche Preisauszeichnung, automatisierte Bestellbestätigung. Output: Subsumtionsraster und Gutachtenstil.

# Invitatio ad offerendum und Werbung — Angebot oder Aufforderung?

## Mandantenfall

- Online-Shop listet Artikel für 1 € statt 100 € — Preisfehler: Ist die Preisangabe ein verbindliches Angebot?
- Schaufensterwerbung mit Preisschild: Kunde fordert Verkauf zum angezeigten Preis — Angebot oder invitatio?
- Klausurkonstellation: Katalogversand eines Händlers enthält konkrete Mengen- und Preisangaben — Bindungswirkung?

## Erste Schritte

1. Willenserklärung des Werbenden prüfen: Enthält die Werbung alle wesentlichen Vertragsbestandteile (essentialia negotii)?
2. Rechtsbindungswille: Wollte der Erklärende sich verbindlich binden oder nur zur Angebotsabgabe auffordern?
3. Auslegung nach §§ 133 und 157 BGB: Empfängerhorizont eines objektiven Dritten anlegen.
4. Lagerbestand und Kapazitätsgrenzen: Kann ein Anbieter bei Massengeschäften an unbegrenzt viele Kunden gebunden sein?
5. Automatisierte Bestellbestätigung: Ist sie Annahme oder nur Eingangsbestätigung?
6. Rechtsfolge: Vertragsschluss oder Anfechtung wegen Irrtums (§ 119 Abs. 1 BGB) bei Preisfehler.

## Rechtsrahmen

- § 145 BGB: Antrag — Bindungswirkung für den Antragenden.
- § 147 BGB: Annahmefrist unter Anwesenden und Abwesenden.
- §§ 133 und 157 BGB: Auslegung von Willenserklärungen und Verträgen nach Treu und Glauben.
- § 119 Abs. 1 BGB: Irrtumsanfechtung wegen Inhalts- oder Erklärungsirrtum bei Preisfehler.
- § 122 BGB: Schadensersatzpflicht des Anfechtenden gegenüber dem gutgläubigen Empfänger.

## Prüfraster

1. Enthält die Werbung alle wesentlichen Vertragsbestandteile (Ware, Preis, Menge)?
2. Rechtsbindungswille nach objektivem Empfängerhorizont bejaht oder verneint?
3. Handelt es sich um ein Massengeschäft ohne feste Mengenbegrenzung (typisch invitatio)?
4. Automatisierte Bestellbestätigung: Rechtsfolge Annahme oder nur Zugangsbestätigung?
5. Bei Preisfehler: Voraussetzungen der Irrtumsanfechtung § 119 Abs. 1 BGB prüfen.
6. Schadensersatz aus § 122 BGB: positives oder negatives Interesse des Empfängers?
7. Sonderproblem Online-Auktionen: §§ 156 und 312 ff. BGB beachten.

## Typische Fallstricke

- Schaufensterwerbung ist in Deutschland grundsätzlich invitatio, nicht Angebot — häufiger Klausurfehler.
- Automatisierte Eingangsbestätigungen im Online-Handel sind keine Annahmeerklärung.
- Preisfehler-Anfechtung nach § 119 Abs. 1 BGB erfordert unverzügliche Erklärung (§ 121 BGB).
- § 122 BGB schützt den Empfänger: Anfechtender haftet auf das negative Interesse.

## Output

- Gutachtenstil-Abschnitt: invitatio oder Angebot mit vollständiger Subsumtion
- Prüfampel: Vertragsschluss wirksam / Anfechtung möglich / offen
- Rückfragenliste zu Mengenangaben, Automatisierungsgrad und Empfängerkenntnis
- Klausurlösungsskizze mit Folgeprüfung § 122 BGB

## Quellen

- [§ 145 BGB — gesetze-im-internet.de](https://www.gesetze-im-internet.de/bgb/__145.html)
- [§ 119 BGB — gesetze-im-internet.de](https://www.gesetze-im-internet.de/bgb/__119.html)
- [§ 122 BGB — gesetze-im-internet.de](https://www.gesetze-im-internet.de/bgb/__122.html)
- [dejure.org § 145 BGB](https://dejure.org/gesetze/BGB/145.html)
- [dejure.org § 157 BGB](https://dejure.org/gesetze/BGB/157.html)

## Vertiefung

### Wirtschaftliche Bedeutung der Abgrenzung

Die Abgrenzung von Angebot und invitatio ad offerendum hat erhebliche wirtschaftliche Konsequenzen:
Wäre jede Preisauszeichnung ein verbindliches Angebot, wäre der Einzelhändler an jeden Preis gebunden,
auch bei Schreibfehlern. Deshalb ist die Schaufensterwerbung in Deutschland grundsätzlich invitatio.

### Internet-Preisfehler in der Praxis

BGH-Rechtsprechung zu Preisfehlern im Internet: Das Einstellen eines Artikels im Online-Shop ist
in der Regel eine invitatio. Die Bestellung des Kunden ist das Angebot. Die Bestellbestätigung
kann Annahme sein — hier kommt es auf die konkrete Formulierung an.

### Klausur-Checkliste invitatio

- Alle essentialia negotii in der Werbung enthalten?
- Rechtsbindungswille nach objektivem Empfängerhorizont?
- Massengeschäft ohne Mengenbegrenzung typischerweise invitatio?
- Automatisierte Bestellbestätigung: Annahme oder nur Eingangsbestätigung?
- Preisfehler: Anfechtung nach § 119 Abs. 1 BGB — unverzüglich nach § 121 BGB?
