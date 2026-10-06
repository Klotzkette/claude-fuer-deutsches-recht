# Rechtsquellen und Grenzen der Dokumentenerstellung

## 1. Prüfstand und Methode

Die nachstehenden öffentlichen amtlichen Quellen wurden am 6. Oktober 2026 live geöffnet und inhaltlich geprüft. Ein Quellenabruf ist keine Prüfung des konkreten berechtigten Interesses, der Vertretung, eines Empfängers oder eines importierten Ortsprofils. Vor einer Einreichung muss die Rechtsabteilung den aktuellen Rechts- und Verfahrensstand erneut prüfen. Die Zitierweise folgt [der zentralen Referenz](../../references/zitierweise.md).

Der Dokumentenbaustein erzeugt deterministisch vier Entwürfe aus den Vorgangsangaben. Er recherchiert weder Eigentümer noch führt er einen Grundbuchabruf durch. Er versendet keine Anfrage und beauftragt keinen Notar. Alle Ausgaben bleiben als `ENTWURF - NICHT FREIGEGEBEN` markiert. HTML ist vollständig und wird als `.html` ausgegeben; DOCX wird tatsächlich mit `python-docx` erstellt. Die Grundschrift ist Times New Roman, 11 pt. Überschriften sind dezimal gegliedert; der Text besteht aus ausformulierten Sätzen und zeigt fehlende Angaben als `[ergänzen]`.

## 2. Bundesrechtliche Zugangswege

### 2.1. Grundbucheinsicht und Abschriften

Paragraf 12 Absatz 1 GBO setzt grundsätzlich die Darlegung eines berechtigten Interesses voraus. Absatz 2 erlaubt Abschriften im Umfang des zulässigen Einsichtsrechts; eine Beglaubigung muss verlangt werden. Zweck, konkrete Beziehung zur Fläche, notwendiger Umfang und Nachweise werden deshalb getrennt erfasst. Eine bloße Versorgungsaufgabe eines Stadt- oder Wasserwerks beweist weder das konkrete Interesse noch eine privilegierte Behördenstellung. Der Entwurf behauptet keine bereits erteilte Berechtigung. [Amtlicher Gesetzestext: Paragraf 12 GBO](https://www.gesetze-im-internet.de/gbo/__12.html).

Der Einzelabruf von Paragraf 12 schlug beim Livecheck mit einem Abrufzeitfehler fehl. Der vollständige Normtext wurde anschließend in der amtlichen [Gesamtausgabe der GBO, Abschnitt Paragraf 12](https://www.gesetze-im-internet.de/gbo/BJNR001390897.html) gelesen. Die Prüfung beruht somit nicht allein auf einem Suchtreffer.

### 2.2. Automatisiertes Abrufverfahren

Paragraf 133 GBO betrifft die Einrichtung und Zulässigkeit eines automatisierten Abrufverfahrens. Es gelten insbesondere die Grenzen des zulässigen Einsichtsumfangs, Kontrollierbarkeit und Genehmigungsvoraussetzungen. Die Erstellung eines Formularentwurfs ersetzt weder die Genehmigung noch die materielle Berechtigung. Das Plugin nimmt an diesem Verfahren nicht teil. [Amtlicher Gesetzestext: Paragraf 133 GBO](https://www.gesetze-im-internet.de/gbo/__133.html).

### 2.3. Notarielle Mitteilung als Alternative

Paragraf 133a Absatz 1 GBO erlaubt notarielle Mitteilungen an Personen, die ein berechtigtes Interesse im Sinne von Paragraf 12 GBO darlegen. Absatz 2 schließt Mitteilungen im öffentlichen Interesse sowie zu wissenschaftlichen und Forschungszwecken aus. Absatz 5 ermöglicht landesrechtliche Einschränkungen, die vor der Beauftragung zu prüfen sind. Die Protokollierung richtet sich nach den Absätzen 3 und 4. Die Organisation wählt den Notar selbst aus und klärt Umfang und Kosten; die Rechtsabteilung gibt einen Auftrag gesondert frei. Der notarielle Weg und die Anfrage beim Grundbuchamt sind Alternativen, kein automatischer Parallelversand. [Amtlicher Gesetzestext: Paragraf 133a GBO](https://www.gesetze-im-internet.de/gbo/__133a.html).

### 2.4. Grundstück, Flurstück und Grundbuchblatt

Ein Flurstück ist eine katastermäßig abgegrenzte und bezeichnete Bodenfläche. Das Grundstück im grundbuchrechtlichen Sinn ist die unter einer eigenen laufenden Nummer des Bestandsverzeichnisses gebuchte rechtliche Einheit und kann mehrere Flurstücke umfassen. Das Grundbuchblatt ist das Registerblatt und kann mehrere Grundstücke aufnehmen. Die Begriffe und Nummern sind daher nicht austauschbar. Die amtliche GBO unterscheidet die katastermäßige Bezeichnung, das Grundbuchblatt und gemeinschaftliche Buchung insbesondere in Paragrafen 2 bis 4. [Amtlicher Gesetzestext: GBO](https://www.gesetze-im-internet.de/gbo/BJNR001390897.html).

Eine Kartenauswahl ersetzt keine Eigentumsfeststellung. Fehlende Blattstellen werden nicht aus Koordinaten oder Flurstückskennzeichen errechnet. Optional können je Auswahlposition `grundbuchblatt`, `grundbuchblaetter`, `grundbuchbezirk`, `grundbuchblatt_source` und `grundbuchblatt_date` als manuell belegte Angaben übergeben werden. Mehrfache und ungeklärte Zuordnungen bleiben sichtbar. Der Baustein liest aus dem Nachweistext keine Dateien.

## 3. Katasterauskunft ausschließlich für Nordrhein-Westfalen

Paragraf 14 Absatz 1 VermKatG NRW betrifft die Bereitstellung von Katasterdaten. Für Eigentümerangaben verlangt Absatz 2 grundsätzlich ein dargelegtes berechtigtes Interesse. Die Ausnahmen knüpfen an die konkret bezeichneten Rollen und gesetzlichen Aufgaben an; eine Versorgungsorganisation wird nicht pauschal darunter eingeordnet. Absatz 3 verlangt die Löschung nach Zweckerfüllung und verbietet Datenbestände für unbestimmte Zwecke. [Amtlicher Normtext: Paragraf 14 VermKatG NRW](https://recht.nrw.de/lrgv/gesetz/08122020-gesetz-ueber-die-landesvermessung-und-das-liegenschaftskataster-vermessungs/).

Beim Livecheck wurde die dort ausgewiesene Fassung mit Gültigkeit ab 8. Dezember 2020 einschließlich Paragraf 14 gelesen. Dieses Fassungsdatum ist vom Abrufdatum 6. Oktober 2026 zu unterscheiden.

Der NRW-Text wird nur für ein ausdrücklich als Nordrhein-Westfalen bezeichnetes Profil verwendet, sofern mitgelieferte Gemeindeschlüssel nicht widersprechen. Bei anderen oder unbekannten Ländern nennt der Entwurf keine NRW-Norm, sondern einen offenen Prüfpunkt für das einschlägige Landesrecht. Ein importiertes Landesprofil ist kein Nachweis seiner administrativen Richtigkeit.

## 4. Amtliche Verfahren in Münster

### 4.1. Katasterstelle

Die Stadt Münster nennt das Vermessungs- und Katasteramt als Stelle für die Führung und Bereitstellung des Liegenschaftskatasters im Stadtgebiet. Die Kontaktseite nennt das Stadthaus 3, Albersloher Weg 33, 48155 Münster. Diese Kontaktangabe wird nicht ungeprüft zur verbindlichen Briefanschrift oder zum zulässigen elektronischen Einreichungsweg erklärt. [Stadt Münster: Vermessungs- und Katasteramt](https://www.stadt-muenster.de/katasteramt/startseite).

Das Kundenzentrum Planen und Bauen beschreibt Katasterauskünfte und Auszüge nach telefonischer Terminvereinbarung. Damit ist ein örtlicher Informationsweg belegt, aber keine pauschale Eigentümerauskunft für beliebige Antragsteller. [Stadt Münster: Ihre Fragen, unser Service, Abschnitt Karten und Pläne](https://www.stadt-muenster.de/planen-bauen/ihre-fragen-unser-service).

Die neue städtische Seite „Liegenschaftsbuch“ war erreichbar, enthielt im abgerufenen Inhalt jedoch keine ausführliche Verfahrensbeschreibung und keinen belastbaren Auskunftsantrag. Deshalb wird kein dort nicht verifiziertes Eigentümerformular und kein E-Mail-Einreichungsrecht behauptet. [Stadt Münster: Liegenschaftsbuch](https://www.stadt-muenster.de/katasteramt/service/liegenschaftskataster/liegenschaftsbuch).

### 4.2. Grundbuchamt

Das Amtsgericht Münster nennt für Grundbuchausdrucke die schriftliche, persönliche oder Fax-Antragstellung und verweist auf Antragsformulare sowie Identitäts- und gegebenenfalls Berechtigungsnachweise. Es stellt den Notar als Alternative dar und bietet eine Terminbuchung für Einsichten an. Das Vorhandensein einer Kontakt-E-Mail wird damit nicht als zulässige Antragstellung ausgegeben. Kosten werden in den Entwürfen nicht fest zugesagt, sondern vor Tätigkeit geklärt. [Amtsgericht Münster: Grundbuchamt, Abschnitte Einsicht und Antrag](https://www.ag-muenster.nrw.de/aufgaben/abteilungen/Grundbuchamt/index.php).

Die verlinkte amtliche NRW-Formularübersicht wurde ebenfalls live geöffnet. Vor einer konkreten Einreichung sind das passende Formular und seine aktuellen Hinweise zu wählen. Eine Formularübersicht beweist nicht die Zuständigkeit für jeden im Stadtgebiet liegenden Sonderfall. [NRW-Justiz: Grundbuchformulare](https://www.justiz.nrw/BS/formulare/grundbuch).

## 5. Import- und Exportgrenzen

`validate_case(case)` nimmt ein bereits dekodiertes JSON-Objekt entgegen und gibt eine unabhängige geprüfte Kopie zurück oder wirft `ValueError`. Ein unbekanntes Feld wird auch innerhalb von Profilen, Quellen, Behörden, Anbietern, Geometrien und Empfängern abgewiesen. Fehlende Formularwerte dürfen leer bleiben; das erlaubt die Vorschau eines noch unvollständigen Vorgangs. Kennzeichen sind Zeichenketten, damit führende Nullen erhalten bleiben.

Die serialisierte Eingabe darf 2 MiB und die Auswahl 200 Positionen nicht überschreiten. Eine einzelne GeoJSON-Geometrie darf höchstens 256 KiB und 10000 Positionen enthalten; für die gesamte Auswahl gelten 40000 Positionen. Die Koordinaten müssen endlich sein und im WGS84-Bereich liegen. Polygonringe müssen geschlossen sein. Unzulässige Steuerzeichen, überlange Texte und übertiefe Datenstrukturen werden verworfen.

### 5.1. Vertrag mit Oberfläche und Server

Alle Felder sind optional; vorhandene Felder müssen den vereinbarten Typ haben. Fehlende Textwerte werden als `""` übertragen, nicht als `null`. Eine Ausnahme bilden ausdrücklich optionale historische Metadaten und Zeitangaben. Die vollständigen, maschinenlesbaren Whitelists sind `CASE_SCHEMA`, `PROFILE_SCHEMA`, `PROVIDER_SCHEMA`, `AUTHORITY_SCHEMA`, `EVIDENCE_SCHEMA`, `COVERAGE_SCHEMA` und `PARCEL_SCHEMA` in `app/documents.py`.

- Das Profil erlaubt die Textfelder `id`, `profile_id`, `name`, `state`, `state_code`, `district`, `municipality_code`, `verification_state`, `center_method`, `attribution` und `license`. `verified_at` und `data_date` sind Text oder `null`. `source_url` und `district_source_url` sind HTTP(S)-URLs oder leere Zeichenketten; `source_urls` ist eine Liste solcher URLs. `warnings` ist eine Textliste. `providers`, `authorities` und `evidence` sind Listen der jeweils strikt geprüften Objekte.
- `center` verwendet wie Leaflet `[Breite, Länge]`; alternativ ist das Objekt mit `latitude` und `longitude` zulässig. `bounds` verwendet `[West, Süd, Ost, Nord]`. Beide dürfen `null` sein. Davon getrennt verwenden GeoJSON-Positionen `[Länge, Breite]`, optional mit numerischer Höhe.
- Anbieter erlauben unter anderem `id`, `provider_id`, `title`, `role`, `protocol`, `version`, `type_name`, `format`, `axis_order`, `license`, `attribution`, `test_result` und die dokumentierten URL-Felder. `license` und `test_result` sind ausschließlich Text, keine offenen Metadatenobjekte. `layers` und `crs` sind Text oder Textlisten; `layers_or_collections` ist eine Textliste. `verified_at` ist Text oder `null`. `requires_host_approval` ist ein boolescher Wert, der keinen serverseitigen Freigabenachweis ersetzt.
- `coverage` ist ein strikt begrenztes Objekt mit `country`, `verification_state`, `state_codes` als Textliste und `bounds` als Liste von Bounding-Boxen. Fremde Felder werden nicht durchgereicht.
- Behörden erlauben `type` beziehungsweise `authority_type`, Namen, Zuständigkeits-, Adress- und Verfahrensangaben, Status und die expliziten Quellenfelder. `verified_at` darf `null` sein. Nachweise erlauben unter anderem `official_name`, `kind`, `source_url`, Prüfstatus und Zeitangaben; `matched` und `returned` sind wie die CSW-Attribute Text oder `null`.
- Flurstücksangaben sind Texte; `area_value` ist ausschließlich eine endliche nichtnegative Zahl oder `null`. `geometry` ist eine geprüfte GeoJSON-Geometrie oder `null`. Die optionale Blattzuordnung wird in Nummer 2.4 beschrieben. Der WFS-Adapter und die Oberfläche müssen Flächenzeichenketten vor der Übergabe in Zahlen normalisieren.

Quellenfelder erlauben nur HTTP(S)-URLs ohne Zugangsdaten; lokale Hostnamen und nicht öffentliche IP-Literale werden abgewiesen. Das ersetzt keine SSRF-Absicherung des Netzwerkadapters, weil dieses Modul weder DNS auflöst noch URLs abruft. Positive Prüfbehauptungen in importierten Profilen, Anbietern, Behörden und Nachweisen werden unabhängig von einem mitgelieferten Datum auf `gefunden_ungeprueft` zurückgestuft. Historische Prüfdaten bleiben zur Nachvollziehbarkeit erhalten. Die Laufzeitverifikation liegt beim Server. Die Entwürfe bezeichnen Profilstatus ausdrücklich als überlieferte Angaben und nicht als neu überprüfte Tatsachen.

`validate_case` wird auch für laufende Vorgänge verwendet und wertet deshalb `selected_parcels.identification_status` nicht pauschal ab. Der Importendpunkt muss unbewiesene positive Identifikationsbehauptungen gezielt zu `manuell_ergaenzt` zurückstufen; Punkte und unidentifizierte Lagehinweise bleiben `location_hint`. Eine bekannte `profile_id` oder Anbieter-ID beweist nicht die Herkunft der einzelnen Auswahl. Sollen importierte Angaben wieder als serverseitig belegt gelten, ist ein Abgleich mit den tatsächlich ausgegebenen Flurstücksdaten erforderlich. Sämtliche Entwürfe erklären unabhängig davon ausdrücklich, dass Quellen und Identifikationsstatus aus dem Vorgang übernommen werden und keine serverseitige Prüfung der einzelnen Flurstücke bestätigen.

`build_documents(case)` liefert in fester Reihenfolge `uebergabe`, `kataster`, `grundbuch` und `notar` mit Titel und vollständigem HTML. `export_document(case, format, document_id=None)` liefert Bytes, MIME-Typ und einen festen Dateinamen. `html` und `docx` können einzeln oder gesammelt ausgegeben werden. `zip` enthält stets vier DOCX, vier HTML, `vorgang.json` und `quellen.txt`. `json` exportiert nur den Vorgang. HTML wird niemals als `.doc` etikettiert. Die HTML-Druckansicht ermöglicht den PDF-Druck durch den Browser; ein eigener PDF-Export wird nicht behauptet.

## 6. Prüfungen

Die isolierten Modultests in `tests/test_documents.py` prüfen HTML-Escaping, echte DOCX-Struktur und Textgleichheit, vollständige Auswahl, NRW-Abgrenzung, Entwurfskennzeichnung, ausformulierte Sätze, alternative Zugangswege, reproduzierbare Exporte, unveränderte Eingaben, verschachtelte Typen, unbekannte Felder, Größenlimits, Geometrien und fehlende Netzwerkzugriffe. Diese technischen Eingaben sind keine Testakten und keine behaupteten realen Grundstücke. Ein bestandener Modultest belegt weder einen erfolgreichen Live-Kartenabruf noch die Berechtigung eines Antragstellers.
