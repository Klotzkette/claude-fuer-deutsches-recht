# beA-Empfang und kontrollierter Versand: Quellen und Selbstprüfung

## 1. Umfang und Ergebnis

Prüfdatum: 08.10.2026. Der vorhandene Skill wurde unter demselben Slug erweitert. Körperwortzahl: vorher 6560, nachher 6514. Beschreibung: 324 Zeichen. Neue Referenz: 3609 Wörter. Keine Testakten, Zugangsmittel oder produktiven Postfächer wurden geöffnet oder geändert; keine Nachricht wurde gesendet.

Die Anlagenaufbereitung bleibt erhalten. Vollständige Helferdetails, Rückfragen und ein langer technischer Fehlerfall wurden in die verlinkte Referenz verschoben. Neu sind Eingangsexport, separates eEB, kontrollierter Auftrag und Sendeversuch, Timeout-Aufklärung, persönliche Sendeschritte und Token-Notfall. Die Kennungen entsprechen der zentralen Produktmatrix: `eingang-<id>`, `eeb-<id>`, `versandauftrag-<id>`, `versandnachweis-<id>`; `bea-versuch-<id>` dokumentiert einen davon getrennten Versuch.

## 2. Rechtliche und technische Grenzen

Die Vorschriften und die unten bezeichneten Entscheidungsstellen wurden tatsächlich geöffnet und gelesen. Der Agentenklick in einer anwaltlichen Sitzung wird als eigener vorsichtiger Prototypstandard nicht als persönlicher Versand qualifiziert; keine Entscheidung wird als ausdrückliche Entscheidung über diesen Prototyp ausgegeben. Gültige qeS erlaubt nicht von selbst beliebigen Zugriff oder Datenweitergabe. Für Gesellschaftspostfächer und eEB-Sonderrollen werden die Voraussetzungen getrennt geprüft.

Die beBPo-Entscheidung VII ZB 29/24 von 2026 wird mit ihrer Grenze eingebaut: technische Vollautomatisierung hebt natürliche Inhaltsverantwortung nicht auf; die fehlende Versand-Personenidentität im Behördenpostfach ist nicht auf ein persönliches beA übertragbar. Alle Anker besitzen Trägt und Trägt nicht.

Token/PIN-Hinterlegung ist nur im tatsächlich geeigneten Client beziehungsweise durch einen geprüften Geheimnisspeicher ohne Auslesen durch Modell oder Agentenwerkzeuge vorgesehen. Bei Vollzugriff auf denselben Geheimnisspeicher besteht keine wirksame Trennung; dann bleibt die persönliche Eingabe außerhalb der Agentensicht. Das Plugin stellt weder einen Connector noch eine Zertifizierung produktiver Eignung bereit.

## 3. Amtliche Texte und produktive Herstellerdokumentation

Lokale Rohabrufe liegen zur Nachvollziehbarkeit unter `/tmp/ki339-bea/`; die Tabelle enthält ihre SHA-256-Werte. Erfolgreicher HTTP-Abruf allein wurde nicht als Lektüre ausgegeben. Test- und Schulungshandbücher wurden nicht als Beleg verwendet.

| Geöffnete Quelle | Tatsächlich gelesener Umfang | SHA-256 des Rohabrufs |
|---|---|---|
| [Primärquelle](https://www.gesetze-im-internet.de/ravpv/__26.html) | Vollständig: persönliche Zuordnung, PIN-Geheimhaltung und Anhaltspunkte für unverzügliche Schutzmaßnahmen. | `1cd50b0cc41525f5a6ed9fd06944951e28865989231a7006625f575a01d55de0` |
| [Primärquelle](https://www.gesetze-im-internet.de/ravpv/__23.html) | Vollständig, besonders Absatz 3: Sendedelegation, Ausnahme eEB, Berufsausübungsgesellschaft und Rechtewiderruf. | `19254899cc9d061d789464c34d3ff17653ebbba3c54ca064b1b4e708a650b820` |
| [Primärquelle](https://www.gesetze-im-internet.de/zpo/__130a.html) | Vollständig: Formwege, Anlageausnahme, sicherer Weg, Eingang und geeignete Nachreichung. | `84ac976ec9a6c9ee6a19bb6d2256f5c27d16dead83a8f7cdee1e9768d00dd827` |
| [Primärquelle](https://www.gesetze-im-internet.de/zpo/__130d.html) | Vollständig: elektronische Nutzungspflicht, vorübergehende technische Unmöglichkeit und Glaubhaftmachung. | `44f8608bb8913b34cc4f9083e0597df90b33af4a2e036cfdf3f1e442e5c06620` |
| [Primärquelle](https://www.gesetze-im-internet.de/zpo/__173.html) | Vollständig: Absatz 3 eEB/Strukturdaten und Abgrenzung der Adressaten in Absatz 4. | `09437a29738c64733c2c75bfc8caca36b9111bc96c793fcb345dc6a47f969b81` |
| [Primärquelle](https://www.gesetze-im-internet.de/zpo/__175.html) | Vollständig: Schriftstücke gegen Empfangsbekenntnis, Rückgabewege. | `56fab2932da5ca095384661592103adde694cf7a628f482a746bd11c7c933df2` |
| [Primärquelle](https://www.gesetze-im-internet.de/brao/__43e.html) | Vollständig: Dienstleister, Umfang, Textform, Ausland, Mandatseinwilligung und Ausnahmen. | `7dc7b09b6f28a8ba59ad88b60486db2e804876a9971ee27cbda7b573e638b8bd` |
| [Primärquelle](https://handbuch.bea-brak.de/einstellungen-in-ihrem-bea/profilverwaltung/sicherheits-token/name-1) | Hinterlegen und Freischalten, Abschnitte 1 und 2, persönliche Tokenbedienung. | `f75acbd66baa9f7c0dd29a4aaa828e89ef14c7b3b3cdb91e28ce1b01dbd22ab2` |
| [Primärquelle](https://handbuch.bea-brak.de/einstellungen-in-ihrem-bea/postfachverwaltung/benutzerverwaltung-berechtigungskonzept/liste-der-rechte) | Öffnen/Export/Entwurf/Versand, vertrauliche Nachrichten, eEB und VHN-Sonderrollen. | `e86af5c0cdcb522a0ddf59822fa6de5304c218bba45848cef53a3d74e1810d23` |
| [Primärquelle](https://handbuch.bea-brak.de/arbeiten-mit-ihrem-bea/nachrichten/verwalten/exportieren) | Exportdialog, ZIP-Inhalt und verschachtelter Stapelexport. | `70bf1d5acf61757a44e205b247d501f08b9e631e66294c4294c1462cf7aae409` |
| [Primärquelle](https://handbuch.bea-brak.de/arbeiten-mit-ihrem-bea/nachrichten/oeffnen-und-anzeigen/elektronisches-empfangsbekenntnis-eeb/versenden) | Abgeben, Ablehnen, Zustellungsdatum, Signaturweg, einmalige Antwort und Sendeschritt. | `a370290da68d06407eab1f17caa7844c490dd81e05d4e0df88d21c64d05dfdb0` |
| [Primärquelle](https://handbuch.bea-brak.de/arbeiten-mit-ihrem-bea/nachrichten/erstellen-und-senden/dialog-nachrichtenentwurf) | Absender/Empfänger/Aktenzeichen, Anhangstyp und Signatur-/eEB-Felder. | `21c14819dc51029c3c5f8167d8bbc24c5c50e7f4890f6277bf3e5631950da46f` |
| [Primärquelle](https://handbuch.bea-brak.de/arbeiten-mit-ihrem-bea/nachrichten/oeffnen-und-anzeigen) | Nachrichten-ID, Eingangszeit, Status und eEB-Anforderung/Antwort. | `236b7fada720edbeac47ea6c0f78ac586c7fed41b269b1fc7ddf016e16842493` |
| [Primärquelle](https://handbuch.bea-brak.de/einstellungen-in-ihrem-bea/profilverwaltung/sicherheits-token) | Postfachseitige Tokenverwaltung; Grenze zum nur lokalen Löschen. | `c11cbc2bf7ee072573f93245e054d7ca992bf8056f6e643cd855a79d4404a324` |
| [Primärquelle](https://handbuch.bea-brak.de/einrichtung-von-bea/bea-client-security/authentifizieren/vertrauenswuerdiger-herkunftsnachweis-vhn) | Prüfprotokoll, vhn.xml und fehlende Benutzerausweisung bei besonderen Rechten. | `e6a13d97b7863b80b8d03f1817f71a3c2bf2efbac9e316a08730f513fedeb64a` |
| [Primärquelle](https://handbuch.bea-brak.de/einrichtung-von-bea/organisatorische-und-technische-voraussetzungen/notwendige-schutzvorkehrungen-fuer-diese-anwendung) | Geschützter Einsatzbereich, aktuelle Software und vertrauliche PIN-Eingabe. | `ee6f09e6f3822703d0316cb48992fa19ed0dfbf4b096c68a40d71f71df818d9d` |
| [Primärquelle](https://www.bundesgerichtshof.de/SharedDocs/Entscheidungen/DE/Zivilsenate/VIII_ZS/2022/VIII_ZB__80-22.pdf?__blob=publicationFile&v=1) | Rn. 20–35: richtige Datei, Dateiname/Anhangsbezeichnung und Eingangskontrolle. | `5ad7c07c3d209bfe580cc3f216afaf0575227655115459f3b0b004f97037d06f` |
| [Primärquelle](https://www.bundesgerichtshof.de/SharedDocs/Entscheidungen/DE/Zivilsenate/VIII_ZS/2023/VIII_ZB__59-23.pdf?__blob=publicationFile&v=1) | Rn. 7–10: tatsächlicher gerichtlicher Eingang und spätere Aktenzuordnung. | `02c9dd1b79b61baa53ac0069fba1d940f67128b099ee7e48d2231f41dec3ea1f` |
| [Primärquelle](https://www.bundesgerichtshof.de/SharedDocs/Entscheidungen/DE/Zivilsenate/VII_ZS/2024/VII_ZB__29-24.pdf?__blob=publicationFile&v=1) | Rn. 23–29 und 33–34: persönliches beA, beBPo, natürliche Inhaltsverantwortung bei automatischem Verfahren. | `cf95ae289aa3af22fda42c912eff29e4a51b89970102271eb1b30c8ed3d4d787` |
| [Primärquelle](https://www.bundesgerichtshof.de/SharedDocs/Entscheidungen/DE/Zivilsenate/IX_ZS/2023/IX_ZB__30-23.pdf?__blob=publicationFile&v=1) | Rn. 9–15; außerdem Berichtigungsbeschluss 25.03.2024, nur Schreibversehen in Rn. 5. | `735d7a5b7392aeaf71596d9b1ddbfed0997312c22154ac389c82b30b8aaa479f` |
| [Primärquelle](https://www.bundesfinanzhof.de/de/entscheidung/entscheidungen-online/detail/pdf/STRE202410229?type=1646225765) | Rn. 20–26: persönliche Versendung einfach signierter Dokumente, keine Weitergabe anwaltlicher Zugangsdaten. | `f89482edadea1e70de60170db35c52089d20f5a93c2868f0f886086b884c63e7` |
| [Primärquelle](https://zertifizierungsstelle.bnotk.de/sperren) | Aktuelle Sperrseite: beA-Hotline, berechtigte Person, persönliches Sperrkennwort, schriftlicher Weg. | `445779eba1add17f6a1c86b8c7b94b8a146ac743b39fb4f29f1431a8f7ee0d0f` |
| [Primärquelle](https://zertifizierungsstelle.bnotk.de/bestellen/beaprodukte/bea-produkte-softwarezertifikat) | Produktfunktionen und Grenzen; keine Aussage über Zulassung autonomer KI-Bedienung. | `f6690661bca0a3f298242c6e5914ffa2a90e29bc1de285dfe81f9141584d1411` |
| [Primärquelle](https://zertifizierungsstelle.bnotk.de/agb) | Besondere Produktbedingungen, beA-Softwarezertifikat und beA-Karte Mitarbeiter; keine Übernahme sonstiger Gebühren-/Fristangaben. | `641544879919b5929516a4f2cc479a6e3110c66db7b9ec6ad9310dbfabda8ed4` |
| [Primärquelle](https://www.gesetze-im-internet.de/zpo/__131.html) | Vollständig: Abschrift, Auszug, bekannte/umfangreiche Urkunden. | `8338c4db92e22e91cb15c52159ba31334ef5fbb2971d7bc1f7df6b61efce04ac` |
| [Primärquelle](https://www.gesetze-im-internet.de/zpo/__133.html) | Vollständig: Abschriftenausnahme elektronischer Dokumente. | `7ace4832935f83d4b05b904d989a67a5b0b7103e837209eb2910b8556eaa3ce7` |
| [Primärquelle](https://www.gesetze-im-internet.de/ervv/__2.html) | Vollständig: PDF/TIFF, technische Standards, strukturierter Datensatz. | `6cf8f537bdeb65fb13478a6442166a344b32d3d809c706cdb00729f27bc869b2` |
| [Primärquelle](https://www.gesetze-im-internet.de/ervv/__4.html) | Vollständig: Übermittlungswege bei qeS und Verbot der Containersignatur. | `890bd24249fb820d5b55c480f750050ca8e34287aa65fe88f20e364d33e27b52` |
| [Primärquelle](https://www.gesetze-im-internet.de/ervv/__5.html) | Vollständig: Gegenstände der technischen Bekanntmachung. | `a1072680ffc87d3234e772ab392e008b62e752ce4bbdc1f80afae467c440b8fd` |
| [Primärquelle](https://justiz.de/laender-bund-europa/elektronische_kommunikation/bundesanzeiger_29_07_2025.pdf) | Beide Seiten: Formate, Grenzen, Dateinamen, technische Eigenschaften und Signaturstandards. | `5934eb2fbfe8c569cd6b00d153089afddc8be4f3bd8abcc80856a0ac67ab31de` |
| [Primärquelle](https://handbuch.bea-brak.de/arbeiten-mit-ihrem-bea/nachrichten/erstellen-und-senden/anhaenge-hochladen) | Uploadgrenzen 84/90 Zeichen, Gesamtzahl und Menge einschließlich Zusatzdateien. | `6e2bdb953d2ffb3af5b194123c79829325cfd89b5a5a51a985c378a971aadb53` |

Der amtliche BVerwG-Volltext [5 B 8.25, Rn. 3–5](https://www.bverwg.de/160525B5B8.25.0) wurde über das Webwerkzeug geöffnet und gelesen; der parallele direkte Abruf erhielt 403. Es wird daher kein lokaler Rohhash behauptet. Die geraten benannte Unterseite zur PIN-Eingabe erhielt 404 und ist weder Quelle noch Link der Endfassung. Für die PIN-Sicherheit wurden § 26 RAVPV und die produktiven Schutzvorkehrungen gelesen.

## 4. Selbstprüfung und tatsächliche Testgrenze

Der lokale Strukturtest prüfte die sechs Hauptabschnitte in ihrer Reihenfolge, den Wortkorridor, die Beschreibung mit maximal 360 Zeichen, Pflichtwörter, verbotene Zeichen, existierende relative Links, maximal vier Tabellenspalten und Leerzeilen nach Überschriften. Ergebnis: bestanden. 2 ausgeschriebene Wochentage wurden mit Python datetime gegen ihr Datum abgeglichen; bestanden.

Inhaltliche Gegenproben: bloße Computerfreigabe erlaubt keinen Ausgang; einfache Signatur fordert persönliche Versendung; qeS ohne rechtmäßigen Zugang reicht nicht; Eingang löst kein eEB aus; eEB-Datum wird nicht aus Öffnungszeit erfunden; Timeout führt zuerst zur Aufklärung; lokales Tokenlöschen ersetzt keine Sperrung; Fristobjekt bleibt ohne echten Kalendereintrag vorläufig. Die beschriebenen Gegenproben sind redaktionelle Prüfungen, keine Behauptung eines produktiven UI- oder Modelltests. Unabhängige Gesamtproben und Pakettests führt die Integrationsrunde aus.

Skill-SHA-256 nach dieser Teilprüfung: `a2d7bf1d6bbc7813a80c4d931074fc5b159b4db476dc676ec2c96f9f54f35568`. Referenz-SHA-256: `840d281fa22bb1e1866d451ebff2c2a542477e774d45512b8c5f0c4ee06ca42d`.

## 5. Nachtrag der Integration

Die Referenz stellt nach dem Skill-Selbsttest zusätzlich ausdrücklich klar, dass der Computerlauf-Prototyp jedes eEB der benannten Person überlässt. Das ist eine engere technische Vorgabe, keine pauschale Rechtsaussage über sämtliche Delegationsmöglichkeiten. Der Skill blieb unverändert. Endhash der Referenz: `06b3ae071b8226576879a6a51fe18940fca3d60c6483a2e3fb28858c840cc964`.
