# Softwarepflege- und Supportvertrag (Maintenance; SLA)

---

Kurz-Hinweis: Diese Vorlage ist unverbindlich, ein experimenteller Text und keine Rechtsberatung. Nutzung nur auf eigene Gewähr, eigene Gefahr und ohne Gewähr. Die ausführlichen Hinweise zu § 43a Abs. 2 BRAO, § 203 StGB, DSGVO sowie Apache-2.0 OR MIT stehen in der README dieser Vorlage.

---

## Vorlage

[WARNHINWEIS — nicht Vertragsbestandteil, nicht mit unterzeichnen]

Diese Vorlage ersetzt nicht die anwaltliche Eigenleistung. Sie liefert das Gerüst, nicht den Fall. Der Anwender bringt den Sachverhalt, die Beweismittel, die taktische Entscheidung und die Verantwortung; die Vorlage bringt Struktur, Sprache und die unbedingt zu prüfenden Stellen. Wer nur Platzhalter füllt, ohne den eigenen Sachverhalt zu durchdenken, hat noch keinen Vertrag, sondern einen Entwurf.

Weitere Hinweise und ausführliche Praxis-Erläuterungen in der README dieser Vorlage.

### Vertragseingang und Bearbeitungsstand

Kundin ist [vollständige Firma, Rechtsform, Register, Sitz, Anschrift, Vertretung].

Pflegegeberin ist [vollständige Firma, Rechtsform, Register, Sitz, Anschrift, Vertretung].

Pflegegegenstand ist [Softwareprodukt, Version, Lizenzgrundlage, Installationsumgebung, produktive Mandanten, kritische Geschäftsprozesse].

Der Bearbeitungsstand ist [Entwurf / Verhandlung / Unterzeichnung / Vollzug], Datum: [Datum], Akte: [Az.].

### 1. Präambel / Gegenstand

1.1 Die Pflegegeberin übernimmt Pflege, Support und Störungsbeseitigung für die in Anlage 1 bezeichnete Softwareinstallation der Kundin. Der Vertrag betrifft den produktiven Betrieb der Software, nicht deren erstmalige Erstellung und nicht die Überlassung zusätzlicher Nutzungsrechte außerhalb der bestehenden Lizenzgrundlage.

1.2 Die Pflegeleistungen sichern die Nutzbarkeit der Software für die in Anlage 1 bezeichneten Kernprozesse. Geschuldet sind Störungsannahme, Fehleranalyse, qualifizierte Rückmeldung, Workaround, Fehlerkorrektur, sicherheitsrelevante Updates, Releaseinformationen, Fernwartung und geordneter Exit nach Maßgabe dieses Vertrags.

### 2. Pflegegegenstand, Releaseumfang und ausgeschlossene Leistungen

2.1 Gepflegt werden der bei Vertragsbeginn produktiv eingesetzte Release-Stand sowie der jeweils unmittelbar vorhergehende freigegebene Release-Stand. Ältere Stände, individuell veränderte Programmstände, nicht freigegebene Erweiterungen und kundenseitig veränderte Datenbankschemata werden nur gepflegt, wenn Anlage 1 sie ausdrücklich einbezieht.

2.2 Updates sind Fehlerkorrekturen, Sicherheitskorrekturen, Anpassungen an zwingende gesetzliche oder technische Vorgaben und Kompatibilitätskorrekturen innerhalb desselben Hauptreleases. Updates sind von der Pflegepauschale umfasst.

2.3 Upgrades sind neue Hauptreleases mit erweitertem Funktionsumfang, geänderter Architektur oder zusätzlichem Modulumfang. Upgrades sind [von der Pflegepauschale umfasst / gesondert nach Angebot zu vergüten / nur bei Sicherheits- oder Compliance-Erforderlichkeit umfasst].

2.4 Nicht geschuldet sind Individualentwicklung, Datenmigration, Schulung, Prozessberatung, kundenspezifische Reports, Wiederherstellung nach fehlender Datensicherung, Beseitigung von Störungen durch nicht freigegebene Drittsoftware, Hardwarefehler, kundenseitige Netzwerkstörungen, unautorisierte Eingriffe und Bedienfehler außerhalb dokumentierter Standardnutzung.

2.5 Leistungen während einer noch laufenden kauf- oder werkvertraglichen Mängelhaftung aus dem Lizenz-, Kauf- oder Projektvertrag werden nicht über die Pflegepauschale vergütet, soweit sie dort als Nacherfüllung geschuldet sind. Die Parteien dokumentieren in Anlage 1, welche offenen Gewährleistungspunkte bei Vertragsbeginn bestehen.

### 3. Störungsmeldung, Klassifizierung und Service Level

3.1 Die Kundin meldet Störungen über [Ticketsystem / Hotline / E-Mail-Adresse] mit Zeit, Release-Stand, Mandant, Nutzerrolle, betroffener Funktion, Fehlermeldung, Logauszug, Reproduktionsschritten, Geschäftsauswirkung und erreichbarer Ansprechperson.

3.2 Eine Störung der Klasse 1 liegt vor, wenn der produktive Betrieb insgesamt ausfällt, ein kritischer Geschäftsprozess nicht ausführbar ist, Datenverlust droht oder eine Sicherheitsfunktion versagt. Die Pflegegeberin bestätigt den Eingang binnen [Stunden] innerhalb der Servicezeit und beginnt unverzüglich mit der Entstörung. Sie arbeitet bis zur Wiederherstellung oder bis zur Bereitstellung eines zumutbaren Workarounds mit Vorrang fort.

3.3 Eine Störung der Klasse 2 liegt vor, wenn eine wesentliche Funktion erheblich beeinträchtigt ist, der Betrieb aber mit Workaround oder manueller Ersatzhandlung fortgeführt werden kann. Die Pflegegeberin bestätigt den Eingang binnen [Stunden] und stellt binnen [Werktage] einen Workaround, Patchtermin oder begründeten Maßnahmenplan bereit.

3.4 Eine Störung der Klasse 3 liegt vor, wenn Nebenfunktionen, Komfortfunktionen, Anzeigen, Reports oder nicht produktionskritische Schnittstellen beeinträchtigt sind. Die Pflegegeberin beantwortet die Meldung binnen [Werktage] und ordnet die Korrektur einem Wartungsrelease zu.

3.5 Reaktionszeit ist die Zeit vom Eingang einer qualifizierten Meldung bis zur ersten fachlich verwertbaren Rückmeldung der Pflegegeberin. Wiederherstellungszeit ist die Zeit bis zur produktiv nutzbaren Fehlerumgehung oder Fehlerkorrektur. Beide Zeiten laufen nur, soweit die Kundin die in Abschnitt 5 genannten Mitwirkungen erfüllt.

3.6 Verfehlt die Pflegegeberin die Reaktionszeit für Klasse 1 oder Klasse 2 schuldhaft, erhält die Kundin je angefangenem Kalendertag der Überschreitung einen Service Credit von [Prozentsatz] Prozent der monatlichen Pflegepauschale, höchstens [Prozentsatz] Prozent der jährlichen Pflegepauschale. Weitergehende Ansprüche bleiben bestehen; Service Credits werden auf Schadensersatz angerechnet.

### 4. Updates, Sicherheitskorrekturen und Releasewechsel

4.1 Die Pflegegeberin stellt Sicherheitsupdates unverzüglich bereit, wenn eine Schwachstelle die Vertraulichkeit, Integrität oder Verfügbarkeit der Software oder der verarbeiteten Daten wesentlich gefährdet. Bei kritischen Schwachstellen benennt sie binnen [Stunden] Risiko, betroffene Versionen, Workaround, Patchziel und Prüfempfehlung.

4.2 Funktionale Updates werden mit Release Notes, Installationshinweisen, bekannten Einschränkungen, Rückfallplan und Testempfehlung bereitgestellt. Die Kundin entscheidet nach fachlicher Prüfung, ob und wann sie ein nicht sicherheitskritisches Update produktiv einspielt.

4.3 Releasewechsel werden mindestens [Anzahl] Kalendertage vor Ende der Pflegebereitschaft des alten Releases angekündigt. Die Pflegegeberin unterstützt Testinstallation, Kompatibilitätsprüfung, Schnittstellentest und Rückfallkonzept nach Anlage 2.

4.4 Ändert ein Update Datenmodell, Schnittstelle, Rollenmodell, Berichtswesen oder Exportformat, beschreibt die Pflegegeberin die Änderung so konkret, dass die Kundin betroffene Prozesse, Drittanwendungen und Berechtigungen prüfen kann.

### 5. Mitwirkung, Systemumgebung und Datensicherung

5.1 Die Kundin hält die in Anlage 1 bezeichnete Systemumgebung, Datenbankversion, Middleware, Betriebssysteme, Browser, Schnittstellen, Netzverbindungen und Rechtekonzepte innerhalb der freigegebenen Supportmatrix.

5.2 Die Kundin benennt fachkundige Key User, technische Ansprechpersonen und Eskalationskontakte. Nur diese Personen geben Störungen frei, priorisieren Tickets und entscheiden über Workarounds, Testfreigabe und Produktiveinspielung.

5.3 Vor jedem Update, vor jeder produktiven Datenänderung und vor jeder Fernwartung mit Änderungsrisiko erstellt die Kundin eine rückspielbare Datensicherung. Unterbleibt diese Sicherung, haftet die Pflegegeberin für Datenverlust nur, soweit der Schaden auch bei ordnungsgemäßer Sicherung entstanden wäre.

5.4 Verzögern fehlende Logdateien, fehlende Zugänge, unvollständige Reproduktionsschritte, nicht erreichbare Ansprechpersonen oder eine abweichende Systemumgebung die Leistung, verlängern sich Service-Level-Fristen angemessen. Mehraufwand wird nach Anlage 4 vergütet, wenn die Pflegegeberin die Behinderung dokumentiert und die Kundin hierauf hingewiesen hat.

### 6. Fernwartung, Datenschutz und Vertraulichkeit

6.1 Fernwartung erfolgt nur über die in Anlage 3 bezeichneten Zugänge mit personalisierten Kennungen, Protokollierung, zeitlicher Begrenzung und Freigabe im Einzelfall. Dauerzugänge sind nur zulässig, wenn Anlage 3 Zweck, Rollen, Authentifizierung, Sperrverfahren und Protokollkontrolle festlegt.

6.2 Soweit die Pflegegeberin bei Pflege, Support, Fernwartung, Logging oder Ticketbearbeitung personenbezogene Daten verarbeitet, gilt der Auftragsverarbeitungsvertrag in Anlage 3. Produktiver Zugriff darf erst erfolgen, wenn Weisungen, technische und organisatorische Maßnahmen, Unterauftragnehmer, Löschung, Rückgabe und Kontrollrechte geregelt sind.

6.3 Die Pflegegeberin verpflichtet alle eingesetzten Personen auf Vertraulichkeit. Sie behandelt Quellcode, Datenbankauszüge, Systemarchitektur, Zugangsdaten, Fehlerberichte, Geschäftsprozesse, Preislisten und nicht öffentliche Sicherheitsinformationen als Geschäftsgeheimnisse im Sinne des GeschGehG.

### 7. Vergütung, Zusatzleistungen und Abrechnung

7.1 Die Pflegepauschale beträgt [Betrag in EUR] netto je [Monat / Quartal / Jahr] und umfasst die in Abschnitt 2 bis Abschnitt 6 beschriebenen Standardleistungen für die in Anlage 1 bezeichnete Softwareinstallation.

7.2 Nicht pauschalierte Leistungen werden nur vergütet, wenn die Kundin sie in Textform beauftragt oder wenn sie zur Abwehr einer Störung der Klasse 1 objektiv erforderlich sind und eine vorherige Freigabe nicht rechtzeitig eingeholt werden kann. Die Stundensätze, Zuschläge, Reisezeiten, Bereitschaftskosten und Nachweispflichten ergeben sich aus Anlage 4.

7.3 Rechnungen sind binnen [Anzahl] Kalendertagen nach Zugang zahlbar. Die Pflegegeberin legt bei Zusatzleistungen Ticketnummer, Leistungsdatum, Rolle, Zeitaufwand, Ergebnis und Freigabe bei.

7.4 Preisänderungen der Pflegepauschale sind frühestens nach [Anzahl] Monaten zulässig. Sie müssen [Anzahl] Monate vor Wirksamwerden in Textform angekündigt werden. Übersteigt die Erhöhung [Prozentsatz] Prozent innerhalb von zwölf Monaten, kann die Kundin zum Erhöhungszeitpunkt kündigen.

### 8. Laufzeit, Kündigung und Pflegeende

8.1 Der Vertrag beginnt am [Datum] und läuft zunächst bis [Datum]. Er verlängert sich um jeweils [Anzahl] Monate, wenn er nicht mit einer Frist von [Anzahl] Monaten zum Laufzeitende in Textform gekündigt wird.

8.2 Das Recht zur Kündigung aus wichtigem Grund bleibt unberührt. Ein wichtiger Grund zugunsten der Kundin liegt insbesondere vor, wenn die Pflegegeberin wiederholt Klasse-1-Störungen nicht bearbeitet, Sicherheitsupdates nicht bereitstellt, Fernwartungszugänge missbraucht oder die Pflegebereitschaft ohne geordneten Migrationspfad einstellt.

8.3 Das Recht zur Kündigung aus wichtigem Grund zugunsten der Pflegegeberin besteht insbesondere bei Zahlungsverzug trotz Mahnung, unzulässiger Veränderung der Software, fortgesetzter Nutzung nicht freigegebener Systemumgebungen oder wiederholter Verweigerung erforderlicher Mitwirkung.

8.4 Bei Vertragsende übergibt die Pflegegeberin offene Tickets, Störungshistorie, Release-Stand, Konfigurationsdokumentation, bekannte Workarounds, kundenspezifische Skripte und noch offene Sicherheitsmeldungen in strukturierter Form. Eine Übergabe an eine neue Pflegegeberin erfolgt nach Anlage 4.

### 9. Haftung, Gewährleistungsabgrenzung und Audit

9.1 Die Pflegegeberin haftet unbeschränkt für Vorsatz, grobe Fahrlässigkeit, Verletzung von Leben, Körper oder Gesundheit, ausdrücklich übernommene Garantien und zwingende gesetzliche Haftung.

9.2 Bei einfacher Fahrlässigkeit haftet die Pflegegeberin nur bei Verletzung wesentlicher Vertragspflichten und begrenzt auf den vertragstypischen, vorhersehbaren Schaden. Die Haftungsobergrenze beträgt [Jahrespflegepauschale / Betrag in EUR] je Schadensfall und [Betrag in EUR] insgesamt je Vertragsjahr, soweit diese Begrenzung wirksam vereinbart werden kann.

9.3 Die Kundin darf einmal je Vertragsjahr die Einhaltung der vereinbarten Supportprozesse, Fernwartungsprotokolle, Unterauftragnehmerliste und Ticketnachweise prüfen, soweit dadurch Geschäftsgeheimnisse anderer Kunden nicht offengelegt werden. Datenschutzrechtliche Kontrollrechte aus Anlage 3 bleiben unberührt.

### 10. Schlussbestimmungen

10.1 Änderungen, Nebenabreden, Freigaben, Updatefreigaben, Kündigungen und Eskalationen bedürfen der Textform, soweit nicht gesetzlich strengere Form vorgeschrieben ist.

10.2 Es gilt das Recht der Bundesrepublik Deutschland unter Ausschluss des UN-Kaufrechts.

10.3 Gerichtsstand ist [Ort], soweit gesetzlich zulässig.

### Schluss, Unterzeichnung und Freigabe

[Ort], den [Datum]

| Für die Kundin | Für die Pflegegeberin |
|---|---|
| _____________________________ | _____________________________ |
| [Name, Funktion, Vertretungsrolle] | [Name, Funktion, Vertretungsrolle] |

**Weitere Zustimmung / fachliche Freigabe:** [nicht erforderlich / IT-Leitung / Datenschutzfreigabe / Informationssicherheitsfreigabe / Einkaufsfreigabe]

## Anlagen

### Anlage 1 — Pflegegegenstand, Systemumgebung und offene Gewährleistungspunkte

1. Software und Lizenzgrundlage

1.1 Produkt, Version, Modulumfang, Lizenzvertrag und Installationsdatum: [Produktname; Versionsstand; gepflegte Module; Lizenzvertragsdatum; Installationsdatum; produktive Instanz].

1.2 Produktive Mandanten, Standorte, Geschäftsprozesse und kritische Zeitfenster: [Mandantennamen; Standorte; betroffene Geschäftsprozesse; Monatsabschluss; Produktionsfenster; Sperrzeiten].

2. Systemumgebung

2.1 Betriebssysteme, Datenbank, Middleware, Browser, Schnittstellen, Drittsoftware und Infrastruktur: [Serverbetriebssystem; Datenbankversion; Middleware; Browserfreigabe; API; Drittsoftware; Cloud- oder On-Premises-Umgebung].

2.2 Freigegebene Abweichungen und nicht gepflegte Komponenten: [abweichende Konfiguration; kundeneigene Anpassung; nicht unterstütztes Release; ausgenommene Schnittstelle; Risikoübernahme durch Auftraggeberin].

3. Offene Gewährleistungspunkte

3.1 Offene Mängel aus Lizenz-, Kauf- oder Projektvertrag: [Ticketnummer; Mangelbild; geschuldete Nacherfüllung; Verantwortlichkeit].

### Anlage 2 — Störungsklassen, Releaseplan und Testfreigabe

1. Störungsklassen

1.1 Klasse 1, Klasse 2 und Klasse 3 mit Reaktionszeit, Wiederherstellungsziel, Eskalationskontakt und Service-Credit-Schwelle: [Störungsklasse; produktiver Stillstand; Reaktionszeit; Wiederherstellungsziel; Eskalationskontakt; Service-Credit-Schwelle].

2. Releaseplan

2.1 Wartungsfenster, Sicherheitsupdatepfad, unterstützte Releases und Ende der Pflegebereitschaft: [reguläres Wartungsfenster; Notfallpatchverfahren; unterstützte Major-Versionen; End-of-Support-Datum; Vorankündigungsfrist].

3. Testfreigabe

3.1 Testumgebung, Testdaten, fachliche Abnahmekriterien, Rückfallplan und Produktivfreigabe: [Testsystem; anonymisierte Testdaten; Abnahmekriterien; Rückfallplan; Freigabeverantwortliche; Produktivsetzungstermin].

### Anlage 3 — Fernwartung, Auftragsverarbeitung und Sicherheitsmaßnahmen

1. Fernwartung

1.1 Zugangswerkzeug, Authentifizierung, Freigabeprozess, Protokollierung, Sperrverfahren und Verantwortliche: [Fernwartungstool; Multi-Faktor-Authentifizierung; Ticketfreigabe; Sitzungsprotokoll; Notfallsperre; verantwortliche Administratoren].

2. Auftragsverarbeitung

2.1 Gegenstand, Dauer, Weisungen, Kategorien personenbezogener Daten, betroffene Personen, Unterauftragnehmer, technische und organisatorische Maßnahmen, Löschung, Rückgabe, Audit und Unterstützungspflichten: [Supportzugriff; Laufzeit; Weisungskanal; Datenkategorien; Beschäftigte oder Kunden; Unterauftragnehmer; TOM; Löschfrist; Rückgabeformat; Auditnachweis].

3. Sicherheitsvorfall

3.1 Meldeweg, Kontaktpersonen, Erstinformation, Frist, Eindämmung und Abschlussbericht: [Sicherheitskontakt; Meldekanal; Erstmeldung binnen Stunden; Eindämmungsmaßnahme; Statusbericht; Abschlussbericht].

### Anlage 4 — Vergütung, Zusatzleistungen und Exit

1. Pflegepauschale

1.1 Betrag, Abrechnungsperiode, Zahlungsziel und enthaltene Leistungen: [Pflegepauschale in EUR; monatliche oder jährliche Abrechnung; Zahlungsziel in Tagen; enthaltene Supportstunden; enthaltene Releases].

2. Zusatzleistungen

2.1 Stundensätze, Zuschläge, Bereitschaft, Reisezeiten, Nachweise und Freigabeverfahren: [Stundensatz in EUR; Nacht- oder Wochenendzuschlag; Bereitschaftspauschale; Reisezeit; Leistungsnachweis; Bestellfreigabe].

3. Exit

3.1 Übergabepaket, offene Tickets, Konfigurationen, Dokumentation, Übergabe an Dritte und Vergütung der Übergabeleistungen: [Exportpaket; offene Ticketliste; Konfigurationsdokumentation; Schnittstellenbeschreibung; Übergabetermin; Vergütung in EUR].

---

Lizenz: Apache-2.0 OR MIT.
