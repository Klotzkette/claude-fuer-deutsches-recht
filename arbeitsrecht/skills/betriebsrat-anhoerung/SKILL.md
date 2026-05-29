---
name: betriebsrat-anhoerung
description: "Prüft und dokumentiert die ordnungsgemäße Anhörung des Betriebsrats vor Kündigungen nach § 102 BetrVG. Lädt, wenn die Wirksamkeit einer BR-Anhörung (Inhalt, Fristen, Reaktion des BR) beurteilt oder ein Anhörungsschreiben erstellt werden soll."
---

# Betriebsratsanhörung vor Kündigung (§ 102 BetrVG)

## Zweck

Dieser Skill dient der Prüfung und Durchführung der Betriebsratsanhörung nach § 102 BetrVG als notwendige Wirksamkeitsvoraussetzung jeder Arbeitgeberkündigung in Betrieben mit Betriebsrat. Die fehlerhafte oder unterbliebene Anhörung führt nach § 102 Abs. 1 Satz 3 BetrVG zwingend zur Unwirksamkeit der Kündigung – unabhängig davon, ob ein Kündigungsschutzrecht im Übrigen besteht. Der Skill ist einschlägig bei der Prüfung einer erhaltenen Kündigung (Arbeitnehmerperspektive), beim Entwurf des Anhörungsschreibens (Arbeitgeberperspektive) sowie bei der Frage des Widerspruchsrechts des BR (§ 102 Abs. 3 BetrVG) und des Weiterbeschäftigungsanspruchs (§ 102 Abs. 5 BetrVG).

## Eingaben

1. **Art der Kündigung**: ordentlich oder außerordentlich (Frist unterscheidet sich!)
2. **Betrieb**: Betriebsstruktur, Anzahl BR-Mitglieder, BR-Vorsitzender
3. **Arbeitnehmer**: Name, Funktion, Sozialdaten (Alter, Betriebszugehörigkeit, Familienstand, Unterhaltspflichten, Schwerbehinderung)
4. **Kündigungsgrund**: betriebsbedingt, personenbedingt oder verhaltensbedingt; konkrete Sachverhaltsdarstellung
5. **Zeitplan**: Wann soll Kündigung ausgesprochen werden? (Rückwärtsrechnung der Fristen)
6. **Reaktion des BR**: Stellungnahme, Schweigen, Widerspruch (§ 102 Abs. 3 BetrVG)?
7. **Anhörungsunterlagen** (bei Prüfung aus Arbeitnehmersicht): Anhörungsschreiben, Stellungnahme des BR, Protokoll der BR-Sitzung

## Rechtlicher Rahmen

### Kernvorschriften

- § 102 Abs. 1 Satz 1 BetrVG: Anhörungspflicht vor jeder Kündigung
- § 102 Abs. 1 Satz 2 BetrVG: Pflicht zur Mitteilung der Gründe; Inhalt der Mitteilung
- § 102 Abs. 1 Satz 3 BetrVG: Sanktion – ohne ordnungsgemäße Anhörung ist die Kündigung unwirksam (absolute Unwirksamkeitsfolge)
- § 102 Abs. 2 BetrVG: Fristen (1 Woche bei ordentlicher Kündigung, 3 Tage bei außerordentlicher Kündigung; Verlängerung bei Aufklärungsbedarf nicht zulässig; Frist beginnt mit Zugang des vollständigen Anhörungsschreibens)
- § 102 Abs. 3 BetrVG: Widerspruchsrecht des BR bei ordentlicher Kündigung (abschließende Gründe in Nr. 1–5)
- § 102 Abs. 5 BetrVG: Weiterbeschäftigungsanspruch des Arbeitnehmers bis zum rechtskräftigen Abschluss des Kündigungsschutzverfahrens, wenn BR widersprochen hat und Klage erhoben wurde
- § 99 BetrVG: Mitbestimmung bei Einstellung (zum Vergleich und zum Verständnis der Abgrenzung)

### Leitentscheidungen (BGH-Stil)

- **Inhalt der Anhörungsmitteilung / subjektive Determinierung:**
  BAG, Urteil vom 27.02.1997 - 2 AZR 302/96: Der Arbeitgeber muss dem Betriebsrat die Umstaende mitteilen, die seine Kuendigungsentscheidung tatsaechlich bestimmt haben; auch dem AG bekannte, fuer den AN guenstige Umstaende sind grundsaetzlich mitzuteilen. Quelle: dejure.org-Vernetzung BAG 27.02.1997 - 2 AZR 302/96.
  BAG, Urteil vom 05.02.1998 - 2 AZR 227/97: Praezisierung der subjektiven Determinierung; objektiv relevante Umstaende duerfen nicht zurueckgehalten werden. Quelle: dejure.org-Vernetzung.

- **Fristbeginn / Vollstaendigkeit der Unterlagen:**
  BAG, Urteil vom 10.10.2002 - 2 AZR 472/01: Bei Nachreichung relevanter Informationen beginnt die Stellungnahmefrist neu. Quelle: dejure.org-Vernetzung.

- **Widerspruch des BR / Weiterbeschaeftigung:**
  Hier weitere Rechtsprechung zur § 102 Abs. 5 BetrVG-Weiterbeschaeftigung vor Schriftsatzverwendung in dejure.org / openjur.de / bundesarbeitsgericht.de verifizieren.

- **Nachschieben von Kuendigungsgruenden:**
  Standardrechtsprechung: Nachschieben grundsaetzlich nur fuer Kuendigungsgruende, die im Zeitpunkt der Anhoerung bereits objektiv vorlagen und dem Arbeitgeber bekannt waren - vor Zitat konkretes BAG-Aktenzeichen in dejure.org verifizieren.

### Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Ablauf

### Schritt 1 – Prüfung: Betriebsrat vorhanden?

- Existiert ein gewählter Betriebsrat im Betrieb des Arbeitgebers (§§ 1 ff. BetrVG)?
- Achtung: Maßgeblich ist der **Betrieb** (nicht das Unternehmen), in dem der Arbeitnehmer tätig ist.
- Kein BR → keine Anhörungspflicht nach § 102 BetrVG (aber ggf. andere Beteiligungsrechte, z. B. bei Gemeinsamen Betrieben, § 47 BetrVG, Konzernbetriebsrat § 58 BetrVG).

### Schritt 2 – Inhalt des Anhörungsschreibens (§ 102 Abs. 1 Satz 2 BetrVG)

Das Anhörungsschreiben muss folgende Angaben enthalten:

| Inhaltspunkt | Anforderung |
|---|---|
| **Personalien** | Name, Funktion, Abteilung des Arbeitnehmers |
| **Sozialdaten** | Alter, Betriebszugehörigkeit, Familienstand, Unterhaltspflichten, Schwerbehinderungsgrad (sofern bekannt) |
| **Art der Kündigung** | ordentlich oder außerordentlich; fristlos oder fristgerecht |
| **Beendigungstermin** | Datum der beabsichtigten Beendigung (bei ordentlicher Kündigung unter Nennung der Frist) |
| **Kündigungsgründe** | Konkrete Sachverhaltsdarstellung (bei personenbedingter/verhaltensbedingter Kündigung: alle maßgeblichen Tatsachen; bei betriebsbedingter Kündigung: Darstellung der unternehmerischen Entscheidung und des Wegfalls des Beschäftigungsbedarfs) |
| **Vorherige Abmahnungen** | (bei verhaltensbedingter Kündigung) Datum, Inhalt der Abmahnungen |
| **Sozialauswahl** | (bei betriebsbedingter Kündigung) Auswahlkriterien und Entscheidungsergebnis |

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

### Schritt 3 – Fristen (§ 102 Abs. 2 BetrVG)

| Kündigungsart | Frist | Fristbeginn |
|---|---|---|
| Ordentliche Kuendigung | 1 Woche (§ 102 Abs. 2 Satz 1 BetrVG) | Zugang des vollstaendigen Anhoerungsschreibens beim Vorsitzenden, § 26 Abs. 2 BetrVG |
| Außerordentliche Kündigung | 3 Tage | Zugang des vollständigen Anhörungsschreibens |

- **Fristablauf ohne Stellungnahme des BR** → Arbeitgeber kann kündigen (§ 102 Abs. 2 Satz 2 BetrVG: BR gilt als angehört).
- **Keine Verlängerung** der Frist durch Arbeitgeber möglich.
- **Vorzeitige Stellungnahme des BR** → Arbeitgeber kann sofort kündigen.
- **Fristvorgabe**: Kündigung darf erst ausgesprochen werden, nachdem die Frist abgelaufen ist oder der BR abschließend Stellung genommen hat; Kündigung vor Fristablauf → unwirksam (§ 102 Abs. 1 Satz 3 BetrVG).

### Schritt 4 – Reaktion des Betriebsrats

**A. Zustimmung / keine Stellungnahme:** Kündigung kann nach Fristablauf ausgesprochen werden.

**B. Bedenken (§ 102 Abs. 2 Satz 1 BetrVG):** BR teilt Bedenken mit; Arbeitgeber kann dennoch kündigen; muss Bedenken dem Arbeitnehmer bei der Kündigung mitteilen (§ 102 Abs. 2 Satz 4 BetrVG).

**C. Widerspruch (§ 102 Abs. 3 BetrVG):** Nur bei **ordentlicher** Kündigung möglich; Widerspruchsgründe abschließend (Nr. 1–5: Verstoß gegen Auswahlrichtlinie, Weiterbeschäftigung auf freiem Arbeitsplatz, Sozialauswahl fehler, Umsetzungsmöglichkeit, Umschulung/Fortbildung); muss schriftlich, innerhalb der 1-Wochen-Frist erfolgen; Widerspruch ermöglicht Weiterbeschäftigungsanspruch nach § 102 Abs. 5 BetrVG.

### Schritt 5 – Weiterbeschäftigungsanspruch (§ 102 Abs. 5 BetrVG)

- Voraussetzungen: Wirksamer BR-Widerspruch (form- und fristgerecht, § 102 Abs. 3 BetrVG) + Erhebung der Kündigungsschutzklage.
- Anspruch: Weiterbeschäftigung zu unveränderten Bedingungen bis Rechtskraft des Urteils.
- **Ausnahme (Antrag des Arbeitgebers § 102 Abs. 5 Satz 2 BetrVG):** Arbeitsgericht kann Arbeitgeber von Weiterbeschäftigungspflicht entbinden, wenn Klage keine hinreichende Aussicht auf Erfolg hat, die Kündigung nicht offensichtlich unwirksam ist oder die Weiterbeschäftigung zu einer unzumutbaren wirtschaftlichen Belastung führt.

### Schritt 6 – Fehlerhaftigkeitsprüfung aus Arbeitnehmersicht

Checkliste für die Prüfung:
- Wurde der BR überhaupt angehört? (Nachweis durch Arbeitgeber)
- Waren die Sozialdaten vollständig und richtig?
- War die Kündigungsgrunddarstellung ausreichend konkret?
- Wurde die Frist eingehalten (Kündigung erst nach Fristablauf)?
- Wurde ggf. ein Widerspruch fristgerecht erhoben?
- Hat der Arbeitgeber einen Widerspruch bei der Kündigung mitgeteilt?

## Ausgabeformat

- **Standardausgabe**: Memo im Gutachtenstil mit Checkliste der Anhörungsanforderungen.
- **Auf Anforderung**: Vollständiges Anhörungsschreiben (Urteilsstil, alle Pflichtangaben).
- **Auf Anforderung**: Prüfschema Anhörungsfehler als Tabelle (Arbeitnehmerperspektive).

## Beispiel

**Sachverhalt:** Arbeitgeberin C-GmbH will Arbeitnehmer D (Buchhalter, 10 Jahre BZ, 44 Jahre alt, verheiratet, 2 Kinder, keine Schwerbehinderung) betriebsbedingt kündigen wegen Wegfalls seiner Stelle (Outsourcing der Buchhaltung). Der Betriebsrat besteht aus 5 Mitgliedern.

**Anhörungsschreiben (Auszug):**

> "Betreff: Anhörung nach § 102 BetrVG – Beabsichtigte ordentliche betriebsbedingte Kündigung von Herrn D
>
> Wir beabsichtigen, das Arbeitsverhältnis mit Herrn D, geb. [Datum], Buchhalter, seit [Datum] beschäftigt, verheiratet, 2 unterhaltsberechtigte Kinder, zum [Datum] ordentlich zu kündigen.
>
> Grund: Die C-GmbH hat beschlossen, die gesamte Buchhaltung mit Wirkung zum [Datum] an den externen Dienstleister E-GmbH auszulagern. Infolge dieser unternehmerischen Entscheidung entfällt der Beschäftigungsbedarf für die Position des Herrn D dauerhaft. Eine anderweitige Beschäftigungsmöglichkeit im Unternehmen besteht nicht. [Sozialauswahl: Herr D ist der einzige Buchhalter auf dieser Hierarchieebene; vergleichbare Arbeitnehmer, die in die Sozialauswahl einzubeziehen wären, sind nicht vorhanden.]
>
> Wir bitten um Stellungnahme innerhalb von einer Woche nach Zugang dieses Schreibens."

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Risiken und typische Fehler

| Fehler | Konsequenz | Abhilfe |
|---|---|---|
| Keine Anhörung des BR | § 102 Abs. 1 Satz 3 BetrVG: Kündigung unwirksam | Anhörung immer vor Ausspruch der Kündigung |
| Unvollständige Sozialdaten | Kündigung unwirksam (Fitting, BetrVG, 32. Aufl. 2024, § 102 Rn. 45) | Alle bekannten Sozialdaten aufnehmen |
| Pauschaler Kündigungsgrund ohne Sachverhaltsdarstellung | Anhörung unzureichend, Kündigung unwirksam | Konkrete Tatsachen schildern |
| Kündigung vor Ablauf der Anhörungsfrist | Unwirksamkeit | Frist genau berechnen, Kündigung erst danach |
| Vergessen: 3-Tage-Frist bei außerordentlicher Kündigung | Unwirksamkeit | Fristenkalender bei außerordentlichen Kündigungen besonders prüfen |
| Nachschieben nicht angehörter Gründe | Im Prozess unbeachtlich | Alle Kündigungsgründe bereits im Anhörungsschreiben benennen |
| BR-Widerspruch nicht an Arbeitnehmer weitergegeben | Formfehler, § 102 Abs. 2 Satz 4 BetrVG | Widerspruch stets bei Kündigung mitteilen |
| § 203 StGB / Datenschutz | Strafbarkeit | Sozialdaten nur intern und an BR; kein Dritter |

**Beweislast:** Der Arbeitgeber trägt im Kündigungsschutzprozess die volle Darlegungs- und Beweislast für die ordnungsgemäße Durchführung der Betriebsratsanhörung (Richardi, in: Richardi, BetrVG, 17. Aufl. 2022, § 102 Rn. 117).

## Quellenpflicht

Jede juristische Aussage in jedem auf diesem Skill basierenden Dokument ist nach **references/zitierweise.md** zu belegen:

- Rechtsprechungsbelege im BGH-Stil (Gericht, Entscheidungsform, Datum, AZ, Fundstelle, Rn.).
- Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen zitieren. Literatur nur nutzen, wenn der Nutzer die Quelle bereitstellt oder ein lizenzierter Live-Zugriff sie verifiziert.
- Bei umstrittenen Fragen (z. B. Umfang der Mitteilungspflicht, Fehlerfolgen) h. M. und Gegenauffassung getrennt zitieren.
- Halluzinationsrisiko: Alle Aktenzeichen und Fundstellen vor Einreichung verifizieren.
- Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen zitieren. Literatur nur nutzen, wenn der Nutzer die Quelle bereitstellt oder ein lizenzierter Live-Zugriff sie verifiziert.
