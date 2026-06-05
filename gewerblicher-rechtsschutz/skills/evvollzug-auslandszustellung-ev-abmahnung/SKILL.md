---
name: evvollzug-auslandszustellung-ev-abmahnung
description: "Evvollzug Auslandszustellung EV Abmahnung: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Evvollzug Auslandszustellung EV Abmahnung

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Evvollzug Auslandszustellung EV Abmahnung** im Plugin Gewerblicher Rechtsschutz. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `evvollzug-neu-006-auslandszustellung-ev-und-uebersetzung` | EV-Vollzug: Auslandszustellung einstweiliger Verfügungen im IP-Recht nach EuZustVO, HZÜ und HCCH 2019. Übersetzungspflicht, Zustellwege EU/Nicht-EU, Vollziehungsfrist und praktische Fallstricke bei grenzüberschreitenden IP-Verfügungen. |
| `evvollzug-neu-007-abmahnung-abschlussschreiben-und-hauptsache` | EV-Vollzug: Abschlussschreiben nach einstweiliger Verfügung, Übergang in die Hauptsache und Verhältnis zur vorangegangenen Abmahnung. Wann Hauptsacheklage nötig, wann Abschlussvereinbarung ausreicht, Fristen und Kostenfallen. |
| `evvollzug-neu-008-schutzschrift-register-und-forumstrategie` | EV-Vollzug (Gegenseite): Schutzschrift im Schutzschriftenregister, Forumsstrategie des Antragsgegners und vorauseilende Rechtsverteidigung gegen einstweilige Verfügungen im gewerblichen Rechtsschutz. |

## Arbeitsweg

Im Plugin Gewerblicher Rechtsschutz gilt für **Evvollzug Auslandszustellung EV Abmahnung**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `evvollzug-neu-006-auslandszustellung-ev-und-uebersetzung`

**Fokus:** EV-Vollzug: Auslandszustellung einstweiliger Verfügungen im IP-Recht nach EuZustVO, HZÜ und HCCH 2019. Übersetzungspflicht, Zustellwege EU/Nicht-EU, Vollziehungsfrist und praktische Fallstricke bei grenzüberschreitenden IP-Verfügungen.

# EV-Vollzug 006: Auslandszustellung der EV und Übersetzungspflicht

## Zweck und Mandatsbezug

Dieser Skill behandelt die **grenzüberschreitende Zustellung einstweiliger Verfügungen** – ein häufiges Problem im gewerblichen Rechtsschutz, wenn Marken-, Patent- oder UWG-Verletzer im Ausland sitzen. Die Auslandszustellung ist komplex, zeitintensiv und kann die Vollziehungsfrist nach § 929 Abs. 2 ZPO gefährden.

Mandatsbezug: Deutsches Gericht erlässt EV gegen englischen Online-Händler oder US-amerikanischen App-Anbieter. Die Monatsfrist läuft; parallele Zustellwege müssen koordiniert werden.

## Rechtlicher Rahmen

### Zentrale Normen und Verordnungen

- **§ 929 Abs. 2 ZPO** – Vollziehungsfrist ein Monat; bei Auslandszustellung Fristverlängerungsantrag möglich (§ 929 Abs. 2 Satz 2 ZPO).
- **EuZustVO 2020 (VO (EU) 2020/1784)** – Zustellung gerichtlicher und außergerichtlicher Schriftstücke in EU-Mitgliedstaaten; gilt ab 1. Juli 2022.
- **HZÜ 1965** – Haager Übereinkommen über die Zustellung gerichtlicher und außergerichtlicher Schriftstücke in Zivil- und Handelssachen; gilt für zahlreiche Nicht-EU-Staaten (u.a. USA, UK post-Brexit, Japan, Schweiz).
- **§§ 183, 184 ZPO** – Auslandszustellung in Nicht-Vertragsstaaten; Botschaftszustellung.
- **Art. 8 EuZustVO 2020** – Übersetzungspflicht: Empfänger kann Annahmeverweigerung erklären, wenn Schriftstück nicht in Amtssprache des Empfangsstaats vorliegt.

### Zustellwege im Überblick

| Zielstaat | Rechtsgrundlage | Zustellweg | Zeitaufwand |
|---|---|---|---|
| EU-Mitgliedstaat | EuZustVO 2020 | Empfangsstelle; elektronische Übermittlung | 1–4 Wochen |
| UK (post-Brexit) | HZÜ 1965 | Central Authority; Solicitor | 4–8 Wochen |
| USA | HZÜ 1965 | Central Authority (US DoJ) | 4–12 Wochen |
| Schweiz | HZÜ 1965 | Kantonales Gericht | 4–8 Wochen |
| China | HZÜ 1965 | Ministry of Justice | 6–12 Monate |
| Nicht-Vertragsstaat | § 183 ZPO | Botschaftszustellung | sehr lang |

## Kaltstart in 5 Fragen

1. **Sitzstaat des Schuldners:** In welchem Land sitzt der Schuldner? EU, HZÜ-Vertragsstaat oder sonstiger Staat?
2. **Vollziehungsfrist:** Wie viel Zeit bleibt bis zum Ablauf der Monatsfrist (§ 929 Abs. 2 ZPO)?
3. **Anwalt im Ausland:** Hat Schuldner einen inländischen Prozessvertreter? Dann Inlandszustellung möglich.
4. **Übersetzung:** Liegt eine Übersetzung des EV-Beschlusses in die Sprache des Empfangsstaats vor?
5. **Parallele Zustellung:** Wird Fristverlängerungsantrag beim deutschen Gericht gestellt?

## Prüfprogramm

### Schritt 1 – Zustellungsform nach Zielstaat bestimmen

**EU-Mitgliedstaat (EuZustVO 2020):**
- Empfangsstelle des Mitgliedstaats identifizieren (Liste auf EJN-Website).
- Formblatt L (Standardformular EuZustVO) ausfüllen.
- Elektronische Übermittlung über Dezentrales IT-System ab 2025 schrittweise.
- Übersetzung: Empfänger kann Annahme verweigern, wenn keine Übersetzung (Art. 8 EuZustVO); bei Verdacht immer übersetzen.

**HZÜ-Vertragsstaat (USA, UK, Schweiz etc.):**
- Central Authority des Empfangsstaats identifizieren.
- Haager Formblätter (Modèle CN, CN-A) verwenden.
- Übersetzungsanforderungen des Empfangsstaats beachten (USA: Englisch; Schweiz: Deutsch/Französisch/Italienisch je nach Kanton).
- Zeitplan: Realistische Bearbeitungszeit einkalkulieren (USA: 4–12 Wochen).

**Nicht-Vertragsstaat:**
- § 183 ZPO: Zustellung über diplomatischen Weg.
- Extrem langwierig; im Einzelfall: Schuldner hat deutschen Anwalt? Wenn ja, Inlandszustellung bevorzugen.

### Schritt 2 – Fristverlängerungsantrag

- § 929 Abs. 2 Satz 2 ZPO ermöglicht Verlängerung der Vollziehungsfrist auf Antrag.
- Antrag muss vor Fristablauf gestellt werden.
- Begründung: Auslandszustellung in Bearbeitung, konkrete Zustellungsschritte darlegen.
- Gericht hat Ermessen; praktisch werden bei substantiierten Anträgen Verlängerungen gewährt.

### Schritt 3 – Übersetzung organisieren

- Zertifizierter Übersetzer (in der Regel vereidigter Übersetzer) erforderlich.
- Inhalt: Gesamter Beschlusstext inkl. Tenor, Begründung und ggf. Kostenentscheidung.
- Bei Eilsache: Schnellübersetzung beauftragen; Kosten als Verfahrenskosten erstattungsfähig.
- Wichtig: Übersetzung muss aktuell sein; nachträgliche Beschlussänderungen einarbeiten.

### Schritt 4 – Inländischen Zustellungsempfänger prüfen

- Hat der Schuldner einen deutschen Prozessbevollmächtigten? Dann Inlandszustellung über diesen.
- Hat der Schuldner eine inländische Niederlassung? Zustellung an Niederlassung möglich (§ 178 Abs. 1 Nr. 2 ZPO).
- Hat der Schuldner einen Zustellungsbevollmächtigten in Deutschland benannt? Vorrang.
- Diese Prüfung spart Monate gegenüber dem Auslandszustellungsweg.

### Schritt 5 – Parallele Zustellungsstrategien

- GV-Zustellung an inländischen Vertreter + Auslandszustellung parallel.
- Erste wirksame Zustellung beendet das Verfahren.
- Dokumentation: Beide Wege aufzeichnen, um im Ordnungsmittelverfahren den Kenntniszeitpunkt des Schuldners zu belegen.

## Typische Fallen

- **Fristversäumnis durch Unterschätzung des Zeitaufwands:** Auslandszustellung dauert Monate; ohne Fristverlängerungsantrag verliert man die EV.
- **Keine Übersetzung:** Schuldner verweigert Annahme; Zustellung unwirksam.
- **Falsches Formblatt:** Haager Formblätter veraltet oder falsch ausgefüllt; Empfangsstelle sendet zurück.
- **Schuldner hat deutschen Anwalt übersehen:** Einfachere Inlandszustellung möglich gewesen.
- **Unvollständiger Antrag an Central Authority:** Fehlende Anlagen führen zur Rücksendung.

## Output-Module

- **Zustellwegmatrix:** Sitzstaat → Rechtsgrundlage → Zustellweg → Zeitplan.
- **Fristverlängerungsantrag-Vorlage:** Begründung, Darlegung Zustellungsschritte.
- **Übersetzungsauftrag-Checkliste:** Dokument, Sprache, Zertifizierung, Frist.
- **Parallelstrategie-Plan:** Inlandszustellung + Auslandszustellung tabellarisch.

## Quellenregel

- EuZustVO 2020: [eur-lex.europa.eu – VO (EU) 2020/1784](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX%3A32020R1784)
- HZÜ 1965: [hcch.net](https://www.hcch.net/en/instruments/conventions/full-text/?cid=17)
- [§ 183 ZPO – dejure.org](https://dejure.org/gesetze/ZPO/183.html)
- [§ 929 ZPO – dejure.org](https://dejure.org/gesetze/ZPO/929.html)
- Aktuelle Central-Authority-Listen über HCCH-Website prüfen; keine BeckRS-Blindzitate.

## Anschluss-Skills

- `evvollzug-neu-001` – Vollziehungsfrist Überblick
- `evvollzug-neu-003` – GV-Zustellung im Inland
- `spezial-reaktion-internationaler-bezug-und-schnittstellen` – Internationale Bezüge im GewRS

## 2. `evvollzug-neu-007-abmahnung-abschlussschreiben-und-hauptsache`

**Fokus:** EV-Vollzug: Abschlussschreiben nach einstweiliger Verfügung, Übergang in die Hauptsache und Verhältnis zur vorangegangenen Abmahnung. Wann Hauptsacheklage nötig, wann Abschlussvereinbarung ausreicht, Fristen und Kostenfallen.

# EV-Vollzug 007: Abschlussschreiben und Übergang in die Hauptsache

## Zweck und Mandatsbezug

Dieser Skill behandelt den Schritt nach der vollzogenen einstweiligen Verfügung: den **Übergang von der EV in die Hauptsache** – entweder durch Abschlussschreiben und Abschlussvereinbarung oder durch Hauptsacheklage. Ohne diesen Schritt bleibt die EV ein vorläufiges Sicherungsmittel; die endgültige Klärung des Unterlassungsanspruchs steht aus.

Mandatsbezug: Markeninhaber hat EV erwirkt und vollzogen; Schuldner hat weder Widerspruch eingelegt noch Hauptsache erzwungen. Jetzt muss Antragsteller entscheiden, ob er Abschlussschreiben sendet oder Hauptsacheklage erhebt. Umgekehrt: Schuldner sucht Wege, das Verfahren kostengünstig abzuschließen.

## Rechtlicher Rahmen

### Zentrale Normen

- **§ 926 ZPO** – Hauptsacheklage: Gericht kann auf Antrag des Schuldners anordnen, dass Antragsteller binnen Frist Hauptsacheklage erhebt; Nichterhebung führt zur Aufhebung der EV.
- **§ 927 ZPO** – Aufhebung der EV durch veränderte Umstände; Aufhebungsantrag des Schuldners.
- **§ 924 ZPO** – Widerspruch des Schuldners gegen Beschlussverfügung; erzwingt mündliche Verhandlung.
- **§ 945 ZPO** – Schadensersatz bei ungerechtfertigt vollzogener EV (relevant bei Abschlussverhandlung).
- Keine gesetzliche Pflicht zum Abschlussschreiben; es ist eine Praxisregel, die auf der Rechtsprechung zum „freiwilligen Klagloswerden" basiert.

### Konzept des Abschlussschreibens

Das Abschlussschreiben ist ein **außerprozessuales Instrument**: Der Antragsteller fordert den Schuldner auf, die EV als endgültige Regelung anzuerkennen (Abschlussvereinbarung) und damit auf Widerspruch und Hauptsacheklage zu verzichten. Es ist praktisch eingebürgert, aber nicht im Gesetz geregelt.

| Instrument | Rechtsnatur | Folge |
|---|---|---|
| Abschlussschreiben | Außerprozessualer Antrag | Schuldner nimmt an oder nicht |
| Abschlussvereinbarung | Vertrag | Hauptsache erledigt; EV als endgültig anerkannt |
| Hauptsacheklage | Prozesshandlung | Materiell-rechtliche Prüfung des Unterlassungsanspruchs |
| Widerspruch (§ 924 ZPO) | Prozesshandlung des Schuldners | Führt zu mündlicher Verhandlung |

## Kaltstart in 5 Fragen

1. **Status EV:** EV vollzogen? Widerspruchsfrist noch offen oder schon abgelaufen?
2. **Schuldnerverhalten:** Hat Schuldner auf die EV reagiert (Widerspruch, Anwaltschreiben, Schweigen)?
3. **Strategie:** Will Antragsteller Abschlussvereinbarung (Prozessbeendigung) oder Hauptsacheklage?
4. **Frist § 926 ZPO:** Hat Schuldner bereits Klageerhebungsantrag gestellt oder angedroht?
5. **Output:** Abschlussschreiben-Entwurf, Abschlussvereinbarungs-Muster, Kostenrechnung Hauptsache?

## Prüfprogramm

### Schritt 1 – Widerspruchslage klären

- Widerspruchsfrist nach Beschlussverfügung (§ 924 ZPO): keine gesetzliche Frist; Schuldner kann jederzeit Widerspruch einlegen.
- Praxisregel: Abschlussschreiben senden, wenn nach ca. 2–4 Wochen nach Vollzug kein Widerspruch eingelegt wurde.
- Bei Urteilsverfügung: kein Widerspruch möglich; Schuldner muss Berufung einlegen.

### Schritt 2 – Abschlussschreiben formulieren

Pflichtinhalt:
1. Bezug auf die vollzogene EV (Gericht, AZ, Datum, Zustelldatum).
2. Feststellung, dass keine Hauptsacheklage erhoben wurde und Schuldner auch keinen Widerspruch eingelegt hat.
3. Aufforderung, die EV als endgültige Regelung anzuerkennen (Abschlussvereinbarung zu schließen) bis zu einem genannten Datum.
4. Ankündigung, bei Nichtreaktion Hauptsacheklage zu erheben oder Schuldner im Falle von Widerspruch die Kosten des Widerspruchsverfahrens zu tragen hat.
5. Kostenhinweis: Widerspruch nach Abschlussschreiben-Frist führt zu Kostentragung des Schuldners.

### Schritt 3 – Abschlussvereinbarung aushandeln

Typischer Inhalt der Abschlussvereinbarung:
- Schuldner erkennt Unterlassungspflicht als endgültige Regelung an.
- Schuldner verzichtet auf Widerspruch und Hauptsachewiderklage.
- Vertragsstrafe für erneuten Verstoß (üblicherweise höher als Ordnungsgeld).
- Kostenregelung (oft: jede Seite trägt eigene Kosten).
- Optional: Schadensersatzregelung.

### Schritt 4 – Hauptsacheklage als Alternative

- Wenn Schuldner Abschlussvereinbarung verweigert oder Widerspruch einlegt: Hauptsacheklage.
- Zuständigkeit: Regelmäßig dasselbe Gericht (Konnexität); ggf. Klage vor Landgericht.
- Streitwert: Entspricht in der Regel dem Verfügungsstreitwert.
- Wichtig: Bei § 926 ZPO-Antrag des Schuldners ist Frist bindend; Versäumnis führt zur EV-Aufhebung.

### Schritt 5 – Kostenfolgen beachten

- Keine Hauptsacheklage trotz Widerspruch: Kostentragung durch Antragsteller möglich.
- Abschlussschreiben rechtzeitig: Verhindert, dass Schuldner bei späterem Widerspruch keine Kostenfolgen trifft.
- Anwaltskosten für Abschlussschreiben: Erstattungsfähig als Kosten des Verfahrens (str.; BGH-Rechtsprechung beachten).

## Typische Fallen

- **Kein Abschlussschreiben gesendet:** Schuldner legt nach Monaten Widerspruch ein; Antragsteller muss doch Hauptsache führen.
- **Frist § 926 ZPO versäumt:** EV wird auf Schuldnerantrag aufgehoben; Verfahren von vorne.
- **Abschlussvereinbarung ohne Vertragsstrafe:** Erneuter Verstoß kann nur über Ordnungsmittel verfolgt werden; weniger effizient.
- **Abschlussschreiben zu früh:** Schuldner erwägt noch Widerspruch; Schreiben gibt ihm Anlass, Strategie zu überdenken. Timing ist entscheidend.

## Output-Module

- **Abschlussschreiben-Vorlage:** Vollständiger Mustertext mit Platzhaltern.
- **Abschlussvereinbarungs-Muster:** Klauseln für Unterlassung, Vertragsstrafe, Verzicht, Kosten.
- **Kostenrechnung:** Hauptsache vs. Abschluss – Vergleich der voraussichtlichen Kosten.
- **Entscheidungsbaum:** Widerspruch / Kein Widerspruch / § 926-Antrag → Handlungsoptionen.

## Quellenregel

- [§ 926 ZPO – dejure.org](https://dejure.org/gesetze/ZPO/926.html)
- [§ 924 ZPO – dejure.org](https://dejure.org/gesetze/ZPO/924.html)
- [§ 927 ZPO – dejure.org](https://dejure.org/gesetze/ZPO/927.html)
- Rechtsprechung zu Abschlussschreiben: BGH-Entscheidungen auf [bgh.de](https://www.bundesgerichtshof.de); keine BeckRS-Blindzitate.
- Bei Kostenerstattungsfragen konkrete BGH-Entscheidung angeben.

## Anschluss-Skills

- `evvollzug-neu-005` – Ordnungsmittelantrag bei Verstoß nach EV
- `unterlassungsverlangen` – Unterlassungserklärung und Vertragsstrafe
- `spezial-operate-verhandlung-vergleich-und-eskalation` – Vergleichsstrategie
- `verletzungs-triage` – Erstentscheidung IP-Verletzung

## 3. `evvollzug-neu-008-schutzschrift-register-und-forumstrategie`

**Fokus:** EV-Vollzug (Gegenseite): Schutzschrift im Schutzschriftenregister, Forumsstrategie des Antragsgegners und vorauseilende Rechtsverteidigung gegen einstweilige Verfügungen im gewerblichen Rechtsschutz.

# EV-Vollzug 008: Schutzschrift, Register und Forumstrategie (Antragsgegnerperspektive)

## Zweck und Mandatsbezug

Dieser Skill behandelt die **präventive Verteidigungsstrategie des potentiellen Antragsgegners** bei drohender einstweiliger Verfügung im gewerblichen Rechtsschutz. Wer eine Abmahnung erhalten hat oder mit einer EV rechnet, kann durch Einreichung einer Schutzschrift ins zentrale Schutzschriftenregister (ZSSR) das Gericht vorwarnen und die Gewährung einer EV ohne mündliche Verhandlung erschweren.

Mandatsbezug: Mandant hat Abmahnung erhalten (Marke, Patent, UWG, Urheberrecht) und lehnt sie ab; Abmahner hat Klageerhebung angedroht. Mandant will Beschlussverfügung ohne Anhörung verhindern. Oder: Mandant ist Wettbewerber, der beim Markteintritt mit Verfügungsantrag rechnet.

## Rechtlicher Rahmen

### Zentrale Normen und Grundlagen

- **§ 945a ZPO** – Zentrale Schutzschriften-Einreichung; Schutzschriften können beim ZSSR eingereicht werden und sind von allen ordentlichen Gerichten vor Erlass einer EV einzusehen.
- **§ 937 Abs. 2 ZPO** – Beschlussverfügung ohne mündliche Verhandlung; Schutzschrift kann diesen Weg verhindern oder erschweren.
- **§ 922 Abs. 1 ZPO** – Recht des Antragsgegners auf mündliche Verhandlung bei ernsthaften Einwendungen.
- **§ 919 ZPO** – Allgemeine Zuständigkeitsregeln; Forumstrategie des Antragsgegners.
- **§ 32 ZPO** – Besonderer Gerichtsstand der unerlaubten Handlung; beliebter Verfügungsgerichtsstand des Antragstellers.

### Das zentrale Schutzschriftenregister (ZSSR)

- Betrieben von: Elektronisches Gerichts- und Verwaltungspostfach (EGVP) unter www.schutzschriftenregister.de
- Zugang: Rechtsanwälte können Schutzschriften einreichen; Gerichte können abrufen.
- Geltungsdauer: 6 Monate ab Einreichung; Verlängerung möglich.
- Kosten: Keine Gerichtsgebühren; nur Anwaltskosten.
- Pflicht des Gerichts: Vor Erlass einer Beschlussverfügung muss das Gericht das Register abrufen (§ 945a Abs. 3 ZPO).

## Kaltstart in 5 Fragen

1. **Bedrohungslage:** Hat Mandant eine Abmahnung erhalten? Von wem, welcher Anspruch (Marke, UWG, Patent)?
2. **Abmahninhalt:** Welche Verletzungshandlung wird gerügt? Welche Unterlassungserklärung wird verlangt?
3. **Forumsfrage:** Wo würde Antragsteller voraussichtlich EV beantragen (Düsseldorf, Hamburg, München, Frankfurt)?
4. **Dringlichkeit:** Ist Schutzschrift bereits nötig oder gibt es noch Zeit für Korrespondenz?
5. **Output:** Schutzschrift-Entwurf, Forumstrategie-Memo, Entscheidungsempfehlung Unterlassungserklärung ja/nein?

## Prüfprogramm

### Schritt 1 – Schutzschrift als Instrument einschätzen

**Wann sinnvoll:**
- Abmahnung wurde abgelehnt oder modifiziert beantwortet; Antragsteller hat Klage angedroht.
- Mandant hat ernsthafte materielle Einwendungen (kein Schutzrecht, kein Verstoß, Verwirkung, Erschöpfung).
- Antragsteller neigt zu schnellen EV-Anträgen ohne vorherige Reaktion abzuwarten.

**Wann weniger sinnvoll:**
- Verletzung ist offensichtlich; Schutzschrift kaschiert nur das Problem.
- Mandant will ohnehin Hauptsachestreit vermeiden; Einigung besser.
- Schutzschrift enthüllt Verteidigungsstrategie und gibt Antragsteller Gelegenheit zur Vorbereitung.

### Schritt 2 – Schutzschriftinhalt

Pflichtinhalt einer Schutzschrift:
1. **Rubrum:** Antragsgegner (Mandant), potentieller Antragsteller, Anspruchsgegenstand.
2. **Sachverhalt:** Tatsachen aus Sicht des Antragsgegners; konkreter Tatbestand.
3. **Einwendungen:** Warum EV nicht ergehen darf.
 - Material: Schutzrecht ungültig, kein Verstoß, Erschöpfung (§ 24 MarkenG), Verwirkung.
 - Formal: Keine Dringlichkeit, fehlende Aktivlegitimation, Missbrauch.
4. **Beweisangebote:** Dokumente, eidesstattliche Versicherungen, Zeugen.
5. **Antrag:** Gericht möge von Erlass einer EV ohne mündliche Verhandlung absehen.

### Schritt 3 – Forumstrategie

**Bekannte IP-Gerichte und ihre Tendenz:**
| Gericht | Besonderheit | Tendenz EV ohne Verhandlung |
|---|---|---|
| LG Hamburg | „Fliegender Gerichtsstand"; strenger | Häufig EV ohne Verhandlung |
| LG München I | IP-Spezialkammer | Ausgewogen |
| LG Düsseldorf | Starkes Patentgericht | Ausgewogen |
| LG Frankfurt | UWG-Erfahrung | Ausgewogen |
| LG Berlin | UWG, Urheberrecht | Häufig EV ohne Verhandlung |

- Schutzschrift bei allen wahrscheinlichen Gerichtsstandorten einreichen.
- Bei Marke: Sitz des Rechtsinhabers und Ort der Verletzungshandlung (§ 32 ZPO).
- Bei UWG: Ort der Verletzungshandlung oder Niederlassung des Verletzers.

### Schritt 4 – Fristverlängerung nach Abmahnung

- Angemessene Reaktionsfrist auf Abmahnung ist Voraussetzung für Dringlichkeit der EV.
- Schutzschrift + Bitte um Fristverlängerung in Reaktion auf Abmahnung: entzieht dem Antragsteller die Dringlichkeit.
- Wenn Antragsteller trotz laufender Verhandlungen sofort EV beantragt, Selbstwiderlegung der Dringlichkeit rügen.

### Schritt 5 – Abwägung Unterlassungserklärung vs. Schutzschrift

| Option | Vorteile | Nachteile |
|---|---|---|
| Modifizierte Unterlassungserklärung | Verfahrensbeendigung, Kostenkontrolle | Anerkenntnis der Verletzung (faktisch) |
| Schutzschrift ohne Unterlassungserklärung | Keine Anerkennung; Verfahren bleibt offen | Kosten bei Niederlage im Hauptsacheverfahren |
| Keine Reaktion | Kostenlos | EV ohne mündliche Verhandlung wahrscheinlich |

## Typische Fallen

- **Schutzschrift enthüllt Hauptverteidigungsstrategie:** Antragsteller kann diese in EV-Antrag kontern.
- **Schutzschrift nicht beim richtigen Gericht:** Register wird abgerufen, aber Mandant hat falschen Gerichtsstand erwartet.
- **Ablaufende Geltungsdauer übersehen:** Schutzschrift erlischt nach 6 Monaten; bei laufender Abmahnkorrespondenz verlängern.
- **Keine Beweisangebote:** Schutzschrift ohne Belege überzeugt Gericht nicht, von Beschlussverfügung abzusehen.

## Output-Module

- **Schutzschrift-Vorlage:** Muster mit Rubrum, Sachverhalt, Einwendungen, Beweisangeboten.
- **Forumstrategie-Matrix:** Wahrscheinliche Gerichtsstände mit Tendenzeinschätzung.
- **Entscheidungsbaum:** Schutzschrift / Unterlassungserklärung / Keine Reaktion.
- **Fristverlängerungsschreiben an Abmahner:** Entwurf mit Bitte um Verhandlungszeit.

## Quellenregel

- [§ 945a ZPO – dejure.org](https://dejure.org/gesetze/ZPO/945a.html)
- [§ 937 ZPO – dejure.org](https://dejure.org/gesetze/ZPO/937.html)
- ZSSR: [schutzschriftenregister.de](https://www.schutzschriftenregister.de)
- Rechtsprechung zur Dringlichkeitsschädlichkeit: BGH und OLG-Entscheidungen auf openjur.de.
- Keine Kommentar-Blindzitate; aktuelle Gerichtspraxis zu Dringlichkeit per Gerichtsstandort prüfen.

## Anschluss-Skills

- `schutzschrift-eilverfuegung` – Schutzschrift im Detail
- `unterlassungsverlangen` – Unterlassungserklärung als Alternative
- `evvollzug-neu-001` – Vollziehungsfrist (Antragstellerperspektive)
- `verletzungs-triage` – Erstentscheidung IP-Verletzung
