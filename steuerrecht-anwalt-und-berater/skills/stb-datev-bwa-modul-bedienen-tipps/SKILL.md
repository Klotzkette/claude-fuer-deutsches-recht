---
name: stb-datev-bwa-modul-bedienen-tipps
description: "DATEV Kanzlei-Rechnungswesen BWA-Modul Bedienung. Anwendungsfall Erstellung BWA in DATEV Auswahl Form Konfiguration Periodenvergleich Branchenvergleich. Methodik Workflow-Tipps. Output BWA-konfiguriert."
---

# DATEV Kanzlei-Rechnungswesen BWA-Modul — Bedienung

## Kernsachverhalt

DATEV Kanzlei-Rechnungswesen ist die zentrale Steuerberater-Software fuer Buchfuehrung, BWA, SuSa, Jahresabschluss. Das BWA-Modul bietet zahlreiche Standardforms (BWA 01, 11, 21), Branchenanpassungen und individuelle Konfigurations-Moeglichkeiten ueber Berater-Stammdaten. Der Steuerberater nutzt Standardformen, passt sie bei Bedarf an und integriert Branchenvergleich (BBE).

## Kaltstart-Rueckfragen

1. Welche DATEV-Version (jaehrliche Updates)?
2. Welche BWA-Form ist aktuell konfiguriert?
3. Welche Branche?
4. Welche Auswertungsfrequenz?
5. Welche individuellen Anpassungen vorgenommen?
6. Welche Berater-Sicht-Konfiguration?
7. Welche Mandanten-Sicht (Mandantensicht-Filter)?
8. Welche Exportformate (PDF, Excel)?

## Workflow

### Phase 1 — Standardformen kennen

| Form | Verwendung |
|---|---|
| BWA 01 | Standard-BWA fuer 90 Prozent aller Mandanten |
| BWA 11 | Bewegungs-BWA mit detailliertem Vormonatsvergleich |
| BWA 21 | Branchen-BWA mit Branchenvergleich |
| BWA 31 | Kostenstellen-BWA |
| BWA 41 | Liquiditaets-BWA |
| BWA 51 | Statistische BWA |

### Phase 2 — Konfiguration

- Berater-Stammdaten: Mandantengruppen und BWA-Stammvorlagen zentral pflegen (typischer Programmpfad `Bestand → Berater-Stammdaten → BWA-Konfiguration`; exakter Pfad in aktueller DATEV-Programmversion ggf. abweichend).
- Mandantenstammdaten: BWA-Form-Zuordnung pro Mandant unter `Mandantenstammdaten → Auswertungen → BWA`.
- Periodenvergleich: Vorjahresdaten automatisch bei vorhandener Historie; Planwerte ueber `Auswertungen → Plan-Erfassung`.

### Phase 3 — Branchenvergleich

- Branchenschluessel (WZ-Code 2008) im Mandantenstamm hinterlegen.
- BBE-Branchen-Abonnement der DATEV nutzen (Aktualisierung jaehrlich).
- BWA 21 zeigt direkt Branchenmittel; Branchenbericht separat als PDF/Excel.

### Phase 4 — Individualisierung

- Eigene BWA-Form ueber Berater-Stammdaten anlegen (Kopie einer Standard-Form als Ausgangsbasis empfohlen).
- Konten-Zuordnung manuell definieren — pro Konto bzw. Kontenintervall.
- Spalten frei konfigurieren: Plan, Ist, Vorjahr, Vorjahres-kumuliert, Abweichung absolut/prozentual.

### Phase 5 — Ausgabe

- PDF-Export mit Mandanten-Briefkopf ueber das Druckmodul.
- Excel-Export fuer Detailauswertung (Pivot-fhaeig).
- DUO-Versand: BWA wird direkt in das DUO-Postfach des Mandanten gestellt (`Auswertungen → BWA → Versand an DUO`).

### Phase 6 — Updates

- Jaehrliche DATEV-Programm-Updates zum 1. Januar (LSt/SV-Tabellen, USt-Saetze, AfA-Tabellen, neue gesetzliche Pflichtmeldungen).
- Bei groesseren Reformen unterjaehrige Updates (Wachstumschancengesetz, eRechnung-Verfahren).
- Berater-Funktion Updates manuell pruefen, da individuelle Formen nicht automatisch migriert werden.

## Output

- Konfigurierte DATEV-BWA.
- Standard-Vorlagen.
- Branchen-Vergleich.

## Strategie und Praxis-Tipps

- BWA 21 fuer alle BWA-Mandanten mit Branchen-Wunsch.
- Individuelle BWA nur bei besonderem Bedarf — Standard-Form deckt 90 Prozent ab.
- Berater-Stammdaten zentral pflegen — vereinheitlicht Kanzleibetrieb.
- DATEV-Schulungen empfehlenswert (DATEV-Akademie).

## Querverweise

- `stb-bwa-aufbau-grundlagen` — BWA.
- `stb-bwa-branchenvergleich-bbe-datev` — Branchenvergleich.
- `stb-bwa-kontenrahmen-skr03-skr04` — Kontenrahmen.

## Quellen und Updates

Stand: 05/2026.

- DATEV Kanzlei-Rechnungswesen Bedienungs-Dokumentation (aktuelle Version pruefen).
- DATEV-Programm-Updates jaehrlich (Stand 01.01.) sowie unterjaehrige Reform-Updates.
- AO § 146 (Update-Pflicht der Buchfuehrungsprogramme).
- Verifikations-Hinweis: konkrete Programmpfade und Form-Nummern ggf. abweichend in aktueller DATEV-Version.
