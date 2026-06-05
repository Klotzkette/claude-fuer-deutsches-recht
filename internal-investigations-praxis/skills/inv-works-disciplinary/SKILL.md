---
name: inv-works-disciplinary
description: "Inv 042 Works Council Conflict, Inv 043 Disciplinary Measure: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nächsten belastbaren Output."
---

# Inv 042 Works Council Conflict, Inv 043 Disciplinary Measure

## Arbeitsbereich

Dieser Skill bündelt **Inv 042 Works Council Conflict, Inv 043 Disciplinary Measure** zu einem konkreten Arbeitsgang. Starte mit dem Modul, das die Tatsachen der Akte trägt; weitere Module nur hinzunehmen, wenn sie dieselbe Frist, Zuständigkeit, Beweislast oder denselben Output betreffen.

## Arbeitsmodule

| Arbeitsmodul | Fokus |
| --- | --- |
| `inv-042-works-council-conflict` | Löst Konflikte mit dem Betriebsrat während einer Internal Investigation – Mitbestimmungsstreit, Einigungsstelle, einstweiliger Rechtsschutz. |
| `inv-043-disciplinary-measure` | Wählt und setzt arbeitsrechtliche Disziplinarmaßnahmen um – Abmahnung, Versetzung, Kürzung von Boni, Freistellung, Zielvereinbarungsänderung. |

## Arbeitsweg

Für **Inv 042 Works Council Conflict, Inv 043 Disciplinary Measure** zuerst das Arbeitsmodul wählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Im Plugin `internal-investigations-praxis` bleiben Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschter Output getrennt; Module nur kombinieren, wenn dieselbe Akte mehrere dieser Punkte trägt. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Arbeitsmodule im Detail

## 1. `inv-042-works-council-conflict`

**Fokus:** Löst Konflikte mit dem Betriebsrat während einer Internal Investigation – Mitbestimmungsstreit, Einigungsstelle, einstweiliger Rechtsschutz.

# Betriebsrats-Konflikte in Internal Investigations

## Rechtlicher Rahmen

Betriebsräte können eine Internal Investigation erheblich blockieren oder verlangsamen, wenn sie Mitbestimmungsrechte geltend machen. Gleichzeitig ist der Betriebsrat ein wichtiger Partner, dessen Einbindung die Verwertbarkeit von Untersuchungsergebnissen sichert. Konflikte entstehen regelmäßig bei: (1) Streit über Mitbestimmungspflicht bei technischen Überwachungsmaßnahmen (§ 87 Abs. 1 Nr. 6 BetrVG, [gesetze-im-internet.de](https://www.gesetze-im-internet.de/betrvg/__87.html)), (2) Verweigerung der Zustimmung zu Versetzungen oder Kündigungen, (3) Zugang des Betriebsrats zu Untersuchungsergebnissen.

## Ziel dieses Skills

Dieser Skill löst konkrete Betriebsrats-Konflikte und sichert die Fortführung der Untersuchung ohne unnötige Verzögerungen.

## Arbeitsprogramm

### 1. Streit über Mitbestimmungspflicht bei IT-Überwachungsmaßnahmen
- § 87 Abs. 1 Nr. 6 BetrVG: Mitbestimmung bei technischen Einrichtungen, die Verhalten oder Leistung überwachen.
- Streitfrage: Ist die forensische Auswertung bestehender Daten (ohne neue Überwachungsanlage) mitbestimmungspflichtig?
- BAG-Rechtsprechung: einmalige, anlassbezogene Auswertung ist regelmäßig nicht mitbestimmungspflichtig; fortlaufende Überwachung schon.
- Wenn Betriebsrat Zustimmung verweigert: Einigungsstelle (§ 76 BetrVG, [gesetze-im-internet.de](https://www.gesetze-im-internet.de/betrvg/__76.html)) oder einstweiliger Rechtsschutz beim Arbeitsgericht.

### 2. Zugangsanspruch des Betriebsrats
- § 80 Abs. 2 BetrVG: Unterrichtungsrecht des Betriebsrats über Angelegenheiten, die die Arbeitnehmer betreffen.
- Grenzen: keine Offenlegung von Anwaltsgeheimnissen, keine Offenbarung von personenbezogenen Daten unbeteiligter Arbeitnehmer.
- Betriebsrat hat kein Recht auf vollständigen Untersuchungsbericht.
- Praxis: Information über den Sachverhalt in allgemeiner Form; keine Detailprotokolle.

### 3. Zustimmungsverweigerung bei Kündigung (§ 102 BetrVG)
- § 102 Abs. 3 BetrVG: Betriebsrat kann Widerspruch gegen Kündigung einlegen; begründeter Widerspruch ermöglicht Weiterbeschäftigung bis zum ArbG-Urteil.
- Strategische Reaktion: Antizipieren der Widerspruchsgründe und in der Anhörungsmitteilung entkräften.
- Klage auf Zustimmungsersetzung: nicht möglich; aber Kündigungsschutzklage des Arbeitnehmers ist der eigentliche Prüfstein.

### 4. Einigungsstelle
- § 76 BetrVG: Einigungsstelle als Schlichter bei Meinungsverschiedenheiten zwischen Arbeitgeber und Betriebsrat.
- Einsetzung: auf Antrag durch Arbeitsgericht (§ 76 Abs. 2 BetrVG).
- Einigungsstellenspruch ist für beide Parteien bindend (bei erzwingbarer Mitbestimmung).
- Zeitdauer: Einigungsstellenverfahren kann Monate dauern; Untersuchung sollte nicht blockiert werden.

### 5. Einstweiliger Rechtsschutz
- Arbeitgeber kann bei dringendem Bedarf Eilantrag beim Arbeitsgericht stellen.
- Voraussetzung: dringendes betriebliches Bedürfnis überwiegt Mitbestimmungsrecht (§ 100 Abs. 1 BetrVG für Versetzungen).
- § 87 BetrVG: einstweilige Verfügung auf vorläufige Zustimmungsersetzung in Ausnahmefällen.

### 6. Betriebsrat als Interessenkollision
- Wenn Betriebsratsmitglied selbst Beschuldigter ist: § 103 BetrVG (Zustimmung zur Kündigung, [gesetze-im-internet.de](https://www.gesetze-im-internet.de/betrvg/__103.html)).
- Betriebsrat muss sich von eigenen Mitgliedern, die Beschuldigte sind, distanzieren und darf sich nicht schützend vor sie stellen.
- Strafbarkeit: Betriebsratsmitglied, das Untersuchung aktiv behindert, kann sich nach § 274 StGB (Beweisunterdrückung) oder § 258 StGB (Strafvereitelung) strafbar machen.

### 7. Konstruktive Kooperationsstrategie
- Betriebsrat frühzeitig in allgemeiner Form informieren, bevor er von dritter Seite erfährt.
- Regelmäßige, kontrollierte Updates; kein Informationsvakuum.
- Betriebsvereinbarung über Untersuchungsprozesse als langfristige Lösung.
- Betriebsrat als Partner in der Remediation-Phase einbinden.

## Red-Team-Fragen

- Ist die Mitbestimmungspflicht für alle Untersuchungsmaßnahmen korrekt eingeschätzt worden?
- Hat der Betriebsrat tatsächlich Zugang zu Unterlagen erhalten, der über sein gesetzliches Recht nach § 80 BetrVG hinausgeht?
- Wurde die Betriebsratsanhörung nach § 102 BetrVG für alle geplanten Kündigungen korrekt durchgeführt?
- Blockiert der Betriebsrat die Untersuchung aus legitimen Gründen oder aus verfahrensfremden Motiven?
- Gibt es ein Betriebsratsmitglied unter den Beschuldigten, und sind die Verfahrensrechte nach § 103 BetrVG beachtet?
- Wurde eine konstruktive Einbindungsstrategie entwickelt, die den Betriebsrat zum Partner macht?

## Normenregister

| Norm | Inhalt | Quelle |
|---|---|---|
| § 87 BetrVG | Mitbestimmung Überwachung | [gesetze-im-internet.de](https://www.gesetze-im-internet.de/betrvg/__87.html) |
| § 80 BetrVG | Überwachungsrecht | [gesetze-im-internet.de](https://www.gesetze-im-internet.de/betrvg/__80.html) |
| § 102 BetrVG | Anhörung vor Kündigung | [gesetze-im-internet.de](https://www.gesetze-im-internet.de/betrvg/__102.html) |
| § 103 BetrVG | Kündigung Betriebsratsmitglied | [gesetze-im-internet.de](https://www.gesetze-im-internet.de/betrvg/__103.html) |
| § 76 BetrVG | Einigungsstelle | [gesetze-im-internet.de](https://www.gesetze-im-internet.de/betrvg/__76.html) |

## Ausgabeformate

- **Mitbestimmungs-Prüfmatrix** (Maßnahme × § 87 BetrVG × Streitfrage)
- **Informationsschreiben** an Betriebsrat (kontrollierte Zusammenfassung)
- **Betriebsratsanhörung** nach § 102 BetrVG
- **Einigungsstellen-Antrag** (Musterstruktur)
- **Kooperationsstrategie-Memo** für konstruktive Einbindung

Rechtsprechungszitate nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle.

## 2. `inv-043-disciplinary-measure`

**Fokus:** Wählt und setzt arbeitsrechtliche Disziplinarmaßnahmen um – Abmahnung, Versetzung, Kürzung von Boni, Freistellung, Zielvereinbarungsänderung.

# Disziplinarmaßnahmen nach Internal Investigations

## Rechtlicher Rahmen

Nach Abschluss einer Internal Investigation müssen geeignete Disziplinarmaßnahmen ergriffen werden. Dies ergibt sich aus der Pflicht des Vorstands, auf festgestellte Verstöße zu reagieren (§ 93 AktG, BGH II ZR 234/09, [openjur.de](https://openjur.de/o/577696.html)) und aus § 130 OWiG (fehlende Reaktion ist selbst ein Aufsichtspflichtverstoß, [gesetze-im-internet.de](https://www.gesetze-im-internet.de/owig/__130.html)). Gleichzeitig müssen Disziplinarmaßnahmen verhältnismäßig sein und das Betriebsverfassungsrecht beachten.

## Ziel dieses Skills

Dieser Skill wählt die proportionale Disziplinarmaßnahme auf Grundlage der Untersuchungsergebnisse aus und stellt die rechtssichere Umsetzung sicher.

## Arbeitsprogramm

### 1. Disziplinarmaßnahmen-Spektrum
| Schwere | Maßnahme | Rechtsgrundlage |
|---|---|---|
| Leicht | Ermahnung (ohne Abmahnung) | Arbeitsvertrag, § 242 BGB |
| Mittel | Abmahnung | § 314 BGB analog |
| Mittel-schwer | Versetzung, Funktionsentzug | § 106 GewO, Direktionsrecht |
| Schwer | Ordentliche Kündigung | § 1 KSchG |
| Sehr schwer | Außerordentliche Kündigung | § 626 BGB |
| Parallel | Strafanzeige | StGB |
| Finanziell | Bonusentzug, Gehaltskürzung | Arbeitsvertrag, § 315 BGB |

### 2. Verhältnismäßigkeitsprüfung
- Schwere des Verstoßes: war es vorsätzlich oder fahrlässig?
- Schadensausmaß: wirtschaftlicher Schaden für das Unternehmen.
- Verschulden: war der Mitarbeiter allein verantwortlich, oder hat das System versagt?
- Vorleben: gab es frühere Verstöße?
- Mitwirkung: hat der Mitarbeiter an der Untersuchung kooperiert?

### 3. Abmahnung
- Konkrete Beschreibung der Verfehlung (nicht pauschal) mit Datum, Handlung, Norm.
- Hinweis auf mögliche Kündigung bei Wiederholung.
- Keine Abmahnung erforderlich bei sehr schweren Verstößen (Betrug, Bestechung).
- Wirkungsdauer: ca. 2 Jahre; nach Ablauf oft keine Grundlage mehr für verhaltensbedingte Kündigung.

### 4. Versetzung und Funktionsentzug
- § 106 GewO (Direktionsrecht): Arbeitgeber kann Aufgabenbereich ändern, soweit nicht ausdrücklich vertraglich ausgeschlossen.
- Versetzung bei Interessenkonflikt: z. B. Entfernung aus Beschaffungsfunktion.
- Funktionsentzug bei Verdacht: Entzug von Zugriffsrechten, Zeichnungsberechtigungen.
- Betriebsrat: § 99 BetrVG – Zustimmung bei wesentlicher Versetzung (vgl. inv-006-betriebsrat).

### 5. Bonus- und Gehaltskürzungen
- Leistungsabhängige Boni: können bei Compliance-Verstößen verweigert oder zurückgefordert werden, wenn Vertrag entsprechende Klausel enthält (Claw-Back).
- Claw-Back-Klauseln: in Vergütungsstrukturen von Banken (§ 5 Abs. 6 InstVV) und börsennootierten Unternehmen.
- § 315 BGB: Billigkeitsbestimmung bei einseitigem Bestimmungsrecht des Arbeitgebers.
- Keine Gehaltskürzungen ohne arbeitsvertragliche Grundlage.

### 6. Maßnahmen gegen Organmitglieder
- Vorstandsmitglied: Abberufung (§ 84 AktG bei wichtigem Grund, [gesetze-im-internet.de](https://www.gesetze-im-internet.de/aktg/__84.html)); Schadensersatz (§ 93 Abs. 2 AktG).
- Aufsichtsratsmitglied: Abberufung durch Hauptversammlung (§ 103 AktG); Haftung nach § 116 AktG.
- D&O-Versicherung: Deckungsschutz prüfen; oft kein Schutz bei vorsätzlichem Handeln.
- Gehalts- und Tantième-Rückforderung: § 93 Abs. 3 AktG; Insolvenzanfälligkeit prüfen.

### 7. Dokumentation
- Alle Disziplinarmaßnahmen schriftlich und im Personalakt dokumentieren.
- Betriebsratsanhörung gemäß § 102 BetrVG für alle Kündigungen.
- Fristen einhalten: § 626 Abs. 2 BGB (2-Wochen-Frist für außerordentliche Kündigung ab Kenntniserlangung).
- Nachverfolgung: wurden Maßnahmen tatsächlich vollständig umgesetzt?

## Red-Team-Fragen

- Ist die gewählte Disziplinarmaßnahme verhältnismäßig zur festgestellten Verfehlung?
- Wurden alle Mitarbeiter mit ähnlichem Verhalten gleich behandelt (Gleichbehandlungsgrundsatz)?
- Ist die 2-Wochen-Frist für außerordentliche Kündigung eingehalten?
- Gibt es Claw-Back-Klauseln in den Vergütungsverträgen, die bei Compliance-Verstößen aktiviert werden können?
- Wurden alle Betriebsratsrechte gewahrt (§ 102 BetrVG-Anhörung)?
- Sind die Disziplinarmaßnahmen nach außen hin konsistent – keine unterschiedliche Behandlung nach Hierarchieebene ohne sachlichen Grund?

## Normenregister

| Norm | Inhalt | Quelle |
|---|---|---|
| § 626 BGB | Außerordentliche Kündigung | [gesetze-im-internet.de](https://www.gesetze-im-internet.de/bgb/__626.html) |
| § 106 GewO | Direktionsrecht | [gesetze-im-internet.de](https://www.gesetze-im-internet.de/gewo/__106.html) |
| § 84 AktG | Abberufung Vorstand | [gesetze-im-internet.de](https://www.gesetze-im-internet.de/aktg/__84.html) |
| § 93 AktG | Haftung Vorstand | [gesetze-im-internet.de](https://www.gesetze-im-internet.de/aktg/__93.html) |
| § 102 BetrVG | Anhörung vor Kündigung | [gesetze-im-internet.de](https://www.gesetze-im-internet.de/betrvg/__102.html) |

## Ausgabeformate

- **Disziplinarmaßnahmen-Entscheidungsmatrix** (Schwere × Maßnahme × Rechtsgrundlage)
- **Abmahnungsvorlage**
- **Betriebsratsanhörung** nach § 102 BetrVG
- **Claw-Back-Berechnungs-Vorlage**
- **Organhaftungs-Schadensersatz-Memo**

Rechtsprechungszitate nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle.
