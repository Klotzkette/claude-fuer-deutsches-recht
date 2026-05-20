---
name: nda-abgleich
description: "NDA-Verhandlungshilfe fuer die empfangende Seite. Zwei Modi: (A) Standard-Destillation aus 1 bis n eigenen NDAs und frei beschreibbarer Erfahrung in einen konsolidierten Haltelinien-Standard mit Ampelmatrix ROT/GELB/GRUEN; (B) Redlining-Lauf, der einen Entwurf der Gegenseite gegen genau diesen Standard chirurgisch mit echten Word-Tracked-Changes umarbeitet (w:ins und w:del als Geschwister auf Laufebene, mit author und date). Keine Absatzloeschungen, keine kompletten Klausel-Neufassungen, jede Aenderung minimalinvasiv. Verwenden bei Formulierungen wie 'aus unseren NDAs einen Standard ableiten', 'Haltelinien aus mehreren Vertraegen destillieren', 'NDA der Gegenseite anpassen', 'NDA Redlining', 'Standard durchsetzen', 'NDA Tracked Changes', 'NDA chirurgisch redigieren'."
---

# NDA-Abgleich: eigenen Standard destillieren und chirurgisch durchsetzen

## Wann diesen Skill aufrufen

Wenn der Anwender (typischerweise als Inhouse-Jurist oder externer Anwalt der **empfangenden Seite**) entweder seinen eigenen NDA-Standard erst noch **erarbeiten** muss oder einen NDA-Entwurf der Gegenseite bekommen hat, den er **nicht durch einen eigenen Entwurf ersetzen** kann oder will, aber dessen interne Haltelinien er dennoch durchsetzen muss.

Der Skill hat zwei Einsatzmodi, die unabhaengig oder nacheinander laufen koennen:

- **Modus A — Standard-Destillation:** Aus 1 bis n eigenen NDAs (oder NDA-Entwuerfen, Verhandlungsergebnissen aus alten Akten, Excel-Auszuegen mit Klauselverweisen, freien Erfahrungswerten) wird ein konsolidierter **Haltelinien-Standard** mit Ampelmatrix ROT/GELB/GRUEN erzeugt. Dieser Standard ist die Eingangsgroesse fuer Modus B und fuer kuenftige Verhandlungen.
- **Modus B — Redlining-Lauf:** Der NDA-Entwurf der Gegenseite wird gegen genau diesen Standard chirurgisch redigiert. Ausgabe ist eine .docx mit echten Word-Tracked-Changes.

Der Skill greift, sobald der Anwender mindestens einen der beiden Anwendungsfaelle anstoesst. Typische Aufschlaege:

- "Hier sind unsere letzten zehn NDAs, mach uns daraus einen Standard."
- "Wir haben zwar ein eigenes NDA-Template, aber wichtig ist eigentlich, was wir in der Praxis verhandelt haben — destilliere unseren echten Haltelinien-Standard."
- "Hier ist der NDA-Entwurf der Gegenseite und unser Standard. Bitte chirurgisch anpassen."
- "Macht eine .docx mit Tracked Changes draus, so dass die Gegenseite das Dokument noch als ihres erkennt."

Nicht zustaendig: Erstellung eines NDA von Null ohne jegliche Vorlage, allgemeine Vertragspruefung ohne Bezug zu NDA-Klauseln, materiell-rechtliche Wuerdigung der Vertragsverletzungsfolgen.

## Modus A — Standard-Destillation

### Inputs in Modus A

Alles, was der Anwender beibringen kann, ist verwertbar — gerade weil der Standard aus gelebter Praxis und nicht aus einem Template-Fetisch entstehen soll. Verarbeitbar sind:

- **Eigene NDAs** als .docx oder .pdf (auch viele auf einmal, typischerweise 1 bis 50). Jede Datei wird einzeln analysiert.
- **NDAs der Gegenseite aus frueheren Verhandlungen**, soweit der Anwender sie freigibt. Diese werden besonders interessant ausgewertet: wo hat der Mandant nachgegeben, wo hat die Gegenseite nachgegeben, wo wurde eine Mittelloesung gefunden?
- **Verhandlungs-Notizen, E-Mails, Aktenvermerke** in beliebigem Format. Werden ausgelesen und in den Standard eingeflochten als "Erfahrungswert".
- **Frei beschriebene Erfahrung** des Anwenders im Chat: "Wir akzeptieren nie Schiedsklauseln, weil unser letzter Schiedsfall in Singapur 14 Monate gedauert hat." Solche freitext-Saetze werden als zusaetzliche Haltelinien aufgenommen, sofern sie konkret genug sind.
- **Eigenes Template-NDA**, sofern vorhanden, als grobe Strukturreferenz. Der Skill **gewichtet das Template aber nicht hoeher als die gelebte Praxis** — wenn die Praxis vom Template abweicht, gewinnt die Praxis.

Wenn nur ein einziger NDA verfuegbar ist, ist das auch in Ordnung; der Skill arbeitet dann mit einer entsprechend duenneren Belegbasis und macht das im Reporting transparent.

### Methodik der Destillation

Fuer jede der typischen NDA-Klauseln (siehe Klauselkatalog unten) wertet der Skill ueber alle Inputs hinweg aus:

1. **Welche Position kommt vor?** Pro Klausel werden die tatsaechlich vereinbarten Formulierungen extrahiert (Vertragslaufzeit, Gerichtsstand, Vertragsstrafe etc.).
2. **Wie haeufig?** Die Verteilung wird sichtbar gemacht: "In 9 von 12 NDAs deutsches Recht, in 2 schweizerisches, in 1 englisches."
3. **Mit welcher Streuung?** Wo eine echte Bandbreite besteht (z. B. Nachwirkungsfrist zwischen 2 und 5 Jahren), wird die Spanne und der Median dokumentiert.
4. **Welche Outlier?** Eine einzelne Abweichung aus einem Spezialfall (z. B. ein NDA fuer eine US-Akquisition mit Delaware-Recht) wird nicht zur Regel hochgerechnet, sondern als Ausnahme markiert.
5. **Welche Vorzugsformulierung?** Pro Klausel wird die im Mandantenkreis am haeufigsten verwendete Formulierung als Standardposition vorgeschlagen — woertlich, damit sie spaeter in Modus B als Einfuegungstext direkt zur Verfuegung steht.

### Output von Modus A

Die Destillation liefert drei Dateien im Workspace:

- `Haltelinien-Standard_<Mandant>_<Datum>.md` — die konsolidierte Ampelmatrix mit Klausel, Status (ROT/GELB/GRUEN), Standardposition, Bandbreite, Quelle (welche Vertraege belegen die Position), Begruendung.
- `Haltelinien-Standard_<Mandant>_<Datum>.docx` — dieselbe Matrix als formatierte Tabelle zum internen Verteilen.
- `Haltelinien-Standard_<Mandant>_<Datum>.json` — maschinenlesbare Repraesentation derselben Matrix; wird von Modus B als Eingangsgroesse genutzt.

Die Ampel-Zuordnung folgt diesen Heuristiken (der Anwender kann jede ueberstimmen):

- **ROT** wird vorgeschlagen, wenn in **allen** verfuegbaren NDAs dieselbe Position vereinbart wurde und/oder der Anwender sie als "nicht verhandelbar" beschrieben hat.
- **GELB** wird vorgeschlagen, wenn die Klausel ueber die Inputs hinweg innerhalb einer engen Bandbreite variiert (z. B. Nachwirkungsfrist 3 bis 5 Jahre, Vertragsstrafe 10 bis 50 TEUR).
- **GRUEN** wird vorgeschlagen, wenn die Klausel in der gelebten Praxis sehr unterschiedlich gehandhabt wurde, ohne dass das den Schutzinteressen des Mandanten geschadet haette (Form der Mitteilungen, Sprache, Counterparts).

Der Skill **fragt vor Finalisierung nach**, ob die vorgeschlagene Ampel-Zuordnung passt; im Zweifel werden GELB-Positionen mit der zugehoerigen Bandbreite belassen.

### Klauselkatalog (Mindestumfang der Destillation)

Der Skill arbeitet jede der folgenden Klauseln ab — auch dann, wenn sie in den Inputs nicht vorkommt, dann mit Markierung "nicht belegt, Standardvorschlag aus juristischem Allgemeingut":

- Parteibezeichnung und Bilateralitaet (gegenseitig oder einseitig).
- Definition Confidential Information und Kennzeichnungserfordernis.
- Zweckbindung.
- Geheimhaltungspflicht und Sorgfaltsmassstab.
- Weitergabekreis (Representatives, Konzerngesellschaften, externe Berater).
- Ausnahmen / Carve-outs (oeffentlich bekannt, vor Offenlegung bekannt, eigenstaendig entwickelt, von Dritten ohne Geheimhaltungspflicht erhalten, gesetzliche Offenlegungspflicht).
- IP / kein Rechteuebergang / Lizenzen.
- Rueckgabe und Vernichtung; Wahlrecht; Aufbewahrungspflichten fuer Compliance.
- Vertragslaufzeit und Nachwirkungsfrist.
- Vertragsstrafe und Schadenersatz.
- Schriftformklausel (einfach / doppelt) und elektronische Form.
- Anwendbares Recht (mit oder ohne CISG / IPR-Verweisungen).
- Gerichtsstand oder Schiedsklausel.
- Form der Mitteilungen (Notices).
- Sprache des Vertrags und massgebliche Fassung.
- Counterparts, salvatorische Klausel.

Weitere Klauseln, die in den Inputs auftauchen (z. B. Non-Solicitation, Standstill, Publicity, Audit-Right), werden mit aufgenommen und mit Ampel-Vorschlag versehen.

### Iteratives Schaerfen

Der Skill behandelt den destillierten Standard als **lebendes Dokument**. Wenn der Anwender spaeter weitere NDAs einreicht, kann derselbe Skill den bestehenden Standard re-destillieren — neue Erkenntnisse fliessen ein, alte Belegbasis bleibt versioniert. Im Workspace wird die jeweils neue Fassung mit Zeitstempel abgelegt, die alte nicht ueberschrieben.

## Modus B — Redlining-Lauf

### Grundprinzip in Modus B: chirurgisches Redigieren

Der Entwurf der Gegenseite ist das Ausgangsdokument. Er bleibt strukturell **vollstaendig erhalten**:

- Alle Absaetze des Originals bleiben in der Ausgabe enthalten.
- Keine Absatzloeschungen, keine kompletten Klausel-Neufassungen.
- Streichungen und Einfuegungen wirken **auf Wort- und kurzer Phrasenebene**.
- Die Gegenseite muss das Dokument beim Oeffnen sofort wiedererkennen.
- Aenderungen sind als echte Word-Tracked-Changes sichtbar und einzeln annehmbar oder ablehnbar.

Hintergrund: Wer ganze Klauseln durch eigene Formulierungen ersetzt, signalisiert der Gegenseite, dass man einen neuen Entwurf vorlegen will. Das eskaliert die Verhandlung. Wer dagegen drei Worte streicht und durch zwei andere ersetzt, signalisiert: "Wir verhandeln auf eurem Papier, aber unsere Haltelinien stehen fest." Das ist anschlussfaehiger und politisch klueger.

### Inputs in Modus B

Fuer Modus B braucht der Skill:

- den **NDA-Entwurf der Gegenseite** (.docx oder .pdf, OCR falls Bild-PDF) als Ausgangsdokument, und
- den **Haltelinien-Standard des Mandanten**. Diesen liefert idealerweise Modus A in Form der `.json`- oder `.md`-Datei. Alternativ akzeptiert der Skill auch ein eigenes Standard-NDA des Mandanten plus eine kurze Ampelmatrix als Eingabe — er destilliert dann intern "on the fly" einen Minimal-Standard daraus (mit Hinweis, dass Modus A grundsaetzlich die solidere Grundlage ist).

Vor der ersten Aenderung liest der Skill alle Inputs vollstaendig:

- Der Entwurf der Gegenseite wird in seine Absaetze zerlegt und durchnummeriert (typischerweise 60 bis 100 Absaetze). Diese Nummerierung dient als Adresse fuer jede Aenderung.
- Der Haltelinien-Standard liefert die **Zielformulierungen** fuer jede Klausel — also die genauen Worte, mit denen die eigene Position sprachlich am elegantesten ins Dokument der Gegenseite eingebaut werden kann.
- Die Ampelmatrix liefert die **Reihenfolge der Verbindlichkeit**:
  - ROT-Eintraege sind **nicht verhandelbar**. Jeder ROT-Punkt muss in der Ausgabe-Datei adressiert sein, andernfalls schlaegt das Mandat fehl.
  - GELB-Eintraege werden in **Standardposition** eingebracht; die zulaessige Bandbreite ist in der Matrix definiert.
  - GRUEN-Eintraege werden nur dann beruehrt, wenn die Gegenseite eine Formulierung gewaehlt hat, die deutlich vom Standard abweicht — sonst stehen sie unveraendert.

Wenn die Ampelmatrix unklar oder unvollstaendig ist, **fragt der Skill nach**, bevor er beginnt. Er erfindet keine Haltelinien.

## Mapping Klauseln zu Ampelpunkten

Schritt 1: Strukturanalyse des Gegenseite-Entwurfs.

Typische Klauseln im NDA, die der Skill identifiziert:

- Parteibezeichnung und Rollen (einseitig oder bilateral?)
- Definition Confidential Information
- Zweckbindung (Purpose)
- Verpflichtungen der empfangenden Seite
- Ausnahmen / Carve-outs (oeffentlich bekannt, eigenstaendige Entwicklung, gesetzliche Offenlegungspflicht etc.)
- Weitergabekreis (Representatives)
- IP / kein Rechteuebergang / Lizenzen
- Rueckgabe und Vernichtung
- Laufzeit und Nachwirkungsfrist
- Vertragsstrafe
- Schriftformklausel
- Anwendbares Recht und Gerichtsstand
- Schiedsklausel
- Form der Mitteilungen (Notices)
- Sprache des Vertrags
- Ausfertigungen, salvatorische Klausel, Schriftform, Counterparts

Schritt 2: Mapping jeder erkannten Klausel zu **genau einer** Zeile der Ampelmatrix. Klauseln, die keinem Matrixpunkt entsprechen, werden in der Antwort separat aufgefuehrt, **nicht aber stillschweigend mitveraendert**.

Schritt 3: Pro Matrixpunkt entscheiden, ob der Gegenseite-Text bereits der eigenen Position entspricht (dann keine Aenderung) oder ob ein Tracked Change noetig ist.

## Stil der Tracked Changes

Jede einzelne Aenderung folgt diesen Regeln:

- **So wenige Worte wie moeglich, so viele wie noetig.** Wo ein Wort genuegt, wird nicht ein Halbsatz veraendert.
- **Streichung und Einfuegung gehoeren zusammen.** Niemals nur loeschen, ohne den Ersatz mitzugeben. Niemals nur einfuegen, ohne die alte Stelle zu streichen, wo eine semantische Verschiebung passiert.
- **Niemals ganze Absaetze loeschen.** Auch eine vollstaendig unakzeptable Klausel wird durch wenige zielgenau geaenderte Worte gerettet — etwa "Disclosing Party" zu "Each Party", "California law" zu "the laws of the Federal Republic of Germany".
- **Keine neuen Absaetze einfuegen.** Wenn ein Punkt im Entwurf der Gegenseite gar nicht vorkommt (etwa ein vollstaendiger Carve-out-Katalog fehlt), wird in einem **Kommentar** angemerkt, dass dies in einer separaten Verhandlungsrunde adressiert werden muss — der Skill schlaegt nicht eigenmaechtig neue Absaetze vor.
- **Inhalt vor Sprache.** Tippfehler und sprachliche Unsauberkeiten der Gegenseite werden **nur dann** angetastet, wenn sie zugleich eine inhaltliche Verschiebung bewirken. Eine reine Korrektur von "posseses" zu "possesses" ist nicht Aufgabe des Skills.

## Sprache und Ausgangstextpflege

Englischsprachige Entwuerfe werden in Englisch redigiert; deutschsprachige in Deutsch. Mischsprache ist erlaubt, wenn der Standard die deutsche Formulierung vorgibt, der Gegenseite-Entwurf aber englisch ist — dann wird die Einfuegung zweisprachig oder rein in der Vertragssprache der Gegenseite formuliert. Der Anwender entscheidet im Zweifel.

## Technische Spezifikation der Tracked Changes (Word XML)

Die Ausgabedatei ist **valid .docx** und enthaelt echte Word-Tracked-Changes. Pruefkriterien:

- **`<w:ins>` und `<w:del>` als Geschwister-Elemente** auf der Ebene der Run-Container, nicht verschachtelt.
- Eingefuegter Text steht in `<w:ins>` mit einem Kind-Run `<w:r>`, der wieder einen `<w:t>` traegt.
- Geloeschter Text steht in `<w:del>` mit einem Kind-Run, dessen Text in `<w:delText>` (statt `<w:t>`) liegt.
- Beide Elemente tragen die Attribute **`w:id`**, **`w:author`** und **`w:date`**.
  - `w:author` Standardwert: **"Receiving Party Counsel"** (oder vom Anwender vorgegeben).
  - `w:date` als ISO-8601-Zeitstempel der Bearbeitung, z. B. `2026-05-20T01:55:00Z`.
- Jede `w:id` ist im ganzen Dokument eindeutig.
- Die Datei oeffnet ohne Reparatur-Dialog in Microsoft Word ab Version 2016 und in LibreOffice ab Version 7.

Beispiel fuer einen Wortaustausch in einem Lauf:

```xml
<w:r>
  <w:t xml:space="preserve">governed by </w:t>
</w:r>
<w:del w:id="42" w:author="Receiving Party Counsel" w:date="2026-05-20T01:55:00Z">
  <w:r>
    <w:delText xml:space="preserve">the laws of the State of Delaware</w:delText>
  </w:r>
</w:del>
<w:ins w:id="43" w:author="Receiving Party Counsel" w:date="2026-05-20T01:55:00Z">
  <w:r>
    <w:t xml:space="preserve">the laws of the Federal Republic of Germany, excluding the CISG and rules of private international law</w:t>
  </w:r>
</w:ins>
<w:r>
  <w:t xml:space="preserve">.</w:t>
</w:r>
```

## Empfehlung zur Umsetzung im Code

Ueber das Python-Paket `python-docx` lassen sich `w:ins` und `w:del` nicht direkt anlegen; der Skill manipuliert das Dokument deshalb auf XML-Ebene mit `lxml` (oder `xml.etree.ElementTree`) auf der `document.xml`-Datei innerhalb der ZIP-Struktur der .docx. Schritte:

1. `.docx` als ZIP entpacken (Python `zipfile`).
2. `word/document.xml` einlesen, Namespaces registrieren (`w` = `http://schemas.openxmlformats.org/wordprocessingml/2006/main`).
3. Pro geplanter Aenderung den passenden `<w:r>`-Lauf finden, an der Wortgrenze splitten, `<w:del>` und `<w:ins>` mit den korrekten Attributen einfuegen.
4. Alle anderen Dateien (`word/styles.xml`, `_rels`, `[Content_Types].xml`, Headers/Footers) unveraendert lassen.
5. ZIP neu schreiben.

Wichtig: Niemals den Text direkt am Anfang der `document.xml` ueber regulaere Ausdruecke ersetzen, weil dabei Run-Splits, Formatierung und Tracked-Change-Markup brechen. Immer ueber den DOM-Baum.

## Header-Eintrag fuer die empfangende Partei

Der Name des Mandanten (z. B. Wernherr & Dimpflmoser Spezialventiltechnik GmbH & Co. KG) wird als **Tracked Change** an der Stelle eingefuegt, wo der Entwurf "[Company Name]" oder einen aequivalenten Platzhalter enthaelt. Ist kein Platzhalter vorhanden, wird die naechstpassende Stelle (in der "between"-Klausel der Praeambel) verwendet und der Eintrag dort durch einen `w:ins`-Block ergaenzt.

## Reporting im Chat

Nach Abschluss der Bearbeitung gibt der Skill drei Bloecke aus:

1. **Aenderungsuebersicht** als Tabelle: Absatznummer (gem. eigener Nummerierung des Entwurfs der Gegenseite), Klausel, Matrixpunkt (ROT/GELB/GRUEN), kurze Beschreibung der vorgenommenen Aenderung.
2. **Offene Punkte**: Was nicht adressiert wurde, weil die Klausel im Entwurf der Gegenseite fehlt (z. B. vollstaendiger Carve-out-Katalog, doppelte Schriftformklausel). Diese Punkte muessen separat in der Begleitnachricht an die Gegenseite eingebracht werden.
3. **Verhandlungsrisiken**: Punkte, die GELB sind und voraussichtlich noch Diskussion erfordern. Hinweis auf Bandbreiten der Matrix.

## Datei-Benennung

Die Ausgabedatei traegt den Namen des Ursprungsdokuments mit dem Suffix `_redlined_<Datum>.docx`. Beispiel: `NDA_TechVantage_Global_redlined_2026-05-20.docx`. Keine Umlaute, keine Leerzeichen.

## Was der Skill nicht tut

- **Keine Bewertung des Endverhandlungsergebnisses.** Der Skill stellt nur die Haltelinien sicher; ob das Verhandlungsergebnis kommerziell akzeptabel ist, entscheidet der Anwender.
- **Keine Pruefung der Bonitaet oder Rechtsfaehigkeit der Gegenseite.**
- **Keine Pruefung der eigenen Bevollmaechtigung.** Der Anwender muss selbst sicherstellen, dass er fuer den Mandanten zeichnen darf.
- **Keine Schwaerzung von Drittinformationen.** Wenn der Entwurf der Gegenseite Drittinformationen enthaelt (Namen, E-Mails von nicht beteiligten Personen in Kommentaren), wird das gemeldet, aber nicht automatisch entfernt.
- **Keine elektronische Signatur und kein Versand.** Die fertige .docx wird im Workspace abgelegt, der Anwender uebernimmt Versand und Signatur.

## Berufspflichtlicher Hinweis

Auch wenn der Skill chirurgisch arbeitet, bleibt die **Letztverantwortung** fuer den Inhalt des unterzeichneten NDA beim Anwalt. Insbesondere die Pruefung, ob alle materiellen Haltelinien der Ampelmatrix tatsaechlich gewahrt sind, ob die GeschGehG-relevanten Anforderungen (Geschaeftsgeheimnisgesetz § 2 Nr. 1 lit. b) eingehalten werden und ob keine Drittinteressen oder Mandatsgeheimnisse verletzt werden, ist und bleibt anwaltlich. Der Skill erinnert daran, ersetzt es aber nicht.

## Beispielformulierungen, die diesen Skill ausloesen

Fuer Modus A (Destillation):

- "Hier sind unsere letzten zehn NDAs. Destilliere daraus unseren Standard."
- "Wir haben zwar ein Template, aber wichtig ist die Praxis. Bau uns daraus eine Ampelmatrix."
- "Aus diesen NDAs und meinen Notizen einen Haltelinien-Katalog ableiten."
- "Pruef nochmal mit diesen drei neuen NDAs, ob unser Standard noch stimmt."

Fuer Modus B (Redlining):

- "Hier ist der NDA-Entwurf von TechVantage Global und unser Standard. Bitte chirurgisch anpassen."
- "Macht eine .docx mit Tracked Changes draus, so dass wir unsere Haltelinien durchsetzen, aber die Gegenseite das Dokument noch als ihres erkennt."
- "NDA Redlining gegen unsere Ampelmatrix, behutsam."
- "Wir sind Receiving Party, die andere Seite hat vorgelegt. Standard durchsetzen ohne neue Absaetze."
- "Bitte nur Wortaenderungen, keine ganzen Klauseln neu schreiben."
