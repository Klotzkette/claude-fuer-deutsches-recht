---
name: kuendigung-per-schriftsatz-zustellung-formfragen
description: "Anwalt versendet oder empfängt eine Kündigung per Schriftsatz und fragt nach Formwirksamkeit. Prüft Schriftform, beA, qES, § 130a ZPO, § 130e ZPO, § 46h ArbGG, § 173 ZPO, § 186 ZPO, § 298 Abs. 3 ZPO und § 174 BGB. Output: Form- und Zugangsmatrix mit Zustellungsweg, Vollmachtsrisiko und Empfehlung."
---

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
