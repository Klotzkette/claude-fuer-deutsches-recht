---
name: stb-datentransfer-mandant-cloud-dsgvo
description: "Datentransfer Mandant zu Cloud DSGVO-Aspekte. Anwendungsfall Pruefung der DSGVO-Konformitaet beim Cloud-Datentransfer AVV Auftragsverarbeitung TOM technisch-organisatorische Massnahmen Drittlandtransfer. Methodik Pruefliste. Output DSGVO-Compliance-Dokument."
---

# Datentransfer Mandant-Cloud — DSGVO-Aspekte

## Kernsachverhalt

Beim Datentransfer zwischen Mandant, StB und Cloud-Dienstleistern muss DSGVO-Konformitaet sichergestellt sein. Wesentliche Aspekte: AVV nach Art. 28 DSGVO mit jedem Auftragsverarbeiter, TOM (technisch-organisatorische Massnahmen), Drittlandtransfer-Pruefung (USA-Server problematisch), Einhaltung der Daten-Minimierung. Bei Verstoss: Bussgeld bis 4 Prozent Jahresumsatz.

## Kaltstart-Rueckfragen

1. Welche Cloud-Dienstleister sind im Einsatz (DATEV, BuchhaltungsButler, sevDesk, Microsoft, Google)?
2. Liegen AVV mit allen Auftragsverarbeitern vor?
3. Welche Daten werden gespeichert (Mandantendaten, Lohndaten, Mitarbeiterdaten)?
4. Welcher Server-Standort (EU, Drittland)?
5. Welche TOM-Massnahmen?
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

- Aufsichtsbehoerden DSK-Beschluesse.
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

### Phase 2 — AVV-Pruefung Art. 28 DSGVO

- Schriftlicher AVV-Vertrag.
- Inhalte: Verarbeitungstaetigkeit, Daten-Kategorien, TOM-Bestimmungen, Sub-Verarbeiter, Pflichten beidseitig.
- Aktualitaet pruefen.

### Phase 3 — Drittlandtransfer Pruefung

- USA-Server: nach Schrems II zusaetzliche Massnahmen erforderlich.
- Standardvertragsklauseln (SCC).
- Transfer Impact Assessment (TIA).
- Bei sensiblen Daten (Mandantenidentifizier, Gesundheitsdaten): EU-Server bevorzugen.

### Phase 4 — TOM-Massnahmen

| Bereich | Massnahmen |
|---|---|
| Vertraulichkeit | Verschluesselung Transport (TLS), Verschluesselung at-rest |
| Integritaet | Hashverfahren, Audit-Logs |
| Verfuegbarkeit | Backup, Redundanz |
| Belastbarkeit | Disaster Recovery |
| Wiederherstellbarkeit | Backup-Restore |
| Pruefverfahren | Regelmaessige Audits |
| Pseudonymisierung | wo moeglich |

### Phase 5 — Mandantenkommunikation

- Datenschutzhinweise gem. Art. 13 DSGVO bei Mandatsaufnahme.
- Information bei wesentlichen Aenderungen.
- Mandantenanfragen Art. 15 DSGVO beantworten.

### Phase 6 — Datenschutz-Folgenabschaetzung (DSFA)

- Bei umfangreicher Verarbeitung personenbezogener Daten.
- Bei systematischer Profilbildung.
- Bei besonderen Datenkategorien.

## Output

- DSGVO-Compliance-Dokument.
- AVV-Mappe.
- TOM-Massnahmen-Liste.

## Strategie und Praxis-Tipps

- Die Berufsverschwiegenheit nach § 57 StBerG ist durch § 203 Abs. 1 Nr. 3 StGB strafrechtlich abgesichert; die Einbeziehung externer Dienstleister (Cloud-Anbieter) erfordert nach § 203 Abs. 3, 4 StGB die schriftliche Verpflichtung des Dienstleisters auf die Schweigepflicht — entsprechende Klauseln im AVV pruefen.
- Schrems II (EuGH v. 16.07.2020, C-311/18) hat den Privacy Shield gekippt; bei USA-Cloud-Diensten zusaetzliche Schutzmassnahmen (Standardvertragsklauseln, Transfer Impact Assessment, ggf. Verschluesselung) zwingend; EU-Hosting bevorzugen.
- DSGVO-Bussgelder bis 20 Mio. EUR oder 4 % des weltweiten Jahresumsatzes (Art. 83 Abs. 5 DSGVO) — Compliance unverzichtbar.
- Jaehrliche DSGVO-Pruefung im Kanzleiteam (Verzeichnis Verarbeitungstaetigkeiten, AVV-Mappe, TOM-Liste aktualisieren).
- StBVV: DSGVO-Compliance-Beratung fuer Mandanten als separater Auftrag nach § 13 StBVV (Beratung) oder als Bestandteil der Buchfuehrungspauschale.

## Querverweise

- `stb-online-portal-datev-mandantenshop` — DUO.
- `stb-buchhaltungsbutler-mandantencloud` — Cloud.
- `stb-ki-tools-im-stb-betrieb-grenzen-berufsrecht` — KI-Tools.

## Quellen und Updates

Stand: 05/2026.

- DSGVO Art. 5, 13, 28, 32, 44-50.
- StBerG § 57.
- StGB § 203.
- Schrems II-Urteil EuGH.
- DSK-Beschluesse.
