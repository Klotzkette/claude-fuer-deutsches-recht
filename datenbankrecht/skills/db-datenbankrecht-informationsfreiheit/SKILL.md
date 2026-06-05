---
name: db-datenbankrecht-informationsfreiheit
description: "DB Datenbankrecht Informationsfreiheit: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# DB Datenbankrecht Informationsfreiheit

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **DB Datenbankrecht Informationsfreiheit** im Plugin Datenbankrecht. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `db-051-datenbankrecht-fuer-behoerden` | Datenbankrecht für Behörden und öffentliche Stellen: Behörden als Datenbankherstellerinnen nach § 87a UrhG, Verhältnis zu § 5 UrhG (amtliche Werke), IWG-Weiterverwendungspflichten, Open-Data-RL 2019/1024 und DSGVO-Anforderungen für Behördendatenbanken. Erstellt Datenbankrechte-Konzept für öffentliche Verwaltungen und bewertet Weiterverwendungsansprüche. |
| `db-052-datenbankrecht-und-informationsfreiheit` | Datenbankrecht im Verhältnis zu Informationsfreiheitsgesetzen (IFG): Spannungsfeld zwischen Datenbankherstellerrecht (§ 87a UrhG) und IFG-Auskunftsansprüchen, Reichweite von Datenbankschutz gegenüber IFG-Ansprüchen, Grenzen des IFG bei Betriebs- und Geschäftsgeheimnissen sowie Schutzrechten Dritter. Erstellt Abgrenzungsanalyse für Behörden und IFG-Antragsteller. |
| `db-053-datenbankrechte-bei-schul-und-hochschuldaten` | Datenbankrecht für Bildungsdatenbanken: §§ 87a-87e UrhG für Lehrmaterialdatenbanken und Hochschularchive, Schranken nach § 60a UrhG (Bildung und Unterricht), Herstellerrecht bei Lernmanagementsystemen und DSGVO-Anforderungen für Schüler- und Studierendendaten. Erstellt Lizenzkonzept und Compliance-Leitfaden für Bildungseinrichtungen. |

## Arbeitsweg

Im Plugin Datenbankrecht gilt für **DB Datenbankrecht Informationsfreiheit**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `db-051-datenbankrecht-fuer-behoerden`

**Fokus:** Datenbankrecht für Behörden und öffentliche Stellen: Behörden als Datenbankherstellerinnen nach § 87a UrhG, Verhältnis zu § 5 UrhG (amtliche Werke), IWG-Weiterverwendungspflichten, Open-Data-RL 2019/1024 und DSGVO-Anforderungen für Behördendatenbanken. Erstellt Datenbankrechte-Konzept für öffentliche Verwaltungen und bewertet Weiterverwendungsansprüche.

# Datenbankrecht für Behörden — Herstellerrecht und Weiterverwendungspflichten

## Mandantenfall

- Bundesbehörde fragt, ob sie Datenbankherstellerrecht an ihrer Statistikdatenbank geltend machen kann, obwohl das IWG Weiterverwendung grundsätzlich erlaubt.
- Landesamt behauptet Herstellerrecht an seiner Geodatenbank und will kommerziellen Nutzern Lizenzgebühren in Rechnung stellen — ist das nach Open-Data-RL zulässig?
- Unternehmen will behördliche Datenbanken für ein Compliance-Produkt nutzen und muss klären, welche Nutzungsrechte und -pflichten bestehen.

## Erste Schritte

1. Herstellerrechts-Schutz für Behörden prüfen: § 87a UrhG gilt für alle Hersteller, einschließlich Behörden — wesentliche Investition in Datenbeschaffung und -pflege nachweisen.
2. § 5 UrhG-Ausnahme abgrenzen: Amtliche Werke (Gesetze, Verordnungen, gerichtliche Entscheidungen) genießen keinen Urheberrechtsschutz — aber strukturierte Behördendatenbanken können Datenbankherstellerrecht haben.
3. IWG-Pflichten klären: § 3 IWG — Behörden müssen auf Antrag Informationen zur Weiterverwendung bereitstellen; Gebühren sind begrenzt.
4. Open-Data-RL 2019/1024 anwenden: Kategorien hochwertige Datensätze müssen kostenlos und maschinenlesbar bereitgestellt werden.
5. DSGVO-Anforderungen: Personenbezogene Daten in Behördendatenbanken unterliegen DSGVO — Zweckbindung, Auskunfts- und Löschungsrechte.
6. Lizenzgebühren prüfen: Sind Behörden nach IWG und Open-Data-RL berechtigt, Lizenzgebühren zu erheben — Grenzen?

## Rechtsrahmen

- § 87a UrhG: Behörden als Datenbankherstellerinnen — wesentliche Investition begründet Herstellerrecht auch für öffentliche Stellen.
- § 5 UrhG: Amtliche Werke — kein Urheberrechtsschutz für Gesetze, Verordnungen, Entscheidungen; aber Herstellerrecht an strukturierten Zusammenstellungen.
- IWG § 3: Weiterverwendungsrecht — Anspruch auf Bereitstellung von Behördendaten; Gebühren auf Grenzkosten begrenzt.
- Open-Data-RL 2019/1024 Art. 11: Hochwertige Datensätze kostenlos bereitstellen (z. B. statistische Daten, Geodaten).
- DSGVO Art. 5 Abs. 1: Zweckbindungsgrundsatz für Behördendatenbanken mit personenbezogenen Daten.
- § 12 GBO / § 30 GWG: Bereichsspezifische Zugangsbeschränkungen für Grundbuch und Transparenzregister.

## Prüfraster

- Hat die Behörde eine wesentliche Investition in ihre Datenbankinfrastruktur (Datenbeschaffung, Qualitätsprüfung, Darstellung) getätigt?
- Fällt die Datenbank unter § 5 UrhG-Ausnahme (amtliche Werke) oder ist sie trotzdem herstellerrechtsschutzfähig?
- Gilt das IWG für die betreffende Behörde und Datenbank — welche Ausnahmen bestehen?
- Handelt es sich um hochwertige Datensätze nach Open-Data-RL Art. 11 — kostenlose Bereitstellungspflicht?
- Enthält die Datenbank personenbezogene Daten — welche DSGVO-Rechtsgrundlage und Zweckbindung gilt?
- Sind die erhobenen Lizenzgebühren durch IWG-Grenzkosten-Begrenzung gerechtfertigt?
- Besteht ein Weiterverwendungsanspruch gegen Behörden-Weigerung — Verwaltungsrecht und IWG-Rechtsweg?

## Typische Fallstricke

- Behörden irren, wenn sie § 5 UrhG als Schutzausschluss für ihre Datenbanken verstehen — § 87a UrhG gilt daneben.
- IWG-Weiterverwendungsansprüche schließen das Datenbankherstellerrecht nicht aus — beides besteht parallel.
- Hochwertige Datensätze nach Open-Data-RL Art. 11 müssen kostenlos bereitgestellt werden — Lizenzgebühren unzulässig.
- Personenbezogene Daten in Behördendatenbanken dürfen nicht unbeschränkt zur Weiterverwendung freigegeben werden.
- Behörden als Hersteller können Unterlassungsansprüche gegen kommerzielle Nutzung geltend machen, soweit IWG nicht greift.

## Output

- Datenbankherstellerrecht-Check für öffentliche Stellen
- IWG-Weiterverwendungsanspruch-Vorlage
- Open-Data-Richtlinien-Compliance-Check für Behördendatenbanken
- DSGVO-Zweckbindungs-Prüfbogen für Behördendaten
- Lizenzgebühren-Zulässigkeitsanalyse (IWG-Grenzkosten vs. kommerzieller Gebühr)

## Quellen

- [§ 87a UrhG — dejure.org](https://dejure.org/gesetze/UrhG/87a.html)
- [§ 5 UrhG — dejure.org](https://dejure.org/gesetze/UrhG/5.html)
- [IWG — gesetze-im-internet.de](https://www.gesetze-im-internet.de/iwg/index.html)
- [Open-Data-Richtlinie 2019/1024 — EUR-Lex](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX%3A32019L1024)
- [DSGVO Art. 5 — dejure.org](https://dejure.org/gesetze/DSGVO/5.html)
- [RL 96/9/EG — EUR-Lex](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX%3A31996L0009)

## 2. `db-052-datenbankrecht-und-informationsfreiheit`

**Fokus:** Datenbankrecht im Verhältnis zu Informationsfreiheitsgesetzen (IFG): Spannungsfeld zwischen Datenbankherstellerrecht (§ 87a UrhG) und IFG-Auskunftsansprüchen, Reichweite von Datenbankschutz gegenüber IFG-Ansprüchen, Grenzen des IFG bei Betriebs- und Geschäftsgeheimnissen sowie Schutzrechten Dritter. Erstellt Abgrenzungsanalyse für Behörden und IFG-Antragsteller.

# Datenbankrecht und Informationsfreiheit — IFG versus Herstellerrecht

## Mandantenfall

- Journalist stellt IFG-Antrag auf Zugang zu einer behördlichen Datenbank — die Behörde verweigert mit Hinweis auf Datenbankherstellerrecht.
- Behörde fragt, ob sie IFG-Antragstellern den Zugang zur vollständigen Datenbank verweigern kann, um ihr Datenbankherstellerrecht zu schützen.
- NGO will Teile einer Behördendatenbank veröffentlichen, die über IFG zugänglich geworden sind — darf sie das?

## Erste Schritte

1. IFG-Anspruch prüfen: § 1 IFG (Bund) oder Landes-IFG — hat der Antragsteller einen Anspruch auf Zugang zu Behördeninformationen?
2. Datenbankherstellerrecht als IFG-Ausnahme: Schließen Schutzrechte Dritter (§ 6 IFG — Schutz geistigen Eigentums) den IFG-Anspruch aus?
3. Eigenes Herstellerrecht der Behörde: Kann eine Behörde ihr eigenes Datenbankherstellerrecht dem IFG-Anspruch entgegenhalten?
4. Reichweite des gewährten Zugangs: Wenn IFG-Zugang gewährt — darf der Antragsteller die Daten weiterveröffentlichen (IWG-Verhältnis)?
5. Teilschwärzung vs. vollständige Verweigerung: Kann ein Teil der Datenbank herausgegeben werden, während Drittrechte an anderen Teilen den Rest schützen?
6. Rechtsbehelfe: Verwaltungsgericht bei IFG-Verweigerung; Verhältnis zu datenbankrecht­lichen Ansprüchen.

## Rechtsrahmen

- § 1 IFG: Informationsfreiheitsrecht — Anspruch auf Zugang zu amtlichen Informationen.
- § 6 IFG: Schutz geistigen Eigentums als IFG-Ausnahme — Drittrechte (Urheberrecht, Datenbankrecht) können IFG-Anspruch ausschließen.
- § 9 IFG: Betriebs- und Geschäftsgeheimnisse als weiterer Ausschlussgrund.
- § 87a UrhG: Datenbankherstellerrecht — kann Behörde eigenes Recht dem IFG-Antrag entgegenhalten?
- IWG § 3: Weiterverwendungsrecht — IFG-Zugang eröffnet nicht automatisch Weiterverwendungsrecht.
- DSGVO Art. 86: Öffentlichkeitszugang zu amtlichen Dokumenten — Verhältnis zu DSGVO bei personenbezogenen Daten.

## Prüfraster

- Liegt ein wirksamer IFG-Anspruch vor — ist die Behörde auskunftspflichtig nach § 1 IFG?
- Schützt § 6 IFG Schutzrechte Dritter (z. B. Urheberrecht an eingebetteten Berichten) gegenüber dem IFG-Anspruch?
- Kann die Behörde ihr eigenes Datenbankherstellerrecht dem IFG-Antrag entgegenhalten — oder gilt es nur gegenüber privaten Dritten?
- Enthält die Datenbank personenbezogene Daten — schließt DSGVO den vollständigen IFG-Zugang aus?
- Wenn IFG-Zugang gewährt: Darf der Antragsteller die Datenbankinformationen veröffentlichen oder weiterverarbeiten (IWG-Abgrenzung)?
- Besteht die Möglichkeit einer Teilschwärzung — nicht-schutzrechtsbeschränkte Teile herausgeben?
- Welches Verwaltungsgericht ist für eine IFG-Klage bei Verweigerung zuständig?

## Typische Fallstricke

- Behörden können ihr eigenes Datenbankherstellerrecht nicht ohne weiteres dem IFG-Anspruch entgegenhalten — Sinn und Zweck des IFG-Grundsatzes überwiegt.
- § 6 IFG schützt nur Drittrechte (Urheberrechte der Autor), nicht eigene Behördenrechte.
- IFG-Zugang gewährt Einsichtsrecht, nicht automatisch Weiterverwendungsrecht — IWG-Antrag muss zusätzlich gestellt werden.
- Personenbezogene Daten in Behördendatenbanken sind DSGVO-geschützt — vollständige Datenbank nicht IFG-zugänglich.
- Schwärzungsentscheidungen der Behörde müssen begründet werden — pauschale Verweigerung ist rechtswidrig.

## Output

- IFG-Anspruchs-Prüfbogen (§ 1 IFG) mit Datenbankrecht-Abgrenzung
- Behörden-Antwortentwurf bei IFG-Datenbankantrag (Ablehnung / Teilgewährung)
- IWG-Weiterverwendungsantrag nach IFG-Zugangsgewährung
- Klage auf IFG-Zugang vor Verwaltungsgericht — Muster
- DSGVO-Teilschwärgungs-Konzept für personenbezogene Datenbankdaten

## Quellen

- [§ 1 IFG — gesetze-im-internet.de](https://www.gesetze-im-internet.de/ifg/index.html)
- [§ 6 IFG — gesetze-im-internet.de](https://www.gesetze-im-internet.de/ifg/index.html)
- [§ 87a UrhG — dejure.org](https://dejure.org/gesetze/UrhG/87a.html)
- [IWG — gesetze-im-internet.de](https://www.gesetze-im-internet.de/iwg/index.html)
- [DSGVO Art. 86 — dejure.org](https://dejure.org/gesetze/DSGVO/86.html)
- [Open-Data-Richtlinie 2019/1024 — EUR-Lex](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX%3A32019L1024)

## 3. `db-053-datenbankrechte-bei-schul-und-hochschuldaten`

**Fokus:** Datenbankrecht für Bildungsdatenbanken: §§ 87a-87e UrhG für Lehrmaterialdatenbanken und Hochschularchive, Schranken nach § 60a UrhG (Bildung und Unterricht), Herstellerrecht bei Lernmanagementsystemen und DSGVO-Anforderungen für Schüler- und Studierendendaten. Erstellt Lizenzkonzept und Compliance-Leitfaden für Bildungseinrichtungen.

# Datenbankrechte bei Schul- und Hochschuldaten — Bildungseinrichtungen

## Mandantenfall

- Universität hat eine umfangreiche Forschungsdatenbank aufgebaut und fragt, ob sie EdTech-Startups Lizenzen erteilen kann oder ob das Hochschulrecht dem entgegensteht.
- Schulbuchverlag behauptet Datenbankherstellerrecht an seiner digitalen Aufgabendatenbank — Lehrerin fragt, welche Aufgaben sie frei nutzen darf.
- Lernmanagementsystem-Betreiber will wissen, ob die von Lehrkräften hochgeladenen Materialien sein Datenbankherstellerrecht begründen oder ob die Lehrkräfte selbst Rechteinhaber bleiben.

## Erste Schritte

1. Herstellerrecht der Bildungseinrichtung prüfen: Hat die Hochschule oder Schule eine wesentliche Investition in Datenbankbeschaffung und -pflege getätigt?
2. Lehrkraft vs. Einrichtung als Hersteller: Hat die Lehrkraft das Material selbst erstellt (Urheberrecht verbleibt bei ihr) oder hat die Einrichtung investiert?
3. Bildungsschranke § 60a UrhG: Vervielfältigung und Bereitstellung für Unterricht und Forschung in gebotenem Umfang — gilt auch für Datenbankentnahmen (§ 87c UrhG i.V.m. § 60a UrhG)?
4. LMS-Inhaberschaft klären: Hat der LMS-Betreiber Herstellerrecht an der Gesamtdatenbank, oder nur Infrastrukturrecht?
5. DSGVO für Lernerdaten: Schüler- und Studierendendaten in Lernmanagementsystemen sind personenbezogen — besonders schützenswert bei Minderjährigen (§ 8 DSGVO).
6. Lizenzmodell für EdTech-Nutzung: Welche Rechte kann die Hochschule lizenzieren — Herstellerrecht, Urheberrecht an Inhalten, Datenbankzugang?

## Rechtsrahmen

- § 87a UrhG: Datenbankherstellerrecht für Bildungseinrichtungen — wesentliche Investition in Aufbau und Pflege von Lehrmaterial-Datenbanken.
- § 60a UrhG: Bildungsschranke — Vervielfältigung für Unterricht und Forschung zulässig; gilt auch für Datenbanken.
- § 87c UrhG: Erlaubte Handlungen — Verweis auf § 60a UrhG als Schranke auch gegenüber Herstellerrecht.
- § 43 UrhG: Arbeitnehmerurheberrecht — Herstellerrecht der Einrichtung bei Arbeitnehmer-Erstellungen im Dienst.
- DSGVO Art. 8: Einwilligung Minderjähriger — ab 16 Jahren selbstständig (in DE ggf. ab 14 nach § 8 Abs. 1 DSGVO-Öffnungsklausel).
- § 60a Abs. 1 UrhG: Unterrichtsschranke — bis 15 % eines Werks, für Lehrende und Lernende der Einrichtung.

## Prüfraster

- Hat die Bildungseinrichtung eine eigenständige wesentliche Investition in ihre Datenbankstruktur getätigt?
- Wer ist Urheber oder Hersteller — Einrichtung, Lehrkraft oder beide (§§ 8 / 43 UrhG)?
- Greift § 60a UrhG als Schranke gegenüber dem Verlagsherstellerrecht oder der Einrichtungs-Datenbank?
- Hat der LMS-Betreiber Herstellerrecht an der Gesamtdatenbank oder nur Infrastrukturrecht?
- Sind Schüler- und Studierendendaten (Lernfortschritte, Noten, Anwesenheit) in der Datenbank — welche DSGVO-Anforderungen gelten?
- Ist die EdTech-Lizenzierung mit dem Hochschulrecht und staatlichen Förderungsbedingungen vereinbar?
- Besteht ein Open-Access-Mandat für Forschungsdaten der Hochschule (DFG, BMBF)?

## Typische Fallstricke

- Lehrmaterialien, die Lehrkräfte im Dienst erstellen, können Herstellerrecht der Einrichtung begründen — persönliches Urheberrecht der Lehrkraft bleibt aber bestehen.
- § 60a UrhG-Schranke gilt nur für Lehrende und Lernende der eigenen Einrichtung, nicht für externe Plattformen.
- LMS-Datenbankrecht des Betreibers schließt nicht das Urheberrecht der hochladenden Lehrkraft aus — differenzierte Klärung nötig.
- Minderjährigen-DSGVO-Anforderungen werden in EdTech-AGB häufig unzureichend berücksichtigt.
- Open-Access-Pflichten für geförderte Forschungsdaten kollidieren manchmal mit Verlagslizenzen — Prüfung der Förderbedingungen nötig.

## Output

- Datenbankherstellerrecht-Gutachten für Bildungseinrichtung
- Bildungsschranken-Check (§ 60a UrhG für Unterrichtsdatenbank-Nutzung)
- LMS-Inhaberschafts-Matrix (Einrichtung / Lehrkraft / LMS-Betreiber)
- DSGVO-Minderjährigen-Compliance-Checkliste für Schul-IT-Systeme
- EdTech-Lizenzvertrag-Vorlage für Hochschuldatenbanknutzung

## Quellen

- [§ 87a UrhG — dejure.org](https://dejure.org/gesetze/UrhG/87a.html)
- [§ 60a UrhG — dejure.org](https://dejure.org/gesetze/UrhG/60a.html)
- [§ 87c UrhG — dejure.org](https://dejure.org/gesetze/UrhG/87c.html)
- [§ 43 UrhG — dejure.org](https://dejure.org/gesetze/UrhG/43.html)
- [DSGVO Art. 8 — dejure.org](https://dejure.org/gesetze/DSGVO/8.html)
- [RL 96/9/EG — EUR-Lex](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX%3A31996L0009)
