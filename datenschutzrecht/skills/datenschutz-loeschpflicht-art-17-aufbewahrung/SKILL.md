---
name: datenschutz-loeschpflicht-art-17-aufbewahrung
description: "Konflikt Loeschpflicht Art. 17 DSGVO und Aufbewahrungspflichten HGB § 257 AO § 147 GoBD geordnet aufloesen. Sieben-Fragen-Diagnose: Datenkategorie Verarbeitungszweck Rechtsgrundlage konkurrierende Pflicht Sperrung statt Loeschung Backup-Strategie Drittweitergabe. Schritt-für-Schritt: NICHT pausch..."
---

# Datenschutz Loeschpflicht — Art. 17 DSGVO und Aufbewahrung

## Wann dieses Modul hilft / Kaltstart-Fragen

Sie brauchen den Skill, sobald (a) ein Loeschantrag eingeht, (b) Daten ohne Antrag rechtmaessig zu loeschen waeren oder (c) ein Loeschkonzept erstellt werden soll.

Sieben-Fragen-Diagnose:

1. **Datenkategorie:** Kunden-, Mitarbeiter-, Bewerber-, Buchhaltungs-, Vertragsdaten?
2. **Verarbeitungszweck:** Welcher Zweck rechtfertigte die Verarbeitung, ist er noch aktuell?
3. **Rechtsgrundlage:** Art. 6 I a-f? Einwilligung widerrufbar Art. 7 III?
4. **Konkurrierende Aufbewahrungspflicht:** § 257 HGB sechs/zehn Jahre, § 147 AO acht/zehn Jahre, GoBD, § 17 GwG, sozialversicherungsrechtlich?
5. **Sperrung statt Loeschung:** Ist Art. 18 DSGVO einschlaegig?
6. **Backup-Strategie:** Werden Daten auch in Backups gehalten? Konzept für Loeschung Backup oder nur Produktivsystem?
7. **Drittweitergabe:** Art. 19 DSGVO Mitteilungspflicht?

## Rechtlicher Rahmen

- **Art. 17 I DSGVO** Loeschpflicht bei: (a) Zweckwegfall, (b) Widerruf Einwilligung, (c) Widerspruch Art. 21, (d) unrechtmäßige Verarbeitung, (e) gesetzliche Pflicht zur Loeschung, (f) Kinderdaten Art. 8.
- **Art. 17 II DSGVO** verstaerkte Pflicht bei öffentlich gemachten Daten — Mitteilung an andere Verantwortliche (EuGH C-460/20 Google "Right to be Forgotten").
- **Art. 17 III DSGVO** Ausnahmen: (a) Meinungs- und Informationsfreiheit, (b) rechtliche Verpflichtung, (c) öffentliches Interesse Gesundheit, (d) Archivzwecke, (e) Rechtsverteidigung.
- **Art. 18 DSGVO** Einschraenkung (Sperrung) — als Alternative wenn Loeschung nicht möglich.
- **Art. 19 DSGVO** Mitteilungspflicht gegenueber Empfaengern.
- **§ 257 HGB** Aufbewahrung Handelsbuecher zehn Jahre; Handelsbriefe sechs Jahre.
- **§ 147 AO** Aufbewahrung Buchungsbelege zehn Jahre (Stand 2026 nach Wachstumschancengesetz acht Jahre für bestimmte Belege), sonstige sechs Jahre.
- **§ 17 GwG** Mindestaufbewahrung Sorgfaltspflicht-Dokumentation fuenf Jahre, bis zu zehn.
- **§ 28 SGB IV** sozialversicherungsrechtliche Aufbewahrung.
- **EuGH C-129/21 Proximus** (Urteil 27.10.2022): Verantwortlicher muss bei Änderung der Verarbeitungslage selbst Maßnahmen ergreifen.
- **EuGH C-460/20 Google** (Urteil 08.12.2022): Recht auf Aushebung von Verlinkung bei Falschangaben.

## Mandantenfuehrung Schritt-für-Schritt

1. **Zuerst:** Loeschkonzept beim Mandanten anfordern oder erstellen. Ohne Konzept keine geordnete Loeschung.
2. **Als zweites:** Pro Datenkategorie prüfen — Aufbewahrungspflicht ja oder nein? Falls ja, bis wann?
3. **Als drittes:** **NICHT pauschal alles loeschen.** Auch nicht "vorsorglich". Loeschungen müssen dokumentiert werden.
4. **Als viertes:** Wenn Aufbewahrungspflicht besteht: Sperrung Art. 18 DSGVO bzw. Zugriffsbeschraenkung nach § 35 III BDSG, mit Sperrvermerk.
5. **Als fuenftes:** Backup-Strategie — moderne Praxis: Sperrung im Produktivsystem, Loeschung aus Backup bei naechstem Lifecycle.
6. **NICHT erst loeschen, dann auf Auskunft Art. 15 antworten** — Auskunftsobjekt entfaellt.
7. **NICHT** Aufsicht informieren, dass Daten nicht geloescht werden können, ohne Mandantenfreigabe.

## Trade-off-Matrix

| Variante | Vorteil | Nachteil |
|---|---|---|
| Sofortige Loeschung Produktivsystem | Erfuellt Art. 17 sichtbar | Risiko Verletzung Aufbewahrungspflicht |
| Sperrung Art. 18 + Loeschung bei Ablauf | Saubere Konfliktloesung | Aufwand, technisch nicht immer einfach |
| Pseudonymisierung | Reduziert Personenbezug | Re-Identifizierung möglich, kein voller Schutz |
| Pauschale Ablehnung mit Verweis HGB AO | Schnell | Aufsicht prüft Einzelpflicht |

## Mustertexte

### Ablehnungsschreiben (Sperrung statt Loeschung)

> Sehr geehrte/r [Name],
>
> Ihrem Antrag auf Loeschung nach Art. 17 DSGVO können wir vollumfaenglich nicht entsprechen. Hintergrund ist eine konkurrierende gesetzliche Aufbewahrungspflicht nach § 257 HGB / § 147 AO / § 17 GwG (zutreffend einsetzen). Daher findet die Ausnahme nach Art. 17 Abs. 3 lit. b DSGVO Anwendung.
>
> Wir haben Ihre Daten gemäß Art. 18 DSGVO in der Verarbeitung eingeschraenkt (Sperrvermerk). Die Daten werden mit Ablauf der gesetzlichen Aufbewahrungspflicht am [Datum] vollstaendig geloescht. Bis dahin werden die Daten nur für den oben genannten Aufbewahrungszweck verarbeitet.
>
> Ihr Beschwerderecht nach Art. 77 DSGVO bei [zuständige Aufsichtsbehoerde] bleibt unberuehrt.

### Sperrvermerk (intern)

```
Datenkategorie: [konkret]
Betroffener: [Name]
Sperrgrund: [Aufbewahrungspflicht § X HGB / § Y AO]
Sperrbeginn: [Datum]
Voraussichtliche Loeschung: [Datum]
Zugriffsbeschraenkung: [nur Buchhaltung / nur für Pruefung]
DSB benachrichtigt: [ja/nein]
```

### Loeschkonzept-Skizze (intern)

```
Datenkategorie 1 (Buchhaltungsdaten): § 147 AO 10 Jahre → Loeschung Jahr 11
Datenkategorie 2 (Handelsbriefe): § 257 II HGB 6 Jahre → Loeschung Jahr 7
Datenkategorie 3 (Bewerberdaten): regelmaessig 6 Monate (Diskriminierungspraevention § 15 IV AGG)
Datenkategorie 4 (Mitarbeiter aktiv): waehrend Beschaeftigung + Aufbewahrungspflicht steuerlich
Datenkategorie 5 (Marketing): nach Widerruf / Widerspruch sofort
```

## Typische Fehler

- "DSGVO sagt loeschen" — Aufbewahrungspflicht uebersehen.
- "HGB sagt aufbewahren" — Sperrungspflicht Art. 18 DSGVO uebersehen.
- Loeschung nicht protokolliert.
- Backup-System wird vergessen.
- Recht auf Vergessenwerden Art. 17 II nicht beachtet bei öffentlich gemachten Daten.

**Was triggert die Aufsichtsbehoerde?** Pauschale Ablehnungen ohne konkrete Norm, kein Loeschkonzept, keine Sperrvermerke, fehlende Backup-Strategie.

## Quellen Stand 06/2026

- DSGVO Art. 17, 18, 19, 77.
- BDSG § 35.
- HGB § 257.
- AO § 147 (in der Fassung nach Wachstumschancengesetz 2024).
- GwG § 17.
- AGG § 15.
- EuGH C-129/21 Proximus, Urteil 27.10.2022.
- EuGH C-460/20 Google, Urteil 08.12.2022.
- Keine Aufsatzfundstellen aus Modellwissen.
