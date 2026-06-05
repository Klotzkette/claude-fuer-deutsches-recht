---
name: delikt-organisationspflicht-psychische
description: "Delikt Organisationspflicht Psychische: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Delikt Organisationspflicht Psychische

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Delikt Organisationspflicht Psychische** im Plugin Bgb Bt Pruefer. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `delikt-organisationspflicht` | Prüft Organisationspflichten im Deliktsrecht: § 831 BGB, § 823 BGB Verkehrssicherungspflicht und organschaftliche Haftung. |
| `delikt-psychische-schaeden` | Prüft Ersatzfähigkeit psychischer Schäden im Deliktsrecht: Schockschaden, PTBS, Gesundheitsverletzung § 823 Abs. 1 BGB. |
| `delikt-verkehrspflicht-digital` | Prüft Verkehrssicherungspflichten im digitalen Raum: Plattformhaftung, IT-Sicherheit, Datenpannen und deliktische Haftung. |

## Arbeitsweg

Im Plugin Bgb Bt Pruefer gilt für **Delikt Organisationspflicht Psychische**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `delikt-organisationspflicht`

**Fokus:** Prüft Organisationspflichten im Deliktsrecht: § 831 BGB, § 823 BGB Verkehrssicherungspflicht und organschaftliche Haftung.

# Delikt: Organisationspflicht

## Fachkern: Delikt: Organisationspflicht
- **Spezialgegenstand:** Delikt: Organisationspflicht; der Skill muss die konkrete Fachfrage tragen und nicht nur in einen allgemeinen Startdialog zurückfallen.
- **Normen-/Quellenanker:** BGB Besonderer Teil: Kaufrecht, Werk-/Dienstvertrag, Auftrag/Geschäftsbesorgung, Miet-/Leasingnähe, GoA, Bereicherung, Delikt, Verjährung und AGB-Schnittstellen.
- **Entscheidende Weiche:** Anspruchsgrundlage, Vertragstyp/Mischvertrag, Pflichtverletzung, Vertretenmüssen, Schaden, Einwendung und Beweisfrage sauber trennen.
- **Arbeitsprodukt:** Liefere eine fallbezogene `Norm / Tatsache / Beleg / Wertung / Gegenargument / nächster Schritt`-Matrix und einen direkt nutzbaren Textbaustein, wenn der Nutzer einen Entwurf braucht.


## Zweck

Organisationsverschulden und Verkehrssicherungspflichten im Deliktsrecht prüfen: Haftung des Unternehmens für Organisationsdefizite nach § 823 Abs. 1 BGB und § 831 BGB.

## Normanker

- § 823 Abs. 1 BGB: Verkehrssicherungspflicht als Bestandteil des allgemeinen Deliktsrechts
- § 831 BGB: Haftung für den Verrichtungsgehilfen (Exkulpationsmöglichkeit)
- § 840 BGB: gesamtschuldnerische Haftung mehrerer Schädiger
- § 31 BGB: Haftung des Vereins/der juristischen Person für Organmitglieder
- § 278 BGB: Erfüllungsgehilfenhaftung (Abgrenzung zu § 831 BGB)
- BGH-Rechtsprechung zu Organisationsverschulden: nur nach Live-Prüfung zitieren

## Intake

- Wer hat die schädigende Handlung begangen: Organ, leitender Mitarbeiter oder einfacher Verrichtungsgehilfe?
- Welche Organisations- und Aufsichtspflichten hatte das Unternehmen?
- Kann das Unternehmen nach § 831 Abs. 1 Satz 2 BGB entlastet werden (Sorgfalt bei Auswahl und Überwachung)?
- Liegt ein Organisationsdefizit vor (fehlende Dokumentation, Schulung, Kontrollen)?
- Sind mehrere juristische Personen oder natürliche Personen beteiligt?

## Prüfraster

1. Schädiger-Identifikation: natürliche Person, Organ (§ 31 BGB) oder Verrichtungsgehilfe (§ 831 BGB)?
2. Bei Organ: § 31 BGB-Haftung der juristischen Person für Organe ohne Exkulpationsmöglichkeit
3. Bei Verrichtungsgehilfe: § 831 Abs. 1 BGB-Haftung, Exkulpation nach Satz 2 (sorgfältige Auswahl, Überwachung, Ausrüstung)
4. Verkehrssicherungspflichten nach § 823 Abs. 1 BGB: Umfang und Inhalt der Pflichten
5. Organisationsverschulden: Hat das Unternehmen notwendige Strukturen, Schulungen, Kontrollen eingerichtet?
6. Kausalität zwischen Organisationsdefizit und Schaden
7. Gesamtschuldnerische Haftung nach § 840 BGB
8. § 278 BGB als Alternative bei vertraglicher Grundlage

## Fallstricke

- § 31 BGB erfasst alle Personen, die zur selbstständigen Leitung eines Teils der Unternehmenstätigkeit berufen sind (erweiterter Organbegriff).
- Exkulpation nach § 831 Abs. 1 Satz 2 BGB setzt sorgfältige Auswahl, Anleitung und Überwachung voraus.
- Organisationspflichten können sich aus öffentlich-rechtlichen Vorschriften ergeben (z.B. Arbeitssicherheitsrecht).
- Beweislast für Exkulpation liegt beim Geschäftsherrn.
## Stoppschilder

- Keine Kommentar-, Aufsatz- oder BeckRS/Juris-Blindzitate.
- Tragende Gesetzesstände live gegen amtliche/frei zugängliche Quellen prüfen.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und überprüfbarer Quelle verwenden.
- Bei Unsicherheit die Annahme ausdrücklich markieren und eine Rückfrage oder Quellenprüfung auslösen.

## Output

- Haftungsstruktur-Diagramm (Organ/Verrichtungsgehilfe/Unternehmen)
- Exkulpations-Checkliste nach § 831 Abs. 1 Satz 2 BGB
- Organisationsdefizit-Analyse
- Risikoampel und Handlungsempfehlungen

## Qualitätsregeln

- § 31 BGB und § 831 BGB immer klar voneinander trennen.
- Exkulpationsvoraussetzungen für § 831 BGB vollständig auflisten.
- Parallele vertragliche Haftung nach § 278 BGB prüfen.

## Anschluss-Skills

- deliktsrecht-haftung-fuer-verrichtungen-paragraph-831
- produzentenhaftung-und-verkehrssicherung
- delikt-verkehrspflicht-digital
- delikt-vertrag-konkurrenz


## Quellen

- https://www.gesetze-im-internet.de/bgb/__823.html
- https://www.gesetze-im-internet.de/bgb/__831.html
- https://www.gesetze-im-internet.de/bgb/__280.html
## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.

## 2. `delikt-psychische-schaeden`

**Fokus:** Prüft Ersatzfähigkeit psychischer Schäden im Deliktsrecht: Schockschaden, PTBS, Gesundheitsverletzung § 823 Abs. 1 BGB.

# Delikt: Psychische Schäden

## Fachkern: Delikt: Psychische Schäden
- **Spezialgegenstand:** Delikt: Psychische Schäden; der Skill muss die konkrete Fachfrage tragen und nicht nur in einen allgemeinen Startdialog zurückfallen.
- **Normen-/Quellenanker:** BGB Besonderer Teil: Kaufrecht, Werk-/Dienstvertrag, Auftrag/Geschäftsbesorgung, Miet-/Leasingnähe, GoA, Bereicherung, Delikt, Verjährung und AGB-Schnittstellen.
- **Entscheidende Weiche:** Anspruchsgrundlage, Vertragstyp/Mischvertrag, Pflichtverletzung, Vertretenmüssen, Schaden, Einwendung und Beweisfrage sauber trennen.
- **Arbeitsprodukt:** Liefere eine fallbezogene `Norm / Tatsache / Beleg / Wertung / Gegenargument / nächster Schritt`-Matrix und einen direkt nutzbaren Textbaustein, wenn der Nutzer einen Entwurf braucht.


## Zweck

Ersatzfähigkeit psychischer und psychosomatischer Schäden nach § 823 Abs. 1 BGB prüfen: Schockschäden, PTBS und Abgrenzung zu nicht ersatzfähigen Trauerschäden.

## Normanker

- § 823 Abs. 1 BGB: Gesundheitsverletzung als Rechtsgut
- § 253 BGB: Schmerzensgeld
- § 249 BGB: Naturalrestitution (Behandlungskosten)
- BGH-Rechtsprechung zu Schockschäden: nur nach Live-Prüfung mit Aktenzeichen zitieren
- BGH-Linie zur Abgrenzung: echte Gesundheitsverletzung vs. normale seelische Belastung

## Intake

- Welche psychischen Beeinträchtigungen liegen vor: PTBS, depressive Episode, Anpassungsstörung?
- Ist die psychische Beeinträchtigung ärztlich diagnostiziert und belegt?
- In welchem Zusammenhang steht die Beeinträchtigung zum schädigenden Ereignis?
- War die betroffene Person selbst Unfallopfer oder Zeuge (Schockschaden)?
- Welcher Schadensposten wird geltend gemacht: Behandlungskosten, Schmerzensgeld, Verdienstausfall?

## Prüfraster

1. Rechtsgutsverletzung: Ist die psychische Beeinträchtigung als Gesundheitsverletzung im Sinne des § 823 Abs. 1 BGB einzustufen?
2. Kriterien der Gesundheitsverletzung: pathologisch diagnostizierbar, über normale seelische Reaktion hinaus
3. Schockschaden: Voraussetzungen (enge Beziehung zum Primäropfer, unmittelbarer Wahrnehmungsbezug)
4. Kausalität: äquivalente und adäquate Kausalität; Schutzzweck der Norm
5. Zurechnungszusammenhang: war psychische Reaktion für Schädiger vorhersehbar?
6. Schadenshöhe: Behandlungskosten, Schmerzensgeld nach § 253 BGB, Verdienstausfall
7. Mitverursachung des Geschädigten nach § 254 BGB
8. Verjährung: § 199 BGB (Kenntniserlangung von Arztdiagnose)

## Fallstricke

- Normale Trauer und seelische Belastung ohne Krankheitswert sind nicht ersatzfähig.
- Schockschaden erfordert in aller Regel eigene Gesundheitsverletzung, nicht nur mittelbare Betroffenheit.
- Beweislast liegt beim Geschädigten: ärztliche Diagnose und Kausalitätsnachweis erforderlich.
- Verjährungsbeginn knüpft an Kenntniserlangung von der Diagnose an.
## Stoppschilder

- Keine Kommentar-, Aufsatz- oder BeckRS/Juris-Blindzitate.
- Tragende Gesetzesstände live gegen amtliche/frei zugängliche Quellen prüfen.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und überprüfbarer Quelle verwenden.
- Bei Unsicherheit die Annahme ausdrücklich markieren und eine Rückfrage oder Quellenprüfung auslösen.

## Output

- Gesundheitsverletzungs-Analyse mit Diagnoseabgleich
- Kausalitätsgutachten-Checkliste
- Schadensberechnung (Behandlungskosten, Schmerzensgeld, Verdienstausfall)
- Beweislast-Lückenliste

## Qualitätsregeln

- Psychische Schäden immer mit medizinischer Dokumentation verknüpfen.
- Abgrenzung Gesundheitsverletzung/normale seelische Reaktion explizit begründen.
- BGH-Schockschadenrechtsprechung nur nach Live-Prüfung zitieren.

## Anschluss-Skills

- deliktsrecht-paragraph-823-1
- schadensrecht-paragraphen-249-253
- dienstvertrag-und-behandlungsvertrag
- workflow-beweislast-und-belegmatrix


## Quellen

- https://www.gesetze-im-internet.de/bgb/__823.html
- https://www.gesetze-im-internet.de/bgb/__253.html
- https://www.gesetze-im-internet.de/bgb/__249.html
## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.

## 3. `delikt-verkehrspflicht-digital`

**Fokus:** Prüft Verkehrssicherungspflichten im digitalen Raum: Plattformhaftung, IT-Sicherheit, Datenpannen und deliktische Haftung.

# Delikt: Verkehrspflicht Digital

## Fachkern: Delikt: Verkehrspflicht Digital
- **Spezialgegenstand:** Delikt: Verkehrspflicht Digital; der Skill muss die konkrete Fachfrage tragen und nicht nur in einen allgemeinen Startdialog zurückfallen.
- **Normen-/Quellenanker:** BGB Besonderer Teil: Kaufrecht, Werk-/Dienstvertrag, Auftrag/Geschäftsbesorgung, Miet-/Leasingnähe, GoA, Bereicherung, Delikt, Verjährung und AGB-Schnittstellen.
- **Entscheidende Weiche:** Anspruchsgrundlage, Vertragstyp/Mischvertrag, Pflichtverletzung, Vertretenmüssen, Schaden, Einwendung und Beweisfrage sauber trennen.
- **Arbeitsprodukt:** Liefere eine fallbezogene `Norm / Tatsache / Beleg / Wertung / Gegenargument / nächster Schritt`-Matrix und einen direkt nutzbaren Textbaustein, wenn der Nutzer einen Entwurf braucht.


## Zweck

Verkehrssicherungspflichten in digitalen Umgebungen prüfen: Haftung von Plattformbetreibern, IT-Sicherheitspflichten und deliktische Konsequenzen bei Datenpannen oder Cyberangriffen.

## Normanker

- § 823 Abs. 1 BGB: allgemeine Verkehrssicherungspflicht, auch im digitalen Bereich
- § 823 Abs. 2 BGB in Verbindung mit Art. 32 DSGVO: IT-Sicherheitspflicht als Schutzgesetz
- § 1004 BGB analog: Beseitigung und Unterlassung bei Persönlichkeitsrechtsverletzungen online
- TMG (§§ 7–10 TMG) bzw. DSA (Digital Services Act): Haftungsprivileg und Pflichtenrahmen für Hostingprovider
- NIS2-Richtlinie und BSIG: Cybersicherheitspflichten für kritische Infrastrukturen
- BGH-Rechtsprechung zu Plattformhaftung: nur nach Live-Prüfung zitieren

## Intake

- Welche digitale Infrastruktur (Plattform, Software, IoT-Gerät) ist betroffen?
- Welcher Schaden ist entstanden: Datenverlust, Persönlichkeitsrechtsverletzung, Vermögensschaden?
- Hat der Betreiber zumutbare IT-Sicherheitsmaßnahmen nach Art. 32 DSGVO ergriffen?
- Greift das Haftungsprivileg nach §§ 7–10 TMG oder DSA?
- Sind Dritte (z.B. Hacker) als Mitschädiger beteiligt?

## Prüfraster

1. Rechtsgutsverletzung: Eigentum, allgemeines Persönlichkeitsrecht, Gesundheit oder sonstiges Recht
2. Verkehrssicherungspflicht: Welche Sicherheitsmaßnahmen sind für diesen digitalen Dienst angemessen?
3. IT-Sicherheitspflichten nach Art. 32 DSGVO als Schutzgesetz im Sinne des § 823 Abs. 2 BGB
4. Haftungsprivileg nach DSA/TMG: greift es hier (Hosting, Caching, Mere Conduit)?
5. Kausalität: hat Pflichtverletzung den Schaden verursacht (auch mittelbare Kausalität durch Dritte)?
6. Zurechenbarkeit: war Angriff vorhersehbar und hätte Betreiber ihn durch zumutbare Maßnahmen abwenden können?
7. Mitverschulden des Geschädigten nach § 254 BGB (schwaches Passwort, veraltete Software)
8. Schadensersatz: materielle und immaterielle Schäden (auch Datenschutzschäden nach Art. 82 DSGVO)

## Fallstricke

- Haftungsprivileg nach DSA gilt nicht, wenn Plattform von rechtswidrigem Inhalt Kenntnis hatte und nicht handelte.
- Art. 82 DSGVO gibt eigene Schadensersatzansprüche, die neben § 823 BGB stehen.
- NIS2-Pflichten begründen keine direkte privatrechtliche Haftung, können aber Schutzgesetzverletzung indizieren.
- Beweissicherung bei Cybervorfällen muss sofort erfolgen (Logs, Backups, Forensik).
## Stoppschilder

- Keine Kommentar-, Aufsatz- oder BeckRS/Juris-Blindzitate.
- Tragende Gesetzesstände live gegen amtliche/frei zugängliche Quellen prüfen.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und überprüfbarer Quelle verwenden.
- Bei Unsicherheit die Annahme ausdrücklich markieren und eine Rückfrage oder Quellenprüfung auslösen.

## Output

- Haftungsanalyse (Betreiber, Plattform, Dienstleister)
- IT-Sicherheitspflichten-Checkliste
- Schadensberechnung und DSGVO-Parallelprüfung
- Beweissicherungshinweise

## Qualitätsregeln

- DSA und TMG immer auf Aktualität prüfen.
- DSGVO-Haftung parallel zu § 823 BGB prüfen.
- Beweissicherung bei Cybervorfall immer als ersten Schritt anordnen.

## Anschluss-Skills

- deliktsrecht-paragraph-823-1
- delikt-organisationspflicht
- produzentenhaftung-und-verkehrssicherung
- workflow-livequellen-rechtsstand


## Quellen

- https://www.gesetze-im-internet.de/bgb/__823.html
- https://www.gesetze-im-internet.de/tmg/
- https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32022R2065
## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.
