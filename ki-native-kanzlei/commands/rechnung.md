---
description: "Rechnung oder E-Rechnung aus Honorarstand und Zeitstand entwerfen und Gate G4 öffnen."
argument-hint: "Akte und Abrechnungszeitraum"
---

Führe den Ablauf aus Abschnitt 1.12 mit dem Skill abrechnung-e-rechnung aus. Erstelle die Berechnung nach § 10 RVG, bestimme Leistungsempfänger und Format, führe auf Stufe 2 den internen `rechnung`-Entwurf fort. Das ausgabefertige Paket mit `rechnung-xml` entsteht ab Stufe 3. Öffne G4 mit registrierter Produktkennung oder Manifest; endgültige Nummer und Hash gehören zur später freizugebenden Fassung.

Eingabe: $ARGUMENTS

Lies zuerst den Mandatslauf mit `python3 "<Pluginordner>/scripts/mandatslauf.py" status --akte "<Akte>"` oder den letzten Textstatus. Bei mehreren Akten lies deren Status einzeln; ohne vorhandenen Lauf kläre Akten-ID und Stufe, bevor du ihn anlegst. Übernimm führende Fassungen, Fristobjekte, Honorar- und Zeitstand; frage nur entscheidende neue Angaben ab. Arbeite innerhalb der Stufe weiter und schließe mit dem Statusblock nach [Mandatslauf, Abschnitt 1.11](../references/mandatslauf-und-freigaben.md): Phase, Produkte mit Pfad/Hash oder Textfassung, Friststatus, Honorar, bestätigte Minuten, offene Gates mit zuständiger Person, offene Fragen und nächstes Produkt. Nicht berechnete Hashes oder fehlende Namen bleiben offen. G2 hat Vorrang; unabhängige interne Arbeit bleibt möglich. Außenwirkung setzt eine tatsächlich erklärte, namentlich dokumentierte menschliche Freigabe für die konkrete Fassung voraus. [Kanzleialltag](../references/kanzleialltag-workflows.md).
