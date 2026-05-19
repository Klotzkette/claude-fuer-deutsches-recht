# eingang/ — eingehende prozessuale Schriftsätze und Korrespondenz

Dieses Verzeichnis enthält die Triagierung und Bearbeitung aller von außen eingehenden Schriftstücke: empfangene Mahnschreiben, der Sozietät zugestellte Beweisanordnungen, behördliche Anfragen, Aufforderungen zur Beweissicherung sowie an uns gerichtete Abmahnungen.

Getrennt von `mahnschreiben/` (ausgehend) und `mandate/` (erfasstes Portfolio), weil eingehende Schriftstücke einen eigenen Ablauf haben: lesen → triagieren → entscheiden → antworten (oder Mandat anlegen). Nicht jedes Eingangsstück wird zu einem erfassten Mandat.

## Verzeichnisstruktur

```
eingang/
├── _README.md
└── [slug]/
    ├── eingang.pdf              # oder .eml / .docx — das Original (oder Verweis/Pfad)
    ├── triage.md                # Analyse: Umfang, Berechtigung, Optionen, Empfehlung
    └── antwort-v1.docx          # Antwortentwurf, sofern eine Antwort erfolgt (v2, v3 bei Überarbeitungen)
```

## Slug-Konventionen

`[art]-[absender-kurz]-[jjjj-mm]`. Beispiele:

- `mahnung-eingegangen-mustermann-2026-04` (empfangenes Mahnschreiben)
- `vorlageanordnung-schmidt-v-bundesrepublik-2026-04` (Beweisanordnung als Drittpartei)
- `behoerde-bundeskartellamt-anfrage-2026-04`
- `beweissicherung-auftragnehmer-2026-04` (eingegangene Beweissicherungsaufforderung)

## Ablauf

| Art | Befehl | Ergebnisse |
|---|---|---|
| Empfangenes Mahnschreiben | `/prozessrecht:mahnung-eingegangen [pfad]` | triage.md + optionaler Antwortentwurf |
| Vorlage-/Beweisanordnung erhalten | `/prozessrecht:vorlageanordnung [pfad]` | triage.md + Einwendungs-Memo |
| Behördliche Anfrage | *zukünftiger Skill* | |

Jede Triagierung gleicht `mandate/_log.yaml` auf verwandte Mandate ab (gleiche Gegenseite, überschneidender Gegenstand). Liegt ein verwandtes Mandat vor, weist die Triagierung darauf hin und bietet an, dieses Schriftstück als `verwandte_mandate`-Eintrag hinzuzufügen. Soll das eingegangene Schriftstück selbst zu einem erfassten Mandat werden, übergibt die Triagierung an `/mandat-aufnahme` mit vorausgefüllten Feldern.

## Verhältnis zu Mandaten

- Eingang + verwandt mit bestehendem Mandat → Verknüpfung über das Feld `verwandte_mandate` in `_log.yaml`; Datei verbleibt in `eingang/`.
- Eingang + soll eigenständiges Mandat werden → Mandat anlegen; `mandat.md` verweist zurück auf `eingang/[slug]/`.
- Eingang + erledigt und abgeschlossen (kein Mandat erforderlich) → verbleibt in `eingang/` als Beleg.

## Verhältnis zu ausgehenden Schriftstücken

Ist die Antwort auf ein eingehendes Mahnschreiben selbst ein ausgehendes Mahnschreiben (Gegenmahnschreiben), übergibt die Triagierung an `/mahnung-aufnahme` mit vorausgefüllten Feldern. Das ausgehende Schreiben liegt in `mahnschreiben/`, mit Rückverweis auf diesen Eingangsordner.
