# Custody-Policy für Kryptoverwahrung nach MiCAR

[WARNHINWEIS — nicht Vertragsbestandteil, nicht mit unterzeichnen]

Diese Vorlage ersetzt nicht die anwaltliche Eigenleistung. Sie liefert das Gerüst, nicht den Fall. Der Anwender bringt den Sachverhalt, die Beweismittel, die taktische Entscheidung und die Verantwortung; die Vorlage bringt Struktur, Sprache und die unbedingt zu prüfenden Stellen. Wer nur Platzhalter füllt, ohne den eigenen Sachverhalt zu durchdenken, hat noch kein verwendbares Dokument, sondern einen Entwurf.

Weitere Hinweise und ausführliche Praxis-Erläuterungen in der README dieser Vorlage.

---

Kurz-Hinweis: Diese Vorlage ist unverbindlich, ein experimenteller Text und keine Rechtsberatung. Nutzung nur auf eigene Gewähr, eigene Gefahr und ohne Gewähr. Die ausführlichen Hinweise zu § 43a Abs. 2 BRAO, § 203 StGB, DSGVO sowie Apache-2.0 OR MIT stehen in der README dieser Vorlage.

Interne Verwahrungsrichtlinie für die Verwahrung und Verwaltung von Kryptowerten für Kunden.

---

### Rubrum, Freigabe, Institut und Dokumentenstand

Institut oder CASP: [Firma, Sitz, Register, BaFin-Geschäftszeichen].

Verantwortlich für die Policy: [Geschäftsleiter, Ressort, Funktion].

Betroffene Dienstleistung: Verwahrung und Verwaltung von Kryptowerten für Kunden nach Art. 75 MiCAR.

Fassung: [Version], freigegeben am [Datum] durch [Gremium].

## 1. Verwahrmodell und Geltungsbereich

1.1 Diese Custody-Policy gilt für die Verwahrung und Verwaltung von Kryptowerten für Kunden durch [Firma]. Sie erfasst [Kryptowerte, Netzwerke, Wallet-Typen, Kundengruppen] und gilt für alle Mitarbeitenden, Systeme, Dienstleister und Sub-Custodians, die Zugriff auf Kundenkryptowerte oder Zugriffsmittel haben.

1.2 Das Verwahrmodell beruht auf [Omnibus-Wallet mit internem Positionsregister / segregierten Kunden-Wallets / MPC-Modell / Cold-Wallet-Modell / Hybridmodell]. Die konkrete Zuordnung jeder Kundenposition erfolgt im Positionsregister nach Abschnitt 3.

1.3 Nicht erfasst sind [Eigenbestände / nicht unterstützte Token / DeFi-Protokolle / Staking / Lending / nicht verwahrte Non-Custodial-Wallets], soweit diese nicht gesondert freigegeben werden.

## 2. Kundenvertrag und Kundeninformation

2.1 Der Kundenvertrag beschreibt Dienstleistung, Verwahrmodell, Sicherheitsmodell, Gebühren, Kommunikationswege, Weisungs- und Authentifizierungsverfahren, anwendbares Recht, Beschwerdeverfahren und Rückgabeverfahren.

2.2 Kunden erhalten vor Vertragsschluss eine Zusammenfassung dieser Custody-Policy in elektronischer Form. Die Zusammenfassung erklärt, wie Kundentrennung, Schlüsselkontrolle, Auszüge, Forks, Airdrops, Rückgabe und Haftung behandelt werden.

2.3 Änderungen an der Custody-Policy werden Kunden mitgeteilt, wenn sie Verwahrmodell, Rückgabemöglichkeiten, Gebühren, Haftung, Sub-Custody oder Sicherheit wesentlich betreffen.

## 3. Positionsregister und Kundentrennung

3.1 Für jeden Kunden wird eine Position eröffnet, die Kryptowert, Menge, Netzwerk, Wallet-Zuordnung, Rechtsgrund, Sperren, Transaktionen und Bewertungsinformation enthält.

3.2 Jede Bewegung wird unverzüglich im Positionsregister erfasst. Die Eintragung enthält Kundenweisung, Authentifizierung, Freigabe, Transaktionskennung, Zeitstempel, Netzwerkstatus und verantwortliche Person oder Systemrolle.

3.3 Kundenkryptowerte werden rechtlich und operativ von Eigenbeständen getrennt. Eigenbestände dürfen nicht auf Kunden-Wallets gehalten werden; Kundenbestände dürfen nicht als Sicherheit, Liquiditätspuffer oder Betriebsvermögen verwendet werden.

3.4 Abstimmungsdifferenzen zwischen Kundenbuch, Wallet-Bestand, Sub-Custody-Auszug und Blockchain-Daten werden täglich klassifiziert. Kritische Differenzen werden binnen [Frist in Bankarbeitstagen] an Geschäftsleitung, Compliance, Informationssicherheit und, soweit meldepflichtig, an die Aufsicht eskaliert. Die Bereinigung wird erst abgeschlossen, wenn Kundenposition, Wallet-Saldo, Transaktionshistorie und Korrekturbuchung wieder übereinstimmen.

## 4. Schlüsselkontrolle und Wallet-Governance

4.1 Private Schlüssel, Seed-Phrasen, MPC-Shares, HSM-Zugänge oder sonstige Zugriffsmittel werden nach dem Rollen- und Berechtigungskonzept in Anlage 1 verwaltet.

4.2 Hot-Wallet-Limite betragen [Betrag oder Prozentwert]. Überschreitungen lösen [automatisierte Rebalancing-Regel / manuelle Genehmigung / Sperre] aus. Cold-Wallet-Transfers erfordern [Vier-Augen-Prinzip / Mehrparteienfreigabe / Geschäftsleiterfreigabe ab Schwelle].

4.3 Schlüsselmaterial wird erzeugt, gespeichert, rotiert, gesichert und vernichtet nach Anlage 2. Jeder Zugriff wird protokolliert und auf Auffälligkeiten geprüft.

## 5. Kundenweisungen und Transaktionsfreigabe

5.1 Kundenweisungen werden nur über [zugelassene Kanäle] angenommen. Vor Ausführung prüft [System oder Funktion] Identität, Berechtigung, Sanktions- und Wallet-Risiko, Plausibilität, Netzwerkstatus und verfügbare Kundenposition.

5.2 Transaktionen ab [Schwelle] oder mit [Risikomerkmal] benötigen zusätzliche Freigabe durch [Funktion]. Eine Freigabe darf nicht durch dieselbe Person erfolgen, die die Transaktion angelegt hat.

5.3 Fehlgeschlagene, verzögerte oder auffällige Transaktionen werden nach Anlage 3 behandelt. Kunden werden informiert, wenn Ausführung, Rückgabe oder Rechteausübung wesentlich beeinträchtigt ist.

5.4 Bei Sanktionstreffern, Wallet-Risiken, fehlerhaften Zieladressen, Fork-Konflikten oder technischen Störungen wird die Weisung nicht stillschweigend ausgeführt. Die Entscheidung wird in der Transaktionsakte mit Risikogrund, Freigabeebene und Kundenkommunikation dokumentiert.

## 6. Forks, Airdrops, Staking und Protokollereignisse

6.1 Änderungen der Distributed-Ledger-Technologie, Forks, Airdrops, Token-Swaps oder sonstige Ereignisse werden bewertet nach technischer Unterstützbarkeit, Rechtslage, Sicherheitsrisiko, steuerlicher Offenheit, Geldwäscherisiko und Kundeninteresse.

6.2 Kunden erhalten neu entstehende Kryptowerte oder Rechte nur nach Maßgabe des Kundenvertrags und dieser Policy. Jede abweichende Behandlung muss vor dem Ereignis vertraglich transparent geregelt sein.

6.3 Staking, Lending, Governance-Voting oder vergleichbare Nutzungen von Kundenkryptowerten finden nur statt, wenn sie gesondert vereinbart, technisch getrennt, risikogeprüft und aufsichtsrechtlich freigegeben sind.

## 7. Auszüge, Rückgabe und Exit

7.1 Kunden erhalten mindestens quartalsweise und auf Anfrage einen elektronischen Auszug mit Kryptowert, Bestand, Wert, Bewegungen und Stichtag.

7.2 Die Rückgabe von Kryptowerten oder Zugriffsmitteln erfolgt über [On-Chain-Transfer / Wallet-Wechsel / interne Umbuchung] binnen [Frist in Bankarbeitstagen], sofern keine gesetzliche Sperre, Sanktionsprüfung, Geldwäscheprüfung oder technische Störung entgegensteht.

7.3 Der Exit-Plan nach Anlage 4 beschreibt, wie Kundenbestände bei Geschäftsaufgabe, Verlust der Zulassung, Dienstleisterausfall, Wallet-Kompromittierung oder Insolvenznähe zurückgegeben oder auf einen autorisierten Anbieter übertragen werden.

## 8. Sub-Custody und Auslagerung

8.1 Sub-Custodians oder andere CASP werden nur eingesetzt, wenn sie autorisiert sind, die erforderliche Dienstleistung zu erbringen, und wenn Vertrag, Prüfungsrechte, Kundentrennung, Haftung, Informationspflichten und Exit geprüft sind.

8.2 Kunden werden über den Einsatz von Sub-Custodians informiert. Die Verantwortung des Instituts für Auswahl, Steuerung und Überwachung bleibt unberührt.

## 9. Haftung, Vorfälle und Kontrolle

9.1 Ein Verlust von Kryptowerten, Zugriffsmitteln oder Kundenrechten wird als Vorfall erfasst, klassifiziert und nach Anlage 5 untersucht. Die Prüfung trennt technische Ursache, menschliches Fehlverhalten, Drittparteienfehler, Netzwerkereignis und nicht zurechenbares Ereignis.

9.2 Das Institut haftet nach Maßgabe des Kundenvertrags und der gesetzlichen Vorgaben für zurechenbare Verluste. Die Schadensbewertung dokumentiert Zeitpunkt, Marktwert, betroffene Kundenposition, Ursache, Mitwirkung Dritter und Wiederherstellungsmöglichkeiten.

9.3 Compliance, Risikocontrolling, Informationssicherheit und Interne Revision prüfen diese Policy mindestens jährlich und anlassbezogen nach Vorfällen, neuen Kryptowerten, neuen Wallet-Modellen oder wesentlichen Dienstleisteränderungen.

9.4 Die Ursachenanalyse zu Verlusten oder Registerabweichungen schließt erst, wenn technische Ursache, Kontrollversagen, Kundenauswirkung, Ersatzentscheidung, Regressprüfung und Maßnahmen gegen Wiederholung dokumentiert sind.

## Anlagen

### Anlage 1 — Rollen- und Berechtigungskonzept

1. Rollen

1.1 Rolle [Name] darf [Berechtigung] nur für [Zweck] ausüben.

1.2 Kritische Rollen werden getrennt in [Anlage, Freigabe, Kontrolle, Revision].

### Anlage 2 — Schlüsselmanagement

1. Erzeugung und Speicherung

1.1 Schlüsselmaterial wird erzeugt mit [Verfahren].

1.2 Speicherung erfolgt in [HSM / MPC / Cold Storage / sonstiges].

2. Rotation und Vernichtung

2.1 Rotation erfolgt bei [Trigger].

2.2 Vernichtung wird dokumentiert durch [Nachweis].

### Anlage 3 — Transaktions- und Vorfallsmatrix

1. Freigabe

1.1 Schwelle [Betrag] erfordert [Freigabe].

1.2 Risikomerkmal [Merkmal] erfordert [Eskalation].

2. Vorfall

2.1 Vorfallklasse [Klasse] löst [Maßnahme] aus.

### Anlage 4 — Rückgabe- und Exit-Plan

1. Rückgabe

1.1 Standardrückgabe: [Frist und Verfahren].

1.2 Sonderfall: [Sperre, Prüfung, technische Störung].

2. Exit

2.1 Auslöser: [Zulassungsverlust, Geschäftsaufgabe, Dienstleisterausfall].

2.2 Zielzustand: [Rückgabe / Übertragung / geordnete Abwicklung].

### Anlage 5 — Verlust- und Haftungsprüfung

1. Erfassung

1.1 Betroffene Position: [Kunde, Kryptowert, Menge, Zeitpunkt].

1.2 Ursache: [technisch, menschlich, Drittpartei, Netzwerk].

2. Bewertung

2.1 Marktwert zum Verlustzeitpunkt: [Betrag in EUR].

2.2 Wiederherstellung: [möglich / nicht möglich / offen].

[Ort], den [Datum]

_____________________________
[Unterschrift Geschäftsleitung, Name, Funktion]

_____________________________
[Unterschrift Compliance oder Informationssicherheit, Name, Funktion]

---

Lizenz: Apache-2.0 OR MIT.
