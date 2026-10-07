---
description: "Rechnung oder E-Rechnung aus Honorarstand und Zeitstand entwerfen und Gate G4 öffnen."
argument-hint: "Akte und Abrechnungszeitraum"
---

Führe den Ablauf aus Abschnitt 1.12 mit dem Skill abrechnung-e-rechnung aus. Erstelle die Berechnung nach § 10 RVG, bestimme Leistungsempfänger und Format, erzeuge bei Bedarf mit `xrechnung.py` einen XML-Entwurf und öffne G4 mit dem Hash des Entwurfs.

Eingabe: $ARGUMENTS

Lies zuerst den Mandatslauf (`scripts/mandatslauf.py status` oder den Textblock im letzten Übergabevermerk), die führenden Fassungen, offene Gates, offene Fragen, Honorarstand und Zeitstand. Arbeite innerhalb der gesetzten Freigabestufe selbständig und schließe mit drei Sätzen: führende Fassung mit Pfad, Gate mit wartender Person, offene Frage. Versand, Einreichung, Kalenderbestätigung, Rechnungsausgabe, Auszahlung, Dienstleisterzugang, Meldung und Löschung sind Gates und werden nur vorbereitet. Ablauf im Einzelnen: [Kanzleialltag](../references/kanzleialltag-workflows.md).
