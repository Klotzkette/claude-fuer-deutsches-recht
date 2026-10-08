---
name: angebotsoeffnung-formfehler-preisblatt
description: "Auftraggeberprüfung für Angebotsöffnung, Form und Preisblatt: sichert Frist, Integrität und Öffnungsprotokoll, trennt rettbare Unterlagenmängel von unzulässiger Angebotsänderung und erstellt eine belastbare Ausschlussentscheidung."
---

# Angebotsöffnung, Formfehler und Preisblatt prüfen

<!-- BEGIN output-format-block (autogen) -->

## Output-Format (verbindlich)

Schriftart Times New Roman, Schriftgrad 11 pt. Dezimalgliederung 1, 1.1, 1.1.1, 2, 2.1 fortlaufend ohne Lücken, maximal vier Ebenen. Aufzählungen mit Spiegelstrich oder Bullet. Hervorhebung nur durch Kursivsetzung bei Gesetzes- und Aktenzeichenfundstellen, kein Fettdruck, keine Unterstreichung. Vollständige Regeln in [`references/OUTPUT-FORMAT.md`](../../references/OUTPUT-FORMAT.md). Bei abweichenden Vorgaben der Stelle (Portal, Gericht, Kammer) gilt die Stelle.

<!-- END output-format-block (autogen) -->

## Öffnung zuerst sichern

1. Angebotsfrist, Serverzeit und Eingang jedes Angebots aus dem Portalprotokoll übernehmen. Vor Fristablauf darf nach § 55 Abs. 1 VgV niemand vom Inhalt Kenntnis nehmen.
2. Öffnung unverzüglich nach Fristablauf dokumentieren. § 55 Abs. 2 VgV verlangt grundsätzlich zwei Vertreter; bei elektronischen Angeboten entfällt dieses Vier-Augen-Prinzip nur, wenn deren dauerhafte Vollständigkeit und Unverändertheit technisch gesichert ist.
3. Für jedes Angebot Originaldatei, Hashwert, Eingangsquittung, Dateiname, Format, Signaturstatus und Öffnungszeit festhalten. Eine Arbeitskopie nie an die Stelle des Originals setzen.

## Prüfweiche je Auffälligkeit

| Befund | Rechtsfrage | Aktenbeleg | Nächster Schritt |
|---|---|---|---|
| verspäteter Eingang | § 57 Abs. 1 Nr. 1 VgV; hat der Bieter die Verspätung zu vertreten? | Portal- und Störungsprotokoll | Verantwortung feststellen, dann Ausschluss oder Zulassung begründen |
| Form oder Signatur abweichend | §§ 53, 57 Abs. 1 Nr. 1 VgV und konkrete Bekanntmachung | Formvorgabe, Datei, Prüfbericht | verlangte und tatsächlich eingehaltene Form vergleichen |
| Unterlage fehlt oder ist fehlerhaft | § 56 Abs. 2 bis 5 VgV | Unterlagenliste und Fundstelle | Nachforderungsentscheidung gesondert treffen |
| wertungsrelevante Leistungsangabe fehlt | § 56 Abs. 3 VgV | Kriterium, Angebotsstelle | grundsätzlich keine Nachforderung |
| unwesentlicher Einzelpreis fehlt | Ausnahme des § 56 Abs. 3 Satz 2 VgV | Preisblatt und Rechenprobe | nur retten, wenn Gesamtpreis, Rangfolge und Wettbewerb unberührt bleiben |
| Rechenfehler oder Preiswiderspruch | § 56 Abs. 1 VgV; Vergabeunterlagen | Originalpreisblatt und Formel | rechnerisch prüfen, keine neue Preisentscheidung zulassen |
| Nebenangebot | § 35 VgV und veröffentlichte Mindestanforderungen | Bekanntmachung und Nebenangebot | Zulässigkeit vor inhaltlicher Wertung prüfen |

Eine Aufklärung darf den bereits feststehenden Angebotsinhalt verständlich machen, aber weder Preis noch Leistung nach Fristablauf neu festlegen. Mischkalkulationsverdacht, Nullpreise und ungewöhnlich niedrige Gesamtpreise zusätzlich im Skill `ungewoehnlich-niedriges-angebot` prüfen.

## Ausschlussvermerk

Der Vermerk nennt Angebots-ID, konkreten Befund, veröffentlichte Vorgabe, einschlägige Norm, Originalfundstelle, mögliche Rettungsnorm, Gleichbehandlungsvergleich und Rechtsfolge. Vor Ausschluss dokumentieren, weshalb eine mildere Aufklärung oder Nachforderung unzulässig oder ungeeignet ist. Vergleichbare Fehler aller Angebote nach demselben Maßstab behandeln.

## Pflichtoutput

1. Öffnungsprotokoll mit Integritäts- und Zugriffsbelegen.
2. Angebotsmatrix mit den Spalten Frist, Form, Datei, Preisblatt, Nebenangebot, Nachforderung und Ergebnis.
3. Je Auffälligkeit ein freigabefähiger Zulassungs-, Nachforderungs- oder Ausschlussvermerk.
4. Liste fehlender Portal- oder Störungsnachweise und verantwortlicher Beschaffungsstelle.
5. Freigabeampel: `grün` nur bei reproduzierbarem Ergebnis; sonst `gelb` mit Nacharbeit oder `rot` mit Entscheidungsstopp.
