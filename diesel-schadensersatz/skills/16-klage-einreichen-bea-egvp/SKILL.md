---
name: 16-klage-einreichen-bea-egvp
description: "Nur für die tatsächliche beA- oder EGVP-Einreichung eines durch Skill 21 freigegebenen Pakets. Prüft Empfänger, Signaturweg, persönliche Übermittlung und gerichtlichen Eingang. Ohne grünes Paket zurück zu Skill 21."
---

# Klage einreichen über beA und EGVP

## Zweck und Anwendungsfall

Dieser Skill übernimmt ausschließlich von Skill `21-bea-versandfertig-schriftsatz-anlagen` ein freigegebenes Paket und reicht es tatsächlich ein (§ 130d ZPO). Er prüft Empfänger, Signaturweg, Dateiliste und gerichtlichen Eingang und eröffnet die Vorschuss-/Zustellspur. Er läuft nur in einem Host mit privilegiert injiziertem beA-/EGVP-Connector; Standalone-CLI und Freitext versenden nie. Zugangsdaten, Karten, PIN und persönliche Authentisierung werden weder erfragt noch gespeichert.

`EINGEREICHT` setzt den unveränderten Connector-Originalbeleg und eine gültig signierte, daran hashgebundene Connector-Attestierung voraus. Eine lokale Receipt-Datei oder ein Übermittlungsprotokoll allein beweist keinen Gerichtseingang.

## Bedienmodus

Arbeite ergebnisorientiert für Diesel-Geschädigte und ihre Berater. Liefere Fachprodukt, knappe Ampel- und Lückenbewertung und genau einen nächsten Schritt. Tabellen nur bei mindestens drei vergleichbaren Werten oder wiederkehrenden Feldern; sonst vollständige Sätze. Schwierige Rechts- oder RDG-Punkte gehen an eine Rechtsanwältin oder einen Rechtsanwalt und bleiben ohne anwaltliche Verantwortung ungeklärt.

## Erste Antwort

Die erste Antwort nennt sofort Übergabegate, Fingerprint, Freigabe, Frist und verantwortende Person und liefert einen ausformulierten Einreichungsvermerk mit `NICHT_EINGEREICHT`. Bekannte Angaben einsetzen; nur Gericht/Aktenzeichen, Verantwortung, Signaturweg und Eingangsbeleg als konkrete Lücken führen. Nie in der ersten Antwort senden. Höchstens drei echte Rückfragen; keine Theorie-, Menü- oder Werkzeugvorträge. Manueller Abgleich darf ein ausgefallenes Hilfsskript ersetzen, nie einen fehlenden Nachweis.

## Schnelllauf und Übergabe

Verbindlich ist [Promptketten-Schnelllauf](../../references/promptketten-schnelllauf.md). Direkt mit dem referenziell geschlossenen, hashgebundenen `model_state` des kanonischen Heads starten; ausgelassene IDs nur über hostseitiges `retrieve_state_items` gegen denselben Head nachladen. Erledigtes nicht neu herleiten.

Höchstens zwei unabhängige Vorprüfungen parallel; Tabellen erst ab drei Vergleichswerten. Übergabe nur als belegtes Delta mit genau einem nächsten Skill. Fach-, Frist-, Freigabe-, Claim- und Versandgates sowie die Trennung 21/16 bleiben bestehen.

## Eingaben

- Kanonischer V2-Head mit freigegebenem Paket, aktueller Revision, `recipient_id`, stabiler `connector_namespace` (`provider:environment:tenant`) und deterministischer `action_id` aus Skill 21.
- `versand/`, Manifest, Fingerprint, hashgebundene Freigabe, Anlagenverzeichnis, SHA-256-Liste und Prüfbericht ohne Fehler/Warnung; Klagewegvermerk aus Skill 13.
- Strukturierte Host-Freigabe `confirm_submit`, verantwortende Person und Signaturweg: qES oder einfache Signatur plus persönliche sichere Übermittlung derselben Person.
- Privilegiert injizierter Connector derselben Namensdomäne sowie getrennt injizierter Vertrauensanker für Connector-Attestierungen.

## Ablauf / Checkliste

1. **Kanonisches Gate:** Head-Hash, Revision, verifizierten Skill-21-Lauf, `VERSANDFERTIG`, Fingerprint, Pakethash, Freigabe, Gericht, Rolle, Frist und Verantwortung abgleichen. Abweichung oder terminaler/fremder Head → Skill 21 beziehungsweise Stopp.
2. **Action binden:** `confirm_submit`, Paket, Empfänger, `connector_namespace` und `action_id` exakt vergleichen. Namespace des injizierten Dispatchers muss identisch sein. Claim einmalig `reserved` anlegen; anderer Worker sendet nicht. Head bleibt bis Abschluss/Stornierung eingefroren.
3. **ERV live prüfen:** §§ 130a, 130d ZPO, ERVV, aktuelle ERVB und gerichtliche Hinweise am Versandtag; derzeit höchstens 1.000 Dateien/200 MB, PDFs ohne Scripts/eingebettete Objekte.
4. **Nachricht und Dateien:** richtigen Gerichtsempfänger, Art, Betreff, Aktenzeichen/Neueingang und Parteien wählen; alle und nur Manifest-Dateien aus `versand/` in Reihenfolge anhängen. Namen, Anzahl, Größe, Einzelhashes und Fingerprint abgleichen.
5. **Signatur:** qES oder einfache Signatur plus persönliche sichere Übermittlung derselben Person. Kanalname genügt nicht (`VIa ZR 1559/22`); qES-Nachweis oder VHN mit Nachricht und Schriftsatz sichern. `VIa ZR 946/22` betrifft nur den isolierten Sperrabfrage-Standardhinweis bei sonst nachgewiesener qES.
6. **Ausführen:** Claim kurz auf `executing` setzen, dann erst nach letzter Anzeige von Empfänger, Aktenzeichen, Dateiliste und Signaturstatus dieselbe Action-ID idempotent an den privilegierten Connector geben. Automatisierung ersetzt keine persönliche Freigabe/Übermittlung.
7. **Eingang beweisen:** Connector-Originalbeleg unverändert hashen. Automatisierte Eingangsbestätigung auf Erfolg, Empfänger, Zeitpunkt und alle Dateien prüfen. Zusätzlich signierte Attestierung verlangen: `schema_version,status,action_type,action_id,package_sha256,recipient_id,submitted_at,issuer,audience,key_id,connector_namespace,source_receipt_sha256,attestation_signature`. Nur der injizierte Vertrauensanker prüft die Signatur; lokale JSON-Datei allein → `EINGANG_UNGEKLAERT`.
8. **Absturz versöhnen:** dieselbe Action-ID beim selben Namespace abfragen. `submitted` mit Originalbeleg/Attestierung abschließen; `unknown` blockiert. Nur die autoritative Bestätigung, dass die Action-ID beim Connector nicht existiert, erlaubt nach erneuter Claim- und Head-Prüfung denselben idempotenten Versuch. Nie eine neue Action-ID in Skill 16 erfinden.
9. **Störung:** Fehlversuche, Meldungen, Zeitstempel und amtliche Störungsinformation sichern. Ersatzeinreichung nach § 130d Satz 2/3 ZPO nur anwaltlich und mit rechtzeitiger Glaubhaftmachung; Claim-Ausgang nicht durch lokale Stornierung umdeuten.
10. **Folgen:** Vorschuss (§ 12 GKG), Rückwirkung (§ 167 ZPO), Aktenzeichen, Zustellung und Fristen überwachen; Erwiderung → Skill 17, neue Replik anschließend → Skill 21.

## Juristische Schreib- und Argumentationsnorm
<!-- BEGIN juristische-argumentation (autogen) -->
**Intention:** Die freigegebene juristische Endfassung unverändert, formwirksam und mit kontrollierter Eingangsbestätigung einreichen.
**Argumentationskern:** Entscheidungssatz zum Tatbestandsmerkmal; Akten-Tatsache, Vortrag, Indiz und Hypothese trennen; Beleg und Fundstelle sowie Beweisangebot zuordnen; Subsumtion und stärkstes Gegenargument ausformulieren; mit Ergebnis, Lücke und nächstem Schritt schließen.
**Freigabegate:** Materieller Inhalt, Signaturweg, Absenderidentität, Empfänger, Frist und gerichtlicher Eingang sind getrennt bestätigt.
**Arbeitsnorm:** [juristische-schreib-und-argumentationsarchitektur.md](../../references/juristische-schreib-und-argumentationsarchitektur.md)
<!-- END juristische-argumentation (autogen) -->

## Rechtsprechungs-Anker

<!-- BEGIN rechtsprechungs-anker (autogen) -->

Aktiver Satz mit höchstens sechs Ankern. Die vollständige Zuordnung bleibt in `references/gepruefte-anker-dieselgate.md` und im Fünfjahreskorpus; vor externer Verwendung Volltext, Status, Randnummer und Folgeentwicklung live prüfen.

| Anker | Aussage für diesen Skill | Status |
| --- | --- | --- |
| Keine Dieselgate-Leitentscheidung einschlägig | Für den elektronischen Versand tragen §§ 130a, 130d ZPO, ERVV, aktuelle ERVB, Signatur- und Versandweg sowie die kontrollierte gerichtliche Eingangsbestätigung. | Hinweis |
| BGH, Urt. v. 14.07.2026 - VIa ZR 946/22 | Der isolierte Standardhinweis auf eine unterbliebene Trustcenter-Sperrabfrage ist ohne konkretes Sperrindiz kein festgestellter qES-Fehler; Dateien, Prüfbericht und Eingang trotzdem vollständig sichern. | Amtlich geprüft |
| BGH, Urt. v. 18.06.2026 - VIa ZR 1559/22 | Die bloße Kanalangabe beA/EGVP beweist keine formgerechte Einreichung; entweder qES oder einfache Signatur plus persönliche sichere Übermittlung und VHN vollständig nachweisen. | Amtlich geprüft |

<!-- END rechtsprechungs-anker (autogen) -->

## Arbeitsmaterial

### Formulierungsbausteine

Baustein Einreichungsvermerk (nach positiv kontrolliertem Originalbeleg und gültiger Connector-Attestierung):

„1 Einreichung

In Sachen [Name der Klägerin] gegen [Name des Herstellers] wurde die Klage am [Datum TT.MM.JJJJ] um [Uhrzeit] Uhr durch [verantwortende Person] persönlich aus deren beA-Postfach an das [Gericht] übermittelt. Übermittelt wurden die im Paketmanifest gebundenen [Anzahl] Dateien in dokumentierter Reihenfolge; Namen, Anzahl, Gesamtgröße und Paket-Fingerprint stimmen mit der Freigabe aus Skill 21 überein.

2 Signaturweg

Der Schriftsatz trägt [die qualifizierte elektronische Signatur der verantwortenden Person / die einfache Signatur der verantwortenden Person am Textende und wurde von ihr persönlich auf sicherem Übermittlungsweg versandt]. Der Nachweis ([qES-Prüfbericht / Transfervermerk mit VHN]) ist zusammen mit Nachricht und Schriftsatz archiviert.

3 Gerichtseingang

Die automatisierte gerichtliche Eingangsbestätigung vom [Datum TT.MM.JJJJ], [Uhrzeit] Uhr weist Erfolg, richtigen Empfänger und alle [Anzahl] Dateinamen aus. Ihr unveränderter Hash ist durch die geprüfte Connector-Attestierung zur Action-ID [Action-ID] gebunden. Status: EINGEREICHT. Die Vorschuss- und Zustellspur wird fortgeschrieben."

Baustein Störungsvermerk (Ersatzeinreichung):

„Am [Datum TT.MM.JJJJ] war die Übermittlung aus dem beA von [Uhrzeit] bis [Uhrzeit] Uhr aus technischen Gründen vorübergehend unmöglich. Gesichert sind Fehlermeldungen mit Zeitstempel, Bildschirmfotos der Versuche um [Uhrzeit] und [Uhrzeit] Uhr sowie die amtliche Störungsinformation vom [Datum TT.MM.JJJJ]. Nach anwaltlicher Entscheidung wurde die Klage nach § 130d Satz 2 ZPO ersatzweise nach den allgemeinen Vorschriften eingereicht; die vorübergehende Unmöglichkeit wurde mit der Ersatzeinreichung glaubhaft gemacht (§ 130d Satz 3 ZPO). Das elektronische Dokument wird auf gerichtliche Anforderung unverzüglich nachgereicht."

### Entscheidungstabelle Einreichung über beA und EGVP

| Wenn (Befund) | Dann (Pfad) | Begründung | Nächster Schritt |
| --- | --- | --- | --- |
| Rechtsanwältin oder Rechtsanwalt reicht ein | Nur elektronisch über das persönliche beA | Aktive Nutzungspflicht nach § 130d ZPO; Papier oder Fax wäre formunwirksam | Signaturweg festlegen |
| Schriftsatz trägt qES der verantwortenden Person | Versand darf auch durch eine andere Person ausgelöst werden | Die qES ersetzt die persönliche Versendung; Prüfvermerk sichern | Dateiabgleich, dann Versand |
| Nur einfache Signatur am Textende | Persönliche Versendung durch dieselbe verantwortende Person zwingend | Sicherer Übermittlungsweg wirkt nur bei Identität von Signatur und Versender; `VIa ZR 1559/22` verlangt den vollständigen Nachweis | VHN nach Versand kontrollieren |
| Datei kein zugelassenes PDF oder mit Scripts/eingebetteten Objekten | Nicht anhängen, Paket zurückgeben | ERVV und aktuelle ERVB bestimmen die zulässigen Formate | Rückroute zu Skill 21 |
| Paket über 200 MB oder mehr als 1.000 Dateien | Aufteilen oder Nachreichung planen | Aktuelle ERVB-Grenzen am Versandtag prüfen | ERV-Check wiederholen |
| Originalbeleg fehlt, weist Dateien nicht aus oder Attestierung ist ungültig | `EINGANG_UNGEKLAERT`, sofortige Nachkontrolle | Protokoll oder lokales JSON ersetzt die signierte Connector-Beweiskette nicht | Anwaltliche Eskalation |
| beA-Störung am Fristtag | Störung dokumentieren, Ersatzeinreichung nur nach anwaltlicher Entscheidung | § 130d Satz 2 und 3 ZPO mit rechtzeitiger Glaubhaftmachung | Störungsvermerk-Baustein |

## Quellenpflicht

Es gelten `references/zitierweise.md`, `references/bea-versandfertig.md` und der Verfahrensstand in `references/rechtsstand-2026-gesetzgebung.md`. ERV-Aussagen mit Normanker (§§ 130a, 130d ZPO; §§ 2, 5 ERVV; aktuelle ERVB); technische Vorgaben der Justiz am Versandtag live prüfen. Keine erfundenen Aktenzeichen oder Versandbestätigungen.

## Ausgabeformat

1. **Kontrollansicht**

   Stelle dem Arbeitsprodukt den kompakten `Kanzlei-Arbeitskopf` mit Status, Ampelgrund, Frist, Quellenstand, Arbeitsprodukt und genau einem `Nächsten Schritt` voran. Er ist eine Kontroll- und Begleitansicht und nie Bestandteil eines Schriftsatzes, einer Anlage oder einer Exportdatei.

2. **Fachprodukt**

   Einreichungsvermerk mit Empfänger, Aktenzeichen/Neueingang, Verantwortung, Signaturweg, bestätigter Dateiliste, Versandzeitpunkt, Eingangsstatus, Originalbeleg-/Attestierungsreferenzen, Vorschuss und Zustellung. `EINGEREICHT` nur nach positiv kontrolliertem Originalbeleg und gültiger Connector-Attestierung. Vor Versand `NICHT_EINGEREICHT`; nach Versuch ohne diese Beweiskette `EINGANG_UNGEKLAERT`.

## Beispiele

- Eingang: Klage mit neun Anlagen, Skill-21-Bericht grün. Erste Antwort: Gate-Befund und vollständiger Vermerk mit Dateiliste; Versandzeitpunkt und Eingang bleiben offen. Erst Originalbeleg mit allen zehn Dateien plus gültige, hashgebundene Connector-Attestierung setzen `EINGEREICHT` und eröffnen die Vorschussspur.
- Eingang: beA-Störung am Fristtag, 17:40 Uhr. Kernbefund: Übermittlung vorübergehend unmöglich. Erste Antwort: vorläufiger, aber vollständig ausformulierter Störungsvermerk mit vorhandenen Zeitstempeln; als konkrete Lücken werden weiterer Störungsverlauf und Belegdateien geführt. Ersatzeinreichung nach § 130d Satz 2 ZPO nur nach anwaltlicher Entscheidung.
- Eingang: Übermittlungsprotokoll liegt vor, gerichtliche Eingangsbestätigung fehlt. Kernbefund: Eingang nicht belegt. Erste Antwort: Vermerk mit Status `EINGANG_UNGEKLAERT`, sofortige Nachkontrolle und anwaltliche Eskalation als einziger nächster Schritt.
- Eingang: beA-Kanal protokolliert, aber weder qES noch VHN nachweisbar. Kernbefund: Formnachweis fehlt (`VIa ZR 1559/22`). Erste Antwort: Gate-Tabelle mit roter Signaturzeile, Status `NICHT_EINGEREICHT` beziehungsweise nach Versuch `EINGANG_UNGEKLAERT` und sofortige anwaltliche Behandlung des Form- und Fristnotfalls.
