---
name: kuendigung-per-mandantenkorrespondenz-zugang
description: "Kuendigung PER Mandantenkorrespondenz Zugang: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Kuendigung PER Mandantenkorrespondenz Zugang

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Kuendigung PER Mandantenkorrespondenz Zugang** im Plugin Schriftform/Textform BGB. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `kuendigung-per-schriftsatz-zustellung-formfragen` | Anwalt versendet oder empfängt eine Kündigung per Schriftsatz und fragt nach Formwirksamkeit. Prüft Schriftform, beA, qES, § 130a ZPO, § 130e ZPO, § 46h ArbGG, § 173 ZPO, § 186 ZPO, § 298 Abs. 3 ZPO und § 174 BGB. Output: Form- und Zugangsmatrix mit Zustellungsweg, Vollmachtsrisiko und Empfehlung. |
| `mandantenkorrespondenz-form-und-zugang-templates` | Prüffeld für mandantenkorrespondenz form und zugang templates: prüft Normtext, Nutzerangaben, Fristen, Belege und verifizierte Rechtsprechung mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle. |
| `mandantenwarnung-qes-per-email-whatsapp-und-zugang` | Prüffeld für mandantenwarnung qes per email whatsapp und zugang: prüft Normtext, Nutzerangaben, Fristen, Belege und verifizierte Rechtsprechung mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle. |

## Arbeitsweg

Im Plugin Schriftform/Textform BGB gilt für **Kuendigung PER Mandantenkorrespondenz Zugang**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `kuendigung-per-schriftsatz-zustellung-formfragen`

**Fokus:** Anwalt versendet oder empfängt eine Kündigung per Schriftsatz und fragt nach Formwirksamkeit. Prüft Schriftform, beA, qES, § 130a ZPO, § 130e ZPO, § 46h ArbGG, § 173 ZPO, § 186 ZPO, § 298 Abs. 3 ZPO und § 174 BGB. Output: Form- und Zugangsmatrix mit Zustellungsweg, Vollmachtsrisiko und Empfehlung.

# Kündigung per Schriftsatz — Zustellung und Formfragen

## Rechtsgrundlagen

- **§ 126, § 126a, § 130 BGB** — Schriftform, elektronische Form und Zugang empfangsbedürftiger Willenserklärungen
- **§ 568 BGB, § 623 BGB** — typische Kündigungsformen mit Schriftformerfordernis
- **§ 174 BGB** — Zurückweisung bei fehlender Vollmachtsurkunde
- **§ 130a ZPO** — elektronisches Dokument: qES oder einfache Signatur der verantwortenden Person plus sicherer Übermittlungsweg
- **§ 130d ZPO** — Nutzungspflicht für Rechtsanwälte und andere professionelle Einreicher
- **§ 130e ZPO** — Formfiktion für klar erkennbare Willenserklärungen in vorbereitenden elektronischen Schriftsätzen
- **§ 173 ZPO** — elektronische Zustellung auf sicherem Übermittlungsweg
- **§ 186 ZPO** — Anwalt-zu-Anwalt-Zustellung mit Empfangsbekenntnis
- **§ 46c, § 46g, § 46h ArbGG** — arbeitsgerichtlicher elektronischer Rechtsverkehr und Formfiktion
- **§ 298 Abs. 3 ZPO** — Transfervermerk bei Ausdruck elektronischer Dokumente
- **§ 132 BGB** — Zustellung durch Gerichtsvollzieher als Zugangssurrogat außerhalb des laufenden Prozesses

## BGH-Linie

### Anwaltsbeglaubigung § 169 Abs. 2 ZPO

Wenn ein Rechtsanwalt im Rahmen einer Parteizustellung eine beglaubigte Abschrift eines Schriftsatzes herstellt und dem Gegner zustellt, ist die anwaltliche Beglaubigung nur für den Zustellungsnachweis relevant.

Für die materielle Formwirksamkeit einer Kündigung gilt: Die Beglaubigung durch den Rechtsanwalt ist keine eigenhändige Unterschrift des Kündigenden. Für Schriftform nach § 126 BGB muss entweder der Mandant selbst unterschrieben haben oder der Rechtsanwalt als Bevollmächtigter mit eigener Unterschrift handeln.

### beA und § 130a ZPO

Ein Schriftsatz ist prozessual nach § 130a Abs. 3 ZPO wirksam eingereicht, wenn er entweder qualifiziert elektronisch signiert ist oder von der verantwortenden Person einfach signiert und auf einem sicheren Übermittlungsweg eingereicht wird. Das eigene beA kann also die prozessuale Einreichungsform tragen.

Das ist aber nicht automatisch die materielle elektronische Form nach § 126a BGB. Für § 126a BGB braucht das elektronische Dokument den Namen des Ausstellers und eine qES. Die bloße sichere Übermittlung aus dem beA ersetzt diese qES nicht, solange keine gesetzliche Formfiktion eingreift.

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

Vor § 130e ZPO musste bei einer schriftformbedürftigen Kündigung in einem qES-Schriftsatz geprüft werden, ob die qES-Datei dem Erklärungsempfänger elektronisch mit prüfbarer Signatur zugegangen ist. Ein Ausdruck mit Transfervermerk nach § 298 Abs. 3 ZPO genügte nicht. Auch eine beA-Weiterleitung war nicht allein deshalb ausreichend, weil die Einreichung gegenüber dem Gericht prozessual ordnungsgemäß war. Entscheidend blieb die Verifikationsfunktion gegenüber dem materiell-rechtlichen Empfänger.

### § 130e ZPO — Formfiktion seit 17.07.2024

§ 130e ZPO löst das alte Schriftsatzkündigungsproblem für den Zivilprozess, wenn alle Tatbestandsmerkmale sauber vorliegen:

- empfangsbedürftige Willenserklärung
- gesetzliche oder gewillkürte Schriftform oder elektronische Form
- klare Erkennbarkeit im vorbereitenden Schriftsatz
- Einreichung als elektronisches Dokument nach § 130a ZPO
- Zustellung oder Mitteilung an den Empfänger
- richtiger zeitlicher Anwendungsbereich

Dann gilt die Willenserklärung als in schriftlicher oder elektronischer Form zugegangen. Das gilt nach dem Gesetz auch dann, wenn die Ersetzung der schriftlichen Form durch die elektronische Form ausgeschlossen ist. Deshalb muss der Skill bei arbeitsrechtlichen Kündigungen nach § 623 BGB nicht bei "elektronisch = unwirksam" stehen bleiben, sondern den gesonderten arbeitsgerichtlichen Pfad nach § 46h ArbGG prüfen.

### § 46h ArbGG — arbeitsgerichtliche Formfiktion

Im arbeitsgerichtlichen Verfahren enthält § 46h ArbGG eine parallele Formfiktion. Sie ist besonders relevant für Kündigungen und Aufhebungsangebote in elektronischen vorbereitenden Schriftsätzen. Trotzdem bleiben vier Punkte aktiv zu prüfen:

- Ist die Erklärung im Schriftsatz wirklich klar erkennbar und nicht nur beiläufig erwähnt?
- Ist der Schriftsatz als elektronisches Dokument nach § 46c ArbGG eingereicht?
- Wurde dem richtigen Empfänger zugestellt oder mitgeteilt?
- Kann der Empfänger nach § 174 BGB wegen fehlender Vollmachtsurkunde zurückweisen?

### Transfervermerk § 298 Abs. 3 ZPO

Der Transfervermerk nach § 298 Abs. 3 ZPO dokumentiert die Übertragung eines elektronischen Dokuments in die Papierakte. Er begründet keinen formgerechten Zugang beim materiell-rechtlichen Erklärungsempfänger und ersetzt keine prüfbare qES. Für Alt-Fälle vor § 130e ZPO bleibt das ein zentraler Fehlerpunkt.

## Workflow

### Kündigung per Anwaltsschriftsatz

```
□ Erklärungsträger bestimmen:
 → Mandant erklärt selbst?
 → Rechtsanwalt erklärt als Vertreter?
 → Schriftsatz enthält nur Sachvortrag oder eine echte Willenserklärung?

□ Formquelle bestimmen:
 → Wohnraumkündigung § 568 BGB
 → Arbeitskündigung oder Aufhebungsvertrag § 623 BGB
 → andere Schriftform oder elektronische Form
 → vertragliche Form nach § 127 BGB

□ Direkte Form prüfen:
 → Papieroriginal mit eigenhändiger Unterschrift?
 → qES-Datei nach § 126a BGB?
 → nur einfache Signatur plus beA?

□ Zugang prüfen:
 → Papieroriginal beim Empfänger?
 → qES-Datei beim Empfänger mit prüfbarer Signatur?
 → gerichtliche Zustellung oder Mitteilung?
 → Anwalt-zu-Anwalt-Zustellung mit eEB?

□ Formfiktion prüfen:
 → Zivilprozess: § 130e ZPO seit 17.07.2024
 → Arbeitsgericht: § 46h ArbGG seit 17.07.2024
 → andere Prozessordnungen nur bei ausdrücklicher Grundlage

□ Vollmacht prüfen:
 → Vertretung offengelegt?
 → Originalvollmacht beigefügt oder entbehrlich?
 → Zurückweisung nach § 174 BGB unverzüglich möglich?
```

### Ergebnisbaustein

```
Die Erklärung ist nicht allein deshalb formwirksam, weil sie über das beA
eingereicht oder zugestellt wurde. Zuerst ist zu trennen:

1. prozessuale Einreichungsform nach § 130a ZPO bzw. § 46c ArbGG,
2. materielle Form nach §§ 126, 126a BGB oder Spezialnorm,
3. Zugang nach § 130 BGB,
4. Formfiktion nach § 130e ZPO bzw. § 46h ArbGG.

Trägt die Formfiktion, gilt die Willenserklärung als in schriftlicher oder
elektronischer Form zugegangen. Trägt sie nicht, bleibt es bei der direkten
Formprüfung: Papieroriginal oder qES-Datei mit prüfbarem elektronischem
Zugang.
```

## Templates

### Anschreiben bei Kündigung durch Rechtsanwalt als Bevollmächtigten

```
[Briefkopf Kanzlei]

[Ort, Datum]

Sehr geehrte(r) Herr/Frau [Name],

im Auftrag und in Vollmacht unseres Mandanten erklären wir hiermit die
ordentliche Kündigung des Vertragsverhältnisses zum [Datum].

Die Bevollmächtigung wird offengelegt. Eine Vollmachtsurkunde ist beigefügt,
soweit sie nach § 174 BGB erforderlich ist.

Mit freundlichen Grüßen
[Unterschrift Rechtsanwalt]

Anlage: Vollmachtsurkunde
```

### Hinweis bei § 174 BGB-Zurückweisung

```
Wir weisen die durch Herrn/Frau Rechtsanwalt/Rechtsanwältin [Name]
erklärte Kündigung vom [Datum] unverzüglich zurück, weil uns keine
Vollmachtsurkunde im Original vorgelegt wurde (§ 174 Satz 1 BGB).
```

## Fallstricke

- **Keine Vollmacht vorgelegt**: Kündigung durch Vertreter ohne Originalvollmacht kann nach § 174 BGB unverzüglich zurückgewiesen werden.
- **qES des Rechtsanwalts ist nicht automatisch qES des Mandanten**: Entscheidend ist, wer die Erklärung abgibt und ob Vertretung offengelegt ist.
- **beA ohne qES**: Eine einfache Signatur plus beA kann § 130a ZPO erfüllen, aber nicht automatisch § 126a BGB. Erst § 130e ZPO oder § 46h ArbGG kann die materielle Formfrage über eine gesetzliche Fiktion lösen.
- **§ 130e ZPO nicht als Zustellungsnorm missverstehen**: Die Norm fingiert Form und Zugang der Willenserklärung, wenn Zustellung oder Mitteilung ordnungsgemäß erfolgt ist. Sie ersetzt keine bereitgestellten Lehrmaterialien und keine verifizierte Quellenarbeit.
- **Andere Prozessordnungen**: VwGO, SGG, FGO, FamFG und StPO haben eigene ERV-Regeln. Eine Formfiktion wie § 130e ZPO nur anwenden, wenn die jeweilige Prozessordnung sie ausdrücklich enthält oder eindeutig verweist.

## Querverweise

- → `zugang-formgerechter-erklaerung-bgh-viii-zr-159-23`
- → `zugang-empfangsbeduerftiger-willenserklaerung-paragraph-130-bgb`
- → `wohnraummiete-kuendigung-paragraph-568-bgb`
- → `elektronische-form-paragraph-126a-bgb-qes`
- → `prozessablauf-papier-vs-elektronisch`

## 2. `mandantenkorrespondenz-form-und-zugang-templates`

**Fokus:** Prüffeld für mandantenkorrespondenz form und zugang templates: prüft Normtext, Nutzerangaben, Fristen, Belege und verifizierte Rechtsprechung mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle.

# Mandantenkorrespondenz — Form und Zugang: Templates

## Fachkern: Mandantenkorrespondenz — Form und Zugang: Templates

- **Spezialfrage (Mandantenkorrespondenz — Form und Zugang: Templates):** Prüffeld für mandantenkorrespondenz form und zugang templates: prüft Normtext, Nutzerangaben, Fristen, Belege und verifizierte Rechtsprechung mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle.
- **Arbeitsweise:** Erst Sachverhalt, Norm, Frist, Zuständigkeit und Beweis klären; Rechtsprechung nur verifiziert als tragenden Beleg einsetzen.


## Rechtsgrundlagen

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- §§ 126a, 126b, 130, 568, 656a BGB

## Templates

### Template 1 — Mandantenbrief Mieter: qES-E-Mail nicht löschen

```
[Briefkopf Kanzlei]

[Ort, Datum]

Vertraulich / Persönlich

Herrn/Frau [Name Mieter]
[Adresse]

Betreff: Wichtiger Hinweis — Kündigung per E-Mail mit digitaler Signatur möglich

Sehr geehrte(r) Herr/Frau [Name],

wir möchten Sie auf eine aktuelle Entwicklung in der Rechtsprechung hinweisen,
die unmittelbar Ihr Mietverhältnis betreffen kann.

Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
wirksam per E-Mail erklärt werden kann, wenn das angehängte PDF-Dokument mit einer
qualifizierten elektronischen Signatur (qES) versehen ist.

Was bedeutet das für Sie?

Ihr Vermieter kann künftig eine wirksame Kündigung per E-Mail-Anhang an Sie
übermitteln. Die Kündigung gilt als zugegangen, sobald die E-Mail in Ihrem
Postfach eingegangen ist — unabhängig davon, ob Sie sie gelesen haben.

Bitte beachten Sie daher:

1. Prüfen Sie Ihr E-Mail-Postfach regelmäßig, einschließlich des Spam-Ordners.

2. Löschen Sie PDF-Anhänge von Ihrem Vermieter oder dessen Rechtsanwalt nicht.

3. Prüfen Sie PDF-Anhänge in Adobe Acrobat Reader auf eine
 Signaturmarkierung (blaues oder grünes Zertifikatsfeld).

4. Wenn Sie eine mögliche Kündigung erhalten haben, kontaktieren Sie
 uns unverzüglich.

5. Sichern Sie alle relevanten E-Mails und PDF-Dateien durch Export
 oder Screenshot.

Wir stehen Ihnen für Rückfragen jederzeit zur Verfügung.

Mit freundlichen Grüßen

[Kanzleiname]
[Unterschrift]
[Kontaktdaten]
```

### Template 2 — Mandantenbrief Vermieter: Empfehlung Papier per Boten

```
[Briefkopf Kanzlei]

[Ort, Datum]

Herrn/Frau [Name Vermieter]
[Adresse]

Betreff: Kündigung des Mietverhältnisses — Formempfehlung

Sehr geehrte(r) Herr/Frau [Name],

für die von Ihnen beabsichtigte Kündigung des Mietverhältnisses
über die Wohnung [Adresse] empfehlen wir folgendes Vorgehen:

Empfohlene Vorgehensweise (Papier per Boten):

1. Wir bereiten die Kündigung schriftlich vor und legen sie Ihnen
 zur eigenhändigen Unterzeichnung vor.

2. Sie übergeben das unterschriebene Original persönlich oder durch
 einen Boten an den Mieter. Der Mieter bestätigt den Empfang durch
 Unterschrift auf einer Quittung.

3. Alternativ: Übergabe durch Einschreiben mit Rückschein.

Warum empfehlen wir Papier?

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
per E-Mail mit qualifizierter elektronischer Signatur (qES) grundsätzlich
möglich. Jedoch bestehen praktische Risiken:

- Der Zugangsnachweis ist bei E-Mail schwieriger zu führen.
- Spam-Filter können die E-Mail vom Mieter abfangen.
- Der Mieter könnte bestreiten, die E-Mail erhalten zu haben.

Die Kündigung per Papier mit Boten-Quittung ist die sicherste Methode.

Bitte vereinbaren Sie zeitnah einen Termin zur Unterzeichnung der Kündigung.

Mit freundlichen Grüßen

[Kanzleiname]
[Unterschrift]
```

### Template 3 — Mandantenbrief Mieter: qES-Anhang prüfen (Checkliste)

```
[Briefkopf Kanzlei]

[Ort, Datum]

CHECKLISTE: Mögliche qES-Kündigung erhalten?

Wenn Sie eine E-Mail oder WhatsApp-Nachricht mit PDF-Anhang von Ihrem
Vermieter oder dessen Anwalt erhalten haben, prüfen Sie bitte:

SCHRITT 1: Öffnen Sie die PDF-Datei in Adobe Acrobat Reader (kostenlos).

SCHRITT 2: Sehen Sie im Dokument ein blaues oder grünes Banner mit
 "Signiert und alle Signaturen sind gültig" oder ähnlichem?
 → Wenn JA: Es könnte sich um eine rechtlich wirksame Kündigung handeln.

SCHRITT 3: Prüfen Sie, ob das Dokument eine Kündigung des Mietverhältnisses
 enthält und auf welches Datum die Kündigung verweist.

SCHRITT 4: Sichern Sie die E-Mail und die PDF-Datei.
 → E-Mail: als PDF drucken oder .eml exportieren
 → PDF: auf Ihrem Computer und auf einem USB-Stick oder Cloud speichern
 → Screenshot der E-Mail anfertigen

SCHRITT 5: Kontaktieren Sie uns unverzüglich mit:
 → Weiterleitung der E-Mail an [Kanzlei-E-Mail]
 → Datum des Eingangs der E-Mail
 → Inhalt des PDF (Scan oder Weiterleitung der Datei)

Wichtig: Reagieren Sie schnell — Kündigungsfristen und Reaktionsfristen
laufen ab Zugang der Kündigung.

[Kanzleiname, Kontaktdaten]
```

### Template 4 — Checkliste Maklervertrag-E-Mail (Käufer)

```
CHECKLISTE — Maklervertrag per E-Mail (§ 656a BGB)

Haben Sie einen Maklervertrag für den Kauf einer Wohnung oder eines
Einfamilienhauses per E-Mail geschlossen?

Bitte prüfen Sie:

□ Hat der Makler Ihnen per E-Mail ein Angebot über den Maklerauftrag gemacht?
 → Enthielt die E-Mail: Name des Maklers, Provisionsangebot, Auftragsbeschreibung?

□ Haben Sie den Auftrag per E-Mail bestätigt?
 → Enthielt Ihre E-Mail: Ihren Namen, Ihre Bestätigung des Auftrags?

□ Ist aus dem E-Mail-Austausch erkennbar, dass ein Vertrag geschlossen wurde?

□ Gibt es Anzeichen, dass kein Textform-konformer Vertrag vorliegt?
 → Nur mündliche Absprachen per Telefon?
 → Nur unverbindliche Anfragen ohne klare Beauftragung?

Bedeutung:

Wenn die Textform des § 656a BGB nicht gewahrt wurde, ist der
Maklervertrag nichtig. Der Makler kann keine Provision verlangen.
Eine bereits gezahlte Provision können Sie möglicherweise zurückfordern.

Bitte schicken Sie uns den vollständigen E-Mail-Verlauf zur Prüfung.

[Kanzleiname, Kontaktdaten]
```

### Template 5 — Hinweisschreiben Vermieter: qES-Kündigung per E-Mail (wenn gewählt)

```
[Briefkopf]

Betreff: Kündigung Wohnraummietverhältnis [Adresse] — qES-Dokument

Sehr geehrte(r) Herr/Frau [Name Mieter],

anbei erhalten Sie die Kündigung des Mietverhältnisses über die
Wohnung [Adresse] als PDF-Dokument.

Das Dokument ist mit einer qualifizierten elektronischen Signatur
nach § 126a BGB versehen, die die gesetzliche Schriftform des
Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

Bitte beachten Sie:

- Die Kündigung gilt mit Eingang dieser E-Mail in Ihrem Postfach als zugegangen.
- Prüfen Sie die elektronische Signatur in Adobe Acrobat Reader oder
 unter validator.bund.de.
- Drucken Sie das Dokument aus und bewahren Sie die elektronische Datei auf.

Bitte bestätigen Sie den Empfang dieser E-Mail durch kurze Rückantwort.

Die Kündigung wird zum [Datum] wirksam. Wir bitten Sie, die Wohnung
bis zu diesem Termin geräumt zu übergeben.

Mit freundlichen Grüßen
[Vermieter / Kanzlei]
```

## Fallstricke

- **Template nie ungeprüft verwenden**: Alle Templates sind Mustertexte, die auf den Einzelfall angepasst werden müssen. Fristen, Namen und Daten sind zwingend zu ergänzen.
- **Mandantenbrief ≠ Rechtsgutachten**: Die Mandantenbriefe ersetzen keine vollständige rechtliche Beratung. Bei komplexen Sachverhalten ist ein ausführlicheres Beratungsschreiben erforderlich.
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Querverweise

- → `mandantenwarnung-qes-per-email-whatsapp-und-zugang`
- → `wohnraummiete-kuendigung-paragraph-568-bgb`
- → `maklervertrag-paragraph-656a-bgb-textform-bgh-i-zr-202-25`
- → `dokumentations-und-beweisarchitektur`
- → `prozessablauf-papier-vs-elektronisch`

## 3. `mandantenwarnung-qes-per-email-whatsapp-und-zugang`

**Fokus:** Prüffeld für mandantenwarnung qes per email whatsapp und zugang: prüft Normtext, Nutzerangaben, Fristen, Belege und verifizierte Rechtsprechung mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle.

# Mandantenwarnung: qES per E-Mail und WhatsApp — Zugang im Mietverhältnis

## Fachkern: Mandantenwarnung: qES per E-Mail und WhatsApp — Zugang im Mietverhältnis

- **Spezialfrage (Mandantenwarnung: qES per E-Mail und WhatsApp — Zugang im Mietverhältnis):** Prüffeld für mandantenwarnung qes per email whatsapp und zugang: prüft Normtext, Nutzerangaben, Fristen, Belege und verifizierte Rechtsprechung mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle.
- **Arbeitsweise:** Erst Sachverhalt, Norm, Frist, Zuständigkeit und Beweis klären; Rechtsprechung nur verifiziert als tragenden Beleg einsetzen.


## Rechtsgrundlagen

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- **§ 568 Abs. 1 BGB** — Schriftform Wohnraummiete-Kündigung
- **§ 126a Abs. 1 BGB** — qES als Schriftformersatz
- **§ 130 Abs. 1 BGB** — Zugang empfangsbedürftiger Willenserklärungen

## BGH-Linie

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

**Folge für die Praxis**: Vermieter können künftig wirksame Kündigungen per E-Mail-Anhang (PDF mit qES) oder ggf. per WhatsApp-Dateianhang übermitteln. Mieter, die solche digitalen Nachrichten ignorieren, löschen oder nicht zur Kenntnis nehmen, riskieren, dass eine wirksame Kündigung bereits zugegangen ist.

## Workflow

### Was Mieter jetzt tun müssen

```
1. E-Mail-Postfach regelmäßig prüfen (auch Spam-Ordner)
2. Unbekannte Absender mit Dateianhängen (PDF) nicht vorschnell löschen
3. PDF-Anhänge öffnen und auf qES-Signaturanzeige achten
 (in Adobe Acrobat Reader: blaues Signaturfeld oder Zertifikats-Panel)
4. Bei qES-Kündigung: sofort anwaltlichen Rat einholen
5. Datei sichern — nicht löschen, nicht bloß ausdrucken
6. WhatsApp-Dateianhänge ebenfalls sichern (Backup aktivieren)
```

### Wie Vermieter qES-Kündigung richtig zustellen

```
1. Kündigungsschreiben als PDF/A erstellen
2. qES über qualifizierten Anbieter anbringen (nicht FES/einfache Signatur)
3. PDF-Datei per E-Mail als Anhang an Mieter senden
4. In der E-Mail ausdrücklich darauf hinweisen, dass ein rechtliches
 Dokument mit qualifizierter elektronischer Signatur beigefügt ist
5. Eingangsbestätigung anfordern
6. Sendebericht / Auslieferungsnachweis sichern
7. Alternativ: zusätzlich Papierkündigung mit Originalunterschrift per Boten
```

## Templates

### Mandantenmemo Mieter — Warnung qES-Kündigung per E-Mail

```
MANDANTENMEMO — VERTRAULICH

An: [Name Mieter]
Von: [Kanzleiname]
Datum: [Datum]
Betreff: Achtung — Wohnraumkündigung kann künftig wirksam per E-Mail zugehen

Sehr geehrte(r) Frau/Herr [Name],

nach live verifizierter Rechtsprechung zu elektronischer Form, qES und Zugang
Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
Wohnraumkündigung wirksam per E-Mail oder WhatsApp übermitteln, wenn
er dabei eine qualifizierte elektronische Signatur (qES) verwendet.

Was bedeutet das für Sie?

- Eine E-Mail von Ihrem Vermieter (oder dessen Anwalt) mit einem
 PDF-Anhang kann eine wirksame Kündigung enthalten.
- Die Kündigung gilt als zugegangen, sobald die E-Mail in Ihrem
 Postfach eingegangen ist — auch wenn Sie sie noch nicht gelesen haben.
- Sie müssen Ihren E-Mail-Spam-Ordner regelmäßig prüfen.
- WhatsApp-Dateianhänge ebenfalls beachten.

Was sollten Sie tun?

- Öffnen Sie alle PDF-Anhänge von Ihrem Vermieter oder dessen Anwalt.
- Prüfen Sie, ob das PDF eine Signaturmarkierung enthält (sichtbar in
 Adobe Acrobat Reader als blaues/grünes Zertifikatsfeld).
- Löschen Sie solche E-Mails und Dateien NICHT.
- Kontaktieren Sie uns umgehend, wenn Sie eine mögliche Kündigung
 erhalten haben.

Wir empfehlen, Ihren E-Mail-Posteingang und WhatsApp-Verlauf auf
solche Nachrichten hin zu überprüfen und uns bei Unsicherheit sofort
zu kontaktieren.

Mit freundlichen Grüßen
[Kanzleiname]
```

### Mandantenmemo Vermieter — Empfehlung Kündigung

```
MANDANTENMEMO — VERTRAULICH

An: [Name Vermieter]
Von: [Kanzleiname]
Datum: [Datum]
Betreff: Kündigung Wohnraummietverhältnis — Formempfehlung 2025/2026

Sehr geehrte(r) Frau/Herr [Name],

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
des Wohnraummietverhältnisses per qualifizierter elektronischer Signatur
(qES) erklären, wenn das qES-Dokument dem Mieter so digital zugeht,
dass er die Signatur prüfen kann.

Unsere Empfehlung in der Reihenfolge der Sicherheit:

Option A (sicherste Methode):
 Papierkündigung mit eigenhändiger Unterschrift, übergeben durch
 einen Boten gegen schriftliche Empfangsquittung.

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
 PDF mit qES per E-Mail an den Mieter. Eingangsbestätigung anfordern.
 Sendebericht aufbewahren. Hinweistext in der E-Mail einfügen.

Option C (vermeiden):
 Nur Papierdruck der qES-Kündigung — der Mieter erhält damit kein
 prüfbares Dokument. Zugang der Schriftform fraglich.

Wir stehen für weitere Beratung zur Verfügung.

Mit freundlichen Grüßen
[Kanzleiname]
```

### IT-Hinweis: qES in PDF prüfen (Anleitung für Mandanten)

```
Schritt-für-Schritt: qES in PDF-Datei erkennen

1. Öffnen Sie die PDF-Datei mit Adobe Acrobat Reader (kostenlos).
2. Achten Sie auf ein blaues oder grünes Banner oben oder ein
 Signaturfeld im Dokument.
3. Klicken Sie auf das Signaturfeld oder "Signaturen" im Menü.
4. Prüfen Sie: Ist das Zertifikat gültig? Ist der Name des
 Unterzeichners korrekt?
5. Alternativ: Laden Sie die Datei auf validator.bund.de hoch.
 (Kostenloser Signaturprüfdienst der Bundesverwaltung.)

Wenn Sie unsicher sind: Senden Sie uns die Datei per E-Mail.
Löschen Sie die Datei NICHT, bevor wir sie geprüft haben.
```

## Fallstricke

- **Mieter löscht qES-E-Mail als Spam**: Kündigung kann trotzdem zugegangen sein, wenn E-Mail im Postfach eingegangen war. Spam-Filter schützt nicht vor Zugang.
- **WhatsApp ohne Cloud-Backup**: WhatsApp-Dateien sind nach Geräteverlust oder App-Löschung weg. Mieter sollten Auto-Backup aktivieren oder Dateien separat sichern.
- **Fehlende qES erkannt**: Wenn das PDF keine prüfbare qES enthält, ist die Schriftform nicht gewahrt — Kündigung formunwirksam. Diesen Einwand unverzüglich gegenüber dem Vermieter erheben.
- **Frist versäumt durch Ignorieren der E-Mail**: Selbst wenn der Mieter die E-Mail nicht gelesen hat, beginnt die Frist für ggf. erforderliche Handlungen ab Zugang zu laufen.

## Querverweise

- → `zugang-formgerechter-erklaerung-bgh-viii-zr-159-23`
- → `wohnraummiete-kuendigung-paragraph-568-bgb`
- → `elektronische-form-paragraph-126a-bgb-qes`
- → `dokumentations-und-beweisarchitektur`
- → `mandantenkorrespondenz-form-und-zugang-templates`
