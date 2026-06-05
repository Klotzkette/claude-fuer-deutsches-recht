---
name: force-majeure-geheimhaltung-nda
description: "Force Majeure Geheimhaltung NDA: bündelt 2 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Force Majeure Geheimhaltung NDA

## Arbeitsbereich

Dieser Skill bündelt 2 sachlich verwandte Arbeitsschritte rund um **Force Majeure Geheimhaltung NDA** im Plugin Word-Legal-AI für deutsche Anwälte. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `force-majeure-und-erschwerung-313-bgb` | Drafting und Abgrenzung von Force-Majeure-Klauseln und § 313 BGB (Wegfall der Geschäftsgrundlage). Strukturiert Definition höherer Gewalt, Anzeigepflicht, Suspendierung der Leistungspflicht und Kaskade bis zur Long-Stop-Kündigung. Klärt die Voraussetzungen des § 313 BGB (schwerwiegende Veränderung der Geschäftsgrundlage, kein vertraglich allokiertes Risiko, Vorrang der Anpassung vor Rücktritt) und grenzt COVID-Sonderkonstellationen von der allgemeinen Lage ab. |
| `geheimhaltung-nda-vertraulichkeit` | Drafting eines stand-alone NDA und einer Geheimhaltungsklausel als Vertragsbaustein. Strukturiert Definition der vertraulichen Information, Standardausnahmen (öffentlich bekannt, eigenständig entwickelt, von Dritten rechtmäßig erhalten, gesetzliche Offenlegungspflicht), Nutzungsbeschränkung, Pflichten zur Geheimhaltung, Dauer, Rückgabe und Löschung, Vertragsstrafe (mit Blick auf § 309 Nr. 6 BGB), Gerichtsstand und das Verhältnis zum GeschGehG mit der Pflicht zu angemessenen Geheimhaltungsmaßnahmen. |

## Arbeitsweg

Im Plugin Word-Legal-AI für deutsche Anwälte gilt für **Force Majeure Geheimhaltung NDA**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `force-majeure-und-erschwerung-313-bgb`

**Fokus:** Drafting und Abgrenzung von Force-Majeure-Klauseln und § 313 BGB (Wegfall der Geschäftsgrundlage). Strukturiert Definition höherer Gewalt, Anzeigepflicht, Suspendierung der Leistungspflicht und Kaskade bis zur Long-Stop-Kündigung. Klärt die Voraussetzungen des § 313 BGB (schwerwiegende Veränderung der Geschäftsgrundlage, kein vertraglich allokiertes Risiko, Vorrang der Anpassung vor Rücktritt) und grenzt COVID-Sonderkonstellationen von der allgemeinen Lage ab.

# Force Majeure und § 313 BGB (Wegfall der Geschäftsgrundlage)

## Zweck

Dieser Skill unterstützt Sie beim Drafting der Risikoallokation für außergewöhnliche Ereignisse. Force-Majeure-Klauseln (höhere Gewalt) regeln vertraglich, was geschieht, wenn eine Leistung wegen außerhalb der Sphäre liegender Ereignisse unmöglich oder unzumutbar wird. § 313 BGB greift dort, wo die Geschäftsgrundlage entfällt und keine vertragliche Risikoallokation existiert. Ein gutes Drafting trennt beides sauber und stellt die Reihenfolge klar.

## Eingaben

- Vertragstyp (Lieferung, Werkleistung, Dienstleistung, langfristiger Bezug).
- Lieferketten- und Logistik-Profil.
- Regelungsziel der Klausel (vollständige Allokation oder Hilfsregel?).
- Erwartete Ereignistypen (Naturereignisse, Pandemie, Krieg, Sanktionen, Streik, Cyberangriff, regulatorische Eingriffe).
- Mandatsumfeld (B2B oder B2C, internationale Lieferkette, INCOTERMS-Bezug).

## Rechtlicher und methodischer Rahmen

- **Vertragliche Risikoallokation:** Ohne Klausel greifen §§ 275 (Unmöglichkeit), 326 (Folgen), 313 BGB (Geschäftsgrundlage). Force Majeure ist kein gesetzlicher Begriff im BGB; die Klausel definiert ihn vertraglich.
- **§ 313 BGB:** Voraussetzungen sind (i) schwerwiegende Veränderung der Geschäftsgrundlage, (ii) hypothetischer Wille zum anderen Vertragsschluss bei Kenntnis, (iii) Unzumutbarkeit der Festhaltung, (iv) Risiko nicht vertraglich allokiert. Rechtsfolge ist Anpassung; Rücktritt nur, wenn Anpassung nicht möglich oder zumutbar (§ 313 III BGB).
- **Verhältnis zur Force-Majeure-Klausel:** Existiert eine ausdrückliche Klausel, geht sie als spezielle Risikoallokation der allgemeinen Regel des § 313 BGB grundsätzlich vor.
- **Anzeige- und Mitwirkungspflichten:** Eine Force-Majeure-Klausel sollte eine Anzeigepflicht mit Frist, Inhalt und Form regeln; Versäumnis kann zum Verlust der Berufung auf höhere Gewalt führen.
- **Folgen:** Suspendierung der Leistungspflicht für die Dauer des Ereignisses, kein Verzug, ggf. Rücktrittsrecht (Long Stop) nach festgelegter Dauer.
- **COVID-Erfahrung:** BGH hat zu Mietverträgen während Pandemie § 313 BGB herangezogen (Vertragsanpassung mit Halbierung der Miete nicht pauschal, sondern Einzelfall). Die Linie ist nicht auf alle Pandemiefolgen übertragbar; die Entscheidungen sind vom Nutzer fundstellengenau zu verifizieren.

## Ablauf / Checkliste

1. Klären, ob die Klausel allokativ-vollständig sein soll oder neben § 313 BGB stehen darf.
2. Definition höherer Gewalt entwerfen: katalogartig mit "insbesondere", inhaltlich Ereignisse außerhalb des Einflussbereichs und nicht vorhersehbar bei Vertragsschluss.
3. Pflichten festlegen: unverzügliche Anzeige (Frist, Form), Beschreibung des Ereignisses, voraussichtliche Dauer, Mitigation.
4. Rechtsfolge: Suspendierung der Leistungspflicht, kein Verzug, kein Schadensersatz wegen Leistungsstörung, jedoch ggf. Pflicht zur Mitigation.
5. Long-Stop-Kündigungsrecht ab definierter Dauer (z. B. 30, 60, 90 Tage).
6. Anpassungs- bzw. Neuverhandlungspflicht: nach welchem Maßstab und mit welcher Frist?
7. Verhältnis zu § 313 BGB klären: vorrangig Klausel, ergänzend § 313 BGB? Vollständiger Ausschluss von § 313 BGB ist in B2B-Individualabreden zulässig, in AGB regelmäßig nach § 307 BGB problematisch.
8. AGB-Check: keine pauschale Risikoabwälzung auf den Verwender oder den Vertragspartner.
9. Internationaler Bezug: ICC Force Majeure Clause 2020 oder ähnliches Muster als Referenz nutzbar; immer prüfen, ob das anwendbare Recht überlagert.
10. Beweisthemen vorbereiten: Anzeige, Kausalität, Mitigation.

## Typische Drafting-Fehler

- Pauschaler Force-Majeure-Verweis ohne Anzeige und Long Stop: führt zu unbegrenzter Suspendierung, Vertrag verharrt im Schwebezustand.
- Übernahme angloamerikanischer Muster ohne Anpassung an deutsches Recht: insbesondere "frustration"-Logik passt nicht.
- Vollständiger Ausschluss von § 313 BGB in AGB: regelmäßig § 307 BGB unwirksam.
- Definition zu eng (nur Naturereignisse): Sanktionen, regulatorische Eingriffe oder Cyberangriffe fallen heraus.
- Definition zu weit (jeder "ungewöhnliche Umstand"): keine Trennschärfe, Auslegungsstreit.
- Keine Mitigation: Vertragspartner darf untätig bleiben.
- Anpassung nach § 313 II BGB nicht beachtet: Klausel springt direkt zum Rücktritt.

## Ausgabeformat

- Klauselentwurf mit Definition, Anzeigepflicht, Suspendierung, Long Stop, Anpassung.
- Memo mit Risikobewertung, AGB-Check, Hinweis zu § 313 BGB.
- Begleitende Checkliste für die Anzeige im Eintrittsfall.

## Beispiel

Mustertext (Force-Majeure-Klausel, B2B-Lieferrahmen):

> § X Höhere Gewalt
> (1) Höhere Gewalt im Sinne dieses Vertrages ist ein Ereignis außerhalb des Einflussbereichs der betroffenen Partei, das bei Vertragsschluss nicht vorhersehbar war und trotz zumutbarer Sorgfalt nicht abgewendet werden konnte. Hierzu zählen insbesondere Naturkatastrophen, Krieg, Aufruhr, Embargos und Sanktionen, behördliche Maßnahmen mit allgemeiner Wirkung, flächendeckende Energie- oder Telekommunikationsausfälle und Pandemien mit hoheitlichen Beschränkungen, soweit sie die Vertragserfüllung unmittelbar verhindern.
> (2) Die betroffene Partei zeigt das Ereignis der anderen Partei unverzüglich, spätestens innerhalb von zehn Werktagen nach Kenntnis, in Textform an und beschreibt Ursache, voraussichtliche Dauer und betroffene Leistungspflichten. Sie unternimmt zumutbare Anstrengungen zur Schadensbegrenzung (Mitigation) und unterrichtet die andere Partei über deren Stand.
> (3) Für die Dauer der höheren Gewalt sind die betroffenen Leistungspflichten suspendiert. Ein Verzug oder Anspruch auf Schadensersatz wegen der suspendierten Pflichten besteht nicht. Pflichten, die nicht betroffen sind, bleiben bestehen.
> (4) Dauert das Ereignis länger als sechzig Tage an, kann jede Partei den Vertrag mit Wirkung zum Monatsende durch Erklärung in Textform kündigen, soweit die andere Partei nicht zuvor eine zumutbare Anpassung anbietet.
> (5) Das Recht zur Anpassung oder zum Rücktritt nach § 313 BGB bleibt unberührt; vorrangig ist diese Klausel.

## Querverweise

- `kuendigungsklauseln-und-vertragsbeendigung` – Long-Stop-Kündigung in der Kaskade.
- `boilerplate-klauseln-katalog` – Schiedsklausel und Gerichtsstand bei Streit.
- `haftungsausschluss-und-haftungsbegrenzung` – Abgrenzung zu Haftungsausschlüssen für Leistungsstörungen.
- `b2b-vs-b2c-klausel-strategie` – AGB-Bewertung in beiden Welten.

## Quellen (Stand 05/2026)

- §§ 275, 313, 326, 307 BGB.
- BGH-Urteile zu pandemiebedingten Anpassungen nach § 313 BGB sind vom Nutzer fundstellengenau zu verifizieren.
- ICC Force Majeure Clause 2020 (als internationale Vorlage; nicht deutsches Recht).
- Zitierweise: `references/zitierweise.md`.

## 2. `geheimhaltung-nda-vertraulichkeit`

**Fokus:** Drafting eines stand-alone NDA und einer Geheimhaltungsklausel als Vertragsbaustein. Strukturiert Definition der vertraulichen Information, Standardausnahmen (öffentlich bekannt, eigenständig entwickelt, von Dritten rechtmäßig erhalten, gesetzliche Offenlegungspflicht), Nutzungsbeschränkung, Pflichten zur Geheimhaltung, Dauer, Rückgabe und Löschung, Vertragsstrafe (mit Blick auf § 309 Nr. 6 BGB), Gerichtsstand und das Verhältnis zum GeschGehG mit der Pflicht zu angemessenen Geheimhaltungsmaßnahmen.

# Geheimhaltung, NDA und Vertraulichkeit

## Zweck

Dieser Skill unterstützt Sie bei der Erstellung von Geheimhaltungsregeln in zwei Varianten: als eigenständige Vertraulichkeitsvereinbarung (Non Disclosure Agreement, kurz NDA: Vertrag zur Nicht-Offenlegung von Informationen) und als Geheimhaltungsklausel innerhalb eines größeren Vertrags. Ein gutes NDA definiert exakt, was schützenswert ist, schränkt die Nutzung ein, regelt Ausnahmen, Dauer und Sanktion und ist anschlussfähig an das Geschäftsgeheimnisgesetz (GeschGehG).

## Eingaben

- Konstellation (einseitig, gegenseitig, mehrseitig).
- Anlass (Anbahnung Transaktion, Lieferantengespräch, Personalanbahnung, Due Diligence).
- Art der vertraulichen Information (Technik, Finanzen, Personal, Strategie, Sourcecode).
- Übermittlungswege (Datenraum, E-Mail, Demo, Probemuster).
- Empfängerkreis (eigene Mitarbeitende, Berater, Konzern, Subunternehmer).
- Gewünschte Sanktion (Schadensersatz, Unterlassung, Vertragsstrafe).
- Gerichtsstand, Rechtswahl, Dauer.

## Rechtlicher und methodischer Rahmen

- **Vertraglicher Rahmen:** §§ 241 II, 242, 311 II BGB; Geheimhaltungspflicht entsteht oft schon vorvertraglich. Eine vertragliche Klausel schafft Bestimmtheit und Beweisbarkeit.
- **GeschGehG (Geschäftsgeheimnisgesetz, 2019):** Geheimnisschutz setzt nach § 2 Nr. 1 b GeschGehG "den Umständen nach angemessene Geheimhaltungsmaßnahmen" voraus. Ein NDA ist deshalb auch aus Gründen des Schutzes nach GeschGehG empfehlenswert; die Klausel sollte konkrete Maßnahmen benennen (Zugangsbeschränkung, Need-to-Know, Verschwiegenheitsverpflichtung der Empfänger).
- **AGB-Recht:** Vertraulichkeitsklauseln sind grundsätzlich AGB-fähig, jedoch Inhaltskontrolle nach § 307 BGB. Vertragsstrafe in AGB: § 309 Nr. 6 BGB im Verbraucher-Geschäft unwirksam, im B2B nur eingeschränkt zulässig.
- **DSGVO:** Personenbezogene Daten benötigen eigene Rechtsgrundlage; das NDA ersetzt nicht den AVV (Auftragsverarbeitungsvertrag, Art. 28 DSGVO).
- **Form:** Schriftform empfohlen, jedoch nicht gesetzlich vorgeschrieben. Textform genügt zivilrechtlich.

## Ablauf / Checkliste

1. Zweckbestimmung formulieren: Wofür darf die Information genutzt werden (Permitted Purpose)?
2. Definition der vertraulichen Information klären: weit genug für Schutz, eng genug für Bestimmtheit. Empfehlung: alle als "vertraulich" gekennzeichneten Informationen plus solche, die ihrer Natur nach vertraulich sind.
3. Standardausnahmen aufnehmen: öffentlich bekannt ohne Vertragsverletzung, vor Erhalt bereits bekannt, von Dritten rechtmäßig erlangt, eigenständig entwickelt, gesetzliche oder behördliche Offenlegungspflicht.
4. Pflichten kombinieren: Nutzungsbeschränkung (use restriction) und Offenlegungsverbot (non-disclosure). Beides ist nötig.
5. Empfängerkreis regeln: Need-to-Know, gleichlautende Verpflichtung der Empfänger, Haftung für deren Verhalten.
6. Dauer festlegen: Geheimhaltungspflicht typischerweise drei bis fünf Jahre nach Beendigung; technische oder strategische Information ggf. dauerhaft.
7. Rückgabe und Löschung: auf Verlangen oder bei Vertragsende, mit Bestätigung in Textform. Ausnahme für Backups und gesetzliche Aufbewahrungspflichten.
8. Sanktion: Unterlassungsanspruch, Schadensersatz, optional Vertragsstrafe mit Bezug auf den Skill `vertragsstrafe-339-bgb`.
9. Gerichtsstand, Rechtswahl, Schiedsklausel je nach Konstellation.
10. GeschGehG-Maßnahmen dokumentieren: das NDA muss Teil eines Bündels angemessener Maßnahmen sein.

## Typische Drafting-Fehler

- Definition zu weit ("alle Informationen, die jemals fließen"): Risiko der Intransparenz nach § 307 BGB und Beweisprobleme.
- Definition zu eng ("nur als 'vertraulich' gekennzeichnet"): Inhalt aus Gesprächen, Demos und Bildschirmpräsentationen fällt heraus.
- Fehlende Ausnahmen: jeder Vortrag in einer öffentlichen Konferenz wird zur Vertragsverletzung.
- Pflicht zur Offenlegung an Behörden ohne Mitteilungsvorbehalt: keine Möglichkeit zur Schutzanordnung.
- Keine Regelung der Empfänger: Haftung für Berater und Subunternehmer ungeklärt.
- Vertragsstrafe in Verbraucher-AGB: § 309 Nr. 6 BGB.
- Dauer "unbegrenzt": in AGB nach § 307 BGB regelmäßig unzulässig.

## Ausgabeformat

- Vollständiger Mustertext NDA (bei stand-alone) mit Präambel, Definitionen, Pflichten, Ausnahmen, Dauer, Rückgabe, Sanktionen, Gerichtsstand.
- Alternativ Klauselbaustein für Vertragseinbindung mit Querverweis auf Beendigung.
- Kommentar: Risiken, AGB-Bewertung, GeschGehG-Anschluss.

## Beispiel

Mustertext (Geheimhaltungsklausel in einem Rahmenvertrag, B2B):

> § X Geheimhaltung
> (1) Vertrauliche Informationen im Sinne dieses Vertrages sind alle Informationen, die eine Partei der anderen im Zusammenhang mit der Vertragserfüllung in mündlicher, schriftlicher, elektronischer oder verkörperter Form offenlegt und die als vertraulich gekennzeichnet sind oder deren Vertraulichkeit sich aus den Umständen ergibt.
> (2) Ausgenommen sind Informationen, die (i) ohne Verletzung dieses Vertrages öffentlich bekannt sind oder werden, (ii) der empfangenden Partei vor der Offenlegung nachweislich bekannt waren, (iii) der empfangenden Partei rechtmäßig durch Dritte ohne Geheimhaltungspflicht zugänglich gemacht werden oder (iv) von der empfangenden Partei eigenständig ohne Nutzung vertraulicher Informationen entwickelt wurden.
> (3) Die empfangende Partei nutzt vertrauliche Informationen ausschließlich zum Zweck der Vertragsdurchführung und gibt sie nicht an Dritte weiter. Sie verpflichtet ihre Mitarbeitenden und hinzugezogenen Berater inhaltsgleich und nach dem Need-to-Know-Prinzip.
> (4) Eine Offenlegung auf gesetzliche oder behördliche Anordnung bleibt zulässig, wobei die empfangende Partei die offenlegende Partei vorab unterrichtet, soweit gesetzlich zulässig, um die Möglichkeit gerichtlichen Schutzes zu eröffnen.
> (5) Die Pflichten gelten für die Vertragslaufzeit und für weitere fünf Jahre nach Beendigung.
> (6) Auf Verlangen oder bei Vertragsende gibt die empfangende Partei alle Verkörperungen der vertraulichen Informationen zurück oder vernichtet sie und bestätigt dies in Textform. Ausgenommen sind automatisierte Backups und gesetzlich vorgeschriebene Aufbewahrung.

## Querverweise

- `vertragsstrafe-339-bgb` – Strafversprechen zur Verstärkung.
- `kuendigungsklauseln-und-vertragsbeendigung` – Survival-Klausel für Geheimhaltung.
- `boilerplate-klauseln-katalog` – Gerichtsstand, Rechtswahl, Schriftform.
- `agb-konforme-klauseln-305-310-bgb` – AGB-Prüfung des NDA.

## Quellen (Stand 05/2026)

- §§ 241 II, 242, 280, 307, 309 Nr. 6, 311 II BGB.
- §§ 1, 2, 3, 4 GeschGehG (Begriff, Erlaubte Handlungen, Verletzungshandlungen, angemessene Geheimhaltungsmaßnahmen).
- Art. 28 DSGVO (zur Abgrenzung NDA und AVV).
- BGH- und OLG-Rechtsprechung zur Angemessenheit der Geheimhaltungsmaßnahmen nach § 2 Nr. 1 b GeschGehG ist vom Nutzer fundstellengenau zu verifizieren.
- Zitierweise: `references/zitierweise.md`.
