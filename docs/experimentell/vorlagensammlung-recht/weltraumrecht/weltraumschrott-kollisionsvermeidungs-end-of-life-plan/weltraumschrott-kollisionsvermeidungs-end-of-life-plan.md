# Weltraumschrott-, Kollisionsvermeidungs- und End-of-Life-Plan

---

Kurz-Hinweis: Diese Vorlage ist unverbindlich, ein experimenteller Text und keine Rechtsberatung. Nutzung nur auf eigene Gewähr, eigene Gefahr und ohne Gewähr. Die ausführlichen Hinweise zu § 43a Abs. 2 BRAO, § 203 StGB, DSGVO sowie Apache-2.0 OR MIT stehen in der README dieser Vorlage.

---

## Vorlage

[WARNHINWEIS — nicht Planbestandteil, vor Freigabe entfernen]

Diese Vorlage ersetzt nicht die flugdynamische, technische und rechtliche Eigenleistung. Sie liefert das Entscheidungsgerüst, nicht die Bahnberechnung. Der Anwender bringt aktuelle Ephemeriden, Kovarianzen, Manöverleistung, Treibstoffbudget und Risikomodelle; die Vorlage bringt Schwellen, Rollen und die unbedingt zu prüfenden Stellen.

Weitere Hinweise und ausführliche Praxis-Erläuterungen in der README dieser Vorlage.

An die

[freigabeverantwortliche Missionsleitung]

### 1. Mission und verbindlicher Maßstab

1.1 Mission: [Missionsname und Kennung]. Betreiber: [Firma, Rechtsform, Sitz und Leitstelle]. Weltraumgegenstand: [Satellit, Stufe, Adapter, Aussetzvorrichtung und weitere freigesetzte Gegenstände].

1.2 Geplanter Orbit: [Orbitregime, mittlere Höhe, Inklination, Exzentrizität, Perigäum und Apogäum]. Aussetzung: [Datum, Träger, Startplatz und Aussetzsequenz]. Betriebsdauer: [Dauer].

1.3 Maßgeblicher technischer Standard ist [Standard, Fassung und Missionsklasse]. Abweichungen sind ausschließlich die in Anlage 1 begründeten und genehmigten Abweichungen.

### 2. Verantwortungen und Erreichbarkeit

2.1 Mission Operations entscheidet über Routinebetrieb. Flight Dynamics berechnet Bahnen und Manöver. Der Collision Avoidance Officer bewertet Begegnungen. Der Mission Director trifft die abschließende Go-No-Go-Entscheidung.

2.2 Rund-um-die-Uhr-Kontaktstellen lauten: [Name, Funktion, Telefon, E-Mail und Ersatzkontakt]. Meldungen von Trackingdiensten werden an [Funktionspostfach und technischer Eingang] automatisch verteilt und quittiert.

2.3 Externe Tracking-, Manöver- und Startdienstleister sind in Anlage 2 mit Datenformat, Aktualisierungsintervall, Verfügbarkeit, Eskalation und Haftungsschnittstelle bezeichnet.

### 3. Freisetzungs- und Bruchvermeidung

3.1 Die Mission setzt planmäßig ausschließlich [vollständige Liste der Gegenstände] frei. Schutzkappen, Halterungen, Drähte, Adapterteile und Betriebsstoffe bleiben [gebunden / werden mit begründetem Verhalten freigesetzt].

3.2 Druckbehälter, Batterien, Antrieb, Schwungräder, pyrotechnische Komponenten und gespeicherte Energie sind in Anlage 3 mit Betriebs- und Versagenszuständen erfasst.

3.3 Unbeabsichtigte Freisetzung oder Fragmentierung wird durch [Konstruktionsmaßnahme, Test, Überwachung und Betriebsgrenze] verhindert. Ein Ereignis löst unverzüglich [Sicherungsmaßnahme, Bahncharakterisierung, Betreiber- und Behördenmeldung] aus.

### 4. Tracking und Bahnbestimmung

4.1 Eigene Bahnbestimmung verwendet [GNSS, Radar, Laser, Funkmessung oder Kombination]. Messdaten werden mindestens [Intervall] aktualisiert; während kritischer Phasen gilt [Intervall].

4.2 Bahnzustand und Unsicherheit werden in [Referenzsystem, Zeitmaßstab und Datenformat] geführt. Qualitätsgrenzen sind [Kovarianz-, Residuen- oder Altersgrenze]. Überschreitungen lösen zusätzliche Messungen aus.

4.3 Der Betreiber bezieht conjunction data messages oder gleichwertige Warnungen von [Dienst]. Nachrichten werden automatisch archiviert und einer Missionskennung zugeordnet.

### 5. Kollisionsbewertung

5.1 Jede Begegnung wird anhand von Kollisionswahrscheinlichkeit, Miss Distance, radialem, entlangbahnigem und normalem Abstand, Objektgröße, Datenalter, Kovarianzqualität, relativer Geschwindigkeit und Zeit bis zur engsten Annäherung bewertet.

5.2 [Variante A — numerische Schwelle]

Ab [Schwelle der Kollisionswahrscheinlichkeit] oder [räumliche Abstandsschwelle] beginnt die vertiefte Analyse; ab [Schwelle für die Manöverentscheidung] ist eine dokumentierte Manöverentscheidung erforderlich.

5.3 [Variante B — risikobasierte Schwelle]

Wenn Unsicherheit und mögliche Schadensfolge eine sichere Entwarnung nicht tragen, beginnt unabhängig von einer einzelnen Kennzahl die vertiefte Analyse.

5.4 Flight Dynamics aktualisiert die Bewertung bis [Entscheidungszeit vor Annäherung] und dokumentiert Datenquelle, Annahmen, Sensitivität, mögliche Sekundärbegegnungen und Auswirkungen auf Mission und End-of-Life-Budget.

### 6. Kollisionsvermeidungsmanöver

6.1 Für jedes Manöver werden mindestens drei Optionen berechnet: [radial / entlang der Bahn / normal zur Bahnebene oder missionsgeeignete Alternativen]. Jede Option weist Delta-v, Ausführungsfenster, Kraftstoffverbrauch, Missionsausfall, Sekundärbegegnungen und Rückkehrplan aus.

6.2 Die Go-No-Go-Entscheidung enthält Ausgangsrisiko, Datenqualität, gewählte Option, Restrisiko, Auswirkungen auf Dritte, Freigaben und Zeitpunkt. Sie wird von [Rollen] unterzeichnet oder elektronisch freigegeben.

6.3 Nach Ausführung werden Telemetrie, tatsächliches Delta-v, neue Bahn und verbleibendes Risiko geprüft. Abweichungen oberhalb [Schwelle] lösen eine Neubewertung aus.

### 7. Koordinierung mit anderen Betreibern

7.1 Die Identität und Kontaktstelle des anderen Betreibers werden über [Quelle] verifiziert. Ausgetauscht werden nur erforderliche Bahn-, Manöver- und Kontaktinformationen.

7.2 Beide Betreiber klären, wer manövriert, welche Bahnabsicht zugrunde liegt, wann die Entscheidung fällt und wie widersprüchliche Absichten aufgelöst werden. Eine fehlende Einigung entbindet den Betreiber nicht von der eigenen Risikobewertung.

### 8. End-of-Life-Auslöser und Reserve

8.1 Die End-of-Life-Phase beginnt bei [geplantes Missionsende] oder vorzeitig bei [Treibstoffschwelle, Energiezustand, Kommunikationsausfall, kritischem Komponentenverlust oder Risikoschwelle].

8.2 Für Kollisionsvermeidung und End-of-Life bleibt eine geschützte Reserve von [Delta-v, Treibstoffmasse und Energiebudget]. Eine Freigabe für andere Missionszwecke erfordert [Risikoprüfung und Genehmiger].

8.3 [Variante A — kontrollierter Wiedereintritt: Zielkorridor, Zeitfenster, Überflugbewertung, Fragmentanalyse, Behörden- und Verkehrsinformation sowie Abbruchpunkte ergeben sich aus Anlage 4.; Variante B — natürlicher oder gesteuerter unkontrollierter Wiedereintritt: erwartete Restlebensdauer, Überlebensanalyse, Bodenrisiko, Bahnüberwachung und Kommunikationsplan ergeben sich aus Anlage 4.; Variante C — Friedhofs- oder Entsorgungsorbit: Zielbahn, Stabilität, Freihaltung geschützter Regionen und langfristige Entwicklung ergeben sich aus Anlage 4.]

### 9. Passivierung

9.1 Nach dem letzten erforderlichen Manöver werden verbleibende Treibstoffe, Druck, Batterieladung, Schwungradenergie und pyrotechnische Kreise nach der Sequenz [Bezeichnung] in einen dauerhaft sicheren Zustand überführt.

9.2 Telecommand-Empfang und Nutzlastbetrieb werden [deaktiviert / auf sicheren Restbetrieb begrenzt]. Der endgültige Zustand verhindert unbeabsichtigtes Wiederhochfahren und spätere Fragmentierung.

9.3 Der Passivierungserfolg wird durch [Telemetriekanäle und Schwellen] nachgewiesen. Teilerfolg oder Ausfall führt zu [Ersatzsequenz, erneuten Kontaktversuchen und Risikobewertung].

### 10. Kontrollverlust und ungeplanter Ausfall

10.1 Bei Kontaktverlust werden in der Reihenfolge [Bodenstationen, Frequenzen, Safe-Mode-Befehle und externe Hilfe] Wiedergewinnungsversuche unternommen. Versuche, Ergebnisse und aktualisierte Bahnprognosen werden protokolliert.

10.2 Wenn Kontrolle nicht wiederhergestellt wird, bestimmt der Betreiber Bahn, Rotationszustand, Energie- und Fragmentierungsrisiko soweit möglich und aktualisiert Tracking- und Kontaktstellen.

10.3 Behörden, Registerstelle, Startdienstleister, Versicherer und betroffene Betreiber werden nach der in Anlage 5 festgelegten Zuständigkeits- und Meldeprüfung informiert.

### 11. Abschluss und Nachbetrieb

11.1 Der Abschlussbericht enthält finale Orbitparameter, Manöverhistorie, Passivierungsstatus, verbleibende Gefahrenquellen, erwartete Bahnlebensdauer, offene Trackingpflichten und Abweichungen vom Plan.

11.2 Registrierungs- und Statusangaben werden anhand `weltraumrecht/registrierungsdossier-weltraumgegenstand/` aktualisiert. Die nationale Kontaktstelle erhält [Statusmeldung und Nachweise] am [Datum].

11.3 Bahn- und Ereignisdaten werden für [Dauer und Rechts- oder Vertragsgrund] aufbewahrt. Verantwortlich für den Nachbetrieb bis [Endereignis] ist [Rechtsträger und Kontaktstelle].

### 12. Freigabe

12.1 Der Plan wurde gegen Mission, Startvertrag, Versicherungsbedingungen und den in Abschnitt 1.3 bestimmten Standard geprüft.

[Ort], den [Datum]

[Name und Funktion Mission Director]

[Name und Funktion Flight Dynamics Lead]

[Unterschriften oder dokumentierte elektronische Freigaben]

## Anlagen

### Anlage 1 — Standards und Abweichungen

1.1 [Anforderung, Nachweis, Abweichung, Begründung, Kompensation und Genehmiger].

### Anlage 2 — Tracking- und Kontaktstellen

2.1 [Dienst, Daten, Format, Intervall, Verfügbarkeit, Kontakt und Eskalation].

### Anlage 3 — Freisetzungs- und Energieinventar

3.1 [Gegenstand oder Energiequelle, Zustand, Risiko, Kontrolle und Endzustand].

### Anlage 4 — End-of-Life-Analyse

4.1 [Variante, Bahn, Manöver, Fragment- und Bodenrisiko, Annahmen und Nachweise].

### Anlage 5 — Ereignis- und Meldematrix

5.1 [Ereignis, Schwelle, Sofortmaßnahme, Entscheidung, Empfänger, Frist und Nachweis].

---

Lizenz: Apache-2.0 OR MIT.
