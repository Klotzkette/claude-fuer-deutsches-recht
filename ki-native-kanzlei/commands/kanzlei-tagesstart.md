---
description: "Tagesstart der Kanzlei: alle Mandate nach Dringlichkeit ordnen, Posteingang zuordnen, Fristauslöser erfassen und den Tagesbericht liefern."
argument-hint: "Kanzleiordner und gegebenenfalls Posteingangsordner"
---

Führe den Ablauf Tagesstart aus Abschnitt 1.3 der Kanzleialltag-Referenz aus. Erzeuge mit `scripts/mandatslauf.py cockpit --kanzlei <Kanzleiordner> --format md` die Mandatsübersicht, ordne neue Posteingänge einer Akte zu, erfasse Fristauslöser als Fristobjekte und übergib sie an den Skill fristen-berechnen-ueberwachen. Liefere den Tagesbericht mit Fristen, wartenden Gates und offenen Fragen.

Eingabe: $ARGUMENTS

Lies zuerst den Mandatslauf (`scripts/mandatslauf.py status` oder den Textblock im letzten Übergabevermerk), die führenden Fassungen, offene Gates, offene Fragen, Honorarstand und Zeitstand. Arbeite innerhalb der gesetzten Freigabestufe selbständig und schließe mit drei Sätzen: führende Fassung mit Pfad, Gate mit wartender Person, offene Frage. Versand, Einreichung, Kalenderbestätigung, Rechnungsausgabe, Auszahlung, Dienstleisterzugang, Meldung und Löschung sind Gates und werden nur vorbereitet. Ablauf im Einzelnen: [Kanzleialltag](../references/kanzleialltag-workflows.md).
