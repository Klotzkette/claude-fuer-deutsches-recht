---
description: "Neue Mandatsanfrage aufnehmen, Kollision und GwG anlassbezogen prüfen, Honorarstand klären und die Annahme zur Freigabe vorbereiten."
argument-hint: "Anfrage, Mandant, Gegner, Anliegen"
---

Führe den Ablauf aus Abschnitt 1.4 aus: ki-kanzlei-steuern für den Aufnahmevermerk, mandatsannahme-interessenkollision für Kollision und Annahmeschreiben, geldwaesche-pruefen nur bei Katalogtätigkeit, honorar-budget-vereinbaren für den Honorarstand, akte-fristen-anlegen für die Akte. Lege ab Stufe 2 mit `python3 "<Pluginordner>/scripts/mandatslauf.py" init --akte "<Akte>" --matter-id "<Akten-ID>" --stufe 2` den Lauf an, wenn noch keiner besteht. Auf niedrigerer Stufe bleibt er Textstatus. Öffne G1 mit Produkt `annahme` und benannter zuständiger Person; der Name bedeutet keine Freigabe.

Eingabe: $ARGUMENTS

Lies zuerst den Mandatslauf mit `python3 "<Pluginordner>/scripts/mandatslauf.py" status --akte "<Akte>"` oder den letzten Textstatus. Bei mehreren Akten lies deren Status einzeln; ohne vorhandenen Lauf kläre Akten-ID und Stufe, bevor du ihn anlegst. Übernimm führende Fassungen, Fristobjekte, Honorar- und Zeitstand; frage nur entscheidende neue Angaben ab. Arbeite innerhalb der Stufe weiter und schließe mit dem Statusblock nach [Mandatslauf, Abschnitt 1.11](../references/mandatslauf-und-freigaben.md): Phase, Produkte mit Pfad/Hash oder Textfassung, Friststatus, Honorar, bestätigte Minuten, offene Gates mit zuständiger Person, offene Fragen und nächstes Produkt. Nicht berechnete Hashes oder fehlende Namen bleiben offen. G2 hat Vorrang; unabhängige interne Arbeit bleibt möglich. Außenwirkung setzt eine tatsächlich erklärte, namentlich dokumentierte menschliche Freigabe für die konkrete Fassung voraus. [Kanzleialltag](../references/kanzleialltag-workflows.md).
