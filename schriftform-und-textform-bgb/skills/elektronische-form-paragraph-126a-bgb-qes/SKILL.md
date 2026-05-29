---
name: elektronische-form-paragraph-126a-bgb-qes
description: "Workflow-Skill zu elektronische form paragraph 126a bgb qes. Nutzt Normtext, Nutzerangaben und verifizierte Quellen; Rechtsprechung nur nach Live-Pruefung mit Gericht, Datum und Aktenzeichen."
---

# Elektronische Form § 126a BGB — Qualifizierte elektronische Signatur

## Rechtsgrundlagen

- **§ 126a Abs. 1 BGB** — elektronische Form als Ersatz der Schriftform: Name des Ausstellers plus qualifizierte elektronische Signatur
- **§ 126a Abs. 2 BGB** — bei Verträgen: beide Parteien signieren dasselbe elektronische Dokument oder jeweils das für die andere Partei bestimmte gleichlautende Dokument
- **§ 126 Abs. 3 BGB** — Schriftform kann durch elektronische Form ersetzt werden, soweit das Gesetz nichts anderes bestimmt
- **§ 130 BGB** — Zugang empfangsbedürftiger Willenserklärungen
- **§ 130a ZPO** — elektronisches Dokument im Zivilprozess: qES oder einfache Signatur plus sicherer Übermittlungsweg
- **§ 130e ZPO** — Formfiktion für klare Willenserklärungen in vorbereitenden elektronischen Schriftsätzen
- **§ 46h ArbGG** — arbeitsgerichtliche Formfiktion
- **§ 298 Abs. 3 ZPO** — Transfervermerk beim Ausdruck elektronischer Dokumente
- **eIDAS-VO (EU) Nr. 910/2014** — technischer Rahmen der qualifizierten elektronischen Signatur
- **VDG** — deutsches Vertrauensdienstegesetz

## Grundsatz

Die qES ist der direkte elektronische Schriftformersatz. Sie ersetzt keine bereitgestellten Lehrmaterialien und keine verifizierte Quellenarbeit.

## Abgrenzung beA, qES und Formfiktion

| Situation | Prozessual wirksam? | Materielle Form nach § 126a BGB? | Sonderpfad |
|---|---:|---:|---|
| qES-Datei direkt an Empfänger | möglich | ja, wenn qES gültig und Zugang prüfbar | § 126a BGB |
| einfache Signatur plus beA an Gericht | ja nach § 130a ZPO | nein | § 130e ZPO prüfen |
| qES-Schriftsatz bei Gericht | ja | nur bei formgerechtem Zugang der qES-Datei | § 130e ZPO seit 17.07.2024 prüfen |
| Ausdruck mit Transfervermerk | ja für Akte | nein | kein § 126a-Zugang |
| Arbeitsgerichtlicher elektronischer Schriftsatz | ja nach § 46c ArbGG | nicht automatisch | § 46h ArbGG prüfen |

## BGH-Linie

### VIII ZR 155/23 und VIII ZR 159/23

Der BGH hat für Alt-Fälle vor § 130e ZPO klargestellt: Bei einer schriftformbedürftigen Kündigung in einem elektronisch signierten Schriftsatz reicht es nicht, dass der Schriftsatz beim Gericht ordnungsgemäß elektronisch eingereicht wurde. Entscheidend ist, ob das qualifiziert signierte elektronische Dokument dem Erklärungsempfänger so zugeht, dass die Signatur selbst prüfbar bleibt. Ein Papierausdruck mit Transfervermerk wahrt diese Verifikationsfunktion nicht.

### Konsequenz

Bei empfangsbedürftigen Willenserklärungen müssen Abgabe, Signatur und Zugang zusammen geprüft werden. Die beste qES nützt materiellrechtlich wenig, wenn nur eine nicht signierte Kopie, ein Ausdruck oder eine beA-Nachricht ohne formtragende Fiktion beim Empfänger ankommt.

## § 130e ZPO seit 17.07.2024

§ 130e ZPO fingiert den formgerechten Zugang, wenn eine empfangsbedürftige Willenserklärung, die schriftlicher oder elektronischer Form bedarf, klar erkennbar in einem vorbereitenden Schriftsatz enthalten ist, dieser Schriftsatz als elektronisches Dokument nach § 130a ZPO bei Gericht eingereicht und dem Empfänger zugestellt oder mitgeteilt wurde.

Wichtig: Der Schriftsatz muss nicht zwingend eine qES tragen, wenn § 130a ZPO auf anderem Weg erfüllt ist. Eine einfache Signatur plus sicherer Übermittlungsweg aus dem eigenen beA kann prozessual genügen. Die materielle Formwirkung kommt dann nicht aus § 126a BGB, sondern aus § 130e ZPO.

## § 46h ArbGG

Für arbeitsgerichtliche Verfahren gilt § 46h ArbGG als Parallele. Das ist besonders wichtig, weil § 623 BGB die elektronische Form für Kündigungen und Aufhebungsverträge ausschließt. § 46h ArbGG kann dennoch eine Formfiktion auslösen, wenn die Erklärung klar erkennbar in einem elektronischen vorbereitenden Schriftsatz nach § 46c ArbGG enthalten ist und zugestellt oder mitgeteilt wird.

Das macht die direkte elektronische Kündigung per E-Mail oder Signaturplattform nicht wirksam. Es ist ein enger prozessualer Sonderpfad und ersetzt nicht die Prüfung von Vollmacht, § 174 BGB, Zustellung und Klarerkennbarkeit.

## Workflow

### Technische Anforderungen qES

```
qES = qualifizierte elektronische Signatur im Sinne von Art. 3 Nr. 12 eIDAS-VO:
  ├── qualifiziertes Zertifikat
  ├── qualifizierter Vertrauensdiensteanbieter
  ├── qualifizierte Signaturerstellungseinheit
  └── prüfbare Integrität des konkreten Dokuments

Nicht ausreichend:
  - eingescannte Unterschrift
  - Bild einer Unterschrift im PDF
  - einfache elektronische Signatur
  - fortgeschrittene elektronische Signatur ohne qES
  - beA-Versand ohne qES, wenn keine Formfiktion trägt
```

### Zugangs-Checkliste

```
□ Enthält die Datei selbst eine prüfbare qES?
□ Ist genau diese Datei beim Empfänger angekommen?
□ Kann der Empfänger die Signatur technisch prüfen?
□ Ist das Zertifikat zum Signaturzeitpunkt gültig?
□ Gibt es einen belastbaren Zugangsnachweis?
□ Wenn nur Schriftsatzweg: greift § 130e ZPO oder § 46h ArbGG?
□ Wenn Arbeitsrecht: § 623 BGB, § 46h ArbGG und § 174 BGB trennen.
```

## Templates

### Mandantenhinweis qES-Versand

```
Wenn Sie ein Schriftformdokument elektronisch erklären wollen, muss die
qualifiziert elektronisch signierte Datei selbst beim Empfänger ankommen.
Ein Papierausdruck, ein Scan oder eine bloß weitergeleitete Kopie genügt
nicht. Bitte sichern Sie die Originaldatei, das Prüfprotokoll, den
Versandnachweis und eine Empfangsbestätigung.

Wird die Erklärung in einem gerichtlichen Schriftsatz abgegeben, prüfen wir
gesondert, ob § 130e ZPO oder im Arbeitsgericht § 46h ArbGG die Form wahrt.
```

### Klausel qES-Zugang

```
Elektronisch übermittelte Willenserklärungen in gesetzlicher Schriftform
gelten nur dann als in elektronischer Form zugegangen, wenn die mit einer
qualifizierten elektronischen Signatur (§ 126a BGB) versehene Originaldatei
in den Machtbereich des Empfängers gelangt und die Signatur prüfbar bleibt.
Gesetzliche Formfiktionen bleiben unberührt.
```

## Fallstricke

- **Ausdruck vernichtet die Prüfbarkeit**: Der Ausdruck eines qES-Dokuments zeigt den Text, nicht die kryptographisch prüfbare Signatur.
- **beA ist kein qES-Ersatz**: beA kann den sicheren Übermittlungsweg nach § 130a ZPO liefern, aber nicht allein § 126a BGB erfüllen.
- **§ 130e ZPO ist eng**: Die Willenserklärung muss im vorbereitenden Schriftsatz klar erkennbar sein und zugestellt oder mitgeteilt werden.
- **§ 623 BGB bleibt direkt streng**: Kündigung und Aufhebungsvertrag per E-Mail, DocuSign oder beA-Nachricht außerhalb des § 46h ArbGG bleiben riskant bis unwirksam.
- **Verträge brauchen zwei Seiten**: Bei § 126a Abs. 2 BGB muss die Vertragsmechanik beidseitig elektronisch sauber abgebildet sein.

## Querverweise

- → `zugang-formgerechter-erklaerung-bgh-viii-zr-159-23`
- → `kuendigung-per-schriftsatz-zustellung-formfragen`
- → `mandantenwarnung-qes-per-email-whatsapp-und-zugang`
- → `wohnraummiete-kuendigung-paragraph-568-bgb`
- → `dokumentations-und-beweisarchitektur`
