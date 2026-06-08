---
name: avv-konzern-und-multi-party-konstellation
description: "AVV im Konzern und in Multi-Party-Konstellationen. Behandelt Konzern-AVV mit zentraler Group-IT Shared-Service-Center und konzernweiter Liste der Auftragsverarbeiter. Klaert die Frage ob Konzern als Einheit auftritt oder jede Gesellschaft eigenstaendig. Output: Konzern-AVV-Klauselgeruest mit Beitrittsmechanik."
---

# AVV im Konzern und in Multi-Party-Konstellationen

## Zweck / Purpose

Strukturierung von Auftragsverarbeitungsvertraegen in Konzernverbuenden und Multi-Party-Konstellationen, in denen mehrere Konzerngesellschaften gemeinsam Auftraggeber oder gemeinsam Auftragnehmer sind. Purpose (EN): How to structure DPAs in corporate group setups and multi-party constellations.

## Wann dieses Modul hilft

- Konzernmutter und mehrere Toechter beziehen denselben Cloud-Dienst und sollen unter einem Vertragsschirm liegen.
- Konzernweite Shared-Service-Center (HR, IT, Payroll) verarbeiten Daten anderer Konzerngesellschaften.
- Ein Konsortium oder Joint Venture nimmt gemeinsam Dienstleistungen in Anspruch.
- Es ist abzuklaeren, ob nicht stattdessen Konzern-BCR (Art. 47 DSGVO) oder eine Joint-Controller-Vereinbarung (Art. 26 DSGVO) erforderlich ist.

## Rechtlicher Rahmen

- Art. 28 DSGVO – auch im Konzern keine Privilegierung; jede juristische Person ist eigenstaendige Verantwortliche.
- Erwaegungsgrund 48 DSGVO – Berechtigtes Interesse an konzerninternem Datenaustausch für interne Verwaltungszwecke.
- Erwaegungsgrund 36 DSGVO – Niederlassung und Verantwortlichkeit im Konzern.
- Art. 26 DSGVO – Joint Controller, falls gemeinsame Zweckentscheidung.
- Art. 47 DSGVO – Verbindliche interne Datenschutzvorschriften (BCR).
- § 26 BDSG – Beschaeftigtendatenschutz bei konzerninternem HR-Transfer.

## Ablauf / Checkliste

1. **Konzernstruktur erfassen.**
 - Mutter, Toechter, Schwestern, Gemeinschaftsunternehmen.
 - Wer ist Vertragspartner des Dienstleisters?
 - Wer ist tatsaechlicher Verantwortlicher für die Daten?

2. **Vertragsstrukturen vergleichen.**

 | Struktur | Beschreibung | Anwendungsfall |
 |---|---|---|
 | Hauptvertrag der Mutter mit Beitrittsmechanik | Mutter unterzeichnet, Toechter treten bei | Konzernlizenz Cloud-Dienst |
 | Rahmen-AVV mit Einzelbestellungen | Jede Gesellschaft schliesst eigenen AVV unter Rahmen ab | Multi-Country-Rollout |
 | Multilateraler AVV | Alle Konzerngesellschaften unterzeichnen gemeinsam | Wenige Gesellschaften, hohe Datenkritikalitaet |
 | Konzern-AVV (intra-group) | Mutter ist Auftragsverarbeiter für Toechter (Shared Service) | Group-IT, Group-HR, Group-Finance |

3. **Rollenmix klaeren.**
 - Mutter als Auftragsverarbeiterin der Toechter setzt voraus, dass die Mutter weisungsgebunden ist.
 - Wenn die Mutter eigenstaendige Konzernzwecke verfolgt (Konzernsteuerung, Reporting), liegt regelmaessig Art. 26 DSGVO oder eigene Verantwortlichkeit vor.
 - EuGH C-498/16 (Wirtschaftsakademie / Fanpages) – verifiziert: weite Auslegung gemeinsamer Verantwortlichkeit.

4. **Drittlandbezug pruefen.**
 - Konzern weltweit – BCR nach Art. 47 DSGVO oder SCC nach Beschluss (EU) 2021/914 für jede Konzerngesellschaft im Drittland.
 - DPF nur für US-Konzerngesellschaften mit aktiver Selbstzertifizierung.

5. **Beitrittsmechanik (Docking Clause).**
 - Vergleichbar dem Mechanismus in den EU-SCC nach Beschluss (EU) 2021/914.
 - Beitritt durch Unterzeichnung einer Beitrittsanlage.
 - Wirkung: Beitretende Gesellschaft wird Vertragspartei mit allen Rechten und Pflichten.

## Mustertext / Template

Konzern-AVV-Klauseln (Auszug):

> "Praeambel
>
> Diese Vereinbarung wird zwischen dem Auftragsverarbeiter und [Muttergesellschaft] als koordinierender Konzerngesellschaft geschlossen. Weitere Konzerngesellschaften im Sinne des § 15 AktG koennen dieser Vereinbarung durch Unterzeichnung der Beitrittsanlage (Anlage 5) beitreten. Mit Wirkung der Beitrittsanlage ist die beitretende Konzerngesellschaft Verantwortliche im Sinne dieser Vereinbarung; ihre Rechte und Pflichten richten sich nach den Bestimmungen dieser Vereinbarung.
>
> § 1 Verarbeitungstaetigkeiten
>
> Die Verarbeitung erfolgt für jede Konzerngesellschaft im Umfang der jeweils mit dieser geschlossenen Bestellung. Anlage 1 (Beschreibung der Verarbeitung) wird je Konzerngesellschaft befuellt.
>
> § 2 Weisungsrechte und Weisungsregister
>
> Jede Konzerngesellschaft erteilt Weisungen ausschliesslich für die sie betreffenden Verarbeitungen. Konzernweit gueltige Weisungen werden vom Konzern-Datenschutzbeauftragten dokumentiert. Der Auftragsverarbeiter fuehrt für jede Konzerngesellschaft ein eigenes Weisungsregister.
>
> § 3 Konzerngesamtleitung und Kommunikation
>
> Die Muttergesellschaft uebt für die beigetretenen Konzerngesellschaften die Funktion der zentralen Anlaufstelle aus, soweit dies mit der jeweiligen Konzerngesellschaft schriftlich vereinbart ist. Die Pflichten und Rechte aus Art. 28 DSGVO bestehen unabhaengig davon im Verhaeltnis Auftragsverarbeiter zu jeweiliger Konzerngesellschaft fort.
>
> § 4 Beitritt und Austritt von Konzerngesellschaften
>
> (1) Beitritt: Die Beitrittsanlage ist von der beitretenden Konzerngesellschaft und dem Auftragsverarbeiter zu unterzeichnen.
> (2) Austritt: Eine Konzerngesellschaft kann ihre Teilnahme mit einer Frist von drei Monaten zum Quartalsende beenden; die Pflichten aus § 9 (Loeschung/Rueckgabe) gelten entsprechend."

## Typische Drafting-Fehler

- Annahme einer "Konzernprivilegierung" – existiert in der DSGVO nicht.
- Eine einzige Vertragspartei "im Namen aller Konzerngesellschaften" ohne Vollmacht oder Beitrittsmechanik.
- Konzern-Shared-Service als pauschal "Auftragsverarbeitung" eingestuft, obwohl die Mutter eigene Konzernzwecke verfolgt – tatsaechlich Art. 26 oder eigene Verantwortlichkeit.
- Drittlandbezug einer Konzerngesellschaft uebersehen.
- Beitrittsanlage ohne Pflicht zur Information des Dienstleisters – Versionierungschaos.

## Querverweise

- `datenschutzrecht/skills/avv-rolemix-getrennt-vs-gemeinsam-verantwortlich/SKILL.md`
- `datenschutzrecht/skills/avv-art-26-joint-controllership-deutsch/SKILL.md`
- `datenschutzrecht/skills/avv-cloud-und-subverarbeitung-art-28-iv/SKILL.md`
- `datenschutzrecht/skills/drittlandstransfer-pruefung/SKILL.md`

## Quellen Stand 06/2026

- DSGVO Art. 28, Art. 26, Art. 47 sowie ErwGr. 36 und 48.
- BDSG § 26.
- EuGH C-498/16 (Wirtschaftsakademie) – verifiziert; Volltext ueber curia.europa.eu.
- EDSA-Leitlinien 07/2020 zur Abgrenzung Verantwortlicher / Auftragsverarbeiter (Final 07.07.2021).
- EU-Kommission Beschluss (EU) 2021/914 mit Docking Clause (Klausel 7).
- Zitierweise: `../../../references/zitierweise.md`.

## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.

## Normen und Rechtsprechung

### Kuratierte Normen-Bibliothek

- Art. 5 DSGVO (Grundsätze der Verarbeitung)
- Art. 6, 9 DSGVO (Rechtsgrundlagen, besondere Datenkategorien)
- Art. 13, 14 DSGVO (Informationspflichten)
- Art. 15 DSGVO (Auskunftsrecht)
- Art. 28 DSGVO (Auftragsverarbeitung)
- Art. 32 DSGVO (Sicherheit der Verarbeitung)
- Art. 33, 34 DSGVO (Meldepflichten bei Verletzung)
- Art. 82 DSGVO (Schadensersatz)
- Art. 83 DSGVO (Bußgelder)
- §§ 4, 20, 41 BDSG (Aufsicht, Rechtsweg, Strafvorschriften)

### Leitentscheidungen

- EuGH C-300/21 (immaterieller Schaden Art. 82 DSGVO)
- EuGH C-634/21 (automatisierte Bonitätsbewertung Schufa)
- EuGH C-26/22 (Datenschutzbehörden-Befugnisse)
- EuGH C-807/21 (Bußgeldhaftung juristischer Personen)
- BVerfG 1 BvR 16/13 (Recht auf Vergessen I)

### Anwendung im Skill

- Rechtsgrundlage nach Art. 6 DSGVO sauber waehlen; berechtigte Interessen nach Art. 6 Abs. 1 lit. f DSGVO mit dokumentierter Abwaegung.
- Bei Datenpannen die 72-Stunden-Frist nach Art. 33 DSGVO einhalten; Risikoabwaegung Art. 34 DSGVO separat dokumentieren.
- Auskunftsanspruch Art. 15 DSGVO nicht mit Kopie nach Art. 15 Abs. 3 DSGVO verwechseln; EuGH C-307/22 Reichweite beachten.
