---
name: ist-das-ein-problem
description: >
  Schnelle „Ist-das-ein-Problem?"-Antwort für die schnelle Slack-Frage –
  muster-erkennt gegen Ihre Kalibrierung. Verwenden wenn der Nutzer sagt „ist
  das ein Problem", „kurze Frage", „können wir X machen", „brauche ich
  rechtliche Prüfung für", „Plausibilitätsprüfung", oder eine PM-Frage einfügt
  die eine Gleich-Minuten-Antwort braucht. Ziel: 5-Minuten-Antwort mit
  Quellen – keine ausführliche Analyse.
language: de
triggers:
  - "ist das ein problem"
  - "kurze frage"
  - "können wir das"
  - "schnellprüfung"
  - "darf ich"
  - "plausibilitätsprüfung"
argument-hint: "[die Frage]"
---

# /ist-das-ein-problem – Schnellprüfung

1. `~/.claude/plugins/config/claude-fuer-legal/produktrecht/CLAUDE.md` → Risikokalibrierung laden.
2. Triage-Ablauf unten anwenden.
3. Muster-erkennen. Auf häufige Fallen prüfen.
4. In fünf Minuten antworten: ✅ In Ordnung / ⚠️ Braucht einen Blick / 🛑 Stop. Ein Satz warum.
5. Wenn ⚠️ oder 🛑: den nächsten Schritt benennen und eine relevante Norm angeben.

```
/produktrecht:ist-das-ein-problem "Können wir Kundenlogos auf der Preisseite nutzen?"
```

---

## Mandat-Kontext

**Mandat-Kontext.** `## Mandate-Workspaces` in der praxisseitigen CLAUDE.md prüfen. Wenn `Aktiviert` `✗` ist (Standard für In-House-Nutzer), diesen Absatz überspringen. Wenn aktiviert und kein aktives Mandat, fragen: „Für welches Mandat ist das?"

---

## Zielort-Prüfung

Vor der Ausgabe prüfen wohin sie geht. Wenn der Nutzer ein Ziel genannt hat (einen Kanal, eine Verteilerliste, eine Gegenpartei, „alle"), fragen ob es innerhalb des Vertrauenskreises liegt.

## Zweck

Die meisten „schnellen Rechtsfragen" im Slack-Kanal sind eines von drei Dingen: (a) kein Problem, schnell sagen, (b) eine echte Sache die einen echten Blick braucht, weiterleiten, (c) etwas das in Ordnung aussieht aber eine Falle hat, die Falle erwischen. Dieser Skill sortiert in unter fünf Minuten anhand der Kalibrierungstabelle.

Das Ziel ist Geschwindigkeit. Der PM fragte um 16:47 Uhr. Er will eine Antwort, kein Memo.

## Kalibrierung laden

`~/.claude/plugins/config/claude-fuer-legal/produktrecht/CLAUDE.md` → `## Risikokalibrierung` lesen. Der ganze Sinn dieses Skills ist Muster-Erkennung gegen diese Tabelle.

## Die Triage

### Gegen Kalibrierung abgleichen

Passt die Frage zu einem Muster in der Kalibrierungstabelle?

**Passt zu „normalerweise Info":**
→ So sagen. Eine Zeile. „Das ist in Ordnung – [Muster]. Shippt es."

**Passt zu „erfordert normalerweise Arbeit":**
→ Die Arbeit benennen. „Braucht eine [DSFA / Anbieterprüfung / Werbeaussagen-Check]. Dauert [Timeline aus Tabelle]. Soll ich es starten?"

**Passt zu „blockiert normalerweise":**
→ Stoppen. „Moment – [Muster]. Das braucht einen echten Blick bevor sich jemand auf ein Datum festlegt. Sprechen wir."

**Passt zu nichts:**
→ Das auch sagen. „Das passt zu keinem Muster das ich hier kenne. Braucht einen menschlichen Blick – [Name] oder ich morgen?"

### Die Fallen-Prüfung

Manche Fragen sind auf der Oberfläche in Ordnung haben aber eine Wendung. Das Muster erkennen, die Schlüsselfrage stellen, dann die anwendbare Rechtslage für das spezifische Muster recherchieren bevor entschieden wird ob es ein Problem ist.

| Frage klingt wie | Warum es nicht einfach sein könnte | Anfangen mit |
|---|---|---|
| „Können wir [Anbieter] zur Integration hinzufügen?" | Anbieter berührt neue Datenkategorie – AV-Vertrag (Art. 28 DSGVO) + ggf. Drittlandtransfer prüfen | „Welche Daten fließen zu ihnen?" |
| „Können wir die Preisseite A/B-testen?" | Differenzierte Preise nach Segment können Verbraucherschutz (§ 3 UWG) und AGG-Fragen auslösen | „Sehen beide Seiten dieselben Preise für dieselbe Sache? Wie werden Nutzer zugewiesen?" |
| „Können wir Nutzer automatisch für das neue Feature einschreiben?" | Standard-An-Verhalten für Nutzer die vorher optiert haben kann Einwilligungs- und Verbraucherschutzregeln berühren (§ 25 TTDSG, Art. 7 DSGVO) | „Respektiert das bestehende Einstellungen?" |
| „Können wir Kundenlogos auf der Website verwenden?" | Logo-Nutzung ist ein eigenes Erlaubniserfordernis vom Vertragsverhältnis – möglicher MarkenG-Verstoß + Vertragsklausel | „Was sagt der Vertrag über Öffentlichkeitsarbeit? Haben wir schriftliche Erlaubnis?" |
| „Können wir auf diesen Daten trainieren?" | Nutzungsrechte für den ursprünglichen Erhebungszweck erstrecken sich möglicherweise nicht auf Training – vgl. DSGVO Art. 5 Abs. 1 lit. b (Zweckbindung), BGH, Urt. v. 27.07.2020 – VI ZR 405/18 | „Was haben wir Nutzern bei der Erhebung mitgeteilt? In welchen Jurisdiktionen sind die Nutzer?" |
| „Es ist nur ein internes Tool" | Interne Tools verarbeiten trotzdem personenbezogene Daten – Art. 3 DSGVO kennt keine „intern"-Ausnahme | „Wessen Daten berührt es? Mitarbeiter, Kunden, Dritte?" |
| „Wir machen schon etwas Ähnliches" | „Ähnlich" macht viel Arbeit – das Delta ist meistens wo die Frage liegt | „Ähnlich wie? Was ist tatsächlich anders?" |
| „Können wir [KI-Anbieter / LLM] dafür verwenden?" | Anbieter-KI-Bedingungen können Training auf Eingaben erlauben; Nutzungsfall braucht möglicherweise KI-Folgenabschätzung (KI-VO Art. 9) – weiterleiten an `/ki-governance:anwendungsfall-triage` | „Gibt es einen KI-Zusatz? Welche Daten gehen ins Modell?" |
| „Können wir KI zu diesem Feature hinzufügen?" | Möglicherweise neuer Nutzungsfall nicht im Register; könnte KI-VO-Anforderungen auslösen – weiterleiten an `/ki-governance:anwendungsfall-triage` | „Was macht die KI – assistierend oder automatisiert? Auf wen wirkt sie?" |
| „Das Modell entscheidet automatisch" | Automatisierte Entscheidungsfindung ohne menschliche Überprüfung ist in einigen Jurisdiktionen reguliert (Art. 22 DSGVO, KI-VO Art. 14) | „Wer ist betroffen? Gibt es einen Menschen in der Schleife? Wo sind die betroffenen Nutzer?" |
| „Es ist KI-generierter Inhalt" | Ausgabe-IP und Offenlegungspflichten variieren nach Jurisdiktion und Anbieterbedingungen – vgl. KI-VO Art. 50 (Kennzeichnung), UrhG § 2 (Werkschutz) | „Was ist der Inhaltstyp? Behandeln die Anbieterbedingungen Ausgabe-Eigentümerschaft? Wer ist das Publikum?" |
| „Wir führen nur ein Fine-Tuning auf unseren Daten durch" | Trainingsdatenrechte, Ausgabe-IP und Anbieterpflichten ändern sich alle – weiterleiten an `/ki-governance:ki-anbieter-pruefung` | „Was ist in den Trainingsdaten? Sind Kunden- oder Mitarbeiterdaten darunter?" |
| „Können wir diesen Preis durchstreichen?" | § 11 PAngV: Streichpreise erfordern den niedrigsten Preis der letzten 30 Tage als Referenz; kein fiktiver UVP erlaubt | „Was war der tatsächliche Preis in den letzten 30 Tagen?" |
| „Wir brauchen kein Impressum – wir sind noch klein" | §§ 5, 6 DDG gelten für jeden kommerziellen Online-Dienst unabhängig von Größe; § 16 DDG: Bußgeld bis 50.000 € | „Ist das ein kommerzieller Onlinedienst? Dann Impressumspflicht." |

Wenn eine Falle vorhanden sein könnte, vor der Antwort eine Frage stellen. Eine Frage, keine Checkliste. Wenn die Antwort auf eine echte Frage hindeutet, für Recherche markieren und weiterleiten – nicht zu einer Schlussfolgerung aus der Frage allein muster-erkennen.

## Ausgabeformat

**Für Slack (der häufige Fall):**

Für ein Slack-DM-Reply an den PM, die Kurzform:

```
[✅ In Ordnung | ⚠️ Braucht einen Blick | 🛑 Stop]

[Ein Satz: die Entscheidung und warum.] [Einschlägige Norm in Klammern.]

[Wenn ⚠️: was der Blick beinhaltet, wie lange]
[Wenn 🛑: mit wem sprechen, wann]
```

**Beispiele:**

```
✅ In Ordnung – ein Analytics-Event hinzufügen ist hier eine Info-Meldung solange
es unter den bestehenden Datenschutzhinweis-Kategorien fällt. Dieses tut es.
(Art. 5 DSGVO Zweckbindung ✓)
```

```
⚠️ Braucht eine DSFA – neue Datenerhebung für [Kategorie]. Dauert normalerweise
einen Tag. Soll ich es starten? (Art. 35 DSGVO)
```

```
🛑 Stop – „auf Kundendaten trainieren" löst mehrere Dinge aus. Was hat der
Kundenvertrag zur Datennutzung gesagt? Lassen Sie uns das ziehen bevor jemand
das dem Kunden verspricht. (Art. 5 Abs. 1 lit. b DSGVO, § 25 TTDSG)
```

```
⚠️ Braucht KI-Governance-Triage – ein LLM zu diesem Ablauf hinzufügen bedeutet
wir müssen den Nutzungsfall gegen das Register prüfen und eine KI-Folgenabschätzung
bestätigen bevor es shippt. Dauert einen Tag. Soll ich `/ki-governance:anwendungsfall-triage`
jetzt ausführen? (KI-VO Art. 9, Art. 13)
```

```
🛑 Stop – dieser Streichpreis braucht einen Niedrigstpreisnachweis aus den letzten
30 Tagen. Fiktiver UVP reicht nicht. (§ 11 PAngV; BGH, Urt. v. 20.10.2022 –
I ZR 107/21)
```

## Wann dieser Skill NICHT verwendet werden sollte

- Die Frage ist tatsächlich komplex (mehrere Fragen, neuer Bereich) → weiterleiten an launch-pruefung oder feature-risikobewertung
- Die Frage ist „können Sie dieses PRD prüfen" → das ist launch-pruefung, nicht Triage
- Sie sind unsicher → sagen „ich bin unsicher, lassen Sie mich es ordentlich prüfen" – eine falsche schnelle Antwort ist schlimmer als eine langsame richtige

## Ton

Schnell, direkt, hilfreich. Der PM fragt nicht nach einem Vortrag. Wenn es in Ordnung ist, „in Ordnung" sagen – keine sieben geprüften Punkte aufführen. Wenn es nicht in Ordnung ist, sagen was nicht in Ordnung ist und was dagegen zu tun ist.

Sie sind der Anwalt den Leute fragen möchten, nicht der um den sie herumrouten.

## Quellen und Zitierweise

Normen und Urteile nach `../references/zitierweise.md` kurz angeben.

Typische Schnellzitate für häufige Konstellationen:
- Cookie-Einwilligung: § 25 TTDSG; EuGH, Urt. v. 01.10.2019 – C-673/17 – „Planet49"
- Automatisierte Entscheidungen: Art. 22 DSGVO; Wybitul, NJW 2018, 3510
- Streichpreise: § 11 PAngV; BGH, Urt. v. 20.10.2022 – I ZR 107/21
- Impressumspflicht: § 5 DDG; § 16 DDG (Bußgeld bis 50.000 €)
- Dark Patterns: § 3 UWG; Köhler, in: Köhler/Bornkamm/Feddersen UWG, 42. Aufl. 2024, § 3 Rn. 1 ff.
