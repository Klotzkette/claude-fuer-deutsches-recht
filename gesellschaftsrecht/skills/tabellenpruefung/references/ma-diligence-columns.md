# M&A Due Diligence — Standard-Spaltensatz

Das Standardschema für eine käuferseitige Zielgesellschafts-Vertragsanalyse. Beginnen Sie hier und ergänzen oder streichen Sie Spalten je nach Transaktion. Dies ist ein Ausgangspunkt, keine Checkliste — die Garantien im Kaufvertrag und die Anforderungsliste bestimmen, was tatsächlich relevant ist.

```yaml
schema:
  name: "M&A Due Diligence — Standard"
  columns:
    - id: vertragspartner
      label: "Vertragspartner"
      type: verbatim
      prompt: "Nennen Sie die Vertragspartei außer der Zielgesellschaft, genau wie sie erscheint."

    - id: vertragstyp
      label: "Vertragstyp"
      type: classify
      options: [rahmenvertrag, kaufauftrag, lizenz_eingehend, lizenz_ausgehend, mietvertrag, dienstleistung, lieferung, vertrieb, nda, gemeinschaftsunternehmen, darlehen, buergschaft, arbeitsvertrag, sonstige]
      prompt: "Um welche Art von Vertrag handelt es sich?"

    - id: wirksamkeitsdatum
      label: "Wirksamkeitsdatum"
      type: date
      prompt: "Wann ist dieser Vertrag wirksam geworden?"

    - id: laufzeit
      label: "Laufzeit"
      type: duration
      prompt: "Was ist die anfängliche Vertragslaufzeit?"

    - id: automatische_verlaengerung
      label: "Automatische Verlängerung"
      type: classify
      options: [keine, jaehrlich, feste_periode, unbefristet]
      prompt: "Verlängert sich der Vertrag automatisch? In welchem Turnus?"

    - id: kuendigung_ohne_grund
      label: "Kündigung ohne wichtigen Grund"
      type: classify
      options: [keine, beide_parteien, nur_zielgesellschaft, nur_vertragspartner]
      prompt: "Kann eine Partei ohne Grund kündigen? Wer?"

    - id: kuendigungsfrist
      label: "Kündigungsfrist"
      type: duration
      prompt: "Welche Frist ist für eine Kündigung einzuhalten?"

    - id: kontrollwechsel
      label: "Kontrollwechsel (Change of Control)"
      type: classify
      options: [keine_regelung, zustimmung_erforderlich, zustimmung_nicht_unbillig_verweigert, automatische_beendigung, nur_anzeige, kuendigungsrecht_vertragspartner]
      prompt: "Regelt der Vertrag einen Kontrollwechsel bei der Zielgesellschaft? Was löst er aus und welche Folge hat er?"

    - id: abtretung
      label: "Abtretung / Vertragsübernahme"
      type: classify
      options: [keine_regelung, zustimmung_erforderlich, zustimmung_nicht_unbillig_verweigert, frei_abtretbar, abtretbar_an_verbundene_unternehmen, nicht_abtretbar]
      prompt: "Kann die Zielgesellschaft diesen Vertrag abtreten? Welche Beschränkungen gelten?"

    - id: exklusivitaet
      label: "Exklusivität / Wettbewerbsverbot"
      type: classify
      options: [keine, exklusiver_lieferant, exklusiver_abnehmer, wettbewerbsverbot, abwerbeverbot, gebietsschutz, meistbeguenstigungsklausel]
      prompt: "Schränkt der Vertrag eine Partei darin ein, mit anderen zu konkurrieren oder Verträge abzuschließen?"

    - id: haftungshoechstbetrag
      label: "Haftungshöchstbetrag"
      type: currency
      prompt: "Ist die Haftung begrenzt? Wie lautet der Betrag oder der Multiplikator?"

    - id: freistellung
      label: "Freistellung (Indemnification)"
      type: classify
      options: [keine, gegenseitig, zielgesellschaft_stellt_frei, vertragspartner_stellt_frei, nur_schutzrechte, nur_drittansprueche]
      prompt: "Wer stellt wen frei, und wofür?"

    - id: anwendbares_recht
      label: "Anwendbares Recht"
      type: verbatim
      prompt: "Welches Recht ist anwendbar?"

    - id: streitbeilegung
      label: "Streitbeilegung"
      type: classify
      options: [ordentliche_gerichte, schiedsverfahren_bindend, schiedsverfahren_nicht_bindend, schlichtung_vorgeschaltet, keine_regelung]
      prompt: "Wie werden Streitigkeiten beigelegt?"

    - id: meistbeguenstigung
      label: "Meistbegünstigung / Preisschutz"
      type: classify
      options: [keine, meistbeguenstigung, preisanpassung, benchmarking_recht]
      prompt: "Gibt es eine Meistbegünstigungs- oder Preisschutzklausel?"

    - id: mindestabnahme
      label: "Mindestabnahme / Volumenverpflichtung"
      type: currency
      prompt: "Gibt es Mindestabnahme-, Volumen- oder Ausgabenverpflichtungen?"

    - id: schutzrechte_eigentum
      label: "Schutzrechte-Eigentum"
      type: classify
      options: [jede_partei_eigene, zielgesellschaft_eignet_arbeitsergebnis, vertragspartner_eignet_arbeitsergebnis, gemeinschaftlich, nur_lizenz, keine_regelung]
      prompt: "Wem gehören die im Rahmen des Vertrags geschaffenen oder genutzten Schutzrechte?"

    - id: vertraulichkeit_nachvertragliche_dauer
      label: "Nachvertragliche Vertraulichkeit"
      type: duration
      prompt: "Wie lange gelten Vertraulichkeitspflichten nach Vertragsende fort?"

    - id: versicherungspflichten
      label: "Versicherungspflichten"
      type: classify
      options: [keine, haftpflicht, berufshaftpflicht, cyber, berufsunfaehigkeit, dachpolice]
      prompt: "Welche Versicherungen müssen unterhalten werden?"

    - id: pruefsrechte
      label: "Prüfrechte"
      type: classify
      options: [keine, vertragspartner_prueft_zielgesellschaft, zielgesellschaft_prueft_vertragspartner, gegenseitig]
      prompt: "Hat eine Partei Prüfrechte?"

    - id: benachrichtigungen
      label: "Zustellungsanforderungen"
      type: verbatim
      prompt: "Was ist die Zustellungsadresse und -methode für die Zielgesellschaft?"
```

## Häufige Ergänzungen nach Transaktionstyp

- **Tech- / IP-schwerpunktmäßige Ziele:** Quellcode-Hinterlegung (§ 69a ff. UrhG), Open-Source-Beschränkungen, Datenrechte, Trainingsrechte für Modelle, API-Zugang
- **Healthcare / Life Sciences:** AVV-Vorhandensein (Art. 28 DSGVO), Meldepflichten gegenüber Behörden, Behördenkorrespondenz (BfArM/PEI), klinische Studienpflichten
- **Öffentliche Auftraggeber:** Zustimmungserfordernisse zur Vertragsübernahme, Weitergabeklauseln, Sicherheitsüberprüfung, Verweise auf VOB/A, VgV
- **Immobilien:** Verlängerungsoptionen, Mietanpassungsklauseln, Nebenkostenregelungen, Vorrangs- und Bestätigungserfordernisse
- **Reguliertes Finanzwesen:** Genehmigungsvorbehalte (BaFin), Kapitalanforderungen (CRR/CRD), Meldepflichten (WpHG, MiFIR)

## Häufige Kürzungen für einen schnellen Erstdurchlauf

Für einen zeitkritischen ersten Überblick beantworten diese 6 Spalten 80 % der frühen Transaktionsfragen: vertragspartner, wirksamkeitsdatum, laufzeit, kontrollwechsel, abtretung, kündigung_ohne_grund. Diese zuerst durchführen und das Schema erweitern, sobald das Deal-Team Prioritäten gesetzt hat.
