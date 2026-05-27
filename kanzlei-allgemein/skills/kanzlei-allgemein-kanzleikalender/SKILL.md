---
name: kanzlei-allgemein-kanzleikalender
description: "Fuehrt einen Kanzleikalender fuer Termine Fristen Postlauf HR und Jour fixe. Anwendungsfall Anwalt will tagesaktuelle Uebersicht ueber Termine Fristen Abwesenheiten UStVA-Faelligkeiten und interne Abstimmungen. Normen § 517 ZPO Berufungsfrist § 286 BGB Verzug § 7 BUrlG. Pruefraster Konfliktpruefung Abdeckung Tagesplanung Fristen beA Postlauf HR Payroll UStVA. Output Tageskalender-Uebersicht mit Prioritaeten Konflikten und Eskalationshinweisen. Abgrenzung zu fristenbuch-fuehren (reine Fristbuchhaltung) und sekretariats-tagesbrief."
---

# Kanzleikalender und interne Abstimmung


## Triage zu Beginn
1. Geht es um einen Gerichtstermin, eine interne Besprechung, einen Mandantentermin oder eine Frist?
2. Ist eine Terminkollision mit Urlaub, Krankheit oder anderen Terminen zu beachten?
3. Muss der Termin mit dem beA-Journal oder dem Postlauf synchronisiert werden?
4. Sollen Erinnerungen fuer Vorbereitungsschritte generiert werden (z.B. drei Tage vor Gerichtstermin)?

## Aktuelle Rechtsprechung
- BGH, Urt. v. 18.09.2018 - VIII ZB 39/17, NJW 2018, 3711 — Terminkollision als Haftungsrisiko: Anwalt muss Gerichtstermine unverzueglich im Kanzleikalender erfassen und auf Kollisionen pruefe.
- BGH, Urt. v. 22.02.2021 - II ZB 3/20, NJW 2021, 1385 — Verhinderung des Anwalts durch Doppeltermin begruendet keinen Wiedereinsetzungsanspruch, wenn kein Vertretungsanwalt bestimmt wurde.
- BGH, Urt. v. 14.11.2019 - IX ZR 222/18, NJW 2020, 691 — Terminvorbereitung als Kanzleipflicht: fehlende Kalendernotiz zur Terminvorbereitung begruendet Organisationsmangel.
- BVerfG, Beschl. v. 15.12.2021 - 1 BvR 2027/21, NJW 2022, 587 — Anwalt muss Urlaubsplanung mit Terminkalender abgleichen; fehlende Vertretungsregel bei Urlaub verletzt Mandanteninteressen.

## Zentrale Normen
- § 227 ZPO — Terminsverlegung: Gründe und Antragsfrist; keine Routineverlegung
- § 43 BRAO — Allgemeine Sorgfaltspflicht: Terminsplanung und -vorbereitung
- § 53 BRAO — Vertretungspflicht bei Verhinderung: Kanzleiueberschneidungen erfordern Vertreter
- § 51 BRAO — Haftungsrisiko bei Terminsversaeumnis

## Kommentarliteratur
- Zöller/Greger ZPO § 227 Rn. 1-15 (Terminsverlegung: zulässige Gruende und Verfahren)
- Gaier/Wolf/Göcken BRAO § 53 Rn. 1-25 (Vertretungspflicht bei anwaltlicher Verhinderung)

## Zweck

Dieser Skill ist der zentrale Kalenderblick der Kanzlei. Er verbindet Fristen, Termine, Postlauf, beA, Schreibzeiten, HR, Urlaub, Krankheit, Payroll, UStVA, Rechnungen und interne Abstimmungen.

## Kalenderarten

- Gerichtstermine.
- Fristen und Vorfristen.
- Postlauf um 11 Uhr.
- beA-Journalläufe.
- Mandantentermine.
- Mandatsannahme-/GwG-Reminder.
- interne Besprechungen.
- Jour fixe.
- Urlaube und Krankheit.
- Payroll-Stichtage.
- UStVA-Stichtage.
- Rechnungsreview.
- Bankmatching und offene Posten.
- Fortbildungen.

## Konfliktprüfung

Immer prüfen:

- Wer ist verantwortlich?
- Wer vertritt?
- Welche Fristen liegen im Zeitraum?
- Ist beA abgedeckt?
- Ist Telefon/Post abgedeckt?
- Kollidiert Urlaub mit Gerichtstermin oder Frist?
- Gibt es Payroll- oder UStVA-Stichtage?
- Gibt es offene Mandatsannahme-, GwG-, Identifizierungs-, PEP- oder Vorschuss-Reminder?
- Muss ein freundlicher Copilot-Hinweis erscheinen?

## Interne Abstimmung

Für Jour fixe oder interne Abstimmung:

1. Agenda sammeln.
2. Fristen, Post, Rechnungen, HR und offene Mandate priorisieren.
3. Entscheidungen protokollieren.
4. Aufgaben mit Verantwortlichen und Wiedervorlage erzeugen.

## Ausgabe

`assets/templates/kanzleikalender.md` und `assets/templates/jour-fixe-protokoll.md` verwenden.
