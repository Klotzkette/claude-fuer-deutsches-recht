---
name: klauselgenerator-formvorbehalt-maklervertrag
description: "Klauselgenerator Formvorbehalt Maklervertrag: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Klauselgenerator Formvorbehalt Maklervertrag

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Klauselgenerator Formvorbehalt Maklervertrag** im Plugin Schriftform/Textform BGB. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `klauselgenerator-formvorbehalt-und-aenderungsvorbehalt` | Prüffeld für klauselgenerator formvorbehalt und aenderungsvorbehalt: prüft Normtext, Nutzerangaben, Fristen, Belege und verifizierte Rechtsprechung mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle. |
| `maklervertrag-paragraph-656a-bgb-textform-bgh-i-zr-202-25` | Prüffeld für Maklervertrag, § 656a BGB und Textform. Nutzt Normtext, Nutzerangaben und verifizierte Quellen; behauptete Rechtsprechung zu I ZR 202/25 nie ohne Live-Pruefung zitieren. |
| `amtlicher-formkern-bgb-zpo-check` | Amtlicher Formkern-Check für BGB und ZPO: trennt Schriftform, Textform, elektronische Form, qES, beA/EGVP, § 130e ZPO, Zustellung, Zugang und Beweiskraft elektronischer Dokumente. |

## Arbeitsweg

Im Plugin Schriftform/Textform BGB gilt für **Klauselgenerator Formvorbehalt Maklervertrag**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `klauselgenerator-formvorbehalt-und-aenderungsvorbehalt`

**Fokus:** Prüffeld für klauselgenerator formvorbehalt und aenderungsvorbehalt: prüft Normtext, Nutzerangaben, Fristen, Belege und verifizierte Rechtsprechung mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle.

# Klauselgenerator — Formvorbehalt und Änderungsvorbehalt

## Rechtsgrundlagen

- **§ 126 BGB** — Schriftform
- **§ 126b BGB** — Textform
- **§ 127 BGB** — Gewillkürte Form
- **§ 305b BGB** — Vorrang der Individualabrede vor AGB
- **§ 307 BGB** — Inhaltskontrolle AGB
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## BGH-Linie

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

Der BGH hat im Gewerbemietrecht anerkannt, dass eine qualifizierte Schriftformklausel — die auch mündliche Nebenabreden ausschließt und auch Änderungen der Klausel selbst der Schriftform unterwirft — zulässig ist und die Schriftform des § 550 BGB absichert.

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

Eine doppelte Schriftformklausel in AGB (die auch die Aufhebung der Schriftformklausel der Schriftform unterwirft) ist grundsätzlich zulässig. Sie kann aber § 305b BGB nicht außer Kraft setzen: Individuelle Abreden haben Vorrang vor AGB, auch wenn sie mündlich getroffen wurden. Die doppelte Schriftformklausel schützt nicht vollständig vor mündlichen individuellen Abweichungen — sie schafft aber ein Beweisindiz und eine erhöhte Hürde.

## Klausel-Bibliothek

### Klausel 1 — Einfache Schriftformklausel

```
§ [X] Schriftform

Änderungen und Ergänzungen dieses Vertrages bedürfen zu ihrer Wirksamkeit
der Schriftform gemäß § 126 BGB. Mündliche Absprachen und telefonische
Vereinbarungen genügen nicht.
```

**Anwendung**: Einfache Verträge ohne AGB-Charakter, individuelle Abreden zwischen Kaufleuten oder gewerblichen Parteien.

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

```
§ [X] Schriftform

(1) Änderungen und Ergänzungen dieses Vertrages bedürfen zu ihrer Wirksamkeit
der Schriftform gemäß § 126 BGB. Dies gilt auch für die Aufhebung dieser
Schriftformklausel.

(2) Mündliche Nebenabreden — auch soweit sie vor Abschluss dieses Vertrages
getroffen wurden — sind nur wirksam, wenn sie schriftlich bestätigt werden.

(3) Die vorstehenden Absätze gelten entsprechend für Ergänzungsverträge
und Nachtragsvereinbarungen.

Hinweis für AGB-Kontext: Diese Klausel schließt individuelle mündliche
Abreden nach § 305b BGB nicht aus.
```

**Anwendung**: Gewerbliche Mietverträge, Dienstleistungsverträge, Lizenzverträge.

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

```
§ [X] Schriftform und Vertragsänderungen

(1) Dieser Mietvertrag sowie alle Änderungen, Ergänzungen, Nebenabreden
und Kündigungen bedürfen der Schriftform gemäß §§ 126, 550 BGB.
Die Schriftform ist nur gewahrt, wenn eine gemeinsame Vertragsurkunde
von beiden Parteien eigenhändig unterschrieben ist oder beide Parteien
gleichlautende Einzelurkunden eigenhändig unterzeichnet haben.

(2) Mündliche Nebenabreden — auch vor Vertragsabschluss getroffene —
sind ausgeschlossen und begründen keine rechtlich verbindlichen Änderungen
dieses Vertrages.

(3) Textform (§ 126b BGB), Telefax, E-Mail oder andere elektronische
Kommunikationsmittel genügen dem Schriftformerfordernis dieses Vertrages
nur, wenn zusätzlich eine qualifizierte elektronische Signatur nach
§ 126a BGB beigefügt und dem Empfänger so zugegangen ist, dass er
die Signatur prüfen kann.

(4) Die vorstehende Klausel gilt auch für ihre eigene Änderung oder
Aufhebung.
```

**Anwendung**: Gewerberaummietverträge über mehr als ein Jahr.

### Klausel 4 — Textformklausel (für Maklervertrag oder Mieterhöhung)

```
§ [X] Textform

Erklärungen im Rahmen dieses Vertrages — insbesondere Beauftragungen,
Widerrufe, Angebote und Bestätigungen — können in Textform (§ 126b BGB)
abgegeben werden. Textform ist gewahrt durch lesbare Erklärung auf
einem dauerhaften Datenträger (z. B. E-Mail, PDF), in der die erklärende
Person genannt ist und das Ende der Erklärung erkennbar ist.

Mündliche Erklärungen per Telefon oder persönlichem Gespräch genügen
der Textform nicht.
```

**Anwendung**: Maklerverträge (§ 656a BGB), Mieterhöhungsvereinbarungen, Verbraucherverträge.

### Klausel 5 — Elektronische Form mit qES-Anforderung

```
§ [X] Elektronische Form

Die Parteien vereinbaren, dass Willenserklärungen in elektronischer Form
gemäß § 126a BGB abgegeben werden können. Voraussetzung ist, dass:

(a) das elektronische Dokument mit einer qualifizierten elektronischen
Signatur (§ 126a Abs. 1 BGB i.V.m. Art. 3 Nr. 12 eIDAS-VO) versehen ist,

(b) das Dokument dem Empfänger in einer Form zugeht, die ihm die Prüfung
der qualifizierten elektronischen Signatur ermöglicht — insbesondere als
elektronische Datei per E-Mail oder über eine Plattform, die die Signatur
zugänglich macht; ein bloßer Ausdruck auf Papier genügt nicht.

(c) Eine Eingangsbestätigung des Empfängers ist anzufordern.
```

**Anwendung**: Verträge zwischen Unternehmen, die elektronische Kommunikation vereinbaren wollen.

### Klausel 6 — Schriftformvorbehalt Widerrufsrecht (Verbraucher)

```
Widerrufsbelehrung — Textform des Widerrufs

Ihr Widerruf muss keine bestimmte Form wahren. Sie können den Widerruf
per Brief, Telefax oder E-Mail erklären. Um Ihren Widerruf nachweisen
zu können, empfehlen wir die Erklärung in Textform (E-Mail oder Brief),
in der Sie Ihren Namen und die zu widerrufende Erklärung eindeutig
benennen.
```

## Fallstricke

- **§ 305b BGB Vorrang Individualabrede**: Auch die beste doppelte Schriftformklausel in AGB schützt nicht vollständig vor mündlichen individuellen Abweichungen. Beweis der mündlichen Abrede bleibt beim Behauptenden — die Klausel schafft aber ein erhebliches Beweisindiz.
- **Schriftformklausel selbst in AGB**: Eine Schriftformklausel ist selbst AGB-pflichtig (§ 307 BGB). Sie darf nicht so formuliert sein, dass Verbraucher benachteiligt werden.
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Querverweise

- → `form-checker-fuer-vertrag-oder-willenserklaerung`
- → `gewerberaummiete-paragraph-550-bgb-langzeitform`
- → `elektronische-form-paragraph-126a-bgb-qes`
- → `verteidigungsstrategie-bei-formangriff` (§ 242 BGB vs. Schriftformklausel)

## 2. `maklervertrag-paragraph-656a-bgb-textform-bgh-i-zr-202-25`

**Fokus:** Prüffeld für Maklervertrag, § 656a BGB und Textform. Nutzt Normtext, Nutzerangaben und verifizierte Quellen; behauptete Rechtsprechung zu I ZR 202/25 nie ohne Live-Pruefung zitieren.

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Rechtsgrundlagen

- **§ 656a BGB** — Textform für Maklervertrag über Wohnraumkauf/-verkauf (seit 23.12.2020, Gesetz ueber die Verteilung der Maklerkosten bei der Vermittlung von Kaufvertraegen ueber Wohnungen und Einfamilienhaeuser vom 12.06.2020).
- **§ 656c BGB** — Halbteilungsgrundsatz bei Doppeltaetigkeit.
- **§ 656d BGB** — Halbteilungsgrundsatz bei Anspruchsabwaelzung auf den Kaeufer.
- **§ 126b BGB** — Textform: lesbare Erklärung auf dauerhaftem Datenträger; Person des Erklärenden und Abschluss der Erklärung erkennbar.
- **§ 125 BGB** — Nichtigkeit bei Formverstoß.
- **§ 812 Abs. 1 S. 1 BGB** — Bereicherungsanspruch.

## Rechtsprechung BGH 2025

- BGH, Urt. v. 06.03.2025 – Az. I ZR 32/24 — Halbteilungsgrundsatz § 656c BGB beim Verkauf eines Einfamilienhauses; Definition des Einfamilienhauses; analoge Anwendung auf Maklervertraege mit Dritten. Quelle: https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=06.03.2025&Aktenzeichen=I+ZR+32/24 (BGH-Presseinformation Nr. 44/2025).
- BGH, Urt. v. 06.03.2025 – Az. I ZR 138/24 — Gesamtnichtigkeit der Abwaelzungsvereinbarung bei Verstoss gegen § 656d BGB; kein Anspruch des Maklers gegen den Kaeufer auf die volle Provision. Quelle: https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=06.03.2025&Aktenzeichen=I+ZR+138/24
- BGH, Urt. v. 09.10.2025 – Az. I ZR 159/24 — Maklervertraege ueber Online-Anbahnung ohne Buttonloesung (§ 312j BGB analog) sind im B2C-Verhaeltnis bei fehlender ausdruecklicher Zahlungsbutton-Bestaetigung unwirksam. Quelle: https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=09.10.2025&Aktenzeichen=I+ZR+159/24
- Rechtsprechung zu Az. I ZR 202/25 ist nach offen zugaenglichen Quellen (Stand Mai 2026) nicht als entscheidungstragende BGH-Entscheidung belegt; falls im Mandat darauf abgehoben wird, ueber https://dejure.org und https://www.bundesgerichtshof.de verifizieren und bei fehlendem Treffer nicht zitieren.

## Rechtsprechung live prüfen

### Pflichtprogramm vor jeder Rechtsprechungszitierung

1. Suche in der BGH-Datenbank, bei dejure.org und möglichst zusätzlich in einer frei zugänglichen Gerichtsdatenbank nach Gericht, Datum und Aktenzeichen.
2. Prüfe, ob der gefundene Treffer wirklich § 656a BGB, Textform, Maklerprovision und die konkrete Aussage betrifft.
3. Zitiere nur, wenn Gericht, Entscheidungsform, Datum, Aktenzeichen, Quelle und tragende Aussage zusammenpassen.
4. Wenn ein Aktenzeichen aus einer Mandatsakte nicht auffindbar ist, schreibe offen: "Keine verifizierte Entscheidung gefunden"; dann aus Normtext, Aktenlage und verifizierter Rechtsprechung argumentieren.

### Prüfproblem: Provisionshinweis in E-Mail-Signatur

Ein Provisionshinweis unterhalb der Grußformel, in einer Standardsignatur oder in einem Footer ist nicht automatisch Teil der eigentlichen Vertragserklärung. Der Skill prüft deshalb ohne ungeprüftes BGH-Zitat:

- Steht der Provisionshinweis im eigentlichen Nachrichtentext oder nur in der Signatur?
- Wird im Haupttext auf die Provision ausdrücklich Bezug genommen?
- Sind Parteien, Objekt, Provisionshöhe und Anlass des Hauptvertrags bestimmbar?
- Ist der Abschluss der Erklärung erkennbar?
- Gibt es eine Annahmeerklärung des Kunden auf einem dauerhaften Datenträger?
- Falls die Form fehlt: Welche Folgen ergeben sich aus § 125 BGB, § 812 BGB, § 818 BGB, § 242 BGB und dem Schutzzweck des § 656a BGB?

### Systematische Einordnung

§ 656a BGB wurde durch das Gesetz über die Verteilung der Maklerkosten bei der Vermittlung von Kaufverträgen über Wohnungen und Einfamilienhäuser vom 12. Juni 2020 eingeführt (in Kraft 23.12.2020). Zweck ist der Verbraucherschutz: Käufer sollen vor überraschenden Maklerprovisionen geschützt werden.

**Verhältnis zu § 656c / § 656d BGB**: § 656a BGB regelt die Form; §§ 656c, 656d BGB regeln die Halbteilung der Maklerprovision zwischen Käufer und Verkäufer bei Doppeltätigkeit oder Käuferprovision.

### Praktische Folgen

**Für den Makler (zentral)**: Wer als Makler die Provision rechtssicher haben will, sollte den Provisionshinweis und das Provisionsverlangen innerhalb der eigentlichen Erklärung unterbringen — nicht in einer Signatur, nicht im Footer, nicht unter der Grußformel. Die Erklärung muss erkennbar dort enden, wo der Erklärende seinen Erklärungswillen abgeschlossen hat.

**Für den Kaufinteressenten (Verbraucher)**: Ist der Provisionshinweis nur in einem Footer, einer Signatur oder unterhalb der Grußformel platziert, liegt ein starker Formeinwand nahe. Der Maklervertrag kann nach § 125 BGB nichtig sein. Eine bereits gezahlte Provision kann nach § 812 BGB zurückgefordert werden; Wertersatz- und Treuwidrigkeitseinwände sind gesondert und quellenbasiert zu prüfen.

## Workflow

### Checkliste Maklervertrag — Textform-Compliance

```
□ Maklervertrag über Kauf/Verkauf einer Wohnung oder eines Einfamilienhauses?
 → § 656a BGB: Textform zwingend erforderlich

□ Textformtraeger vorhanden?
 → E-Mail / PDF / WhatsApp / SMS / Brief moeglich
 → Lesbar auf dauerhaftem Datentraeger

□ Person des Erklaerenden erkennbar?
 → Absender-Adresse, Name, Briefkopf

□ ABSCHLUSS DER ERKLAERUNG ERKENNBAR? (Kernpunkt)
 → Provisionshinweis VOR Grussformel und Namensangabe?
 → Oder: Bezugnahme auf Hinweis im Haupttext?
 → NICHT genuegend: Provisionshinweis im Footer / unter der Grussformel
 ohne Bezug aus dem Haupttext

□ Wesentliche Bestandteile bestimmbar?
 → Parteien des Maklervertrags
 → Hoehe der Provision (Prozentsatz oder Betrag)
 → Gegenstand des in Aussicht genommenen Hauptvertrags (Immobilie)
 → Ggf. Rueckgriff auf Umstaende ausserhalb der Erklaerung zulaessig,
 wenn zureichender Anhaltspunkt in der Urkunde

□ Angebot und Annahme:
 → Koennen auf getrennten E-Mails stehen, wenn beide Erklaerungen die Textform wahren
 → Konkludente Annahme nur vorsichtig bejahen und mit verifizierter Rechtsprechung absichern

□ Archivierung gesichert?
 → Beide Seiten sollten E-Mails und Anhaenge dauerhaft sichern

□ Bei Formverstoss:
 → Maklervertrag nichtig (Paragraph 125 BGB)
 → Wertersatz-/Bereicherungsanspruch des Maklers am Schutzzweck des § 656a BGB pruefen
 → Bereits gezahlte Provision kann der Kaeufer zurueckfordern
```

### Pruefung von E-Mails auf Textform-Wirksamkeit

| Stelle des Provisionshinweises | Ergebnis |
|----|----|
| Im Haupttext der E-Mail, vor der Grussformel | Textform gewahrt (sofern auch die anderen Voraussetzungen vorliegen) |
| Im Haupttext, mit ausdruecklicher Bezugnahme | Textform gewahrt |
| In separatem Absatz nach Grussformel, aber mit Verweis aus dem Haupttext | Textform gewahrt — der Haupttext zieht den Hinweis in die Erklaerung |
| Rechtsprechung live prüfen | keine Entscheidung aus Modellwissen; Quelle vor Ausgabe protokollieren |
| In separater Anlage / PDF, im Haupttext darauf verwiesen | Textform gewahrt, sofern Anlage dauerhaft uebermittelt |
| In einer Standardsignatur, die in jeder E-Mail steht | Textform NICHT gewahrt — die Erklaerung endet vor der Signatur |

### Haeufige Fallkonstellationen

| Sachverhalt | Ergebnis |
|----|----|
| Makler beauftragt per E-Mail "Bitte vermitteln Sie", Interessent antwortet "Bestaetigt" — Provision im Haupttext | Textform gewahrt, Provisionsanspruch besteht |
| Rechtsprechung live prüfen | keine Entscheidung aus Modellwissen; Quelle vor Ausgabe protokollieren |
| Mündliche Beauftragung am Telefon, spaeter schriftliche Bestaetigung des Maklers, der Kaeufer antwortet aber nie | Keine Textform-Annahme — kein wirksamer Vertrag |
| Makler schickt Auftragsbestaetigung mit Provisionshinweis im Haupttext, Kaeufer nimmt Leistung in Anspruch ohne explizite Antwort | Konkludente Annahme moeglich (Leitsatz 2), wenn wesentliche Bestandteile bestimmbar |
| Gewerbeimmobilie | § 656a BGB nicht anwendbar — Maklervertrag formfrei zulaessig |

## Templates

### Textformwirksamer Maklerauftrag per E-Mail (Makler-Vorlage, quellenfest)

```
Betreff: Maklerauftrag Immobilie [Adresse] — Auftragsbestaetigung

Sehr geehrte(r) Herr/Frau [Name Kaufinteressent],

hiermit bestaetige ich, dass ich fuer Sie als Makler taetig werde
und die Immobilie [Adresse, kurze Beschreibung] vermittele.

Im Erfolgsfall — Abschluss eines notariellen Kaufvertrags ueber
diese Immobilie — ist eine Maklerprovision in Hoehe von [X %] des
beurkundeten Kaufpreises zuzueglich der gesetzlichen Mehrwertsteuer
von Ihnen an mich zu zahlen.

Bitte bestaetigen Sie diesen Auftrag durch Antwort-E-Mail.

Damit endet meine Erklaerung. Es folgen nur noch Grussformel und
Kontaktdaten.

Mit freundlichen Gruessen
[Name Makler / Maklerunternehmen]
[Datum]

--
[Standardsignatur — gehoert nicht zur Erklaerung]
```

**Wichtig zur Textform**: Der Provisionshinweis steht **vor** der Grussformel im Haupttext. Die Signatur darunter enthaelt keine vertragsrelevanten Informationen. Damit ist der Abschluss der Erklaerung erkennbar.

### Mandantenhinweis fuer Kaeufer

```
Wichtiger Hinweis zur Maklerprovision beim Wohnungskauf:

Seit dem 23. Dezember 2020 muss ein Maklervertrag ueber den Kauf
einer Wohnung oder eines Einfamilienhauses in Textform geschlossen
werden (§ 656a BGB). Ohne Textform ist der Vertrag nichtig und
der Makler hat keinen Anspruch — auch nicht im Wege des
Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

Textform ist z. B. gewahrt durch:
- E-Mail-Austausch (Angebot des Maklers + Ihre Bestaetigung), wenn
 der Provisionshinweis im Haupttext steht
- Schriftlicher Auftrag auf Papier
- WhatsApp-Nachrichtenfolge, wenn dauerhaft gespeichert und
 inhaltlich klar

Textform ist NICHT gewahrt, wenn der Provisionshinweis:
- nur in einer Signatur oder im Footer der E-Mail steht
- unter der Grussformel angefuegt ist, ohne dass der Haupttext
 darauf Bezug nimmt
- nur muendlich (Telefon, persoenlich) genannt wurde

Wenn Sie bereits gezahlt haben und Zweifel bestehen, kann eine
Rueckforderung nach Paragraph 812 BGB in Betracht kommen.
```

### Mandantenhinweis fuer Makler

```
Hinweis zur rechtssicheren Provisionsvereinbarung:

Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
ist bei Maklertaetigkeit fuer Wohnungen und Einfamilienhaeuser
unbedingt zu beachten:

1. Provisionshinweis MUSS im Haupttext der E-Mail stehen — nicht
 unter der Grussformel, nicht im Footer, nicht in der Signatur.
 Sonst ist die Textform fuer den Hinweis NICHT gewahrt.

2. Die Erklaerung muss klar erkennbar dort enden, wo der
 Erklaerende den Erklaerungswillen abschliesst. Alles, was unter
 der Grussformel steht, gehoert nicht mehr zur Erklaerung — es
 sei denn, der Haupttext nimmt ausdruecklich darauf Bezug.

3. Wesentliche Bestandteile muessen aus der Erklaerung
 bestimmbar sein:
 - Parteien
 - Hoehe der Provision (Prozentsatz oder Betrag)
 - Gegenstand des Hauptvertrags (welche Immobilie)

4. Folge eines Formverstosses: kein Provisionsanspruch, auch
 Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

Empfehlung: standardisiertes E-Mail-Template mit Provisionshinweis
im Haupttext verwenden und durch Bestaetigung des Kaufinteressenten
abschliessen lassen.
```

## Fallstricke

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- **Grussformel-Falle**: Was nach "Mit freundlichen Gruessen" und Namensangabe steht, ist nicht mehr Teil der Erklaerung, es sei denn, der Haupttext nimmt darauf Bezug.
- **Bereicherungssperre wirkt nur in eine Richtung**: Der **Makler** kann nicht ueber § 812 BGB Provision verlangen. Der **Kaeufer** kann hingegen eine bereits gezahlte Provision nach § 812 BGB zurueckfordern — die Bereicherungssperre dient gerade dem Verbraucherschutz.
- **Konkludente Annahme aber Textform-Angebot**: Auch wenn der Vertrag konkludent zustande kommen kann (Leitsatz 2), muss das **Angebot** in Textform vorliegen und die wesentlichen Bestandteile bestimmbar enthalten. Eine rein muendliche Anbahnung mit konkludenter Annahme genuegt nicht.
- **Gewerbeimmobilien**: § 656a BGB gilt nur fuer Wohnungen und Einfamilienhaeuser. Bei Gewerbeimmobilien ist der Maklervertrag formfrei zulaessig.
- **Verkaeufer- und Kaeuferseite**: § 656a BGB gilt fuer beide Vertragsbeziehungen, wenn die Verbrauchereigenschaft auf der jeweiligen Seite vorliegt.

## Querverweise

- → `textform-paragraph-126b-bgb-dauerhafter-datentraeger`
- → `anspruchsformulierungen-bei-formverstoss`
- → `form-checker-fuer-vertrag-oder-willenserklaerung`
- → `dokumentations-und-beweisarchitektur`

## 3. `amtlicher-formkern-bgb-zpo-check`

**Fokus:** Amtlicher Formkern-Check für BGB und ZPO: trennt Schriftform, Textform, elektronische Form, qES, beA/EGVP, § 130e ZPO, Zustellung, Zugang und Beweiskraft elektronischer Dokumente.

# Amtlicher Formkern BGB/ZPO

## Zweck

Dieser Skill wird genutzt, wenn eine Erklärung an einer Form, einem Übermittlungsweg oder einem Zustellungs-/Zugangsbeweis hängt. Er trennt materielles Privatrecht und Prozessrecht sauber.

## Prüfschritte

1. Erklärung bestimmen: Vertrag, Kündigung, Bürgschaft, Rücktritt, Anfechtung, Schriftsatzerklärung.
2. Formerfordernis bestimmen: § 126, § 126a, § 126b, § 127, § 128 oder § 129 BGB; Spezialnorm prüfen.
3. Zugang prüfen: § 130 BGB oder Zustellungsregime der ZPO.
4. Prozesspfad prüfen: §§ 130a, 130d, 130e, 173, 189 ZPO.
5. Beweiswert prüfen: § 371a ZPO, Versandjournal, eEB, Zustellungsurkunde, Botenprotokoll, Validierungsbericht.

## Entscheidungsmatrix

| Frage | BGB | ZPO |
| --- | --- | --- |
| Ist die Erklärung formwirksam? | §§ 125-129 BGB | § 130e ZPO nur bei konkretem Anwendungsbereich |
| Ist sie zugegangen? | § 130 BGB | §§ 166-190 ZPO bei Zustellung |
| Ist elektronisch eingereicht? | § 126a BGB nur bei qES als materielle Form | §§ 130a, 130d ZPO |
| Ist der Beweis stark genug? | Urkunde, Zeuge, Bote | § 371a ZPO, Zustellungsnachweis |

## Output

Liefer:

- Formentscheidung: wirksam / unwirksam / riskant / Live-Check.
- Versand- und Zustellpfad.
- Beweisordner: welche Nachweise in die Akte gehören.
- Alternativroute: Papier, qES, beA mit Formfiktion, Gerichtsvollzieher, Bote.

## Referenz

Nutze `references/amtlicher-formkern-bgb-zpo.md`.
