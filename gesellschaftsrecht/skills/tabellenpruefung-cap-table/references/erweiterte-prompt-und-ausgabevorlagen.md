# 1. Erweiterte Prompt- und Ausgabevorlagen

Diese Bibliothek wird nur für ein betroffenes Spezialgebiet oder für die abschließende tabellarische Ausgabe geladen.

## 1. Prompt-Bibliothek

## Erweiterte Spaltenprompt-Bibliothek

### Arbeitsrecht / Employment

| Spalte | Typ | Prompt |
|---|---|---|
| Wettbewerbsverbot | klassifizieren | Hat der Arbeitnehmer / die Schlüsselperson ein nachvertragliches Wettbewerbsverbot? Paragraf 74 HGB: Karenzentschädigung erforderlich; Dauer max. 2 Jahre. |
| Change-of-Control-Recht | klassifizieren | Hat der Mitarbeiter ein Sonderkündigungsrecht oder Abfindungsanspruch bei Kontrollwechsel? |
| Geheimnisschutz | wörtlich | Enthält der Vertrag eine Geheimhaltungsklausel? Paragraf 1 GeschGehG: Legaldefinition prüfen. |

### IP / Technologie

| Spalte | Typ | Prompt |
|---|---|---|
| IP-Eigentumsklausel | klassifizieren | Wer ist Eigentümer des während der Zusammenarbeit entwickelten IP? Klassifikation: Auftraggeber / Auftragnehmer / gemeinsam. |
| Lizenzumfang | wörtlich | Welche Nutzungsrechte werden eingeräumt? Territorial, zeitlich, exklusiv/nicht-exklusiv, sublizenzierbar? |
| Open-Source-Verpflichtungen | klassifizieren | Enthält der Vertrag Verpflichtungen aus Open-Source-Lizenzen? Copyleft-Risiko (GPL, AGPL)? |

### Finance / Kredit

| Spalte | Typ | Prompt |
|---|---|---|
| Financial Covenants | wörtlich | Welche Financial Covenants enthält der Vertrag? EBITDA-Mindestwert, Verschuldungsgrad, Interest Cover Ratio. |
| Material Adverse Change | wörtlich | Enthält der Vertrag eine MAC-Klausel? Definition: welche Ereignisse? Schwellenwert? |
| Vorfälligkeitsregelung | klassifizieren | Kann der Kreditgeber vorzeitig kündigen oder fällig stellen? Auslöser: Cross-Default, MAC, Covenant-Verletzung? |

### Real Estate / Immobilien

| Spalte | Typ | Prompt |
|---|---|---|
| Mietfläche | betrag | Gemietete Fläche in m². Wörtliches Zitat aus Mietvertrag. |
| Untervermietungsrecht | klassifizieren | Darf der Mieter untervermieten? Zustimmungserfordernis des Vermieters? Paragraf 540 BGB. |
| Konkurrenzschutz | klassifizieren | Enthält der Mietvertrag eine Konkurrenzschutzklausel zugunsten des Mieters? |

## 2. Ausgabevorlage

## Output-Template

**Adressat:** Bearbeitender Anwalt / Transaktionsteam — Tonfall: sachlich-strukturiert, zeilengenau

```
PROMPT-MATRIX PRUEFERGEBNIS
Mandat: [MANDATSCODE]
Schema-Version: [v1.0 / Datum]
Pruefzeitraum: [DATUM] bis [DATUM]
Erstellt von: [NAME], [KANZLEI]

--- ZUSAMMENFASSUNG ---
Dokumente geprueft: [N]
Spalten im Schema: [N]
Zellen gesamt: [N]
Auffaelligkeiten (prüfung_erforderlich): [N]
Eindeutig bewertete Zellen: [N] ([%])

--- ERGEBNISMATRIX ---
| Nr. | Dokument | [SPALTE 1] | [SPALTE 2] | [SPALTE 3] | Auffaelligkeiten |
|---|---|---|---|---|---|
| 1 | [DATEINAME] | [WERT / "ZITAT"] | [WERT] | unklar | Paragraf [NORM] — prüfung_erforderlich |
| 2 | [DATEINAME] | [WERT] | [WERT] | [WERT] | — |

--- AUFFAELLIGKEITEN (prüfung_erforderlich) ---
1. Dokument [N], Spalte [SPALTENNAME]:
 Befund: [BESCHREIBUNG]
 Relevante Norm: [Paragraf NORM]
 Zitat: "[WORTLAUT AUS DOKUMENT]"
 Empfehlung: [HANDLUNGSHINWEIS]

2. [Weitere Auffaelligkeiten]

--- GRENZFAELLE (menschliche Entscheidung erforderlich) ---
1. Dokument [N]: [BESCHREIBUNG GRENZFALL]
 Moegliche Einordnung A: [OPTION A] — Argument: [BEGRUENDUNG]
 Moegliche Einordnung B: [OPTION B] — Argument: [BEGRUENDUNG]
 Entscheidung erbeten bis: [DATUM]

--- NAECHSTE SCHRITTE ---
1. [AKTION] — verantwortlich: [PERSON] — Frist: [DATUM]
2. [AKTION] — verantwortlich: [PERSON] — Frist: [DATUM]
```

<!-- BEGIN ausformulierungspflicht (autogen) -->
> **Ausformulierungspflicht und Formatstandard.** Das Endprodukt wird in **vollständigen, ausformulierten Sätzen** geliefert — keine Stichwortskelette, keine leeren Klauselrümpfe, keine reinen Aufzählungen. Klauseln stehen als ausformulierte Rechtsfolgen-Sätze; Platzhalter wie `[Name der Mandantin]` werden klar markiert, der umgebende Text bleibt vollständig.
>
> **Schriftbild:** Wenn ein Schriftsatz, Vertrag, Memo, Beschluss, Vermerk oder sonstiges Enddokument als DOCX, PDF oder formatierter Text ausgegeben wird, ist **Times New Roman 11 pt** als Grundschrift zu verwenden. Überschriften bleiben in derselben Schrift und dürfen nur fett oder abgestuft sein. Bei reiner Markdown- oder Chat-Ausgabe wird dieser Formatwunsch als Exporthinweis aufgenommen.
>
> **Nummerierung:** Gliederung ausschließlich dezimal (`1`, `1.1`, `1.1.1` und so weiter). Keine römischen Ziffern, keine Buchstaben- oder Mischgliederung.
<!-- END ausformulierungspflicht (autogen) -->
