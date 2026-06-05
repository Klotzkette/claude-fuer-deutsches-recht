---
name: db-data-act-bei-backup-export
description: "Db Data Act Zugang Iot / Db Datenbankrecht Bei Saas Cloudmigration / Db Backup Export Vendor Lock: führt durch diese fachlich verbundenen Arbeitsmodule, wählt den passenden Prüfpfad und erzeugt den nächsten belastbaren Output."
---

# Db Data Act Zugang Iot / Db Datenbankrecht Bei Saas Cloudmigration / Db Backup Export Vendor Lock

## Arbeitsbereich

Dieser Skill bündelt **Db Data Act Zugang Iot / Db Datenbankrecht Bei Saas Cloudmigration / Db Backup Export Vendor Lock**. Wähle zuerst das Modul, dessen Tatsachen die Akte tragen; kombiniere weitere Module nur, wenn dieselbe Frist, Zuständigkeit, Beweislast oder derselbe Output dadurch wirklich klarer wird.

## Arbeitsmodule

| Arbeitsmodul | Fokus |
| --- | --- |
| `db-035-data-act-und-zugang-zu-iot-daten` | Data Act (EU-VO 2023/2854) und Zugang zu IoT-Daten im Verhältnis zum Datenbankherstellerrecht: Art. 4-8 Data Act (Nutzerzugangsrechte), Art. 17 (Wechselrecht Cloud), Verhältnis zu §§ 87a-87e UrhG, Betriebs- und Geschäftsgeheimnisschutz als Grenze und DSGVO-Schnittmenge. Erstellt Compliance-Konzept für IoT-Hersteller und Dateninhaber. |
| `db-036-datenbankrecht-bei-saas-und-cloudmigration` | Datenbankrecht bei SaaS-Diensten und Cloud-Migrationen: Inhaberschaft am Datenbankherstellerrecht (§ 87a UrhG) bei SaaS-Betrieb, Datenmitnahme bei Anbieterwechsel (Data Act Art. 17), AGB-Klauseln zur Datenbankzuweisung, Auftragsverarbeitung nach Art. 28 DSGVO und Vendor-Lock-in-Risiken bei propriet­ären Datenbankformaten. Erstellt Vertragsklauseln für SaaS-Kunden. |
| `db-037-backup-export-und-vendor-lock-in` | Datenbankrecht bei Backup-Rechten, Datenexport und Vendor-Lock-in: § 87c UrhG erlaubte Entnahmen für rechtmäßige Nutzer, vertragliche Backup-Klauseln, Data Act Art. 17 Wechselrecht, Exportformat-Anforderungen und rechtliche Mittel gegen Lock-in-Strategien. Bewertet AGB-Wirksamkeit von Export-Verboten und erstellt Vertragsklauseln für Datenmitnahme. |

## Arbeitsweg

Für **Db Data Act Zugang Iot / Db Datenbankrecht Bei Saas Cloudmigration / Db Backup Export Vendor Lock** zuerst das Arbeitsmodul wählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Im Plugin `datenbankrecht` bleiben Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschter Output getrennt; Module nur kombinieren, wenn dieselbe Akte mehrere dieser Punkte trägt. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Arbeitsmodule im Detail

## 1. `db-035-data-act-und-zugang-zu-iot-daten`

**Fokus:** Data Act (EU-VO 2023/2854) und Zugang zu IoT-Daten im Verhältnis zum Datenbankherstellerrecht: Art. 4-8 Data Act (Nutzerzugangsrechte), Art. 17 (Wechselrecht Cloud), Verhältnis zu §§ 87a-87e UrhG, Betriebs- und Geschäftsgeheimnisschutz als Grenze und DSGVO-Schnittmenge. Erstellt Compliance-Konzept für IoT-Hersteller und Dateninhaber.

# Data Act und Zugang zu IoT-Daten — Verhältnis zum Datenbankherstellerrecht

## Mandantenfall

- Maschinenbauer (IoT-Gerätehersteller) fragt, welche Datenzugangspflichten der Data Act für seine Sensordaten begründet und ob das Datenbankherstellerrecht dem entgegensteht.
- B2B-Kunde eines IoT-Anbieters verlangt nach Art. 4 Data Act Zugang zu den Maschinendaten, die sein Gerät erzeugt — welche Pflichten bestehen?
- Cloud-Anbieter will wissen, wie er das Wechselrecht (Art. 17 Data Act) für Kundendaten implementiert und welche Datenbankrechte dabei betroffen sind.

## Erste Schritte

1. Data-Act-Anwendungsbereich prüfen: Gilt die VO 2023/2854 für den konkreten IoT-Dienst (ab 12. September 2025 anwendbar)?
2. Zugangsrecht nach Art. 4 Data Act bestimmen: Nutzer hat Recht auf Zugang zu von seinem Gerät generierten Daten — direkt oder über Dritte.
3. Verhältnis zu Datenbankherstellerrecht prüfen: Art. 4 Abs. 6 Data Act — Zugangsrecht verdrängt nicht das Datenbankherstellerrecht vollständig; aber Dateninhaber kann Zugang nicht mit Herstellerrecht blockieren.
4. Betriebs- und Geschäftsgeheimnisschutz als Grenze: Art. 4 Abs. 6 Data Act erlaubt Verweigerung bei erheblichem Schutz von Betriebsgeheimnissen.
5. Wechselrecht Cloud (Art. 17 Data Act): Kunde kann zu anderem Cloud-Anbieter wechseln und seine Daten mitnehmen — Datenbankherstellerrecht des alten Anbieters?
6. DSGVO-Schnittmenge bei personenbezogenen IoT-Daten: Art. 1 Abs. 3 Data Act stellt klar, dass DSGVO unberührt bleibt.

## Rechtsrahmen

- Data Act VO 2023/2854 Art. 4: Zugangsrecht des Nutzers zu von seinem IoT-Gerät generierten Daten.
- Data Act Art. 6: Bedingungen für Datenweitergabe an Dritte — Verbote unangemessener Bedingungen.
- Data Act Art. 17: Wechselrecht — Anbieter müssen Datentransfer zu Wettbewerbern ermöglichen.
- § 87a UrhG: Datenbankherstellerrecht — Data Act schränkt es ein, wenn Zugangsanspruch besteht.
- GeschGehG § 2 Nr. 1: Geschäftsgeheimnisschutz als Grenze für Datenzugangsansprüche nach Data Act.
- DSGVO Art. 6: Rechtsgrundlagen für personenbezogene IoT-Daten — Vorrang der DSGVO gemäß Art. 1 Abs. 3 Data Act.

## Prüfraster

- Fällt das IoT-Gerät oder der Dienst unter den Data Act (Art. 2 Data Act — sachlicher Anwendungsbereich)?
- Hat der Nutzer ein Zugangsrecht nach Art. 4 Data Act — ist er der Geräteeigentümer oder -nutzer?
- Kollidiert das Datenbankherstellerrecht des Dateninhabers mit dem Zugangsanspruch des Nutzers?
- Rechtfertigt der Schutz von Betriebsgeheimnissen (Art. 4 Abs. 6 Data Act) eine Zugangsverweigerung?
- Ist das Wechselrecht (Art. 17 Data Act) auf die Kundendaten anwendbar, und welche Datenbankrechte tangiert der Transfer?
- Enthalten die IoT-Daten personenbezogene Informationen — gelten DSGVO-Rechte vorrangig?
- Hat der Dateninhaber unangemessene Zugangsbedingungen gestellt (Art. 6 Data Act) — sind diese nichtig?

## Typische Fallstricke

- Data Act schafft Zugangsrechte, hebt aber das Datenbankherstellerrecht nicht vollständig auf — beides muss parallel geprüft werden.
- Betriebs- und Geschäftsgeheimnisschutz als Zugangsverweigerungsgrund muss konkret und erheblich sein — pauschale Verweigerung unzulässig.
- Wechselrecht nach Art. 17 Data Act kann De-facto-Zugang zu Datenbankdaten erzwingen, die der alte Anbieter als Herstellerrecht schützt.
- Personenbezogene IoT-Daten erfordern neben Data-Act-Compliance auch DSGVO-Compliance — beide Regelwerke parallel.
- Data Act ist erst ab September 2025 anwendbar — Übergangsregelungen und Altverträge beachten.

## Output

- Data-Act-Compliance-Check für IoT-Hersteller (Art. 4-6 VO 2023/2854)
- Datenzugangskonzept (Nutzerrechte vs. Datenbankherstellerrecht)
- Betriebsgeheimnis-Prüfbogen für Zugangsverweigerung (Art. 4 Abs. 6 Data Act)
- Wechselrecht-Implementierungsguide (Art. 17 Data Act + Cloud-Transfer)
- DSGVO-/Data-Act-Schnittmengen-Analyse für IoT-Daten

## Quellen

- [Data Act VO 2023/2854 — EUR-Lex](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX%3A32023R2854)
- [§ 87a UrhG — dejure.org](https://dejure.org/gesetze/UrhG/87a.html)
- [GeschGehG — gesetze-im-internet.de](https://www.gesetze-im-internet.de/geschgehg/index.html)
- [DSGVO Art. 6 — dejure.org](https://dejure.org/gesetze/DSGVO/6.html)
- [RL 96/9/EG — EUR-Lex](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX%3A31996L0009)
- [DSM-Richtlinie 2019/790 — EUR-Lex](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX%3A32019L0790)

## 2. `db-036-datenbankrecht-bei-saas-und-cloudmigration`

**Fokus:** Datenbankrecht bei SaaS-Diensten und Cloud-Migrationen: Inhaberschaft am Datenbankherstellerrecht (§ 87a UrhG) bei SaaS-Betrieb, Datenmitnahme bei Anbieterwechsel (Data Act Art. 17), AGB-Klauseln zur Datenbankzuweisung, Auftragsverarbeitung nach Art. 28 DSGVO und Vendor-Lock-in-Risiken bei propriet­ären Datenbankformaten. Erstellt Vertragsklauseln für SaaS-Kunden.

# Datenbankrecht bei SaaS und Cloud-Migration — Inhaberschaft und Datenmitnahme

## Mandantenfall

- Unternehmen wechselt seinen CRM-SaaS-Anbieter und muss alle Kundendaten mitnehmen — welche Rechte am Datenbankinhalt hat es gegenüber dem alten Anbieter?
- SaaS-Anbieter behauptet in seinen AGB, Datenbankherstellerrechte an allen Kundendaten zu halten, die in seiner Plattform gespeichert werden.
- Startup fragt, wie Cloud-Migrationsverträge gestaltet sein müssen, damit die Datenbankrechte beim Kunden bleiben und nicht auf den Cloud-Provider übergehen.

## Erste Schritte

1. Herstellereigenschaft klären: Wer hat die wesentliche Investition in die Datenbankstruktur getragen — der SaaS-Anbieter (Infrastruktur) oder der Kunde (Inhaltsbefüllung)?
2. AGB auf Datenbankrechte-Klauseln prüfen: Behauptet der SaaS-Anbieter Herstellerrecht oder Urheberrecht an Kundendaten — ist das nach § 307 BGB wirksam?
3. Datenmitnahmerecht bestimmen: Data Act Art. 17 (Wechselrecht), DSGVO Art. 20 (Datenportabilität für Verbraucher), vertragliche Herausgabepflicht.
4. Auftragsverarbeitung bewerten: Ist der SaaS-Anbieter Auftragsverarbeiter (Art. 28 DSGVO) — er kann dann kein eigenes Datenbankherstellerrecht beanspruchen.
5. Datenbankformat und Portabilität prüfen: Liefert der SaaS-Anbieter Daten in einem offenen Format oder nur proprietary — Vendor-Lock-in-Risiko?
6. Exit-Klausel im Vertrag: Datenmitnahme-Anspruch, Export-Pflicht des Anbieters, Löschpflicht nach Herausgabe.

## Rechtsrahmen

- § 87a Abs. 2 UrhG: Hersteller ist, wer die wesentliche Investition trägt — Herstellereigenschaft folgt dem wirtschaftlichen Risiko.
- § 307 BGB: AGB-Klausel, die alle Datenbankrechte auf SaaS-Anbieter überträgt, kann unangemessen benachteiligend sein.
- Data Act Art. 17 VO 2023/2854: Wechselrecht — Kunden können zu anderem Anbieter wechseln und Daten mitnehmen.
- DSGVO Art. 20: Datenportabilitätsrecht für Verbraucher (personenbezogene Daten).
- DSGVO Art. 28: Auftragsverarbeitungsvertrag — SaaS-Anbieter als Auftragsverarbeiter hat keinen eigenständigen Datenbankherstelleranspruch.
- § 314 BGB: Außerordentliche Kündigung bei Verweigerung der Datenherausgabe als schwerwiegender Vertragsbruch.

## Prüfraster

- Wer hat die wesentliche Investition in die Datenbankstruktur und -befüllung getragen (Hersteller-Frage)?
- Enthält der SaaS-Vertrag eine Klausel, die Datenbankrechte auf den Anbieter überträgt — ist diese nach § 307 BGB wirksam?
- Greift Data Act Art. 17 — kann der Kunde Wechsel und Datenmitnahme erzwingen?
- Hat der Kunde als Verbraucher einen DSGVO-Portabilitätsanspruch (Art. 20 DSGVO) für personenbezogene Daten?
- Ist der SaaS-Anbieter Auftragsverarbeiter — und was bedeutet das für seine Datenbankrechte-Ansprüche?
- Stellt der Anbieter Daten in einem offenen maschinenlesbaren Format bereit (Vendor-Lock-in-Risiko)?
- Enthält der Vertrag eine Exit-Klausel mit klarer Herausgabe- und Löschpflicht?

## Typische Fallstricke

- SaaS-Anbieter, der nur Infrastruktur bereitstellt, hat meist kein Datenbankherstellerrecht an Kundendaten — das trägt der Kunde als Datenbefüller.
- AGB-Klausel, die alle in der Plattform gespeicherten Daten dem Anbieter zuweist, ist nach § 307 BGB anfechtbar.
- Data Act Art. 17 Wechselrecht gilt erst ab September 2025 — für laufende Verträge muss die vertragliche Grundlage ausreichen.
- Datenportabilität nach DSGVO Art. 20 betrifft nur personenbezogene Daten von Verbrauchern — B2B-Kunden sind nicht erfasst.
- Proprietäre Exportformate können faktisch die Datenmitnahme blockieren, selbst wenn rechtlich Herausgabepflicht besteht.

## Output

- Datenbankherstellerrecht-Inhaberschaftsanalyse für SaaS-Kunden
- AGB-Prüfbogen für Datenbankrechte-Klauseln (§ 307 BGB)
- Exit-Klausel-Vorlage (Datenmitnahme, Format, Löschung)
- Data Act Art. 17 Wechselrecht-Checkliste
- DSGVO-Auftragsverarbeitungsvertrag-Klausel zum Datenbankherstellerrecht

## Quellen

- [§ 87a UrhG — dejure.org](https://dejure.org/gesetze/UrhG/87a.html)
- [§ 307 BGB — dejure.org](https://dejure.org/gesetze/BGB/307.html)
- [Data Act VO 2023/2854 — EUR-Lex](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX%3A32023R2854)
- [DSGVO Art. 20 — dejure.org](https://dejure.org/gesetze/DSGVO/20.html)
- [DSGVO Art. 28 — dejure.org](https://dejure.org/gesetze/DSGVO/28.html)
- [§ 314 BGB — dejure.org](https://dejure.org/gesetze/BGB/314.html)

## 3. `db-037-backup-export-und-vendor-lock-in`

**Fokus:** Datenbankrecht bei Backup-Rechten, Datenexport und Vendor-Lock-in: § 87c UrhG erlaubte Entnahmen für rechtmäßige Nutzer, vertragliche Backup-Klauseln, Data Act Art. 17 Wechselrecht, Exportformat-Anforderungen und rechtliche Mittel gegen Lock-in-Strategien. Bewertet AGB-Wirksamkeit von Export-Verboten und erstellt Vertragsklauseln für Datenmitnahme.

# Backup, Export und Vendor-Lock-in — Datenbankrecht und Datenmitnahme

## Mandantenfall

- Unternehmen hat entdeckt, dass sein Datenbankdienstleister in den AGB den Export der Daten in maschinenlesbarer Form ausschließt — ist das wirksam?
- SaaS-Anbieter verlangt nach Vertragsende eine hohe Gebühr für den Datenexport — darf er das und was sind die rechtlichen Mittel dagegen?
- IT-Leiter fragt, welche Vertragsklauseln beim Abschluss eines neuen Datenbankvertrags verhindern, dass das Unternehmen an einen Anbieter gebunden bleibt.

## Erste Schritte

1. Backup-Recht nach § 87c UrhG prüfen: Erlaubte Handlungen für rechtmäßige Datenbanknutzer — ist eine Sicherungskopie zulässig?
2. Vertragliche Export-Klausel analysieren: Verbietet die AGB den Datenexport — ist das Verbot nach § 307 BGB angemessen?
3. Data Act Art. 17 anwenden: Wechselrecht ab September 2025 — Anbieter müssen Datenmigration ohne unverhältnismäßige Hürden ermöglichen.
4. Exportformat-Standard prüfen: Offenes, maschinenlesbares Format erforderlich — proprietäre Formate können Lock-in begründen.
5. Gebühr für Export bewerten: Angemessene Gebühr nach Data Act Art. 17 zulässig, aber unverhältnismäßige Exportgebühren sind verboten.
6. Vertragsgestaltung für neuen Datenbankvertrag: Exit-Klausel mit Exportpflicht, Format-Anforderungen, Löschpflicht nach Herausgabe.

## Rechtsrahmen

- § 87c UrhG: Erlaubte Handlungen — rechtmäßige Nutzer dürfen Teile einer Datenbank für zulässige Zwecke nutzen; Sicherungskopie analog.
- § 307 BGB: AGB-Wirksamkeit von Export-Verboten — totalem Datenexport-Verbot widerspricht berechtigtem Interesse des Nutzers.
- Data Act VO 2023/2854 Art. 17: Wechselrecht — keine unverhältnismäßigen technischen oder wirtschaftlichen Hürden bei Anbieterwechsel.
- DSGVO Art. 20: Datenportabilität — gilt für personenbezogene Verbraucherdaten; kostenloses, strukturiertes Format.
- § 314 BGB: Außerordentliche Kündigung bei Verweigerung des Datenexports als wesentlicher Vertragspflicht.
- § 93 UrhG analog: Schutz gegen wesentliche Änderungen oder Vernichtung des Datenbankwerks.

## Prüfraster

- Schließen AGB den Datenexport vollständig aus — ist das nach § 307 BGB unverhältnismäßig benachteiligend?
- Besteht nach Data Act Art. 17 ein gesetzliches Wechselrecht — gilt die VO für den betreffenden Dienst?
- Hat der Nutzer ein Recht auf Backup nach § 87c UrhG oder vertraglich?
- Verlangt der Anbieter für den Export eine unangemessene Gebühr (> echte Kosten)?
- Stellt der Anbieter Daten in einem offenen Format bereit oder bindet er durch proprietäre Formate?
- Enthält der bestehende Vertrag eine Exit-Klausel mit Exportpflicht, und ist diese vollstreckbar?
- Umfasst der Export auch Metadaten, Konfigurationsdaten und Datenbankstruktur — oder nur Rohdaten?

## Typische Fallstricke

- AGB-Klauseln, die Datenexport gegen Entgelt erlauben, aber mit unangemessenen Gebühren belasten, sind nach § 307 BGB anfechtbar.
- Data Act Art. 17 Wechselrecht gilt erst ab September 2025 — für bestehende Verträge muss vertragliche Grundlage geprüft werden.
- Proprietäre Exportformate können faktisch den Datenwechsel verhindern, obwohl rechtlich ein Herausgabeanspruch besteht.
- Backup von Datenbankstrukturen ohne Genehmigung kann Herstellerrecht verletzen, wenn keine vertragliche Erlaubnis oder § 87c-Schranke eingreift.
- Löschpflicht nach Export — der alte Anbieter hat kein Recht, eine Kopie der Kundendaten nach Herausgabe zu behalten.

## Output

- AGB-Prüfbogen für Export-Verbote und Exportgebühren (§ 307 BGB)
- Data Act Art. 17 Wechselrecht-Checkliste für Unternehmenskunden
- Exit-Klausel-Vorlage (Export, Format, Gebühr, Löschung)
- DSGVO-Portabilitäts-Anspruchsformulierung für Verbraucher
- Vendor-Lock-in-Risikoanalyse für Datenbankverträge

## Quellen

- [§ 87c UrhG — dejure.org](https://dejure.org/gesetze/UrhG/87c.html)
- [§ 307 BGB — dejure.org](https://dejure.org/gesetze/BGB/307.html)
- [Data Act VO 2023/2854 — EUR-Lex](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX%3A32023R2854)
- [DSGVO Art. 20 — dejure.org](https://dejure.org/gesetze/DSGVO/20.html)
- [§ 314 BGB — dejure.org](https://dejure.org/gesetze/BGB/314.html)
- [§ 87a UrhG — dejure.org](https://dejure.org/gesetze/UrhG/87a.html)
