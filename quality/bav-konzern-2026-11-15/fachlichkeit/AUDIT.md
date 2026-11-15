# 1. Fachlicher Änderungs- und Quellenaudit

Prüfdatum: 15.11.2026. Bearbeitungsumfang: 56 historische FACHINHALT-Dateien und eine Navigationshilfe, zehn aktive Skills, beide Standalone-Prompts und acht neue Fachkapitel. Die historischen Texte wurden vor Archivierung vollständig gelesen; identische wiederholte Absätze wurden einmal mit Vorkommenszuordnung gelesen. Dies ist keine Aussage, sämtliche denkbaren Normen, Literatur oder ausländischen Rechtsordnungen vollständig geprüft zu haben.

## 1.1. Bestand und Erhalt

Die 57 Altdateien liegen unverändert unter `../legacy/`; `../legacy/mapping.json` hält alten Pfad, Archivpfad, Bytezahl und SHA-256 fest. `konsolidierung.json` ordnet jede Altdatei einem fachlichen Zielkapitel zu. Alle zehn Skill-IDs bleiben bestehen. Keine historische Datei ist im installierbaren Plugin nötig. Wiederholte Checklisten, fachfremde allgemeine Sätze und nicht belastbare Detailbehauptungen wurden aus der operativen Anleitung entfernt, bleiben aber im Archiv überprüfbar. Themen wie Expatriates, Steuern, IFRS und Datenschutz wurden als gezielte Prüfpfade erhalten; ungesicherte Länderwerte und Vollständigkeitsansprüche bewusst nicht übernommen.

## 1.2. Konkrete Fehler und Korrekturen

### 1.2.1. drei-stufen-expatriate-pensionsplanung

- Altpfad: `bav-strategie-konzern/skills/drei-stufen-expatriate-pensionsplanung/FACHINHALT.md:65`.
- Historische Passage: „**Kein Rechtfertigungsmaßstab** — absoluter Schutz“.
- Korrektur: 1. Stufe ausnahmsweise bei zwingenden Gründen; kein absoluter Schutz ohne Ausnahme.
- Tragstelle/Prüfgrenze: BAG 02.07.2024 – Az. 3 AZR 247/23, Rn. 15.
- Neue Umsetzung: `bav-strategie-konzern/references/konzern/02-harmonisierung-und-mitbestimmung.md`.

### 1.2.2. pensionsmodelle-risikoampel-und-gegenargumente

- Altpfad: `bav-strategie-konzern/skills/pensionsmodelle-risikoampel-und-gegenargumente/FACHINHALT.md:42`.
- Historische Passage: „| 2 | künftige dienstzeitabhängige Zuwächse“.
- Korrektur: Stufe 2 ist erdiente dienstzeitunabhängige Dynamik; künftige dienstzeitabhängige Zuwächse gehören zu Stufe 3.
- Tragstelle/Prüfgrenze: BAG 02.07.2024 – Az. 3 AZR 247/23, Rn. 15.
- Neue Umsetzung: `bav-strategie-konzern/references/konzern/02-harmonisierung-und-mitbestimmung.md`.

### 1.2.3. psv-pensionssicherungsverein-und-haftungsketten

- Altpfad: `bav-strategie-konzern/skills/psv-pensionssicherungsverein-und-haftungsketten/FACHINHALT.md:31`.
- Historische Passage: „§ 7 Abs. 4 BetrAVG (Konzernhaftung“.
- Korrektur: § 7 Abs. 4 enthält Leistungsbegrenzung/Anrechnung, keine Konzernhaftung.
- Tragstelle/Prüfgrenze: BetrAVG § 7 Abs. 4, amtlicher Volltext.
- Neue Umsetzung: `bav-strategie-konzern/references/konzern/05-finanzierung-cta-und-insolvenzschutz.md`.

### 1.2.4. psv-pensionssicherungsverein-und-haftungsketten

- Altpfad: `bav-strategie-konzern/skills/psv-pensionssicherungsverein-und-haftungsketten/FACHINHALT.md:30`.
- Historische Passage: „§ 14 BetrAVG (Meldepflichten“.
- Korrektur: Meldepflichten in § 11; Beitragsbemessung in § 10.
- Tragstelle/Prüfgrenze: BetrAVG §§ 10 und 11, amtlicher Volltext.
- Neue Umsetzung: `bav-strategie-konzern/references/konzern/05-finanzierung-cta-und-insolvenzschutz.md`.

### 1.2.5. altersversorgung-boutique-fristennotiz-psv

- Altpfad: `bav-strategie-konzern/skills/altersversorgung-boutique-fristennotiz-psv/FACHINHALT.md:39`.
- Historische Passage: „jährliche Beitragspflicht zum 31.03.“.
- Korrektur: Kein solcher allgemeiner Termin; Bemessungsgrundlage nach § 11 Abs. 2 bis 30. September; Zahlung nach tatsächlichem Bescheid.
- Tragstelle/Prüfgrenze: BetrAVG § 11 Abs. 2 und § 10 Abs. 2.
- Neue Umsetzung: `bav-strategie-konzern/references/konzern/05-finanzierung-cta-und-insolvenzschutz.md`.

### 1.2.6. historisch-gewachsene-altsysteme-due-diligence

- Altpfad: `bav-strategie-konzern/skills/historisch-gewachsene-altsysteme-due-diligence/FACHINHALT.md:26`.
- Historische Passage: „bis 1999 fünf Jahre + Alter 35“.
- Korrektur: Historische Voraussetzungen und Auffangregeln anhand § 30f differenziert; alte 10-/12-/3-Jahresalternativen nicht unterschlagen.
- Tragstelle/Prüfgrenze: BetrAVG § 30f.
- Neue Umsetzung: `bav-strategie-konzern/references/konzern/01-bestand-und-zusagen.md`.

### 1.2.7. versorgungsordnung-und-betriebsvereinbarung-drafting

- Altpfad: `bav-strategie-konzern/skills/versorgungsordnung-und-betriebsvereinbarung-drafting/FACHINHALT.md:249`.
- Historische Passage: „BBG-West, aktuell EUR 7.248 p.a. in 2024“.
- Korrektur: Jahreswert und Prozentzahl widersprüchlich; keine statische veraltete Zahl im aktiven Muster. Konkretes Jahr und Prozentbasis künftig amtlich prüfen.
- Tragstelle/Prüfgrenze: BetrAVG § 1a; aktives Kapitel 6 verlangt Jahresquellen statt ungeprüftem Zahlenanker.
- Neue Umsetzung: `bav-strategie-konzern/references/konzern/06-steuer-bilanz-und-international.md`.

### 1.2.8. versorgungsordnung-und-betriebsvereinbarung-drafting

- Altpfad: `bav-strategie-konzern/skills/versorgungsordnung-und-betriebsvereinbarung-drafting/FACHINHALT.md:182`.
- Historische Passage: „wenn die laufenden Renten jährlich um mindestens 1 % erhöht werden“.
- Korrektur: Pauschale Ausnahme um § 30c-Zusagezeitpunkt und weitere §-16-Fälle ergänzt.
- Tragstelle/Prüfgrenze: BetrAVG §§ 16, 30c; BAG 25.11.2025 – Az. 3 AZR 91/25, Rn. 18–31.
- Neue Umsetzung: `bav-strategie-konzern/references/konzern/03-anpassung-und-arbeitgeberhaftung.md`.

### 1.2.9. buyout-ma-country-by-cta-contractual

- Altpfad: `bav-strategie-konzern/skills/buyout-ma-country-by-cta-contractual/FACHINHALT.md:93`.
- Historische Passage: „üblicherweise 0,5–1 % Transaktionswert“.
- Korrektur: Unbelegte Marktquote entfernt; Angebot mit Datum, versicherter Partei und Ausschlüssen prüfen. Keine Ersatzquote erfunden.
- Tragstelle/Prüfgrenze: Kein belastbarer Primärbeleg für Altbehauptung vorhanden; explizit als unbelegt verworfen.
- Neue Umsetzung: `bav-strategie-konzern/references/konzern/04-transaktionen-und-rentnergesellschaft.md`.

### 1.2.10. buyout-ma-country-by-cta-contractual

- Altpfad: `bav-strategie-konzern/skills/buyout-ma-country-by-cta-contractual/FACHINHALT.md:29`.
- Historische Passage: „§§ 133, 134, 157 HGB“.
- Korrektur: Unpassende Normenkette nicht fortgeschrieben; tatsächlichen Weg nach § 613a BGB, § 4 BetrAVG und gegebenenfalls § 133 UmwG bestimmen.
- Tragstelle/Prüfgrenze: Amtliche Normen BGB § 613a, BetrAVG § 4, UmwG § 133.
- Neue Umsetzung: `bav-strategie-konzern/references/konzern/04-transaktionen-und-rentnergesellschaft.md`.

### 1.2.11. pensionsmodelle-fuenf-bav-cta-pensionsfond

- Altpfad: `bav-strategie-konzern/skills/pensionsmodelle-fuenf-bav-cta-pensionsfond/FACHINHALT.md:255`.
- Historische Passage: „§ 1 Abs. 2 Nr. 2 SGB VI (Versicherungsfreiheit reine DC“.
- Korrektur: Reine Beitragszusage folgt § 1 Abs. 2 Nr. 2a BetrAVG im Sozialpartnermodell; nicht Beitragszusage mit Mindestleistung oder behauptete SGB-VI-Versicherungsfreiheit.
- Tragstelle/Prüfgrenze: BetrAVG § 1 Abs. 2 Nr. 2 und 2a; BAG 14.03.2023 – Az. 3 AZR 176/22, Rn. 25–35.
- Neue Umsetzung: `bav-strategie-konzern/references/konzern/01-bestand-und-zusagen.md`.

### 1.2.12. internationale-buyout-datenflows-und-datenschutz

- Altpfad: `bav-strategie-konzern/skills/internationale-buyout-datenflows-und-datenschutz/FACHINHALT.md:109`.
- Historische Passage: „DSFA, Art. 35 DSGVO): Obligatorisch“.
- Korrektur: Pauschalen Automatismus verworfen; konkreten Tatbestand, Datenart und Verarbeitung prüfen. Internationale Einzelwerte nicht ohne lokalen aktuellen Volltext übernehmen.
- Tragstelle/Prüfgrenze: Redaktionelle Begrenzung; keine vollständige Datenschutz-/Drittlandprüfung in diesem Audit behauptet.
- Neue Umsetzung: `bav-strategie-konzern/references/konzern/06-steuer-bilanz-und-international.md`.

### 1.2.13. governance-und-anpassungsmechanismen

- Altpfad: `bav-strategie-konzern/skills/governance-und-anpassungsmechanismen/FACHINHALT.md:33`.
- Historische Passage: „MaRisk (Mindestanforderungen an das Risikomanagement — analog anwendbar“.
- Korrektur: Keine allgemeine rechtliche MaRisk-Analogie für jedes interne Pension Committee behaupten; konkrete Gesellschaft und anwendbares Aufsichtsrecht prüfen.
- Tragstelle/Prüfgrenze: Unbelegte Generalisierung verworfen; aktives Kapitel 7 formuliert interne Gestaltung als Vorschlag.
- Neue Umsetzung: `bav-strategie-konzern/references/konzern/07-arbeitsprodukte-und-governance.md`.

### 1.2.14. governance-und-anpassungsmechanismen

- Altpfad: `bav-strategie-konzern/skills/governance-und-anpassungsmechanismen/FACHINHALT.md:47`.
- Historische Passage: „DBO über EUR 100 Mio.“.
- Korrektur: Unbelegte Volumenschwelle nicht als Markt- oder Gesetzesregel übernehmen; Governance nach konkreter Organisation entwerfen.
- Tragstelle/Prüfgrenze: Kein belastbarer Primärbeleg für Altquote vorhanden; keine Ersatzquote erfunden.
- Neue Umsetzung: `bav-strategie-konzern/references/konzern/07-arbeitsprodukte-und-governance.md`.

## 1.3. Weitere bewusst nicht fortgeschriebene Aussagen

CTA als genereller Ersatz des PSV, pauschale Haftungsentlassung durch Buyout-Prämie, automatische IAS-19-Einordnung, unbedingte §-613a-Folgen jedes Asset Deals, starre Aufsichtsfristen und pauschale Ländersteuerwerte werden nicht übernommen. Die Neufassung setzt positive Voraussetzungen, Vertragsprüfung und fachliche Grenzen an ihre Stelle. Wo keine aktuelle Detailquelle geprüft wurde, gibt es einen konkret begrenzten Rechercheauftrag statt eines vermeintlich sicheren Ergebnisses. Die vollständig erhaltenen Originale ermöglichen die Nachprüfung der weggefallenen Detailformulierungen.

## 1.4. Quellenstatus und Reichweite

`quellen/manifest.json` dokumentiert 22 Originalabrufe mit URL, Abrufdatum, Dateigröße und SHA-256 der unkomprimierten Antwort. Die gzip-Archive enthalten die empfangenen Originalbytes; die zusätzlichen TXT-Dateien dienen nur dem Lesen. Die Prüftabelle in `quellenpruefung.json` nennt tatsächlich gelesene Normen beziehungsweise Randnummern. Abruf und Hash sind kein Ersatz für inhaltliche Prüfung. Bei Rechtsprechung wurden Metadaten und die angegebenen Passagen mit Kontext geprüft; keine pauschale Volltextlektüre aller zwölf Urteile behauptet.

BRSG II: tatsächliches Gesetz statt Entwurfsstand; allgemeines Inkrafttreten 22.01.2026 und spätere Änderungen von § 6 BetrAVG/§ 100 EStG zum 01.01.2027 getrennt. Neue Unterdeckungsregel aus Art. 3 Nr. 7 mit Voraussetzungen gelesen. Die Hinweise zu Steuer, IFRS und internationalem Recht sind bewusst begrenzt; keine umfassende aktuelle IFRS- oder Auslandsgutachtenprüfung. Keine erfundene Literatur oder Marktstatistik.

## 1.5. Konkrete redaktionelle Gegenprüfung

Root-Gegenlese hat § 20 Abs. 3 um den ausdrücklichen BV-/DV-Weg ergänzt, § 133 UmwG auf Nachhaftung nicht zugewiesener Verbindlichkeiten präzisiert und Fiktionshinweise auf Paket-README statt zusätzliche PDF-Warnseiten abgestimmt. Entscheidungszitate tragen „Az.“ und die Entscheidungsart. Die erste Stufe, KBR-Zuständigkeit bei freiwilliger ausschließlich konzernweiter Gewährung sowie §-16-Übergangsrecht wurden ausdrücklich gegen die häufigsten falschen Kurzformeln abgegrenzt.

## 1.6. Technische Nachweise

Die tatsächlichen Prüfresultate stehen in `strukturpruefung.json`. Der Fachagent bestätigt damit nur seinen Inhalts-/Strukturbestand, nicht einen Release, Paketdownload, entfernte CI oder Veröffentlichung. Diese Schritte führt die übergeordnete Integration gesondert aus.

Aktualitätsnachsuche: 1 AZR 147/24 zusätzlich mit Rn. 29–43 und 63–78 aufgenommen; die Sitzungsergebnisliste bis November 2026 geprüft. 3 AZR 70/26 aus September war dort ohne Volltextlink; keine Sachregel aus dem Tenor übernommen.
