---
name: copy-paste-fehler-erkennung
description: "Für Copy-Paste-Fehler erkennen: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt."
---

# Copy-Paste-Fehler erkennen

## Rolle und Fokus
Findet uebernommene Textstellen aus Vorlaeuferdokumenten: alte Parteinamen, falsche Datumsangaben in Standardabsaetzen, Verweise auf nicht existente Anhaenge oder Beschlüsse.

## Anwendungsbeispiel
Wandeldarlehen NordCap vom 14.03.2026: § 4 verweist auf 'Gesellschafterbeschluss vom 22.01.2026' — solcher Beschluss existiert nicht; jung uebernommene Klausel aus Wandeldarlehensvorlage einer anderen Portfoliogesellschaft. § 11 nennt 'LausitzWind GmbH' statt 'LausitzStorage 200 GmbH i.G.' an einer Stelle.

## Output-Module
- Auffaelligkeitsliste mit Fundstelle, Verdacht, Verweisziel
- Querliste an Skill `unterschriftspruefung` (Beschluss als Wirksamkeitsbedingung)
- Reparatur-Vorschlag für Nachtragsvereinbarung

<!-- BEGIN ausformulierungspflicht (autogen) -->
> **Ausformulierungspflicht und Formatstandard.** Das Endprodukt wird in **vollständigen, ausformulierten Sätzen** geliefert — keine Stichwortskelette, keine leeren Klauselrümpfe, keine reinen Aufzählungen. Klauseln stehen als ausformulierte Rechtsfolgen-Sätze; Platzhalter wie `[Name der Mandantin]` werden klar markiert, der umgebende Text bleibt vollständig.
>
> **Schriftbild:** Wenn ein Schriftsatz, Vertrag, Memo, Beschluss, Vermerk oder sonstiges Enddokument als DOCX, PDF oder formatierter Text ausgegeben wird, ist **Times New Roman 11 pt** als Grundschrift zu verwenden. Überschriften bleiben in derselben Schrift und dürfen nur fett oder abgestuft sein. Bei reiner Markdown- oder Chat-Ausgabe wird dieser Formatwunsch als Exporthinweis aufgenommen.
>
> **Nummerierung:** Gliederung ausschließlich dezimal (`1`, `1.1`, `1.1.1` und so weiter). Keine römischen Ziffern, keine Buchstaben- oder Mischgliederung.
<!-- END ausformulierungspflicht (autogen) -->

