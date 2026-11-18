# Stammdaten-Erhebung

Nutze diese Detailreferenz nur für den konkreten Arbeitsschritt. Quellenstatus und Grenzen älterer Anker stehen in der [Rechtsprüfung](../../../references/rechtsstand.md); für Zitate gilt die [Zitierweise](../../../../references/zitierweise.md).

## 1. Ziel

Einen vollständigen, fehlerfreien Zeugniskopf generieren. Falsche Stammdaten sind eigenständige Berichtigungspunkte.

## 2. Eingang - was wird abgefragt

| Datenpunkt | Pflicht | Hinweis |
|---|---|---|
| Vollständiger Name | ja | Verifizierte Personalunterlagen; keine Ausweiskopie standardmäßig verlangen |
| Geburtsdatum | nein | Nur bei sachlichem Bedarf oder dokumentiertem Wunsch; TT.MM.JJJJ |
| Eintrittsdatum | ja | Rechtlichen Beginn und tatsächlichen Tätigkeitsbeginn unterscheiden |
| Austrittsdatum | ja | Letzter vertraglich relevanter Tag; bei Zwischenzeugnis leer lassen |
| Positionsbezeichnung | ja | Tatsächliche Funktion; Abweichungen vom Vertrag belegen |
| Hierarchiestufe | bei Führungskräften | z.B. „Leiterin", „Senior", „Teamleiter" |
| Abteilung/Bereich | empfohlen | Für Einordnung im Aufgabenblock |
| Unternehmensname und Rechtsform | ja | GmbH, AG, GbR usw. |
| Unternehmensanschrift | ja | Für Briefkopf |
| Name und Funktion des Unterzeichners | ja | Muss hierarchisch befugt sein |

## 3. Generier-Regeln

- Einleitungssatz: „[Vollständiger Name], geboren am [Datum], war vom [Eintrittsdatum] bis zum [Austrittsdatum] in unserem Unternehmen als [Positionsbezeichnung] tätig."
- Präzise Positionsbezeichnung verwenden - nicht „Mitarbeiter" wenn „Projektleiter IT-Infrastruktur" die korrekte Bezeichnung ist.
- Bei Rollenwechseln prägende Funktionen mit Zeiträumen nennen; siehe [Rollenverlauf](mehrere-positionen-im-zeugnis.md).
- Der Einleitungssatz funktioniert ohne Geburtsdatum; die eindeutige Identität ist entscheidend.

## 4. Platzhalter-Konventionen

Fehlende Daten werden immer als Platzhalter gesetzt:
- `[Vorname Name]`
- `[TT.MM.JJJJ]`
- `[Positionsbezeichnung]`
- `[Unternehmen GmbH]`

Platzhalter niemals stillschweigend erfinden - der Nutzer muss sie explizit bestätigen.

## 5. Formalia-Check

Bei Papierform muss die Person unterschreiben, die im Unterschriftsblock mit Name und Funktion ausgewiesen ist. Vertretungsbefugnis und geeignete Stellung gegenüber der beurteilten Person müssen erkennbar sein. BAG, Urteil vom 21.09.1999 - Az. 9 AZR 893/98 wird in BAG, Urteil vom 27.04.2021 - Az. 9 AZR 262/20, Rn. 11 für die äußeren Anforderungen herangezogen; die spezielle Hierarchiefrage ist damit nicht unmittelbar entschieden. Deshalb werden Zeichnungsbefugnis, Funktion und Hierarchie geprüft; ein Personalsachbearbeiter ist nicht allein wegen seiner Abteilungszugehörigkeit ausgeschlossen, muss aber als geeigneter Vertreter erkennbar sein. In elektronischer Form treten mit Einwilligung des Arbeitnehmers die qualifizierte elektronische Signatur und Paragraf 126a BGB an die Stelle der eigenhändigen Unterschrift.

## 6. Stolpersteine

- Bei faktisch höherer Funktion Aufgaben und Befugnisse belegen; weder allein am Vertrag festhalten noch einen nicht getragenen Titel vergeben.
- Eintrittsdatum bei Übernahme aus Zeitarbeit oder befristeten Vorverträgen unklar - immer beim Nutzer nachfragen, da es den Gesamteindruck des Zeugnisses prägt.
- Bei fehlendem Austrittsdatum Status und Verfahrensstand klären; nicht automatisch ein Zwischenzeugnis erstellen.

## 7. Anti-Muster

- Positionsbezeichnung eigenständig „aufhübschen" (aus „Sachbearbeiter" wird „Spezialist").
- Ein fehlendes Geburtsdatum als gesetzlichen Formmangel behandeln.
- Unternehmensname ohne Rechtsform nennen.

## 8. Ausgabeformat

Das Endprodukt wird in vollständigen, ausformulierten und grammatikalisch sauberen Sätzen geliefert; Stichworte, Halbsätze, leere Klauselrümpfe und reine Aufzählungs-Skelette sind als Endprodukt unzulässig (Ausformulierungspflicht). Die hier katalogisierten Formeln und Bausteine sind Zwischenergebnisse und werden im fertigen Zeugnis zu vollständigem Fließtext verbunden. Soweit technisch möglich, verwendet das formatierte Enddokument Times New Roman in 11 pt und ausschließlich dezimale Gliederung (1, 1.1, 1.1.1); bei reiner Markdown- oder Chat-Ausgabe wird dieser Formatwunsch ausdrücklich als Exporthinweis vermerkt.
