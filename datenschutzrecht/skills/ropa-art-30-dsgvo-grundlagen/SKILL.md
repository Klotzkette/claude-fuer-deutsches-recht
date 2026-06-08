---
name: ropa-art-30-dsgvo-grundlagen
description: "Grundlagen des Verzeichnisses von Verarbeitungstaetigkeiten nach Art. 30 DSGVO. Anwendungsbereich, Schwellenwert, Mindestinhalte Controller und Processor, Verhaeltnis zu § 70 BDSG, Vorlagepflicht gegenueber der Aufsichtsbehoerde. Einstiegs-Skill für das Records of Processing Activities (RoPA)."
---

# Verzeichnis von Verarbeitungstaetigkeiten – Art. 30 DSGVO Grundlagen

## Zweck

Dieser Skill ordnet das Verzeichnis von Verarbeitungstaetigkeiten (Records of Processing Activities, kurz RoPA) nach Art. 30 DSGVO ein. Er erklaert Pflichtige, Inhalte, Form und Verhaeltnis zu anderen Dokumentationspflichten (DSFA, AVV, RoPA), damit Kanzleien und Datenschutzbeauftragte das richtige Werkzeug für das richtige Dokument waehlen.

## Wann dieses Modul hilft

- Mandant fragt: "Brauchen wir ein Verarbeitungsverzeichnis?"
- Aufsichtsbehoerde verlangt nach Art. 30 Abs. 4 DSGVO Vorlage des Verzeichnisses.
- Audit eines bestehenden Verzeichnisses auf Vollstaendigkeit.
- Erstaufbau eines RoPA in einer Kanzlei, einem Unternehmen oder einer öffentlichen Stelle.
- Abgrenzung Controller-Verzeichnis (Art. 30 Abs. 1 DSGVO) vs. Processor-Verzeichnis (Art. 30 Abs. 2 DSGVO).

## Rechtlicher Rahmen

### Art. 30 Abs. 1 DSGVO – Verzeichnis des Verantwortlichen (Controller)

Pflichtinhalte:

1. Name und Kontaktdaten des Verantwortlichen, ggf. gemeinsam Verantwortlicher, Vertreter und Datenschutzbeauftragter.
2. Zwecke der Verarbeitung.
3. Beschreibung der Kategorien betroffener Personen und der Kategorien personenbezogener Daten.
4. Kategorien von Empfaengern, denen offengelegt wurde oder noch offengelegt wird.
5. Drittlandtransfer: Empfaengerland und Dokumentation geeigneter Garantien (Art. 46 Abs. 2 DSGVO).
6. Vorgesehene Loeschfristen für die verschiedenen Datenkategorien.
7. Allgemeine Beschreibung der technischen und organisatorischen Massnahmen (TOMs) gemaess Art. 32 Abs. 1 DSGVO.

### Art. 30 Abs. 2 DSGVO – Verzeichnis des Auftragsverarbeiters (Processor)

Pflichtinhalte:

1. Name und Kontaktdaten des Auftragsverarbeiters und jedes Verantwortlichen, für den er taetig ist, ggf. Vertreter und DSB.
2. Kategorien der im Auftrag jedes Verantwortlichen durchgefuehrten Verarbeitungen.
3. Drittlandtransfer: Empfaengerland und geeignete Garantien.
4. Allgemeine Beschreibung der TOMs (Art. 32 Abs. 1 DSGVO).

### Art. 30 Abs. 3 DSGVO – Schriftform

Schriftlich oder elektronisch. In der Praxis: Excel, Datenbank, RoPA-Software, Word-Dokument. Wichtig: aktuell halten, datierte Versionen.

### Art. 30 Abs. 4 DSGVO – Vorlagepflicht

Auf Anforderung der Aufsichtsbehoerde vorzulegen.

### Art. 30 Abs. 5 DSGVO – Ausnahme für KMU

Unternehmen oder Einrichtungen mit weniger als 250 Mitarbeitern sind grundsaetzlich befreit, **es sei denn**:

- die Verarbeitung birgt ein Risiko für Rechte und Freiheiten;
- die Verarbeitung erfolgt nicht nur gelegentlich;
- die Verarbeitung umfasst besondere Datenkategorien (Art. 9 DSGVO) oder Daten ueber strafrechtliche Verurteilungen (Art. 10 DSGVO).

In der Praxis: praktisch jede Kanzlei, jede Arztpraxis, jedes HR-System eines Mittelstaendlers erfuellt mindestens einen Ausnahmegrund. Die KMU-Ausnahme ist daher weitgehend Theorie.

### § 70 BDSG – RoPA für Bundesbehoerden

Fuer Bundesbehoerden im Anwendungsbereich der JI-Richtlinie (Polizei und Justiz) gilt § 70 BDSG mit eigenen Mindestinhalten.

## Ablauf / Checkliste

1. **Rollenklaerung:** Ist die Stelle Verantwortlicher, gemeinsam Verantwortlicher (Art. 26 DSGVO), Auftragsverarbeiter (Art. 28 DSGVO) oder mehreres zugleich?
2. **Pflichtenpruefung:** Greift Art. 30 Abs. 5 DSGVO oder ist Verzeichnis ohnehin Pflicht?
3. **Inventar:** Welche Verarbeitungstaetigkeiten gibt es? Faustregel: pro Geschaeftsprozess eine Zeile.
4. **Mindestinhalte erfassen:** je nach Rolle 7 (Controller) oder 4 (Processor) Felder.
5. **Drittlandtransfer:** separate Spalte; Verweis auf SCC, BCR, DPF, Angemessenheitsbeschluss.
6. **Loeschfristen:** konkrete Fristen, nicht "nach gesetzlichen Vorgaben".
7. **TOM-Referenz:** Verweis auf TOM-Konzept; nicht jede Massnahme im RoPA wiederholen.
8. **Versionierung:** Datierte Snapshots für Audit-Trail.
9. **Review-Zyklus:** jaehrlich oder bei wesentlicher Aenderung.

## Mustertext / Template

Tabellenkopf (Controller):

| Lfd. Nr. | Verarbeitungstaetigkeit | Zweck | Rechtsgrundlage | Kategorien Betroffene | Datenkategorien | Empfaengerkategorien | Drittland / Garantie | Loeschfrist | TOM-Verweis |
|---|---|---|---|---|---|---|---|---|---|

Tabellenkopf (Processor):

| Lfd. Nr. | Auftraggeber | Verarbeitungskategorie | Drittland / Garantie | TOM-Verweis |
|---|---|---|---|---|

Konkrete Vorlagen liefern die Skills:

- `ropa-art-30-controller-deutsch-vorlage`
- `ropa-art-30-processor-deutsch-vorlage`
- `ropa-en-controller-template`
- `ropa-en-processor-template`

## Typische Fehler

- KMU-Ausnahme bejaht, obwohl regelmäßige Personalverarbeitung erfolgt.
- TOM-Spalte mit "Verschluesselung" abgespeist – zu pauschal, Aufsichtsbehoerde fordert Konkretion.
- Drittlandtransfer nicht erfasst, obwohl SaaS in den USA gehostet wird.
- Empfaengerkategorien fehlen oder werden mit Einzelempfaengern verwechselt.
- Kein Versionsstand; bei Audit unklar, welcher Stand zum Pruefzeitpunkt galt.
- Loeschfristen pauschal "10 Jahre"; ohne Differenzierung nach Datenkategorie.
- Doppelte Pflege RoPA / DSFA / TOM-Konzept ohne Querverweise.

## Querverweise

- `dsfa-erstellung` für hochrisikobehaftete Verarbeitungen.
- `avv-art-28-dsgvo-grundtatbestand` für Processor-Vertraege.
- `drittlandstransfer-pruefung` für Art. 44 ff. DSGVO.
- `dsb-bestellungspflicht-pruefung` für DSB-Verantwortlichkeiten.

## Quellen Stand 06/2026

- VO (EU) 2016/679 (DSGVO), insbesondere Art. 30, Erwaegungsgrund 13, 82.
- BDSG, insbesondere § 70 für Bundesbehoerden.
- EDSA: Position Paper on Article 30(5) GDPR (vom 19.04.2018).
- Konferenz der unabhaengigen Datenschutzaufsichtsbehoerden des Bundes und der Länder (DSK): Kurzpapier Nr. 1 "Verzeichnis von Verarbeitungstaetigkeiten" (Stand 17.12.2018).

## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.
