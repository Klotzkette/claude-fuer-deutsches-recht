# Nachprüfungen zum ersten Strukturlauf

Der erste umfassende Lauf führte 88 Prüfkommandos aus. Drei meldeten einen Fehler: ein bloßer Domainname im Mini, während der Neuerzeugung noch alte Akten-URLs sowie zwölf direkte Markdown-Dateilinks im neuen README. Die Formulierung wurde bereinigt, die Kataloge vollständig neu erzeugt und die Downloadlinks auf den vorhandenen Downloadhandler umgestellt.

Anschließend wurden `audit-generated-prompt-hygiene.py`, `validate-testakten-readme-downloads.py` und `validate-readme-navigation.py` erneut erfolgreich ausgeführt. Die neuen Artikel-14-/Artikel-15-Tests des zwischenzeitlich übernommenen Hauptzweigs bestanden ebenfalls (25 und 16 Tests). Vor dem Push bestanden die vier vorgeschriebenen Prüfungen einschließlich Gesamt-PDF-Validierung sowie die erneut ausgeführte Dokumentqualitätsprüfung und das Qualitätsprofil-Audit. Die einzelnen Ergebnisse des ersten Laufs werden nicht nachträglich als ursprünglich bestanden umgeschrieben.
