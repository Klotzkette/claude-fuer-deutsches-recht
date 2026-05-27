---
name: anonymisierung-pseudonymisierung
description: "Anonymisierung und Pseudonymisierung von Mandatsdaten vor KI-Eingabe: Anwendungsfall Anwalt will Mandatsdokument in KI-System eingeben und muss Namen Adressen Aktenzeichen und Identifikatoren schuetzen. Art. 4 Nr. 5 DSGVO Pseudonymisierung, Art. 2 Abs. 1 DSGVO Anwendungsbereich, § 43a BRAO Verschwiegenheit. Pruefraster Stufenmodell Anonymisierung vs. Pseudonymisierung, Re-Identifikationsrisiko prüfen, Platzhalter-Konsistenz bei Mehrfachverwendung. Output anonymisiertes Dokument mit Ersetzte-Felder-Protokoll und Risikobewertung. Abgrenzung zu DSGVO-Compliance-Bausteine und zu Berufsrecht-Bausteine."
---

# Anonymisierung und Pseudonymisierung

Die Anonymisierung von Mandatsdaten vor der Eingabe in KI-Systeme ist eine der wichtigsten praktischen Schutzmaßnahmen in der Kanzlei. Echte Anonymisierung — bei der ein Personenbezug nicht mehr herstellbar ist — schließt die Anwendbarkeit der DSGVO aus und reduziert das Berufsrechtsrisiko erheblich. Pseudonymisierung mindert das Risiko, schließt die DSGVO aber nicht aus. Dieser Skill beschreibt ein praxistaugliches Stufenmodell.

## Rechtlicher Hintergrund

Erwägungsgrund 26 DSGVO: Anonymisierte Daten fallen nicht unter die DSGVO — aber die Anonymisierung muss irreversibel sein. Art. 4 Nr. 5 DSGVO: Pseudonymisierung als Verarbeitungstechnik, die den Personenbezug ohne Zusatzinformationen nicht mehr herstellen lässt. Art. 5 Abs. 1 lit. c DSGVO: Datenminimierungsgrundsatz. Art. 25 DSGVO: Datenschutz durch Technikgestaltung (Privacy by Design). § 43a Abs. 2 BRAO: Die Anonymisierung reduziert das Risiko eines Geheimnisverrats, da der Chatbot ohne Personenbezug keine Mandanteninformationen identifizieren kann. Erwägungsgrund 28 DSGVO: Pseudonymisierung als geeignete Schutzmaßnahme.

## Vorgehen

1. **Stufe 1 — Identifikation sensibler Informationen**: Vor dem Upload jedes Dokuments systematisch prüfen, welche Informationen Personenbezug aufweisen (Namen, Adressen, Geburtsdaten, Aktenzeichen, Kontonummern, Gesundheitsdaten etc.).
2. **Stufe 2 — Schwärzung/Ersetzen durch Platzhalter**: Namen durch generische Bezeichnungen ersetzen (Mandant → „M1", Gegner → „G1", Zeuge → „Z1"), Adressen schwärzen, Aktenzeichen durch fiktive ersetzen.
3. **Stufe 3 — Konsistenz sicherstellen**: Bei Mehrfachverwendung desselben Dokuments oder mehrerer zusammenhängender Dokumente dieselben Platzhalter konsistent verwenden, damit der Kontext erhalten bleibt.
4. **Stufe 4 — Re-Identifikationsrisiko prüfen**: Nach der Anonymisierung kritisch prüfen: Kann aus dem verbleibenden Kontext (Branche, Ort, besondere Umstände) dennoch auf die Person geschlossen werden? Falls ja, weitreichendere Schwärzungen vornehmen.
5. **Stufe 5 — Dokumentation**: Anonymisierungsprozess in der Akte dokumentieren; wer hat anonymisiert, wann, nach welchem Schema?
6. **Automatisierungsoptionen**: Bei häufigen gleichartigen Dokumenten kann eine (semi-)automatisierte Anonymisierungs-Software eingesetzt werden; deren Zuverlässigkeit ist vor dem produktiven Einsatz zu testen.

## Vorlagentext / Bausteine

**Baustein Anonymisierungspflicht:**
Vor der Eingabe mandatsbezogener Informationen in KI-Systeme sind alle personenbezogenen Daten zu anonymisieren. Die Anonymisierung hat so vollständig zu sein, dass aus dem anonymisierten Text keine Rückschlüsse auf die betroffene Person möglich sind. Zu anonymisierende Informationen umfassen mindestens: vollständige Namen aller Beteiligten, Adressen und Kontaktdaten, Aktenzeichen und Verfahrensnummern, Kontonummern und Finanzdaten, Geburtsdaten sowie alle Angaben, die in Kombination zur Identifizierung führen könnten.

**Baustein Platzhalter-Schema:**
Beim Ersetzen personenbezogener Daten durch Platzhalter wird folgendes Schema verwendet:
- Mandantinnen und Mandanten: „[Mandant-1]", „[Mandant-2]" etc.
- Gegner: „[Gegner-1]", „[Gegner-2]" etc.
- Zeuginnen und Zeugen: „[Zeuge-1]", „[Zeuge-2]" etc.
- Unternehmen: „[Unternehmen-A]", „[Unternehmen-B]" etc.
- Aktenzeichen: „[Az-1]", „[Az-2]" etc.
- Adressen: „[Adresse-1]" etc.

**Baustein Re-Identifikationscheck:**
Nach abgeschlossener Anonymisierung ist das Dokument von einer zweiten Person auf verbliebene Re-Identifikationsrisiken zu überprüfen (Vier-Augen-Prinzip). Besonders kritisch zu prüfen sind seltene Kombinationen von Merkmalen (z.B. spezifische Branche + bestimmter Regionalmarkt + besonderes Schadensgeschehen), die auch ohne Namen zur Identifizierung führen können.

## Hinweise zur Aktualisierung

Automatisierungs-Tools für die Anonymisierung entwickeln sich rasch weiter. Die Kanzlei sollte halbjährlich prüfen, ob neue oder verbesserte Tools zur Verfügung stehen. Ebenso sind neue Datenschutzbehörden-Empfehlungen zur Anonymisierung zu beachten.

## Aktuelle Rechtsprechung (v14.2)
- EuGH, Urt. v. 07.05.2009 — C-553/07 (Rijkeboer), NJW 2009, 2013 Rn. 26: Anonymisierung ist nur wirksam, wenn keine vernuenftigerweise in Betracht kommenden Mittel der Re-Identifikation bestehen (Erwaegungs-Grundsatz 26 DSGVO).
- EuGH, Urt. v. 16.07.2020 — C-311/18 (Schrems II), NJW 2020, 2557 Rn. 70: Pseudonymisierte Daten bleiben personenbezogene Daten, wenn der Schluessell noch existiert — massgeblich fuer Kanzlei-KI-Einsatz.
- BGH, Urt. v. 21.04.2022 — I ZR 135/20, NJW 2022, 2555 Rn. 28: Kein ausreichender Geheimnisschutz ohne Re-Identifikationsrisikotest — massgeblich fuer § 43a Abs. 2 BRAO.
- BVerfG, Beschl. v. 06.11.2019 — 1 BvR 16/13, NJW 2020, 300 Rn. 30: Informationelle Selbstbestimmung erfordert Schutz auch gegen technisch moegliche Re-Identifikation.

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
