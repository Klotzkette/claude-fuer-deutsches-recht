---
name: avv-cloud-und-subverarbeitung-art-28-iv
description: "Auftragsverarbeitung bei Cloud-Diensten und Sub-Verarbeitung nach Art. 28 Abs. 2 und Abs. 4 DSGVO. Behandelt die Sub-AV-Kette das Genehmigungsverfahren die Informationspflicht beim Wechsel sowie die Haftungsdurchleitung. Output: Sub-AV-Klauselbaukasten und Pruefraster für Sub-AV-Listen."
---

# Cloud und Sub-Auftragsverarbeitung Art. 28 Abs. 2 und Abs. 4 DSGVO

## Zweck / Purpose

Behandlung von Sub-Auftragsverarbeitern in Cloud-Konstellationen mit typischerweise mehrstufiger Kette: Anbieter (Tier 1), Hyperscaler (Tier 2), Drittland-Support (Tier 3). Purpose (EN): Sub-processing under Article 28 (2) and (4) GDPR in cloud and SaaS deployment chains.

## Wann dieses Modul hilft

- SaaS-/Cloud-Anbieter wird beauftragt und nutzt selbst Hyperscaler-Infrastruktur (AWS, Azure, Google Cloud).
- Es ist die Liste der Sub-AV zu pruefen oder zu erstellen.
- Eine Aufsichtsbehoerde fragt nach der Sub-AV-Kette und der Haftungsdurchleitung.
- Ein Sub-AV im Drittland soll hinzugefuegt werden.

## Rechtlicher Rahmen

- Art. 28 Abs. 2 Satz 1 DSGVO: Auftragsverarbeiter nimmt keinen weiteren Auftragsverarbeiter ohne vorherige gesonderte oder allgemeine schriftliche Genehmigung des Verantwortlichen in Anspruch.
- Art. 28 Abs. 2 Satz 2 DSGVO: Bei allgemeiner Genehmigung Information ueber jede beabsichtigte Aenderung; Verantwortlicher hat Recht zum Einspruch.
- Art. 28 Abs. 4 DSGVO: Sub-Auftragsverarbeiter unterliegt durch Vertrag oder anderes Rechtsinstrument den gleichen Datenschutzpflichten wie der Auftragsverarbeiter. Wenn er diese nicht erfuellt, haftet der primaere Auftragsverarbeiter weiter gegenueber dem Verantwortlichen.
- Beschluss (EU) 2021/914 Klausel 9: Sub-AV-Mechanik im SCC-Kontext.

## Ablauf / Checkliste

1. **Sub-AV-Kette dokumentieren.**
 - Tier 1: Vertragspartner.
 - Tier 2: Direkter Sub-AV des Tier 1 (z. B. Hyperscaler).
 - Tier 3+: Weitere Sub-AV (z. B. Support-Dienstleister, Backup-Provider).
 - Pro Sub-AV: Name, Sitz, Verarbeitungsumfang, Datenort, Drittlandbezug, Schutzmechanismus.

2. **Genehmigungsmodell festlegen.**

 | Modell | Vorteil | Nachteil |
 |---|---|---|
 | Spezifische Genehmigung | Volle Kontrolle | Praktisch unhandhabbar bei vielen Sub-AV |
 | Allgemeine Genehmigung mit Liste | Praktikabel | Voraussetzung: aktuelle Liste, ausreichende Frist, Einspruchsrecht |
 | Allgemeine Genehmigung ohne Liste | Bequem | Nicht Art. 28 DSGVO-konform |

3. **Informationspflicht und Einspruchsrecht.**
 - Frist Praxis: 30 Tage vor Wirksamwerden, mindestens aber so, dass Einspruch faktisch moeglich ist.
 - Einspruchsgrund: berechtigte Bedenken (Drittland, fehlende TOM, Wettbewerber, Aufsichtsbehoerde).
 - Folge: Auftragsverarbeiter sucht alternative Sub-AV, sonst ausserordentliche Kuendigung durch Verantwortlichen.

4. **Haftungsdurchleitung.**
 - Vertraglich oder per Rechtsinstrument identische Pflichten beim Sub-AV.
 - Praxis: Back-to-Back-Vertrag oder Inkorporation des AVV als Anlage.
 - Beweisbarkeit: Auftragsverarbeiter muss die Sub-AV-Vertraege auf Verlangen vorlegen.

5. **Drittlandbezug.**
 - Sub-AV im Drittland: zusaetzlich SCC Beschluss (EU) 2021/914 (Module C2P oder P2P, je nach Konstellation).
 - DPF nur für US-Sub-AV mit aktiver Selbstzertifizierung.
 - TIA nach EDSA-Empfehlungen 01/2020.

## Mustertext / Template

Sub-AV-Klausel mit allgemeiner Genehmigung und Listenmechanik:

> "(1) Der Verantwortliche erteilt dem Auftragsverarbeiter die allgemeine Genehmigung im Sinne des Art. 28 Abs. 2 DSGVO, weitere Auftragsverarbeiter ('Sub-Auftragsverarbeiter') gemaess der als Anlage 3 beigefuegten Liste mit der Verarbeitung personenbezogener Daten zu beauftragen.
>
> (2) Der Auftragsverarbeiter informiert den Verantwortlichen mindestens dreissig (30) Kalendertage vor Wirksamwerden ueber jede beabsichtigte Aenderung in Bezug auf die Hinzuziehung oder die Ersetzung von Sub-Auftragsverarbeitern.
>
> (3) Der Verantwortliche kann der Aenderung innerhalb von dreissig (30) Kalendertagen nach Zugang der Information aus berechtigten Gruenden schriftlich widersprechen. Berechtigte Gruende liegen insbesondere vor bei Drittlandverarbeitung ohne ausreichende Schutzmassnahmen, bei unzureichenden technischen und organisatorischen Massnahmen oder bei einem Sub-Auftragsverarbeiter, der ein direkter Wettbewerber des Verantwortlichen ist.
>
> (4) Im Fall eines berechtigten Widerspruchs, den der Auftragsverarbeiter nicht durch zumutbare technische oder organisatorische Massnahmen ausraeumen kann, ist der Verantwortliche zur ausserordentlichen Kuendigung des Hauptvertrags und dieses Auftragsverarbeitungsvertrags berechtigt.
>
> (5) Der Auftragsverarbeiter schliesst mit jedem Sub-Auftragsverarbeiter einen Vertrag im Sinne des Art. 28 Abs. 4 DSGVO, der dem Sub-Auftragsverarbeiter im Wesentlichen die gleichen Datenschutzpflichten auferlegt wie sie in diesem Vertrag für den Auftragsverarbeiter festgelegt sind. Der Auftragsverarbeiter haftet gegenueber dem Verantwortlichen für die Erfuellung der Pflichten durch den Sub-Auftragsverarbeiter unveraendert weiter.
>
> (6) Auf Anforderung des Verantwortlichen legt der Auftragsverarbeiter den Sub-Auftragsverarbeiter-Vertrag in einer Form vor, die berechtigte Geschäftsgeheimnisse des Sub-Auftragsverarbeiters wahrt (z. B. mit Schwaerzungen)."

## Typische Drafting-Fehler

- Allgemeine Genehmigung "für alle gegenwaertigen und zukuenftigen Sub-AV ohne Information" – nicht Art. 28 Abs. 2 DSGVO-konform.
- Liste der Sub-AV nicht aktuell, kein Aenderungsverfahren definiert.
- Frist zu kurz (z. B. 7 Tage) – Einspruchsrecht faktisch ausgehoehlt.
- Back-to-Back-Vertrag nicht abgeschlossen oder nicht nachweisbar.
- Drittland-Sub-AV ohne SCC oder ohne TIA.
- Kein Recht zur ausserordentlichen Kuendigung bei berechtigtem Widerspruch.

## Querverweise

- `datenschutzrecht/skills/avv-art-28-mindestinhalte-checkliste/SKILL.md`
- `datenschutzrecht/skills/avv-haftung-risikoallokation-art-82-dsgvo/SKILL.md`
- `datenschutzrecht/skills/avv-eu-us-data-privacy-framework-bezug/SKILL.md`
- `datenschutzrecht/skills/drittlandstransfer-pruefung/SKILL.md`

## Quellen Stand 06/2026

- Art. 28 Abs. 2 und Abs. 4 DSGVO.
- Beschluss (EU) 2021/914 Klausel 9 – Sub-AV-Mechanik.
- EDSA-Leitlinien 07/2020 zur Abgrenzung Verantwortlicher / Auftragsverarbeiter (Final 07.07.2021).
- EDSA-Empfehlungen 01/2020 zur Transferfolgenabschaetzung (Version 2.0 Juni 2021).
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
