# Einwilligungserklärung E-Mail-Marketing (Art. 6 Abs. 1 lit. a DSGVO; § 7 Abs. 2 Nr. 2 UWG; Double Opt-In)

---

Kurz-Hinweis: Diese Vorlage ist unverbindlich, ein experimenteller Text und keine Rechtsberatung. Nutzung nur auf eigene Gewähr, eigene Gefahr und ohne Gewähr. Die ausführlichen Hinweise zu § 43a Abs. 2 BRAO, § 203 StGB, DSGVO sowie Apache-2.0 OR MIT stehen in der README dieser Vorlage.

---

## Vorlage

[WARNHINWEIS — nicht Vertragsbestandteil, nicht mit unterzeichnen]

Diese Vorlage ersetzt nicht die anwaltliche Eigenleistung. Sie liefert das Gerüst, nicht den Fall. Der Anwender bringt den Sachverhalt, die Beweismittel, die taktische Entscheidung und die Verantwortung; die Vorlage bringt Struktur, Sprache und die unbedingt zu prüfenden Stellen. Wer nur Platzhalter füllt, ohne den eigenen Sachverhalt zu durchdenken, hat noch keinen Vertrag, sondern einen Entwurf.

Weitere Hinweise und ausführliche Praxis-Erläuterungen in der README dieser Vorlage.

---

### Rubrum, Einwilligende und Marketingkanal

**Erklärungskopf**

Einwilligende Person: [E-Mail-Adresse, Name soweit erhoben, Double-Opt-In-Zeitpunkt, IP-Protokoll soweit zulässig].

Verantwortliche Anbieterin: [Unternehmen, Anschrift, Datenschutzkontakt, Newsletter- oder Marketingdienst].

Werbekanal und Inhalt: [Newsletter / Produktinformationen / Einladungen, Produktbereich, Widerrufsweg].

Version, Datum und Fassungsstand: [Version], [Datum], [Entwurf / live geschaltet / archiviert].

### TEIL A — OPT-IN-TEXT (Anmeldeformular auf der Website)

**Checkboxtext (nicht vorausgewählt; muss aktiv angehakt werden):**

> ☐ Ich möchte den Newsletter von **[Unternehmensname]** erhalten und stimme zu, dass meine E-Mail-Adresse [ggf.: sowie mein Vorname] zum Versand des Newsletters und zu Werbezwecken für [kurze Produktkategorie, z. B. „unsere Software-Produkte und Dienstleistungen"] verarbeitet werden. Diese Einwilligung kann ich jederzeit per Klick auf den Abmeldelink in jeder Newsletter-E-Mail oder durch Nachricht an [datenschutz@…] widerrufen. Weitere Informationen zur Datenverarbeitung finden Sie in unserer Datenschutzerklärung: [URL Datenschutzerklärung].

**Pflichthinweis unter dem Formular:**

> Kein Spam. Nur relevante Inhalte. Abmeldung jederzeit möglich.

**Technischer Hinweis für die Implementierung:**

- Checkbox darf **nicht** vorausgewählt sein.
- Formulardaten müssen protokolliert werden: Zeitpunkt der Anmeldung, IP-Adresse, Checkboxstatus (Art. 7 Abs. 1 DSGVO — Nachweispflicht).
- Einwilligungstext ist unveränderlich mit dem Zeitpunkt der Einwilligung zu verknüpfen (Versionierung des Einwilligungstexts empfohlen).

---

### TEIL B — BESTÄTIGUNGS-E-MAIL (Double Opt-In, Step 1)

**Betreff:** Bitte bestätigen Sie Ihre Newsletter-Anmeldung

---

Sehr geehrte Damen und Herren,

vielen Dank für Ihre Anmeldung zum Newsletter von **[Unternehmensname]**.

Um Ihre Anmeldung abzuschließen, klicken Sie bitte auf den folgenden Link:

**Newsletter-Anmeldung bestätigen:** [Bestätigungs-URL mit Token]

Dieser Link ist gültig bis: [Datum/Uhrzeit — empfohlen: 24–48 Stunden].

Falls Sie sich nicht angemeldet haben, ignorieren Sie diese E-Mail. Es werden keine weiteren Nachrichten an Sie versandt.

Mit freundlichen Grüßen

[Unternehmensname]
[Anschrift]
[Impressum-URL]
[Datenschutzerklärung-URL]

---

**Technischer Hinweis:**

- Diese E-Mail darf **ausschließlich** der Einwilligungsbestätigung dienen; keine Werbeinhalte (BGH I ZR 164/09).
- Bestätigungstoken: kryptographisch zufällig, mindestens 128 Bit Entropie; nach Bestätigung oder Ablauf löschen.
- Zeitpunkt der Bestätigung und IP-Adresse protokollieren (Nachweis der Einwilligung).
- Bestätigungslink: HTTPS; Token als URL-Parameter oder Pfadbestandteil; serverseitige Validierung.

---

### TEIL C — PFLICHTHINWEIS IN JEDER MARKETING-E-MAIL

*Dieser Text ist als Footer in jede versandte Newsletter-E-Mail einzufügen:*

---

Sie erhalten diese E-Mail, weil Sie sich am [Datum der Anmeldung] mit der E-Mail-Adresse [E-Mail-Adresse] für unseren Newsletter angemeldet haben.

**Abmeldung:** Klicken Sie auf [Abmeldelink] oder antworten Sie mit dem Betreff „Abmeldung", um den Newsletter abzubestellen. Ihre Adresse wird dann unverzüglich aus dem Verteiler gelöscht.

Verantwortlicher: **[Unternehmensname]**, [Anschrift] | Datenschutzerklärung: [URL Datenschutzerklärung] | Impressum: [URL Impressum]

---

### TEIL D — WIDERRUFS-/ABMELDEBESTÄTIGUNG

**Betreff:** Ihre Newsletter-Abmeldung wurde bestätigt

---

Sehr geehrte Damen und Herren,

Sie haben sich erfolgreich vom Newsletter von **[Unternehmensname]** abgemeldet.

Ihre E-Mail-Adresse wurde aus unserem Verteiler gelöscht. Sie erhalten keine weiteren Newsletter-E-Mails.

Falls Sie sich versehentlich abgemeldet haben, können Sie sich jederzeit erneut auf unserer Website anmelden: [URL]

Die Löschung Ihrer Einwilligungsdaten (Protokoll der Anmeldung) erfolgt nach Ablauf der regulären Aufbewahrungsfristen für Nachweiszwecke (Art. 7 Abs. 1 DSGVO; im Regelfall 3 Jahre nach Widerruf).

Mit freundlichen Grüßen

[Unternehmensname]

---

### Schluss, Unterzeichnung und Zugang

**Erklärende Person:** [vollständiger Name, Rolle]

[Ort], den [Datum]

_____________________________
[Unterschrift, Name, Funktion, Vertretungsrolle]

**Einwilligungsnachweis:** Erklärung abgegeben durch [betroffene Person oder Kennung] am [Datum und Uhrzeit] über [Formular / Double-Opt-in / Papier]; Wortlaut und Bestätigung protokolliert unter [Nachweis-ID].

### Anlage 1 — Checkliste vor Freigabe/Versand

1. Die Checkbox in Teil A ist im Live-Formular nicht vorausgewählt, und die Anmeldung zum Newsletter ist keine Bedingung für einen Vertragsschluss oder Download, oder eine etwaige Kopplung ist am Maßstab des Art. 7 Abs. 4 DSGVO geprüft und dokumentiert.

2. Der Einwilligungstext nennt Verantwortlichen, Werbezweck mit konkreter Produktkategorie, Kanal und Widerrufsweg in verständlicher Sprache; unterschiedliche Zwecke (Newsletter, Produktwerbung, Marktforschung) sind granular trennbar und nicht in einer Sammelklausel gebündelt.

3. Die Double-Opt-In-Strecke ist durchgängig getestet: Anmeldung, Bestätigungs-E-Mail, Token-Validierung und Eintrag in den Verteiler funktionieren, und die Bestätigungs-E-Mail nach Teil B enthält keinerlei Werbeinhalte.

4. Die Nachweisprotokollierung nach Art. 7 Abs. 1 DSGVO ist aktiv: Anmeldezeitpunkt, Bestätigungszeitpunkt, IP-Adressen, Checkboxstatus und die konkrete Version des Einwilligungstexts werden revisionssicher gespeichert.

5. Der Einwilligungstext ist versioniert, und jede Textänderung erzeugt eine neue Version, die künftigen Anmeldungen zugeordnet wird, ohne die Nachweise der Alt-Anmeldungen zu überschreiben.

6. Der Widerruf ist so einfach wie die Erteilung: Der Abmeldelink in Teil C funktioniert in jeder versandten E-Mail, der Versand stoppt unverzüglich, und die Abmeldebestätigung nach Teil D wird ohne Werbeinhalte versandt.

7. Nach der Abmeldung wird die Adresse in eine interne Sperrliste übernommen, damit sie nicht durch spätere Importe erneut angeschrieben wird; die Rechtsgrundlage der Sperrliste und ihre Aufbewahrungsdauer sind dokumentiert.

8. Die verlinkte Datenschutzerklärung erfüllt die Informationspflichten nach Art. 13 DSGVO vollständig für den Newsletterversand: Empfänger (Versanddienstleister), Speicherdauer, Widerrufsrecht, Beschwerderecht und etwaige Drittlandübermittlung.

9. Mit dem Newsletter- oder Marketingdienstleister ist ein Auftragsverarbeitungsvertrag geschlossen, und dessen Drittlandstatus ist geprüft (DPF-Listung oder Standardvertragsklauseln mit Prüfdatum).

10. Eine etwaige Erfolgsmessung im Newsletter (Öffnungs- und Klickraten über Zählpixel) ist im Einwilligungstext oder in der Datenschutzerklärung ausdrücklich erwähnt und am Maßstab des § 25 TDDDG geprüft.

11. Die Verarbeitung ist im Verzeichnis der Verarbeitungstätigkeiten nach Art. 30 DSGVO mit Zweck, Empfängern, Löschfrist und Nachweissystem eingetragen.

12. Werbung an Bestandskunden ohne Einwilligung nach § 7 Abs. 3 UWG (Gesetz gegen den unlauteren Wettbewerb) läuft über eine getrennte Strecke mit dokumentiertem Hinweis bei der Adresserhebung und wird nicht mit dieser Einwilligungsstrecke vermischt.

---

Lizenz: Apache-2.0 OR MIT.
