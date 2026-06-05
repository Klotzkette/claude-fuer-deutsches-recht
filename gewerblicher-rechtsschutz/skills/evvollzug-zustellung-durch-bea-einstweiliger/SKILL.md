---
name: evvollzug-zustellung-durch-bea-einstweiliger
description: "Evvollzug Zustellung Durch BEA Einstweiliger: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Evvollzug Zustellung Durch BEA Einstweiliger

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Evvollzug Zustellung Durch BEA Einstweiliger** im Plugin Gewerblicher Rechtsschutz. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `evvollzug-neu-003-zustellung-durch-gerichtsvollzieher-im-ip-verf` | EV-Vollzug: Zustellung durch Gerichtsvollzieher (GV) bei einstweiligen Verfügungen im IP-Recht – Marke, Patent, UWG, Urheberrecht. Auftrag, Vorschuss, Zustellurkunde, Protokoll und Fehlerquellen bei natürlichen und juristischen Personen. |
| `evvollzug-neu-004-bea-zustellung-einstweiliger-rechtsschutz-risi` | EV-Vollzug: beA-Zustellung bei einstweiligen Verfügungen im IP-Recht – Voraussetzungen, Risiken, Nachweisführung und Alternativen. Wann beA sicher ist, wann nicht, und wie Vollzugsrisiken minimiert werden. |
| `evvollzug-neu-005-ordnungsmittelantrag-vollstreckung-unterlassun` | EV-Vollzug: Ordnungsmittelantrag nach § 890 ZPO bei Verstoß gegen Unterlassungstitel aus einstweiliger Verfügung. Tatbestandsvoraussetzungen, Antragsinhalt, Höhe Ordnungsgeld, Verschuldensmaßstab und typische Verteidigungsstrategien des Schuldners. |

## Arbeitsweg

Im Plugin Gewerblicher Rechtsschutz gilt für **Evvollzug Zustellung Durch BEA Einstweiliger**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `evvollzug-neu-003-zustellung-durch-gerichtsvollzieher-im-ip-verf`

**Fokus:** EV-Vollzug: Zustellung durch Gerichtsvollzieher (GV) bei einstweiligen Verfügungen im IP-Recht – Marke, Patent, UWG, Urheberrecht. Auftrag, Vorschuss, Zustellurkunde, Protokoll und Fehlerquellen bei natürlichen und juristischen Personen.

# EV-Vollzug 003: Zustellung durch Gerichtsvollzieher im IP-Verfahren

## Zweck und Mandatsbezug

Dieser Skill behandelt die **Gerichtsvollzieherzustellung als bevorzugten Vollziehungsweg** bei einstweiligen Verfügungen im gewerblichen Rechtsschutz. Der Gerichtsvollzieher (GV) ist das verlässlichste Instrument für die Parteizustellung einer Beschlussverfügung, weil er eine förmliche Zustellurkunde nach § 182 ZPO ausfertigt, die später für Ordnungsmittelanträge benötigt wird.

Mandatsbezug: Markenrechtliche Unterlassungsverfügung gegen Wettbewerber; patentrechtliche Unterlassungsverfügung gegen Hersteller; UWG-Verfügung gegen Online-Shop. In allen Fällen ist die GV-Zustellung Standard, da der Zustellnachweis im Vollstreckungsverfahren gerichtsfest sein muss.

## Rechtlicher Rahmen

### Zentrale Normen

- **§ 192 ZPO** – Parteizustellung durch Gerichtsvollzieher; der Gerichtsvollzieher fertigt die Zustellurkunde nach § 182 ZPO aus.
- **§ 182 ZPO** – Inhalt der Zustellurkunde: Empfänger, Ort, Zeit, Art der Zustellung, Unterschrift des GV.
- **§ 178 ZPO** – Ersatzzustellung an Haushaltsangehörige oder Arbeitgeber, wenn Zustellungsadressat nicht angetroffen.
- **§ 179 ZPO** – Ersatzzustellung durch Einlegen in den Briefkasten (Einwurfszustellung).
- **§ 181 ZPO** – Niederlegung bei der Post/Behörde bei gescheiterter Zustellung.
- **§ 929 Abs. 2 ZPO** – Vollziehungsfrist, innerhalb derer der GV-Auftrag erteilt und vollzogen werden muss.
- **§ 1 GvKostG** – Kostenvorschuss für Gerichtsvollzieher.

### Zustellarten durch den GV

| Zustellart | Norm | Nachweis | Beweiswert |
|---|---|---|---|
| Übergabe an Adressat persönlich | § 177 ZPO | Zustellurkunde | Stark |
| Ersatzzustellung Haushaltsmitglied | § 178 Abs. 1 Nr. 1 ZPO | Zustellurkunde | Mittel |
| Ersatzzustellung Arbeitgeber | § 178 Abs. 1 Nr. 2 ZPO | Zustellurkunde | Mittel |
| Einwurfszustellung Briefkasten | § 179 ZPO | Zustellurkunde | Mittel |
| Niederlegung | § 181 ZPO | Benachrichtigung + Urkunde | Schwach |

## Kaltstart in 5 Fragen

1. **Schuldner:** Natürliche Person oder juristische Person (GmbH, AG, GbR)? Handelsregistereintrag bekannt?
2. **Zustellanschrift:** Gesicherte Zustelladresse des Schuldners oder vertretungsberechtigten Organs?
3. **Verfügungsausfertigung:** Liegt vollstreckbare Ausfertigung der EV vor (§ 724 ZPO)?
4. **Vorschuss:** Ist Kostenvorschuss für GV vorbereitet? Welches Vollstreckungsgericht ist zuständig?
5. **Zeitdruck:** Wie viel Zeit der Monatsfrist (§ 929 Abs. 2 ZPO) ist noch verfügbar?

## Prüfprogramm

### Schritt 1 – Zustellanschrift ermitteln

- **Natürliche Person:** Meldeanschrift aus Einwohnermeldeamt (§ 44 BMG) oder bekannte Geschäftsadresse.
- **GmbH/AG:** Sitz laut Handelsregister (handelsregister.de); zustellungsbevollmächtigte Person identifizieren.
- **Personengesellschaft:** Alle Gesellschafter prüfen; Zustellung an einen geschäftsführenden Gesellschafter ausreichend.
- **Zustellbevollmächtigter:** Falls bekannt (z.B. Prozessanwalt des Schuldners), Zustellung an diesen möglich.

### Schritt 2 – Vollstreckbare Ausfertigung besorgen

- Antrag auf Erteilung vollstreckbarer Ausfertigung beim Erlasskammergericht.
- Bei Beschlussverfügung: Ausfertigung mit Vollstreckungsklausel nach § 724 ZPO.
- Originausfertigung an GV übergeben; Fotokopie in eigener Akte behalten.

### Schritt 3 – Zustellauftrag formulieren

Musterinhalt eines GV-Auftrags:
```
An den Gerichtsvollzieher [Zuständigkeitsbereich]
Zustellauftrag gem. § 192 ZPO

In der Sache [Antragsteller] ./. [Schuldner]
Az.: [Gericht, AZ]

Ich beauftrage Sie, die beigefügte vollstreckbare Ausfertigung der einstweiligen Verfügung
des [Gericht] vom [Datum] dem Schuldner
[vollständiger Name, Adresse]
zuzustellen und mir die Zustellurkunde zu übermitteln.

Kostenvorschuss: [Betrag] anbei / per Überweisung
```

### Schritt 4 – Kostenvorschuss und Zuständigkeit

- GV-Kosten nach GvKostG: Zustellgebühr berechnet sich nach dem Streitwert und der Zustellart.
- Zuständiger GV: richtet sich nach Wohnort/Sitz des Schuldners (§ 20 GVGA).
- Online-Beauftragung über GV-Portal vieler Bundesländer möglich.

### Schritt 5 – Zustellurkunde auswerten

- Datum und Uhrzeit der Zustellung prüfen.
- Art der Zustellung (persönlich, Ersatz, Einwurf, Niederlegung) prüfen.
- Bei Niederlegung: Benachrichtigungsschreiben versendet? Aushang?
- Zustellurkunde in Akte, Datum im Fristenbuch.

## Besonderheiten bei juristischen Personen

- **GmbH:** Zustellung an Geschäftsführer persönlich (am Sitz) oder an Prokurist.
- **AG:** An Vorstandsmitglied oder gesetzlichen Vertreter.
- **Wenn kein Vertreter angetroffen:** Ersatzzustellung an Mitarbeiter am Geschäftssitz (§ 178 Abs. 1 Nr. 2 ZPO) möglich.
- **Zustellungsbevollmächtigter in Deutschland:** Wenn ausländischer Schuldner, Zustellungsbevollmächtigten identifizieren oder Auslandszustellung einleiten (→ evvollzug-neu-006).

## Typische Fallen

- **GV kennt Adresse nicht:** GV gibt Auftrag zurück; Frist läuft weiter; neue Adressermittlung nötig.
- **Falscher GV-Bezirk:** Auftrag zurückgesandt; zeitverlust.
- **Keine vollstreckbare Ausfertigung übergeben:** GV kann nicht zustellen; Rücksendung des Auftrags.
- **Niederlegung als ausreichend angesehen:** Bei Ordnungsmittelantrag prüft Gericht, ob Schuldner tatsächlich Kenntnis erhielt; Niederlegung ist schwächster Nachweis.
- **Verfristung:** GV-Auftrag erteilt, aber Vollzug erst nach Fristablauf – Frist gilt als versäumt.

## Output-Module

- **GV-Auftragsformular:** Mustertext mit allen Pflichtfeldern.
- **Checkliste Zustellungsvorbereitung:** Ausfertigung, Adresse, Vorschuss, GV-Bezirk.
- **Zustellurkunden-Auswertungsbogen:** Datum, Art, Empfänger, Beweiswert.
- **Folgepfad bei Zustellversagen:** Adressermittlung, Wiederholung, alternative Zustellwege.

## Quellenregel

- [§ 192 ZPO – dejure.org](https://dejure.org/gesetze/ZPO/192.html)
- [§ 182 ZPO – dejure.org](https://dejure.org/gesetze/ZPO/182.html)
- [§ 178 ZPO – dejure.org](https://dejure.org/gesetze/ZPO/178.html)
- GVKostG: [gesetze-im-internet.de/gvkostg](https://www.gesetze-im-internet.de/gvkostg/)
- Keine Kommentar-Blindzitate; aktuelle GV-Kostenberechnung über offizielle Kostenrechner der Bundesländer prüfen.

## Anschluss-Skills

- `evvollzug-neu-001` – Vollziehungsfrist und Parteizustellung Übersicht
- `evvollzug-neu-004` – beA-Zustellung als Alternative
- `evvollzug-neu-005` – Ordnungsmittelantrag nach Vollzug
- `evvollzug-neu-006` – Auslandszustellung EV

## 2. `evvollzug-neu-004-bea-zustellung-einstweiliger-rechtsschutz-risi`

**Fokus:** EV-Vollzug: beA-Zustellung bei einstweiligen Verfügungen im IP-Recht – Voraussetzungen, Risiken, Nachweisführung und Alternativen. Wann beA sicher ist, wann nicht, und wie Vollzugsrisiken minimiert werden.

# EV-Vollzug 004: beA-Zustellung im Einstweiligen Rechtsschutz – Risiken und Praxis

## Zweck und Mandatsbezug

Dieser Skill analysiert, wann und ob die **Zustellung über das besondere elektronische Anwaltspostfach (beA)** für den Vollzug einer einstweiligen Verfügung im gewerblichen Rechtsschutz geeignet ist. Die beA-Zustellung ist technisch möglich, aber mit spezifischen Risiken verbunden – insbesondere wenn der Schuldner nicht anwaltlich vertreten ist oder der beA-Empfang nicht gesichert ist.

Mandatsbezug: Anwalt erwägt, statt des Gerichtsvollziehers die beA-Zustellung zu nutzen, um Kosten und Zeit zu sparen. Dieser Skill klärt, wann das vertretbar ist und wo die Risiken liegen.

## Rechtlicher Rahmen

### Zentrale Normen

- **§ 173 ZPO** – Elektronische Zustellung; Zustellung durch elektronisches Dokument als gleichwertige Form zur körperlichen Zustellung.
- **§ 173 Abs. 1 ZPO** – Zustellung an Anwälte über beA möglich, wenn diese über beA erreichbar sind.
- **§ 174 ZPO** – Zustellung gegen Empfangsbekenntnis: Anwalt muss Empfang bestätigen; erst mit Empfangsbekenntnis ist Zustellung bewirkt.
- **§ 130a ZPO** – Elektronisches Dokument; technische Anforderungen (qualifizierte elektronische Signatur oder Übermittlung aus De-Mail/beA).
- **§ 192 ZPO** – Parteizustellung; regelt, dass Parteien die Zustellung veranlassen können.
- **§ 929 Abs. 2 ZPO** – Vollziehungsfrist; Fristversäumnis bei unvollständiger Zustellung.

### Zustellungsformen im Vergleich

| Form | Norm | Voraussetzung | Nachweis | Risiko |
|---|---|---|---|---|
| GV-Zustellung | § 192, 182 ZPO | Adresse bekannt | Zustellurkunde | Adressfehler |
| beA an Anwalt des Schuldners | § 173 ZPO | Schuldner anwaltlich vertreten, beA aktiv | Übermittlungsprotokoll + Empfangsbekenntnis | Kein ERB, Fristversäumnis |
| beA an Partei direkt | § 173 Abs. 2 ZPO | Nur bei Unternehmern mit Pflicht-beA | Schwierig | Hohe Unsicherheit |
| Post-Zustellungsauftrag | § 175 ZPO | Einschreiben mit Rückschein | Rückschein | Annahmeablehnung |

## Kaltstart in 5 Fragen

1. **Anwaltliche Vertretung Schuldner:** Ist der Schuldner durch einen Anwalt vertreten und ist dessen beA-Adresse bekannt?
2. **Empfangsbereitschaft:** Liegt ein vorangegangener Schriftwechsel per beA vor, der Empfangsbereitschaft belegt?
3. **Fristlage:** Wie viel Zeit verbleibt bis zum Fristende nach § 929 Abs. 2 ZPO? Reicht Zeit für Rückfragen?
4. **Empfangsbekenntnis-Strategie:** Wie wird sichergestellt, dass das ERB auch tatsächlich und rechtzeitig zurückkommt?
5. **Fallback:** Was ist der Plan, wenn beA-Zustellung scheitert oder ERB nicht zurückkommt?

## Prüfprogramm

### Schritt 1 – Prüfen, ob beA-Zustellung möglich ist

- Schuldner muss durch Anwalt vertreten sein, der ein aktives beA hat.
- Eigener Anwalt sucht die beA-Adresse des gegnerischen Anwalts im BRAK-Verzeichnis.
- Kein beA-Zwang für nicht-anwaltliche Parteien; beA-Zustellung an GmbH-Geschäftsführer persönlich in der Regel nicht möglich.

### Schritt 2 – Übermittlung und Protokoll

- Dokument mit QES oder aus dem beA des eigenen Anwalts versenden.
- Übermittlungsprotokoll des beA abspeichern (zeigt: Datum, Uhrzeit, Empfänger, Größe, Ergebnis).
- Übermittlungsprotokoll allein ist **kein Zustellnachweis**; es belegt nur den Versand.

### Schritt 3 – Empfangsbekenntnis einholen

- Nach § 174 ZPO ist Zustellung erst mit Eingang des Empfangsbekenntnisses (ERB) bewirkt.
- ERB muss Datum des tatsächlichen Empfangs enthalten.
- Gegnerischer Anwalt ist nicht zur sofortigen ERB-Übermittlung verpflichtet.
- Praktisches Problem: Schuldneranwalt verzögert ERB strategisch, Frist läuft ab.

### Schritt 4 – Risikobewertung

**Risikoampel:**
- **Grün (beA-Zustellung sicher):** Schuldneranwalt hat zuvor beA-Empfangsbereitschaft gezeigt, ERB ist schnell zu erwarten, Frist hat noch > 2 Wochen.
- **Gelb (beA-Zustellung riskant):** Erstmaliger Kontakt, Frist läuft in < 1 Woche ab, Unsicherheit über ERB-Zeitpunkt.
- **Rot (GV bevorzugen):** Schuldner nicht anwaltlich vertreten; Frist läuft in < 5 Tagen ab; Schuldneranwalt bekannt für Verzögerungstaktik.

### Schritt 5 – Fallback-Szenario vorbereiten

- Gleichzeitig GV-Auftrag vorbereiten und bei Ausbleiben des ERB sofort erteilen.
- Nie ausschließlich auf beA-Zustellung setzen, wenn Frist eng ist.
- Bei ambivalenter Lage: GV-Zustellung als primären Weg wählen.

## Verfahrenstechnische Details

### Qualifizierte elektronische Signatur (QES)

- Vollstreckbare Ausfertigung muss für beA-Übermittlung als PDF/A vorliegen.
- QES des übermittelnden Anwalts muss gültig und zertifiziert sein.
- Prüfung: BRAK-Zertifikat aktuell? Zeitstempel korrekt?

### Hybridlösung

- Manche Kanzleien nutzen beA-Zustellung parallel zur GV-Zustellung.
- Erste Zustellung (beA oder GV) bewirkt Vollziehung; keine Doppelwirkung.
- Dokumentation beider Wege für den Fall, dass eine angegriffen wird.

## Typische Fallen

- **ERB-Strategie des Gegners:** Empfangsbekenntnis wird mit falschem Datum ausgefüllt; Prüfung des Übermittlungsprotokolls dagegen halten.
- **beA-Postfach inaktiv:** Gegnerisches beA ist seit Entzug der Zulassung inaktiv; keine Zustellung möglich.
- **Kein Anwalt auf Schuldnerseite:** Direkte beA-Zustellung an Partei scheitert.
- **ERB zu spät:** ERB kommt nach Fristablauf; Zustellung gilt als erst dann bewirkt.
- **Falsches Dokument:** Einfache Kopie statt vollstreckbarer Ausfertigung übermittelt; Zustellung unwirksam.

## Output-Module

- **Risikoampel beA vs. GV:** Einschätzung im konkreten Fall.
- **Checkliste beA-Zustellung:** Adresse BRAK-Verzeichnis, QES, Protokoll, ERB.
- **ERB-Tracking-Vorlage:** Datum Versand, erwarteter ERB-Eingang, tatsächlicher Eingang.
- **Fallback-Auftrag GV:** Parallelauftrag für den Fall des Scheiterns.

## Quellenregel

- [§ 173 ZPO – dejure.org](https://dejure.org/gesetze/ZPO/173.html)
- [§ 174 ZPO – dejure.org](https://dejure.org/gesetze/ZPO/174.html)
- [§ 130a ZPO – dejure.org](https://dejure.org/gesetze/ZPO/130a.html)
- BRAK-Hinweise zu beA und Zustellung: [brak.de](https://www.brak.de)
- Keine Kommentar-Blindzitate; aktuelle beA-Praxis über Kammermitteilungen prüfen.

## Anschluss-Skills

- `evvollzug-neu-001` – Vollziehungsfrist Überblick
- `evvollzug-neu-003` – GV-Zustellung als verlässliche Alternative
- `evvollzug-neu-005` – Ordnungsmittelantrag nach Vollzug
- `evvollzug-neu-006` – Auslandszustellung EV

## 3. `evvollzug-neu-005-ordnungsmittelantrag-vollstreckung-unterlassun`

**Fokus:** EV-Vollzug: Ordnungsmittelantrag nach § 890 ZPO bei Verstoß gegen Unterlassungstitel aus einstweiliger Verfügung. Tatbestandsvoraussetzungen, Antragsinhalt, Höhe Ordnungsgeld, Verschuldensmaßstab und typische Verteidigungsstrategien des Schuldners.

# EV-Vollzug 005: Ordnungsmittelantrag (§ 890 ZPO) nach Unterlassungstitel

## Zweck und Mandatsbezug

Dieser Skill behandelt den **Ordnungsmittelantrag nach § 890 ZPO** als das zentrale Vollstreckungsinstrument bei Unterlassungsverfügungen im gewerblichen Rechtsschutz. Der Schuldner hat gegen eine rechtskräftige oder vollzogene Unterlassungsverfügung verstoßen – jetzt muss der Antragsteller die Einhaltung erzwingen.

Mandatsbezug: Markeninhaber hat Unterlassungsverfügung gegen Verletzer erwirkt und vollzogen; Verletzer nutzt das Zeichen weiter. Oder: UWG-Antragsteller hat EV gegen unlauteren Wettbewerber; Wettbewerber stellt nach Verfügungszustellung weiter dieselbe irreführende Werbung ein.

## Rechtlicher Rahmen

### Zentrale Normen

- **§ 890 Abs. 1 ZPO** – Vollstreckung eines Unterlassungsurteils durch Ordnungsgeld (bis 250.000 EUR) oder Ordnungshaft (bis sechs Monate pro Verstoß).
- **§ 890 Abs. 2 ZPO** – Androhungsgebot: Ordnungsmittel dürfen nur vollstreckt werden, wenn sie vorab angedroht wurden; die Androhung erfolgt regelmäßig durch die Unterlassungsverfügung selbst oder einen separaten Androhungsbeschluss.
- **§ 891 ZPO** – Verfahren bei Ordnungsmittelantrag: Antrag des Gläubigers, rechtliches Gehör des Schuldners, Beschluss des Vollstreckungsgerichts.
- **§ 928 ZPO** – Anwendbarkeit der allgemeinen Vollstreckungsvorschriften auf EV.
- **§ 936 ZPO** – Anwendbarkeit der Arrestvorschriften.

### Voraussetzungen des Ordnungsmittelantrags

| Voraussetzung | Inhalt | Prüfpunkt |
|---|---|---|
| Vollstreckbarer Unterlassungstitel | Vollzogene EV oder rechtskräftiges Urteil | Zustellurkunde vorhanden? |
| Androhung der Ordnungsmittel | Im Tenor der EV enthalten oder separater Beschluss | Tenor lesen |
| Zuwiderhandlung | Konkreter Verstoß nach Zustellung der EV | Beleg: Screenshot, Zeuge, Testkauf |
| Verschulden | Schuldner hat vorsätzlich oder fahrlässig gehandelt | Schuldner muss sich entlasten |
| Antrag beim Vollstreckungsgericht | Schriftlicher Antrag mit Belegen | Form und Zuständigkeit prüfen |

## Kaltstart in 5 Fragen

1. **Titelnachweis:** Liegt vollzogene EV mit Zustellurkunde vor? Enthält der Tenor eine Ordnungsmittelandrohung?
2. **Verstoßbeleg:** Wann, wo und wie genau hat der Schuldner gegen die Unterlassung verstoßen? Welche Belege liegen vor?
3. **Zeitpunkt:** War der Verstoß nach der Zustellung der EV an den Schuldner?
4. **Zuständigkeit:** Welches Gericht hat die EV erlassen? Ordnungsmittelantrag an dasselbe Gericht (§ 891 ZPO)?
5. **Output:** Antragsschriftsatz, Checkliste Beleglage, Memo zur Höhe des Ordnungsgeldes?

## Prüfprogramm

### Schritt 1 – Titel und Androhung prüfen

- Tenor der EV auf Androhungspassage prüfen: „Bei Zuwiderhandlung wird ein Ordnungsgeld bis zu 250.000 EUR, ersatzweise Ordnungshaft, angedroht."
- Fehlt die Androhung im Tenor, muss vor dem Ordnungsmittelantrag ein separater Androhungsbeschluss beantragt werden (§ 890 Abs. 2 ZPO).
- Prüfen, ob EV durch Widerspruch oder Berufung aufgehoben wurde – dann kein Ordnungsmittelantrag.

### Schritt 2 – Zuwiderhandlung dokumentieren

- **Datum und Uhrzeit** des Verstoßes genau festhalten (wichtig für Verschuldensfrage).
- **Beweismittel:**
 - Screenshot mit Datum, URL, Metadaten
 - Testkauf mit Quittung
 - Zeuge mit schriftlicher Erklärung
 - eidesstattliche Versicherung des Antragstellers
- Verstoß muss **nach** Zustellung der EV an Schuldner erfolgt sein; Datum der Zustellurkunde ist Bezugspunkt.
- Mehrere Verstöße getrennt dokumentieren; jeder Verstoß kann gesondert geahndet werden.

### Schritt 3 – Antragsschrift verfassen

Pflichtbestandteile:
1. Bezeichnung des Vollstreckungsgerichts
2. Rubrum (Gläubiger, Schuldner)
3. AZ der EV
4. Datum der Zustellung der EV (mit Bezug auf Zustellurkunde)
5. Konkrete Darstellung der Zuwiderhandlung mit Datum
6. Beweismittel als Anlage
7. Antrag: „Es wird beantragt, gegen den Schuldner wegen Zuwiderhandlung gegen den Beschluss des [Gericht] vom [Datum] – AZ [AZ] – ein Ordnungsgeld in Höhe von mindestens [X] EUR, ersatzweise Ordnungshaft, festzusetzen."

### Schritt 4 – Ordnungsgeldhöhe einschätzen

- Keine gesetzliche Tabelle; Gericht übt Ermessen aus.
- Faktoren: Schwere des Verstoßes, Umsatz des Schuldners, Wiederholungsgefahr, Vorsatz/Fahrlässigkeit.
- Richtwerte in IP-Verfahren: 5.000–50.000 EUR für einfachen Verstoß; bei Unternehmen mit hohem Umsatz bis 250.000 EUR.
- Empfehlung im Antrag: Konkreten Betrag nennen; Gericht kann abweichen, aber Orientierungsrahmen setzen.

### Schritt 5 – Schuldnerverteidigung antizipieren

Typische Einwände des Schuldners:
- **Kein Verschulden:** Mitarbeiter habe ohne Wissen gehandelt; Gegenargument: Organisationsverschulden.
- **Titel deckt Verstoß nicht ab:** Verstoßverhalten fällt nicht unter Unterlassungsgebot; prüfen, ob Tenor weit genug formuliert.
- **Verstoß vor Zustellung:** Prüfen: Wurde Verstoß wirklich erst nach Zustellungsdatum begangen?
- **Einstellung des Vertriebs:** Schuldner behauptet, Verstoß eingestellt zu haben; Belege für Fortsetzung beschaffen.

## Nachgelagerte Schritte

- **Ordnungsgeld-Beschluss:** Einzahlung des Ordnungsgeldes an Staatskasse; kein direkter Nutzen für Gläubiger.
- **Unterlassungsklage in der Hauptsache:** Falls EV nur einstweilig – muss Hauptsacheklage innerhalb Frist erhoben werden (Abschlussschreiben beachten → evvollzug-neu-007).
- **Wiederholter Verstoß:** Jeder erneute Verstoß führt zu neuem Ordnungsmittelantrag; kumulativ möglich.

## Output-Module

- **Antragsschriftsatz-Vorlage:** Vollständiger Mustertext mit Platzhaltern.
- **Belegliste Verstoß:** Datum, Art des Verstoßes, Beweismittel, Anlage-Nummer.
- **Ordnungsgeld-Einschätzungsmatrix:** Umsatz, Schwere, Vorsatz, Wiederholung → empfohlene Höhe.
- **Antizipierte Verteidigung:** Tabelle Schuldnereinwand / Gegenargument.

## Quellenregel

- [§ 890 ZPO – dejure.org](https://dejure.org/gesetze/ZPO/890.html)
- [§ 891 ZPO – dejure.org](https://dejure.org/gesetze/ZPO/891.html)
- Rechtsprechung zur Ordnungsgeldhöhe nur mit Gericht, Datum, AZ und prüfbarer Quelle (openjur.de, bgh.de).
- Keine BeckRS-Blindzitate; Gerichtspraxis zu Ordnungsgeld variiert; konkretes Gericht maßgeblich.

## Anschluss-Skills

- `evvollzug-neu-001` – Vollziehungsfrist und Parteizustellung
- `evvollzug-neu-007` – Abmahnung, Abschlussschreiben und Hauptsache
- `unterlassungsverlangen` – Unterlassungserklärung als Alternative zum Gerichtsverfahren
- `verletzungs-triage` – Erstentscheidung bei IP-Verletzung
