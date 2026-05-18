---
name: written-consent
description: >
  Entwirft Beschlüsse im schriftlichen Verfahren (§ 48 Abs. 2 GmbHG) oder Umlaufbeschlüsse
  im Hausstil mit Präzedenzsuche im Beschlussarchiv. Bei der AG: Hinweis, dass HV-Beschlüsse
  Präsenz oder virtuelle HV (§ 118a AktG) erfordern und notariell beurkundet werden
  (§ 130 AktG); Umlaufverfahren bei AG nur für Aufsichtsrat (§ 108 Abs. 4 AktG) und
  Vorstand (§ 77 AktG). Behandelt Stimmverbote (§ 47 Abs. 4 GmbHG), Mehrheitserfordernisse
  und Unterzeichner-Tracking. Lädt bei „Umlaufbeschluss", „schriftlicher Beschluss",
  „Gesellschafterbeschluss" oder Beschreibung einer zustimmungspflichtigen Maßnahme
  ohne Versammlung.
language: de
triggers:
  - "Umlaufbeschluss"
  - "schriftlicher Beschluss"
  - "Gesellschafterbeschluss"
  - "§ 48 Abs. 2 GmbHG"
  - "Beschluss ohne Versammlung"
  - "Aufsichtsratsumlaufbeschluss"
  - "Zustimmungsbeschluss"
  - "schriftliche Abstimmung"
  - "Gesellschafterversammlung schriftlich"
argument-hint: "[Beschreibung der zustimmungspflichtigen Maßnahme]"
---

# Beschluss im schriftlichen Verfahren / Umlaufbeschluss

## Zweck

Routinemäßige Gesellschafterbeschlüsse einer GmbH erfordern keine Versammlung. Geschäftsführerbestellung, Jahresabschluss-Feststellung, Gewinnverwendung, Prokuraerteilung können im schriftlichen Verfahren nach § 48 Abs. 2 GmbHG gefasst werden. Dieser Skill entwirft sie im Hausstil, sucht den nächstliegenden Präzedenzfall und flaggt Maßnahmen, bei denen anwaltliche Prüfung geboten ist.

**Rechtsformhinweis:** Bei der AG sind Hauptversammlungsbeschlüsse in Präsenz-HV (§ 118 AktG), virtueller HV (§ 118a AktG) oder hybrider HV zu fassen; ein schriftliches Aktionärs-Umlaufverfahren ist nicht vorgesehen. Das schriftliche Verfahren ist bei der AG auf Aufsichtsratsbeschlüsse (§ 108 Abs. 4 AktG) und Vorstandsbeschlüsse (Geschäftsordnung) beschränkt.

## Eingaben

- Beschreibung der zu beschließenden Maßnahme
- Angaben zu Gesellschaft (Firma, Rechtsform, Sitz, HRB-Nummer)
- Gesellschafterliste / Unterzeichnerkreis
- Optional: Präzedenz-Beschluss oder Pfad zum Beschlussarchiv aus CLAUDE.md

## Rechtlicher Rahmen

**GmbH-Beschlussfassung:**
§ 48 GmbHG (Gesellschafterversammlung; Abs. 2: schriftliche Abstimmung); § 47 Abs. 4 GmbHG (Stimmverbot bei Interessenkonflikt); § 53 GmbHG (Satzungsänderungen — notarielle Beurkundung); § 46 GmbHG (Zuständigkeiten der Gesellschafterversammlung).

BGH, Urt. v. 11.02.2008 – II ZR 187/06, NZG 2008, 381 Rn. 12 (§ 48 Abs. 2 GmbHG: Einverständnis aller Gesellschafter zum Verfahren erforderlich); BGH, Urt. v. 23.09.2014 – II ZR 44/13, NZG 2014, 1332 Rn. 15 (Stimmverbot und Treuepflichten bei GmbH-Beschluss); BGH, Urt. v. 07.11.1994 – II ZR 108/93, NJW 1995, 260 Rn. 10 (Beschlussmängelrecht GmbH analog §§ 241 ff. AktG).

**AG/SE:** § 108 Abs. 4 AktG (Aufsichtsratumlaufbeschluss); § 118a AktG (virtuelle HV); § 130 AktG (notarielle Niederschrift HV-Beschlüsse).

**Personengesellschaften (MoPeG ab 01.01.2024):** § 714 BGB n.F. (GbR-Beschlussfassung); §§ 105, 110 HGB (OHG); § 163 HGB (KG-Stimmrechte).

**Kommentarliteratur:** Lutter/Hommelhoff/Bayer, GmbHG, 21. Aufl. 2023, § 48 Rn. 1 ff., § 47 Rn. 60 ff.; Scholz/Priester, GmbHG, 13. Aufl. 2022, § 48 Rn. 20 ff.; Roth/Altmeppen, GmbHG, 11. Aufl. 2024, § 48 Rn. 10 ff.; Hüffer/Koch, AktG, 16. Aufl. 2024, § 108 Rn. 15 ff.

## Ablauf

### Sicherheits-Stopp: Wesentliche Maßnahme + Sofortunterzeichnung

Bei Maßnahmen aus der Überprüfungsliste (M&A, Kapitalmaßnahme, Satzungsänderung, Auflösung) und gleichzeitigem Sofortunterzeichnungssignal („heute DocuSign", „vor Closing"):

> ⛔ **Wesentliche Maßnahme + Sofortunterzeichnung — nur Entwurf zur Prüfung.** Ich erstelle den Entwurf, aber nicht in unterschriftsreifer Form ohne anwaltliche Prüfung. Bitte einen der zwei Wege wählen: (1) externer Anwalt prüft zuerst, oder (2) bestätigen, dass externer Anwalt das Vorgehen bereits freigegeben hat.

### Kein-Präzedenz-Stopp

Falls kein Beschlussarchiv konfiguriert und kein Seed-Beschluss bereitgestellt:

> **Kein Präzedenzfall — Stopp.** Entweder (1) einen früheren Beschluss dieser Gesellschaft einfügen/hochladen, oder (2) explizit angeben, dass ein Standardvorlagen-Entwurf akzeptiert wird und die Formalien selbst angepasst werden.

### Schritt 1: Maßnahme identifizieren

- Was soll beschlossen werden? (Ein Satz, ggf. Detailangaben)
- Wirksam ab welchem Datum?
- Unterzeichnerkreis (alle Gesellschafter / Aufsichtsrat / Vorstand)?
- Interessenkonflikt bei einem Gesellschafter? (→ § 47 Abs. 4 GmbHG prüfen)

**Klassifizierung:**

*Routine (direkter Präzedenzfall wahrscheinlich):* Geschäftsführerbestellung/-abberufung; Prokura; Jahresabschluss-Feststellung; Gewinnverwendung; Vertragsfreigabe unterhalb Wesentlichkeitsschwelle; konzerninterneliche Darlehen.

*Überprüfungs-Flag (anwaltliche Prüfung geboten):* M&A; Kapitalerhöhung/-herabsetzung; Satzungsänderung (§ 53 GmbHG); Auflösung (§§ 60 ff. GmbHG); Ergebnisabführungsvertrag; Maßnahmen, die in späterem Datenraum erscheinen.

### Schritt 2: Präzedenzsuche

Beschlussarchiv nach Maßnahmentyp durchsuchen. Nächstliegenden Beschluss auswählen, Beschlussformulierung, Präambelstruktur und Vollmachtstext extrahieren.

### Schritt 3: Beschluss entwerfen

Gesetzliche Grundlage je Rechtsform angeben (§ 48 Abs. 2 GmbHG / § 108 Abs. 4 AktG / § 714 BGB n.F.). Hausstil verwenden:

```
BESCHLUSS DER GESELLSCHAFTER
der [Firma]
im schriftlichen Verfahren nach § 48 Abs. 2 GmbHG

[Datum]

Die unterzeichnenden Gesellschafter der [Firma], einer GmbH mit Sitz in [Ort],
eingetragen im Handelsregister des AG [Ort] unter HRB [Nummer], fassen folgenden
Beschluss ohne Einberufung einer Gesellschafterversammlung:

VORBEMERKUNG
[Hintergrund — ein bis zwei Sätze]

BESCHLUSS
Die Gesellschafter beschließen:
[Präzise Formulierung — Personen namentlich, Beträge, Dokumente mit Datum angeben]

[Folgebeschluss: Bevollmächtigung der Geschäftsführer zur Umsetzung]
[Folgebeschluss: Genehmigung bereits getroffener Vormaßnahmen, falls erforderlich]

Dieser Beschluss wird wirksam mit Eingang der Zustimmungserklärungen aller
Gesellschafter [oder der satzungsmäßig erforderlichen Mehrheit].

_______________________________
[Gesellschaftername]  |  [Anteil %]  |  Datum: _______________
[Für jeden weiteren Gesellschafter wiederholen]
```

Formhinweise: Präzise formulieren (keine Vagen Formulierungen); bevollmächtigte Personen namentlich benennen; genehmigte Dokumente als Anlage beifügen; Hausstil-Formulierungsweise durchgängig einhalten.

### Schritt 4: Gesellschaftsvertragliche Anforderungen prüfen

- Erfordert § 48 Abs. 2 GmbHG Zustimmung aller Gesellschafter zum Verfahren (h.M.)?
- Erhöhtes Mehrheitserfordernis für die Maßnahme (Dreiviertelmehrheit bei Satzungsänderung § 53 Abs. 2 GmbHG)?
- Notarielle Beurkundung erforderlich (§ 53 GmbHG, § 15 Abs. 3 GmbHG)?
- Stimmverbot nach § 47 Abs. 4 GmbHG zu prüfen?
- Handelsregisteranmeldung nach Beschluss erforderlich (§ 39 GmbHG bei GF-Wechsel)?

### Schritt 5: Ausgabe

1. **Beschlussentwurf** — vollständig, zur Prüfung und Zirkulation bereit.
2. **Unterzeichner-Checkliste** mit Stimmverbot-Flag, Mehrheitserfordernis, Notarerfordernis.
3. **Prüf-Checkliste** (Präzision der Formulierung, Anlagen, Gesellschaftsvertrag, § 47 Abs. 4, Handelsregister).
4. **Entwurfs-Hinweis** (vor Unterzeichnung zu entfernen): „Dies ist ein Entwurf zur anwaltlichen Prüfung. Die Unterzeichnung begründet rechtswirksame Gesellschafterbeschlüsse — ein zugelassener Rechtsanwalt prüft, bevor der Beschluss zirkuliert wird."

## Ausgabeformat

Beschlussentwurf + Unterzeichner-Checkliste + Prüf-Checkliste + Entwurfs-Hinweis. Arbeitsergebnis-Kopfzeile auf Prüf-Unterlagen.

## Beispiel

GmbH mit drei Gesellschaftern, schriftliche Geschäftsführerbestellung. Einer der Gesellschafter wird selbst bestellt (Stimmverbot § 47 Abs. 4 GmbHG — str. bei Eigenbestellung, vgl. BGH NJW 1995, 260). Ausgabe: Beschlussentwurf, Unterzeichner-Checkliste ohne befangenen Gesellschafter (Stimmverbot zu klären), Hinweis auf Handelsregisteranmeldung § 39 GmbHG.

## Risiken und typische Fehler

- **§ 48 Abs. 2 GmbHG-Verfahrensvoraussetzung übersehen.** Einverständnis aller Gesellschafter zum schriftlichen Verfahren nach h.M. erforderlich — Satzung prüfen.
- **Stimmverbot nach § 47 Abs. 4 GmbHG ignorieren.** Befangene Gesellschafter in Unterzeichner-Checkliste flaggen.
- **AG-Hauptversammlungsbeschlüsse im Umlaufverfahren.** Unzulässig — HV in Präsenz, virtuell (§ 118a AktG) oder notarielle Niederschrift (§ 130 AktG) erforderlich.
- **Satzungsändernde Beschlüsse ohne Notarhinweis.** § 53 GmbHG: notarielle Beurkundung und Handelsregistereintragung zwingend.
- **Vage Beschlussformulierungen.** In späteren Due-Diligence-Prüfungen müssen Beschlüsse die genehmigten Maßnahmen präzise benennen.

## Quellenpflicht

- `§ 48 Abs. 2 GmbHG` (schriftliches Verfahren), `§ 47 Abs. 4 GmbHG` (Stimmverbot)
- `§ 53 GmbHG` (Satzungsänderung), `§ 108 Abs. 4 AktG` (AR-Umlaufbeschluss), `§ 118a AktG` (virtuelle HV)
- BGH: `BGH, Urt. v. 11.02.2008 – II ZR 187/06, NZG 2008, 381 Rn. 12`; `BGH, Urt. v. 23.09.2014 – II ZR 44/13, NZG 2014, 1332 Rn. 15`
- Kommentare: `Lutter/Hommelhoff/Bayer, GmbHG, 21. Aufl. 2023, § 48 Rn. 5`; `Scholz/Priester, GmbHG, 13. Aufl. 2022, § 48 Rn. 20`

Hinweis: Dieser Skill ersetzt keine anwaltliche Beratung im konkreten Einzelfall.
