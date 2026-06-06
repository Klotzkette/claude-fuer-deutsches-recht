---
name: registereintrag-finalcheck-registerfuehrende
description: "Prüft vor Freigabe Vollständigkeit, Richtigkeit, Aktualitaet, Irreführungsfreiheit, Quellenstand und Plausibilitaet aller Pflichtangaben. Output Finalcheck-Protokoll im Lobbyregister Bundestag: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Arbeitsschritt."
---

# Registereintrag Finalcheck

## Arbeitsbereich

Prüft vor Freigabe Vollständigkeit, Richtigkeit, Aktualitaet, Irreführungsfreiheit, Quellenstand und Plausibilitaet aller Pflichtangaben. Output Finalcheck-Protokoll. Die Prüfung konzentriert sich auf dieses Prüfungslinie und trennt Rolle, Frist, Zuständigkeit, Beweislast und gewünschten Output.

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: § 3 LobbyRG Eintragung vor erster Interessenvertretung, § 5 LobbyRG jährliche Aktualisierung, Berichtspflicht ggf. innerhalb 3 Monaten nach Ende des Geschäftsjahres.
- Tragende Normen verifizieren: LobbyRG §§ 1, 2, 3, 5, 6, 7, 8 (i.d.F. Reform 2024), Verhaltenskodex Lobbyregister, GOBT, BGleiG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Interessenvertreter, Bundestagsverwaltung (Lobbyregisterstelle), Geschäftsstelle, registrierte Verbände, Bundesregierung (zweiter Registerteil).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Lobbyregistereintrag, Verhaltenskodex-Bestätigung, Tätigkeitsbericht, Hausausweisantrag, Finanzangaben, Verbandsmitgliederliste — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Einsatz

Den Eintrag vor Absendung wie eine Compliance-Akte gegenlesen.

## Gefuehrter Ablauf

1. Sachverhalt in einem Satz zusammenfassen: Wer will mit wem worueber sprechen oder hat bereits gehandelt?
2. Offizielle Quelle und Rechtsstand nennen: LobbyRG, Lobbyregister-FAQ, Handbuch oder Verhaltenskodex.
3. Die folgenden Leitfragen nacheinander stellen und fehlende Angaben als offene Punkte markieren.
4. Ergebnis nicht als Rechtsrat ausgeben, sondern als prueffaehige Arbeitsunterlage mit Annahmen, Belegen und naechster Portalaktion.

## Leitfragen

1. Sind alle Pflichtfelder belegt?
2. Passen Personen, VZAE, Kosten, Auftraggeber und Vorhaben zusammen?
3. Sind Risiken, Annahmen und Nachreichpflichten markiert?

## Quellenanker

## Doppelregistrierungs-Check

Vor Freigabe muss geprueft werden, ob mehrere Registerentwuerfe dieselbe juristische Person, dieselben betrauten Personen, dieselben Finanzaufwendungen oder dieselben Regelungsvorhaben doppelt abbilden. Bei Doppelungen: einen Streitvermerk erstellen, Primaerentwurf markieren und eine Anfrage an die registerfuehrende Stelle vorbereiten.

## API- und Export-Nachkontrolle

Der Finalcheck hat zwei Zeitpunkte:

1. **Vor Portalabgabe:** Interne Daten mit `assets/templates/registerdaten-json-mapping.md` JSON-nah auf das oeffentliche Schema mappen. Das Mapping ist nur QA, keine Einreichung.
2. **Nach Veroeffentlichung:** Oeffentlichen Registereintrag per API V2 oder JSON-Download abrufen und mit `assets/templates/registerexport-diff.md` gegen die Freigabeakte pruefen.

Im Nachcheck mindestens pruefen: Registernummer, Version, Gesetzeslage, Aktivstatus, Name/Rechtstraeger, Adresse, Niederlassungen, betraute Personen, VZAE, Taetigkeitsbeschreibung, Interessenbereiche, Regelungsvorhaben, Stellungnahmen, Auftraggeber, Unterauftragnehmer, Finanzaufwendungen, Zuwendungen, Schenkungen, Berichte, Verhaltenskodex, verweigerte Angaben, verspaetete Aktualisierung und Kodexverstoesse.

- LobbyRG: https://www.gesetze-im-internet.de/lobbyrg/BJNR081800021.html
- Lobbyregister FAQ: https://www.lobbyregister.bundestag.de/informationen-und-hilfe/informationen-fuer-interessenvertreter-863572
- Handbuch: https://www.lobbyregister.bundestag.de/informationen-und-hilfe/handbuch
- Leitplanken: ../../references/lobbyregister-leitplanken.md
- Open Data/API: ../../references/open-data-api-v2.md

## Output

Finalcheck-Protokoll mit Gruen/Orange/Rot, Korrekturliste, Freigabeempfehlung, API-Nachkontrollplan und Registerexport-Diff.

## Qualitaetsgate

- Pflichtgrund, Ausnahme und freiwillige Registrierung werden getrennt.
- Jede Frist bekommt Triggerdatum, Verantwortliche und Wiedervorlage.
- Jede Portalangabe bekommt Quelle, Freigabe und offenen Pruefpunkt.
- Unsichere Rechts- oder Tatsachenfragen werden nicht geglaettet, sondern sichtbar markiert.
- Jede API-Abweichung wird als rechtlich relevant, technisch relevant oder Anzeige-/Schemaeffekt klassifiziert.

## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.
