---
name: gebrauchsmuster-patent-patentrechts
description: "Gebrauchsmuster Patent Patentrechts: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Gebrauchsmuster Patent Patentrechts

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Gebrauchsmuster Patent Patentrechts** im Plugin Patentrecht (Verfahren, Verletzung). Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `gebrauchsmuster-oder-patent-route` | Prüft strategisch Patent, Gebrauchsmuster, EP/PCT, Geheimhaltung, defensive Veröffentlichung oder keine Anmeldung; berücksichtigt Offenbarung, Geschwindigkeit, Kosten, Technikart und Zielmärkte. |
| `internationaler-patentrechts-und-laendercheck` | Routet grenzüberschreitende Patentmandate nach DE, EP, UPC, PCT, USA, Kanada, Japan, Schweiz, UK, Türkei und Israel; trennt Recherche, Anmeldung, Rechtsstand, Verletzung, Rechtsbestand und lokale Counsel-Fragen. |
| `israel-patentrecht-ilpo-opposition-revocation` | Prüft israelische Patentfragen: ILPO-Register, Examination, Opposition vor Erteilung, Revocation/Cancellation, Verletzung, einstweilige Maßnahmen und technologiebezogene Counsel-Fragen. |

## Arbeitsweg

Im Plugin Patentrecht (Verfahren, Verletzung) gilt für **Gebrauchsmuster Patent Patentrechts**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `gebrauchsmuster-oder-patent-route`

**Fokus:** Prüft strategisch Patent, Gebrauchsmuster, EP/PCT, Geheimhaltung, defensive Veröffentlichung oder keine Anmeldung; berücksichtigt Offenbarung, Geschwindigkeit, Kosten, Technikart und Zielmärkte.

# Gebrauchsmuster oder Patent

## Entscheidungsparameter

| Frage | Bedeutung |
| --- | --- |
| Wie schnell braucht der Mandant Schutz? | Gebrauchsmuster kann schnell eingetragen sein; Patentprüfung dauert länger. |
| Welche Technik? | Verfahren sind für Gebrauchsmuster besonders kritisch; konkrete Schutzfähigkeit prüfen. |
| Welche Länder? | Gebrauchsmuster ist territorial begrenzt; EP/PCT kann Internationalisierung vorbereiten. |
| Wurde schon veröffentlicht? | Neuheitsschonfrist nur sehr vorsichtig und normgenau prüfen. |
| Wie streitfest soll es sein? | Geprüftes Patent wirkt anders als ungeprüftes Gebrauchsmuster. |
| Wie hoch ist das Budget? | Route muss Kosten, Fristen und Business-Ziel abbilden. |

## Pfade

1. **Deutsche Patentanmeldung:** klassischer Schutz, später EP/PCT-Priorität möglich.
2. **EP-Anmeldung:** breiter europäischer Schutz, Prüfungsverfahren und Validierung/Einheitspatent beachten.
3. **PCT:** internationale Option sichern, keine weltweite Patenterteilung.
4. **Gebrauchsmuster:** schneller Registerschutz, aber ungeprüft und nicht für jede Technik passend.
5. **Geheimhaltung:** wenn Reverse Engineering schwer und Offenbarung schädlich wäre.
6. **Defensive Veröffentlichung:** wenn Schutz nicht gesucht wird, aber Dritten Patentierung erschwert werden soll.

## Output

- Entscheidungsmatrix.
- Fristenplan.
- Kosten-/Nutzenhinweise ohne Scheingenauigkeit.
- Empfehlung mit Alternativroute.

## Normen und Trade-offs

- **Patent vs. Gebrauchsmuster (§§ 1, 3 ff. PatG vs. §§ 1, 3 GebrMG):**
 - Patent: erfinderische Tätigkeit (§ 4 PatG, "erfinderischer Schritt" beim GebrM gemäß § 1 GebrMG ist materiell ähnlich, aber Maßstab wurde durch BGH "Demonstrationsschrank" GRUR 2006, 842 stärker an Patent-Maßstab gerückt).
 - Patent: 20 Jahre Schutzdauer (§ 16 PatG); Gebrauchsmuster: max. 10 Jahre (§ 23 GebrMG).
 - Patent: geprüft, daher rechtsbeständig; Gebrauchsmuster: ungeprüft, im Verletzungsprozess Streit über Schutzfähigkeit.
- **Neuheitsschonfrist:** § 3 Abs. 1 GebrMG kennt 6-Monats-Schonfrist für Offenbarung durch Anmelder/Vorgänger; § 3 PatG kennt KEINE allgemeine Schonfrist (Ausnahme § 3 Abs. 5 PatG: missbräuchliche Offenbarung, Schau iSd Pariser Übereinkunft). USA: 12 Monate Grace Period (35 U.S.C. § 102(b)). EP: keine allgemeine Schonfrist.
- **Verfahrensanmeldungen:** Reine Verfahren sind nach § 2 Nr. 3 GebrMG NICHT gebrauchsmusterfähig — nur Patent.
- **Strategie:** Doppelschutz (Patent + Gebrauchsmuster) durch Abzweigung (§ 5 GebrMG) bis 10 Jahre nach Patentanmeldung möglich.
- Falle: Vor Anmeldung öffentliche Vorführung — bei Patent neuheitsschädlich, bei Gebrauchsmuster nur, wenn vom Anmelder/Rechtsvorgänger ausgehend und älter als 6 Monate.


## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.

## 2. `internationaler-patentrechts-und-laendercheck`

**Fokus:** Routet grenzüberschreitende Patentmandate nach DE, EP, UPC, PCT, USA, Kanada, Japan, Schweiz, UK, Türkei und Israel; trennt Recherche, Anmeldung, Rechtsstand, Verletzung, Rechtsbestand und lokale Counsel-Fragen.

# Internationaler Patent- und Ländercheck

## Aufgabe

Master-Routing für internationale Patentfragen: Territorien, Patentfamilie, Priorität, PCT/Nationalphasen, Validierungen, Einheitspatent, UPC-Opt-out, nationale Verletzungs- und Nichtigkeitsrisiken.

## Einstieg

Frage zu Beginn nur die Punkte ab, die für die nächste irreversible Entscheidung gebraucht werden:

1. Welche Rolle hat der Nutzer: Anmelder, Patentinhaber, Angreifer, Beklagter, Investor, Vertrieb, Lizenznehmer oder Local Counsel?
2. Welche Schutzrechte, Produkte, Länder und Fristen sind betroffen?
3. Liegen Patentnummern, Registerauszüge, Anspruchsfassungen, Prior-Art-Treffer, Abmahnung, Klage, Office Action oder Vertragsentwurf vor?
4. Braucht der Nutzer deutschen Output, englischen Output oder eine zweisprachige Fassung?

## Arbeitsworkflow

1. **Territorien und wirtschaftliche Märkte priorisieren.**
2. **Patentfamilie, Prioritäten, Anmelder- und Inhaberkette erfassen.**
3. **Pro Land trennen: Schutzfähigkeit, Rechtsstand, Verletzung, Rechtsbestand, Durchsetzung, Kosten.**
4. **Live-Register definieren: DPMA, EPO Register, Espacenet, WIPO PATENTSCOPE, USPTO, CIPO, J-PlatPat, Swissreg, UKIPO, TURKPATENT, ILPO.**
5. **Lokale Counsel-Fragen und Übersetzungsbedarf ausgeben.**


## Prüfmatrix

| Ebene | Prüffrage | Ergebnis |
| --- | --- | --- |
| Schutzrecht | Welche Anspruchsfassung, welcher Status, welche Priorität und welche Territorien? | Register live prüfen; Annahmen markieren. |
| Technik | Welche Merkmale, Varianten, Ausführungsformen und Belege sind wirklich tragend? | Merkmalsgliederung/Claim Chart. |
| Verfahren | Welches Forum, welche Frist, welche Sprache, welche Verfahrensart? | Forum- und Fristenampel. |
| Rechtsbestand | Welche Angriffe tragen realistisch und welche Belege fehlen? | Invalidity-/Opposition-Map. |
| Strategie | Was ist wirtschaftlich sinnvoll: Angriff, Verteidigung, Design-around, Lizenz, Vergleich? | Handlungsempfehlung. |

## Output

Erzeuge je nach Auftrag:

- Ländermatrix.
- Register-Rechercheplan.
- Local-Counsel-Fragenkatalog.
- Risikomemo DE/EN.


## Anschluss-Skills

- `internationaler-patentrechts-und-laendercheck`, wenn weitere Länder oder Patentfamilien betroffen sind.
- `stand-der-technik-recherche-workflow` und das Schwesterplugin `patentrecherche`, wenn Datenbankrecherche erforderlich ist.
- `patentrecht-redteam-qualitygate`, bevor ein Ergebnis nach außen geht.

## Quellenregel

Keine erfundenen Registerstände, Fristen oder ausländischen Rechtsaussagen. Für Status und Verfahrensdaten immer amtliche Register oder aktuelle Local-Counsel-Informationen verwenden. Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle ausgeben; sonst als zu verifizieren markieren.

## 3. `israel-patentrecht-ilpo-opposition-revocation`

**Fokus:** Prüft israelische Patentfragen: ILPO-Register, Examination, Opposition vor Erteilung, Revocation/Cancellation, Verletzung, einstweilige Maßnahmen und technologiebezogene Counsel-Fragen.

# Israel: ILPO, Opposition und Revocation

## Aufgabe

Israelisches Patentrecht mit starker High-Tech-/MedTech-Relevanz und Register-/Opposition-Fokus.

## Einstieg

Frage zu Beginn nur die Punkte ab, die für die nächste irreversible Entscheidung gebraucht werden:

1. Welche Rolle hat der Nutzer: Anmelder, Patentinhaber, Angreifer, Beklagter, Investor, Vertrieb, Lizenznehmer oder Local Counsel?
2. Welche Schutzrechte, Produkte, Länder und Fristen sind betroffen?
3. Liegen Patentnummern, Registerauszüge, Anspruchsfassungen, Prior-Art-Treffer, Abmahnung, Klage, Office Action oder Vertragsentwurf vor?
4. Braucht der Nutzer deutschen Output, englischen Output oder eine zweisprachige Fassung?

## Arbeitsworkflow

1. **ILPO-Status, Priorität und Patentfamilie prüfen.**
2. **Pre-grant opposition und post-grant revocation/cancellation unterscheiden.**
3. **Verletzungs- und Eilrechtsschutzroute über lokale Counsel vorbereiten.**
4. **Technische Belege, Produktvergleich und Geschäftsgeheimnisse sichern.**
5. **DE/EN Counsel Brief und Mandantenampel erstellen.**


## Prüfmatrix

| Ebene | Prüffrage | Ergebnis |
| --- | --- | --- |
| Schutzrecht | Welche Anspruchsfassung, welcher Status, welche Priorität und welche Territorien? | Register live prüfen; Annahmen markieren. |
| Technik | Welche Merkmale, Varianten, Ausführungsformen und Belege sind wirklich tragend? | Merkmalsgliederung/Claim Chart. |
| Verfahren | Welches Forum, welche Frist, welche Sprache, welche Verfahrensart? | Forum- und Fristenampel. |
| Rechtsbestand | Welche Angriffe tragen realistisch und welche Belege fehlen? | Invalidity-/Opposition-Map. |
| Strategie | Was ist wirtschaftlich sinnvoll: Angriff, Verteidigung, Design-around, Lizenz, Vergleich? | Handlungsempfehlung. |

## Output

Erzeuge je nach Auftrag:

- Israel Patent Status Note.
- Opposition/Revocation Matrix.
- Infringement Evidence List.
- Local Counsel Brief.


## Anschluss-Skills

- `internationaler-patentrechts-und-laendercheck`, wenn weitere Länder oder Patentfamilien betroffen sind.
- `stand-der-technik-recherche-workflow` und das Schwesterplugin `patentrecherche`, wenn Datenbankrecherche erforderlich ist.
- `patentrecht-redteam-qualitygate`, bevor ein Ergebnis nach außen geht.

## Quellenregel

Keine erfundenen Registerstände, Fristen oder ausländischen Rechtsaussagen. Für Status und Verfahrensdaten immer amtliche Register oder aktuelle Local-Counsel-Informationen verwenden. Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle ausgeben; sonst als zu verifizieren markieren.
