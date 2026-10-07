---
description: "Zahlungseingänge zuordnen, Fremdgeld trennen und Buchungsvorschläge erstellen; Auszahlungen über Gate G5."
argument-hint: "Kontoauszug oder Zahlungsavis"
---

Führe den Ablauf aus Abschnitt 1.12 mit dem Skill zahlungen-buchhaltung aus. Ordne mit Tilgungsbestimmung zu, buche belegte Eingänge mit `kanzlei.py payment`, halte Fremdgeld getrennt und öffne G5 für jede Auszahlung, Verrechnung oder Weiterleitung.

Eingabe: $ARGUMENTS

Lies zuerst den Mandatslauf (`scripts/mandatslauf.py status` oder den Textblock im letzten Übergabevermerk), die führenden Fassungen, offene Gates, offene Fragen, Honorarstand und Zeitstand. Arbeite innerhalb der gesetzten Freigabestufe selbständig und schließe mit drei Sätzen: führende Fassung mit Pfad, Gate mit wartender Person, offene Frage. Versand, Einreichung, Kalenderbestätigung, Rechnungsausgabe, Auszahlung, Dienstleisterzugang, Meldung und Löschung sind Gates und werden nur vorbereitet. Ablauf im Einzelnen: [Kanzleialltag](../references/kanzleialltag-workflows.md).
