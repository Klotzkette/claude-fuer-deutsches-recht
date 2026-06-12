---
name: datentransfer-mandant-cloud-dsgvo
description: "Datentransfer Mandant zu Cloud DSGVO-Aspekte. Anwendungsfall Prüfung der DSGVO-Konformität beim Cloud-Datentransfer AVV Auftragsverarbeitung TOM technisch-organisatorische Maßnahmen Drittlandtransfer. Methodik Prüfliste. Output DSGVO-Compliance-Dokument."
---

# Datentransfer Mandant-Cloud — DSGVO-Aspekte

## Fachlicher Anker

- **Normen:** § 6a, Art. 28 DSGVO, § 57.
- **Entscheidungs-/Quellenanker:** Tragende Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle einsetzen; keine Entscheidung aus Modellwissen erzwingen.
- **Quellenhygiene:** `references/quellenhygiene.md` und `references/zitierweise.md` beachten.

## Kernsachverhalt

Beim Datentransfer zwischen Mandant, StB und Cloud-Dienstleistern muss DSGVO-Konformitaet sichergestellt sein. Wesentliche Aspekte: AVV nach Art. 28 DSGVO mit jedem Auftragsverarbeiter, TOM (technisch-organisatorische Maßnahmen), Drittlandtransfer-Prüfung (USA-Server problematisch), Einhaltung der Daten-Minimierung. Bei Verstoss: Bussgeld bis 4 Prozent Jahresumsatz.

## Kaltstart-Rueckfragen

1. Welche Cloud-Dienstleister sind im Einsatz (DATEV, BuchhaltungsButler, sevDesk, Microsoft, Google)?
2. Liegen AVV mit allen Auftragsverarbeitern vor?
3. Welche Daten werden gespeichert (Mandantendaten, Lohndaten, Mitarbeiterdaten)?
4. Welcher Server-Standort (EU, Drittland)?
5. Welche TOM-Maßnahmen?
6. Welche Mandantenkommunikation Datenschutzhinweise?
7. Welche Sicherheits-Vorfaelle in der Vergangenheit?
8. Welche Berufsverschwiegenheit (§ 57 StBerG)?

## Rechtlicher Rahmen

### Primaernormen

**DSGVO Art. 5** — Grundsaetze.

**DSGVO Art. 28** — Auftragsverarbeiter.

**DSGVO Art. 32** — Sicherheit der Verarbeitung.

**DSGVO Art. 44-50** — Drittlandtransfer.

**§ 57 Abs. 1 StBerG** — Verschwiegenheit.

**§ 203 StGB** — Verletzung Berufsgeheimnis.

### Verwaltungsanweisungen

- Aufsichtsbehoerden DSK-Beschlüsse.
- Schrems II-Urteil EuGH (Drittlandtransfer USA).

## Workflow

### Phase 1 — Auftragsverarbeitungs-Inventar

| Dienstleister | Datenart | EU-Server | AVV |
|---|---|---|---|
| DATEV | Mandantendaten | Ja | Ja |
| Microsoft 365 | E-Mail, Office | Teilweise EU | Ja, mit Standardvertragsklauseln |
| Google Workspace | E-Mail, Storage | EU/USA | Ja |
| BuchhaltungsButler | Mandanten-Buchhaltung | EU | Ja |
| Zoom | Videokonferenz | Mix | Ja |

### Phase 2 — AVV-Prüfung Art. 28 DSGVO

- Schriftlicher AVV-Vertrag.
- Inhalte: Verarbeitungstaetigkeit, Daten-Kategorien, TOM-Bestimmungen, Sub-Verarbeiter, Pflichten beidseitig.
- Aktualitaet prüfen.

### Phase 3 — Drittlandtransfer Prüfung

- USA-Server: nach Schrems II zusaetzliche Maßnahmen erforderlich.
- Standardvertragsklauseln (SCC).
- Transfer Impact Assessment (TIA).
- Bei sensiblen Daten (Mandantenidentifizier, Gesundheitsdaten): EU-Server bevorzugen.

### Phase 4 — TOM-Maßnahmen

| Bereich | Maßnahmen |
|---|---|
| Vertraulichkeit | Verschluesselung Transport (TLS), Verschluesselung at-rest |
| Integritaet | Hashverfahren, Audit-Logs |
| Verfuegbarkeit | Backup, Redundanz |
| Belastbarkeit | Disaster Recovery |
| Wiederherstellbarkeit | Backup-Restore |
| Prüfverfahren | Regelmäßige Audits |
| Pseudonymisierung | wo möglich |

### Phase 5 — Mandantenkommunikation

- Datenschutzhinweise gem. Art. 13 DSGVO bei Mandatsaufnahme.
- Information bei wesentlichen Änderungen.
- Mandantenanfragen Art. 15 DSGVO beantworten.

### Phase 6 — Datenschutz-Folgenabschaetzung (DSFA)

- Bei umfangreicher Verarbeitung personenbezogener Daten.
- Bei systematischer Profilbildung.
- Bei besonderen Datenkategorien.

## Strategie und Praxis-Tipps

- Die Berufsverschwiegenheit nach § 57 StBerG ist durch § 203 Abs. 1 Nr. 3 StGB strafrechtlich abgesichert; die Einbeziehung externer Dienstleister (Cloud-Anbieter) erfordert nach § 203 Abs. 3, 4 StGB die schriftliche Verpflichtung des Dienstleisters auf die Schweigepflicht — entsprechende Klauseln im AVV prüfen.
- Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- DSGVO-Bussgelder bis 20 Mio. EUR oder 4 % des weltweiten Jahresumsatzes (Art. 83 Abs. 5 DSGVO) — Compliance unverzichtbar.
- Jaehrliche DSGVO-Prüfung im Kanzleiteam (Verzeichnis Verarbeitungstaetigkeiten, AVV-Mappe, TOM-Liste aktualisieren).
- StBVV: DSGVO-Compliance-Beratung für Mandanten als separater Auftrag nach § 13 StBVV (Beratung) oder als Bestandteil der Buchfuehrungspauschale.

## Quellen und Updates

Stand: 05/2026.

- DSGVO Art. 5, 13, 28, 32, 44-50.
- StBerG § 57.
- StGB § 203.
- Schrems II-Urteil EuGH.
- DSK-Beschlüsse.
