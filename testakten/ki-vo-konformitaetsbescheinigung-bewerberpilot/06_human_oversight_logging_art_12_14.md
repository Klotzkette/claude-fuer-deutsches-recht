# Human Oversight und Logging

Stand: 18.05.2026

## 1. Menschliche Aufsicht

TalentRank zeigt Recruitern Score, Ranggruppe, Muss-Kriterium-Flag und Erklärmerkmale an. Jede Ablehnung muss durch eine menschliche Person bestätigt werden. Das System erzwingt einen Prüfschritt:

1. Bewerbung öffnen.
2. Systemvorschlag anzeigen.
3. Recruiter bestätigt, korrigiert oder verwirft Vorschlag.
4. Bei Ablehnung muss mindestens ein menschlich geprüfter Grund gewählt oder frei begründet werden.
5. System speichert Entscheidung, Zeitpunkt, Nutzerkennung und Abweichung vom KI-Vorschlag.

## 2. UI-Hinweise

Jede Rankingansicht enthält:

- "Dieser Vorschlag ist keine Entscheidung."
- "Prüfen Sie Muss-Kriterien und Kontext selbst."
- "Niedrige Scores dürfen nicht automatisch zur Ablehnung führen."
- "Sensible Angaben dürfen nicht berücksichtigt werden."

## 3. Logging

| Ereignis | Inhalt | Aufbewahrung |
|---|---|---|
| Upload | Bewerbungs-ID, Zeitpunkt, Nutzer, Stellenprofil | 24 Monate |
| Scoring | Modellversion, Score, Erklärmerkmale, Datenversion | 24 Monate |
| Ansicht | Recruiter-ID, Zeitpunkt, Bewerbungs-ID | 18 Monate |
| Entscheidung | Status, menschliche Begründung, Abweichung vom Score | 24 Monate |
| Override | Grund, Freigabe, Kommentar | 24 Monate |
| Export | Empfänger, Zweck, Zeitpunkt | 24 Monate |

## 4. Teststand

Das Logging funktioniert im Release Candidate. Noch offen ist ein Praxistest mit 20 Recruitern, ob die Hinweise verstanden werden und ob niedrige Scores faktisch doch zu Nichtprüfung führen. Dieser Test ist für Juni 2026 geplant.

## 5. Bewertung

Art. 12 ist technisch weitgehend belegt. Art. 14 ist konzeptionell stark, aber ohne Nutzerakzeptanztest noch nicht final freigabereif.
