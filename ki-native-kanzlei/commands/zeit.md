---
description: "Tatsächliche Arbeitszeit des Tages abfragen, buchen und den Rechnungsentwurf fortschreiben."
argument-hint: "Akte oder leer für alle heutigen Arbeiten"
---

Führe den Ablauf aus Abschnitt 1.10 mit dem Skill zeiten-erfassen aus. Schlage Narrative vor, buche erst nach Angabe der tatsächlichen Minuten und der Abrechenbarkeit mit `kanzlei.py time` und melde Budget- oder Deckelwirkung an honorar-budget-vereinbaren.

Eingabe: $ARGUMENTS

Lies zuerst den Mandatslauf mit `python3 "<Pluginordner>/scripts/mandatslauf.py" status --akte "<Akte>"` oder den letzten Textstatus. Bei mehreren Akten lies deren Status einzeln; ohne vorhandenen Lauf kläre Akten-ID und Stufe, bevor du ihn anlegst. Übernimm führende Fassungen, Fristobjekte, Honorar- und Zeitstand; frage nur entscheidende neue Angaben ab. Arbeite innerhalb der Stufe weiter und schließe mit dem Statusblock nach [Mandatslauf, Abschnitt 1.11](../references/mandatslauf-und-freigaben.md): Phase, Produkte mit Pfad/Hash oder Textfassung, Friststatus, Honorar, bestätigte Minuten, offene Gates mit zuständiger Person, offene Fragen und nächstes Produkt. Nicht berechnete Hashes oder fehlende Namen bleiben offen. G2 hat Vorrang; unabhängige interne Arbeit bleibt möglich. Außenwirkung setzt eine tatsächlich erklärte, namentlich dokumentierte menschliche Freigabe für die konkrete Fassung voraus. [Kanzleialltag](../references/kanzleialltag-workflows.md).
