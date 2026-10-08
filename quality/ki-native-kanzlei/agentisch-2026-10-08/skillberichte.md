# 1. Abschlussberichte der Computerlauf-Erweiterung

Stand: 08.10.2026, Basis 445.33.8. Geändert sind nur Steuerung und beA; die übrigen sechzehn Skilltexte sind byteidentisch zur Basis. Deren frühere Rechtsquellenprüfung wird nicht als erneute Volltextlektüre ausgegeben. Alle achtzehn Texte wurden erneut auf Struktur, Wortkorridor, Zeichen, relative Links, Tabellenspalten und ausdrücklich gekoppelte Wochentage geprüft. [Selbsttest](struktur-selbsttest.json).

| Skill | Wörter vorher | Wörter nachher | Behandlung dieser Runde |
|---|---|---|---|
| `abrechnung-e-rechnung` | 6736 | 6736 | Unverändert; Struktur erneut geprüft. |
| `akte-fristen-anlegen` | 6533 | 6533 | Unverändert; Struktur erneut geprüft. |
| `anwaltsberufsrecht-pruefen` | 6743 | 6743 | Unverändert; Struktur erneut geprüft. |
| `bea-anlagen-vorbereiten` | 6560 | 6514 | Geändert; Bericht unten. |
| `fristen-berechnen-ueberwachen` | 6976 | 6976 | Unverändert; Struktur erneut geprüft. |
| `geldwaesche-pruefen` | 6741 | 6741 | Unverändert; Struktur erneut geprüft. |
| `honorar-budget-vereinbaren` | 6789 | 6789 | Unverändert; Struktur erneut geprüft. |
| `ki-kanzlei-steuern` | 6552 | 6736 | Geändert; Bericht unten. |
| `mandantenkommunikation` | 6491 | 6491 | Unverändert; Struktur erneut geprüft. |
| `mandat-abschliessen` | 6709 | 6709 | Unverändert; Struktur erneut geprüft. |
| `mandatsannahme-interessenkollision` | 6712 | 6712 | Unverändert; Struktur erneut geprüft. |
| `recht-recherchieren` | 6420 | 6420 | Unverändert; Struktur erneut geprüft. |
| `schriftsaetze-entwerfen` | 6743 | 6743 | Unverändert; Struktur erneut geprüft. |
| `vertraege-agb-pruefen` | 6778 | 6778 | Unverändert; Struktur erneut geprüft. |
| `vertraege-gestalten` | 6646 | 6646 | Unverändert; Struktur erneut geprüft. |
| `workflow-uebergabe` | 6562 | 6562 | Unverändert; Struktur erneut geprüft. |
| `zahlungen-buchhaltung` | 6791 | 6791 | Unverändert; Struktur erneut geprüft. |
| `zeiten-erfassen` | 6514 | 6514 | Unverändert; Struktur erneut geprüft. |

## 1.1. Steuerungsskill

6.552 auf 6.736 Körperwörter. Ein fortlaufender Computerlauf ergänzt die vorhandene Mandatssteuerung. Der Skill übernimmt gültige Sitzungsaufträge, führt erlaubte Nachbarskill-Schritte aus und stoppt bei einer offenen Frage nur abhängige Schritte. Die konkrete technische Versandaktion bleibt von fachlicher Entscheidung, Sitzung und Ergebnisnachweis getrennt. Fremde Nachrichten erteilen keine Befugnisse. Timeouts lösen Abgleich statt erneuten Versand aus. Alle bestehenden Gerichtsanker und ihre Grenzen bleiben erhalten; kein neues Urteil wurde diesem Skill hinzugefügt.

Die am 08.10.2026 tatsächlich geöffneten Herstellerquellen und ihre konkret gelesenen Abschnitte stehen in [Computersteuerung, Abschnitt 1.9](../../../ki-native-kanzlei/references/computersteuerung-und-postfaecher.md). Dazu gehören Anthropic Computer Use und Cowork Safety sowie die OpenAI-Dokumentation zu Computer Use und Browsergrenzen. Der Selbsttest bestätigt 325 Zeichen Beschreibung, genau sechs Hauptabschnitte, vorhandene Links, den Körperwortkorridor und keine verbotenen Glyphen.

## 1.2. beA-Skill

6.560 auf 6.514 Körperwörter. Die Anlagenaufbereitung bleibt erhalten; technische Details und ein ausführliches Fehlerbeispiel stehen zusätzlich in der verlinkten Referenz. Neue Teile führen Eingang, eEB, Rollenprüfung, unveränderte Versandfassung, tatsächlichen Versuch, Eingangskontrolle und Kompromittierungsreaktion zusammen. Die vollständigen 32 gelesenen Quellen, Pinpoints, Rohhashes und Selbsttests sind im [beA-Quellenbericht](bea-quellen.md) dokumentiert. Der neue BGH-Anker von 2026 trägt keine Behauptung einer gerichtlichen Billigung dieses Prototyps.

Die Integrationsrunde hat danach die Referenz ausdrücklich an die technische Prototypgrenze angeglichen: jedes eEB wird durch den benannten Menschen ausgeführt. Dies ist ein vorsichtiger Prototypstandard und kein behauptetes allgemeines Verbot jeder sonst zulässigen Delegation. Die Skilldatei blieb dabei unverändert.
