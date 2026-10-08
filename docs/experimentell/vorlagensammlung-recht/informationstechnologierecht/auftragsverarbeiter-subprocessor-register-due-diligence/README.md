# Auftragsverarbeiter- und Subprocessor-Register für Datenschutz-Due-Diligence

Registervorlage zur Prüfung der Dienstleisterkette einer Zielgesellschaft.

## Download
- [⬇ Auftragsverarbeiter- und Subprocessor-Register – ODT herunterladen](https://github.com/Klotzkette/claude-fuer-deutsches-recht/raw/main/docs/experimentell/vorlagensammlung-recht/informationstechnologierecht/auftragsverarbeiter-subprocessor-register-due-diligence/auftragsverarbeiter-subprocessor-register-due-diligence.odt) — Offene Bürofassung (OpenDocument)
- [⬇ Auftragsverarbeiter- und Subprocessor-Register – Markdown (ZIP) herunterladen](https://github.com/Klotzkette/claude-fuer-deutsches-recht/raw/main/docs/experimentell/vorlagensammlung-recht/informationstechnologierecht/auftragsverarbeiter-subprocessor-register-due-diligence/auftragsverarbeiter-subprocessor-register-due-diligence.md.zip) — Bearbeitbare Markdown-Fassung, gepackt für direkten Download

Vorschau im Repository: [`auftragsverarbeiter-subprocessor-register-due-diligence.odt`](auftragsverarbeiter-subprocessor-register-due-diligence.odt) · [`auftragsverarbeiter-subprocessor-register-due-diligence.md`](auftragsverarbeiter-subprocessor-register-due-diligence.md)

## Vorspruch und Nutzungsgrenze

Diese Vorlage ist unverbindlich, ein experimenteller Text und keine Rechtsberatung. Sie ist ein Struktur- und Formulierungsvorschlag, kein Gutachten und kein ungeprüft verwendbares Mandatsprodukt. Nutzung nur auf eigene Gewähr und eigene Gefahr; vor jedem Einsatz sind Sachverhalt, Rechtslage, Form, Fristen, Zuständigkeit, Vertretungsmacht, Datenschutz, Vollziehbarkeit und wirtschaftliche Folgen fachkundig zu prüfen, anzupassen und freizugeben.

Mandatsbezogene und personenbezogene Inhalte sind nach § 43a Abs. 2 BRAO, § 203 StGB und DSGVO zu schützen. Bei Verarbeitung in Drittsystemen sind Anonymisierung, Rechtsgrundlage, Auftragsverarbeitung und Löschkonzept zu prüfen.

Lizenz: Apache-2.0 OR MIT.

## Anwendungsbereich

Die Vorlage passt, wenn in einer Due Diligence nicht nur gefragt wird, ob AVV existieren, sondern ob die reale Lieferantenkette, Unterauftragnehmer, Speicherorte, Supportzugriffe, Drittlandtransfers und Löschwege nachvollziehbar sind. Für den eigentlichen AVV siehe `informationstechnologierecht/auftragsverarbeitungsvertrag-dsgvo/`.

## Einschlägige Normen

- Art. 28 Abs. 1 bis Abs. 4 DSGVO für Auftragsverarbeiter, Vertragsinhalt und Unterauftragsverarbeiter.
- Art. 30 Abs. 2 DSGVO für das Verzeichnis des Auftragsverarbeiters.
- Art. 32 DSGVO für technische und organisatorische Maßnahmen.
- Art. 44 bis 49 DSGVO für Drittlandbezüge in der Lieferantenkette.
- Durchführungsbeschluss (EU) 2021/914 für SCC bei Drittlandübermittlung.

## Pflichtangaben

Benötigt werden Dienstleistername, Rolle, Leistung, Vertragsgrundlage, Datenkategorien, Betroffenengruppen, Systeme, Speicherorte, Unterauftragnehmer, Transferinstrument, TOM, Lösch- und Exit-Regelung sowie DD-Bewertung.

## Mustertext mit Platzhaltern

Die Vorlage enthält ein Registerblatt je Dienstleister und einen Abschnitt für Nachforderungen und kaufvertragliche Relevanz.

## Hinweise zur Verwendung

In Transaktionen scheitert die Datenschutzprüfung häufig nicht am fehlenden AVV, sondern an unklaren Subprocessor-Ketten. Ein AVV ohne aktuelle Unterauftragnehmerliste, Speicherort, Drittlandinstrument und Löschweg ist für die Risikobewertung nur begrenzt brauchbar.

Bei SaaS- und Cloud-Diensten muss zusätzlich geprüft werden, ob Supportzugriffe aus Drittländern möglich sind. Auch reine Fernzugriffe können Kapitel-V-DSGVO-Relevanz haben, wenn personenbezogene Daten für den Drittlandempfänger zugänglich werden.

## Taktische Hinweise

Vorgehensreihenfolge: Zuerst werden das Verzeichnis der Verarbeitungstätigkeiten und die Vertragsliste der Zielgesellschaft angefordert, denn das Register wird gegen diese Quellen aufgebaut und nicht aus dem Gedächtnis der IT-Abteilung. Danach werden die kritischen Dienstleister nach Ziffer 1.3 priorisiert (Produktbetrieb, Hosting, Beschäftigtendaten, Drittlandtransfer) und zuerst geprüft, weil dort die kaufpreisrelevanten Risiken liegen. Nachforderungen werden mit fester Frist nach Abschnitt 3 gestellt; erst nach deren Ablauf wird abschließend bewertet und die Rest-Grau-Quote offen ausgewiesen.

Typische Einwände der Zielgesellschaft oder des Verkäufers und Antwortlinien:

- „Die Subprocessor-Listen unserer Anbieter sind vertraulich." — Die Listen sind bei fast allen Cloud-Anbietern öffentlich oder über das Kundenportal abrufbar; wo nicht, genügt die Offenlegung im Datenraum unter der ohnehin bestehenden Vertraulichkeitsvereinbarung.
- „Der AVV ist der unveränderbare Standard des Anbieters, eine Prüfung bringt nichts." — Geprüft wird nicht die Verhandelbarkeit, sondern ob der Standard den Pflichtkatalog des Art. 28 Abs. 3 DSGVO abdeckt und ob die Zielgesellschaft die dort vorgesehenen Kontrollrechte je ausgeübt hat.
- „Konzerninterne Dienstleistungen brauchen keinen AVV." — Die DSGVO kennt kein Konzernprivileg; auch die Schwestergesellschaft als Auftragsverarbeiter braucht einen Vertrag nach Art. 28 DSGVO oder eine andere tragfähige Rollenzuordnung.
- „Der Anbieter ist zertifiziert, das genügt als Nachweis." — Zertifikate belegen das Managementsystem des Anbieters, ersetzen aber weder die aktuelle Unterauftragnehmerliste noch das Transferinstrument noch den Löschweg für genau diese Datenkategorien.

Erledigungs- und Einigungskorridor: Rote Befunde werden in Transaktionen selten zum Abbruchgrund, sondern regelmäßig in eine Kombination aus Closing Condition für die kritischsten Verträge, Freistellung für Altverstöße bis zum Stichtag und Post-Closing-Covenant mit Umsetzungsfrist von [Frist] übersetzt; gelbe Befunde wandern in einen Nachforderungskatalog mit Stichtagsbestätigung des Verkäufers.

Häufige Fehler:

- Es wird nur die Existenz eines AVV abgehakt, ohne Speicherorte, Supportstandorte und Unterauftragnehmerkette zu erfassen, sodass das Register die eigentliche Risikofrage nicht beantwortet.
- Fernzugriffe von Support-Teams aus Drittländern werden übersehen, weil nur nach dem Serverstandort gefragt wurde.
- Das Register wird nicht mit dem Verzeichnis nach Art. 30 DSGVO abgeglichen, sodass Dienstleister auftauchen, deren Verarbeitung nirgends dokumentiert ist — oder umgekehrt.
- Bewertungen werden ohne Nachweisdokument vergeben; ein „grün" auf Zuruf der IT-Abteilung ist in der Gewährleistungsverhandlung wertlos.
- Die Registerpflege endet mit dem Signing; ohne Aktualisierungstrigger nach Ziffer 4.2 ist das Register beim Closing bereits veraltet.

## Verwandte Vorlagen

- [Auftragsverarbeitungsvertrag (Art. 28 DSGVO; SDM)](../auftragsverarbeitungsvertrag-dsgvo/) — Der eigentliche AVV nach Art. 28 DSGVO, dessen Existenz und Inhalt dieses Register je Dienstleister prüft.
- [Anlage TOM zum Auftragsverarbeitungsvertrag](../avv-tom-anlage-dsgvo/) — TOM-Anlage, gegen die die Maßnahmenangaben der Dienstleisterkarte (Ziffer 2.10) abgeglichen werden.
- [Datenschutzrechtliche Due-Diligence-Anforderungsliste](../datenschutz-due-diligence-anforderungsliste/) — Anforderungsliste für den Datenraum, aus der die Unterlagen für dieses Register angefordert werden.
- [Datenschutz-Gap-Report für M&A-Due-Diligence](../datenschutz-gap-report-due-diligence/) — Gap-Report, in den die roten und gelben Registerbefunde als Findings überführt werden.
- [Verzeichnis der Verarbeitungstätigkeiten für Datenschutz-Due-Diligence](../verzeichnis-verarbeitungstaetigkeiten-due-diligence/) — Prüfung des Art.-30-Verzeichnisses, mit dem dieses Register abgeglichen wird.
