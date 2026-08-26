---
name: anschluss-routing
description: "Leitet eine begonnene Migrationsakte anhand von Status, Stichtag, Frist und Ziel in den passenden Fachskill weiter."
---

# 1. Anschluss-Routing im Migrationsrecht

## 1.1 Vorprüfung

Lies das bisherige Arbeitsergebnis und die vorhandenen Dokumente. Wiederhole kein Kaltstartinterview, wenn Status, Bescheid und Ziel bereits erkennbar sind.

## 1.2 Routingweichen

1. Welcher Status besteht heute und welche Entscheidung wird angegriffen oder beantragt?
2. Wann wurde ein Asylantrag gestellt und gilt altes Recht oder das seit 12. Juni 2026 anwendbare neue GEAS?
3. Welche Frist läuft aus welchem Dokument?
4. Drohen Überstellung, Abschiebung, Haft, Erlöschen eines Titels oder Verlust einer Beschäftigung?
5. Welches konkrete Arbeitsprodukt wird jetzt benötigt?

## 1.3 Hauptpfade

| Fallkern | Hauptskill | Produkt |
| --- | --- | --- |
| Schutzantrag, Anhörung oder Ablehnung | `workflow-asyl-start` | Schutzgrund-, Fristen- und Belegmatrix |
| Verantwortlicher Mitgliedstaat | `workflow-dublin-geas-start` | Stichtags- und Zuständigkeitsprüfung |
| Ausweisung | `workflow-ausweisung-start` oder `ausweisung-abwaegung` | Abwägungsmatrix und Rechtsbehelf |
| Aufenthalts- oder Beschäftigungstitel | `workflow-aufenthaltstitel-router` | Anspruchs- und Unterlagenplan |
| Folgeantrag | `asylantrag-folgeverfahren-paragraf-71-asylg` | Wiederaufgreifens- und Neuigkeitsprüfung |
| Akute Frist | `workflow-fristenrettung-asyl-aufenthalt` | fristwahrender Entwurf und Eilplan |
| Abschiebehaft | `abschiebehaft-paragraf-62-aufenthg` | Haftgrund-, Dauer- und Beschwerdeprüfung |

## 1.4 Qualitätsregeln

1. Nenne genau einen Hauptskill und höchstens zwei Nebenspuren.
2. Berechne die Frist aus dem konkreten Bescheid und dem anwendbaren Übergangsrecht.
3. C-490/16 ist nur ein Altfallsanker für Dublin III; C-247/20 betrifft Freizügigkeitsrecht und Krankenversicherung, nicht Asyl oder Ausweisung im Allgemeinen.
4. Trenne Statusentscheidung, Vollziehung, Abschiebungsandrohung, Einreiseverbot und Haft.
5. Gib sofort das nächste Arbeitsprodukt aus, nicht nur eine Liste möglicher Skills.

## 1.5 Ausgabe

Erstelle eine Routingkarte mit Status, Stichtagsregime, Frist, Hauptskill, Nebenspur, fehlenden Unterlagen und dem nächsten versandfertigen Produkt.
