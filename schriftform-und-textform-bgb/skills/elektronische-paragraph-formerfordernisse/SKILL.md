---
name: elektronische-paragraph-formerfordernisse
description: "Elektronische Paragraph Formerfordernisse: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Elektronische Paragraph Formerfordernisse

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Elektronische Paragraph Formerfordernisse** im Plugin Schriftform/Textform BGB. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `elektronische-form-paragraph-126a-bgb-qes` | Prüffeld für elektronische form paragraph 126a bgb qes: prüft Normtext, Nutzerangaben, Fristen, Belege und verifizierte Rechtsprechung mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle. |
| `formerfordernisse-im-bgb-ueberblick` | Systematik der Formerfordernisse im BGB: gesetzliche vs. gewillkürte Form, §§ 125-129 BGB, Nichtigkeitsfolge § 125 BGB, Heilungsmöglichkeiten, Formhierarchie von Textform bis notarielle Beurkundung — Einstieg und Überblick für die Kanzleipraxis. |
| `gewerberaummiete-paragraph-550-bgb-langzeitform` | Gewerbemieter oder Vermieter fragt: Ist ein laenger als 1 Jahr laufender Gewerberaummietvertrag wegen Schriftform-Verstoß vorzeitig kündbar? § 550 BGB Langzeitform Gewerberaummietvertrag. Prüfraster: Schriftformerfordernis Mietvertraege über 1 Jahr Folge Verstoß ordentliche Kündigung möglich Heilung durch Nachholung Teilnichtigkeit Auflockerungsrechtsprechung. Reformdiskussionen 2025 und 2026. Output: Schriftform-Analyse und Kündigungsrisiko-Einschaetzung. Abgrenzung zu wohnraummiete-kündigung-paragraph-568-bgb (Wohnraum) und kündigung-per-schriftsatz-zustellung-formfragen. |

## Arbeitsweg

Im Plugin Schriftform/Textform BGB gilt für **Elektronische Paragraph Formerfordernisse**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `elektronische-form-paragraph-126a-bgb-qes`

**Fokus:** Prüffeld für elektronische form paragraph 126a bgb qes: prüft Normtext, Nutzerangaben, Fristen, Belege und verifizierte Rechtsprechung mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle.

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


## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.

## 2. `formerfordernisse-im-bgb-ueberblick`

**Fokus:** Systematik der Formerfordernisse im BGB: gesetzliche vs. gewillkürte Form, §§ 125-129 BGB, Nichtigkeitsfolge § 125 BGB, Heilungsmöglichkeiten, Formhierarchie von Textform bis notarielle Beurkundung — Einstieg und Überblick für die Kanzleipraxis.

# Formerfordernisse im BGB — Überblick

## Rechtsgrundlagen

- **§ 125 BGB** — Nichtigkeit wegen Formmangels (gesetzliche Form) / Zweifelsnorm bei gewillkürter Form
- **§ 126 BGB** — Schriftform: eigenhändige Unterschrift auf Urkunde
- **§ 126a BGB** — Elektronische Form: qualifizierte elektronische Signatur (qES)
- **§ 126b BGB** — Textform: lesbare Erklärung auf dauerhaftem Datenträger
- **§ 127 BGB** — Gewillkürte Form: Auslegung der Vereinbarung
- **§ 128 BGB** — Notarielle Beurkundung (gesetzlich)
- **§ 129 BGB** — Öffentliche Beglaubigung

## BGH-Linie

Die BGH-Rechtsprechung unterscheidet strikt zwischen **gesetzlicher Form** (Nichtigkeit ex lege bei Verstoß, § 125 S. 1 BGB) und **gewillkürter Form** (nur Zweifelsregel, § 125 S. 2 BGB, Nichtigkeit nur bei erkennbarem Parteiwillen).

Gesetzliche Formerfordernisse sind eng auszulegen. Eine analoge Anwendung setzt planwidrige Regelungslücke voraus (BGH-Dauerrechtsprechung).

## Workflow

### Schritt 1 — Form-Quelle identifizieren

| Form-Quelle | Konsequenz bei Verstoß |
|-------------|----------------------|
| Gesetzliches Formerfordernis | Nichtigkeit gem. § 125 S. 1 BGB |
| Vertraglich vereinbarte Form | Nichtigkeit nur wenn erkennbarer Willen, § 125 S. 2 BGB |
| Handelsrechtlicher Kaufmann ohne gesetzliche Vorschrift | Formfreiheit als Regel |

### Schritt 2 — Formhierarchie (aufsteigend)

1. **Textform** § 126b BGB — niedrigste Anforderung (E-Mail, SMS, WhatsApp, PDF)
2. **Elektronische Form** § 126a BGB — qualifizierte elektronische Signatur (qES)
3. **Schriftform** § 126 BGB — eigenhändige Unterschrift auf Papier
4. **Öffentliche Beglaubigung** § 129 BGB — Notar beglaubigt Unterschrift
5. **Notarielle Beurkundung** § 128 BGB — Notar beurkundet gesamten Vorgang

### Schritt 3 — Heilungsmöglichkeiten prüfen

Heilung trotz Formmangels ist nur in gesetzlich bestimmten Ausnahmefällen möglich:

- **Grundstückskauf** § 311b Abs. 1 S. 2 BGB: Heilung durch Auflassung und Eintragung
- **GmbH-Anteilsübertragung** § 15 Abs. 4 GmbHG: analog Heilung durch vollständige Erfüllung (streitig)
- **Bürgschaft** § 766 S. 3 BGB: Heilung durch Hauptschuldnertilgung (str.)
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

### Schritt 4 — § 242 BGB Treuwidrigkeitseinwand

Die Berufung auf einen Formmangel kann nach § 242 BGB treuwidrig sein, wenn:
- Der Formmangel von der Partei selbst veranlasst wurde
- Vollzug und berechtigtes Vertrauen ein evidentes Missverhältnis begründen
- Spezielle Schutzzweckerwägungen entgegenstehen

## Templates

### Prüfungsschema Formerfordernis

```
1. Liegt ein gesetzliches Formerfordernis vor?
 → Welche Norm? (§ 126, § 126a, § 126b, § 128, § 129 BGB oder Sondergesetz)
 → Schutzzweck: Warn-, Beweis-, Beratungs-, Identitätsfunktion?

2. Wurde die Form eingehalten?
 → Eigenhändige Unterschrift vorhanden?
 → qES technisch korrekt und zugegangen?
 → Textform: dauerhafter Datenträger, Person erkennbar, Abschluss erkennbar?

3. Wenn Formmangel: Heilung möglich?
 → Gesetzliche Heilungsnorm?
 → § 242 BGB Treuwidrigkeitseinwand vertretbar?

4. Konsequenz: Nichtigkeit (§ 125 S. 1) oder Zweifelsregel (§ 125 S. 2)?
```

## Fallstricke

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- **Digitale Konvergenz**: WhatsApp und E-Mail erfüllen Textform (§ 126b BGB), aber nicht Schriftform (§ 126 BGB). Wer irrtümlich Textform für ausreichend hält, riskiert Nichtigkeit bei gesetzlichem Schriftformerfordernis.
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Querverweise

- → `schriftform-paragraph-126-bgb-eigenhaendige-unterschrift`
- → `elektronische-form-paragraph-126a-bgb-qes`
- → `textform-paragraph-126b-bgb-dauerhafter-datentraeger`
- → `notarielle-beurkundung-und-oeffentliche-beglaubigung`
- → `form-checker-fuer-vertrag-oder-willenserklaerung`

## 3. `gewerberaummiete-paragraph-550-bgb-langzeitform`

**Fokus:** Gewerbemieter oder Vermieter fragt: Ist ein laenger als 1 Jahr laufender Gewerberaummietvertrag wegen Schriftform-Verstoß vorzeitig kündbar? § 550 BGB Langzeitform Gewerberaummietvertrag. Prüfraster: Schriftformerfordernis Mietvertraege über 1 Jahr Folge Verstoß ordentliche Kündigung möglich Heilung durch Nachholung Teilnichtigkeit Auflockerungsrechtsprechung. Reformdiskussionen 2025 und 2026. Output: Schriftform-Analyse und Kündigungsrisiko-Einschaetzung. Abgrenzung zu wohnraummiete-kündigung-paragraph-568-bgb (Wohnraum) und kündigung-per-schriftsatz-zustellung-formfragen.

# Gewerberaummiete § 550 BGB — Langzeitform

## Rechtsgrundlagen

- **§ 550 BGB** — Schriftform bei Mietverträgen über Räume für längere Zeit als ein Jahr: bei Verstoß gilt Vertrag als auf unbestimmte Zeit geschlossen → ordentlich kündbar nach einem Jahr.
- **§ 578 BGB** — Entsprechende Anwendung von § 550 BGB auf Pachtverhältnisse über Grundstücke.
- **§ 126 BGB** — Schriftform: eigenhändige Unterschrift.
- **§ 126a BGB** — Ersatz der Schriftform durch qualifizierte elektronische Signatur (qES) nach eIDAS-VO; bei Mietvertraegen ueber Wohn- und Gewerberaum ueber 1 Jahr seit 2023/2024 praxisrelevant.
- Rechtsprechung BGH XII. ZS (Gewerberaummiete) ist staendige Linie zur Auflockerungsrechtsprechung; konkrete Aktenzeichen vor Schriftsatzverwendung ueber https://dejure.org und https://www.bundesgerichtshof.de pruefen.

## BGH-Linie

### Grundsatz § 550 BGB

Ein Gewerberaummietvertrag, der für länger als ein Jahr abgeschlossen werden soll, muss schriftlich geschlossen werden. Die Schriftform des § 126 BGB ist einzuhalten — also eigenhändige Unterschrift beider Parteien auf einer Urkunde (oder auf gleichlautenden Urkunden).

**Rechtsfolge bei Verstoß**: Der Vertrag gilt als auf unbestimmte Zeit geschlossen und kann nach Ablauf eines Jahres von jeder Partei unter Einhaltung der gesetzlichen Kündigungsfrist ordentlich gekündigt werden (§ 550 S. 1 BGB). Der Vertrag ist nicht nichtig — er ist lediglich so zu behandeln, als wäre er auf unbestimmte Zeit abgeschlossen.

### Urkundeneinheit und Anlagen

Alle wesentlichen Vertragsbestandteile müssen von der Schriftform erfasst sein. Anlagen zum Mietvertrag (Grundrisse, Ausbaustandards, Nachtragvereinbarungen) müssen mit dem Hauptvertrag körperlich verbunden oder zumindest eindeutig in Bezug genommen sein. Lose beigelegte Anlagen ohne Seitenverbindung oder Querverweise gefährden die Schriftform.

**BGH-Dauerrechtsprechung**: Wenn wesentliche Vertragsbestandteile nicht aus der Urkunde selbst oder aus in Bezug genommenen Anlagen ersichtlich sind, ist die Schriftform verletzt.

### Auflockerungsrechtsprechung

Der BGH hat die strenge Schriftformrechtsprechung durch die "Auflockerungsrechtsprechung" gemildert: Ergänzungen und Änderungen des Mietvertrags durch nachträgliche konkludente Vereinbarungen berühren nicht stets die Schriftform des Hauptvertrags, wenn sie von untergeordneter Bedeutung sind.

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

### Reformdiskussion 2025/2026

Es gibt seit Jahren Bestrebungen, § 550 BGB zu reformieren oder die strenge Schriftformrechtsprechung durch Spezialregeln für Gewerberaum abzumildern. Stand 2026: keine abgeschlossene gesetzliche Reform — bestehende Rechtsprechung gilt fort.

## Workflow

### Checkliste Schriftform-Compliance Gewerberaummietvertrag

```
□ Mietvertrag über Räume für länger als ein Jahr?
 → § 550 BGB: Schriftform des § 126 BGB zwingend

□ Unterschriften beider Parteien auf Urkunde?
 → Eigenhändig auf dem Vertragstext
 → Räumlich unter dem gesamten Inhalt

□ Alle wesentlichen Vertragsbestandteile in der Urkunde?
 → Mietzins, Mietdauer, Mietsache, Nebenkosten
 → Anlagen (Grundrisse, Ausbaustandards) in Bezug genommen und verbunden?

□ Nachtragsvereinbarungen schriftlich dokumentiert?
 → Jeder Nachtrag muss ebenfalls Schriftform wahren
 → Mündliche Nebenabreden können § 550 BGB-Problem auslösen

□ Schriftformklausel (qualifiziert) im Vertrag enthalten?
 → Schützt vor Schriftformverlust durch nachträgliche Absprachen
```

### Konsequenzen bei Schriftformverstoß

| Zeitpunkt des Verstoßes | Folge |
|------------------------|-------|
| Vertragsschluss formwidrig | Vertrag gilt als auf unbestimmte Zeit geschlossen |
| Nachtrag formwidrig | Ggf. nur der Nachtrag betroffen oder Hauptvertrag infiziert |
| Partei erkennt Schriftformmangel | Kann ordentlich kündigen (auch wenn dies unbillig erscheint) |
| Gegenpartei beruft sich auf § 242 BGB | Treuwidrigkeitseinwand möglich (hohe Hürden) |

### Heilung des Schriftformmangels

§ 550 BGB kennt keine automatische Heilung. Die Parteien können jedoch:
- Den Vertrag nachträglich in ordnungsgemäßer Schriftform neu beurkunden
- Eine schriftliche Vereinbarung treffen, die den formwidrigen Vertrag in einen formwirksamen umwandelt

## Templates

### Qualifizierte Schriftformklausel (Gewerberaummietvertrag)

```
§ [X] Schriftform

(1) Änderungen und Ergänzungen dieses Vertrages — einschließlich dieser
Klausel — bedürfen der Schriftform gemäß § 126 BGB. Die Schriftform ist
nur durch eigenhändige Unterzeichnung einer gemeinsamen Urkunde oder durch
gegenseitige Unterzeichnung gleichlautender Urkunden gewahrt.

(2) Mündliche Nebenabreden, nachträgliche Vereinbarungen per E-Mail,
Messenger oder Fax sowie Vereinbarungen, die nur durch Beglaubigung
oder Kopie dokumentiert sind, genügen der Schriftform dieses Vertrages
nicht und begründen keine rechtlich bindenden Änderungen des Mietvertrages.

(3) Auf das Schriftformerfordernis kann nur durch ausdrückliche schriftliche
Vereinbarung der Parteien verzichtet werden.
```

### Nachtrag zum Gewerberaummietvertrag (Schriftform-Muster)

```
Nachtrag Nr. [X] zum Mietvertrag vom [Datum] über [Adresse]

zwischen

[Vermieter-Name, Adresse] — nachfolgend "Vermieter" —

und

[Mieter-Name, Adresse] — nachfolgend "Mieter" —

Die Parteien vereinbaren folgende Änderung des oben genannten Mietvertrages:

[Inhalt der Änderung]

Im Übrigen bleibt der Mietvertrag vom [Datum] unverändert bestehen.

[Ort], [Datum]

________________________ ________________________
[Unterschrift Vermieter] [Unterschrift Mieter]
```

## Fallstricke

- **Lose Anlagen**: Anlagen zum Mietvertrag, die nicht fest verbunden sind und nicht eindeutig in Bezug genommen werden, gefährden die Schriftform des gesamten Vertrags. Konsequenz: Vertragspartner kann ordentlich kündigen.
- **Mieterhöhung per E-Mail**: Wird eine Mieterhöhung für einen Langzeitmietvertrag per E-Mail vereinbart, verletzt dies die Schriftform — der Gesamtvertrag kann als auf unbestimmte Zeit geltend behandelt werden.
- **Treuwidrigkeitseinwand**: Die Berufung auf den Schriftformmangel kann nach § 242 BGB treuwidrig sein, wenn die Partei, die sich auf den Mangel beruft, diesen selbst veranlasst hat. Die Hürde ist hoch (BGH-Dauerrechtsprechung).

## Querverweise

- → `schriftform-paragraph-126-bgb-eigenhaendige-unterschrift`
- → `klauselgenerator-formvorbehalt-und-aenderungsvorbehalt`
- → `verteidigungsstrategie-bei-formangriff` (§ 242 BGB Treuwidrigkeitseinwand)
- → `formerfordernisse-im-bgb-ueberblick`
