---
name: mandatsabbruch-empfehlung-beweisbedarf
description: "Mandatsabbruch Empfehlung Beweisbedarf: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Mandatsabbruch Empfehlung Beweisbedarf

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Mandatsabbruch Empfehlung Beweisbedarf** im Plugin Subsumtions-Prüfer. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `mandatsabbruch-empfehlung-an-fachanwalt` | Erkennt Indikatoren für Komplexitaetsgrenzen des mechanischen Prüfens und empfiehlt Abbruch sowie Weiterleitung an Fachanwalt, Notar, Steuerberater oder Behoerde. Warnt bei Strafrecht, Verfassungsrecht, internationalem Privatrecht und Existenzgefaehrdung. |
| `beweisbedarf-und-belege-erfassen` | Erfasst pro Tatbestandsmerkmal den Beweisbedarf: Beweismittel-Katalog (Urkunden, Zeugen, Sachverständige, Augenschein, Parteivernehmung), Belege hochladen, Tatsachenbehauptung eintragen oder 'beweise ich spaeter'-Markierung setzen. Strukturiertes Beweis-Tracking nach §§ 355-484 ZPO. |
| `darlegungs-und-beweislast-verteilen` | Verteilt Darlegungs- und Beweislast nach Grundregel (wer Recht behauptet traegt Beweislast), Beweislastumkehr (Produkthaftung, Diskriminierung, DSGVO), sekundaerer Darlegungslast und Anscheinsbeweis. Pro TBM: wer muss was beweisen. |

## Arbeitsweg

Im Plugin Subsumtions-Prüfer gilt für **Mandatsabbruch Empfehlung Beweisbedarf**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `mandatsabbruch-empfehlung-an-fachanwalt`

**Fokus:** Erkennt Indikatoren für Komplexitaetsgrenzen des mechanischen Prüfens und empfiehlt Abbruch sowie Weiterleitung an Fachanwalt, Notar, Steuerberater oder Behoerde. Warnt bei Strafrecht, Verfassungsrecht, internationalem Privatrecht und Existenzgefaehrdung.

# Mandatsabbruch-Empfehlung: Weiterleitung an Fachanwalt

## Triage zu Beginn — Abbruch-Indikatoren prüfen

1. Enthält der Sachverhalt strafrechtliche Tatbestände mit möglicher Freiheitsstrafe?
2. Sind mehr als drei miteinander verknüpfte Rechtsverhältnisse betroffen?
3. Hat der Sachverhalt ausländischen Bezug oder mehrere mögliche Gerichtsstände?
4. Ist das gesamte Ergebnis von einer Generalklausel (§ 242, § 138 BGB) abhängig?
5. Betrifft der Sachverhalt Wohnung, Arbeitsplatz, Aufenthaltsstatus oder wesentliches Vermögen?

## Zweck

Mechanisches Subsumieren hat Grenzen. Dieser Skill markiert den Punkt, an dem automatisierte Hilfe nicht mehr ausreicht und qualifizierte Fachleute unverzüglich eingeschaltet werden müssen.

## Zentrale berufsrechtliche Normen

- § 43 BRAO — Pflicht des Rechtsanwalts zur gewissenhaften Berufsausübung; Mandant darf nicht schlechtergestellt werden
- § 3 Abs. 3 RDG — Erlaubnisfreie Rechtsdienstleistung endet, wo Rechtsberatung erforderlich wird
- § 90 BVerfGG — Verfassungsbeschwerde: Erschöpfung Rechtsweg, 1-Jahres-Frist (§ 93 Abs. 1 BVerfGG)
- §§ 1 ff. InsO — Insolvenzantragspflicht und Forderungsanmeldung erfordern Fachanwaltswissen

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Abbruch-Indikatoren

Das System empfiehlt Abbruch und Verweisung an Fachleute bei folgenden Konstellationen:

### Strafrecht mit drohender Freiheitsstrafe

Sobald ein Sachverhalt Straftatbestände enthält, die eine Freiheitsstrafe von mehr als einem Jahr vorsehen oder bei denen eine Verhaftung, Untersuchungshaft oder Anklage droht: **Sofortige Empfehlung eines Strafverteidigers (Fachanwalt für Strafrecht).**

Nemo-tenetur-Grundsatz: Niemand ist verpflichtet, sich selbst zu belasten. Mechanisches Subsumieren kann diesen Grundsatz nicht beachten.

### Internationales Privatrecht / Kollisionsrecht

Sachverhalte mit ausländischen Vertragsparteien, ausländischen Vermögenswerten oder mehreren Gerichtsständen erfordern die Prüfung des anwendbaren Rechts (Rom I-VO, Rom II-VO, EuErbVO, Haager Übereinkommen). Empfehlung: Fachanwalt mit IPR-Erfahrung.

### Verfassungsbeschwerden und Grundrechts-Intensiveingriffe

Empfehlung: Fachanwalt für Verfassungsrecht oder spezialisierte Kanzlei. Rechtswegerschöpfung und 1-Jahres-Frist (§ 93 Abs. 1 BVerfGG) sind formal komplex.

### Insolvenzrecht mit laufendem Insolvenzverfahren

Sobald ein Schuldner insolvent ist oder das Insolvenzverfahren eröffnet wurde, unterliegen Forderungsanmeldung, Anfechtungsrecht und Aussonderung eigenen Regeln (InsO). Empfehlung: Fachanwalt für Insolvenz- und Sanierungsrecht.

### Existenzgefährdende Sachverhalte

Sachverhalte, bei denen ein wesentlicher Teil des Vermögens, der Wohnung, des Arbeitsplatzes oder der Aufenthaltsstatus betroffen ist.

### Mehr als drei miteinander verknüpfte Rechtsverhältnisse

Wenn der Sachverhalt mehr als drei miteinander verknüpfte Rechtsverhältnisse enthält (z.B. Dreiecksbeziehungen, Konzernstrukturen, mehrstufige Verträge).

## Empfehlungen nach Sachgebiet

| Sachgebiet | Empfehlung |
|-----------|-----------|
| Strafrecht | Fachanwalt für Strafrecht, ggf. Pflichtverteidiger |
| Steuer | Steuerberater, Fachanwalt für Steuerrecht |
| Notarielle Beurkundung (Immobilien, GmbH-Anteile, Erbvertrag) | Notar |
| Behördlicher Bescheid | Fachanwalt für Verwaltungsrecht |
| Sozialleistungen | Sozialrechtsberatungsstelle, Fachanwalt für Sozialrecht |
| Arbeitsrecht | Fachanwalt für Arbeitsrecht, Gewerkschaftsrechtsschutz |
| Aufenthaltsrecht | Fachanwalt für Migrationsrecht |
| Familienrecht | Fachanwalt für Familienrecht |
| Insolvenz | Fachanwalt für Insolvenz- und Sanierungsrecht |
| IPR/Internationales Recht | Spezialkanzlei IPR/Auslandsbezug |

## Output-Template Abbruchhinweis

**Adressat:** Mandant — Tonfall verständlich-erklärend, klar

```
Wichtiger Hinweis: Grenzen der automatisierten Prüfung

Ihr Sachverhalt enthält Elemente, die eine qualifizierte anwaltliche Beratung
zwingend erfordern. Grund: [ABBRUCHINDIKATOR]

Wir empfehlen Ihnen dringend:
1. Kontaktieren Sie einen Fachanwalt für [FACHGEBIET]
2. Bringen Sie zum Termin mit: [DOKUMENTE]
3. Wichtige Frist: [DATUM/FRIST] — bitte nicht verstreichen lassen

Suche nach Fachanwälten: www.rechtsanwaltskammer.de oder www.anwaltauskunft.de
```

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.

## 2. `beweisbedarf-und-belege-erfassen`

**Fokus:** Erfasst pro Tatbestandsmerkmal den Beweisbedarf: Beweismittel-Katalog (Urkunden, Zeugen, Sachverständige, Augenschein, Parteivernehmung), Belege hochladen, Tatsachenbehauptung eintragen oder 'beweise ich spaeter'-Markierung setzen. Strukturiertes Beweis-Tracking nach §§ 355-484 ZPO.

# Beweisbedarf und Belege erfassen

## Triage zu Beginn — kläre vor der Beweiserfassung

1. In welchem Verfahren wird Beweis geführt? (ZPO / VwGO / StPO / SGG / FamFG)
2. Welche Partei trägt die Beweislast für das TBM? (Anspruchsteller oder Gegenseite)
3. Ist die Tatsache streitig — oder unstreitig/offenkundig (§ 291 ZPO)?
4. Liegt bereits ein Beweisbeschluss (§ 359 ZPO) vor?
5. Besteht Gefahr im Verzug? → Antrag auf Sicherung des Beweises §§ 485-494a ZPO prüfen

## Zweck

Jede Subsumtion steht und fällt mit dem Beweisergebnis. Dieser Skill erfasst für jedes Tatbestandsmerkmal (TBM), welche Beweismittel benötigt werden, welche der Nutzer bereits hat und welche noch beschafft werden müssen. Er erstellt eine strukturierte Beweisliste.

## Zentrale Normen

- §§ 355-484 ZPO — Beweisaufnahme allgemein
- § 286 ZPO — Freie Beweiswürdigung; volle richterliche Überzeugung erforderlich
- § 287 ZPO — Schadensschätzung bei Ausschluss anderer Beweismittel
- §§ 415 ff. ZPO — Urkundsbeweis (öffentliche und private Urkunden)
- §§ 373 ff. ZPO — Zeugenbeweis
- §§ 402 ff. ZPO — Sachverständigenbeweis
- §§ 371 ff. ZPO — Augenschein und elektronische Dokumente
- §§ 445-455 ZPO — Parteivernehmung (subsidiär)
- §§ 485-494a ZPO — Selbständiges Beweisverfahren

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Beweismittel-Katalog (ZPO)

| Beweismittel | § ZPO | Typische Nachweise |
|-------------|-------|-------------------|
| Urkundsbeweis | §§ 415 ff. ZPO | Vertrag, Rechnung, E-Mail, Bescheid, Quittung, Protokoll |
| Zeugenbeweis | §§ 373 ff. ZPO | Personen, die den TBM-relevanten Vorgang erlebt haben |
| Sachverständigenbeweis | §§ 402 ff. ZPO | Technische, medizinische, buchhalterische Fragen |
| Augenschein | §§ 371 ff. ZPO | Besichtigung von Sachen, Orten, digitalen Inhalten |
| Parteivernehmung | §§ 445 ff. ZPO | Nur subsidiär; Nutzer als Partei |
| Elektronische Beweismittel | § 371 Abs. 1 S. 2 ZPO | Screenshots, Metadaten, Logs — Echtheit muss dargelegt werden |

Im Verwaltungs- und Strafverfahren gelten die jeweiligen Verfahrensordnungen (VwGO, StPO); das System passt den Katalog an.

## Schritt-für-Schritt-Vorgehen pro TBM

Das System geht jedes TBM der Reihe nach durch und fragt:

1. **Tatsachenbehauptung:** Was behauptet der Nutzer für dieses TBM? (Freitext-Eingabe)
2. **Beweislast:** Wer muss beweisen? — Grundsatz: Wer einen Anspruch geltend macht, trägt die Beweislast für dessen Voraussetzungen; Gegenseite für Einwendungen/Einreden.
3. **Beleg vorhanden?** Der Nutzer kann angeben:
 - (A) Beleg liegt vor (Dokument, Foto, Screenshot) → Hochladen oder Benennen
 - (B) Zeuge bekannt → Name und Erreichbarkeit notieren
 - (C) Tatsache behaupte ich; Beleg beschaffe ich später → Markierung "offen"
 - (D) Keine Tatsache vorhanden für dieses TBM → TBM als nicht erfüllt markieren
4. **Sekundäre Darlegungslast:** Liegt ein Fall vor, in dem der Gegner näherliegende Informationen hat? → Verweis auf BGH-Rechtsprechung zur sekundären Darlegungslast
5. **Beweiswert-Hinweis:** Das System gibt einen groben Hinweis auf den typischen Beweiswert des genannten Beweismittels (z.B. öffentliche Urkunde: voller Beweis § 415 ZPO; Privaturkunde: § 416 ZPO begrenzt).

## Entscheidungsbaum Beweisführung

```
Ist die Tatsache streitig?
├─ Nein → unstreitig oder offenkundig → kein Beweismittel nötig
└─ Ja → Beweislast bestimmen
 ├─ Kläger trägt Last → Beweismittel aus Katalog wählen
 │ ├─ Urkunde verfügbar? → Urkundsbeweis §§ 415 ff. ZPO
 │ ├─ Zeuge vorhanden? → Zeugenbeweis §§ 373 ff. ZPO
 │ ├─ Technische Frage? → Sachverständiger §§ 402 ff. ZPO
 │ └─ Kein direktes Beweismittel? → Anscheinsbeweis prüfen
 └─ Beklagter trägt Last → Einwand/Einrede belegen
```

## Besondere Konstellationen

### Anscheinsbeweis (prima facie)

Bei typischem Geschehensablauf greift der Anscheinsbeweis (z.B. Auffahrunfall → Abstandsmangel). Der Gegner muss den typischen Ablauf erschüttern durch Darlegung atypischer Umstände.

### Elektronische Dokumente

E-Mails, Screenshots und PDFs sind Beweismittel, aber ihre Echtheit kann bestritten werden. Das System empfiehlt:
- Metadaten sichern (Datum, Absender, Header)
- Zeitnahe Sicherung und Archivierung
- Ggf. Datenschutz-Aspekte bei personenbezogenen Drittdaten beachten

### Selbständiges Beweisverfahren (§§ 485-494a ZPO)

Vor Klageerhebung oder wenn Beweis zu sichern ist: Antrag auf Einholung eines Sachverständigengutachtens. Voraussetzung: Antragsteller hat rechtliches Interesse an Feststellung (z.B. drohender Beweismittelverlust, Verjährungsgefahr).

### Zeugenbeweis

Das System fragt nach vollständigem Namen und Adresse des Zeugen. Es weist darauf hin, dass das Gericht den Zeugen selbst lädt.

### Urkundsbeweis — Originale vs. Kopien

Das System weist darauf hin, dass Originale stets vorzuziehen sind. Kopien können bestritten werden (§ 420 ZPO).

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Beweis-Tracking-Liste

Am Ende der Beweiserfassung erstellt das System eine tabellarische Übersicht:

| TBM | Behauptete Tatsache | Beweismittel | Beweislast | Status |
|-----|--------------------|--------------|-----------|----|
| [TBM 1] | [Nutzerangabe] | [Typ] | Kläger/Beklagter | vorhanden / offen / fehlt |
| [TBM 2] | … | … | … | … |

"Offen" markierte TBM werden als Risikopositionen der Klage / des Antrags ausgewiesen.

## Output-Template Beweisliste (Mandantenbrief-Auszug)

**Adressat:** Mandant — Tonfall verständlich-erklärend

```
Sehr geehrte/r Frau/Herr [NAME],

zur Vorbereitung des Verfahrens [AKTENZEICHEN] benötige ich folgende
Unterlagen und Informationen:

1. [Beweismittel zu TBM 1] — bitte bis [DATUM] einreichen
2. [Zeuge zu TBM 2] — Name und Anschrift: [...]
3. [Noch offen / wird durch Gegenseite beizubringen]

Bitte beachten Sie: Ohne diese Nachweise kann ich den Anspruch auf
[RECHTSVERLETZUNG] nicht mit der erforderlichen Sicherheit belegen.

Mit freundlichen Grüßen
[KANZLEI]
```

---

Hinweis: Keine Rechtsberatung. Mechanische Prüfung anhand vom Nutzer behaupteter Tatsachen und der vom Nutzer gewählten Norm. Falsche Normwahl oder falsche Sachverhaltsdarstellung kann das gesamte Ergebnis entwerten.

<!-- AUDIT 27.05.2026
BGH VI ZR 290/18 (NOT_FOUND): Aktenzeichen existiert auf dejure.org nicht. Gesamte Zeile aus "Aktuelle Rechtsprechung" entfernt.
-->

## 3. `darlegungs-und-beweislast-verteilen`

**Fokus:** Verteilt Darlegungs- und Beweislast nach Grundregel (wer Recht behauptet traegt Beweislast), Beweislastumkehr (Produkthaftung, Diskriminierung, DSGVO), sekundaerer Darlegungslast und Anscheinsbeweis. Pro TBM: wer muss was beweisen.

# Darlegungs- und Beweislast verteilen

## Zweck

Die Beweislast bestimmt, wer im Prozess das Risiko des Nichtbeweises trägt. Dieser Skill ordnet jedem Tatbestandsmerkmal zu, welche Partei darlegungs- und beweislastpflichtig ist, und weist auf Ausnahmen und Beweislastumkehrungen hin.

## Grundregel

**Grundsatz:** Jede Partei trägt die Beweislast für die Tatsachen, aus denen sie für sich günstige Rechtsfolgen ableitet (BGH ständige Rechtsprechung; normentheoretische Lehre).

**Konkret bei Anspruchsgrundlagen:**
- Anspruchsteller (Kläger) beweist die anspruchsbegründenden TBM (z. B. Abschluss des Vertrags, Pflichtverletzung, Schaden, Kausalität)
- Anspruchsgegner (Beklagter) beweist rechtsvernichtende (z. B. Erfüllung § 362 BGB), rechtshindernde (z. B. Anfechtung § 142 BGB) und rechtshemmende (z. B. Einrede der Verjährung) Tatsachen

## Beweismaß

- **§ 286 ZPO (Regelfall):** Volle richterliche Überzeugung; kein mathematischer Beweis, aber ein für das praktische Leben brauchbarer Grad an Gewissheit.
- **§ 287 ZPO (Schadenshöhe, haftungsausfüllende Kausalität):** Überwiegende Wahrscheinlichkeit genügt; richterliches Schätzungsermessen.
- **§ 294 ZPO (einstweiliger Rechtsschutz):** Glaubhaftmachung; eidesstattliche Versicherung zulässig.

## Beweismittel ZPO

| Beweismittel | Normen ZPO | Besonderheit |
|---|---|---|
| Urkunden | §§ 415–455 ZPO | Öffentl. Urkunde: volle Beweiswirkung (§ 415); Privaturkunde: Echtheitsvermutung (§ 440) |
| Zeugen | §§ 373–401 ZPO | Ladung, Vernehmung, Zeugnisverweigerungsrecht §§ 383 ff. |
| Sachverständige | §§ 402–414 ZPO | Gutachten, Ergänzungsgutachten, Obergutachten |
| Augenschein | §§ 371–372a ZPO | Besichtigung, digitale Daten |
| Parteivernehmung | §§ 445–455 ZPO | Subsidiär; nur bei Einverständnis oder besonderer Sachlage |

## Beweislastumkehr

In bestimmten Rechtsgebieten ist die Beweislast gesetzlich oder richterrechtlich umgekehrt:

### Produkthaftung (ProdHaftG / DSGVO-Haftung)

- § 1 Abs. 4 ProdHaftG: Hersteller muss beweisen, dass Fehler nicht vorlag oder nicht auf sein Verhalten zurückzuführen ist
- Art. 82 Abs. 3 DSGVO: Verantwortlicher muss beweisen, dass er nicht verantwortlich ist

### Arbeitsrecht

- § 22 AGG: Bei Indizien für Diskriminierung muss der Arbeitgeber beweisen, dass kein Verstoß gegen das Benachteiligungsverbot vorliegt
- § 1 Abs. 2 S. 4 KSchG: Arbeitgeber trägt Beweislast für dringende betriebliche Erfordernisse

### Arzthaftung

- § 630h Abs. 5 BGB: Bei grobem Behandlungsfehler, der geeignet ist, den eingetretenen Schaden zu verursachen, tritt Beweislastumkehr ein (BGH-Linie; live zu prüfen unter bgh.de oder dejure.org)

### DSGVO

- Art. 5 Abs. 2 DSGVO (Rechenschaftspflicht): Verantwortlicher muss Einhaltung der Grundsätze nachweisen können

## Sekundäre Darlegungslast

Wenn der Darlegungspflichtige außerhalb des maßgeblichen Geschehensablaufs steht:

**Voraussetzungen (BGH-Linie; live zu prüfen):**
1. Kläger kann bestimmte Tatsachen nicht näher darlegen
2. Beklagter hat eigene Kenntnisse, die er offenbaren könnte
3. Offenbarung ist dem Beklagten zumutbar

Folge: Substantiiertes Bestreiten mit Gegenangaben; bloßes Leugnen genügt nicht (§ 138 Abs. 2 ZPO).

## Anscheinsbeweis (Prima facie)

Bei typischen Geschehensabläufen, die nach allgemeiner Lebenserfahrung auf eine bestimmte Ursache hindeuten:

- Auffahrunfall → Anschein für Unaufmerksamkeit des Auffahrenden
- Sturz durch nasse Böden in Supermarkt → Anschein für Verkehrspflichtverletzung
- Kfz-Unfall durch defekte Bremsen → Anschein für Halterhaftung

**Erschütterung:** Gegner muss konkrete Umstände vortragen, die den Anschein erschüttern; kein Vollbeweis des Gegenteils erforderlich.

## Negativbeweis

Wer eine negative Tatsache beweisen muss (z. B. keine Kenntnis, keine Zahlung), kann durch Indizienbeweis oder Erschütterung des Gegenbeweises vorgehen. Das System weist auf erhöhten Schwierigkeitsgrad und sekundäre Darlegungslast der Gegenseite hin.

## Ausgabe

Pro TBM: Tabelle mit Angabe der beweisbelasteten Partei, dem einschlägigen Rechtssatz und dem Beweismitteltyp. Markierung von Ausnahmen (Umkehr, sekundäre Darlegungslast, Anscheinsbeweis).

---

Hinweis: Keine Rechtsberatung. Mechanische Prüfung anhand vom Nutzer behaupteter Tatsachen und der vom Nutzer gewählten Norm.

## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern (dejure.org, bgh.de, openjur.de).
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.
- Normtext live prüfen: gesetze-im-internet.de (BGB, ZPO, ProdHaftG, AGG, KSchG), dejure.org (Querverweise und Rechtsprechungsübersicht).
