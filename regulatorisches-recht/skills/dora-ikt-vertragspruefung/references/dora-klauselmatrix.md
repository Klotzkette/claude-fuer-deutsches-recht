# DORA-Klauselmatrix – Vollversion

Diese Matrix wird von der Tabular-Review-Engine verwendet. Spalten:
`#`, `Anker`, `Pflichtinhalt (Soll)`, `Geltung`, `Prüfkriterien`, `Akzeptanzkriterien`, `Beispiel-Klauselentwurf`.

## Allgemeine Pflichten (Art. 30 Abs. 2 DORA – alle Verträge)

| # | Anker | Soll | Geltung | Prüfkriterien | Akzeptanzkriterien | Klauselentwurf (DE) |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Art. 30 II lit. a | Klarer Leistungs- und Funktionsbeschrieb inkl. Subfunktionen | alle | Vollständigkeit, Eindeutigkeit | Funktion(en) sind zuordenbar und granular benannt | "Der Auftragnehmer erbringt die in Anlage 1 abschließend beschriebenen IKT-Dienste, einschließlich aller Sub-Funktionen und Module …" |
| 2 | Art. 30 II lit. b | Standortangaben Leistung/Daten | alle | Region/Land je Funktion | Adressen, Rechenzentren, Backup-Standorte | "Die Leistung wird in der EU/EWR-Region [X] erbracht; abweichende Standorte bedürfen vorheriger schriftlicher Zustimmung." |
| 3 | Art. 30 II lit. c | Datenqualität (Verfügbarkeit, Authentizität, Integrität, Vertraulichkeit) | alle | technisch-organisatorische Maßnahmen, Verschlüsselung | TOMs definiert, Standards (ISO 27001, BSI C5) referenziert | "Der Auftragnehmer gewährleistet … nach ISO 27001/BSI C5 Typ 2 … Verschlüsselung at rest und in transit nach Stand der Technik." |
| 4 | Art. 30 II lit. d | Zugriff, Wiederherstellung, Rückgabe und Löschung von Daten | alle | Format, Frist, Nachweis | maschinenlesbar, ≤ 30 Tage Rückgabe, ≤ 90 Tage Löschung mit Protokoll | siehe SKILL.md Beispiel |
| 5 | Art. 30 II lit. e | Service Levels | alle | KPIs, Pönalen | Verfügbarkeit, RTO/RPO, Reaktion/Lösung | "Verfügbarkeit ≥ 99,9 % p. M.; RTO ≤ 4 h; RPO ≤ 15 min; Pönale gemäß Anlage SLA." |
| 6 | Art. 30 II lit. f | Incident Support | alle | Unterstützung bei IKT-Vorfällen | 24/7 Hotline; ohne/mit Zusatzkosten klar geregelt | "Bei IKT-Vorfällen leistet der Auftragnehmer 24/7-Support ohne Zusatzkosten innerhalb der vereinbarten SLA." |
| 7 | Art. 30 II lit. g | Mitwirkung gegenüber zuständigen Behörden + Resolution Authority | alle | Pflichtklausel | Auskünfte, Vor-Ort-Zugang, Dokumentenherausgabe | "Der Auftragnehmer wirkt … auf erstes Anfordern und ohne gesonderte Vergütung mit der zuständigen Behörde und der Resolution Authority zusammen …" |
| 8 | Art. 30 II lit. h | Kündigungsrechte | alle | außerordentliche Kündigung; Mindestfristen | mindestens behördliche Anordnung, gravierende Vorfälle, Insolvenz, Verstoß gegen anwendbares Recht | "Der Auftraggeber kann den Vertrag außerordentlich kündigen, wenn … (Katalog)." |
| 9 | Art. 30 II lit. i | Schulung / Awareness | alle | Teilnahme an Schulungen sofern relevant | mindestens jährlich; Nachweis | "Der Auftragnehmer nimmt an den jährlichen IKT-Sicherheits-Schulungen des Auftraggebers teil." |

## Verschärfte Pflichten (Art. 30 Abs. 3 DORA – kritisch oder wichtig)

| # | Anker | Soll | Prüfkriterien | Akzeptanzkriterien |
| --- | --- | --- | --- | --- |
| 10 | Art. 30 III lit. a | Ausführliche SLAs inkl. Updates/Versionen | granular, mit Eskalation | klare Änderungssteuerung, Patch-/Upgrade-Pfad |
| 11 | Art. 30 III lit. b | Kündigung + Berichtspflichten zugunsten Aufsicht | Vorabanzeige Behörde, Übergangshilfe | mindestens 6 Monate Übergangszeitraum |
| 12 | Art. 30 III lit. c | Fortlaufende Überwachung | KPIs, Monitoring-Rechte, Reports | Real-Time-Dashboard oder mindestens monatlicher Bericht |
| 13 | Art. 30 III lit. d | IKT-Sicherheitsanforderungen + Schulungen | TOMs, Awareness | Compliance-Nachweise jährlich |
| 14 | Art. 30 III lit. e | Beteiligung an TLPT (Art. 26, 27 DORA + RTS 2024/3172) | Vereinbarung über Mitwirkung im Tests-Zyklus | Mitwirkungspflicht; Kosten geregelt |
| 15 | Art. 30 III lit. f | Audit-/Einsichtsrechte | kostenfrei, anlassbezogen, Lead Overseer einschließen | Audit-Klausel deckt Behörden und externe Prüfer |
| 16 | Art. 30 III lit. g | Exit-Strategie | Migrationshilfe, Datenformat, Übergangszeitraum | Exit-Plan dokumentiert |
| 17 | Art. 30 III lit. h | Notfallpläne, BCM, DR | RTO/RPO; Tests; Berichte | mindestens jährliche Tests, Bericht an Auftraggeber |

## Sub-Outsourcing (RTS 2024/1773)

| # | Anker | Soll | Prüfkriterien |
| --- | --- | --- | --- |
| 18 | Art. 30 II lit. j; RTS 2024/1773 Art. 5, 6 | Materialitätsschwellen, Ex-ante-Anzeige, Genehmigungsvorbehalt für Tier-N-Subs | Liste der Subs, Kettenabbildung, Anzeigewege |

## Informationsregister (DurchfVO 2024/2956)

| # | Anker | Soll |
| --- | --- | --- |
| 19 | DurchfVO 2024/2956 | Vertrag liefert alle Felder des Informationsregisters (z. B. LEI, Funktionstyp, Datenort) |

## Aufsichts- und Resolution-Rechte (Art. 28 VII DORA)

| # | Anker | Soll |
| --- | --- | --- |
| 20 | Art. 28 VII | Keine vertragliche Beschränkung der Rechte zuständiger Behörden und der Resolution Authority |

## Querschnitt – Datenschutz, Berufsgeheimnis, AGB

| # | Anker | Soll |
| --- | --- | --- |
| 21 | Art. 28 DSGVO | AVV vorhanden, Sub-AV-Konsens, EU-SCC bei Drittland |
| 22 | § 203 III StGB | "Mitwirkende Personen"-Klausel mit Verpflichtungserklärung |
| 23 | § 9 KWG / § 311 VAG | Wahrung Bankgeheimnis/Versicherungsgeheimnis |
| 24 | §§ 305 ff. BGB | AGB-Kontrolle B2B: keine unangemessenen Haftungsausschlüsse |

## Bewertungs-Schema Kritikalität

| Stufe | Beschreibung |
| --- | --- |
| 5 | Verstoß gegen Pflichtvorgabe für **kritische/wichtige** Funktion; Re-Papering vor Geltungsbeginn zwingend |
| 4 | Pflichtinhalt fehlt teilweise oder ist unklar; Nachverhandlung dringend |
| 3 | Klausel vorhanden, aber unvollständig oder nicht aktuell |
| 2 | Klausel akzeptabel, mit Optimierungspotenzial |
| 1 | Klausel konform |
