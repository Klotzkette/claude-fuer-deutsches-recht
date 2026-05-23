---
name: schulung-urteilsbauer
description: "Trainerleitfaden fuer Schulungen zum Plugin urteilsbauer-relationsmacher. Lernziele Stundenplan eine Tagesschulung und zwei Tage Praktische Uebungen anhand der Schulungsakte. Adressaten Proberichter/-innen Assessoren/-innen Rechtspfleger/-innen."
---

# Trainer-Leitfaden Schulung Urteilsbauer

Zielgruppe: Proberichter/-innen, Assessoren/-innen, Rechtspfleger/-innen.

## Lernziele

Die Teilnehmenden koennen am Ende

1. eine Zivilakte strukturiert intaken,
2. eine Relation aufbauen,
3. die einschlaegigen Anspruchsgrundlagen identifizieren,
4. CISG- und IPR-Probleme erkennen,
5. einen Beweisbeschluss vorbereiten,
6. eine Beweiswuerdigung schreiben (mit Eigenanteil),
7. Tenor, Tatbestand und Entscheidungsgruende formulieren,
8. ein vollstaendiges Urteil im offiziellen Layout ausgeben.

## Eintagesschulung

| Block | Skills |
| --- | --- |
| Akteintake und Relation | `aktenintake-zivil`, `relation-zivil`, optional `vollrelation-langfassung` |
| Zulaessigkeit und Anspruchsgrundlagen | `zulaessigkeit-pruefen`, `anspruchsgrundlagen-pruefen` |
| Internationales | `internationales-privatrecht`, `cisg-pruefen`, `kollidierende-agb-pruefen`, `incoterms-und-gefahruebergang` |
| Beweis | `beweisbeschluss-vorbereiten`, `beweiswuerdigung-mit-richter-input` |
| Urteil schreiben | `tenor-bauen-zivil`, `tatbestand-zivil-schreiben`, `entscheidungsgruende-zivil-schreiben` |
| Nebenentscheidungen | `kostenentscheidung-bauen`, `vorlaeufige-vollstreckbarkeit`, `rechtsmittelbelehrung-zivil` |
| Selbstkontrolle | `berufungsfest-pruefen`, `revisionsfest-pruefen` |
| Ausgabe | `dokumente-rendern-urteil-docx` |

## Zweitagesschulung

Tag 1 wie oben. Tag 2 vertieft die Schulungsakte `testakten/solis-vision-x-smartglasses/`:
- Vormittag: kollidierende AGB Schweizer Recht und EU-Recht; CISG-Anwendbarkeit ohne und mit ordnungsgemaessem Ausschluss
- Mittag: DSGVO als Eingriffsnorm und Auswirkung auf den Sachmangel
- Nachmittag: Beweiswuerdigung des Gutachtens; Schreiben des Urteilstenors und der Entscheidungsgruende; Render des DOCX

## Hinweis zur Pruefungstaeuschung

Im Trainerleitfaden zu Beginn jeder Schulung den Hinweis mitgeben: **Die hier ausgegebenen Relationen und Urteilsentwuerfe duerfen nicht in Klausuren des Vorbereitungsdienstes als eigene Arbeit eingereicht werden.** Es handelt sich um Schulungs- und Praxismaterial; die Eigenleistung der Teilnehmer/-innen ist nicht verzichtbar.

## Workflow-Entscheidungspunkte

Am Anfang **immer** vier Wahlfragen stellen:

1. **Relations-Stil**: Vollrelation Schulstandard (mit `vollrelation-langfassung`) oder Kurzrelation Praxisstandard (nur `relation-zivil`)?
2. **Dokumenttyp**: Urteil Versaeumnisurteil oder Beschluss?
3. **Ausgabeformat**: nur DOCX oder DOCX und PDF?
4. **Tenor-Variante**: Soll die wahrscheinliche Variante (A B oder C aus der Tenorierungsstation) gerendert werden oder eine bestimmte Variante?

Die Antworten werden im Akten-Workspace gespeichert (Datei `workflow-entscheidungen.yaml`) damit nachvollziehbar bleibt was geliefert wurde.

## Lernfallen in der Schulungsakte

1. Klaeger glaubt, deutsches Recht gelte - die AGB der Beklagten verweisen aber auf Schweizer Recht.
2. Beide AGB kollidieren - Knock-out Doktrin greift.
3. CISG ist anwendbar, auch ohne ausdruecklichen Ausschluss in beiden AGB.
4. Incoterm FOB Galway - Gefahruebergang dort, also vor Eintritt in die EU - aber DSGVO greift trotzdem nach Art. 3 II DSGVO.
5. Streitwert 1577 EUR - sachlich zustaendig AG nach Paragraf 23 Nr. 1 GVG.
6. Berufung waere ohne Zulassung nicht statthaft (Beschwer unter 600 EUR fuer Beklagte) - der Klaeger hat aber Beschwer ueber 600 EUR, also Berufung statthaft.
