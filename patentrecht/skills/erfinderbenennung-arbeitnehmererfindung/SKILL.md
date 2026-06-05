---
name: erfinderbenennung-arbeitnehmererfindung
description: "Erfinderbenennung Arbeitnehmererfindung: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Erfinderbenennung Arbeitnehmererfindung

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Erfinderbenennung Arbeitnehmererfindung** im Plugin Patentrecht (Verfahren, Verletzung). Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `erfinderbenennung-und-arbeitnehmererfindung` | Prüft Erfinderbenennung, Rechtekette und Arbeitnehmererfindungs-Schnittstellen: wer ist Erfinder, wer ist Anmelder, Diensterfindung, freie Erfindung, Inanspruchnahme, Vergütung und Dokumentationsrisiken. |
| `erfindungsmeldung-aufnahme-und-rueckfragen` | Nimmt rohe Erfindungsideen, Skizzen, Mandantenmails und Prototypnotizen auf; trennt technische Lehre von bloßer Idee, erkennt Offenbarungsrisiken und erstellt Rückfragen für eine patentfähige Anmeldung. |
| `freedom-to-operate-und-schutzbereich` | Prüft Freedom-to-Operate und Schutzbereich: Zielprodukt, Territory, Registerstand, Anspruchsmerkmale, wortsinngemäße Verwirklichung, Äquivalenz, Design-around und Risikomemo. |

## Arbeitsweg

Im Plugin Patentrecht (Verfahren, Verletzung) gilt für **Erfinderbenennung Arbeitnehmererfindung**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `erfinderbenennung-und-arbeitnehmererfindung`

**Fokus:** Prüft Erfinderbenennung, Rechtekette und Arbeitnehmererfindungs-Schnittstellen: wer ist Erfinder, wer ist Anmelder, Diensterfindung, freie Erfindung, Inanspruchnahme, Vergütung und Dokumentationsrisiken.

# Erfinderbenennung und Arbeitnehmererfindung

## Erfinderstatus

Erfinder ist, wer einen schöpferischen Beitrag zur technischen Lehre geleistet hat. Nicht ausreichend sind bloße Aufgabenstellung, Finanzierung, Management, Routineversuche oder mechanische Umsetzung ohne eigenen Beitrag.

## Prüffragen

1. Wer hatte welche konkrete technische Idee?
2. Welche Beiträge betreffen den erfinderischen Kern?
3. Arbeitnehmer, Geschäftsführer, Freelancer, Universität, Kunde, Lieferant?
4. Gibt es Arbeitsvertrag, Entwicklungsvertrag, NDA, IP Assignment, Hochschul-/Forschungsbedingungen?
5. Wurde eine Diensterfindung gemeldet und in Anspruch genommen?
6. Sind Vergütungs- und Nachweisdokumente vorhanden?
7. Muss die Anmeldung korrigiert oder eine Rechtekette geschlossen werden?

## Output

- Erfinderbeitragsmatrix.
- Rechtekettenübersicht.
- Rückfragen an HR/Legal/Technik.
- Warnhinweise zur Anmeldung und Lizenzierung.

## Red Flags

- Anmelder ist Konzernmutter, erfunden wurde aber bei Tochter/Freelancer.
- Erfinder sollen aus politischen Gründen aufgenommen oder gestrichen werden.
- "Alle Rechte übertragen" steht im Vertrag, aber Erfinderbenennung/ArbEG-Logik ist ungeklärt.
- Lizenzvertrag setzt Inhaberschaft voraus, Register und Aktenlage tragen das nicht.

## ArbEG — Pflichtnormen

- **§ 5 ArbEG Meldepflicht:** Arbeitnehmer muss Diensterfindung unverzüglich schriftlich melden; Arbeitgeber bestätigt schriftlich. Frist für Bestätigung: unverzüglich.
- **§ 6 ArbEG Inanspruchnahme:** Arbeitgeber kann binnen 4 Monaten nach ordnungsgemäßer Meldung ablehnen; sonst gilt sie als unbeschränkt in Anspruch genommen (§ 6 Abs. 2 ArbEG seit 01.10.2009).
- **§ 9 ArbEG Vergütung:** angemessene Vergütung nach Lizenzanalogie; Vergütungsrichtlinien (RL Nr. 1 bis 39 vom 20.07.1959 / Anpassungen). Üblich: Erfindungswert x Anteilsfaktor (a, b, c) x Persönlicher Anteil. Vergütung verfällt nicht mit Beendigung des Arbeitsverhältnisses.
- **§ 16 ArbEG Schutzrechtsanmeldung:** Arbeitgeber muss Patent anmelden, sonst Rückübertragungsanspruch (§ 16 ArbEG).
- **§ 37 PatG Erfinderbenennung:** Erfinder muss in Anmeldung benannt werden; Anmeldung ohne richtige Erfinderbenennung ist anfechtbar (§ 8 PatG Vindikation).
- **Spezialfälle:** Hochschulerfindungen § 42 ArbEG (Hochschullehrer); Universitäten haben 30 % Vergütungsanteil; Veröffentlichungsfreiheit zu wahren.
- **Vergütung Routinearbeit:** § 9 ArbEG-Logik nicht auf "freie" Erfindungen anwendbar — Trennung sauber ziehen.
- Falle: Bei Konzernlizenzen IP-Inhaberschaft live im DPMA-Register prüfen; "wirtschaftliche" Zuordnung reicht nicht; Diensterfinderbenennung darf nicht zur Familienangelegenheit werden — § 8 PatG Vindikationsanspruch droht.


## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.

## 2. `erfindungsmeldung-aufnahme-und-rueckfragen`

**Fokus:** Nimmt rohe Erfindungsideen, Skizzen, Mandantenmails und Prototypnotizen auf; trennt technische Lehre von bloßer Idee, erkennt Offenbarungsrisiken und erstellt Rückfragen für eine patentfähige Anmeldung.

# Erfindungsmeldung aufnehmen

## Vorgehen

1. **Erfindung in Alltagssprache erfassen:** Was soll besser funktionieren als bisher?
2. **Technisches Problem bestimmen:** Welcher technische Nachteil wird überwunden?
3. **Lösung in Merkmale zerlegen:** Bauteile, Schritte, Steuerlogik, Sensorik, Material, Parameter, Wechselwirkungen.
4. **Wirkung festhalten:** Warum bewirkt gerade diese Merkmalskombination den Vorteil?
5. **Varianten sammeln:** minimale Ausführung, bevorzugte Ausführung, Alternativen, optionale Merkmale, Ersatzteile.
6. **Offenbarung prüfen:** Website, Messe, Pitch, Kundenangebot, Zeitungsbericht, Verkauf, Prototypvorführung, NDA ja/nein.
7. **Erfinder klären:** wer hat zum erfinderischen Beitrag beigetragen, wer nur umgesetzt?

## Rückfragen an Mandanten

Rückfragen müssen technisch präzise sein. Nicht fragen: "Bitte beschreiben Sie die Erfindung genauer." Besser:

- Welches Bauteil oder welcher Verfahrensschritt unterscheidet Ihre Lösung von bekannten Produkten?
- Welche Variante funktioniert noch, wenn dieses Merkmal fehlt?
- Welche Messwerte oder Beobachtungen belegen den technischen Vorteil?
- Wer hat wann welche Idee eingebracht?
- Wurde die Lösung bereits ohne Geheimhaltungsbindung gezeigt, verkauft oder beschrieben?
- Gibt es Fotos, Skizzen, CAD, Stücklisten, Quellcode, Laborbuch, Prototypen oder E-Mails?

## Output

- Erfindungssteckbrief.
- Merkmalsliste.
- Offenbarungs- und Fristenwarnung.
- Rückfragenkatalog.
- Empfehlung: Anspruchsentwurf, Recherche, Geheimhaltung, Sofortanmeldung oder Nichtanmeldung.

## Rechtlicher Rahmen

- **§ 1 PatG:** Patente werden für Erfindungen auf allen Gebieten der Technik erteilt, sofern sie neu sind, auf erfinderischer Tätigkeit beruhen und gewerblich anwendbar sind.
- **Neuheit (§ 3 PatG; Art. 54 EPÜ):** alles, was vor dem Anmelde-/Prioritätstag der Öffentlichkeit zugänglich war, ist neuheitsschädlich. **Kein "grace period"** im EPÜ -- Vorveröffentlichung durch den Erfinder ist genauso schädlich wie die durch Dritte (Ausnahme nur § 3 Abs. 5 PatG für offensichtlichen Missbrauch / einschlägige Ausstellung).
- **Erfinderische Tätigkeit (§ 4 PatG; Art. 56 EPÜ):** Aufgabe-Lösungs-Ansatz (Problem-Solution-Approach) des EPA.
- **Diensterfindung (ArbnErfG):** Meldepflicht des Arbeitnehmers (§ 5 ArbnErfG); Inanspruchnahme durch Arbeitgeber innerhalb von 4 Monaten ab Meldung (§ 6 ArbnErfG); Vergütung nach § 9 ArbnErfG.
- **Erfinderbenennung (§ 37 PatG):** binnen 16 Monaten nach Anmeldetag bzw. Prioritätstag; sonst Versagung.

## Sofortmaßnahme bei drohender Offenbarung
- Bei kurzfristiger Messe/Pitch: prioritätsbegründende DPMA- oder EPA-Erstanmeldung mit knapp möglichem Anspruchssatz; Nachreichung Beschreibung und Zeichnungen binnen Prioritätsjahr (Art. 87 EPÜ).


## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.

## 3. `freedom-to-operate-und-schutzbereich`

**Fokus:** Prüft Freedom-to-Operate und Schutzbereich: Zielprodukt, Territory, Registerstand, Anspruchsmerkmale, wortsinngemäße Verwirklichung, Äquivalenz, Design-around und Risikomemo.

# Freedom-to-Operate und Schutzbereich

## Reihenfolge

1. **Zielprodukt fixieren:** Version, technische Spezifikation, Prozess, Lieferkette, Zielmärkte.
2. **Relevante Schutzrechte finden:** Patente, Gebrauchsmuster, EP-Validierungen, Einheitspatente, nationale Teile.
3. **Rechtsstand prüfen:** in Kraft, erteilt, abgelaufen, Einspruch, Beschränkung, Jahresgebühr, Inhaber.
4. **Ansprüche gliedern:** nur geltende Anspruchsfassung verwenden.
5. **Produkt gegen Merkmale legen:** vorhandene Daten, fehlende Daten, Annahmen.
6. **Verletzung prüfen:** wortsinngemäß, dann Äquivalenz mit Vorsicht.
7. **Einwendungen:** Nichtigkeit, Vorbenutzung, Erschöpfung, Lizenz, Verwirkung, experimentelle Nutzung.
8. **Design-around:** technische Alternativen und Restgefahren.

## Output

- FTO-Ampel je Schutzrecht und Territory.
- Claim Chart.
- Registerstand mit Abrufdatum.
- Offene technische Beweisfragen.
- Handlungsempfehlung: Launch, Redesign, Lizenz, Rechtsbestandsangriff, Standstill.

## Pflichtsatz

FTO ist nie absolute Freiheit. Das Ergebnis ist eine risikogewichtete Recherche und Prüfung auf Grundlage der konkret geprüften Schutzrechte und Datenbanken.

## Schutzbereich-Auslegung — Pflichtnormen

- **§ 14 PatG / Art. 69 EPÜ und Auslegungsprotokoll:** Schutzbereich primär nach Ansprüchen, Beschreibung und Zeichnungen heranziehen, aber nicht zur Erweiterung über den Anspruch hinaus.
- **Wortsinn vor Äquivalenz:** Erst exakte Merkmalsverwirklichung prüfen; dann Äquivalenz nach BGH "Schneidmesser I/II" (X ZR 168/00) — gleiche Wirkung, naheliegende Auffindbarkeit, Gleichwertigkeit aus Anspruch.
- **Mittelbare Verletzung § 10 PatG:** Lieferung von Mitteln, die sich auf wesentliche Erfindungselemente beziehen, kann verletzen, auch wenn Anwender nicht verletzt.
- **Einwendungen prüfen:** Vorbenutzungsrecht (§ 12 PatG), Erschöpfung (§ 9 S. 2 PatG), Lizenz, Verwirkung (§ 242 BGB), Versuchsprivileg (§ 11 Nr. 2 PatG), Bolar-Klausel Medikamentenzulassung.
- **UPC-Zuständigkeit:** Bei Einheitspatent zentrale Klage am UPC; Opt-out nur bis Ende Übergangszeit; danach Bindung an UPC-Spruch.
- Tipp: Claim Chart immer mit Anspruchsversion (Anmeldetag, Erteilungstext, Einspruchstext) und Registerabrufdatum versehen.


## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.
