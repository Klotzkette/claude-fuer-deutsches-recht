# Sieben-Kategorien-Framework für die Produkt-Launch-Prüfung

Standardframework, wenn das Team kein eigenes hat. Entwickelt aus interner
Produkt-Legal-Praxis. Jede Kategorie hat eine Schlüsselfrage und eine
automatische Überspringbedingung.

Die Kategorien sind stabile Rahmenbegriffe. Was innerhalb einer Kategorie als
"Nachbesserungsbedarf" oder "Blocker" gilt, hängt von den anwendbaren Rechtsordnungen,
Sektorregimen und der eigenen Kalibrierung des Unternehmens in
`~/.claude/plugins/config/claude-fuer-deutsches-recht/produktrecht/CLAUDE.md` ab.
Die einschlägigen Regulierungsregime für den Sektor, die Zielgruppe und die
Rechtsordnungen des Produkts sind zu recherchieren, bevor der Schluss gezogen
wird, ob ein konkretes Tatsachenbild ein Problem darstellt oder nicht.

## 1. Vertragliche Verpflichtungen

**Schlüsselfrage:** Steht dies im Widerspruch zu einem kundenseitigen Versprechen?

Prüfen: Nutzungsbedingungen, SLA-Verpflichtungen, Marketingmaterialien, Kundenverträge
(insbesondere Unternehmens-Rahmenverträge mit individuellen Klauseln), veröffentlichte
Dokumentation.

**Automatisch überspringen wenn:** Keine kundenseitigen Änderungen — internes Werkzeug,
Infrastruktur oder für Benutzer unsichtbare Änderung.

**Häufige Befunde:**
- Neues Feature widerspricht einer AGB-Einschränkung
- SLA-Auswirkungen einer neuen Abhängigkeit
- Feature wurde als "enthalten" vermarktet und wird in einen kostenpflichtigen Tarif verschoben

## 2. Datenschutz

**Schlüsselfrage:** Neue Datenerhebung, neuer Zweck oder neue Weitergabe?

Prüfen: Welche Daten betroffen sind, ob neu oder bestehend, ob der Zweck von der
aktuellen Datenschutzerklärung abgedeckt wird, ob ein neuer Dritter Zugang erhält.
Die anwendbaren Datenschutzregime für die Rechtsordnungen der betroffenen Nutzer
sind zu recherchieren, bevor der Schluss gezogen wird, ob eine neue Datenschutzhinweispflicht,
Einwilligung oder Datenschutz-Folgenabschätzung (Art. 35 DSGVO) erforderlich ist.

**Automatisch überspringen wenn:** Keine Datenänderungen — reine UI-Änderung,
reine Infrastruktur ohne neue Protokollierung.

**Häufige Befunde:** Siehe den DSFA-Skill des Datenschutz-Plugins.

## 3. Sicherheit

**Schlüsselfrage:** Neue Angriffsfläche?

Prüfen: neue Endpunkte, neue ruhende Daten, neue Zugriffspfade, neue Authentifizierungsanforderungen.

**Automatisch überspringen wenn:** Reine UI-Änderung, kein Backend. (Aber sorgfältig prüfen,
ob es wirklich rein UI ist — eine "UI-Änderung", die einen neuen API-Aufruf hinzufügt, ist es nicht.)

**Nicht allein Sache der Rechtsabteilung** — Sicherheitsteam einbeziehen. Die Aufgabe der
Rechtsabteilung ist es sicherzustellen, dass die Sicherheitsprüfung stattgefunden hat und
etwaige Befunde adressiert wurden.

## 4. Schutzrechte (IP)

**Schlüsselfrage:** Drittanbieter-Code, -Inhalte oder potenziell verletzende Ausgaben?

Prüfen: neue Open-Source-Abhängigkeiten (Lizenzkompatibilität — einige Copyleft-Lizenzen begründen
Pflichten, die mit einem proprietären Produkt unvereinbar sind; die konkrete Lizenz recherchieren),
Drittanbieter-Inhalte (Stockbilder, Schriften, Datensätze), Features, die Inhalte ausgeben,
die verletzen könnten (KI-Generierung, öffentlich angezeigte Benutzer-Uploads).

**Automatisch überspringen wenn:** Keine neuen Abhängigkeiten, keine Inhaltsgenerierung,
keine Benutzer-Uploads.

**Häufige Befunde:**
- Copyleft-Lizenz in einer neuen Abhängigkeit
- Herkunft der Trainingsdaten unklar
- Nutzergenerierte Inhalte ohne Notice-and-Takedown-Verfahren nach §§ 7 ff. DDG,
  Art. 16 DSA — anwendbares Safe-Harbor-Regime recherchieren

## 5. Drittanbieter-Interaktionen

**Schlüsselfrage:** Neuer Anbieter, Partner oder neue Integration?

Prüfen: Liegt ein Vertrag vor, liegt ein Auftragsverarbeitungsvertrag (Art. 28 DSGVO) vor,
wenn Daten fließen, ist der Ausfall des Drittanbieters unser Problem (Verfügbarkeit, Sicherheit).

**Automatisch überspringen wenn:** Keine neuen externen Parteien.

**Häufige Befunde:**
- Neuer Anbieter ohne AVV (Art. 28 DSGVO)
- Integrations-Partner mit abweichenden Datenpraktiken
- API-Abhängigkeit ohne SLA

## 6. Regulatorisch / sektorspezifisch

**Schlüsselfrage:** Berührt dies einen regulierten Sektor, eine regulierte Zielgruppe oder Rechtsordnung?

Die einschlägigen Regulierungsregime für den Sektor des Produkts sind zu recherchieren (z. B.
Gesundheit: ProdSichG/GPSR, MDR, ProdHaftG; Finanzdienstleistungen: KWG, WpHG, MiFIR; Kinder
und Schüler: DSGVO Art. 8, § 11 TDDDG (vormals TTDSG, seit Mai 2024); Versicherungen: VAG; Telekommunikation: TKG; Arbeitsrecht:
ArbSchG, ArbZG; Werbung: UWG, HWG, LMIV, Health-Claims-VO), Zielgruppe und Rechtsordnungen
(Deutschland, EU-Mitgliedstaaten, UK und sonstige Regionen, die das Produkt erreicht). Außerdem
Barrierefreiheit (BFSG, European Accessibility Act) und Ausfuhrkontrolle (AWV, Dual-Use-VO) prüfen,
soweit relevant. Primärquellen zitieren und Aktualität verifizieren — regulierte Sektoren und
Rechtsordnungen ändern sich häufig.

**Automatisch überspringen wenn:** Dieselben Nutzer, dieselben Sektoren, dieselben Rechtsordnungen
wie das bestehende Produkt — kein neuer regulatorischer Umfang.

**Häufige Befunde:**
- Einstieg in einen regulierten Sektor ohne die vom Regime geforderte Infrastruktur
  (Verträge, Kontrollen, Offenlegungen)
- Feature, das von einer regulierten Zielgruppe (z. B. Kindern) genutzt werden könnte, ohne
  die vom anwendbaren Regime geforderten Schutzmaßnahmen
- Internationale Expansion in eine Rechtsordnung mit Lokalisierungs-, Zulassungs- oder
  Informationspflichten

## 7. Marketingaussagen

**Schlüsselfrage:** Gibt es Aussagen, die einer Substanziierung bedürfen?

Siehe den Skill zur Prüfung von Marketingaussagen (UWG § 5, § 6; Health-Claims-VO; HWG § 3).

**Automatisch überspringen wenn:** Keine Marketingkomponente — stiller Launch, internes Feature,
Feature-Flag-Umschaltung.
