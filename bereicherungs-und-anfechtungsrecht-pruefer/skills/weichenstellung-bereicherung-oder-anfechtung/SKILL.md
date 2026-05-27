---
name: weichenstellung-bereicherung-oder-anfechtung
description: "Triage-Entscheidung: welcher Regelungskreis ist einschlaegig - Bereicherungsrecht, ausserinsolvenzliche Anfechtung oder Insolvenzanfechtung. Normen: §§ 812 ff. BGB, AnfG, §§ 129 ff. InsO. Pruefraster: Rechtsgrundmangel, Insolvenzeroffnung, vollstreckbarer Titel. Output: Weiterleitungsmatrix zum richtigen Pruef-Skill. Abgrenzung: kein inhaltlicher Anspruchsguetachter."
---

# Weichenstellung: Bereicherung oder Anfechtung?

## Triage — kläre vor der Weichenstellung

1. Besteht ein wirksamer Rechtsgrund für die Vermögensverschiebung (wirksamer Vertrag, gesetzliche Pflicht), oder fehlt er (nichtig, weggefallen)?
2. Ist über das Vermögen des Schuldners ein Insolvenzverfahren eröffnet oder beantragt?
3. Hat der Gläubiger einen vollstreckbaren Titel gegen den Schuldner (§ 2 AnfG)?
4. Hat die Zwangsvollstreckung nicht zur Befriedigung geführt (Fruchtlosigkeit als AnfG-Voraussetzung)?
5. Besteht noch Eigentum des Anspruchstellers am streitigen Gegenstand (§ 985 BGB vorrangig)?

## Zentrale Normen

§ 812 Abs. 1 BGB (Leistungskondiktion: kein Rechtsgrund) — §§ 129 ff. InsO (Insolvenzanfechtung: Verfahren eröffnet) — §§ 1–13 AnfG (Gläubigeranfechtung: Titel vorhanden, kein Insolvenzverfahren) — § 985 BGB (Vindikation: Eigentum noch vorhanden) — § 17 InsO (Zahlungsunfähigkeit) — § 2 AnfG (Titel + Fruchtlosigkeit) — § 826 BGB (sittenwidrige Schädigung, Konkurrenz)

## Rechtsprechung

BGH, Urt. v. 25.02.1999 – IX ZR 30/98, NJW 1999, 1704 — Ist der Rechtsgrund für die Vermögensverschiebung von Anfang an nicht entstanden oder nachträglich weggefallen, ist § 812 Abs. 1 S. 1 BGB die einschlägige Anspruchsgrundlage; Anfechtungsrecht setzt dagegen einen (zunächst) wirksamen Rechtsgrund voraus.

BGH, Urt. v. 12.07.2007 – IX ZR 235/03, NJW 2007, 3069 — Mit Eröffnung des Insolvenzverfahrens (§ 27 InsO) ist das Anfechtungsrecht nach §§ 1 ff. AnfG für den Einzelgläubiger ausgeschlossen; an die Stelle tritt das Recht des Insolvenzverwalters nach §§ 129 ff. InsO.

BGH, Urt. v. 07.07.2005 – IX ZR 221/04, NJW 2005, 2983 — Das AnfG setzt als unverzichtbare Voraussetzung einen vollstreckbaren Titel (§ 2 AnfG) und die fruchtlose Zwangsvollstreckung voraus; fehlt der Titel, ist die Anfechtungsklage nach AnfG unzulässig.

BGH, Urt. v. 19.01.2012 – IX ZR 2/11, NJW 2012, 1209 — § 985 BGB ist vorrangig gegenüber § 812 BGB, solange das Eigentum des Anspruchstellers besteht; erst nach Eigentumsübergang (z. B. gutgläubiger Erwerb) ist § 812 BGB einschlägig.

## Kommentarliteratur

Lorenz in: Staudinger, BGB, Neubearbeitung 2023, § 812 Rn. 1–30 (Abgrenzung Bereicherungsrecht / Anfechtungsrecht).
Kayser in: MüKoInsO, 4. Aufl. 2023, § 129 Rn. 1–20 (Abgrenzung InsO-Anfechtung / AnfG / § 812 BGB).
Huber in: AnfG, 12. Aufl. 2022, § 1 Rn. 1–30, § 2 Rn. 1–25 (Titelerfordernis, Abgrenzung zu InsO).

## Weichenstellungs-Schema

### Frage 1: Liegt ein Rechtsgrund für die Vermögensverschiebung vor?

**Kein Rechtsgrund** (Vertrag nichtig, nie zustande gekommen, weggefallen):
→ Bereicherungsrecht §§ 812 ff. BGB.
→ Skill: `leistungskondiktion-grundtatbestand-812-i-1-alt-1`

**Rechtsgrund vorhanden** (wirksamer Vertrag, gesetzliche Pflicht):
→ Weiter zu Frage 2.

### Frage 2: Ist ein Insolvenzverfahren eröffnet oder beantragt?

**Insolvenzverfahren eröffnet oder Antrag gestellt:**
→ Insolvenzanfechtung §§ 129 ff. InsO.
→ Skill: `inso-grundtatbestand-129-glaeubigerbenachteiligung`

**Kein Insolvenzverfahren:**
→ Weiter zu Frage 3.

### Frage 3: Liegt ein vollstreckbarer Titel vor?

**Vollstreckbarer Titel vorhanden** + fruchtlose Vollstreckung:
→ AnfG-Anfechtung (§ 2 AnfG).
→ Skill: `anfg-grundtatbestand-und-anfechtungsberechtigte`

**Kein Vollstreckungstitel:**
→ AnfG nicht unmittelbar anwendbar; Klage auf Leistung oder Feststellung prüfen.

## Kombinationen und Besonderheiten

- § 812 BGB und AnfG können nebeneinander stehen, wenn der Rechtsgrund nachträglich entfällt.
- Mit Insolvenzverfahren verdrängt § 129 InsO den AnfG-Pfad.
- § 133 InsO kann mit § 826 BGB konkurrieren.

## Merksatz

Kein Rechtsgrund → Bereicherungsrecht.
Rechtsgrund + kein Insolvenzverfahren + Titel → AnfG.
Rechtsgrund + Insolvenzverfahren → InsO-Anfechtung.

## Output-Template

**Weichenstellung: Bereicherung oder Anfechtung?**

Sachverhalt (kurz): [...]

| Frage | Antwort | Pfad |
|---|---|---|
| Rechtsgrund vorhanden? | nein → | § 812 BGB |
| Rechtsgrund vorhanden? | ja → Frage 2 | |
| Insolvenzverfahren eröffnet/beantragt? | ja → | §§ 129 ff. InsO |
| Kein Insolvenzverfahren, Titel vorhanden? | ja + fruchtlos → | AnfG (§ 2) |
| Eigentum noch vorhanden? | ja → | § 985 BGB (vorrangig) |

**Empfohlener Regelungskreis:** [...] → Weiter zu Skill: [...]

---

Hinweis: Keine Rechtsberatung. Mechanische Prüfung anhand vom Nutzer behaupteter Tatsachen. Falsche Normwahl oder unvollständiger Sachverhalt kann das Ergebnis vollständig entwerten.
