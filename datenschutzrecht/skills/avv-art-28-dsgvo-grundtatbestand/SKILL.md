---
name: avv-art-28-dsgvo-grundtatbestand
description: "Grundtatbestand der Auftragsverarbeitung nach Art. 28 DSGVO. Klaert Rollenzuordnung Verantwortlicher gegen Auftragsverarbeiter wenn ein Dienstleister personenbezogene Daten im fremden Auftrag verarbeitet. Wann gilt Art. 28 wann Art. 26 wann Funktionsuebertragung. Output: Prüfvermerk zur Rollenzu..."
---

# Auftragsverarbeitung Art. 28 DSGVO – Grundtatbestand

## Zweck / Purpose

Strukturierte Prüfung, ob ein Vertragsverhaeltnis dem Grundtatbestand der Auftragsverarbeitung nach Art. 28 DSGVO unterfaellt und damit ein Auftragsverarbeitungsvertrag (AVV / Data Processing Agreement, DPA) abzuschliessen ist. Purpose (EN): Determine whether a contractual relationship triggers Art. 28 GDPR data processing on behalf of a controller and therefore requires a DPA.

## Wann dieses Modul hilft

- Mandant bezieht einen IT-/Cloud-/SaaS-Dienst und ist unsicher, ob AVV erforderlich ist.
- Mandant ist Anbieter und prüft, ob er als Auftragsverarbeiter einzustufen ist.
- Es bestehen Zweifel, ob nicht stattdessen Art. 26 DSGVO (gemeinsame Verantwortlichkeit) oder eine eigenstaendige Verantwortlichkeit (Funktionsuebertragung, separate Verantwortliche) vorliegt.
- Eine Aufsichtsbehoerde fragt nach Rollenzuordnung im Verarbeitungsverzeichnis (Art. 30 DSGVO).

## Rechtlicher Rahmen

- Art. 4 Nr. 7 DSGVO: Verantwortlicher entscheidet über Zwecke und Mittel.
- Art. 4 Nr. 8 DSGVO: Auftragsverarbeiter verarbeitet im Auftrag des Verantwortlichen.
- Art. 28 Abs. 1 DSGVO: Auswahl nur solcher Auftragsverarbeiter, die hinreichende Garantien bieten.
- Art. 28 Abs. 3 DSGVO: AVV in Schriftform oder elektronisch; Mindestinhalte lit. a bis h.
- Art. 28 Abs. 10 DSGVO: Eigenstaendige Verantwortlichkeit des Auftragsverarbeiters bei Ueberschreiten der Weisungen.
- Art. 29 DSGVO: Weisungsgebundenheit der Verarbeitung.
- § 62 BDSG: Spezialnormen für öffentliche Stellen.
- EDSA-Leitlinien 07/2020 zur Abgrenzung Verantwortlicher / Auftragsverarbeiter (angenommen 07.07.2021).

## Ablauf / Checkliste

1. **Sachverhalt erfassen.**
 - Welche personenbezogenen Daten werden verarbeitet?
 - Welcher Akteur entscheidet über Zweck (Wozu?) und Mittel (Wie?)?
 - Gibt es Weisungsmoeglichkeiten und Weisungsrechte?
 - Welchen wirtschaftlichen Vorteil zieht jeder Akteur aus der Verarbeitung?

2. **Drei-Stufen-Test für Rollenzuordnung.**

 | Frage | Indiz für Auftragsverarbeitung | Indiz gegen Auftragsverarbeitung |
 |---|---|---|
 | Wer legt Zweck fest? | Verantwortlicher allein | Dienstleister mitbestimmend |
 | Wer legt wesentliche Mittel fest? | Verantwortlicher | Dienstleister bestimmt Architektur und Datenlogik |
 | Eigene Datennutzung des Dienstleisters? | Nein, nur weisungsgebunden | Ja, für eigene Zwecke (Werbung, KI-Training, Statistik) |
 | Wirtschaftliches Interesse | Verantwortlicher | Dienstleister hat eigenes Interesse an Daten |
 | Berufsbild | Reiner Auftragnehmer | Eigene Rechtsdienstleistung, Berufstraegerstellung |

3. **Negativabgrenzung.**
 - **Funktionsuebertragung:** Bei Berufsgeheimnistraegern (Steuerberater, Rechtsanwaelte, Aerzte), Inkassodienstleistern und Wirtschaftspruefern ist die Rollenzuordnung wegen § 203 StGB und § 43a Abs. 2 BRAO besonders kritisch (Querverweis: funktionsuebertragung-vs-auftragsverarbeitung).
 - **Gemeinsame Verantwortlichkeit (Art. 26 DSGVO):** Wenn beide Akteure gemeinsam über Zwecke und Mittel entscheiden – EuGH C-210/16 Wirtschaftsakademie, EuGH C-40/17 Fashion ID, EuGH C-25/17 Zeugen Jehovas.
 - **Getrennte Verantwortlichkeit:** Wenn jeder Akteur dieselben Daten für eigene Zwecke mit eigener Rechtsgrundlage verarbeitet.

4. **Rechtsfolge feststellen.**
 - Auftragsverarbeitung bejaht: AVV-Pflicht nach Art. 28 Abs. 3 DSGVO.
 - Keine Verarbeitung im Auftrag, sondern Art. 26 DSGVO: Joint-Controller-Vereinbarung (Querverweis: avv-art-26-joint-controllership-deutsch).
 - Funktionsuebertragung: Eigener Vertragstyp, ggf. Datenuebermittlungsklausel und Geheimhaltungsvereinbarung statt AVV.

5. **Dokumentation.**
 - Im Verarbeitungsverzeichnis Art. 30 DSGVO: Rolle eintragen.
 - AVV als Anlage zum Hauptvertrag oder eigenstaendig.

## Mustertext / Template

Praeambel-Klausel für einen AVV nach Art. 28 DSGVO:

> "Der Auftraggeber (im Folgenden 'Verantwortlicher' im Sinne des Art. 4 Nr. 7 DSGVO) beauftragt den Auftragnehmer (im Folgenden 'Auftragsverarbeiter' im Sinne des Art. 4 Nr. 8 DSGVO) mit der Verarbeitung personenbezogener Daten im Auftrag und nach Weisung des Verantwortlichen. Gegenstand, Dauer, Art und Zweck der Verarbeitung, die Art der personenbezogenen Daten sowie die Kategorien betroffener Personen sind in Anlage 1 abschliessend beschrieben. Der Auftragsverarbeiter verarbeitet die personenbezogenen Daten ausschließlich auf dokumentierte Weisung des Verantwortlichen, soweit nicht eine Verarbeitungspflicht nach Unionsrecht oder dem Recht der Mitgliedstaaten besteht; in diesem Fall teilt der Auftragsverarbeiter dem Verantwortlichen diese rechtliche Verpflichtung vor der Verarbeitung mit, sofern das betreffende Recht eine solche Mitteilung nicht wegen eines wichtigen öffentlichen Interesses verbietet."

## Typische Drafting-Fehler

- AVV abgeschlossen, obwohl tatsaechlich Art. 26 DSGVO (gemeinsame Verantwortlichkeit) gegeben ist – falsche Rollenzuordnung wird durch AVV nicht geheilt.
- Pauschalverweis auf "Datenschutz" statt konkreter Mindestinhalte nach Art. 28 Abs. 3 lit. a bis h DSGVO.
- AVV mit Berufstraegern ohne Beruecksichtigung von § 203 StGB.
- Vermischung mit allgemeinen Geheimhaltungsklauseln; AVV-Pflichten sind eigenstaendig.
- AVV erst nach Verarbeitungsbeginn abgeschlossen (Art. 28 Abs. 9 DSGVO Form).

## Quellen Stand 06/2026

- DSGVO Art. 4 Nr. 7, Nr. 8, Art. 28, Art. 29.
- BDSG § 62.
- EDSA-Leitlinien 07/2020 zur Abgrenzung Verantwortlicher / Auftragsverarbeiter (Final 07.07.2021); abrufbar über edpb.europa.eu.
- EuGH C-25/17 (Zeugen Jehovas) – verifiziertes Aktenzeichen; Volltext über curia.europa.eu prüfen.
- EuGH C-210/16 (Wirtschaftsakademie / Fanpages) – Aktenzeichen verifiziert.
- EuGH C-40/17 (Fashion ID) – Aktenzeichen verifiziert.
- Verbindlich zur Zitierweise: `../../../references/zitierweise.md`.
- Kommentar-, Handbuch- und Aufsatzfundstellen nur, wenn der Mandant die Quelle bereitstellt oder ein lizenzierter Live-Zugriff sie verifiziert.

## Normen und Rechtsprechung

### Kuratierte Normen-Bibliothek

- Art. 5 DSGVO (Grundsätze der Verarbeitung)
- Art. 6, 9 DSGVO (Rechtsgrundlagen, besondere Datenkategorien)
- Art. 13, 14 DSGVO (Informationspflichten)
- Art. 15 DSGVO (Auskunftsrecht)
- Art. 28 DSGVO (Auftragsverarbeitung)
- Art. 32 DSGVO (Sicherheit der Verarbeitung)
- Art. 33, 34 DSGVO (Meldepflichten bei Verletzung)
- Art. 82 DSGVO (Schadensersatz)
- Art. 83 DSGVO (Bußgelder)
- §§ 4, 20, 41 BDSG (Aufsicht, Rechtsweg, Strafvorschriften)

### Leitentscheidungen

- EuGH C-300/21 (immaterieller Schaden Art. 82 DSGVO)
- EuGH C-634/21 (automatisierte Bonitätsbewertung Schufa)
- EuGH C-26/22 (Datenschutzbehörden-Befugnisse)
- EuGH C-807/21 (Bußgeldhaftung juristischer Personen)
- BVerfG 1 BvR 16/13 (Recht auf Vergessen I)

### Anwendung im Skill

- Rechtsgrundlage nach Art. 6 DSGVO sauber waehlen; berechtigte Interessen nach Art. 6 Abs. 1 lit. f DSGVO mit dokumentierter Abwaegung.
- Bei Datenpannen die 72-Stunden-Frist nach Art. 33 DSGVO einhalten; Risikoabwaegung Art. 34 DSGVO separat dokumentieren.
- Auskunftsanspruch Art. 15 DSGVO nicht mit Kopie nach Art. 15 Abs. 3 DSGVO verwechseln; EuGH C-307/22 Reichweite beachten.
