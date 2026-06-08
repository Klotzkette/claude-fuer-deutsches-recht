---
name: datenschutz-datenpanne-art-33-34-72h-incident
description: "Datenpannen-Incident-Response Art. 33 und 34 DSGVO. 72-Stunden-Frist ab Kenntnis Art. 33 I DSGVO und Benachrichtigung Betroffener bei hohem Risiko Art. 34 I DSGVO. Sieben-Fragen-Diagnose: Wer hat wann was entdeckt Datenkategorien Anzahl Betroffener Vertraulichkeit Integritaet Verfuegbarkeit Risiko TOM Art. 32 DSGVO Auftragsverarbeiter beteiligt. Schritt-für-Schritt: Sachverhalt klaeren NICHT vorschnell handeln Risikobewertung dokumentieren Mandantenfreigabe Aufsicht melden Betroffene benachrichtigen Massnahmen Lessons Learned. Mustertexte für Meldebogen und Betroffenenbenachrichtigung. Abgrenzung: keine Bussgeldverteidigung (datenschutz-bussgeldverfahren-art-83-dsgvo-verteidigung)."
---

# Datenschutz Datenpanne — 72 Stunden Incident Response nach Art. 33 und 34 DSGVO

## Zweck

Dieser Skill fuehrt durch den Akutfall einer Datenpanne. Ziel ist die fristwahrende und zugleich bussgeldminimierende Meldung an die Aufsichtsbehoerde nach Art. 33 DSGVO und — falls erforderlich — die Benachrichtigung der Betroffenen nach Art. 34 DSGVO, ohne durch vorschnelle Selbstbelastung das Bussgeldrisiko nach Art. 83 DSGVO zu erhoehen.

## Wann dieses Modul hilft / Kaltstart-Fragen

Sie brauchen den Skill ab dem Moment, in dem der Mandant Kenntnis von einem Vorfall erlangt: Ransomware, Phishing-Mail mit Anhangsverlust, falsch versendete Massen-E-Mail, gestohlener Laptop ohne Verschluesselung, fehlerhaft konfiguriertes Cloud-Bucket, unbefugter Mitarbeiterzugriff, Diebstahl USB, Druckdienstleister-Fehlversand.

Sieben-Fragen-Diagnose mit Antwort-Pattern:

1. **Wer hat wann was entdeckt?** Konkretes Datum und Uhrzeit, Person, Quelle. **Achtung:** Die 72-Stunden-Frist nach Art. 33 I DSGVO laeuft ab **Kenntnis des Verantwortlichen** — bei Auftragsverarbeitern beginnt die Frist beim Verantwortlichen ab dessen Kenntnis (Art. 33 II DSGVO).
2. **Welche Datenkategorien sind betroffen?** Allgemein, Art. 9 DSGVO (Gesundheit, Religion, Gewerkschaft, sexuelle Orientierung, biometrisch), Art. 10 DSGVO (Strafrechtsdaten), Art. 8 DSGVO (Minderjaehrige), Bankdaten, Authentifizierungsdaten?
3. **Anzahl Betroffener?** Geschaetzt — Mindest- und Maximalwert.
4. **Welche Schutzziele verletzt?** Vertraulichkeit (Offenlegung), Integritaet (Veraenderung), Verfuegbarkeit (Verlust)?
5. **Welche TOM nach Art. 32 DSGVO** waren wirksam (Verschluesselung, Pseudonymisierung, Backup)? **Wichtig** für Art. 34 III a DSGVO Ausnahme.
6. **Ist ein Auftragsverarbeiter beteiligt?** Wer ist Verantwortlicher? Wer meldet?
7. **Risiko für Betroffene?** Identitaetsdiebstahl, finanzieller Schaden, Diskriminierung, Rufschaedigung, Verlust der Kontrolle, unbefugte Aufhebung der Pseudonymisierung?

## Rechtlicher Rahmen

- **Art. 4 Nr. 12 DSGVO** Definition Verletzung des Schutzes personenbezogener Daten: Vernichtung, Verlust, Veraenderung, unbefugte Offenlegung oder Zugang.
- **Art. 33 I DSGVO** Meldepflicht innerhalb 72 Stunden ab Kenntnis des Verantwortlichen, ausser unwahrscheinliches Risiko für Rechte und Freiheiten.
- **Art. 33 II DSGVO** Auftragsverarbeiter meldet unverzueglich an Verantwortlichen.
- **Art. 33 III DSGVO** Pflichtinhalt: Art der Verletzung, Kategorien und Anzahl Betroffener, DSB-Kontakt, wahrscheinliche Folgen, ergriffene oder vorgeschlagene Massnahmen.
- **Art. 33 IV DSGVO** Stufenmeldung zulaessig.
- **Art. 33 V DSGVO** Dokumentationspflicht aller Verletzungen unabhaengig von Meldung.
- **Art. 34 I DSGVO** Benachrichtigung Betroffener bei voraussichtlich hohem Risiko.
- **Art. 34 III DSGVO** Ausnahmen: (a) wirksame Verschluesselung, (b) Folgemassnahmen verhindern Risiko, (c) Unverhaeltnismaessigkeit / öffentliche Bekanntmachung.
- **Art. 32 DSGVO** TOM-Pflicht.
- **§ 65 BDSG** Spezifische Meldepflichten Strafverfolgung.
- **EDSA Leitlinien 9/2022** zur Meldung von Datenpannen (angenommen 28.03.2023).

## Mandantenfuehrung Schritt-für-Schritt

1. **Sachverhalt klaeren — NICHT vorschnell handeln.** Erste 4-8 Stunden: Fakten sammeln, Zeitstrahl, Personenkreis. Noch nichts ausserhalb des Mandanten kommunizieren. Vermeiden Sie pauschale Selbstvorwuerfe in Mails (werden im Bussgeldverfahren zur Akte).
2. **Risikobewertung dokumentieren.** Matrix: Eintrittswahrscheinlichkeit Risiko x Schwere. EDSA-Leitlinien 9/2022 als Massstab.
3. **Mandantenfreigabe einholen.** Geschaeftsfuehrung, DSB nach Art. 37 DSGVO, ggf. IT-Sicherheitsbeauftragter, ggf. Betriebsrat.
4. **Aufsicht melden — innerhalb 72 Stunden ab Kenntnis.** Stufenmeldung Art. 33 IV nutzen, wenn Fakten noch unklar. Lieber knapp und ehrlich als spekulativ ueberschwaenglich.
5. **Betroffene benachrichtigen — nur bei hohem Risiko Art. 34 I.** Bei wirksamer Verschluesselung Ausnahme Art. 34 III a pruefen. Nicht voreilig benachrichtigen, wenn Risiko gering — sonst unnoetige Sorge und Reputationsschaden.
6. **Massnahmen einleiten.** Passworter zuruecksetzen, Zugaenge sperren, Backup aktivieren, Vorfall eindaemmen.
7. **Lessons Learned und Dokumentation Art. 33 V DSGVO.** Internes Pannenregister, Update der TOM, ggf. DSFA aktualisieren.

## Trade-off-Matrix

| Variante | Vorteil | Nachteil |
|---|---|---|
| Sofortmeldung unter 24h | Kooperation signalisiert, Bussgeldmilderung Art. 83 II c | Unvollstaendige Fakten erhoehen spaeteren Aenderungsbedarf |
| Stufenmeldung Art. 33 IV | Frist gewahrt, Praezision steigt | Mehr Schreibarbeit, Aufsicht erwartet Update |
| Verschluesselungs-Ausnahme Art. 34 III a | Spart Massenbenachrichtigung | Wirksamkeit muss dokumentiert sein (Schluessel sicher, Algorithmus aktuell) |
| Oeffentliche Bekanntmachung Art. 34 III c | Spart Einzelbenachrichtigung | Reputationsschaden, Anwaltsabmahnung |

## Mustertexte

### Interner Sachverhalts-Zeitstrahl (Vorlage)

```
Vorfall: [kurz]
Entdeckung: [Datum, Uhrzeit, Person]
Vermuteter Eintritt: [Datum]
Datenkategorien: [Art. 6 / Art. 9 / Art. 10 / Bankdaten]
Schaetzung Betroffene: min [n] max [n]
Schutzziel verletzt: [Vertraulichkeit / Integritaet / Verfuegbarkeit]
Wirksame TOM: [Verschluesselung ja/nein, Algorithmus, Schluesselverwaltung]
Auftragsverarbeiter beteiligt: [ja/nein, AVV Art. 28]
Aktuelles Risiko: [niedrig / mittel / hoch]
```

### Meldebogen Aufsichtsbehoerde (Kerntext)

> Meldung einer Verletzung des Schutzes personenbezogener Daten nach Art. 33 DSGVO
>
> 1. Verantwortlicher: [Firma, Anschrift, Ansprechpartner].
> 2. DSB: [Name, Kontakt nach Art. 37 VII DSGVO].
> 3. Art der Verletzung: [konkret, z. B. unbefugte Offenlegung durch Fehlversand].
> 4. Kategorien personenbezogener Daten: [konkret].
> 5. Anzahl Betroffener: [Schaetzung, mit Begruendung].
> 6. Wahrscheinliche Folgen: [konkret nach EDSA 9/2022].
> 7. Ergriffene und vorgeschlagene Massnahmen: [TOM-Bezug Art. 32 DSGVO, Sofortmassnahmen].
> 8. Bewertung der Meldepflicht und der Benachrichtigung Betroffener Art. 34 DSGVO: [Pruefung mit Ergebnis].
> 9. Stufenmeldung Art. 33 IV: [ja/nein, Update bis Datum].

### Betroffenenbenachrichtigung (Art. 34 II DSGVO)

> Sehr geehrte/r [Name],
>
> in einer am [Datum] festgestellten Verletzung des Schutzes personenbezogener Daten sind moeglicherweise auch Ihre Daten betroffen. Wir informieren Sie hiermit gemaess Art. 34 DSGVO.
>
> Was ist passiert: [klar].
> Welche Daten sind betroffen: [konkret].
> Welche moeglichen Folgen koennen entstehen: [konkret].
> Was wir getan haben: [Massnahmen, TOM].
> Was Sie tun koennen: [Passwortwechsel, Konto-Monitoring, Hotline].
>
> Datenschutzbeauftragter: [Kontakt nach Art. 37 VII DSGVO].
> Sie koennen sich beschweren bei der zuständigen Aufsichtsbehoerde nach Art. 77 DSGVO: [Adresse].
>
> Mit freundlichen Gruessen

## Typische Fehler

- Frist 72h aus Art. 33 I DSGVO ab Vorfall statt ab Kenntnis berechnen.
- Selbstbelastung in interner Mail-Kommunikation ("wir hatten doch gesagt, das Backup macht keiner").
- Verschluesselungs-Ausnahme Art. 34 III a behaupten, ohne Schluesselverwaltung und Algorithmus zu belegen.
- Betroffene per Massen-E-Mail aus dem System informieren, das gerade kompromittiert wurde.
- Stufenmeldung Art. 33 IV genannt, aber nie Update geliefert.

**Was triggert die Aufsichtsbehoerde besonders?** Fristueberschreitung, leere Floskeln zu TOM, fehlende Risikoabwaegung Art. 34, keine Mandantenbeteiligung dokumentiert, kein DSB beteiligt.

## Querverweise

- `datenschutz-erstgespraech-mandantenmatrix-7-fragen`
- `datenschutz-mandantenkommunikation-aufsichtsbehoerde`
- `datenschutz-bussgeldverfahren-art-83-dsgvo-verteidigung`
- `datenschutz-schadensersatz-art-82-dsgvo-gerichtsstreit`
- `datenpanne-meldung`
- `it-recht-incident-response-it-sicherheit-und-datenschutz-zusammen`

## Quellen Stand 06/2026

- DSGVO Art. 4 Nr. 12, 32, 33, 34, 37, 82, 83.
- BDSG § 65.
- EDSA, Leitlinien 9/2022 zur Meldung von Verletzungen des Schutzes personenbezogener Daten, Version 2.0, angenommen 28.03.2023.
- EDSA, Leitlinien 01/2021 zu Beispielen für Meldungen von Datenpannen.
- Keine Aufsatzfundstellen aus Modellwissen.

## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.
