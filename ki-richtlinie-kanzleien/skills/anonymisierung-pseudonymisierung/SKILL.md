---
name: anonymisierung-pseudonymisierung
description: "Anonymisierung Pseudonymisierung: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Anonymisierung Pseudonymisierung

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Anonymisierung Pseudonymisierung** im Plugin KI-Richtlinie für Kanzleien. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `anonymisierung-pseudonymisierung` | Anonymisierung und Pseudonymisierung von Mandatsdaten vor KI-Eingabe: Anwendungsfall Anwalt will Mandatsdokument in KI-System eingeben und muss Namen Adressen Aktenzeichen und Identifikatoren schützen. Art. 4 Nr. 5 DSGVO Pseudonymisierung, Art. 2 Abs. 1 DSGVO Anwendungsbereich, § 43a BRAO Verschwiegenheit. Prüfraster Stufenmodell Anonymisierung vs. Pseudonymisierung, Re-Identifikationsrisiko prüfen, Platzhalter-Konsistenz bei Mehrfachverwendung. Output anonymisiertes Dokument mit Ersetzte-Felder-Protokoll und Risikobewertung. Abgrenzung zu DSGVO-Compliance-Bausteine und zu Berufsrecht-Bausteine. |
| `automatisierte-entscheidungen-art-22-dsgvo` | Automatisierte Einzelentscheidungen nach Art. 22 DSGVO in Kanzleien prüfen: Anwendungsfall Kanzlei plant KI-gestützte Mandatszuordnung Honorarberechnung oder Bonitätsprüfung und muss prüfen ob automatisierte Entscheidung ohne Mensch zulässig ist. Art. 22 DSGVO Verbot automatisierter Einzelentscheidungen, Art. 6 DSGVO Rechtsgrundlage, DSGVO Einwilligung. Prüfraster erhebliche Auswirkung der Entscheidung, Ausnahmen Einwilligung Vertrag gesetzliche Grundlage, Widerspruchsrecht und Gegendarstellung. Output Prüfprotokoll mit Einordnung und notwendigen Schutzmaßnahmen. Abgrenzung zu KI-VO-Betreiber-Pflichten und zu DSGVO-Compliance. |
| `berufsrecht-bausteine` | Berufsrechtliche Textbausteine für KI-Nutzungsrichtlinien in Kanzleien: Anwendungsfall Kanzlei erstellt KI-Richtlinie und braucht praezise Bausteine zu Verschwiegenheit Sorgfaltspflicht und Eigenverantwortung. § 43 BRAO Gewissenhaftigkeit, § 43a Abs. 2 BRAO Verschwiegenheit, § 43e BRAO IT-Dienstleister, § 203 StGB Berufsgeheimnis, BRAK-Hinweise 12/2024 DAV-Stellungnahme 32/2025. Prüfraster Verschwiegenheitspflicht beim KI-Einsatz, Haftung für KI-Output OLG Koblenz, eigenverantwortliche Endkontrolle. Output Bausteine-Sammlung mit konkreten Formulierungen für Kanzlei-Richtlinie. Abgrenzung zu DSGVO-Compliance-Bausteine und zu Musterklauseln-IT. |

## Arbeitsweg

Im Plugin KI-Richtlinie für Kanzleien gilt für **Anonymisierung Pseudonymisierung**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `anonymisierung-pseudonymisierung`

**Fokus:** Anonymisierung und Pseudonymisierung von Mandatsdaten vor KI-Eingabe: Anwendungsfall Anwalt will Mandatsdokument in KI-System eingeben und muss Namen Adressen Aktenzeichen und Identifikatoren schützen. Art. 4 Nr. 5 DSGVO Pseudonymisierung, Art. 2 Abs. 1 DSGVO Anwendungsbereich, § 43a BRAO Verschwiegenheit. Prüfraster Stufenmodell Anonymisierung vs. Pseudonymisierung, Re-Identifikationsrisiko prüfen, Platzhalter-Konsistenz bei Mehrfachverwendung. Output anonymisiertes Dokument mit Ersetzte-Felder-Protokoll und Risikobewertung. Abgrenzung zu DSGVO-Compliance-Bausteine und zu Berufsrecht-Bausteine.

# Anonymisierung und Pseudonymisierung

Die Anonymisierung von Mandatsdaten vor der Eingabe in KI-Systeme ist eine der wichtigsten praktischen Schutzmaßnahmen in der Kanzlei. Echte Anonymisierung — bei der ein Personenbezug nicht mehr herstellbar ist — schließt die Anwendbarkeit der DSGVO aus und reduziert das Berufsrechtsrisiko erheblich. Pseudonymisierung mindert das Risiko, schließt die DSGVO aber nicht aus. Dieser Skill beschreibt ein praxistaugliches Stufenmodell.

## Rechtlicher Hintergrund

Erwägungsgrund 26 DSGVO: Anonymisierte Daten fallen nicht unter die DSGVO — aber die Anonymisierung muss irreversibel sein. Art. 4 Nr. 5 DSGVO: Pseudonymisierung als Verarbeitungstechnik, die den Personenbezug ohne Zusatzinformationen nicht mehr herstellen lässt. Art. 5 Abs. 1 lit. c DSGVO: Datenminimierungsgrundsatz. Art. 25 DSGVO: Datenschutz durch Technikgestaltung (Privacy by Design). § 43a Abs. 2 BRAO: Die Anonymisierung reduziert das Risiko eines Geheimnisverrats, da der Chatbot ohne Personenbezug keine Mandanteninformationen identifizieren kann. Erwägungsgrund 28 DSGVO: Pseudonymisierung als geeignete Schutzmaßnahme.

## Vorgehen

1. **Stufe 1 — Identifikation sensibler Informationen**: Vor dem Upload jedes Dokuments systematisch prüfen, welche Informationen Personenbezug aufweisen (Namen, Adressen, Geburtsdaten, Aktenzeichen, Kontonummern, Gesundheitsdaten etc.).
2. **Stufe 2 — Schwärzung/Ersetzen durch Platzhalter**: Namen durch generische Bezeichnungen ersetzen (Mandant → "M1", Gegner → "G1", Zeuge → "Z1"), Adressen schwärzen, Aktenzeichen durch fiktive ersetzen.
3. **Stufe 3 — Konsistenz sicherstellen**: Bei Mehrfachverwendung desselben Dokuments oder mehrerer zusammenhängender Dokumente dieselben Platzhalter konsistent verwenden, damit der Kontext erhalten bleibt.
4. **Stufe 4 — Re-Identifikationsrisiko prüfen**: Nach der Anonymisierung kritisch prüfen: Kann aus dem verbleibenden Kontext (Branche, Ort, besondere Umstände) dennoch auf die Person geschlossen werden? Falls ja, weitreichendere Schwärzungen vornehmen.
5. **Stufe 5 — Dokumentation**: Anonymisierungsprozess in der Akte dokumentieren; wer hat anonymisiert, wann, nach welchem Schema?
6. **Automatisierungsoptionen**: Bei häufigen gleichartigen Dokumenten kann eine (semi-)automatisierte Anonymisierungs-Software eingesetzt werden; deren Zuverlässigkeit ist vor dem produktiven Einsatz zu testen.

## Vorlagentext / Bausteine

**Baustein Anonymisierungspflicht:**
Vor der Eingabe mandatsbezogener Informationen in KI-Systeme sind alle personenbezogenen Daten zu anonymisieren. Die Anonymisierung hat so vollständig zu sein, dass aus dem anonymisierten Text keine Rückschlüsse auf die betroffene Person möglich sind. Zu anonymisierende Informationen umfassen mindestens: vollständige Namen aller Beteiligten, Adressen und Kontaktdaten, Aktenzeichen und Verfahrensnummern, Kontonummern und Finanzdaten, Geburtsdaten sowie alle Angaben, die in Kombination zur Identifizierung führen könnten.

**Baustein Platzhalter-Schema:**
Beim Ersetzen personenbezogener Daten durch Platzhalter wird folgendes Schema verwendet:
- Mandantinnen und Mandanten: "[Mandant-1]", "[Mandant-2]" etc.
- Gegner: "[Gegner-1]", "[Gegner-2]" etc.
- Zeuginnen und Zeugen: "[Zeuge-1]", "[Zeuge-2]" etc.
- Unternehmen: "[Unternehmen-A]", "[Unternehmen-B]" etc.
- Aktenzeichen: "[Az-1]", "[Az-2]" etc.
- Adressen: "[Adresse-1]" etc.

**Baustein Re-Identifikationscheck:**
Nach abgeschlossener Anonymisierung ist das Dokument von einer zweiten Person auf verbliebene Re-Identifikationsrisiken zu überprüfen (Vier-Augen-Prinzip). Besonders kritisch zu prüfen sind seltene Kombinationen von Merkmalen (z.B. spezifische Branche + bestimmter Regionalmarkt + besonderes Schadensgeschehen), die auch ohne Namen zur Identifizierung führen können.

## Hinweise zur Aktualisierung

Automatisierungs-Tools für die Anonymisierung entwickeln sich rasch weiter. Die Kanzlei sollte halbjährlich prüfen, ob neue oder verbesserte Tools zur Verfügung stehen. Ebenso sind neue Datenschutzbehörden-Empfehlungen zur Anonymisierung zu beachten.

## Aktuelle Rechtsprechung (v14.2)
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zentrale Normen (Paragrafenkette)
- Art. 4 Nr. 1 DSGVO — Begriff personenbezogene Daten
- Art. 4 Nr. 5 DSGVO — Pseudonymisierung
- Erwaegungsgrund 26 DSGVO — Anonymisierung und Re-Identifikationsrisiko
- § 43a Abs. 2 BRAO — Verschwiegenheitspflicht
- § 203 StGB — Berufsgeheimnis

## Triage zu Beginn
1. Handelt es sich um echte Anonymisierung oder nur Pseudonymisierung — besteht ein Zuordnungsschluessel?
2. Welche Datenkategorien sind betroffen — besondere Kategorien nach Art. 9 DSGVO?
3. Ist ein Re-Identifikationsrisiko durch Kombination verbleibender Merkmale (Branche, Ort, Umstaende) moeglich?
4. Wird das Dokument in einem KI-System mit Training verarbeitet — besteht Risiko des Modell-Memorizings?
5. Ist der Anonymisierungsprozess dokumentiert und vieraugengeprueft?

## Output-Template — Anonymisierungsprotokoll
**Adressat:** Kanzlei intern (Akte) — Tonfall: knapp, dokumentierend
```
ANONYMISIERUNGSPROTOKOLL
[DATUM] — [AKTENZEICHEN] — Dokument: [BEZEICHNUNG]

Anonymisiert von: [NAME]
Datum: [DATUM]
Verfahren: Platzhalter-Schema (M1/G1/Z1/Az-1)

Ersetzte Kategorien:
☑ Namen
☑ Adressen
☑ Aktenzeichen
☑ Geburtsdaten
☑ Kontonummern
☐ Gesundheitsdaten (falls betroffen)
☐ Sonstige: [BESCHREIBUNG]

Re-Identifikationsrisiko-Check:
Vier-Augen-Pruefung durch: [NAME]
Ergebnis: [KEIN RISIKO / RISIKO — WEITERE SCHWAERZUNG: BESCHREIBUNG]

Anonymisierungsgrad: [ANONYMISIERT / PSEUDONYMISIERT]
DSGVO anwendbar: [JA / NEIN]
```

## 2. `automatisierte-entscheidungen-art-22-dsgvo`

**Fokus:** Automatisierte Einzelentscheidungen nach Art. 22 DSGVO in Kanzleien prüfen: Anwendungsfall Kanzlei plant KI-gestützte Mandatszuordnung Honorarberechnung oder Bonitätsprüfung und muss prüfen ob automatisierte Entscheidung ohne Mensch zulässig ist. Art. 22 DSGVO Verbot automatisierter Einzelentscheidungen, Art. 6 DSGVO Rechtsgrundlage, DSGVO Einwilligung. Prüfraster erhebliche Auswirkung der Entscheidung, Ausnahmen Einwilligung Vertrag gesetzliche Grundlage, Widerspruchsrecht und Gegendarstellung. Output Prüfprotokoll mit Einordnung und notwendigen Schutzmaßnahmen. Abgrenzung zu KI-VO-Betreiber-Pflichten und zu DSGVO-Compliance.

# Automatisierte Entscheidungen Art. 22 DSGVO

Art. 22 DSGVO schützt Personen vor Entscheidungen, die ausschließlich auf automatisierter Verarbeitung — also ohne menschliche Überprüfung — beruhen und erhebliche Auswirkungen auf die betroffene Person haben. Beim Einsatz von KI-Systemen in Kanzleien ist dieses Verbot besonders relevant: Keine rechtlich bedeutsame Entscheidung darf allein auf der Grundlage eines KI-Outputs getroffen werden.

## Rechtlicher Hintergrund

Art. 22 Abs. 1 DSGVO: Betroffene haben das Recht, nicht einer ausschließlich auf automatisierter Verarbeitung beruhenden Entscheidung unterworfen zu werden, die ihnen gegenüber rechtliche Wirkung entfaltet oder sie in ähnlicher Weise erheblich beeinträchtigt. Art. 22 Abs. 2 DSGVO: Ausnahmen — Vertragsdurchführung (lit. a), gesetzliche Grundlage (lit. b), ausdrückliche Einwilligung (lit. c). Art. 22 Abs. 3 DSGVO: Bei Ausnahmen müssen geeignete Maßnahmen zum Schutz der Rechte und Freiheiten sowie der berechtigten Interessen getroffen werden, mindestens: Recht auf menschliche Einflussnahme, Darlegung des eigenen Standpunkts, Anfechtung der Entscheidung. Art. 22 Abs. 4 DSGVO: Besonders sensitive Kategorien nach Art. 9 DSGVO dürfen nicht Grundlage automatisierter Entscheidungen sein, außer bei ausdrücklicher Einwilligung oder erheblichem öffentlichem Interesse. Erwägungsgrund 71 DSGVO: Klarstellung zum Anwendungsbereich.

## Vorgehen

1. **Entscheidungstypen identifizieren**: Welche Entscheidungen in der Kanzlei könnten vollständig oder teilweise durch KI-Systeme getroffen werden?
2. **Automatisierungsgrad prüfen**: Eine Entscheidung ist nur dann nach Art. 22 DSGVO verboten, wenn sie ausschließlich automatisiert ergeht und eine erhebliche Wirkung hat. Menschliche Endkontrolle durchbricht den Tatbestand.
3. **Ausnahmen prüfen**: Liegt eine der Ausnahmen des Art. 22 Abs. 2 DSGVO vor?
4. **Menschliche Aufsicht sicherstellen**: Für jede relevante Entscheidung muss ein Mensch die finale Verantwortung übernehmen und die Möglichkeit haben, das KI-Ergebnis zu korrigieren.
5. **Sensible Daten ausschließen**: Bei Entscheidungen, die auf besonderen Datenkategorien nach Art. 9 DSGVO beruhen, ist besondere Vorsicht geboten.
6. **Betroffenenrechte kommunizieren**: Mandanten und Beschäftigte müssen über ihr Recht informiert werden, automatisierte Entscheidungen anzufechten.

## Vorlagentext / Bausteine

**Baustein Verbot automatisierter Letztentscheidung:**
Kein KI-System trifft in der Kanzlei eine abschließende Entscheidung mit rechtlicher Wirkung oder erheblicher tatsächlicher Beeinträchtigung für eine natürliche Person. Alle von KI-Systemen erzeugten Empfehlungen, Einstufungen oder Bewertungen sind ausnahmslos von einer qualifizierten menschlichen Person zu überprüfen, zu bewerten und freizugeben. Dies gilt insbesondere für: Mandatszuordnungen, Honorarberechnungen, Bonitätsbewertungen von Mandanten sowie Personalentscheidungen.

**Baustein Menschliche Überprüfung:**
Mitarbeitende, die KI-generierte Ergebnisse für Entscheidungsprozesse nutzen, sind angewiesen, das KI-Ergebnis stets als Hilfsmittel — nicht als Entscheidung — zu behandeln. Die menschliche Überprüfung muss inhaltlich erfolgen; ein rein formales "Abnicken" des KI-Outputs ohne eigene Prüfung genügt nicht den Anforderungen des Art. 22 DSGVO.

**Baustein Betroffenenrechte:**
Sofern KI-Systeme an Entscheidungen mit Auswirkungen auf Mandanten oder Dritte beteiligt sind, informiert die Kanzlei betroffene Personen auf Anfrage über die Logik der Entscheidungsfindung sowie über das Recht, eine menschliche Überprüfung der Entscheidung zu verlangen (Art. 22 Abs. 3 DSGVO).

## Hinweise zur Aktualisierung

Mit zunehmender Integration von KI-Systemen in Kanzleimanagement-Software (z.B. automatische Mandatszuordnung, Dokumentenpriorisierung) steigt die Relevanz des Art. 22 DSGVO. Neue EuGH- oder BGH-Entscheidungen zur Auslegung von Art. 22 DSGVO sowie Leitlinien des Europäischen Datenschutzausschusses (EDSA) sind regelmäßig zu prüfen.

## Aktuelle Rechtsprechung (v14.2)
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zentrale Normen (Paragrafenkette)
- Art. 22 Abs. 1 DSGVO — Verbot vollautomatisierter Einzelentscheidungen mit Rechtswirkung
- Art. 22 Abs. 2 lit. a-c DSGVO — Ausnahmen (Vertrag, gesetzliche Pflicht, Einwilligung)
- Art. 22 Abs. 3 DSGVO — Widerspruchsrecht und menschliche Pruefung
- Art. 13/14 DSGVO — Informationspflichten bei automatisierten Entscheidungen
- § 26 BDSG — Beschaeftigtendatenschutz bei KI-Mitarbeiterbewertung

## Triage zu Beginn
1. Liegt eine vollautomatisierte Entscheidung mit Rechtswirkung oder erheblicher Beeintraechtigung vor?
2. Ist eine Rechtsgrundlage nach Art. 22 Abs. 2 lit. a-c DSGVO gegeben?
3. Ist ein menschlicher Ueberpruefer vorgesehen — oder stempelt er nur ab (Stempel-Risiko)?
4. Werden Betroffene nach Art. 13/14 DSGVO ueber die automatisierte Entscheidung informiert?
5. Ist ein Widerspruchsrecht und eine Korrekturmoeglichkeit nach Art. 22 Abs. 3 DSGVO implementiert?

## Output-Template — Art. 22 DSGVO-Pruefprotokoll
**Adressat:** DSB / Compliance — Tonfall: strukturiert, rechtlich
```
ART. 22 DSGVO-PRUEFPROTOKOLL
[DATUM] — System: [SYSTEMNAME] — Anwendungsfall: [BESCHREIBUNG]

Vollautomatisiert: [JA / NEIN]
Rechtswirkung / erhebliche Beeintraechtigung: [JA / NEIN — BEGRUENDUNG]
Art. 22 Abs. 1 DSGVO einschlaegig: [JA / NEIN]

Falls einschlaegig — Rechtsgrundlage Art. 22 Abs. 2:
☑/☐ lit. a — Vertragserfuellung
☑/☐ lit. b — gesetzliche Pflicht
☑/☐ lit. c — ausdrueckliche Einwilligung

Human-in-the-Loop: [JA — wie: BESCHREIBUNG / NEIN / NOMINELL — Stempel-Risiko]
Widerspruchsrecht implementiert: [JA / NEIN]
Informationspflicht Art. 13/14 DSGVO erfuellt: [JA / NEIN]

Ergebnis: [ZULASSIG / UNZULASSIG — MASSNAHME ERFORDERLICH]
Massnahme: [BESCHREIBUNG bis DATUM]
Geprueft von: [NAME], [DATUM]
```

## 3. `berufsrecht-bausteine`

**Fokus:** Berufsrechtliche Textbausteine für KI-Nutzungsrichtlinien in Kanzleien: Anwendungsfall Kanzlei erstellt KI-Richtlinie und braucht praezise Bausteine zu Verschwiegenheit Sorgfaltspflicht und Eigenverantwortung. § 43 BRAO Gewissenhaftigkeit, § 43a Abs. 2 BRAO Verschwiegenheit, § 43e BRAO IT-Dienstleister, § 203 StGB Berufsgeheimnis, BRAK-Hinweise 12/2024 DAV-Stellungnahme 32/2025. Prüfraster Verschwiegenheitspflicht beim KI-Einsatz, Haftung für KI-Output OLG Koblenz, eigenverantwortliche Endkontrolle. Output Bausteine-Sammlung mit konkreten Formulierungen für Kanzlei-Richtlinie. Abgrenzung zu DSGVO-Compliance-Bausteine und zu Musterklauseln-IT.

# Berufsrecht-Bausteine

Das anwaltliche Berufsrecht setzt dem Einsatz von KI-Systemen in Kanzleien spezifische Grenzen. Die Nutzung von Chatbots und KI-Plattformen ist nicht per se verboten, aber die berufsrechtlichen Kernpflichten — Gewissenhaftigkeit, Verschwiegenheit und eigenverantwortliche Endkontrolle — bleiben stets unberührt. Diese Bausteine helfen, die entsprechenden Anforderungen in eine Kanzleirichtlinie zu übersetzen.

## Rechtlicher Hintergrund

§ 43 Satz 1 BRAO: Gewissenhafte Berufsausübung — KI-Nutzung muss von anwaltlicher Eigenverantwortung begleitet sein. § 43a Abs. 2 BRAO: Verschwiegenheitspflicht als oberstes Gebot — kein unbefugtes Offenbaren von Mandatsgeheimnissen. § 43e BRAO: Regelung der IT-Dienstleister-Beauftragung — Befugnis-Norm, die § 203 StGB entschärft. § 203 Abs. 1 Nr. 3, Abs. 3, Abs. 4 StGB: Geheimnisverrat als Straftatbestand. § 2 Abs. 4 lit. c BORA: Sozialadäquanz der Zusammenarbeit mit Dienstleistern. § 31 BORA: Berufsrechtsbeauftragter in Berufsausübungsgemeinschaften. BRAK-Hinweise 12/2024 (Remmertz), DAV-Stellungnahme Nr. 32/2025.

## Vorgehen


**Vorab:** Der untenstehende ist die typische Standardlinie. Wenn die Mandantenlage abweicht (siehe "Strategische Optionen" oben), sind die Schritte entsprechend zu verkuerzen, umzustellen oder durch ein anderes Skill zu ersetzen — der ist Leitfaden, nicht Pflichtprogramm.

1. **Grundsatz der Eigenverantwortung verankern**: Kein KI-Output darf ungeprüft übernommen werden; § 43 BRAO verlangt anwaltliche Endkontrolle.
2. **Verschwiegenheitspflicht operationalisieren**: Für jeden KI-Dienstleister einen § 43e-BRAO-Vertrag abschließen (vgl. Musterklauseln im Plugin `musterklauseln-it-vertrag`).
3. **Prüfpflicht für Zitate festschreiben**: Jede von einem KI-System erzeugte Fundstelle ist auf Existenz und inhaltliche Richtigkeit zu überprüfen (BRAK 12/2024, S. 2; DAV 32/2025).
1. Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
5. **Berufsrechtsbeauftragten einbinden**: Falls vorhanden, nach § 31 BORA bei Erstellung und Schulung einbeziehen.
6. **Ausländische Dienstleister gesondert prüfen**: § 43e Abs. 4 BRAO erlaubt EU-Ausland und Drittstaaten, sofern vergleichbares Schutzniveau.

## Strategische Optionen (vor dem Template entscheiden)

Bevor das Template eins-zu-eins gefuellt wird, ist zu pruefen welche Variante zur Mandantenkonstellation passt. Das Template ist **eine** moegliche Form — nicht die einzige.

| Konstellation | Empfohlener Weg |
|---|---|
| Standard — Berufsrechts-Check KI-Einsatz fuer Kanzlei erstellen | Baustein-Set nach Schema; Template unten |
| Variante A — Kanzlei hat bereits BRAO-Richtlinie | Delta-Update statt Neuerstellung; bestehende Richtlinie ergaenzen |
| Variante B — Internationales Buero mehrere Rechtsordnungen | Separate Bausteine pro Jurisdiction; gemeinsamer Rahmen |
| Variante C — Mandant ist selbst Kanzlei Beratung nicht Kanzlei intern | Externe Beratungsperspektive; nicht interne Richtlinie |

Wenn die Mandantenkonstellation **nicht** ins Standardschema passt, ist das Template anzupassen oder durch ein anderes Skill abzuloesen — nicht das Mandat in das Schema zu pressen.


## Vorlagentext / Bausteine

**Baustein Gewissenhaftigkeit:**
Gemäß § 43 Satz 1 BRAO sind alle Rechtsanwältinnen und Rechtsanwälte zur gewissenhaften Berufsausübung verpflichtet. Der Einsatz von KI-Systemen darf die anwaltliche Tätigkeit lediglich unterstützen, aber niemals ersetzen. Jedes von einem KI-System generierte Ergebnis muss einer eigenverantwortlichen Überprüfung und Endkontrolle durch die zuständige Rechtsanwältin oder den zuständigen Rechtsanwalt unterzogen werden. Die KI entscheidet nie — es entscheidet immer der Mensch.

**Baustein Verschwiegenheit:**
Die Wahrung des Anwaltsgeheimnisses ist oberstes Gebot (§ 43a Abs. 2 BRAO, § 203 Abs. 1 Nr. 3 StGB). Die Zusammenarbeit mit KI-Dienstleistern als externe IT-Dienstleister ist nur unter den Voraussetzungen des § 43e BRAO zulässig. Mit jedem eingesetzten KI-Dienstleister ist eine schriftliche Vereinbarung nach § 43e BRAO abzuschließen, die den Dienstleister zur Verschwiegenheit verpflichtet und auf die strafrechtlichen Folgen eines Verstoßes nach § 203 StGB hinweist.

**Baustein Prüfpflicht/Halluzinationen:**
Alle von KI-Systemen generierten Fundstellen, Zitate und Rechtsangaben sind ausnahmslos auf ihre Existenz und ihren Inhalt hin zu überprüfen. Wer dies unterlässt, handelt pflichtwidrig nach § 43 BRAO und haftet für die Folgen. Ein "Grundvertrauen" wie bei erfahrenen Mitarbeitenden ist bei KI-generierten Arbeitsprodukten nicht angebracht (BRAK-Hinweise 12/2024; DAV-Stellungnahme 32/2025).

--- vor Versand klaeren ---
1. Welches Verhandlungsziel hat der Mandant? [Durchsetzung des Anspruchs / Vergleich / Reputationsschutz / schnelle Loesung]
2. Welche Kompromisslinien sind absolut? [Mindestforderung / Zeitrahmen / Formerfordernis]
3. Sind Anschlusswege erwuenscht? [Mediation / Direktgesprach / Einigung vor Fristablauf]

Schlussabsatz Variante A (kooperativ):
Wir regen eine guetliche Einigung an und stehen fuer ein klaerenden Gesprach zur Verfuegung. Eine einvernehmliche Loesung erspart beiden Seiten Zeit und Kosten.

Schlussabsatz Variante B (formal-streng):
Eine aussergerichtliche Einigung kommt nur in Betracht wenn die Gegenseite innerhalb von [X] Tagen einen akzeptablen Vorschlag unterbreitet. Anderenfalls werden wir alle rechtlichen Schritte einleiten.


## Hinweise zur Aktualisierung

Die BRAK und der DAV aktualisieren ihre Hinweise und Stellungnahmen fortlaufend. Nach jeder Neuveröffentlichung sind die Bausteine zu überprüfen. Ebenso bei neuen OLG- oder BGH-Entscheidungen zur Haftung bei Verwendung von KI-Output in Schriftsätzen.

## Aktuelle Rechtsprechung (v14.2)
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zentrale Normen (Paragrafenkette)
- § 43a Abs. 2 BRAO — Verschwiegenheitspflicht
- § 43e BRAO — IT-Dienstleister und berufsrechtliche Absicherung
- § 203 StGB — Berufsgeheimnis (Freiheitsstrafe bis 2 Jahre)
- §§ 1 ff. BORA — Berufsordnung Rechtsanwaelte
- Art. 28 DSGVO — AVV-Pflicht bei Auftragsverarbeitung

## Triage zu Beginn
1. Ist der KI-Anbieter ein IT-Dienstleister nach § 43e BRAO — liegt eine berufsrechtliche AVV-Vereinbarung vor?
2. Werden Mandatsdaten in das KI-System eingegeben — ist Anonymisierung oder verschlüsselte Verarbeitung sichergestellt?
3. Hat der KI-Anbieter seinen Sitz ausserhalb der EU — droht ein CLOUD Act-Zugriff?
4. Werden KI-Ausgaben ohne menschliche Pruefung verwendet — Haftungsrisiko nach § 280 BGB?
5. Ist die KI in der Lage, Mandate anderer Mandanten zu verwechseln — Interessenkonflikt-Risiko?
- **Was will der Mandant wirklich erreichen?** (Nicht: was steht im Standardweg, sondern: welches Ergebnis ist fuer den Mandanten persoenlich/wirtschaftlich das beste? Manchmal ist der schnellere Vergleich besser als der formal "richtige" Weg.)

## Output-Template — Berufsrechts-Check KI-Einsatz
**Adressat:** Kanzlei-Management / Senior-Partner — Tonfall: strukturiert, berufsrechtlich
```
BERUFSRECHTS-CHECK KI-EINSATZ
[DATUM] — Kanzlei: [NAME MANDANT] — System: [SYSTEMNAME]

§ 43a Abs. 2 BRAO — Verschwiegenheit:
☑/☐ KI-Anbieter durch § 43e BRAO-AVV gebunden
☑/☐ Mandatsdaten anonymisiert vor Eingabe
☑/☐ Kein Training auf Mandatsdaten

§ 203 StGB — Berufsgeheimnis:
☑/☐ Zugriff auf Mandatsdaten auf notwendiges Personal beschraenkt
☑/☐ Verschlüsselte Verarbeitung oder On-Premise

Haftungsrisiko § 280 BGB / § 43 BRAO:
☑/☐ Vier-Augen-Pruefung aller KI-Ausgaben vor Verwendung
☑/☐ Keine unkritische Uebernahme von Rechtsprechungs-Zitaten ohne Pruefung

Ergebnis: [EINSATZ ZULAESSIG / MIT AUFLAGEN / UNZULAESSIG]
Auflagen: [BESCHREIBUNG]
Geprueft von: [NAME], [DATUM]
```
