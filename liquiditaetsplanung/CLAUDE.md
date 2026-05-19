# Plugin `liquiditaetsplanung` — Agenten-Konfiguration

Dieses Plugin ist ein **Bündel-Plugin**: Es definiert keine eigenen Skills, sondern verweist auf die Liquiditätsplanungs-Skills der Plugins `steuerberater-werkzeuge` und `insolvenzrecht`.

## Skill-Auswahl-Logik

| Situation der Nutzerin / des Nutzers | Zu wählender Skill | Heimatplugin |
|---|---|---|
| Wöchentliche Geschäftsführer-Sitzung, frühe Krise, Ampel-Routine | `liquiditaetsvorschau-3wochen` | `steuerberater-werkzeuge` |
| Sanierungskonzept, Bankgespräch, StaRUG-Vorbereitung, integrierte Planung | `liquiditaetsvorschau-3-6-12-monate` | `steuerberater-werkzeuge` |
| Antragspflicht-Prüfung § 15a InsO, Gläubigerantrag § 14 InsO, gerichtliche Beweisführung | `liquiditaetsvorschau-insolvenzrechtlich` | `insolvenzrecht` |

## Verbindliche Maßstäbe

- **§ 17 InsO**: 10-%-Lücke / 3-Wochen-Horizont nach BGH BGHZ 163, 134 Rn. 12 ff.
- **§ 19 InsO**: Zweistufige Überschuldungsprüfung (rechnerische Unterdeckung **und** negative Fortbestehensprognose) — BGH BGHZ 195, 42 Rn. 12 ff.
- **Fortbestehensprognose**: tragfähiges Unternehmenskonzept und integrierter Finanzplan, Maßstab überwiegende Wahrscheinlichkeit — BGH NJW 2020, 1809 Rn. 18.
- **IDW S 6** für Sanierungskonzepte, **IDW S 11** für Insolvenzeröffnungsgründe.

## Eskalationsregel

Wenn ein Liquiditätsplan eine 🔴-Ampel zeigt oder die 3-Wochen-Schließbarkeit nicht gegeben ist, sofort auf das Plugin `insolvenzrecht` umschwenken (`antragspflicht-15a-inso`, `zahlungsunfaehigkeit-pruefung-17-inso`) und auf die Hinweispflicht des Steuerberaters nach § 102 StaRUG aufmerksam machen (Skill `bwa-sus-bilanz-pruefung` aus `steuerberater-werkzeuge`).

## Konfiguration

Dieses Plugin selbst benötigt keine Praxisprofil-Konfiguration — die liegt bei den Heimatplugins der jeweiligen Skills.
