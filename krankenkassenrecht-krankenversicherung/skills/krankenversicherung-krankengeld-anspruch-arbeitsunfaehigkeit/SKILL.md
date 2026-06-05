---
name: krankenversicherung-krankengeld-anspruch-arbeitsunfaehigkeit
description: "Krankengeld Anspruch Arbeitsunfaehigkeit: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Krankengeld Anspruch Arbeitsunfaehigkeit

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Krankengeld Anspruch Arbeitsunfaehigkeit** im Plugin Krankenkassenrecht Krankenversicherung. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `kv-005-krankengeld-anspruch-arbeitsunfaehigkeit-blockfrist-nahtl` | Krankengeldanspruch nach § 44 SGB V: Arbeitsunfähigkeitsbescheinigung, Blockfrist 78 Wochen, Nahtlosigkeit, Lückenfälle und Weiterbewilligungsstrategien. |
| `kv-010-reha-vor-rente-zustaendigkeit-krankenkasse-rentenversiche` | Rehabilitation: Zuständigkeitsabgrenzung GKV (§ 40 SGB V) und Deutsche Rentenversicherung (§ 9 ff. SGB VI), Nahtlosigkeit, Zwang zur Reha. |
| `kv-021-kassenwahl-kuendigung-bindungsfrist-wahltarif` | Kassenwahlrecht nach § 175 SGB V: Bindungsfrist, Kündigung, Sonderkündigungsrecht, Wahltarife und Kostenbeteiligung. |

## Arbeitsweg

Im Plugin Krankenkassenrecht Krankenversicherung gilt für **Krankengeld Anspruch Arbeitsunfaehigkeit**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `kv-005-krankengeld-anspruch-arbeitsunfaehigkeit-blockfrist-nahtl`

**Fokus:** Krankengeldanspruch nach § 44 SGB V: Arbeitsunfähigkeitsbescheinigung, Blockfrist 78 Wochen, Nahtlosigkeit, Lückenfälle und Weiterbewilligungsstrategien.

# Krankengeld: Anspruch, Arbeitsunfähigkeit, Blockfrist, Nahtlosigkeit

## Skill-Zweck

Dieser Skill bearbeitet alle Fragen rund um den **Krankengeldanspruch**: Entstehung, Höhe, Dauer (Blockfrist), Nahtlosigkeitsproblematik und häufige Fristfallen bei der Arbeitsunfähigkeitsbescheinigung.

## Rechtlicher Rahmen

- **§ 44 SGB V** – Krankengeld: Anspruchsvoraussetzungen
- **§ 46 SGB V** – Entstehung des Krankengeldanspruchs (Attestpflicht, Lückenproblematik)
- **§ 47 SGB V** – Höhe des Krankengelds: 70 % des Regelentgelts, max. 90 % des Nettolohns
- **§ 48 SGB V** – Dauer des Krankengelds: 78 Wochen innerhalb von 3 Jahren (Blockfrist)
- **§ 49 SGB V** – Ruhen des Krankengelds (Entgeltfortzahlung, Verletztengeld, fehlende AU-Bescheinigung)
- **§ 51 SGB V** – Leistungsverweigerung bei verweigerter Reha-Mitwirkung
- **§ 192 Abs. 1 Nr. 2 SGB V** – Mitgliedschaftserhaltung durch Krankengeldanspruch
- BSG B 3 KR 4/14 R (Nahtlosigkeit, Attestpflicht), BSG B 3 KR 22/13 R (Blockfrist)

## Blockfrist und Nahtlosigkeit

| Begriff | Bedeutung |
|---------|-----------|
| Blockfrist | 78 Wochen Krankengeld wegen derselben Krankheit innerhalb von je 3 Jahren |
| Nahtlosigkeit | AU-Bescheinigung muss lückenlos ohne einen freien Tag vorliegen |
| Attestpflicht | AU-Attest spätestens am nächsten Werktag nach AU-Beginn (§ 46 Satz 1 Nr. 2 SGB V) |
| Rückwirkendes Attest | Schadet; AU muss prospektiv ausgestellt sein |

## Prüfprogramm

### Schritt 1 – Anspruchsbegründung
- Pflichtversichertes Mitglied? (§ 5 SGB V)
- Beschäftigung mit Anspruch auf Krankengeld? (nicht: freiwillig Versicherte mit Tarif ohne KG)
- AU ärztlich festgestellt? Attest zeitgerecht eingereicht?

### Schritt 2 – Entstehung des Anspruchs (§ 46 SGB V)
- Bei Beschäftigten: ab dem Tag nach ärztlicher Feststellung der AU (§ 46 Satz 1 Nr. 2)
- Lücke von nur einem Tag zwischen zwei AU-Perioden: Anspruch erlischt, Blockfrist beginnt erneut zu laufen – fatale Folge!
- Attestlücke durch Arzt vermeiden: Folgebescheinigung muss spätestens am letzten Tag der vorigen AU ausgestellt sein

### Schritt 3 – Höhe berechnen (§ 47 SGB V)
- Regelentgelt: Bruttoentgelt der letzten Abrechnungsperiode (4 Wochen oder Monat)
- Krankengeld = 70 % Regelentgelt, max. 90 % Nettoentgelt
- Einmalzahlungen anteilig berücksichtigen (BSG-Rechtsprechung)
- Beitragsbemessungsgrenze 2025: 5.512,50 €/Monat – KG-Maximum daraus rechnen

### Schritt 4 – Blockfrist (§ 48 SGB V)
- 78 Wochen wegen derselben Krankheit: 3-Jahres-Block (nicht rollierend, sondern fester Zeitraum)
- Dieselbe Krankheit: nicht identische Diagnose, sondern kausal-medizinisch gleiche Erkrankung (BSG)
- Nach Ablauf: keine weiteren Ansprüche; erst Gesundung + 6 Monate Beschäftigung → neuer Anspruch

### Schritt 5 – Ruhen prüfen (§ 49 SGB V)
- Entgeltfortzahlung des Arbeitgebers läuft → Krankengeld ruht
- Verletztengeld, Übergangsgeld, Mutterschaftsgeld: ebenfalls Ruhen
- Fehlende AU-Bescheinigung: Ruhen bis Vorlage

### Schritt 6 – Nahtlosigkeitssicherung
- Folgebescheinigung durch Arzt zum richtigen Zeitpunkt sicherstellen
- Wenn Arzt nicht erreichbar: Notfallpraxis, Krankenhaus; schriftlich dokumentieren
- Nachträgliche Attestierung: kann Lücke nicht heilen (BSG B 3 KR 4/14 R)

## Typische Fallen

- **Tag der ärztlichen Feststellung**: Der Tag selbst begründet noch keinen KG-Anspruch; erst der Folgetag.
- **Wochenendfalle**: AU läuft bis Freitag; nächste Bescheinigung erst Montag ausgestellt → Samstag/Sonntag Lücke → Anspruch erlischt.
- **Freiwillig Versicherte ohne KG-Tarif**: Haben gesetzlichen Mindestanspruch ab 7. Woche (§ 44 Abs. 2), davor nur tariflich.
- **Entgeltumwandlung in der Berechnung**: Betriebsrentenbeiträge vom Brutto abgezogen → Regelentgelt kleiner → KG kleiner (BSG).

## Output-Formate

- AU-Fristenkalender (Blockfrist-Endberechnung)
- Krankengeld-Berechnung (Arbeitsblatt)
- Widerspruch gegen Ablehnung/Einstellung
- Arzthinweis: Nahtlosigkeitspflicht
- Klageschrift SG bei erschöpfter Blockfrist und streitiger Kausalität

## Quellen

- [§ 44 SGB V](https://www.gesetze-im-internet.de/sgb_5/__44.html)
- [§ 46 SGB V](https://www.gesetze-im-internet.de/sgb_5/__46.html)
- [§ 48 SGB V](https://www.gesetze-im-internet.de/sgb_5/__48.html)
- [BSG B 3 KR 4/14 R – Nahtlosigkeit](https://www.bsg.bund.de/DE/Entscheidungen/entscheidungen_node.html)
- [dejure.org § 44 SGB V](https://dejure.org/gesetze/SGB_V/44.html)
- [GKV-Spitzenverband Krankengeld-Leitfaden](https://www.gkv-spitzenverband.de)

## 2. `kv-010-reha-vor-rente-zustaendigkeit-krankenkasse-rentenversiche`

**Fokus:** Rehabilitation: Zuständigkeitsabgrenzung GKV (§ 40 SGB V) und Deutsche Rentenversicherung (§ 9 ff. SGB VI), Nahtlosigkeit, Zwang zur Reha.

# Reha vor Rente: Zuständigkeit Krankenkasse vs. Rentenversicherung

## Skill-Zweck

Rehabilitation ist häufig Streitgegenstand: **Wer ist zuständig – Krankenkasse oder Rentenversicherung?** Dieser Skill klärt Zuständigkeitsabgrenzung, Nahtlosigkeit und die Folgen der falschen Antragstellung.

## Rechtlicher Rahmen

- **§ 40 SGB V** – Leistungen zur medizinischen Rehabilitation (GKV-Zuständigkeit)
- **§§ 9–31 SGB VI** – Leistungen zur Teilhabe (Rentenversicherung, med. + berufliche Reha)
- **§ 14 SGB IX** – Erstattungspflicht des erstangegangenen Trägers; Weiterleitung innerhalb 2 Wochen
- **§ 15 SGB IX** – Selbstbeschaffung bei Versagen des Trägers
- **§ 16 SGB VI** – „Reha vor Rente" (RvR): Versicherter muss Reha nicht ablehnen wenn Rentenversicherung fordert
- **§ 51 SGB V** – GKV kann Versicherte bei drohender Erwerbsminderung auf Reha-Antrag verweisen
- **SGB IX §§ 4, 6, 14, 15** – Leistungsrecht, Zuständigkeit, Erstattung
- BSG B 1 KR 10/20 R (Reha-Zuständigkeit GKV vs. RV)

## Zuständigkeitsmatrix

| Leistungstyp | Primär zuständig | Sekundär/Nachrang |
|--------------|-----------------|-------------------|
| Med. Reha ohne RV-Bezug | Krankenkasse § 40 SGB V | – |
| Med. Reha bei Erwerbsminderungsrisiko | Deutsche Rentenversicherung § 9 SGB VI | GKV subsidiär |
| Berufliche Rehabilitation | Deutsche Rentenversicherung, Bundesagentur | Krankenkasse nicht zuständig |
| Anschlussrehabilitation (AHB) | Rentenversicherung oder GKV je nach Zuweisung | Krankenhaus koordiniert |

## Prüfprogramm

### Schritt 1 – Zuständigkeit bestimmen
- Hat der Versicherte ausreichende Wartezeit bei Rentenversicherung (15 Jahre) für § 9 SGB VI?
- Besteht Erwerbsminderungsrisiko? (droht Erwerbsminderungsrente)
- Wenn ja: Rentenversicherung primär zuständig → Antrag dort stellen

### Schritt 2 – § 14 SGB IX: Erstangegangener Träger
- Antrag bei falscher Stelle eingereicht: Träger muss innerhalb 2 Wochen weiterleiten
- Wenn Weiterleitung versäumt: Erstangegangener Träger haftet und muss leisten
- Wichtig: Versicherter stellt Antrag bei GKV, obwohl RV zuständig → GKV muss leisten und holt sich Geld von RV zurück

### Schritt 3 – § 51 SGB V: GKV-Reha-Verweis
- GKV kann verlangen, dass Versicherter Reha-Antrag bei RV stellt wenn Krankengeld-Anspruch erschöpft droht
- Verweigert Versicherter: GKV kann Krankengeld einstellen
- Reha-Antrag gilt als Rentenantrag! (§ 51 Abs. 3 SGB V) – darauf hinweisen

### Schritt 4 – Selbstbeschaffung § 15 SGB IX
- Träger verweigert oder verzögert Leistung rechtswidrig → Versicherter kann selbst beschaffen
- Voraussetzung: Anspruch besteht, Versagen des Trägers, notfallmäßige Beschaffung
- Erstattung: volle Kosten der gleichwertigen Leistung

### Schritt 5 – Nahtlosigkeit Krankengeld-Reha
- Übergang Krankengeld → Übergangsgeld (Reha) muss nahtlos sein
- Übergangsgeld: 68 % / 75 % des Regelentgelts (§ 20 SGB VI)
- Rentenversicherung muss Beginn der Reha-Leistung zeitnah koordinieren

## Typische Fallen

- **Reha-Antrag = Rentenantrag**: § 51 Abs. 3 SGB V; Versicherte werden oft nicht aufgeklärt.
- **Anschlussrehabilitation verpasst**: AHB muss im Krankenhaus beantragt werden; nachträgliche Beantragung möglich, aber schwieriger.
- **Berufliche Reha vergessen**: Nur medizinische Reha beantragt; berufliche Reha hätte Erwerbsfähigkeit erhalten.
- **MDK-Verneinung der Reha-Notwendigkeit**: Gegengutachten des behandelnden Arztes; BSG-Maßstab: nicht Heilung, sondern Verbesserung der Teilhabe.

## Output-Formate

- Reha-Antrag (Muster DRV/GKV)
- Zuständigkeitseinrede-Schreiben
- § 51 SGB V-Widerspruch (Reha-Aufforderung)
- Selbstbeschaffungs-Erstattungsantrag
- Übergangsgeld-Berechnungsblatt

## Quellen

- [§ 40 SGB V – Medizinische Rehabilitation](https://www.gesetze-im-internet.de/sgb_5/__40.html)
- [§ 14 SGB IX – Erstangegangener Träger](https://www.gesetze-im-internet.de/sgb_9_2018/__14.html)
- [§ 9 SGB VI – Reha vor Rente](https://www.gesetze-im-internet.de/sgb_6/__9.html)
- [§ 51 SGB V – Reha-Verweis](https://www.gesetze-im-internet.de/sgb_5/__51.html)
- [Deutsche Rentenversicherung – Rehabilitation](https://www.deutsche-rentenversicherung.de)
- [BSG Entscheidungssuche](https://www.bsg.bund.de/DE/Entscheidungen/entscheidungen_node.html)
- [dejure.org SGB IX § 14](https://dejure.org/gesetze/SGB_IX/14.html)

## 3. `kv-021-kassenwahl-kuendigung-bindungsfrist-wahltarif`

**Fokus:** Kassenwahlrecht nach § 175 SGB V: Bindungsfrist, Kündigung, Sonderkündigungsrecht, Wahltarife und Kostenbeteiligung.

# Kassenwahl: Kündigung, Bindungsfrist und Wahltarif

## Skill-Zweck

Dieser Skill regelt das **Kassenwahlrecht in der GKV**: Wie kann man die Kasse wechseln, wann greift das Sonderkündigungsrecht, was sind Wahltarife und wie ist die Bindungsfrist zu beachten?

## Rechtlicher Rahmen

- **§ 175 SGB V** – Ausübung des Kassenwahlrechts, Bindungsfrist, Kündigung
- **§ 53 SGB V** – Wahltarife: Selbstbehalt, Beitragsrückgewähr, Kostenerstattung, Tarifsonderbedingungen
- **§ 173 SGB V** – Wahlrecht, offene Kassen
- **§ 174 SGB V** – Einschränkungen des Wahlrechts
- **§ 242 SGB V** – Zusatzbeitrag und Sonderkündigungsrecht
- BSG B 1 KR 14/17 R (Wahltarife und Bindungsfristen)

## Kündigungsregeln GKV

| Situation | Frist | Rechtsgrundlage |
|-----------|-------|----------------|
| Ordentliche Kündigung | 2 Monate zum Monatsende | § 175 Abs. 4 Satz 1 |
| Bindungsfrist (Neuzugang) | Mindestens 18 Monate Mitgliedschaft | § 175 Abs. 4 Satz 2 |
| Sonderkündigung Zusatzbeitragserhöhung | 1 Monat Frist | § 175 Abs. 4 Satz 5 i.V.m. § 242 |
| Wahltarif Selbstbehalt | Gesonderte Bindung 3 Jahre | § 53 Abs. 8 |

## Prüfprogramm

### Schritt 1 – Ordentliche Kündigung
- Mitgliedschaft mind. 18 Monate? (Bindungsfrist)
- Kündigung schriftlich, spätestens am letzten Tag des Kalendermonats der 2-Monats-Frist
- Nachweis neuer Mitgliedschaft beifügen (Mitgliedsbescheinigung neue Kasse)
- Alte Kasse muss Kündigung bestätigen

### Schritt 2 – Sonderkündigungsrecht bei Zusatzbeitragserhöhung
- Kasse erhöht Zusatzbeitrag → Sonderkündigungsrecht entsteht
- Kündigung innerhalb 1 Monat nach Erhöhung zum Zeitpunkt des Inkrafttretens
- Information durch Kasse: muss schriftlich mit Hinweis auf Sonderkündigungsrecht erfolgen
- Ohne Information: Sonderkündigungsrecht bleibt bestehen bis Kasse nachträglich informiert

### Schritt 3 – Wahltarife (§ 53 SGB V)
- Selbstbehalt-Tarif: Versicherter zahlt bis Schwellenwert selbst; dafür Beitragsrabatt
- Beitragsrückgewähr: Keine Leistungsinanspruchnahme → anteilige Rückerstattung am Jahresende
- Kostenerstattungstarif: Versicherter zahlt Arzt und erhält Erstattung von Kasse
- Bindung 3 Jahre: Wahltarif-Kündigung nur bei Beitragserhöhung oder nach 3 Jahren

### Schritt 4 – Wechsel zu PKV
- GKV-Mitglied kann bei JAEG-Überschreitung (> 73.800 €/Jahr 2025) zur PKV wechseln
- Rückkehr zur GKV: nur bei Unterschreiten der JAEG oder Statuswechsel (→ kv-003)
- Beratungspflicht der Kasse: § 175 Abs. 5 SGB V

### Schritt 5 – Mitgliedsbescheinigung und Übergangsversicherung
- Neue Kasse bestätigt Mitgliedschaft sofort; auch rückwirkend zum Tag nach Kündigung
- Lücke in Versicherung darf nicht entstehen
- Wenn neue Kasse ablehnt (z.B. Satzungsleistungen): Auffangpflichtversicherung

## Typische Fallen

- **Wahltarif und Kündigung der Kasse**: Kassenentaustritt beendet Wahltarif; Rückforderung bei Selbstbehalt-Tarif beachten.
- **18-Monats-Frist nach Kassenwechsel**: Beginnt neu nach jedem Kassenwechsel.
- **Familienversicherung und Kassenwechsel**: Familienmitglieder versichern sich automatisch bei Hauptmitglied mit.
- **Elektronische Kündigung**: Nur per Kassen-App oder gesicherter Verbindung zulässig; einfache E-Mail reicht nicht.

## Output-Formate

- Kündigungsschreiben (Muster)
- Sonderkündigungsrechts-Schreiben
- Wahltarif-Vergleichstabelle
- Widerspruch gegen Kündigung-Ablehnung
- Mitgliedsbescheinigung-Anforderung

## Quellen

- [§ 175 SGB V – Kassenwahlrecht](https://www.gesetze-im-internet.de/sgb_5/__175.html)
- [§ 53 SGB V – Wahltarife](https://www.gesetze-im-internet.de/sgb_5/__53.html)
- [§ 242 SGB V – Zusatzbeitrag](https://www.gesetze-im-internet.de/sgb_5/__242.html)
- [BSG Kassenwechsel-Rechtsprechung](https://www.bsg.bund.de/DE/Entscheidungen/entscheidungen_node.html)
- [dejure.org § 175 SGB V](https://dejure.org/gesetze/SGB_V/175.html)
- [GKV-Spitzenverband Kassenwahl](https://www.gkv-spitzenverband.de)
