# 19 Quotelung, Haftung und Versicherer-Regress

**Akte:** Berufsrecht / KI-Vertragsprüfung — Kanzlei Rotbruch, Köln
**Stichtag Aktenstück:** 15. April 2026

---

## 1. Haftungsquotelung zwischen den Beteiligten

Im vorliegenden Schadensfall sind mehrere potenzielle Verantwortliche zu identifizieren:

| Beteiligter | Haftungsgrundlage | Anteil (geschätzt) |
|---|---|---|
| Dr. Rotbruch | §§ 280, 675 BGB (Anwaltspflichtverletzung) | 85 % |
| LegalTech GmbH | § 280 BGB (Produktfehler, keine ausreichende Warnung) | 10 % |
| Frau Habernau (Mitverschulden) | § 254 BGB | 5 % |

Die Quotelung ist eine Schätzgröße für die Verhandlungsführung; das Gericht wird eine gesamtschuldnerische Haftung nach § 421 BGB bejahen, wenn mehrere Verantwortliche zusammenwirken.

---

## 2. Gesamtschuld zwischen Rotbruch und LegalTech GmbH

Dr. Rotbruch und die LegalTech GmbH könnten als Gesamtschuldner nach § 421 BGB haften, wenn folgende Voraussetzungen vorliegen:

1. Beide haben durch ihre Beiträge denselben Schaden verursacht.
2. Die Klägerin kann von jedem Gesamtschuldner die volle Leistung verlangen.
3. Im Innenverhältnis regeln §§ 421–426 BGB den Ausgleich.

Für eine Gesamtschuld müsste die LegalTech GmbH einen eigenen Haftungstatbestand erfüllen. In Betracht kommt:

- **Produkthaftung (§ 1 ProdHaftG):** JuristAssist Pro 5 ist Software; nach h.M. ist Software kein Produkt i.S.d. ProdHaftG, solange sie nicht in körperlicher Form abgegeben wird. Cloud-SaaS fällt aus dem ProdHaftG heraus. Die EU-Produkthaftungsrichtlinie 2024/2853 schließt Software künftig ein, ist aber noch nicht umgesetzt.
- **Delikt (§ 823 Abs. 1 BGB):** Verletzung des absoluten Rechts auf informationelle Selbstbestimmung durch Verarbeitung ohne AVV. Möglich, aber kaum kausal für den Ehevertrag-Schaden.
- **§ 280 BGB aus dem Nutzungsvertrag:** Der Nutzungsvertrag zwischen Rotbruch und LegalTech GmbH begründet keine Schutzpflichten gegenüber Frau Habernau (kein Vertrag mit Schutzwirkung für Dritte, da Frau Habernau nicht in den Leistungsbereich der LegalTech GmbH einbezogen ist).

Ergebnis: Eine direkte Haftung der LegalTech GmbH gegenüber Frau Habernau ist schwach begründbar. Im Innenverhältnis Rotbruch/LegalTech GmbH kann Rotbruch einen Regressanspruch prüfen.

---

## 3. Regressanspruch Rotbruch gegen LegalTech GmbH

### 3.1 Rechtsgrundlage

Dr. Rotbruch könnte gegen die LegalTech GmbH Regress nehmen nach:

- § 280 BGB (Schlechtleistung aus Nutzungsvertrag): Das Tool hat ein unzureichendes Prüfergebnis geliefert und die Grenzen seiner Leistungsfähigkeit im Output nicht hinreichend deutlich kommuniziert.
- § 634 BGB (Werkmängel), wenn der Vertrag als Werkvertrag zu qualifizieren ist.

### 3.2 Hürden

Der Regressanspruch scheitert voraussichtlich daran, dass:
- die Produktdokumentation ausdrücklich auf die Grenzen des Tools bei der Sittenwidrigkeitsprüfung hingewiesen hat (Aktenstück 04, Abschn. 2.2),
- die AGB der LegalTech GmbH eine Haftungsbeschränkung für Fehler im Output enthielten (Ziffer 12.1 LegalTech AGB: Haftung nur bei grober Fahrlässigkeit und auf direkten Schaden begrenzt auf 12 Monatsbeiträge = 1.068 EUR).

Eine Regressklage erscheint daher wirtschaftlich nicht lohnenswert, aber symbolisch für die Verhandlungsposition gegenüber der LegalTech GmbH relevant.

---

## 4. Regressanspruch Allianz gegen Rotbruch (falls Deckung doch besteht)

Sollte ein Gericht die KI-Ausschlussklausel der Allianz für unwirksam erklären und die Allianz zur Deckung verpflichten, könnte die Allianz im Nachgang nach § 86 VVG auf die LegalTech GmbH übergehen. Der Subrogationsanspruch würde jedoch an den gleichen Hürden scheitern (Produktdokumentation, AGB-Haftungsbeschränkung).

---

## 5. Zusammenfassung der Haftungslandschaft

```
Frau Habernau (Klägerin)
        |
        | § 280, 675 BGB (187.000 EUR)
        |
   Dr. Rotbruch ──── (Regress ?) ──── LegalTech GmbH
        |                                   (schwach)
        |
   Allianz AG ──── (Deckungsklage ?) ──── Rotbruch
   (Deckung abgelehnt)
        |
   ggf. Subrogation § 86 VVG
```

Die Haupthaftung liegt bei Dr. Rotbruch. Die Allianz-Deckungsfrage ist separat zu verfolgen. Ein Regress gegen LegalTech GmbH ist zu erwägen, aber wirtschaftlich unsicher.

---

**Quellen:**
- [§ 280 BGB (dejure.org)](https://dejure.org/gesetze/BGB/280.html)
- [§ 421 BGB (dejure.org)](https://dejure.org/gesetze/BGB/421.html)
- [§ 254 BGB (dejure.org)](https://dejure.org/gesetze/BGB/254.html)
- [§ 86 VVG (dejure.org)](https://dejure.org/gesetze/VVG/86.html)
- [§ 1 ProdHaftG (dejure.org)](https://dejure.org/gesetze/ProdHaftG/1.html)
