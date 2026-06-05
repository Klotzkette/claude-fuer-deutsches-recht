---
name: befristungsabrede-qes-rechtsprechung
description: "Befristungsabrede QES Rechtsprechung: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Befristungsabrede QES Rechtsprechung

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Befristungsabrede QES Rechtsprechung** im Plugin Schriftform/Textform BGB. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `workflow-redteam-qualitygate` | Red-Team Qualitygate im Plugin schriftform-und-textform-bgb: prüft das Ergebnis auf Halluzinationen, Fristenfehler, Zuständigkeit, Quellen, Beweise und Ton. |
| `befristungsabrede-qes-rechtsprechung-stand-2026` | Aktuelle Rechtsprechung zur elektronischen Signatur bei Befristungsabreden nach § 14 Abs. 4 TzBfG. Prüft Scan, einfache E-Signatur, echte qES, ArbG-Gera-Linie, § 623 BGB, § 46h ArbGG als Sonderpfad und Mandantenhinweise für Arbeitgeber und Arbeitnehmer. |
| `spezial-rechtsprechung-livecheck-formfragen` | Livecheck verifizierter Rechtsprechung zu Schriftform, qES und beA: führt schnell durch Sachverhalt, Rechtsgrundlagen, Belege, Risiken und erzeugt einen verwertbaren nächsten Output. |

## Arbeitsweg

Im Plugin Schriftform/Textform BGB gilt für **Befristungsabrede QES Rechtsprechung**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `workflow-redteam-qualitygate`

**Fokus:** Red-Team Qualitygate im Plugin schriftform-und-textform-bgb: prüft das Ergebnis auf Halluzinationen, Fristenfehler, Zuständigkeit, Quellen, Beweise und Ton.

# Red-Team Qualitygate

## Aufgabe
Dieser Prüffeld stresst formrechtliche Ergebnisse gegen typische Fehler: Verwechslung Schrift-/Text-/elektronische Form, falsche Bewertung qualifizierter Signaturen, Übersehen von Heilungstatbeständen.

## Formenkanon prüfen
- **Schriftform (§ 126 BGB):** eigenhändige Namensunterschrift unter der Urkunde; gewillkürte Schriftform (§ 127 BGB) lässt Telekommunikationsformen zu, soweit nicht anders bestimmt.
- **Elektronische Form (§ 126a BGB):** ersetzt Schriftform nur mit qualifizierter elektronischer Signatur (QES) nach Art. 3 Nr. 12, Art. 25 Abs. 2 eIDAS-VO (EU) 910/2014.
- **Textform (§ 126b BGB):** lesbare Erklärung, dauerhafter Datenträger, Person des Erklärenden genannt -- E-Mail genügt regelmäßig; Fax ebenfalls.
- **Notarielle Beurkundung (§ 128 BGB):** für § 311b BGB (Grundstück), § 2247 BGB (Testament alternativ Eigenhändigkeit), § 1410 BGB (Ehevertrag), § 2348 BGB (Erbverzicht).
- **Öffentliche Beglaubigung (§ 129 BGB):** Notar bestätigt Echtheit der Unterschrift -- nicht den Inhalt.

## Red-Team-Punkte
- Schriftform durch eingescannte Unterschrift? -- Nein, allenfalls Textform.
- AGB-mäßige doppelte Schriftformklausel im Arbeitsverhältnis? -- BAG hat solche Klauseln vielfach für unwirksam gehalten (siehe ständige Rspr. des BAG zu § 305c, § 307 BGB; konkrete Az. live prüfen).
- DocuSign / Adobe Sign mit einfacher oder fortgeschrittener Signatur erfüllt **keine** Schriftform; nur QES.
- Heilung beachten: § 311b Abs. 1 S. 2 BGB (Grundstück: Heilung durch Auflassung und Eintragung), § 766 S. 3 BGB (Bürgschaft Vollkaufmanns, § 350 HGB), § 550 BGB (langjährige Mietverträge: Folge ordentliche Kündbarkeit, nicht Nichtigkeit).
- Frist Mietrecht § 550 BGB: nur Verträge mit Laufzeit > 1 Jahr.
- Falle: Bei zustimmungspflichtigem Geschäft Form des Hauptgeschäfts auch für Vollmacht? § 167 Abs. 2 BGB -- Sondertatbestände (Bürgschaft, Grundstück) beachten.

## Einstieg
Prüfe zuerst das vorhandene Material. Stelle nur Rückfragen, die die nächste fachliche Weiche verändern:

1. Wer fragt in welcher Rolle?
2. Was ist das gewünschte Ergebnis?
3. Gibt es Fristen, Termine, Zustellungen, Zahlungen oder Sanktionen?
4. Welche Unterlagen, Daten oder Belege liegen bereits vor?

## Arbeitsworkflow
1. Rolle, Ziel, Frist und Unterlagenlage in höchstens fünf Fragen klären.
2. Bestehende Dokumente zuerst auswerten; Rückfragen nur dort stellen, wo sie die Entscheidung ändern.
3. Passende Fachmodule aus diesem Plugin vorschlagen und begründen.
4. Ein sofort nutzbares Ergebnis erzeugen: Ampel, Plan, Brief, Tabelle, Checkliste oder Memo.

## Output-Standard
- Kurzbild: worum es geht, was gesichert ist, was offen ist.
- Prüf- oder Bearbeitungsmatrix mit den entscheidenden Punkten.
- Konkreter nächster Schritt mit Frist, Zuständigkeit und Unterlagen.
- Bei Außenkommunikation: knapper, sachlicher Textbaustein ohne unnötige Nebenangaben.

## Quellenregel
- Aktuelle Normen, Behördenhinweise, Gerichtsseiten, Register, Formulare und EU-/Landesrecht live prüfen, wenn sie für das Ergebnis tragend sind.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle ausgeben.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate aus Modellwissen.
- Unsicherheiten und Annahmen ausdrücklich markieren.

## 2. `befristungsabrede-qes-rechtsprechung-stand-2026`

**Fokus:** Aktuelle Rechtsprechung zur elektronischen Signatur bei Befristungsabreden nach § 14 Abs. 4 TzBfG. Prüft Scan, einfache E-Signatur, echte qES, ArbG-Gera-Linie, § 623 BGB, § 46h ArbGG als Sonderpfad und Mandantenhinweise für Arbeitgeber und Arbeitnehmer.

# Befristungsabrede — qES-Rechtsprechung Stand 2026

## Rechtsgrundlagen

- **§ 14 Abs. 4 TzBfG** — Befristung des Arbeitsvertrags muss schriftlich vereinbart werden
- **§ 126 BGB** — Schriftform: eigenhändige Unterschrift im Original
- **§ 126 Abs. 3 BGB** i.V.m. **§ 126a BGB** — Ersatz der Schriftform durch elektronische Form mit qualifizierter elektronischer Signatur (qES)
- **§ 126b BGB** — Textform: lesbare Erklärung auf dauerhaftem Datenträger (genügt **nicht** für § 14 Abs. 4 TzBfG)
- **§ 16 TzBfG** — Rechtsfolge bei Formmangel: Befristung unwirksam, Vertrag gilt als unbefristet
- **eIDAS-VO (EU) 910/2014** — technischer Rahmen der qES
- **§ 623 BGB** — Schriftform für Kündigung und Aufhebungsvertrag; elektronische Form (auch qES) **ausgeschlossen**
- **§ 46h ArbGG** — arbeitsgerichtliche Formfiktion für klare Willenserklärungen in elektronischen vorbereitenden Schriftsätzen

## Drei Linien der Rechtsprechung

### Linie 1: Eingescannte Unterschrift — unwirksam (LAG Berlin-Brandenburg)

- LAG Berlin-Brandenburg, Urt. v. 16.03.2022 – Az. 23 Sa 1133/21 — gescannte Unterschrift unter Befristungsabrede wahrt § 14 Abs. 4 TzBfG nicht. Quelle: https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=LAG+Berlin-Brandenburg&Datum=16.03.2022&Aktenzeichen=23+Sa+1133/21 sowie Pressemitteilung der ArbG-Vorinstanz: https://www.berlin.de/gerichte/arbeitsgericht/presse/pressemitteilungen/2022/pressemitteilung.1196191.php
- Eine lediglich auf das Vertragsdokument gescannte Unterschrift wahrt die Schriftform nach § 14 Abs. 4 TzBfG **nicht**.
- Es handelt sich weder um eine eigenhändige Unterschrift im Sinne von § 126 BGB noch um eine qualifizierte elektronische Signatur im Sinne von § 126a BGB.
- Folge: Befristung ist unwirksam, der Arbeitsvertrag gilt nach § 16 TzBfG als unbefristet.
- Die nachträgliche eigenhändige Unterschrift kann den Mangel nicht rückwirkend heilen; entscheidend ist, dass das ordnungsgemäß unterzeichnete Dokument dem Arbeitnehmer **vor Aufnahme der Arbeit** vorliegt.

### Linie 2: Einfache elektronische Signatur — unwirksam (ArbG Berlin)

**ArbG Berlin** (in Linie mit LAG Berlin-Brandenburg) zur einfachen elektronischen Signatur:
- Eine einfache elektronische Signatur (z. B. per Maus gezeichnete Unterschrift, "ich akzeptiere"-Button, eingebettetes Signaturbild ohne qES-Zertifikat) erfüllt die elektronische Form nach § 126a BGB **nicht**.
- Auch eine fortgeschrittene elektronische Signatur ohne qualifiziertes Zertifikat reicht nicht aus.
- Befristung ist unwirksam — Vertrag gilt unbefristet.

### Linie 3: Qualifizierte elektronische Signatur — wirksam (ArbG Gera)

- ArbG Gera, Urt. v. 03.07.2024 – Az. 2 Ca 936/23 — qES per DocuSign-qES wahrt die Schriftform des § 14 Abs. 4 TzBfG; § 623 BGB greift nur fuer Kuendigung und Aufhebungsvertrag und sperrt die elektronische Form dort, nicht aber bei der Befristungsabrede selbst. Quelle: https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=ArbG+Gera&Datum=03.07.2024&Aktenzeichen=2+Ca+936/23
- Eine über DocuSign eingesetzte qualifizierte elektronische Signatur (qES) erfüllt die Voraussetzungen des § 126a BGB.
- Damit ist die Schriftform nach § 14 Abs. 4 TzBfG durch die elektronische Form ersetzt.
- Die Befristungsabrede ist formwirksam.
- Voraussetzungen: zertifizierte qES nach eIDAS-VO; beide Vertragsparteien signieren ein jeweils gleichlautendes Dokument elektronisch (§ 126a Abs. 2 BGB).

### Hinweis zum Vierten Buerokratieentlastungsgesetz (BEG IV)

Mit dem Vierten Buerokratieentlastungsgesetz (BGBl. 2024 I Nr. 323 vom 29.10.2024) wurde § 14 Abs. 4 TzBfG mit Wirkung ab 01.01.2025 dahin ergaenzt, dass die Befristungsabrede grundsaetzlich in Textform abgeschlossen werden kann, sofern kein Tarifvertrag entgegensteht. Fuer das Schriftformerfordernis bei Befristungen vor 2025 sowie fuer Faelle, in denen das Tarifrecht weiterhin Schriftform verlangt, bleibt die qES-Rechtsprechung relevant. Quelle: https://www.gvw.com/aktuelles/blog/detail/buerokratieentlastungsgesetz-beschlossen-weg-frei-fuer-digitale-arbeitsvertraege

### Was bedeutet das praktisch?

| Signaturform | Wirksamkeit nach § 14 Abs. 4 TzBfG |
|----|----|
| Eigenhändige Unterschrift auf Papier (Original) | Wirksam (§ 126 BGB) |
| Rechtsprechung live prüfen | keine Entscheidung aus Modellwissen; Quelle vor Ausgabe protokollieren |
| Maus-Signatur / Touch-Signatur ohne qES-Zertifikat | **Unwirksam** (ArbG Berlin) |
| Einfache E-Mail-Bestätigung "ich akzeptiere" | **Unwirksam** — nur Textform |
| Fortgeschrittene elektronische Signatur (FES) ohne qES-Zertifikat | **Unwirksam** |
| Rechtsprechung live prüfen | keine Entscheidung aus Modellwissen; Quelle vor Ausgabe protokollieren |

## Prüfungsschema für die Praxis

```
□ Welche Form schreibt das Gesetz vor?
 → § 14 Abs. 4 TzBfG → Schriftform (§ 126 BGB)
 → § 623 BGB → Schriftform mit Sperre der elektronischen Form
 → Andere Spezialnormen prüfen

□ Welche Signatur wurde verwendet?
 → Eigenhändig auf Papier? → wirksam
 → Eingescannte Unterschrift? → unwirksam (LAG Berlin-Brandenburg)
 → Einfache elektronische Signatur? → unwirksam (ArbG Berlin)
 → qES nach § 126a BGB? → wirksam bei § 14 Abs. 4 TzBfG
 → unwirksam bei § 623 BGB (Kündigung/Aufhebung)

□ Bei qES — technische Prüfung:
 → Anbieter zertifiziert nach eIDAS-VO?
 → Signatur enthält qualifiziertes Zertifikat?
 → Zertifikat zum Zeitpunkt der Signatur gültig?
 → Bei Vertrag: beide Seiten haben jeweils ein qES-signiertes
 Dokument? (§ 126a Abs. 2 BGB)

□ Zeitpunkt:
 → Dokument vor Arbeitsaufnahme zugegangen?
 → Bei nachträglicher Unterzeichnung: Befristung unwirksam

□ Folgenfeststellung:
 → Wirksam → Befristung greift
 → Unwirksam → Vertrag gilt nach § 16 TzBfG als unbefristet
 → Möglichkeit der Entfristungsklage (3-Wochen-Frist
 ab vereinbartem Befristungsende, § 17 TzBfG)
```

## Wichtige Abgrenzung: § 623 BGB

Für **Kündigung** und **Aufhebungsvertrag** gilt § 623 BGB: Schriftform mit **ausdrücklicher Sperre der elektronischen Form**. Die direkte elektronische Erklärung per qES, beA-Nachricht, E-Mail oder Signaturplattform erfüllt § 623 BGB nicht. Seit 17.07.2024 muss aber im arbeitsgerichtlichen Verfahren § 46h ArbGG als enger Sonderpfad geprüft werden, wenn die Willenserklärung klar erkennbar in einem elektronischen vorbereitenden Schriftsatz nach § 46c ArbGG enthalten ist und zugestellt oder mitgeteilt wurde.

| Vorgang | Form | qES möglich? |
|----|----|----|
| Rechtsprechung live prüfen | Live-Verifikation erforderlich | keine Entscheidung aus Modellwissen; Quelle vor Ausgabe protokollieren |
| Kündigung des Arbeitsverhältnisses (§ 623 BGB) | Schriftform — elektronische Form ausgeschlossen | direkt nein; § 46h ArbGG im Prozess prüfen |
| Aufhebungsvertrag (§ 623 BGB) | Schriftform — elektronische Form ausgeschlossen | direkt nein; § 46h ArbGG im Prozess prüfen |
| Arbeitszeugnis (§ 109 GewO) | Schriftform — elektronische Form ausgeschlossen | **Nein** |

## Templates und Hinweise

### Mandantenhinweis Arbeitgeber

```
Hinweis zur Befristung von Arbeitsverträgen — Stand 2026:

Eine befristete Arbeitsvertragsabrede ist nach § 14 Abs. 4 TzBfG
nur dann wirksam, wenn sie schriftlich (§ 126 BGB) vor Aufnahme
der Arbeit vorliegt.

Wirksame Varianten:
1. Papier mit eigenhändiger Unterschrift beider Parteien
2. Qualifizierte elektronische Signatur (qES) beider Parteien
 über einen nach eIDAS-VO zertifizierten Anbieter
 (z. B. DocuSign mit qES-Zertifikat, bestätigt durch
 Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

NICHT ausreichend (Befristung unwirksam, Vertrag unbefristet):
- eingescannte Unterschrift im PDF
 Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- einfache elektronische Signatur ohne qES-Zertifikat
- Maus- oder Touch-Signatur ohne Zertifikat
- E-Mail-Bestätigung ohne qES

Wichtig für Kündigung und Aufhebungsvertrag (§ 623 BGB):
Direkte elektronische Form ist ausgeschlossen. Papier mit eigenhändiger
Unterschrift bleibt Standard. Nur in einem arbeitsgerichtlichen Verfahren
ist zusätzlich § 46h ArbGG als Formfiktion zu prüfen, wenn die Erklärung
klar in einem elektronischen vorbereitenden Schriftsatz enthalten ist.
```

### Mandantenhinweis Arbeitnehmer

```
Hinweis zur Befristung Ihres Arbeitsvertrags:

Wurde Ihr Arbeitsvertrag elektronisch unterzeichnet oder per
PDF mit eingescannter Unterschrift übermittelt?

Prüfen Sie:
- War eine qualifizierte elektronische Signatur (qES) im Einsatz?
 (Erkennbar am eIDAS-zertifizierten Anbieter wie DocuSign-qES,
 Bundesdruckerei, D-Trust, GlobalSign-qES o.ä. — nicht
 identisch mit "einfacher" DocuSign-Signatur ohne qES)
- Oder nur eine eingescannte Unterschrift / einfache elektronische
 Signatur?

Wenn nur eingescannt oder einfach signiert:
Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
und ArbG Berlin). Ihr Vertrag gilt nach § 16 TzBfG als unbefristet.

Achtung: Sie müssen binnen 3 Wochen nach dem vereinbarten
Befristungsende Klage erheben (§ 17 TzBfG — Entfristungsklage).
```

### Beweissicherung qES — Checkliste

```
□ qES-Datei (z. B. signiertes PDF) im Original archivieren
□ Signaturzertifikat extrahieren und gesondert sichern
□ Zertifikatsanbieter dokumentieren
□ Zeitpunkt der Signatur (Timestamp) erfassen
□ Bestätigungsmail des Signaturdienstes archivieren
□ Bei Vertrag: jeweils ein qES-signiertes Dokument beider Seiten
□ Prüfprotokoll des Signaturdienstes herunterladen
□ Aufbewahrungsdauer mindestens bis 3 Monate nach Vertragsende
 plus 3-Wochen-Klagefrist Puffer
```

## Strategische Hinweise

- Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- **Arbeitnehmerseite**: Bei elektronischer Befristung sehr genau prüfen, ob es eine echte qES war oder nur eine einfache elektronische Signatur. Im Zweifel Entfristungsklage erwägen.
- **Mischformen**: Wenn ein Vertrag teilweise eigenhändig (Arbeitgeber) und teilweise qES (Arbeitnehmer) unterzeichnet wurde, ist die Lage unklar. § 126a Abs. 2 BGB verlangt grundsätzlich elektronische Form für beide Seiten. Saubere Lösung: einheitliche Form.
- **Kündigung nicht direkt elektronisch**: § 623 BGB schließt die elektronische Form ausdrücklich aus. qES-DocuSign-Kündigungen, E-Mails und beA-Nachrichten außerhalb einer gesetzlichen Formfiktion sind kein sicherer Kündigungsweg.
- **§ 46h ArbGG separat prüfen**: Bei arbeitsgerichtlichen Schriftsätzen kann die neue Formfiktion tragen; sie ersetzt aber nicht Zustellung, Vollmacht, Klarerkennbarkeit und § 174 BGB.

## Querverweise

- → `schriftform-paragraph-126-bgb-eigenhaendige-unterschrift`
- → `elektronische-form-paragraph-126a-bgb-qes`
- → `arbeitsrecht-befristung-und-aufhebung-paragraph-14-tzbfg-623-bgb`
- → `kuendigung-per-schriftsatz-zustellung-formfragen`
- → `textform-paragraph-126b-bgb-dauerhafter-datentraeger`
- → `form-checker-fuer-vertrag-oder-willenserklaerung`
- → `mandantenwarnung-qes-per-email-whatsapp-und-zugang`

## 3. `spezial-rechtsprechung-livecheck-formfragen`

**Fokus:** Livecheck verifizierter Rechtsprechung zu Schriftform, qES und beA: führt schnell durch Sachverhalt, Rechtsgrundlagen, Belege, Risiken und erzeugt einen verwertbaren nächsten Output.

# Livecheck verifizierter Rechtsprechung zu Schriftform, qES und beA

## Aufgabe
Dieser Skill ersetzt einen zu groben Spezial-Slot durch einen konkreten Fachim Plugin `schriftform-und-textform-bgb`. Kontext des Plugins: Formerfordernisse im deutschen Zivilrecht: Schriftform, Textform, qES, Zugang, beA/ERV und Prozessordnungen. Mit Checklisten, Dokumentation und Rechtsprechung nur nach Live-Verifikation.

Er arbeitet nicht lexikalisch, sondern fallbezogen: Er trennt zuerst Rollen, Ziel, Fristen, Zuständigkeiten und Belege, prüft dann die fachlichen Weichen und liefert ein Ergebnis, mit dem weitergearbeitet werden kann.

## Einstieg
Wenn Material vorliegt, nutze es zuerst. Frage nur nach, was für die nächste Entscheidung fehlt:

1. Wer handelt in welcher Rolle und gegen wen?
2. Welches praktische Ziel soll erreicht werden?
3. Welche Fristen, Termine, Zustellungen, Schwellenwerte oder Sanktionen stehen im Raum?
4. Welche Unterlagen, Daten, Registerauszüge, Bescheide, Verträge, Screenshots oder sonstigen Belege liegen vor?
5. Soll der Output intern, für Mandantschaft, Behörde, Gericht, Gegnerseite oder Gremium formuliert werden?

## Arbeitsworkflow
1. **Sortieren:** Sachverhalt, Dokumente und offene Punkte in eine knappe Fallmatrix bringen.
2. **Rechtsrahmen:** Einschlägige Normen, Zuständigkeiten, Verfahren, Fristen und formelle Anforderungen live prüfen, soweit Aktualität tragend ist.
3. **Materielle Weichen:** Die Kernfragen zu **Livecheck verifizierter Rechtsprechung zu Schriftform, qES und beA** mit Tatbestandsmerkmalen, Belegen, Gegenargumenten und typischen Praxisfehlern abarbeiten.
4. **Risikoampel:** Ergebnis in Grün/Gelb/Rot mit Begründung, Unsicherheiten und Beweisbedarf einordnen.
5. **Anschluss:** Passende weitere Skills desselben Plugins vorschlagen, wenn Spezialprüfung, Schriftsatz, Tabelle, Brief oder Verhandlungsstrategie sinnvoll ist.

## Output-Standard
- Kurzbild in fünf Sätzen: Lage, Ziel, Frist, Risiko, nächster Schritt.
- Prüfmatrix mit Punkt, Norm/Quelle, Tatsachen, Beleg, Bewertung, To-do.
- Konkreter Textbaustein oder Arbeitsprodukt passend zur Lage: Memo, Mandantenbrief, Behörden-/Gerichtsschreiben, Checkliste, Tabelle oder Verhandlungsagenda.
- Keine Scheingenauigkeit: Annahmen, Lücken und Live-Check-Bedarf offen markieren.

## Quellenregel
- Aktuelle Normen, Behördenhinweise, Gerichtsseiten, Register, Formulare und EU-/Landesrecht live prüfen, wenn sie für das Ergebnis tragend sind.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle ausgeben.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate aus Modellwissen.
- Paywall-Literatur nur verwenden, wenn die Nutzerin oder der Nutzer den Text selbst bereitstellt; dann nicht als frei verifizierte Quelle ausgeben.
