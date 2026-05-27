---
name: elektronische-form-paragraph-126a-bgb-qes
description: "Mandant moechte einen Vertrag elektronisch unterzeichnen der gesetzlich Schriftform erfordert und fragt ob die qES genuegt. § 126a BGB elektronische Form als Schriftformersatz eIDAS-VO (EU) 910/2014. Pruefraster: qES-Anforderungen Zertifikatskette qualifizierter Vertrauensdiensteanbieter Signaturpruefung technische Gueltigkeit Zugangserfordernis BGH VIII ZR 159/23. Output: Formwirksamkeits-Einschaetzung und Empfehlung fuer Vertragsgestaltung. Abgrenzung zu schriftform-paragraph-126-bgb-eigenhaendige-unterschrift (Papierform) und befristungsabrede-qes-rechtsprechung-stand-2026."
---

# Elektronische Form § 126a BGB — Qualifizierte Elektronische Signatur

## Rechtsgrundlagen

- **§ 126a Abs. 1 BGB** — Elektronische Form als Ersatz für Schriftform: Aussteller muss Namen und qualifizierte elektronische Signatur (qES) hinzufügen
- **§ 126a Abs. 2 BGB** — Bei Verträgen: beide Parteien müssen dasselbe elektronische Dokument signieren oder jede Partei signiert das für die andere Partei bestimmte Dokument
- **§ 126 Abs. 3 BGB** — Schriftform kann durch elektronische Form ersetzt werden, soweit nicht Gesetz entgegensteht
- **eIDAS-Verordnung** — VO (EU) Nr. 910/2014, definiert qES als höchste Sicherheitsstufe elektronischer Signaturen
- **§ 2 Nr. 3 VDG** (ehem. SigG) — Umsetzung eIDAS im deutschen Recht

## BGH-Linie

### Grundsatz: qES ersetzt Schriftform

Nach § 126 Abs. 3 i.V.m. § 126a BGB kann die Schriftform durch die elektronische Form ersetzt werden. Voraussetzung ist eine **qualifizierte elektronische Signatur** nach Art. 3 Nr. 12 eIDAS-VO, nicht lediglich eine fortgeschrittene oder einfache elektronische Signatur.

### Kritische BGH-Entscheidung: VIII ZR 159/23 vom 27. November 2024

Der BGH hat in dieser Grundsatzentscheidung zur Wohnraummiete-Kündigung klargestellt:

> **Lehrsatz**: Auch wenn die qES technisch korrekt ist und die Schriftform des § 568 Abs. 1 BGB i.V.m. § 126a BGB grundsätzlich ersetzt, muss die formgerechte Erklärung dem Empfänger so zugehen, dass er die Signatur selbst prüfen kann.

Der Ausdruck eines qES-Dokuments durch das Gericht mit einem Transfervermerk nach § 298 Abs. 3 ZPO genügt für den wirksamen Zugang gegenüber dem Erklärungsempfänger (Mieter) **nicht**. Ein solcher Ausdruck enthält die eigentliche Signatur nicht mehr in prüfbarer Form — der Empfänger erhält lediglich eine Papierversion ohne die kryptographische Signaturinformation.

### Gesetzliche Ausnahmen: qES nicht möglich

| Rechtsgeschäft | qES ausgeschlossen? | Norm |
|---------------|---------------------|------|
| Testament | Ja | § 2231 BGB |
| Erbvertrag | Ja | § 2276 BGB |
| Eheverträge | Ja | § 1410 BGB |
| Grundstücksübertragung | Ja (notarielle Beurkundung) | § 311b BGB |
| Bürgschaftserklärung Verbraucher | Str. — BGH offen | § 766 BGB |
| Kündigung Arbeitsverhältnis | Str. — spezialgesetzliche Auslegung | § 623 BGB |

## Workflow

### Technische Anforderungen qES

```
qES = qualifizierte elektronische Signatur im Sinne von Art. 3 Nr. 12 eIDAS-VO:
  ├── Basiert auf qualifiziertem Zertifikat (Art. 3 Nr. 15 eIDAS-VO)
  ├── Ausgestellt von qualifiziertem Vertrauensdiensteanbieter (Art. 3 Nr. 17 eIDAS-VO)
  ├── Erstellt mit qualifizierter Signaturerstellungseinheit (QSCD, Art. 3 Nr. 23 eIDAS-VO)
  └── Erfüllt Anforderungen des Anhangs I eIDAS-VO

Abgrenzung:
  - Einfache elektronische Signatur: nur Zuordnung zu Person (kein Formersatz)
  - Fortgeschrittene elektronische Signatur (FES): Art. 3 Nr. 11 eIDAS-VO (kein § 126a-Ersatz)
  - Qualifizierte elektronische Signatur (qES): einzig möglicher Schriftformersatz
```

### Zugangs-Checkliste qES-Dokument

```
□ Dokument enthält qES in prüfbarer digitaler Form (kein bloßer Ausdruck)
□ Empfänger erhält das Dokument elektronisch (E-Mail-Anhang, sichere Plattform)
□ Empfänger kann Signatur mit Standardsoftware prüfen (z. B. Adobe Acrobat)
□ Zertifikat ist zum Zeitpunkt der Unterzeichnung gültig (OCSP/CRL-Prüfung)
□ Zeitstempel vorhanden oder Signaturzeitpunkt anderweitig nachweisbar
□ Empfänger hat tatsächlich Zugang erhalten (nicht nur Gerichtsausdruck)
```

### Anbieter qualifizierter Vertrauensdienste in Deutschland (Auswahl)

- **Bundesdruckerei / D-Trust**: qualifizierte Zertifikate nach eIDAS
- **DocuSign (qualifiziert)**: nur bestimmte Kontoarten mit qES
- **Swisscom Trust Services**: qES nach eIDAS
- **DATEV**: qualifizierte Signaturlösung für Steuerberater/Anwälte

## Templates

### Mandantenhinweis: qES-Versand korrekt durchführen

```
Hinweis zur qualifizierten elektronischen Signatur (qES):

Wenn Sie dem Empfänger eine qES-Urkunde übersenden, beachten Sie:
- Die Datei (i.d.R. PDF/A mit eingebetteter Signatur) muss elektronisch
  übermittelt werden — per E-Mail als Anhang oder über eine sichere Plattform.
- Ein Ausdruck des Dokuments auf Papier zerstört die Signaturinformation.
  Der Empfänger kann dann die Signatur nicht mehr prüfen.
- Der wirksame Zugang der Willenserklärung setzt voraus, dass der Empfänger
  die qES tatsächlich prüfen kann (BGH VIII ZR 159/23 vom 27. November 2024).
- Fordern Sie vom Empfänger eine Eingangsbestätigung an.
```

### Klausel: qES-Zugang in Verträgen absichern

```
Elektronisch übermittelte Willenserklärungen gelten als zugegangen, wenn
die mit qualifizierter elektronischer Signatur (§ 126a BGB, Art. 3 Nr. 12
eIDAS-VO) versehene Datei im elektronischen Postfach des Empfängers
eingegangen ist und die Signatur mit dem originalen Zertifikat prüfbar ist.
Ein Ausdruck auf Papier begründet keinen Zugang der elektronischen Form.
```

## Fallstricke

- **Ausdruck vernichtet qES-Nachweis**: Das Gericht kann ein qES-Dokument per § 298 Abs. 3 ZPO ausdrucken und in die Akte nehmen, aber dieser Ausdruck ersetzt nicht den formgerechten Zugang beim Erklärungsempfänger (BGH VIII ZR 159/23).
- **Zertifikats-Ablauf**: Ein abgelaufenes Zertifikat zum Zeitpunkt der Unterschrift führt zur Unwirksamkeit der qES — Langzeitvalidierung (LTV) beachten.
- **DocuSign-Verwechslung**: Viele DocuSign-Produkte verwenden nur FES, nicht qES — im Zweifelsfall explizit qES-Paket buchen und Zertifikat prüfen.
- **§ 623 BGB Kündigung Arbeitsvertrag**: Ob qES die Schriftform des § 623 BGB ersetzen kann, ist umstritten. Bis zur höchstrichterlichen Klärung empfiehlt sich Originalunterschrift auf Papier.

## Querverweise

- → `zugang-formgerechter-erklaerung-bgh-viii-zr-159-23` (Kernlehre Zugangsproblem)
- → `mandantenwarnung-qes-per-email-whatsapp-und-zugang`
- → `wohnraummiete-kuendigung-paragraph-568-bgb`
- → `dokumentations-und-beweisarchitektur` (qES-Validierungsprotokolle)
