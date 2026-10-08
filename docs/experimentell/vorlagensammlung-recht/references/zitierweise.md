# Zitierweise

Verbindlich für alle Vorlagen dieses Repositories. Ziel ist eine
einheitliche, nachvollziehbare Zitierung von Rechtsprechung, Literatur
und Normen — ohne halluzinierte Fundstellen.

## Reihenfolge

Innerhalb einer Belegliste:

1. Rechtsprechung (Rspr.)
2. Literatur (Kommentare, Lehrbücher, Aufsätze)
3. Sonstiges (amtliche Materialien, Verlautbarungen)

Innerhalb der Rechtsprechung: **neueste Entscheidung zuerst**, danach
absteigend. Innerhalb der Literatur: zuerst Kommentare nach Norm,
danach Aufsätze.

## Rechtsprechung

Schema:

> Gericht, Entscheidungsform vom Datum — Az., Fundstelle, Rn. <…>.

Beispiele:

- BGH, Urteil vom 12.06.2024 — IV ZR 341/22, NJW 2024, 2371, Rn. 18.
- BAG, Urteil vom 16.01.2018 — 7 AZR 312/16, BAGE 161, 261, Rn. 27.
- BVerfG, Beschluss vom 07.02.2023 — 2 BvR 1057/22, NVwZ 2023, 412.

Hinweise:

- Datum im Format TT.MM.JJJJ, kein US-Format.
- Aktenzeichen ohne Punkt nach der Senatskennung („IV ZR" statt „IV. ZR").
- Bei Beschlüssen „Beschluss vom", bei Urteilen „Urteil vom".
- Fundstelle nur, wenn verifiziert. Lieber weglassen als raten.
- Randnummern nur, wenn präzise verifizierbar (BGH-Pressemitteilung
  zählt nicht als Quelle für Rn.-Angaben).

## Literatur

### Kommentare

Schema:

> Bearbeiter, in: Kommentar (Hrsg.), Auflage, Jahr, Norm, Rn. <…>.

Beispiele:

- Schaub, in: MüKo BGB, 9. Aufl. 2024, § 611a, Rn. 134.
- Greger, in: Zöller, ZPO, 35. Aufl. 2024, § 253, Rn. 13.

### Lehrbücher / Monografien

> Verfasser, Titel, Auflage, Jahr, Seite/Rn.

Beispiel:

- Köhler/Bornkamm, UWG, 42. Aufl. 2024, § 8, Rn. 1.42.

### Aufsätze

> Verfasser, Titel, Zeitschrift Jahr, Seite (Anfangsseite, ggf. zitierte
> Seite).

Beispiel:

- Habersack, Die Reform des Personengesellschaftsrechts, NJW 2021, 2521
  (2525).

## Normen

- Innerhalb desselben Gesetzes: § 611a Abs. 1 Satz 2 BGB, § 280 Abs. 1 BGB.
- Bei mehrfacher Nennung: erste Nennung mit vollständigem Gesetz, danach
  Kurzform — sofern eindeutig.
- EU-Recht: Art. 28 Abs. 3 DSGVO, Art. 6 Abs. 1 lit. b DSGVO.
- Mehrfachnennung: §§ 280, 281 BGB (mit doppeltem Paragraphenzeichen).

## Englischsprachige Quellen

Originalsprache, deutsche Schreibweise des Verfassers beibehalten,
Fundstelle im Originalformat:

> Gomez, in: Bonell (ed.), The UNIDROIT Principles in Practice, 2nd ed.
> 2006, Art. 7.1.4.

## Was wir nicht tun

- Keine Randnummern aus dem Modellwissen, wenn keine verifizierbare
  Quelle vorliegt.
- Keine ungeprüften Volltext-Zitatschnipsel.
- Keine Quellen ohne Gericht/Datum/Az. — eine Entscheidung ohne diese
  drei Angaben wird nicht zitiert.
- Keine Fundstellen-Konstruktion („BGHZ 236, 358" muss verifiziert
  sein, sonst weglassen).

## Pflicht-Quellenprüfung

Jede Vorlage, die Rechtsprechung zitiert, durchläuft den `human_review`-
Check `r90-az-live-verifiziert`. Vor jeder Mandatsverwendung sind die
Aktenzeichen live in den amtlichen Quellen zu prüfen. Die zentrale Liste
der Prüfquellen steht in [Prüfquellen](pruefquellen.md).

- bundesgerichtshof.de
- bundesarbeitsgericht.de
- bundesfinanzhof.de
- bundessozialgericht.de
- bundesverwaltungsgericht.de
- bundesverfassungsgericht.de
- curia.europa.eu (EuGH/EuG)
- echr.coe.int (EGMR)
