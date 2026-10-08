# Incident-Response-Meldung bei Datenschutzverletzungen (Art. 33/34 DSGVO)

---

Kurz-Hinweis: Diese Vorlage ist unverbindlich, ein experimenteller Text und keine Rechtsberatung. Nutzung nur auf eigene Gewähr, eigene Gefahr und ohne Gewähr. Die ausführlichen Hinweise zu § 43a Abs. 2 BRAO, § 203 StGB, DSGVO sowie Apache-2.0 OR MIT stehen in der README dieser Vorlage.

---

## Vorlage

[WARNHINWEIS — nicht Schriftsatzbestandteil, nicht miteinreichen]

Diese Vorlage ersetzt nicht die anwaltliche Eigenleistung. Sie liefert das Gerüst, nicht den Fall. Der Anwender bringt den Sachverhalt, die Beweismittel, die taktische Entscheidung und die Verantwortung; die Vorlage bringt Struktur, Sprache und die unbedingt zu prüfenden Stellen. Wer nur Platzhalter füllt, ohne den eigenen Sachverhalt zu durchdenken, hat noch keinen Schriftsatz, sondern einen Entwurf.

Weitere Hinweise und ausführliche Praxis-Erläuterungen in der README dieser Vorlage.

---

### Rubrum, Adressat und Beteiligte

**Incident-Response-Meldung bei Datenschutzverletzungen (Art. 33/34 DSGVO) — Beteiligte, Akte und Versand**

Datenschutzrechtlich Verantwortlicher: [Firma oder Behörde, Anschrift, verantwortliche Leitung und Kontaktdaten].

Zuständige Datenschutzaufsichtsbehörde: [Behörde, Meldeportal, Anschrift und vorhandenes Geschäftszeichen].

Interne Kopie an: [Datenschutzbeauftragte / Informationssicherheit / Geschäftsleitung / Auftragsverarbeiter / keine].

Datenschutzverletzung: [interne Vorfallsnummer, Kenntniszeitpunkt, betroffene Systeme, Datenarten und Personengruppen].

Meldung nach Art. 33 DSGVO über: [behördliches Meldeportal / zugelassener sicherer Kanal], Fristende der 72-Stunden-Frist [Datum und Uhrzeit].

### TEIL A — INTERNES MELDEPROTOKOLL (ERSTERFASSUNG; INTERN VERTRAULICH)

**Vorfallsnummer:** [IR-JJJJ-NNNN — fortlaufend vergeben]
**Datum und Uhrzeit der Entdeckung:** [TT.MM.JJJJ, HH:MM Uhr]
**Datum und Uhrzeit der Kenntnisnahme des Verantwortlichen:** [TT.MM.JJJJ, HH:MM Uhr]
**72-Stunden-Frist läuft ab:** [TT.MM.JJJJ, HH:MM Uhr] *(72 Stunden ab Kenntnisnahme)*
**Bearbeiter:** [Name, Funktion]
**DSB informiert am:** [TT.MM.JJJJ, HH:MM Uhr]

---

1 Beschreibung des Vorfalls

| Feld | Inhalt |
|---|---|
| Art der Verletzung | ☐ Unbefugter Zugang ☐ Datenverlust/-vernichtung ☐ Veränderung ☐ Offenlegung ☐ Sonstiges: […] |
| Betroffene Systeme/Anwendungen | [Systembeschreibung] |
| Ursache (soweit bekannt) | [z. B. Phishing, Konfigurationsfehler, Ransomware, Verlust eines Datenträgers] |
| Zeitraum der Verletzung | Von: [TT.MM.JJJJ] Bis: [TT.MM.JJJJ] (oder: noch nicht abgeschlossen) |
| Entdeckt durch | [Person/System/externer Hinweis] |

---

2 Betroffene Daten

| Kategorie | Anzahl betroffener Datensätze (geschätzt) | Besondere Kategorien (Art. 9 DSGVO)? |
|---|---|---|
| [z. B. Namen, E-Mail-Adressen] | [n] | ☐ Ja ☐ Nein |
| [z. B. Passwörter (gehasht/Klartext)] | [n] | ☐ Ja ☐ Nein |
| [z. B. Zahlungsdaten] | [n] | ☐ Ja ☐ Nein |
| [weitere Kategorien] | [n] | ☐ Ja ☐ Nein |

**Betroffene Personen:**
☐ Kunden ☐ Mitarbeiter ☐ Geschäftspartner ☐ Minderjährige ☐ Sonstige: […]
Geschätzte Anzahl betroffener Personen: [n]

---

3 Risikobeurteilung (Erstbewertung)

*Anhand der EDSA-Leitlinien 9/2022 und ErwGr. 85–88 DSGVO:*

| Kriterium | Bewertung |
|---|---|
| Art der Verletzung (Vertraulichkeit / Integrität / Verfügbarkeit) | […] |
| Sensibilität der Daten | ☐ gering ☐ mittel ☐ hoch (Art. 9-Daten, Finanzdaten, Zugangsdaten) |
| Anzahl betroffener Personen | [n] |
| Mögliche Folgen | [z. B. Identitätsdiebstahl, finanzielle Schäden, Diskriminierung, Rufschädigung] |
| Wahrscheinlichkeit des Schadenseintritts | ☐ gering ☐ mittel ☐ hoch |
| **Voraussichtliches Risiko** | ☐ Kein Risiko → keine Meldepflicht ☐ Risiko → Meldung an Aufsichtsbehörde (Art. 33) ☐ Hohes Risiko → zusätzlich Benachrichtigung Betroffener (Art. 34) |

---

4 Sofortmaßnahmen

| Maßnahme | Verantwortlich | Erledigt am |
|---|---|---|
| Zugang gesperrt / System isoliert | [Name] | [Datum] |
| Backup-Überprüfung eingeleitet | [Name] | [Datum] |
| IT-Forensik-Sicherung | [Name] | [Datum] |
| Passwörter zurückgesetzt | [Name] | [Datum] |
| AVV-Partner informiert | [Name] | [Datum] |
| DSB informiert | [Name] | [Datum] |
| Entscheidung über Aufsichtsmeldung | [Name] | [Datum] |

---

### TEIL B — MELDUNG AN DIE AUFSICHTSBEHÖRDE (ART. 33 DSGVO)

**An:** [Name der zuständigen Datenschutz-Aufsichtsbehörde]
**Adresse / Meldeportal:** [URL oder postalische Adresse]
**Vorfallsnummer:** [IR-JJJJ-NNNN]
**Meldedatum:** [TT.MM.JJJJ]
**Art der Meldung:** ☐ Erstmeldung ☐ Ergänzungsmeldung zu Meldung vom [Datum]

---

Sehr geehrte Damen und Herren,

gemäß Art. 33 Abs. 1 DSGVO melden wir hiermit eine Verletzung des Schutzes personenbezogener Daten.

1 Kontaktdaten des Verantwortlichen (Art. 33 Abs. 3 lit. a DSGVO)

Verantwortlicher: **[vollständige Firma]**
Anschrift: [Straße, PLZ, Ort]
Ansprechperson für diese Meldung: [Name, Funktion, Telefon, E-Mail]

Datenschutzbeauftragter (sofern bestellt): [Name, Telefon, E-Mail]

---

2 Art der Datenschutzverletzung (Art. 33 Abs. 3 lit. a DSGVO)

[Freitext; Beschreibung des Vorfalls: Was ist geschehen? Wann wurde die Verletzung entdeckt? Wann ist sie eingetreten? Wie wurde sie entdeckt? Falls noch nicht vollständig aufgeklärt: bisheriger Erkenntnisstand.]

Zeitpunkt der Verletzung (soweit bekannt): [TT.MM.JJJJ] bis [TT.MM.JJJJ]
Zeitpunkt der Entdeckung: [TT.MM.JJJJ, HH:MM Uhr]
Zeitpunkt der Kenntnisnahme des Verantwortlichen: [TT.MM.JJJJ, HH:MM Uhr]

Falls die Meldung nicht innerhalb von 72 Stunden erfolgt: Begründung für die Verzögerung:
[Begründung]

---

3 Kategorien und ungefähre Anzahl betroffener Personen (Art. 33 Abs. 3 lit. b DSGVO)

Betroffene Personengruppen: [Kunden / Mitarbeiter / Geschäftspartner / weitere]
Ungefähre Anzahl betroffener Personen: [n]
Kategorien personenbezogener Daten:

- [z. B. Name, E-Mail-Adresse, Telefonnummer]
- [z. B. Zugangsdaten (Passwörter gehasht / Klartext)]
- [z. B. Zahlungsdaten (Kreditkartendaten, IBAN)]
- [z. B. besondere Kategorien nach Art. 9 DSGVO: Gesundheitsdaten, etc. — sofern betroffen]

Ungefähre Anzahl betroffener Datensätze: [n]

---

4 Name und Kontaktdaten des Datenschutzbeauftragten (Art. 33 Abs. 3 lit. b DSGVO)

*Sofern bestellt:*
Name: […]
Telefon: […]
E-Mail: […]

*Sofern nicht bestellt:*
Ein Datenschutzbeauftragter ist nicht bestellt (§ 38 BDSG nicht einschlägig). Ansprechperson: siehe Ziffer 1.

---

5 Voraussichtliche Folgen (Art. 33 Abs. 3 lit. c DSGVO)

[Freitext: mögliche Folgen für die betroffenen Personen, z. B. Identitätsdiebstahl, Phishing, finanzielle Schäden, Rufschädigung, Diskriminierung]

---

6 Ergriffene und geplante Abhilfemaßnahmen (Art. 33 Abs. 3 lit. d DSGVO)

Bereits ergriffene Maßnahmen:
- [Maßnahme 1, z. B. betroffene Systeme isoliert, Zugänge gesperrt]
- [Maßnahme 2, z. B. Passwörter zurückgesetzt, Benutzer informiert]
- [Maßnahme 3, z. B. forensische Untersuchung eingeleitet]

Geplante Maßnahmen zur Schadensbegrenzung:
- [Maßnahme 1]
- [Maßnahme 2]

Geplante Maßnahmen zur Prävention künftiger Verletzungen:
- [z. B. Zwei-Faktor-Authentifizierung einführen, Penetrationstest beauftragen]

---

7 Benachrichtigung betroffener Personen

☐ Benachrichtigung der betroffenen Personen ist geplant (Art. 34 DSGVO) — voraussichtlich hohes Risiko.
☐ Benachrichtigung ist nicht erforderlich — Begründung: [kein hohes Risiko / Maßnahmen nach Art. 34 Abs. 3 lit. a–c DSGVO greifen / Sonstiges].

---

Mit freundlichen Grüßen

[Name, Funktion]
[Unternehmensname]
[Datum, Ort]

---

### TEIL C — BENACHRICHTIGUNG BETROFFENER PERSONEN (ART. 34 DSGVO)

*Nur versenden, wenn die Verletzung voraussichtlich ein hohes Risiko für die betroffenen Personen mit sich bringt (Art. 34 Abs. 1 DSGVO). Ausnahmen nach Art. 34 Abs. 3 DSGVO prüfen.*

**Betreff:** Wichtige Information: Datenschutzvorfall bei [Unternehmensname]

---

Sehr geehrte Damen und Herren,

wir informieren Sie hiermit gemäß Art. 34 DSGVO über eine Datenschutzverletzung, die auch Ihre personenbezogenen Daten betrifft.

**Was ist geschehen?**

Am [Datum] haben wir festgestellt, dass [kurze, verständliche Beschreibung des Vorfalls in einfacher Sprache — keine technischen Details, kein juristisches Kanzleideutsch]. Betroffen ist der Zeitraum von [Datum] bis [Datum].

**Welche Daten sind betroffen?**

Folgende Ihrer personenbezogenen Daten könnten von dem Vorfall betroffen sein:

- [Datenkategorie 1, z. B. Ihr Name und Ihre E-Mail-Adresse]
- [Datenkategorie 2, z. B. Ihr Kundenkonto-Passwort]
- [weitere Kategorien]

**Welche Risiken bestehen?**

[Erläuterung der möglichen Folgen in einfacher Sprache, z. B.:]
Es besteht das Risiko, dass Dritte versuchen, unter Verwendung Ihrer Daten gefälschte E-Mails zu versenden (Phishing) oder Ihr Konto zu missbrauchen.

**Was haben wir unternommen?**

- [Maßnahme 1, z. B. Wir haben den betroffenen Zugang sofort gesperrt.]
- [Maßnahme 2, z. B. Wir haben alle Passwörter zurückgesetzt.]
- [Maßnahme 3, z. B. Wir haben die zuständige Datenschutzbehörde informiert.]

**Was sollten Sie tun?**

Wir empfehlen Ihnen:

1. Ändern Sie umgehend Ihr Passwort bei [unserem Dienst] sowie bei anderen Diensten, bei denen Sie dasselbe Passwort verwenden.

2. Seien Sie vorsichtig bei E-Mails, die angeblich von uns stammen und nach persönlichen Daten fragen. Wir werden Sie **niemals** per E-Mail nach Ihrem Passwort fragen.

3. [weitere konkrete Empfehlung]

**Ihre Rechte**

Sie haben das Recht, bei der zuständigen Datenschutz-Aufsichtsbehörde Beschwerde einzulegen (Art. 77 DSGVO).

Zuständige Behörde: [Name und Kontaktdaten der Aufsichtsbehörde]

Für Fragen wenden Sie sich bitte an:
[Name, Funktion]
E-Mail: [datenschutz@…]
Telefon: […]

Mit freundlichen Grüßen

[Unternehmensname]
[Anschrift]

---

### TEIL D — DOKUMENTATION FÜR DAS VERARBEITUNGSVERZEICHNIS (ART. 33 ABS. 5 DSGVO)

*Auch bei kein-Risiko-Verletzungen muss eine interne Dokumentation erfolgen.*

| Feld | Inhalt |
|---|---|
| Vorfallsnummer | [IR-JJJJ-NNNN] |
| Datum der Verletzung | [TT.MM.JJJJ] |
| Datum der Entdeckung | [TT.MM.JJJJ] |
| Art der Verletzung | [kurze Beschreibung] |
| Betroffene Daten | [Kategorien] |
| Anzahl betroffener Personen | [n] |
| Risikobeurteilung | ☐ Kein Risiko ☐ Risiko ☐ Hohes Risiko |
| Meldung an Aufsichtsbehörde | ☐ Nein (kein Risiko) ☐ Ja, am: [Datum] |
| Benachrichtigung Betroffener | ☐ Nein ☐ Ja, am: [Datum] |
| Ergriffene Maßnahmen | [kurze Zusammenfassung] |
| Verantwortliche Person | [Name, Funktion] |
| Letzte Aktualisierung | [TT.MM.JJJJ] |

---

Hiermit wird der zuständigen Aufsichtsbehörde nach Art. 33 Abs. 1 DSGVO unverzüglich angezeigt: Es liegt eine Verletzung des Schutzes personenbezogener Daten vor; es wird beantragt, den Eingang der Meldung sowie das Aktenzeichen zu bestätigen.

### Anlage 1 — Prüf- und Bewertungsschema

1. Zweck und Prüfstand

1.1 Dieses Schema prüft vor Versand der Teile B und C, ob die Teile A bis D dieses Dokuments untereinander konsistent, fristgerecht und vollständig sind.

1.2 Vorfallsnummer: [IR-JJJJ-NNNN]; Prüfdatum: [JJJJ-MM-TT, Uhrzeit]; prüfende Person: [Name, Funktion].

2. Fristprüfung entlang des 72-Stunden-Zeitstrahls (Art. 33 Abs. 1 DSGVO)

2.1 Die Zeitpunkte in Teil A (Entdeckung, Kenntnisnahme des Verantwortlichen, Fristablauf) sind mit Belegen unterlegt [Alarm, Ticket, Meldung des Auftragsverarbeiters] und stimmen mit den Zeitangaben in Teil B Ziffer 2 überein.

2.2 Das geplante Meldedatum liegt [innerhalb der Frist / nach Fristablauf — die Verzögerungsbegründung in Teil B Ziffer 2 ist ausgefüllt und tatsachenbasiert].

2.3 Bei laufender Aufklärung ist die Meldung als Erstmeldung mit angekündigter Ergänzungsmeldung gekennzeichnet; der Termin der Ergänzung ist gesetzt: [Datum].

3. Konsistenzprüfung der Risikoentscheidung

3.1 Die Erstbewertung in Teil A Ziffer 3, die Angabe in Teil B Ziffer 7 und die Entscheidung über den Versand des Teils C beruhen auf derselben Risikostufe [kein Risiko / Risiko / hohes Risiko]; Abweichungen sind aufgelöst und begründet.

3.2 Bei Verneinung der Benachrichtigungspflicht ist die Begründung konkret [Verschlüsselungsnachweis / Maßnahmen nach Art. 34 Abs. 3 DSGVO / Risikobewertung] und in Teil D dokumentiert.

3.3 Die Bewertungskriterien folgen den in Teil A benannten Leitlinienkriterien (Suchanker für die Live-Prüfung: EDSA Leitlinien 9/2022 Meldung Datenschutzverletzung).

4. Vollständigkeitsprüfung der Behördenmeldung (Art. 33 Abs. 3 DSGVO)

4.1 Teil B enthält alle Katalogangaben: Beschreibung mit Kategorien und ungefähren Zahlen [Ziffern 2 und 3], Anlaufstelle [Ziffern 1 und 4], voraussichtliche Folgen [Ziffer 5], ergriffene und geplante Maßnahmen [Ziffer 6]; fehlende Angaben sind als nachzureichend gekennzeichnet.

4.2 Die zuständige Aufsichtsbehörde ist anhand der Hauptniederlassung bestimmt, und der Meldeweg [Meldeportal / verschlüsselte E-Mail] ist verifiziert.

5. Verständlichkeitsprüfung der Betroffenenbenachrichtigung

5.1 Teil C beschreibt den Vorfall in klarer und einfacher Sprache nach Art. 34 Abs. 2 in Verbindung mit Art. 12 Abs. 1 DSGVO; Fachjargon und beschönigende Formulierungen sind entfernt.

5.2 Die Handlungsempfehlungen in Teil C sind konkret und für die betroffenen Datenarten passend [Passwortwechsel / Kontoüberwachung / Warnung vor Phishing]; die zuständige Beschwerdebehörde ist mit Kontaktdaten genannt.

6. Dokumentation und Freigabe

6.1 Teil D ist auch dann vollständig ausgefüllt, wenn keine Meldepflicht bejaht wurde (Art. 33 Abs. 5 DSGVO), und die Incident-Akte [Logs, Forensik, Kommunikation] ist unter [Ablageort] verknüpft.

6.2 Interne Freigaben vor Versand: Datenschutzbeauftragte oder Datenschutzbeauftragter [Name, Datum], Geschäftsleitung [Name, Datum], Kommunikationsstelle [Name, Datum].

6.3 Gesamtbefund: [versandfertig / nachzubessern in: Fundstellen]; Vermerk: [Ort, Datum, Name, Funktion].

---

Lizenz: Apache-2.0 OR MIT.
