---
name: inv-geschaeftsgeheimnisse-stpo
description: "Inv 008 Geschaeftsgeheimnisse, Inv 009 Stpo Beschlagnahme: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nächsten belastbaren Output."
---

# Inv 008 Geschaeftsgeheimnisse, Inv 009 Stpo Beschlagnahme

## Arbeitsbereich

Dieser Skill bündelt **Inv 008 Geschaeftsgeheimnisse, Inv 009 Stpo Beschlagnahme** zu einem konkreten Arbeitsgang. Starte mit dem Modul, das die Tatsachen der Akte trägt; weitere Module nur hinzunehmen, wenn sie dieselbe Frist, Zuständigkeit, Beweislast oder denselben Output betreffen.

## Arbeitsmodule

| Arbeitsmodul | Fokus |
| --- | --- |
| `inv-008-geschaeftsgeheimnisse` | Schützt Untersuchungsergebnisse und Unternehmensinterna als Geschäftsgeheimnisse – GeschGehG, § 17 UWG a.F., strafrechtlicher Schutz. |
| `inv-009-stpo-beschlagnahme` | Analysiert Beschlagnahmerisiken nach StPO, Schutzstrategien für Anwaltsunterlagen und Verhalten bei Durchsuchung. |

## Arbeitsweg

Für **Inv 008 Geschaeftsgeheimnisse, Inv 009 Stpo Beschlagnahme** zuerst das Arbeitsmodul wählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Im Plugin `internal-investigations-praxis` bleiben Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschter Output getrennt; Module nur kombinieren, wenn dieselbe Akte mehrere dieser Punkte trägt. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Arbeitsmodule im Detail

## 1. `inv-008-geschaeftsgeheimnisse`

**Fokus:** Schützt Untersuchungsergebnisse und Unternehmensinterna als Geschäftsgeheimnisse – GeschGehG, § 17 UWG a.F., strafrechtlicher Schutz.

# Schutz von Geschäftsgeheimnissen in Internal Investigations

## Rechtlicher Rahmen

Untersuchungsberichte, Interviewprotokolle und forensische Analyseergebnisse können Geschäftsgeheimnisse des Unternehmens sein und genießen Schutz nach dem Gesetz zum Schutz von Geschäftsgeheimnissen (GeschGehG, [gesetze-im-internet.de](https://www.gesetze-im-internet.de/geschgehg/)), das die EU-Richtlinie 2016/943 ([eur-lex.europa.eu](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX%3A32016L0943)) umsetzt. Der strafrechtliche Schutz ergibt sich aus §§ 203, 204 StGB sowie aus § 23 GeschGehG. Gleichzeitig können Mitarbeiter, die im Rahmen einer Untersuchung rechtswidrig erlangte Geheimnisse weitergeben, sich nach § 4 GeschGehG haftbar machen, es sei denn, sie sind durch das HinSchG oder § 5 GeschGehG geschützt.

## Ziel dieses Skills

Dieser Skill klärt, welche Untersuchungsergebnisse als Geschäftsgeheimnisse zu qualifizieren sind, welche Schutzmaßnahmen erforderlich sind und wo der Schutz an Grenzen stößt – insbesondere wenn Whistleblower oder Behörden involviert sind.

## Arbeitsprogramm

### 1. Definition Geschäftsgeheimnis nach GeschGehG
- § 2 Nr. 1 GeschGehG: Information muss (a) geheim sein, (b) wirtschaftlichen Wert haben und (c) durch angemessene Geheimhaltungsmaßnahmen geschützt sein.
- Praxistest: Ist der Untersuchungsbericht als „Confidential – Attorney-Client Privilege" gekennzeichnet? Sind Zugriffsrechte beschränkt? Gibt es NDAs für externe Berater?
- Keine Schutzfähigkeit ohne Schutzmaßnahmen – passive Geheimhaltung reicht nicht.

### 2. Schutzmaßnahmen für Untersuchungsunterlagen
- Wasserzeichen und Versionskontrolle auf allen Berichten.
- Zugriffsbeschränkung: nur Need-to-know-Verteiler; technische Zugangsbeschränkung (DRM, Passwortschutz).
- NDAs für alle externen Berater, Forensiker, Wirtschaftsprüfer (§ 5 Nr. 2 GeschGehG: Offenbarung im Rahmen einer beruflichen Schweigepflicht ggf. erlaubt).
- Physische Sicherung: ausgedruckte Berichte in Tresor; keine Ablage auf ungesicherten Netzlaufwerken.

### 3. Offenbarung gegenüber Behörden
- Selbst-Reporting an BaFin, Staatsanwaltschaft, DOJ: Offenbarung von Geschäftsgeheimnissen an Behörden ist nach § 5 Nr. 2 GeschGehG zulässig, wenn dies zur Aufdeckung einer rechtswidrigen Handlung erforderlich ist.
- Vorbereitung: Vor Herausgabe klären, welche Teile des Berichts Geschäftsgeheimnisse enthalten, und Schutzantrag (In-camera-Verfahren) stellen.
- Drittstaatliche Behörden (DOJ, SEC): Herausgabe bedarf DSGVO-Rechtsgrundlage und ist mit Unternehmensinteressen abzuwägen.

### 4. Whistleblower-Schutz und GeschGehG-Grenze
- § 5 Nr. 2 GeschGehG: Kein Geheimnisschutz, wenn Offenbarung zur Aufdeckung rechtswidrigen Verhaltens dient (Whistleblower-Ausnahme).
- HinSchG 2023 ([gesetze-im-internet.de](https://www.gesetze-im-internet.de/hinschg/)): Hinweisgeber sind vor Repressalien geschützt, wenn sie in gutem Glauben berichten.
- EU-Richtlinie 2019/1937 ([eur-lex.europa.eu](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX%3A32019L1937)): Schutz auch bei Weitergabe von Geschäftsgeheimnissen, wenn Whistleblower zur Aufdeckung eines Verstoßes handelt.
- BGH-Rechtsprechung zum Whistleblower-Schutz: BGH, Urt. v. 3.7.2003 – I ZR 4/01 (zu § 17 UWG a. F.): Arbeitnehmer, der Straftaten anzeigt, handelt nicht pflichtwidrig.

### 5. Kriminelle Nutzung von Untersuchungsergebnissen
- Konkurrent, der durch Social Engineering oder Datenleck an Untersuchungsbericht gelangt: § 23 GeschGehG (strafrechtlicher Schutz).
- Insiderhandel: wenn Untersuchungsergebnis kursrelevante Information enthält und unkontrolliert bekannt wird → § 119 WpHG i. V. m. MAR Art. 14 ([eur-lex.europa.eu](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX%3A32014R0596)).

### 6. § 203 StGB und externe Berater
- Anwälte, Steuerberater, Ärzte: berufliche Schweigepflicht schützt auch in Untersuchungen erhaltene Informationen ([gesetze-im-internet.de](https://www.gesetze-im-internet.de/stgb/__203.html)).
- IT-Forensiker ohne Berufsgeheimnis: brauchen NDA und vertragliche Geheimhaltungspflicht.
- Strafbarkeit nach § 203 StGB bei unbefugter Offenbarung; Strafantrag durch das Unternehmen möglich.

### 7. Datenräume und sichere Bereitstellung
- Aufbau eines Secure Data Room für Berater, Behörden, US-Counsel (vgl. inv-022-data-room-for-counsel).
- Technische Sicherheit: End-to-end-Verschlüsselung, keine Downloadmöglichkeit, Wasserzeichen.
- Protokollierung jedes Zugriffs für spätere Nachweisführung.

## Red-Team-Fragen

- Ist der Untersuchungsbericht als Geschäftsgeheimnis qualifizierbar – wurden alle drei GeschGehG-Voraussetzungen aktiv erfüllt?
- Wurde bei der Übergabe an externe Berater eine NDA abgeschlossen und dokumentiert?
- Könnte ein Whistleblower die § 5 Nr. 2 GeschGehG-Ausnahme in Anspruch nehmen und den Bericht rechtmäßig an Behörden weitergeben?
- Enthält der Bericht kursrelevante Informationen, die Insiderhandelsrisiken begründen?
- Wurden Zugangsprotokolle für den Data Room lückenlos geführt?
- Hat das Unternehmen bei drohender Beschlagnahme einen Schutzantrag (In-camera) vorbereitet?

## Normenregister

| Norm | Inhalt | Quelle |
|---|---|---|
| GeschGehG | Geschäftsgeheimnisschutz | [gesetze-im-internet.de](https://www.gesetze-im-internet.de/geschgehg/) |
| § 203 StGB | Verletzung von Privatgeheimnissen | [gesetze-im-internet.de](https://www.gesetze-im-internet.de/stgb/__203.html) |
| § 23 GeschGehG | Strafbarkeit Geheimnisverrat | [gesetze-im-internet.de](https://www.gesetze-im-internet.de/geschgehg/__23.html) |
| HinSchG § 5 | Schutz des Hinweisgebers | [gesetze-im-internet.de](https://www.gesetze-im-internet.de/hinschg/) |
| EU-RL 2016/943 | Geschäftsgeheimnisrichtlinie | [eur-lex.europa.eu](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX%3A32016L0943) |

## Ausgabeformate

- **Geschäftsgeheimnis-Schutzkonzept** für Untersuchungsunterlagen
- **NDA-Vorlage** für externe Berater und Forensiker
- **Geheimhaltungs-Checkliste** (GeschGehG § 2 Nr. 1)
- **Whistleblower-Risikoanalyse** (§ 5 GeschGehG vs. HinSchG)
- **Secure-Data-Room-Anforderungsliste**

Rechtsprechungszitate nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle.

## 2. `inv-009-stpo-beschlagnahme`

**Fokus:** Analysiert Beschlagnahmerisiken nach StPO, Schutzstrategien für Anwaltsunterlagen und Verhalten bei Durchsuchung.

# StPO-Beschlagnahme und Durchsuchung

## Rechtlicher Rahmen

Die Beschlagnahme von Unterlagen und Gegenständen im Rahmen strafrechtlicher Ermittlungen richtet sich nach §§ 94–111 StPO ([gesetze-im-internet.de](https://www.gesetze-im-internet.de/stpo/__94.html)). Für Internal Investigations besonders relevant sind § 97 StPO (Beschlagnahmeschutz für bestimmte Unterlagen, [gesetze-im-internet.de](https://www.gesetze-im-internet.de/stpo/__97.html)) und § 103 StPO (Durchsuchung bei Dritten, [gesetze-im-internet.de](https://www.gesetze-im-internet.de/stpo/__103.html)). Der Schutz des § 97 StPO greift jedoch nicht unbegrenzt – insbesondere nicht, wenn Unterlagen im Gewahrsam des Unternehmens (als potenziell Beschuldigter) liegen und der Anwalt das Unternehmen, nicht einen individuellen Beschuldigten, vertritt.

## Ziel dieses Skills

Dieser Skill bereitet auf Durchsuchungs- und Beschlagnahme-Szenarien vor, analysiert, welche Unterlagen schutzwürdig sind, und definiert Verhaltenspflichten für den Zeitpunkt der Durchsuchung.

## Arbeitsprogramm

### 1. Beschlagnahmefähige Gegenstände (§ 94 StPO)
- Alle Gegenstände, die als Beweismittel für die Untersuchung von Bedeutung sein können, sind beschlagnahmefähig.
- Dokumente, E-Mails, IT-Systeme, forensische Images, Buchhaltungsunterlagen.
- Freiwillige Herausgabe ist möglich und empfehlenswert (kooperatives Verhalten gegenüber Behörden).

### 2. Beschlagnahmeschutz (§ 97 StPO)
- **Geschützt**: schriftlicher Verkehr zwischen Beschuldigtem und Verteidiger (§ 97 Abs. 1 Nr. 1 StPO).
- **Nicht geschützt**: Unterlagen des Unternehmens beim Anwalt, wenn das Unternehmen selbst als potenziell Beschuldigter/Nebenbeteiligter gilt (BGH, Beschl. v. 5.4.2017 – StB 3/17, [bgh.de](https://www.bgh.de/)).
- Praxisrelevanz: Untersuchungsbericht beim mandatierten Anwalt ist nicht automatisch nach § 97 StPO geschützt.
- Trennung: Work-Product des Anwalts (rechtliche Bewertungen) kann besser geschützt sein als reine Tatsachenzusammenfassungen.

### 3. Durchsuchungsablauf (§§ 102–105 StPO)
- **Durchsuchungsbeschluss** prüfen: Wird ein richterlicher Beschluss vorgelegt? (§ 105 Abs. 1 StPO)
- Bei Gefahr im Verzug: Staatsanwaltschaft oder Polizei können ohne richterlichen Beschluss durchsuchen (§ 105 Abs. 1 S. 2 StPO).
- **Zeuge**: Betriebsvertreter und möglichst Anwalt hinzuziehen (§ 106 StPO, [gesetze-im-internet.de](https://www.gesetze-im-internet.de/stpo/__106.html)).
- Durchsuchung nur im angegebenen Zweck; Überschreitung ist anfechtbar.

### 4. Verhalten bei Durchsuchung – Protokoll
- Sofort Anwalt benachrichtigen (interner und externer Krisenplan).
- Keine Aussagen gegenüber Ermittlern ohne Anwesenheit des Anwalts.
- Inventarliste der beschlagnahmten Gegenstände verlangen (§ 107 StPO, [gesetze-im-internet.de](https://www.gesetze-im-internet.de/stpo/__107.html)).
- Widerspruch gegen Beschlagnahme privilegierter Unterlagen sofort protokollieren und anfechtbar machen (§ 98 Abs. 2 StPO).
- Mitarbeiter: keine eigenständigen Auskünfte; Verweisung auf den Anwalt.

### 5. Anfechtung und Sicherungsmaßnahmen
- Gerichtliche Überprüfung der Beschlagnahme nach § 98 Abs. 2 StPO (Beschwerde beim LG).
- Antrag auf Aussonderung privilegierter Unterlagen (In-camera-Verfahren).
- Sicherungskopie der beschlagnahmten Dokumente als Beleg für Vollständigkeit anfertigen lassen.

### 6. Parallele Durchsuchungen bei Dritten
- § 103 StPO: Durchsuchung bei Personen, die Beschuldigter nicht sind (z. B. Wirtschaftsprüfer, Steuerberater).
- Externe Berater vorbereiten: Was tun, wenn Strafverfolgungsbehörden bei Wirtschaftsprüfer erscheinen?
- Abstimmung mit Wirtschaftsprüfer über Herausgabe vs. Schutz von Mandatsunterlagen.

### 7. Dawn Raid vs. reguläre Durchsuchung
- Dawn Raid (Morgen-Durchsuchung): koordinierte gleichzeitige Durchsuchungen an mehreren Standorten.
- Krisenplan muss vor einem Dawn Raid vorliegen (vgl. inv-021-dawn-raid-playbook).
- Kommunikationsplan: Wer informiert wen (Vorstand, Aufsichtsrat, PR, externe Anwälte)?

## Red-Team-Fragen

- Liegt ein Krisenplan für den Fall einer Durchsuchung vor, und ist er allen Schlüsselpersonen bekannt?
- Wurden alle Interviewprotokolle und Berichte so dokumentiert, dass eine Unterscheidung zwischen privilegierten und nicht-privilegierten Teilen möglich ist?
- Ist der externe Anwalt 24/7 erreichbar und über den Stand der Untersuchung informiert?
- Wurde die Inventarliste beschlagnahmter Gegenstände sorgfältig dokumentiert?
- Gibt es Unterlagen beim Wirtschaftsprüfer, die nicht durch Anwaltsgeheimnis geschützt sind und beschlagnahmt werden könnten?
- Wurde gegen eine etwaige Beschlagnahme privilegierter Unterlagen sofort Widerspruch eingelegt?

## Normenregister

| Norm | Inhalt | Quelle |
|---|---|---|
| § 94 StPO | Beschlagnahmefähige Gegenstände | [gesetze-im-internet.de](https://www.gesetze-im-internet.de/stpo/__94.html) |
| § 97 StPO | Beschlagnahmeschutz | [gesetze-im-internet.de](https://www.gesetze-im-internet.de/stpo/__97.html) |
| § 102 StPO | Durchsuchung bei Beschuldigtem | [gesetze-im-internet.de](https://www.gesetze-im-internet.de/stpo/__102.html) |
| § 103 StPO | Durchsuchung bei Dritten | [gesetze-im-internet.de](https://www.gesetze-im-internet.de/stpo/__103.html) |
| § 105 StPO | Richterlicher Beschluss | [gesetze-im-internet.de](https://www.gesetze-im-internet.de/stpo/__105.html) |
| § 107 StPO | Inventarliste Beschlagnahme | [gesetze-im-internet.de](https://www.gesetze-im-internet.de/stpo/__107.html) |

## Ausgabeformate

- **Durchsuchungs-Krisenplan** (Ablauf, Verantwortlichkeiten, Kontakte)
- **Verhalten-bei-Durchsuchung-Brief** für Mitarbeiter
- **Privilegierungsanalyse** (§ 97 StPO) für vorliegende Unterlagen
- **Beschwerde nach § 98 Abs. 2 StPO** (Musterschriftsatz)
- **Inventarlisten-Vorlage**

Rechtsprechungszitate nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle.
