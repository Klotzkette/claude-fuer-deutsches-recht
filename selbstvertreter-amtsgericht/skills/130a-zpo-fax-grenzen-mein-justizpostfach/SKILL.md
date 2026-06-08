---
name: 130a-zpo-fax-grenzen-mein-justizpostfach
description: "130a ZPO FAX Grenzen Mein Justizpostfach im Selbstvertretung am Amtsgericht: prüft konkret Elektronische Einreichung nach § 130a ZPO für Buerger, Einreichung per Fax und ihre verbleibenden Grenzen, Einrichtung und Nutzung von Mein Justizpostfach (MJP) für. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Schritt."
---

# 130a ZPO FAX Grenzen Mein Justizpostfach

## Arbeitsbereich

**130a ZPO FAX Grenzen Mein Justizpostfach** ordnet den Fall über die tragenden Prüfungslinien: Elektronische Einreichung nach § 130a ZPO für Buerger, Einreichung per Fax und ihre verbleibenden Grenzen, Einrichtung und Nutzung von Mein Justizpostfach (MJP) für. Zuerst wird das Feld bestimmt, das die Akte wirklich trägt; ergänzende Felder kommen nur hinzu, wenn sie dieselbe Frist, Zuständigkeit, Beweislast oder denselben Output berühren.
## Prüfungslinien

| Prüfungslinie | Fokus |
| --- | --- |
| `einreichung-130a-zpo-elektronisch-buerger` | Elektronische Einreichung nach § 130a ZPO für Buerger. Sichere Übermittlungswege qualifizierte elektronische Signatur Bedeutung der Eingangsbestätigung. Abgrenzung zu Email und einfachem Scan. Wann ist elektronische Einreichung fristwahrend. |
| `einreichung-fax-und-grenzen` | Einreichung per Fax und ihre verbleibenden Grenzen. Fax als Schriftform-Ersatz bei kurzfristiger Fristwahrung. Was Sie aufbewahren muessen Sendebericht Bestätigung und Risiken durch Verlust oder unleserliche Übertragung. |
| `einreichung-mein-justizpostfach-mjp-2024` | Einrichtung und Nutzung von Mein Justizpostfach (MJP) für Buerger seit 2024. Sichere elektronische Einreichung von Klagen und Schriftsaetzen an Gerichte. BundID-Login Postfach-Funktion Versandbestätigung und Zustellung. |

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: ZPO §§ 78, 79, 129, 253, 495a, 511, 517, GVG §§ 23, 71, SGG §§ 73, 78, 87, 90, 144, 160; §23 GVG; §511 ZPO-Grenzen, Klage — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.
## Prüfungslinien im Detail

## 1. `einreichung-130a-zpo-elektronisch-buerger`

**Fokus:** Elektronische Einreichung nach § 130a ZPO für Buerger. Sichere Übermittlungswege qualifizierte elektronische Signatur Bedeutung der Eingangsbestätigung. Abgrenzung zu Email und einfachem Scan. Wann ist elektronische Einreichung fristwahrend.

### Elektronische Einreichung nach § 130a ZPO

## Worum geht es?

Eine elektronische Einreichung kann Schriftformersatz sein — aber nur unter bestimmten Voraussetzungen. § 130a ZPO regelt das. Fuer Buerger ist die Hauptvariante Mein Justizpostfach (MJP). Diese Skill ordnet die elektronische Einreichung allgemein ein und zeigt die Unterschiede zwischen den Wegen.

## Wann brauchen Sie diese Skill?

- Sie ueberlegen, ob Sie elektronisch oder per Post einreichen sollen.
- Sie haben qualifizierte elektronische Signatur (qeS) und wollen wissen, wie diese funktioniert.
- Sie wollen wissen, ob Email reicht.

## Fachbegriffe (kurz erklaert)

- **Elektronisches Dokument**: Datei (PDF, anderer Format), die elektronisch uebermittelt wird.
- **Qualifizierte elektronische Signatur (qeS)**: Elektronische Signatur mit Sicherheits-Zertifikat — gleichwertig handschriftlicher Unterschrift.
- **Sicherer Uebermittlungsweg**: Vom Gesetz anerkannte Form der Uebermittlung (beA für Anwaelte, MJP für Buerger).

## Rechtsgrundlagen

- **§ 130a ZPO** — Elektronisches Dokument; einreichungsfaehig wenn signiert (qeS) oder ueber sicheren Uebermittlungsweg + einfache Signatur.
- **§ 130a IV ZPO** — Eingangsbestaetigung.
- **§ 130a V ZPO** — Wirkung des Eingangs.
- **§ 130b ZPO** — Form der gerichtlichen Entscheidungen.
- **§ 174 ZPO** — Zustellung an Anwaelte ueber beA.

## Schritt-für-Schritt-Anleitung

### Schritt 1 — Welche elektronischen Wege gibt es?

Fuer Buerger:

1. **Mein Justizpostfach (MJP)** — empfohlen. Skill `einreichung-mein-justizpostfach-mjp-2024`.
2. **EGVP-Buergerkonto** — aelter, weiter verfuegbar.
3. **De-Mail** (mit Absender-Bestaetigt) — schmaler Anwendungsbereich.
4. **qeS + Email** — selten, aber moeglich, wenn das Gericht eine Adresse veroeffentlicht.

### Schritt 2 — Email ohne qeS reicht NICHT

Eine normale Email **ohne** qualifizierte elektronische Signatur und **ohne** sicheren Uebermittlungsweg ist **kein** § 130a-Eingang. Sie kann verworfen werden und Frist gehen verloren.

### Schritt 3 — qeS einsetzen

Wenn Sie eine qeS haben (z. B. Signaturkarte mit Personalausweis-Funktion):

- PDF mit qeS signieren (Software: signLive, OpenSign, DigiSeal etc.).
- Per Email an die Gerichts-Postfach-Adresse senden.
- Gericht muss Email-Adresse veroeffentlicht haben.

### Schritt 4 — Sicherer Uebermittlungsweg + einfache Signatur

Bei MJP-Versand:

- Einfache Signatur (Name unter PDF) genuegt.
- Voraussetzung: MJP mit BundID Niveau "hoch".

### Schritt 5 — Eingangsbestaetigung pruefen

§ 130a IV ZPO: Gericht muss Eingang bestaetigen.

- MJP zeigt Bestaetigung im Posteingang.
- EGVP-Buerger-Konto ebenfalls.

Speichern Sie die Bestaetigung.

### Schritt 6 — Wirkung des Eingangs

§ 130a V ZPO: Das elektronische Dokument ist eingegangen, sobald es auf der für den Empfang bestimmten Einrichtung des Gerichts gespeichert ist. Datum/Uhrzeit der Speicherung ist Eingang.

Auch um 23:59 Uhr eines Frist-Tags eingereicht ist fristwahrend (sofern Bestaetigung).

### Schritt 7 — Bei Uebertragungsfehler

Wenn die Uebermittlung versagt:

- Sie versuchen es erneut.
- Wenn die Frist abgelaufen ist und Sie unverschuldet nicht uebermitteln konnten: § 130a VI ZPO erlaubt Heilung — Sie reichen unverzueglich nach.

### Schritt 8 — Pflicht oder Wahl?

§ 130d ZPO verpflichtet **Anwaelte und Behörden** zur elektronischen Einreichung. Buerger sind **nicht** verpflichtet — koennen weiter Papier. Aber elektronisch ist praktisch oft besser.

## Worauf Sie besonders achten muessen

- **Email allein reicht nicht**. Ausnahme: Email mit qeS und an veroeffentlichte Adresse.
- **Bestaetigung speichern**. Bei Frist-Streitigkeit ist sie Ihr Beweis.
- **Niveau "hoch" der BundID** ist Kern.
- **Datei-Format**: PDF/A. Andere Formate koennen abgelehnt werden.

## Typische Fehler

- "Email an Gerichts-Email-Adresse genuegt." → Nur wenn qeS oder sicherer Uebermittlungsweg.
- "Ich habe einen Screenshot der Bestaetigung." → Bestaetigungs-Dokument vollstaendig speichern.
- "PDF mit Foto der Unterschrift." → Kein qeS, kein sicherer Weg — bestenfalls wirkungslos.

## Querverweise

- `einreichung-mein-justizpostfach-mjp-2024` — MJP konkret.
- `einreichung-papierform-mit-abschriften` — Papier-Alternative.
- `einreichung-fax-und-grenzen` — Fax.
- `zurechnungsproblem-versand-durch-dritte` — Versand-Risiko.

## Quellen und Aktualitaet

Stand: 05/2026. § 130a ZPO seit Gesetz zur Förderung des elektronischen Rechtsverkehrs (FoeRV) erweitert. § 130d ZPO Anwaltszwang elektronisch — Buerger weiter wahlfrei.

## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.

## 2. `einreichung-fax-und-grenzen`

**Fokus:** Einreichung per Fax und ihre verbleibenden Grenzen. Fax als Schriftform-Ersatz bei kurzfristiger Fristwahrung. Was Sie aufbewahren muessen Sendebericht Bestätigung und Risiken durch Verlust oder unleserliche Übertragung.

### Einreichung per Fax — was noch geht

## Worum geht es?

Fax war jahrzehntelang der Standard für kurzfristige Einreichungen im Justizalltag. Auch heute ist es nicht tot — viele Gerichte halten Fax-Anschluesse. Fuer Buerger ist Fax oft eine pragmatische Loesung, wenn die Frist droht und MJP nicht eingerichtet ist. Aber: Fax ist fehleranfaellig und nicht uneingeschraenkt rechtssicher. Diese Skill zeigt die Grenzen.

## Wann brauchen Sie diese Skill?

- Sie haben eine kurze Frist und keine andere Moeglichkeit.
- Sie wollen wissen, ob Fax bei Ihrem Gericht noch funktioniert.
- Sie haben per Fax gesendet und sind unsicher, ob es angekommen ist.

## Fachbegriffe (kurz erklaert)

- **Fax**: Telefax-Uebertragung; auch heute praktisch noch genutzt.
- **Sendebericht / OK-Bestaetigung**: Fax-Geraet stellt aus, wenn Uebertragung erfolgreich war.
- **Computerfax**: Email-zu-Fax-Dienste, technisch aehnlich Fax.

## Rechtsgrundlagen

- **§ 130 Nr. 6 ZPO** — Unterschrift; bei Telefax reicht eingescannte handschriftliche Unterschrift (BGH-Rspr.).
- **§ 130a ZPO** — Elektronisches Dokument (Fax faellt grundsaetzlich darunter, wenn Anforderungen erfuellt).
- **§ 167 ZPO** — Rueckwirkung Zustellung.

## Schritt-für-Schritt-Anleitung

### Schritt 1 — Fax-Nummer des Gerichts ermitteln

- Website des Amtsgerichts (justiz.de).
- Telefonisch erfragen ueber Geschaeftsstelle.
- Bei Eilbeduerftigkeit unbedingt telefonisch bestaetigen, ob Fax aktiv und betriebsbereit.

### Schritt 2 — Schriftsatz vorbereiten

- Original unterschrieben (handschriftlich).
- Sauberer Druck, hoher Kontrast — Fax verschlechtert die Qualitaet.

### Schritt 3 — Versenden

- Eigenes Fax-Geraet, Online-Fax-Dienst, Hostel/Buero.
- Achten Sie auf vollstaendige Uebertragung (Letzte Seite enthalten?).

### Schritt 4 — Sendebericht aufbewahren

Das **wichtigste**: der **Sendebericht** mit "OK"-Vermerk, Datum, Uhrzeit, Empfaenger-Nummer und Seitenanzahl.

- Fax-Geraet druckt automatisch.
- Online-Dienst zeigt Bestaetigung.

Aufbewahren! Im Fristen-Streit ist er Ihr Beweis.

### Schritt 5 — Empfangsbestaetigung anfordern

Wenn Frist droht und Sie unsicher sind: am naechsten Werktag bei der Geschaeftsstelle anrufen und Empfang bestaetigen lassen.

### Schritt 6 — Fax ist eingegangen, wenn ...

BGH-Linie: Fax ist eingegangen, sobald es auf dem **Empfangsgeraet** des Gerichts vollstaendig gespeichert ist. Speicher-Zeitpunkt des Empfangs-Faxes zaehlt.

Wenn das Fax wegen Geraete-Stoerung beim Empfaenger nicht ankommt — und Sie das nicht erkennen konnten — wirkt sich BGH-Wiedereinsetzungs-Rechtsprechung guenstig aus. Aber: Sie tragen das **Uebertragungsrisiko**, sofern Sie ein technisches Problem haetten erkennen muessen.

### Schritt 7 — Computerfax / Online-Fax

- Email-zu-Fax-Dienst: rechtlich aehnlich Fax.
- Aber: Authentizitaet kann schwerer beweisbar sein.
- BGH hat Online-Fax bei korrektem Sendebericht akzeptiert.

### Schritt 8 — Alternativen wenn moeglich

Fax ist Ueberbrueckung — wenn Sie laufend Schriftsaetze einreichen, richten Sie MJP ein.

## Worauf Sie besonders achten muessen

- **Sendebericht ist Beweis**. Ohne ihn keine Frist-Wahrung.
- **Vollstaendigkeit pruefen**: Manchmal verzichtet das Fax-Geraet bei langen Sendungen auf einzelne Seiten.
- **Lesbarkeit**: Schlechter Druck wird durch Fax noch schlechter.
- **Fristwahrung**: Eingang vor 24:00 Uhr des Fristtags reicht.

## Typische Fehler

- "Ich sende und vergesse Sendebericht." → Beweisfrei.
- "Ich sehe nur 'gesendet' im Display." → "Gesendet" heisst nicht "empfangen". Sendebericht "OK" ist entscheidend.
- "Fax statt MJP für staendige Einreichung." → Auf Dauer zu fehleranfaellig. Wenden Sie sich an MJP.

## Querverweise

- `einreichung-mein-justizpostfach-mjp-2024` — Bessere elektronische Alternative.
- `einreichung-papierform-mit-abschriften` — Papier-Alternative.
- `wiedereinsetzung-frist-233-zpo` — Wenn Frist versaeumt.
- `fristen-berechnen-187-188-bgb` — Frist-Berechnung.

## Quellen und Aktualitaet

Stand: 05/2026. Fax-Einreichung weiterhin moeglich; mehrere Gerichte planen aber Abbau. Vor Verlass auf Fax telefonisch bestaetigen, dass Anschluss aktiv ist.

## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.

## 3. `einreichung-mein-justizpostfach-mjp-2024`

**Fokus:** Einrichtung und Nutzung von Mein Justizpostfach (MJP) für Buerger seit 2024. Sichere elektronische Einreichung von Klagen und Schriftsaetzen an Gerichte. BundID-Login Postfach-Funktion Versandbestätigung und Zustellung.

### Mein Justizpostfach (MJP): elektronisch beim Gericht einreichen

## Worum geht es?

Seit Anfang 2024 koennen Buerger **Mein Justizpostfach (MJP)** nutzen, um Schriftsaetze elektronisch und rechtssicher an Gerichte zu uebermitteln. Das ist der buergerfreundliche Pendant zum beA der Anwaltschaft. Es ist kostenlos, sicher und nutzt die BundID. Mit MJP koennen Sie Klagen, Antraege, Schriftsaetze einreichen — ohne Postweg, mit klarem Zustellungs-Nachweis.

## Wann brauchen Sie diese Skill?

- Sie wollen Klage oder Schriftsatz elektronisch einreichen.
- Sie haben noch kein MJP-Konto und wollen es einrichten.
- Sie wollen wissen, ob MJP für alle Gerichte funktioniert.

## Fachbegriffe (kurz erklaert)

- **Mein Justizpostfach (MJP)**: Buergerportal zur sicheren Kommunikation mit Gerichten und Behörden.
- **BundID**: Bundeseinheitliches Login der Verwaltung — Voraussetzung für MJP.
- **EGVP (Elektronisches Gerichts- und Verwaltungspostfach)**: Das technische Netz, in dem MJP eingebettet ist.
- **Sicherer Uebermittlungsweg**: Form, die § 130a ZPO als gleichwertig zur Schriftform anerkennt.

## Rechtsgrundlagen

- **§ 130a ZPO** — Elektronisches Dokument.
- **§ 130a III ZPO** — Sicherer Uebermittlungsweg.
- **§ 130d ZPO** — Pflicht zur elektronischen Einreichung **für Anwaelte**. Buerger sind nicht zur elektronischen Einreichung verpflichtet — koennen aber.

## Schritt-für-Schritt-Anleitung

### Schritt 1 — BundID einrichten

Vor MJP brauchen Sie eine **BundID**. Diese ist Voraussetzung.

- URL: id.bund.de.
- Identifizierung wahlweise: nPA (neuer Personalausweis) mit AusweisApp, oder Elster-Zertifikat, oder Benutzername+Passwort (geringere Vertrauensstufe).
- Hoechste Vertrauensstufe ("Niveau hoch") ist für rechtssichere MJP-Nutzung erforderlich.

### Schritt 2 — MJP-Konto aktivieren

- Auf bund.de oder ueber das Justizportal "Mein Justizpostfach" suchen.
- Mit BundID einloggen.
- Postfach wird automatisch eingerichtet.

### Schritt 3 — Adresse herausfinden

Jedes Gericht hat eine EGVP-Adresse. Im MJP-Portal koennen Sie nach Empfaenger suchen:

- "Amtsgericht Musterstadt" eingeben.
- Korrekte Behörde auswaehlen.

### Schritt 4 — Schriftsatz vorbereiten

- Klageschrift als PDF/A (langzeitarchivfaehig).
- Anlagen ebenfalls PDF.
- Dateien benennen klar: "Klageschrift.pdf", "Anlage_K1_Vertrag.pdf".

### Schritt 5 — Nachricht erstellen

- Empfaenger Gericht.
- Betreff: "Klage [Name] ./. [Name]".
- Im Nachrichten-Text kurze Eroeffnung.
- Anhang: Klageschrift + Anlagen.

### Schritt 6 — Signieren

Zwei Optionen:

- **Einfache Signatur**: Name unter dem PDF (z. B. "Hans Mustermann"). Bei MJP mit "Niveau hoch" zaehlt das als sicherer Uebermittlungsweg.
- **Qualifizierte elektronische Signatur (qeS)**: Optional. Nur wenn vorhandene Karte/Token.

Fuer Buerger reicht **einfache Signatur + MJP/Niveau hoch**.

### Schritt 7 — Absenden

- Nachricht abschicken.
- Sie erhalten eine **Eingangsbestaetigung** (= Empfangsbekenntnis des Gerichts).
- Bewahren Sie diese auf — sie ist Ihr Beweis für rechtzeitigen Eingang.

### Schritt 8 — Bestaetigung lesen

Pruefen Sie:

- Datum und Uhrzeit des Eingangs.
- Aktenzeichen (kommt spaeter).
- Bei Fehler: Korrektur.

## Worauf Sie besonders achten muessen

- **Niveau "hoch" der BundID** ist Pflicht für rechtssichere Einreichung.
- **Eingangsbestaetigung speichern**: Beweis für Fristwahrung.
- **Datum und Uhrzeit zaehlen**: Eingang vor 24:00 Uhr des letzten Frist-Tags reicht.
- **Kein Anwaltszwang elektronisch**: § 130d ZPO verpflichtet Anwaelte — nicht Buerger. Sie duerfen weiterhin Papier verwenden.
- **Anzeigen pruefen**: Manche Gerichte beantragen Korrektur, wenn Datei-Form falsch.

## Typische Fehler

- "Ich nutze einfache BundID-Stufe (Benutzername)." → Reicht **nicht** für rechtssichere Einreichung; Niveau "hoch" benoetigt.
- "Ich schicke einen Scan." → Scan ist okay, aber PDF/A bevorzugt; Lesbarkeit pruefen.
- "Email reicht doch auch." → Klassische Email ohne Signatur ist **kein** sicherer Uebermittlungsweg. Nicht fristwahrend!

## Querverweise

- `einreichung-130a-zpo-elektronisch-buerger` — Allgemeine elektronische Einreichung.
- `einreichung-papierform-mit-abschriften` — Papierform.
- `zurechnungsproblem-versand-durch-dritte` — Risiko bei Dritten.
- `fristen-berechnen-187-188-bgb` — Frist beachten.

## Quellen und Aktualitaet

Stand: 05/2026. MJP seit 01/2024 im Buerger-Betrieb. § 130a ZPO unveraendert.

## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.

## Normen und Rechtsprechung

### Kuratierte Normen-Bibliothek

- § 23 GVG
- § 114 FamFG
- § 156 StGB
- § 185 GVG
- § 41 GKG
- § 12 GKG
- § 7 StVG
- § 17 GKG
- § 48 GKG
- § 71 GVG
- § 23a GVG
- § 63 GKG

### Leitentscheidungen

- BGH VI ZR 67/15

