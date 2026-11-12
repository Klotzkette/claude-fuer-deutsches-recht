---
name: kontrollversagen-und-organentscheidung
description: "Bearbeitet Kontrollversagen vom Erstbefund bis zum Wiederanlauf. Rekonstruiert die betroffenen Vorgänge anhand von Originalbelegen und unterscheidet bestätigte Abweichungen von offenen Nachweisen. Erstellt einen Organbericht mit Beschlussoptionen, Sperren, Nachtests, Zuständigkeiten und Fristen."
---

# Kontrollversagen und Organentscheidung

## 1 Zweck und Anwendungsfall

Erstellen Sie für Legal, Compliance oder Interne Revision eine belastbare Entscheidungsvorlage, wenn eine Freigabesperre umgangen wurde, eine Kennzahl die Kontrollwirkung falsch darstellt oder ein erheblicher Vorgang außerhalb des Sitzungsturnus eskaliert werden muss. Der Auftrag reicht vom belegbaren Erstbefund über die Sicherung des Betriebs bis zur Entscheidung über einen kontrollierten Wiederanlauf. Die allgemeine Kontrollplanung und Regelberichterstattung bearbeitet der Skill [Kontrollen und Organberichte](../kontrollen-und-organberichte/SKILL.md).

## 2 Eingaben

- Benötigt werden der Kontrollzweck, die zum Vorgang gehörende Anweisung und Version, der genaue Soll-Zeitpunkt, Rollen und Vertretungen, Population und Zeitraum, bereits ergriffene Maßnahmen, Entscheidungsbedarf und Frist.
- Prüfen Sie Originalaufträge, Ausführungs- oder Zahlungsbelege, Genehmigungen, ERP- und Workflow-Logs, Zeitzonen, Buchungs- und Geschäftsereignisse, Ausnahmeregister und Exportdefinitionen. Ziehen Sie Organigramm, Satzung, Geschäftsordnung, Zuständigkeitsordnung und gegebenenfalls Konzernberichte bei.
- Bei fehlenden Belegen beginnen Sie mit dem nachweisbaren Risiko, einer angemessenen vorläufigen Maßnahme und der nächsten fristgebundenen Entscheidung. Nennen Sie die stärkste alternative Erklärung und die Quelle, mit der sie geprüft werden kann. Arbeiten Sie Nachlieferungen in dieselbe Vorlage ein. Kennzeichnen Sie neue Tatsachen, revidierte Kennzahlen und die Folgen für den Beschluss.

## 3 Ablauf und Checkliste

### 3.1 Erstlage und Sicherung

Rekonstruieren Sie den Ablauf vom ausgelösten Geschäftsvorfall bis zur tatsächlichen Leistung oder Zahlung. Halten Sie pro Fall getrennt fest, wer die Entscheidung wann getroffen hat, wann sie dokumentiert wurde und wann sie wirkte. Sichern Sie verfügbare Primärbelege und deren Zeitbasis im berechtigten Kreis. Beschreiben Sie, welcher Prozess, Zeitraum, Standort oder Rechtsträger betroffen ist und welche Abhängigkeiten die Annahme weiterer Fälle stützen.

Entwerfen Sie bei konkretem Wiederholungsrisiko eine eng begrenzte Sperre, manuelle Zweitprüfung oder andere dokumentierte Zwischenmaßnahme. Nennen Sie zuständige Person und Vertretung, Beginn, Grenze, Kontrollnachweis, Kosten, mögliche Nebenwirkungen und Überprüfungstermin. Der Zwischenweg muss im betroffenen Betrieb einschließlich Randzeiten durchführbar sein. Trennen Sie eine Untersuchungshypothese von einer festgestellten Pflichtverletzung. Legen Sie offen, was zum jeweiligen Entscheidungszeitpunkt bekannt war.

### 3.2 Kennzahl mit nachvollziehbarem Nenner

1. Definieren Sie die Prüfeinheit vor der Auswertung. Eine Freigabe je Geschäftsvorfall, ein Lieferant und eine Rechnungszeile führen zu unterschiedlichen Quoten. Legen Sie Stichtag, Quelle, Filter, Pflicht zur Kontrolle, Statusdefinitionen, technische Join-Schlüssel und Zeitzone fest.
2. Leiten Sie aus den Rohzeilen die eindeutigen, kontrollpflichtigen Vorgänge her. Führen Sie Dubletten, stornierte Vorgänge, Testdaten, zulässige Ausnahmen und fehlende Schlüssel mit Anzahl und Gründen auf. Prüfen Sie unabhängig, welche Vorgänge tatsächlich ausgelöst, extern ausgeführt oder bezahlt wurden. Ein ausgeführter Vorgang mit fehlender Zeitspur bleibt in der Risikopopulation sichtbar.
3. Geben Sie mindestens die Grundgesamtheit der Statusauswertung, die Population der materiellen Kontrolle und die Stichprobengröße getrennt an. Stellen Sie jeweils Zähler, Nenner, Regel, Fundstelle und Zeitstand dar. Für zeitliche Prüfbarkeit ist der Zähler die Zahl ausgeführter Vorgänge mit ausreichenden Zeitbelegen und der Nenner die Zahl der für diese Kontrolle relevanten ausgeführten Vorgänge. Für Rechtzeitigkeit ist der Zähler die Zahl belegter rechtzeitiger Freigaben. Wenn Sie dafür nur prüfbare Vorgänge als Nenner verwenden, zeigen Sie die nicht prüfbaren separat bezogen auf die gesamte betroffene Population.
4. Führen Sie Ergebnisse als belegt rechtzeitig, belegt verspätet, begründet ausgenommen und mangels Beleg offen. Trennen Sie »Kontrolle als durchgeführt dokumentiert«, »formal und inhaltlich ordnungsgemäß ausgeführt« und »Wiederholung wirksam verhindert«. Ziehen Sie aus einer risikobasierten Stichprobe keine repräsentative Fehlerquote. Nennen Sie Auswahlmechanismus, Abdeckung und ausgelassene Gruppen. Prüfen Sie bei einer Vollprüfung zusätzlich, ob die Datenquellen die gesamte Population erfassen.
5. Rechnen Sie Auswirkung und Kapazität separat. Geben Sie bei Sperren Volumen, Fristen, verfügbares Personal und verbleibende Lücken an. Stellen Sie mögliche Schadens-, Liquiditäts- und Reputationsfolgen mit Szenario und Annahmen dar. Vermeiden Sie Doppelzählungen und weisen Sie Bandbreiten und offene Kausalität aus.

### 3.3 Unabhängige Nachvollziehung der Kontrollausführung

Beauftragen Sie in der Vorlage eine geeignete Person außerhalb der verantwortlichen Ausführung mit dem erneuten Durchspielen der Kontrolle. Sie ermittelt die vor dem maßgeblichen Zeitpunkt verfügbaren Daten, wendet die damals gültige Regel erneut an und vergleicht ihr Ergebnis mit dem protokollierten Ablauf. Verifizieren Sie Rollen, Autorisierungsgrenzen, Genehmigungsinhalt, Vertrags- oder Ausführungsbeginn, Unveränderlichkeit der Belege und spätere Korrekturen. Unterscheiden Sie die historische Nachvollziehung von einem Funktionsnachtest der geänderten Kontrolle.

| Beobachtung | Aussage und Gegenprobe |
| --- | --- |
| Das System zeigt einen grünen Status. | Ermitteln Sie die auslösende Systemregel und prüfen Sie, ob das Originalereignis und seine Zeitbasis vollständig und vergleichbar vorliegen. |
| Ein Freigabestempel ist erst nach Ausführung sichtbar. | Sichern Sie unabhängige Belege für eine etwaige frühere autorisierte Entscheidung. Prüfen Sie, ob die frühere Form nach der damals geltenden Regel zulässig war und denselben Vorgang erfasste. |
| Ein Paralleltest meldet einen blockierten Auftrag. | Testen Sie die produktionsnahe Schnittstelle, die wirksame Konfiguration und gewöhnliche Rollen. Prüfen Sie manuelle Umgehungen und ob der Ausgang tatsächlich blockiert blieb. |
| Eine Gesamtsumme liegt nahe an einer Zeichnungsgrenze. | Gleichen Sie Auftrag, sachlichen Zusammenhang, Zeitpunkte und Zeichnungsregel ab. Vermerken Sie eine mögliche Aufteilung als prüfbedürftig, solange Zusammenhang und Zurechnung offen sind. |

Halten Sie pro Prüfstück Ausgangsdaten, Soll, Durchführung, Ergebnis, Abweichung, Gegenprobe, Prüfer und Zeit fest. Decken Sie besonders fehlenden Zweitzeichner, verspätete Entscheidung, Ersatzpfad, ausfallende Schnittstelle, manuelle Ausnahme und einen Wiederholungsversuch nach Sperre ab. Führen Sie für materielle Zeitvorgaben Abweichungen in Minuten oder Kalendertagen mit Start- und Endbeleg aus.

### 3.4 Organweg und Rechtsprüfung

- **Leitung.** Ordnen Sie die Entscheidung dem zuständigen Rechtsträger und seinem Leitungsorgan zu. Prüfen Sie Organisations- und Sorgfaltspflichten sowie etwaige unternehmerische Ermessensspielräume nach § 93 Abs. 1 AktG im anwendbaren Gesellschaftsregime. Dokumentieren Sie die damals verfügbare Information, die wesentlichen Alternativen und das Gesellschaftswohl. Prüfen Sie verbindliche Vorgaben und die Abhilfe bei Rechtsverstößen gesondert. § 91 Abs. 2 AktG betrifft die Früherkennung bestandsgefährdender Entwicklungen. Die zusätzliche ausdrückliche IKS- und Risikomanagementpflicht nach Abs. 3 knüpft an die Börsennotierung an.
- **Aufsicht und Ausschuss.** Prüfen Sie bei der AG die Berichtswege des § 90 AktG einschließlich besonderer Anlässe, die Überwachung und Zustimmungsvorbehalte nach § 111 sowie den tatsächlichen Auftrag des Ausschusses nach § 107. Halten Sie Berichtsempfang, Kontrolle, etwaige Zustimmung und operative Durchführung auseinander. Benennen Sie für einen Prüfungsausschuss, welche Unterlagen er braucht und was das Plenum entscheidet. Prüfen Sie für den besonderen Informationsweg nach § 107 Abs. 4 AktG dessen Voraussetzungen und den Weg über den Ausschussvorsitzenden. Ein Bericht oder eine Zustimmung überträgt die Geschäftsführung nicht auf den Aufsichtsrat. [AktG §§ 90–93](https://www.gesetze-im-internet.de/aktg/BJNR010890965.html) · [§ 107 AktG](https://www.gesetze-im-internet.de/aktg/__107.html) · [§ 111 AktG](https://www.gesetze-im-internet.de/aktg/__111.html)
- **SE und Tochtergesellschaft.** Stellen Sie bei der SE Sitz, Leitungsmodell und Satzung fest. Prüfen Sie zunächst SE-VO und SEAG und erst dann das ergänzend anwendbare nationale Recht nach Art. 9 SE-VO. Im dualistischen Modell sind Überwachung und Unterrichtung insbesondere nach Art. 40 und 41 SE-VO zu prüfen. Bei einer deutschen SE kann das einzelne Mitglied Auskunft nach Art. 41 Abs. 3 Satz 1 in Verbindung mit § 18 SEAG beim Leitungsorgan für das Aufsichtsorgan verlangen. Prüfen Sie daneben den konkreten Ausschussauftrag und etwaige Zustimmungsvorbehalte. Stellen Sie für Tochtergesellschaften das örtlich zuständige Organ, die Auswirkungen auf die Mutter und die zulässige Information in den Konzern getrennt fest. Nehmen Sie sensible personenbezogene Daten nur im erforderlichen und zulässigen Umfang auf. [SE-VO, Art. 9 und 38–42](https://eur-lex.europa.eu/eli/reg/2001/2157/oj/deu) · [§ 18 SEAG](https://www.gesetze-im-internet.de/seag/__18.html)
- **§ 130 OWiG.** Benennen Sie die konkrete straf- oder bußgeldbewehrte Pflicht des Inhabers, die tatsächliche Zuwiderhandlung, die im Fall erforderliche Aufsichtsmaßnahme, ihr vorsätzliches oder fahrlässiges Unterlassen und die Vermeidbarkeit oder wesentliche Erschwerbarkeit des Verstoßes durch gehörige Aufsicht. Ordnen Sie Auswahl, Bestellung und Überwachung von Aufsichtspersonen zu. Prüfen Sie gegebenenfalls die Zurechnung nach § 9 OWiG. Eine auffällige Kontrollquote begründet für sich keinen Sanktionsbefund. Abhilfe kann bei nachvollziehbarem Risiko schon während der Sachaufklärung geboten sein. [§ 130 OWiG](https://www.gesetze-im-internet.de/owig_1968/__130.html) · [§ 9 OWiG](https://www.gesetze-im-internet.de/owig_1968/__9.html)

Bestimmen Sie den frühesten belegbaren Zeitpunkt für eine Eskalation und an wen sie gehen muss. Trennen Sie vorläufige Information mit wesentlichen Fakten, Maßnahmen und Unsicherheiten, die spätere vollständige Vorlage und eine gegebenenfalls separate gesetzliche oder vertragliche Meldung. Nennen Sie für eine externe Meldung Rechtsgrundlage, Auslöser, Empfänger, Frist und befugte Stelle. Legen Sie einen Entwurf im beauftragten Umfang vor. Die zuständige Person entscheidet und handelt.

### 3.5 Entscheidung und Wiederanlauftests

Legen Sie den relevanten Entscheidungsträgern realisierbare Optionen mit Kosten und verbleibendem Risiko vor. Der Entwurf bezeichnet den betroffenen Umfang, die Maßnahme, einen namentlich oder funktional bestimmten Verantwortlichen mit Vertretung, den Nachweis, die Frist und die Entscheidungsstelle. Er nennt die Kriterien, bei denen die Übergangsmaßnahme fortbesteht oder erweitert werden muss.

Führen Sie im Wiederanlaufplan die Behebung der Ursache und die unabhängigen Tests mit Sollwert und Protokoll getrennt auf. Testen Sie die Sperre mit einem unvollständigen oder verspäteten Vorgang, die korrekte Freigabe eines zulässigen Vorgangs, Rollenwechsel und den Rückfallweg bei Störung. Verlangen Sie bei Schnittstellenfehlern die Gegenprobe am tatsächlichen Ausgang, einschließlich eines unbeabsichtigten erneuten Starts. Legen Sie fest, wie bereits freigegebene Vorgänge rückwirkend gesichtet und korrigiert werden. Planen Sie den begrenzten Start mit Beobachtungszeit, Stoppschwellen, Eskalationsweg und einem weiteren Prüftermin. Ein unabhängiger Nachtest und eine dokumentierte Entscheidung schließen die Maßnahmen erst im nachgewiesenen Umfang.

## 4 Quellenpflicht

Zitieren Sie je entscheidender Tatsache Originaldatei und Fundstelle, etwa Vorgangs-ID, Tabellenzeile, Protokollzeit mit Zeitzone, Regelversion, Rechnungsposition oder Entscheidungsminute. Nennen Sie bei amtlichen Quellen Norm, Absatz, Fassung, Prüftag und Aussagegrenze. Halten Sie Fallannahmen, offene Nachweise, widerlegte Erklärungen und aktuelle Primärquellen getrennt. Beachten Sie die [Zitierweise](../../references/zitierweise.md), die [Belegprüfung und Fallwege](../../references/belegpruefung-und-fallwege.md) und die [Geschäftspartner- und Kontrollprüfung](../../references/geschaeftspartner-und-kontrollpruefung.md).

## 5 Ausgabeformat

Liefern Sie den **ausformulierten internen Eskalationsbericht** mit Entscheidungsgegenstand und Zeitpunkt, gesichertem Befund, abweichender Lesart, betroffenen Rechtsträgern, geprüften Organwegen, Optionen und beantragtem Beschluss. Die erste Seite nennt Reichweite und Status der Sofortmaßnahme, Entscheidungsstelle und nächsten Termin. Fügen Sie bei Bedarf getrennte Anlagen für Nennerabgleich, Kontrollnachtest, Zeitachse und Maßnahmenplan bei. In der Nachtesttabelle stehen je Vorgang »Prüfgegenstand und Quelle«, »Soll und Zeitpunkt«, »nachvollzogenes Ist«, »Gegenprobe« und »Folge für Sperre oder Wiederanlauf«.

Für das Endprodukt gilt die Ausformulierungspflicht. Schreiben Sie in vollständigen Sätzen. Skelette, Halbsätze und reine Aufzählungen genügen als Endprodukt nicht. Verwenden Sie soweit technisch möglich Times New Roman 11 pt und ausschließlich dezimale Gliederung. Bei reiner Textausgabe steht der Formatstandard in einem getrennten Exporthinweis.

## 6 Beispiele

| Hamelner Fall | Konkretes Prüfprodukt |
| --- | --- |
| ME-12 | Rekonstruieren Sie Freigabe und Ausführung für jeden betroffenen Auftrag. Trennen Sie eine Verspätung, eine belegte frühere Genehmigung und einen fehlenden zweiten Zeichner. |
| ME-16 | Leiten Sie aus dem Rohbestand die berichtsfähigen Fälle ab. Entwerfen Sie für den Ausschuss eine Entscheidungsvorlage mit offenem Nachtest und Grenzen der Kontrollquote. |
| ME-20 | Stellen Sie das risikobasierte Prüfstundenbudget den Werken und konkreten Kontrollschritten gegenüber. Legen Sie offene Abdeckung und den Auslöser für eine Nachprüfung offen. |
| ME-26 | Ordnen Sie den erheblichen Vorgang der Tochter und die Berichtspflicht der Mutter zu. Beurteilen Sie den Informationsweg des einzelnen Mitglieds und die rechtzeitige Unterrichtung des Aufsichtsorgans. |
| ME-28 | Rekonstruieren Sie die Statusquote, den Bestand tatsächlich ausgeführter Vorgänge und den engeren Bestand zeitlich prüfbarer Fälle. Führen Sie gezielte Stichprobe und unabhängigen Wiederanlauftest gesondert. |

In ME-28 ergeben 588 grüne Statuswerte unter 600 Vorgängen eine Anzeigequote von 98 Prozent. Bei 460 extern ausgeführten Vorgängen und 26 fehlenden Zeitstempeln sind im Ausgangsstand höchstens 434 Vorgänge zeitlich prüfbar. Diese Obergrenze belegt noch keine rechtzeitige Freigabe. Vier auffällige Stücke in einer gezielten Probe von 24 Vorgängen begründen weitere Nachtests. Prüfen Sie vor jeder Fortschreibung, ob zusätzliche Originalbelege einen der Fälle klären oder den Nenner verändern.

Ein möglicher Beschlussentwurf folgt.

»Die Bereichsleitung führt die betroffenen Aufträge bis zur erneuten Freigabe nur nach dokumentierter Doppelprüfung aus. Der Prüfauftrag an die Interne Revision umfasst die technische Sperre und den manuellen Ersatzpfad einschließlich Vertretung. Die Revision legt dem Leitungsorgan ihre Ergebnisse mit Originalbelegen zum festgelegten Entscheidungstermin vor. Bei einem nicht bestandenen Sperrtest bleibt die Übergangsregel in Kraft. Das Leitungsorgan berichtet dem zuständigen Aufsichtsorgan über Befund, Reichweite und das Ergebnis der erneuten Entscheidung.«
