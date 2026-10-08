---
description: "Mandat oder Auftragsphase abschließen: Restfristen, Schlussrechnung, Fremdgeld, Herausgabe, Aufbewahrung und Abschlussbrief."
argument-hint: "Akte und Anlass der Beendigung"
---

Führe den Ablauf aus Abschnitt 1.14 mit dem Skill mandat-abschliessen aus. Öffne G3 für den Abschlussbrief und G8 für die Aufbewahrungs- und Löschentscheidung; die Phase abschluss folgt erst, wenn G4, G5 und G8 freigegeben oder begründet nicht erforderlich sind. Eine Ablehnung genügt nicht. Erzeuge `abschlussbrief` und `aufbewahrungsvermerk` schon als interne Vorbereitung, ohne Auszahlung oder Löschung zu behaupten.

Eingabe: $ARGUMENTS

Lies zuerst den Mandatslauf mit `python3 "<Pluginordner>/scripts/mandatslauf.py" status --akte "<Akte>"` oder den letzten Textstatus. Bei mehreren Akten lies deren Status einzeln; ohne vorhandenen Lauf kläre Akten-ID und Stufe, bevor du ihn anlegst. Übernimm führende Fassungen, Fristobjekte, Honorar- und Zeitstand; frage nur entscheidende neue Angaben ab. Arbeite innerhalb der Stufe weiter und schließe mit dem Statusblock nach [Mandatslauf, Abschnitt 1.11](../references/mandatslauf-und-freigaben.md): Phase, Produkte mit Pfad/Hash oder Textfassung, Friststatus, Honorar, bestätigte Minuten, offene Gates mit zuständiger Person, offene Fragen und nächstes Produkt. Nicht berechnete Hashes oder fehlende Namen bleiben offen. G2 hat Vorrang; unabhängige interne Arbeit bleibt möglich. Außenwirkung setzt eine tatsächlich erklärte, namentlich dokumentierte menschliche Freigabe für die konkrete Fassung voraus. [Kanzleialltag](../references/kanzleialltag-workflows.md).

Im Textmodus gilt dieselbe Phasensperre: Solange G4, G5 oder G8 offen oder abgelehnt ist, bleibt der formale Phasenwert bei der bisherigen Bearbeitung, etwa `zahlung`. Der Abschlussentwurf kann bereits vorliegen.
