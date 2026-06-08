---
name: training-generativer-modelle-tdm-opt-out
description: "Training generativer Modelle mit Text, Bild, Musik, Code und Datenbanken: Text-und-Data-Mining, Rechtevorbehalt/Opt-out, Webcrawl, Lizenzpool, Datenherkunft, Beweislast und Risikovermerk für Modellanbieter und Unternehmensnutzer."
---

# Training generativer Modelle: TDM und Opt-out

## Einsatz

Anwendungsfall: ein Modell mit fremden Werken, Datenbanken, Bildern, Musik, Code oder Texten trainiert wurde oder wenn ein Unternehmen ein Modell einkauft und die Trainingsdatenrisiken verstehen muss.

## Prüffragen

1. Welche Werkarten: Text, Bild, Musik, Video, Code, Datenbank, wissenschaftliche Publikation?
2. Welche Quelle: Lizenz, eigene Daten, Webcrawl, Kundenupload, Datensatz, öffentliches Archiv?
3. Ist Text- und Data-Mining einschlägig?
4. Gab es einen wirksamen Rechtevorbehalt/Opt-out?
5. Wurde der Opt-out technisch erkannt und respektiert?
6. Können Trainingsdaten oder geschützte Sequenzen im Output reproduziert werden?
7. Gibt es Datenbankherstellerrechte?

## Risikomatrix

| Risiko | Beispiel | Abhilfe |
|---|---|---|
| ungeklärte Lizenz | fremder Bilddatensatz | Datensatz sperren, Lizenz nachziehen |
| Opt-out | maschinenlesbarer Vorbehalt | Crawler-Regel und Sperrprotokoll |
| Memorization | Output kopiert Passagen | Filter, Red-Team, Logging |
| Datenbankrecht | massenhafter Datenbankauszug | Rechteprüfung, Mengenanalyse |

## Output

Erstelle ein Memo mit:

- Datenquellenkarte;
- TDM-/Opt-out-Bewertung;
- Risikostufen;
- Nachforderungsliste an Anbieter;
- Entscheidung: nutzen, nachverhandeln, sperren, ersetzen.
