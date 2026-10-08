---
description: "Schriftsatz vom Entwurf bis zum beA-Versandpaket führen, mit Fristvorrang, Fehlerkatalog und Gate G3."
argument-hint: "Akte, Art des Schriftsatzes, Auftrag"
---

Führe den Ablauf aus Abschnitt 1.7 aus: Fristgate prüfen, recht-recherchieren für tragende Rechtsfragen, schriftsaetze-entwerfen für den vollständigen Text, ab Stufe 3 bea-anlagen-vorbereiten für das Versandpaket. Auf Stufe 2 liefere den vollständigen Entwurf unter seiner konkreten Produktkennung, etwa `einspruch`, und benenne `versandpaket` als Folgeprodukt. Öffne G3 erst für die vorhandene, registrierte Paketfassung und frage die tatsächlichen Minuten ab.

Eingabe: $ARGUMENTS

Lies zuerst den Mandatslauf mit `python3 "<Pluginordner>/scripts/mandatslauf.py" status --akte "<Akte>"` oder den letzten Textstatus. Bei mehreren Akten lies deren Status einzeln; ohne vorhandenen Lauf kläre Akten-ID und Stufe, bevor du ihn anlegst. Übernimm führende Fassungen, Fristobjekte, Honorar- und Zeitstand; frage nur entscheidende neue Angaben ab. Arbeite innerhalb der Stufe weiter und schließe mit dem Statusblock nach [Mandatslauf, Abschnitt 1.11](../references/mandatslauf-und-freigaben.md): Phase, Produkte mit Pfad/Hash oder Textfassung, Friststatus, Honorar, bestätigte Minuten, offene Gates mit zuständiger Person, offene Fragen und nächstes Produkt. Nicht berechnete Hashes oder fehlende Namen bleiben offen. G2 hat Vorrang; unabhängige interne Arbeit bleibt möglich. Außenwirkung setzt eine tatsächlich erklärte, namentlich dokumentierte menschliche Freigabe für die konkrete Fassung voraus. [Kanzleialltag](../references/kanzleialltag-workflows.md).

Wenn neben der Dokumenterstellung bereits die kontrollierte Einreichung beauftragt ist, führe nach der konkreten G3-Entscheidung mit [beA-Empfang und Versand](../references/bea-versand-empfang.md) weiter. Beachte den aktiven Computerlauf, Stufe 3, tatsächliche Rechte und Signaturweg. Den persönlichen Schlussakt nicht fingieren. Anschließend ordne den tatsächlichen gerichtlichen Eingangsbeleg dem richtigen Dokument und Fristobjekt zu; unklaren Ausgang zuerst klären.
