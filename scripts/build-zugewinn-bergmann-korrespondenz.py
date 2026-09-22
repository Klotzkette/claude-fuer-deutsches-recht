#!/usr/bin/env python3
"""Erzeugt ausschließlich die Korrespondenz und Primärdokumente der Akte Bergmann."""

from __future__ import annotations

import argparse
import hashlib
import io
import json
from datetime import datetime, timezone
from email import policy
from email.message import EmailMessage
from email.parser import BytesParser
from email.utils import format_datetime, parseaddr
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile, ZipInfo

from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Cm, Inches, Pt, RGBColor


ROOT = Path(__file__).resolve().parents[1]
CASE = ROOT / "testakten/zugewinnausgleich-familie-bergmann-potsdam"
AKTEN = CASE / "aktenstuecke"
MAILS = CASE / "korrespondenz"
DOCX_MIME = "vnd.openxmlformats-officedocument.wordprocessingml.document"
STAMP = datetime(2026, 9, 15, 12, 0, tzinfo=timezone.utc)

FELDKAMP = "Dr. Lukas Feldkamp\nRechtsanwalt\nCharlottenstraße 61 · 14467 Potsdam"
RITTER = "Anselm Ritter\nRechtsanwalt\nZeppelinstraße 42 · 14471 Potsdam"
MARA = "Mara Bergmann\nKastanienweg 18\n14476 Potsdam"
JONAS = "Jonas Bergmann\nFeuerbachstraße 9\n14471 Potsdam"
AN_FELDKAMP = "Herrn Rechtsanwalt\nDr. Lukas Feldkamp\nCharlottenstraße 61\n14467 Potsdam"
AN_RITTER = "Herrn Rechtsanwalt\nAnselm Ritter\nZeppelinstraße 42\n14471 Potsdam"


def doc(name, sender, recipient, date, reference, title, paragraphs, signatory,
        salutation=None, closing=None, author=None):
    return dict(name=name, sender=sender, recipient=recipient, date=date,
                reference=reference, title=title, paragraphs=paragraphs,
                signatory=signatory, salutation=salutation, closing=closing,
                author=author or signatory.split("\n")[0].removeprefix("gez. "))


DOCUMENTS = [
    doc(
        "01_eheregister_textabschrift_2026-06-10.docx",
        "Landeshauptstadt Potsdam\nStandesamt\nEheregister",
        MARA, "Potsdam, 10.06.2026", "Bezug: Eheschließung am 18.06.2011 in Potsdam",
        "Abschrift der Angaben zur Eheschließung",
        [
            "Für Frau Mara Bergmann werden die nachstehenden Personen- und Heiratsangaben aus dem Eheregister in Textform wiedergegeben. Die Abschrift beschränkt sich auf diese Angaben.",
            ("1 Eheschließung", "Jonas Bergmann und Mara Kreuter haben am 18.06.2011 in Potsdam die Ehe geschlossen. Die Eheschließung wurde beim Standesamt Potsdam beurkundet."),
            ("2 Angaben zu den Ehegatten", "Der Ehemann führt den Namen Jonas Bergmann. Er wurde am 17.02.1978 geboren. Die Ehefrau führt seit der Eheschließung den Namen Mara Bergmann, geborene Kreuter. Sie wurde am 04.09.1980 geboren."),
            ("3 Namensführung", "Die Ehegatten führen den gemeinsamen Ehenamen Bergmann. Der Geburtsname der Ehefrau bleibt Kreuter."),
            "Diese Textabschrift enthält keine Beglaubigung. Sie wird auf die Anfrage von Frau Bergmann zur Vorlage bei ihrem Verfahrensbevollmächtigten ausgegeben.",
        ], "gez. Helene Krüger\nStandesbeamtin", author="Standesamt Potsdam",
    ),
    doc(
        "02_scheidungsantrag_auszug_2026-06-22.docx", FELDKAMP,
        "Amtsgericht Potsdam\nFamiliengericht\nPotsdam", "Potsdam, 22.06.2026",
        "Mein Zeichen: 166/26 LF\nÜbermittlung über das besondere elektronische Anwaltspostfach",
        "Scheidungsantrag Bergmann gegen Bergmann",
        [
            "Auszug aus dem Antragsschriftstück vom 22.06.2026: Wiedergegeben werden die Angaben zu den Beteiligten, der Scheidungsantrag und der Sachvortrag zur Trennung.",
            "Antragstellerin ist Frau Mara Bergmann, geborene Kreuter, geboren am 04.09.1980, Kastanienweg 18, 14476 Potsdam. Ich vertrete sie aufgrund erteilter Vollmacht. Antragsgegner ist Herr Jonas Bergmann, geboren am 17.02.1978, Feuerbachstraße 9, 14471 Potsdam.",
            ("1 Antrag", "Namens und in Vollmacht der Antragstellerin beantrage ich, die am 18.06.2011 vor dem Standesamt Potsdam geschlossene Ehe der Beteiligten zu scheiden."),
            ("2 Angaben zur Ehe", "Beide Beteiligten besitzen die deutsche Staatsangehörigkeit und leben in Deutschland. Ein Auslandsbezug besteht nicht. Ein Ehevertrag wurde nicht geschlossen. Aus der Ehe stammen Jule Bergmann, geboren am 12.03.2013, und Oskar Bergmann, geboren am 27.08.2016. Die Kinder leben bei der Antragstellerin im bisherigen Familienheim."),
            ("3 Trennung", "Die Beteiligten leben seit dem 01.04.2025 getrennt. Der Antragsgegner zog an diesem Tag aus dem Haus am Kastanienweg 18 in die Wohnung Feuerbachstraße 9. Die Antragstellerin verblieb mit den Kindern im Haus. Die eheliche Lebensgemeinschaft wurde seither nicht wieder aufgenommen. Gemeinsame Absprachen über die Kinder und die Urlaubsorganisation änderten daran nach Angaben der Antragstellerin nichts."),
            "Die Antragstellerin will die eheliche Lebensgemeinschaft nicht wiederherstellen. Sie hält die Ehe für gescheitert und stützt den Scheidungsantrag auf Paragraf 1565 Absatz 1 BGB. Eine Zustimmungserklärung des Antragsgegners wird mit diesem Antrag nicht vorgelegt.",
            "Die vermögensrechtliche Auseinandersetzung ist zwischen den Beteiligten noch nicht abgeschlossen. Ein bezifferter Antrag auf Zugewinnausgleich ist nicht Gegenstand dieses Antragsschriftstücks.",
        ], "Dr. Lukas Feldkamp\nRechtsanwalt", author="Dr. Lukas Feldkamp",
    ),
    doc(
        "03_zustellungsmitteilung_2026-07-13.docx",
        "Amtsgericht Potsdam\nFamiliengericht\nGeschäftsstelle", AN_FELDKAMP,
        "Potsdam, 13.07.2026", "Aktenzeichen: 41 F 218/26\nIhr Zeichen: 166/26 LF",
        "Mitteilung über die Zustellung des Scheidungsantrags",
        [
            "in der Familiensache Mara Bergmann gegen Jonas Bergmann wird auf Ihre Sachstandsanfrage die Zustellung des Scheidungsantrags mitgeteilt.",
            "Der Antrag Ihrer Mandantin vom 22.06.2026 ist am 24.06.2026 bei dem Amtsgericht Potsdam eingegangen. Er wird unter dem oben angegebenen Aktenzeichen geführt.",
            "Nach der zur Gerichtsakte gelangten Zustellungsurkunde ist die Antragsschrift dem Antragsgegner Jonas Bergmann am 08.07.2026 unter der Anschrift Feuerbachstraße 9, 14471 Potsdam, zugestellt worden.",
            "Diese Mitteilung betrifft den Eingang und die Zustellung der Antragsschrift. Eine Entscheidung über den Scheidungsantrag ist damit nicht verbunden. Ein Termin zur persönlichen Anhörung wird gesondert mitgeteilt.",
            "Bitte geben Sie bei weiterem Schriftverkehr das Aktenzeichen 41 F 218/26 an.",
        ], "gez. Svenja Lenz\nJustizbeschäftigte", "Sehr geehrter Herr Rechtsanwalt Dr. Feldkamp,",
        "Mit freundlichen Grüßen", "Amtsgericht Potsdam",
    ),
    doc(
        "04_vollmacht_mara_bergmann_2026-06-03.docx", MARA, AN_FELDKAMP,
        "Potsdam, 03.06.2026", "Mandat: Bergmann gegen Bergmann\nKanzleizeichen: 166/26 LF",
        "Vollmacht in der Ehesache Bergmann",
        [
            "Ich, Mara Bergmann, geborene Kreuter, geboren am 04.09.1980, bevollmächtige Herrn Rechtsanwalt Dr. Lukas Feldkamp, Charlottenstraße 61, 14467 Potsdam, mich in der Ehesache gegen meinen Ehemann Jonas Bergmann, geboren am 17.02.1978, Feuerbachstraße 9, 14471 Potsdam, zu vertreten.",
            ("1 Gegenstand", "Die Vollmacht umfasst die außergerichtliche und gerichtliche Vertretung wegen der Scheidung unserer am 18.06.2011 in Potsdam geschlossenen Ehe sowie die Auskunft, Beleganforderung und Vertretung wegen des Zugewinnausgleichs. Mein Bevollmächtigter darf hierzu Anträge stellen, Erklärungen abgeben, Schriftsätze einreichen und gerichtliche sowie außergerichtliche Mitteilungen entgegennehmen."),
            ("2 Unterlagen und Auskünfte", "Mein Bevollmächtigter darf die für diese Angelegenheiten erforderlichen Gerichtsakten einsehen und Abschriften anfordern. Er darf sich wegen meiner eigenen Vertrags- und Kontounterlagen sowie wegen Unterlagen zu gemeinsam eingegangenen Verbindlichkeiten an die jeweiligen Vertragspartner wenden. Diese Vollmacht erteilt ihm keine Verfügungsmacht über meine Konten und keine Befugnis, fremde Konten zu verwalten."),
            ("3 Vereinbarungen", "Vergleiche, Anerkenntnisse und Verzichte darf mein Bevollmächtigter erst nach meiner vorherigen Zustimmung erklären. Eine Veräußerung oder Belastung meines Anteils am Haus Kastanienweg 18 ist nicht von dieser Vollmacht umfasst. Die Vollmacht enthält insbesondere keinen Auftrag, das gemeinsame Haus zu verkaufen."),
            "Die Vertretung bezieht sich auf die genannten Angelegenheiten. Eine Beauftragung zur eigenständigen Geltendmachung von Ansprüchen der Kinder ist damit nicht verbunden.",
        ], "Mara Bergmann", author="Mara Bergmann",
    ),
    doc(
        "05_auskunftsverlangen_feldkamp_2026-07-20.docx", FELDKAMP, AN_RITTER,
        "Potsdam, 20.07.2026", "Mein Zeichen: 166/26 LF · Ihr Zeichen: 84/26 AR\nBergmann gegen Bergmann · AG Potsdam 41 F 218/26",
        "Auskunft über das Vermögen Ihres Mandanten",
        [
            "ich vertrete Frau Mara Bergmann auch bei der vermögensrechtlichen Auseinandersetzung. Namens meiner Mandantin verlange ich von Herrn Jonas Bergmann nach Paragraf 1379 BGB Auskunft und Belege zu seinem Vermögen. Bitte lassen Sie mir die Auskunft bis zum 20.08.2026 zukommen.",
            ("1 Stichtage und Verzeichnisse", "Erbeten werden getrennte, geordnete Verzeichnisse über das Vermögen und die Verbindlichkeiten am 18.06.2011, am 01.04.2025 und am 08.07.2026. Bitte bezeichnen Sie die einzelnen Gegenstände, Forderungen und Schulden, die jeweiligen Inhaber und die angesetzten Werte. Soweit Werte noch nicht ermittelt sind, bitte ich um Angabe des Bestands und der noch ausstehenden Unterlagen."),
            "Die Antragsschrift wurde Ihrem Mandanten am 08.07.2026 zugestellt. Auf diesen Tag bezieht sich mein Auskunftsverlangen zum Endvermögen im Hinblick auf Paragraf 1384 BGB. Der Eingang des Antrags am 24.06.2026 wird damit nicht gleichgesetzt.",
            ("2 Konten und Unternehmen", "Bitte legen Sie die zu den Stichtagen gehörenden Konto- und Depotunterlagen einschließlich betrieblicher Konten vor. Für das seit 2007 geführte Einzelunternehmen Bergmann Licht & Planung benötige ich die verfügbaren Jahresabschlüsse beziehungsweise Einnahmenüberschussrechnungen, Anlagenverzeichnisse sowie Angaben zu Forderungen und Verbindlichkeiten. Aus den Unterlagen soll auch hervorgehen, welche Gegenstände und Konten zum Betrieb gehören. Mein Verlangen nach einer Unternehmensbewertung wird dadurch nicht auf die Summe der Buchwerte beschränkt."),
            ("3 Grundstücke und Hausdarlehen", "Für das Haus Kastanienweg 18 bitte ich um die Eigentumsunterlagen und die Unterlagen zum Darlehenskonto HD-2014-731 bei der Havelbogen Bank. Zum Grundstück in Wittbrietzen bitte ich um die Erwerbsunterlagen, die genaue Grundstücksbezeichnung und die vorhandenen Wertunterlagen. Bitte unterscheiden Sie beim Hausdarlehen die im Grundbuch eingetragene Sicherheit von der jeweils offenen Darlehensschuld."),
            "PAGEBREAK",
            ("4 Erwerb von Todes wegen", "Bitte erläutern Sie den Erwerb nach dem am 12.02.2019 verstorbenen Horst Bergmann und legen Sie die Unterlagen über die damals übernommenen Vermögensgegenstände und Verbindlichkeiten vor. Dazu gehören auch die Belege über die mitgeteilten Bestattungskosten. Für das Grundstück bitte ich um die Unterlage, auf der die damalige Wertangabe beruhte, nicht nur um eine heutige mündliche Schätzung."),
            ("5 Gold und digitale Vermögenswerte", "Meiner Mandantin ist der Erwerb von vier Goldmünzen im Jahr 2022 bekannt. Bitte nennen Sie die Bestände zu den erbetenen Stichtagen und legen Sie die Kaufbelege sowie Belege über zwischenzeitliche Verkäufe und den Eingang der Erlöse vor. Entsprechendes erbitte ich für die Bitcoin-Anlage. Die E-Mail an meine Mandantin vom 30.06.2026 enthält hierzu nur die Aussage, Bitcoin sei abgestoßen worden. Angaben über Menge, Transaktionen und verbleibende Bestände fehlen dort."),
            ("6 Frühere Auskunft und Zahlungen an die Mutter", "Ihr Mandant beruft sich auf eine Auskunft aus dem Frühjahr 2025. Bitte übersenden Sie genau die Fassung, auf die er sich bezieht, samt damaligen Anlagen und Übermittlungsnachweis. Meine Mandantin erinnert ein Schreiben, bestreitet aber, vollständige Stichtagsunterlagen erhalten zu haben. Bitte erläutern Sie ferner das von Ihrem Mandanten erwähnte frühere Darlehen seiner Mutter und die monatlichen Zahlungen an sie jeweils nach Anlass, Zeitraum und etwaigen Rückzahlungsabreden."),
            "Ich bitte um eine zusammenhängende Antwort, auch wenn einzelne Belege nachgereicht werden müssen. Bitte benennen Sie dann konkret, welche Unterlagen fehlen und wann mit ihnen zu rechnen ist. Eine Zahlungsforderung wird mit diesem Schreiben noch nicht beziffert.",
        ], "Dr. Lukas Feldkamp\nRechtsanwalt", "Sehr geehrter Herr Kollege Ritter,",
        "Mit freundlichen kollegialen Grüßen",
    ),
    doc(
        "06_antwort_ritter_2026-08-20.docx", RITTER, AN_FELDKAMP,
        "Potsdam, 20.08.2026", "Mein Zeichen: 84/26 AR · Ihr Zeichen: 166/26 LF\nIhr Schreiben vom 20.07.2026 · AG Potsdam 41 F 218/26",
        "Stellungnahme zu Ihrem Auskunftsverlangen",
        [
            "mein Mandant hat mir zu Ihrem Schreiben vom 20.07.2026 die nachstehenden Angaben gemacht. Eine vollständige Zusammenstellung aller Stichtagsbelege liegt mir noch nicht vor. Für die Ergänzung bitte ich um Fristverlängerung bis zum 15.09.2026. Über die hier einzeln angesprochenen Positionen hinaus ist mit diesem Schreiben keine abschließende Bestandsangabe verbunden.",
            ("1 Angaben aus dem Jahr 2025", "Herr Bergmann erklärt, Ihrer Mandantin sein Schreiben vom 06.05.2025 am 08.05.2025 per E-Mail übersandt zu haben. Er betrachtet dies als seine damalige Trennungsauskunft. Er räumt ein, nicht zu jeder Position einen Kontoauszug beigefügt zu haben. Die Darstellung, es habe überhaupt keine Angaben gegeben, weist er zurück. Das damalige Schreiben enthält keine Vermögensgesamtsumme."),
            ("2 Haus und Finanzierung", "Das Haus Kastanienweg 18 wurde 2014 für 326.000,00 Euro erworben. Beide Ehegatten sind zu je einem halben Anteil Eigentümer und beide sind Schuldner des Darlehens bei der Havelbogen Bank. Herr Bergmann akzeptiert nicht, dass sein Miteigentumsanteil bereits mit seinem Auszug wirtschaftlich Ihrer Mandantin zugeordnet wird. Ein aktueller Hauswert ist zwischen den Parteien nicht vereinbart. Die Bankunterlagen zum Darlehenskonto HD-2014-731 werden gesondert beschafft."),
            ("3 Betrieb", "Bergmann Licht & Planung ist seit 2007 das Einzelunternehmen meines Mandanten. Herr Bergmann hält einen von seiner persönlichen Mitarbeit losgelösten erheblichen Kundenstammwert für nicht gerechtfertigt. Die Aufträge werden nach seiner Darstellung überwiegend wegen seiner eigenen Planungsleistung erteilt. Eine pauschale Gleichsetzung von Umsatz und Unternehmenswert lehnt er ab. Der Steuerberater Matthias Weigel ist um die vorhandenen betrieblichen Unterlagen gebeten; eine externe Bewertung ist bisher nicht beauftragt."),
            "PAGEBREAK",
            ("4 Nachlass des Vaters", "Horst Bergmann, zuletzt Am Mühlenberg 7, 14547 Beelitz, verstarb am 12.02.2019. Mein Mandant ist Alleinerbe. Zu dem Erwerb gehörten das unbebaute Grundstück in der Gemarkung Wittbrietzen, Flur 3, Flurstück 118/7, mit 612 Quadratmetern sowie ein Kontoguthaben von 4.200,00 Euro. Der damalige Maklerwert des Grundstücks wurde mit 31.000,00 Euro angegeben. Außerdem bestanden ein Darlehen von 8.500,00 Euro und Bestattungskosten von 4.820,00 Euro. Mein Mandant besteht darauf, dass diese Erwerbsvorgänge und Belastungen jeweils berücksichtigt werden. Er behauptet nicht, der damalige Maklerwert sei zugleich ein aktuelles Verkehrswertgutachten."),
            ("5 Gold und Bitcoin", "Mein Mandant bestätigt den Kauf von vier Goldmünzen zu je 1.750,00 Euro im Jahr 2022, insgesamt 7.000,00 Euro. Im Juni 2026 hat er eine Münze für 3.120,00 Euro verkauft. Drei Münzen sind verblieben. Einen aktuellen Gesamtwert der drei Münzen teilt er mit diesem Schreiben nicht mit. Zur Bitcoin-Anlage verweist er bislang auf einen Verkauf im Juni 2026. Die Transaktionsaufstellung liegt mir noch nicht vor; einen vollständigen Abgang aller Bestände kann ich auf dieser Grundlage nicht bestätigen."),
            ("6 Zahlungen an Ursula Bergmann", "Die Mutter meines Mandanten, Ursula Bergmann, geboren am 30.11.1941, lebt in Werder. Mein Mandant unterstützt sie monatlich mit 380,00 Euro; außerdem ist ein Pflegedienst tätig. Eine Eigentumsübertragung oder andere Gegenleistung ist damit nach seiner Darstellung nicht verbunden. Herr Bergmann hält diese Unterstützung für eine gewöhnliche Hilfe innerhalb der Familie und sieht keinen Anlass, sie wegen der Trennung einzustellen. Das bei der Eheschließung noch mit 5.000,00 Euro bestehende Darlehen seiner Mutter wurde 2014 vollständig zurückgezahlt. Eine fortbestehende Darlehensschuld hieraus wird nicht geltend gemacht."),
            "Die Unterlagen Ihrer Mandantin erbitte ich ebenfalls stichtagsbezogen. Mein Mandant erwartet insbesondere, dass die wechselseitigen Angaben zum Haus und zur Finanzierung auf denselben Unterlagen beruhen. Eine Einigung über einzelne Werte oder eine Ausgleichszahlung liegt bisher nicht vor.",
        ], "Anselm Ritter\nRechtsanwalt", "Sehr geehrter Herr Kollege Dr. Feldkamp,",
        "Mit freundlichen kollegialen Grüßen",
    ),
    doc(
        "07_angaben_jonas_trennung_2025-05-06.docx", JONAS, MARA,
        "Potsdam, 06.05.2025", "Zu Deiner Bitte um Aufstellung nach unserem Auszugsgespräch",
        "Meine Vermögensangaben zur Trennung",
        [
            "Du hattest mich gebeten aufzuschreiben, was am 1. April bei mir vorhanden war. Ich habe die Sachen unten zusammengestellt. Die genauen Kontostände habe ich noch nicht aus den Auszügen herausgesucht. Deshalb schreibe ich hier auch keinen Gesamtbetrag hin, der hinterher wieder geändert werden müsste.",
            "Am Haus Kastanienweg 18 gehört mir wie Dir die Hälfte. Wir haben es 2014 für 326.000 Euro gekauft. Das Darlehen bei der Havelbogen Bank läuft auf uns beide. Die Unterlagen zu HD-2014-731 liegen im Hausordner. Was genau Anfang April noch offen war, will ich bei der Bank erfragen; aus der Grundschuld kann ich das nicht ablesen.",
            "Mein Planungsbüro Bergmann Licht & Planung betreibe ich seit 2007 allein. Dazu gehören die Arbeitsgeräte, die laufenden Aufträge und das Geschäftskonto. Es gibt noch offene Kundenrechnungen und laufende betriebliche Rechnungen. Matthias Weigel hat die Buchhaltung. Ich kann Dir im Moment nicht seriös aufschreiben, was jemand für das Büro bezahlen würde, wenn ich selbst nicht mehr dort arbeite.",
            "Von Papa habe ich das unbebaute Grundstück in Wittbrietzen geerbt, Flur 3, Flurstück 118/7, 612 Quadratmeter. Der Makler hatte es 2019 mit 31.000 Euro angesetzt. Ich habe es nicht verkauft. Papa ist am 12. Februar 2019 gestorben. Auch die Konto- und Darlehenssachen von damals muss ich aus dem Nachlassordner heraussuchen.",
            "Die vier Goldmünzen, die ich 2022 für zusammen 7.000 Euro gekauft habe, sind noch da. Außerdem habe ich am 20. Januar dieses Jahres 0,06 Bitcoin gekauft; dafür sind einschließlich Gebühren 5.100 Euro abgegangen. Einen Kurswert zum 1. April habe ich nicht notiert. Das ist privat und steht nicht in der Buchhaltung des Büros.",
            "Die privaten Kontoauszüge und den Stand des Geschäftskontos reiche ich nach. Mamas früheres Darlehen ist keine offene Rechnung mehr. Die bei unserer Hochzeit noch offenen 5.000 Euro habe ich ihr bis 2014 vollständig zurückgezahlt. Die monatlichen 380 Euro, die sie jetzt bekommt, sind Unterstützung im Alltag und keine Raten dafür.",
            "Meine Kleidung und die persönlichen Unterlagen sind in der Feuerbachstraße. Über Möbel und die Sachen der Kinder haben wir noch nicht alles besprochen. Ich möchte die Vermögensunterlagen und die Absprachen zu den Kindern getrennt halten.",
        ], "Jonas", "Hallo Mara,", "Viele Grüße", "Jonas Bergmann",
    ),
    doc(
        "08_haushaltserklaerung_mara_2026-08-28.docx", MARA, AN_FELDKAMP,
        "Potsdam, 28.08.2026", "Ihr Zeichen: 166/26 LF\nBetrifft: Trennung und Nutzung des Hauses Kastanienweg 18",
        "Erklärung zu unserem Haushalt seit der Trennung",
        [
            "Jonas ist am 01.04.2025 in die Feuerbachstraße 9 ausgezogen. Ich bin mit Jule und Oskar im Haus Kastanienweg 18 geblieben. Seine Kleidung, persönliche Papiere und Arbeitssachen hat er mitgenommen. Einiges aus dem Keller und Werkzeug blieb zunächst noch hier.",
            "Jonas kommt zum Abholen und Bringen der Kinder ans Haus. Gelegentlich hat er etwas repariert oder abgeholt. Wir kaufen nicht mehr als Paar ein und führen keinen gemeinsamen Essensplan. Unseren Tagesablauf stimmen wir wegen der Kinder ab. Einen Versuch, wieder als Ehepaar zusammenzuleben, hat es nicht gegeben.",
            "Beim Ostseeurlaub 2025 haben wir trotz der Trennung gemeinsam organisiert. Jonas ist nicht mitgereist; ich war mit Jule und Oskar dort. Die Restzahlung von 1.260 Euro ist laut Bestätigung des Ferienhofs am 10.06.2025 eingegangen. Mit der früheren Anzahlung kostete die Ferienwohnung 1.500 Euro. Wir wollten den Kindern die bereits besprochene Reise nicht nehmen. Jonas und ich sind über die Kosten und über den Zuschuss seiner Mutter aneinandergeraten. Ich hatte Omas Geld als Hilfe für die Kinder verstanden. Jonas meinte, es müsse bei unserer Abrechnung insgesamt abgezogen werden. Eine vollständige Abrechnung habe ich nicht mit ihm unterschrieben.",
            "Die Hausdarlehensverträge wurden nicht geändert; wir sind beide Vertragspartner der Bank geblieben. Eine Übertragung seines Eigentumsanteils auf mich haben wir nicht vereinbart. Auch über einen Hauswert besteht keine Einigung. Darlehenssalden möchte ich anhand der Auszüge zuordnen und nicht aus meiner Erinnerung nennen.",
            "Die Betten, Schreibtische und meisten Sachen der Kinder sind hier geblieben. Sie nehmen Taschen zu Jonas mit. Ich bestelle häufig zuerst, was für Schule und Freizeit benötigt wird; Jonas beteiligt sich aber auch. Wegen Jules Kinderlager 2026 für 420 Euro mussten wir mehrmals über Anmeldung und Zahlung schreiben.",
            "Ich habe weder Zugang zu Jonas' Bitcoin-Konto noch eine Übersicht über seine betrieblichen Konten. Meine Angaben dazu beruhen teilweise nur auf seinen Nachrichten, nicht auf eingesehenen Abrechnungen.",
        ], "Mara Bergmann", "Sehr geehrter Herr Dr. Feldkamp,", "Mit freundlichen Grüßen",
    ),
    doc(
        "09_telefonvermerk_2026-09-03.docx", FELDKAMP,
        "Handakte Mara Bergmann\n166/26 LF", "Potsdam, 03.09.2026",
        "Telefonat mit Frau Bergmann am 03.09.2026, 10:10 bis 10:27 Uhr",
        "Telefonvermerk zu den fehlenden Unterlagen",
        [
            "Frau Bergmann rief wegen des Schreibens von Rechtsanwalt Ritter vom 20.08.2026 an. Das Gespräch führte Dr. Lukas Feldkamp. Der Vermerk gibt ihre Angaben sinngemäß wieder; während des Telefonats wurden keine Kontoauszüge gemeinsam eingesehen.",
            "Zur Aufstellung aus dem Frühjahr 2025 sagte Frau Bergmann: Sie erinnere sich an eine Datei ihres Mannes, habe diese damals aber nicht als vollständige Auskunft verstanden. Die Kontostände hätten darin gefehlt. Ob ihr daneben einzelne Bilder von Auszügen per Messenger zugegangen seien, könne sie ohne Nachsehen nicht sicher sagen. Eine von beiden unterschriebene Vermögensliste habe es nicht gegeben.",
            "Die Formulierung ihres Mannes vom 30.06.2026, Bitcoin habe er abgestoßen, habe sie zunächst als vollständigen Verkauf verstanden. Sie habe keine Verkaufsabrechnung gesehen. Auf Nachfrage konnte sie weder eine verkaufte Menge noch einen verbliebenen Bestand aus eigener Kenntnis nennen. Sie werde keine eigene Zahl aus einem heutigen Kurs zurückrechnen.",
            "Zu den Goldmünzen erklärte sie, vom Kauf der vier Stück im Jahr 2022 zu wissen. Den Verkauf einer Münze im Juni 2026 habe Jonas ihr mitgeteilt. Sie habe die verbliebenen Münzen nicht selbst gezählt. Die Angabe von drei Stück im Schreiben Ritter widerspreche daher keiner eigenen aktuellen Bestandsaufnahme.",
            "Frau Bergmann sagte weiter, sie wolle die Unterstützung für Ursula nicht einstellen lassen. Sie störe sich daran, dass Jonas bei Ausgaben für die Kinder auf fehlendes Geld verweise, während die monatliche Überweisung an seine Mutter selbstverständlich weiterlaufe. Dass Ursula dafür ein Grundstück oder eine andere Gegenleistung zugesagt habe, sei ihr nicht bekannt.",
            "Zum Haus bat Frau Bergmann darum, die weitere Bankpost abzuwarten. Sie könne die im Grundbuch stehende Summe nicht als offenen Kredit bestätigen. Herr Sander sei als Ansprechpartner genannt. Frau Bergmann kündigte an, den Hausordner beim nächsten Kanzleitermin mitzubringen.",
        ], "Dr. Lukas Feldkamp\nRechtsanwalt", author="Dr. Lukas Feldkamp",
    ),
    doc(
        "10_grundbuch_textabschrift_2026-07-16.docx", FELDKAMP,
        "Handakte Mara Bergmann\n166/26 LF", "Potsdam, 16.07.2026",
        "Grundbuch von Bornim, Blatt 2841\nObjekt: Kastanienweg 18, 14476 Potsdam",
        "Unbeglaubigte Grundbuchabschrift Bornim Blatt 2841",
        [
            "Aus der von Frau Bergmann vorgelegten Grundbuchunterlage werden die nachstehenden Grundstücks-, Eigentums- und Belastungsangaben für die Handakte übertragen. Historische Zwischenvermerke und in Bezug genommene Bewilligungen werden nicht im Volltext wiedergegeben.",
            ("1 Bestandsverzeichnis", "Das Grundstück ist im Grundbuch von Bornim auf Blatt 2841 verzeichnet. Es liegt in der Gemarkung Bornim, Flur 6, Flurstück 218/11. Die Wirtschaftsart und Lage lauten Gebäude- und Freifläche, Kastanienweg 18, 14476 Potsdam. Die eingetragene Größe beträgt 486 Quadratmeter."),
            ("2 Abteilung 1 Eigentum", "Mara Bergmann, geborene Kreuter, geboren am 04.09.1980, und Jonas Bergmann, geboren am 17.02.1978, sind jeweils zu 1/2 als Eigentümer eingetragen. Die Eigentumsumschreibung aufgrund Auflassung vom 16.05.2014 wurde am 14.08.2014 eingetragen."),
            ("3 Abteilung 2 Lasten und Beschränkungen", "Es sind keine fortbestehenden Lasten oder Beschränkungen eingetragen."),
            ("4 Abteilung 3 Grundpfandrechte", "Eingetragen ist eine Grundschuld über 280.000,00 Euro zugunsten der Havelbogen Bank. Die Eintragung erfolgte am 19.06.2014 und betrifft das im Bestandsverzeichnis bezeichnete Grundstück. Ein Löschungsvermerk zu diesem Recht ist nicht eingetragen."),
            "Wiedergegeben ist der Grundschuldbetrag; ein Darlehenskontostand wird im Grundbuch nicht ausgewiesen. Die Textübertragung ist unbeglaubigt. Unterschriften oder Siegel des Grundbuchamts werden nicht wiedergegeben.",
        ], "Nora Albrecht\nRechtsanwaltsfachangestellte\nTextübertragung für die Handakte", author="Nora Albrecht",
    ),
    doc(
        "11_arbeitsbestaetigung_mara_2026-08-14.docx",
        "Land Brandenburg\nPersonalverwaltung\nPotsdam", MARA,
        "Potsdam, 14.08.2026", "Ihre Bitte um Bestätigung des Beschäftigungsstatus",
        "Bestätigung des Arbeitsverhältnisses",
        [
            "auf Ihren Wunsch bestätigen wir Ihnen, dass Sie, Frau Mara Bergmann, geborene Kreuter, geboren am 04.09.1980, als leitende Angestellte beim Land Brandenburg beschäftigt sind.",
            "Ihr Beschäftigungsverhältnis ist ein Arbeitsverhältnis. Sie werden als Tarifbeschäftigte in der Entgeltgruppe 14 geführt. Ein Beamtenverhältnis besteht nicht; Sie erhalten Arbeitsentgelt und keine Beamtenbesoldung.",
            "Diese Angaben treffen sowohl für den von Ihnen erfragten 08.07.2026 als auch für den heutigen Ausstellungszeitpunkt zu. Eine Beendigung Ihres Arbeitsverhältnisses ist in der Personalverwaltung nicht verzeichnet.",
            "Die Bestätigung wird Ihnen zur Vorlage bei Ihrem Rechtsanwalt erteilt. Einzelne monatliche Entgeltbestandteile und Auszahlungsbeträge werden hierin nicht bescheinigt. Diese ergeben sich aus den jeweiligen Entgeltabrechnungen. Auch über Kontoguthaben oder sonstiges privates Vermögen enthält diese Bescheinigung keine Angaben.",
            "Bei Rückfragen zu den bescheinigten Beschäftigungsdaten können Sie sich unter Beifügung dieses Schreibens an die Personalverwaltung wenden.",
        ], "gez. Friederike Sommer\nPersonalverwaltung", "Sehr geehrte Frau Bergmann,",
        "Mit freundlichen Grüßen", "Land Brandenburg",
    ),
    doc(
        "12_auskunft_ursula_bergmann_2026-09-07.docx",
        "Ursula Bergmann\nBrandenburger Straße 22\n14542 Werder (Havel)", AN_RITTER, "Werder, 07.09.2026",
        "Ihr Zeichen: 84/26 AR\nIhre Fragen zu meinen Zahlungen und zu Jonas' Unterstützung",
        "Auskunft zu den Geldangelegenheiten mit meinem Sohn",
        [
            "Jonas hat mir Ihre Fragen weitergegeben. Ich heiße Ursula Bergmann, bin am 30.11.1941 geboren und lebe in Werder. Ich möchte erklären, was das Geld von früher und die jetzigen Zahlungen angeht, weil das in unseren Gesprächen offenbar durcheinandergeraten ist.",
            "Bei Jonas' Hochzeit am 18.06.2011 waren aus meinem früheren Darlehen noch 5.000 Euro offen. Das war Geld, das er mir zurückgeben sollte. Er hat das Darlehen bis 2014 vollständig zurückgezahlt. Aus diesem Darlehen fordere ich heute nichts mehr von ihm. Die jetzigen monatlichen Zahlungen haben damit nichts zu tun. Zu den einzelnen Rückzahlungen habe ich Jonas bereits am 9. August geschrieben, nachdem ich die alte Mappe gefunden hatte.",
            "Jonas unterstützt mich monatlich mit 380 Euro. Ich brauche das Geld für meine laufenden Ausgaben. Bei mir kommt auch ein Pflegedienst. Die Überweisung ist nicht der Kaufpreis für irgendetwas und keine Rate für ein Haus oder Grundstück. Ich habe Jonas im Zusammenhang damit kein Eigentum übertragen und ihm auch keine solche Übertragung zugesagt. Er soll mir das Geld nicht später wieder abnehmen können, und ich muss es ihm nicht zurückzahlen.",
            "Für den Ostseeurlaub 2025 habe ich etwas dazugegeben. Das war für Jule und Oskar gedacht, damit wegen des Geldes nicht die ganze Reise ausfällt. Ich wollte daraus weder ein Darlehen an Mara machen noch eine Abrechnung zwischen ihr und Jonas festlegen. Wie die beiden die Reisekosten untereinander aufteilen, habe ich nicht mit ihnen vereinbart. Ich habe ihnen dazu auch keine unterschriebene Aufstellung gegeben.",
            "Die Unterlagen über den Nachlass von Horst verwahre ich nicht für Jonas. Horst und ich waren seit 2006 geschieden; Jonas ist unser einziges Kind. Horst wohnte zuletzt Am Mühlenberg 7 in Beelitz und ist am 12.02.2019 gestorben. Jonas hat die Angelegenheiten als Alleinerbe selbst erledigt. Was der Makler damals zum Grundstück geschrieben hat und welche Belege Jonas aufgehoben hat, kann ich Ihnen nicht aus eigener Durchsicht bestätigen.",
            "Bitte verwenden Sie dieses Schreiben für die Beantwortung Ihrer Fragen. Bei den Bankunterlagen muss Jonas selbst nachsehen; ich möchte keine Beträge aus dem Gedächtnis ergänzen, bei denen ich nicht sicher bin.",
        ], "Ursula Bergmann", "Sehr geehrter Herr Ritter,", "Mit freundlichen Grüßen",
    ),
    doc(
        "13_erbschein_archivabschrift_2019-03-07.docx",
        "Amtsgericht Potsdam\nNachlassgericht", "Nachlass Horst Bergmann",
        "Potsdam, 07.03.2019", "Aktenzeichen: 52 VI 184/19",
        "Erbschein über den Nachlass des Horst Bergmann",
        [
            "Textliche Archivabschrift des Erbscheins vom 07.03.2019. Wiedergegeben wird der Erbscheinsinhalt einschließlich der Bezeichnung des Erblassers und des Erben.",
            "Es wird bezeugt, dass Horst Bergmann, verstorben am 12.02.2019, mit letztem gewöhnlichem Aufenthalt Am Mühlenberg 7, 14547 Beelitz, von seinem Sohn Jonas Bergmann, geboren am 17.02.1978, allein beerbt worden ist.",
            "Jonas Bergmann ist Alleinerbe des Erblassers.",
            "Die Archivabschrift gibt den Text der Urkunde wieder. Ein Beglaubigungsvermerk ist nicht Bestandteil dieser Abschrift.",
        ], "gez. Katrin Voss\nRechtspflegerin", author="Amtsgericht Potsdam",
    ),
    doc(
        "14_grundbuch_wittbrietzen_textabschrift_2026-08-24.docx", RITTER,
        "Handakte Jonas Bergmann\n84/26 AR", "Potsdam, 24.08.2026",
        "Grundbuch von Wittbrietzen, Blatt 1278\nNachlass Horst Bergmann",
        "Unbeglaubigte Grundbuchabschrift Wittbrietzen Blatt 1278",
        [
            "Für die Grundstücksunterlagen meines Mandanten werden die nachstehenden Bestands-, Eigentums- und Grundpfandrechtsangaben in Textform wiedergegeben. Die Abschrift beschränkt sich auf diese Eintragungen und den Löschungsvermerk; sie ist keine vollständige Wiedergabe sämtlicher historischer Vermerke des Blattes.",
            ("1 Bestandsverzeichnis", "Das unbebaute Grundstück ist im Grundbuch von Wittbrietzen auf Blatt 1278 verzeichnet. Es liegt in der Gemarkung Wittbrietzen, Flur 3, Flurstück 118/7. Die eingetragene Größe beträgt 612 Quadratmeter."),
            ("2 Abteilung 1 Eigentum", "Jonas Bergmann, geboren am 17.02.1978, ist als Alleineigentümer eingetragen. Die Eigentumsberichtigung erfolgte am 30.04.2019 aufgrund Erbfolge nach Horst Bergmann, verstorben am 12.02.2019. Als Nachweis ist der Erbschein des Amtsgerichts Potsdam vom 07.03.2019, Aktenzeichen 52 VI 184/19, bezeichnet."),
            ("3 Abteilung 3 Grundpfandrecht und Löschung", "Für die Havelbogen Bank war eine Grundschuld über 8.500,00 Euro eingetragen. Zu diesem Recht ist die Löschung am 20.05.2019 vermerkt. Die Grundschuld wird damit als gelöschte Eintragung wiedergegeben."),
            "Die vorstehende Textübertragung enthält keine Wertangabe zum Grundstück. Sie wurde für die Handakte angefertigt und ist unbeglaubigt. Originalunterschriften und Siegel des Grundbuchamts werden nicht wiedergegeben.",
        ], "Anselm Ritter\nRechtsanwalt\nTextübertragung für die Handakte", author="Anselm Ritter",
    ),
]


def mail(name, sender, recipient, date, subject, body, attachments=(), reply=None, cc=None):
    return dict(name=name, sender=sender, recipient=recipient, date=date,
                subject=subject, body=body, attachments=attachments, reply=reply, cc=cc)


MB = "Mara Bergmann <mara@bergmann-potsdam.de>"
JB = "Jonas Bergmann <jonas@bergmann-licht-planung.de>"
LF = "Dr. Lukas Feldkamp <kanzlei@feldkamp-recht.de>"
AR = "Anselm Ritter <kanzlei@ritter-potsdam.de>"
UB = "Ursula Bergmann <ursula@bergmann-werder.de>"

EMAILS = [
    mail("01_2025-05-08_jonas_aufstellung.eml", JB, MB, "2025-05-08T20:43:00+02:00",
         "Meine Aufstellung vom Dienstag",
         """Hallo Mara,

anbei das Schreiben, das ich am Dienstag fertiggemacht habe. Das ist mein Stand zum 1. April. Bei den Konten fehlen noch die genauen Auszüge. Ich will da keine Zahl aus der Banking-App hinschreiben, die inzwischen schon wieder anders ist.

Den Hausordner brauche ich dafür auch noch einmal. Lass ihn bitte nicht bei den Schulsachen verschwinden, ich habe ihn beim letzten Mal nicht gefunden. Für das Büro frage ich Matthias.

Bei Wittbrietzen habe ich die alte Zahl vom Makler übernommen. Das Grundstück ist noch meins; eine neue Schätzung habe ich für diese Aufstellung nicht eingeholt. Die Unterlagen zu Papas Konto und dem damaligen Darlehen muss ich extra aus dem Nachlassordner holen. Bitte halte die Zahl im Schreiben deshalb nicht für den Betrag, den ich heute beim Verkauf bekommen würde.

Jonas""", attachments=("07_angaben_jonas_trennung_2025-05-06.docx",)),
    mail("02_2025-07-04_mara_ostsee.eml", MB, JB, "2025-07-04T07:52:00+02:00",
         "Ostsee / Unterkunft",
         """Hallo Jonas,

die Restzahlung für die Unterkunft waren 1.260 Euro. Der Ferienhof hat den Eingang am 10. Juni bestätigt; die Anzahlung aus Februar kommt noch dazu. Bitte rechne nicht einfach den Zuschuss Deiner Mutter von meinem Anteil ab. Sie hat am Telefon gesagt, sie will den Kindern etwas zur Reise geben. Ich weiß nicht, was Du mit ihr zusätzlich besprochen hast.

Mir wäre lieber, wir schreiben einmal ordentlich auf, was schon bezahlt ist und was noch offen ist. Ich möchte nicht beim Einkaufen wieder darüber diskutieren. Den Kindern haben wir gesagt, dass die Reise stattfindet, und dabei soll es bleiben.

Jules Regenjacke liegt übrigens noch bei Dir. Bitte am Sonntag mitbringen.

Mara"""),
    mail("03_2025-07-05_jonas_ostsee.eml", JB, MB, "2025-07-05T09:14:00+02:00",
         "Re: Ostsee / Unterkunft",
         """Hallo Mara,

ich wollte Dir nichts wegnehmen. Für mich war Omas Geld ein Zuschuss zur Reise insgesamt. Wenn sie die Kinder unterstützen will, fällt die Unterkunft doch trotzdem für uns beide an. Ich habe nicht mit ihr vereinbart, dass Du dadurch weniger oder mehr zahlen musst.

Die 1.260 Euro Restzahlung stelle ich nicht infrage. Lass uns nur nicht Getränke, Essen unterwegs und alles andere jetzt schon in einen Topf werfen. Ich suche die Buchungsbestätigung heraus. Eine fertige Endabrechnung haben wir bisher beide nicht. Dass ich nicht mitfahre, war ja seit Mai geklärt.

Die Jacke bringe ich. Oskar hat bei mir erzählt, wir ziehen nach dem Urlaub wieder zusammen. Bitte sag ihm auch noch einmal, dass der Urlaub daran nichts ändert.

Jonas""", reply="02_2025-07-04_mara_ostsee.eml"),
    mail("04_2026-06-30_jonas_gold_bitcoin.eml", JB, MB, "2026-06-30T21:06:00+02:00",
         "Wegen Deiner Frage zum Geld",
         """Hallo Mara,

Bitcoin habe ich abgestoßen. Eine der Goldmünzen habe ich diesen Monat auch verkauft, dafür gab es 3.120 Euro. Ich möchte das Thema nicht beim Abholen vor den Kindern besprechen.

Von den vier Münzen sind die anderen drei noch bei mir. Das Geld für die verkaufte Münze ist auf mein Privatkonto gegangen, nicht aufs Geschäftskonto. Was ein Händler für die übrigen drei zahlen würde, habe ich noch nicht angefragt. Den Kaufbeleg von 2022 suche ich zusammen mit der Verkaufsabrechnung heraus.

Die Belege liegen nicht alle im Hausordner. Das meiste kommt online und ich muss es erst herunterladen. Matthias macht die Buchhaltung vom Büro, der hat nicht automatisch jede private Abrechnung von mir.

Ich habe Dir letztes Jahr schon aufgeschrieben, was da war. Dass jetzt wieder alles bei null anfängt, nervt mich, aber ich schicke meinem Anwalt die Unterlagen, die er angefordert hat.

Jonas"""),
    mail("05_2026-07-09_jonas_zustellung.eml", JB, AR, "2026-07-09T08:31:00+02:00",
         "84/26 AR / Post vom Amtsgericht",
         """Sehr geehrter Herr Ritter,

gestern, am 8. Juli, ist mir der Scheidungsantrag zugestellt worden. Auf dem Antrag steht der 22. Juni, das Gericht führt ihn unter 41 F 218/26. Bitte führen Sie die Sache für mich weiter.

Die Trennung am 1. April 2025 und meine jetzige Anschrift stimmen. Wegen des Hauses möchte ich nichts vorschnell unterschreiben. Mara und die Kinder wohnen dort, aber meine Hälfte ist damit doch nicht einfach weg. Ich suche heute Abend die Bankpost zusammen.

Meine Aufstellung aus dem letzten Frühjahr finde ich vermutlich noch im Ordner mit den gesendeten Mails. Ich erinnere mich sicher an das Schreiben, aber nicht mehr daran, welche Kontoauszüge ich damals schon mitgeschickt hatte.

Mit freundlichen Grüßen
Jonas Bergmann"""),
    mail("06_2026-07-21_feldkamp_abschrift.eml", LF, MB, "2026-07-21T11:42:00+02:00",
         "166/26 LF / Abschrift meines Schreibens an Herrn Ritter",
         """Sehr geehrte Frau Bergmann,

anbei erhalten Sie die Abschrift meines gestrigen Schreibens an Herrn Rechtsanwalt Ritter. Darin habe ich die Auskünfte und Belege bis zum 20. August angefordert.

Bitte sehen Sie in Ihrem Postfach nach der Nachricht Ihres Mannes aus Mai 2025. Mir hilft die Nachricht mit der damals beigefügten Datei mehr als ein neuer Ausdruck ohne Datum. Bei den Bankunterlagen nehmen Sie bitte auch Schreiben mit, die Ihnen unbedeutend vorkommen. Wir können sie hier zusammen dem richtigen Darlehenskonto zuordnen.

Den Termin zur Übergabe des Hausordners stimmen Sie bitte kurz mit Frau Albrecht ab. Über eine zusätzliche Beauftragung zur Hausverwertung sprechen wir gesondert; sie ist mit diesem Auskunftsschreiben nicht verbunden.

Mit freundlichen Grüßen
Dr. Lukas Feldkamp
Rechtsanwalt
Charlottenstraße 61, 14467 Potsdam""", attachments=("05_auskunftsverlangen_feldkamp_2026-07-20.docx",)),
    mail("07_2026-07-27_bank_sander.eml",
         "Eike Sander <eike.sander@havelbogen-bank.de>", MB,
         "2026-07-27T14:18:00+02:00", "Darlehenskonto HD-2014-731 / Ihre Anfrage",
         """Sehr geehrte Frau Bergmann,

ich habe Ihre Anfrage zu den Darlehensunterlagen aufgenommen. Bei dem Darlehenskonto HD-2014-731 werden Sie und Herr Jonas Bergmann als Darlehensnehmer geführt. Die angefragten Bestätigungen sollen sich auf den 1. April 2025 und den 8. Juli 2026 beziehen; bitte melden Sie sich, falls Sie zusätzlich einen anderen Zeitpunkt benötigen.

Den jeweiligen Darlehenssaldo müssen wir aus dem Konto bestätigen. Der Grundschuldbetrag aus Ihrer Grundbuchunterlage ist nicht die Kontostandsangabe. Ich möchte Ihnen deshalb am Telefon keinen Betrag nennen, bevor die stichtagsbezogenen Unterlagen vorliegen.

Für die direkte Übersendung an Herrn Dr. Feldkamp benötige ich seine Vollmacht. Sie können die Unterlagen alternativ selbst entgegennehmen. Eine Änderung der Darlehensnehmer ist mit der angeforderten Auskunft nicht verbunden.

Mit freundlichen Grüßen
Eike Sander
Havelbogen Bank
Kundenbetreuung Baufinanzierung"""),
    mail("08_2026-08-03_weigel_betriebsunterlagen.eml",
         "Matthias Weigel <kanzlei@stb-weigel.de>", JB,
         "2026-08-03T16:09:00+02:00", "Bergmann Licht & Planung / Unterlagen für Ihren Anwalt",
         """Guten Tag Herr Bergmann,

die Anfrage Ihres Anwalts betrifft teilweise Unterlagen, die nicht aus der laufenden Buchhaltung hervorgehen. Ich stelle die vorhandenen betrieblichen Auswertungen und Anlagenverzeichnisse zusammen. Für einen Stand mitten im Jahr brauche ich von Ihnen zusätzlich die noch nicht eingereichten Rechnungen und Angaben dazu, welche Kundenforderungen am 8. Juli offen waren.

Bitte schicken Sie mir keine bloße Umsatzliste mit dem Vermerk, das sei der Wert des Büros. Einen Verkaufspreis des Unternehmens habe ich für Sie bisher nicht ermittelt. Auch eine rückwirkende Bestandsaufnahme der privaten Konten ist nicht Teil der laufenden Buchführung.

Die Goldmünzen und die Bitcoin-Anlage haben Sie mir als privat bezeichnet. Die entsprechenden Handelsabrechnungen liegen mir nicht vollständig vor. Laden Sie diese bitte selbst aus dem jeweiligen Zugang herunter und geben Sie sie an Herrn Ritter weiter. Ich kann nicht bestätigen, ob ein Restbestand vorhanden ist.

Viele Grüße
Matthias Weigel
Steuerberater"""),
    mail("09_2026-08-21_ritter_rueckfrage.eml", AR, JB, "2026-08-21T09:37:00+02:00",
         "84/26 AR / Meine Antwort und noch fehlende Angaben",
         """Sehr geehrter Herr Bergmann,

anbei meine gestrige Antwort an Herrn Dr. Feldkamp. Bitte lesen Sie insbesondere die Angaben zu den Goldmünzen und zum Nachlass Ihres Vaters noch einmal durch. Ich habe Ihre Einwände zum Betrieb aufgenommen, aber damit liegt noch keine Bewertung vor.

Zur Bitcoin-Anlage reicht mir Ihre Formulierung aus der Nachricht an Frau Bergmann nicht aus. Bitte übersenden Sie die Transaktionsliste einschließlich Käufen, Verkäufen und angezeigtem Restbestand. Ich benötige die Abrechnungen und nicht nur die Mitteilung, dass ein Verkauf stattgefunden hat.

Wegen des früheren Darlehens Ihrer Mutter habe ich festgehalten, dass es 2014 zurückgezahlt wurde. Fragen Sie Ihre Mutter bitte, ob sie mir das und den Anlass der laufenden Unterstützung kurz in eigenen Worten bestätigen kann. Ich habe um Ergänzungsfrist bis zum 15. September gebeten; eine Zustimmung der Gegenseite liegt mir darauf noch nicht vor.

Mit freundlichen Grüßen
Anselm Ritter
Rechtsanwalt
Zeppelinstraße 42, 14471 Potsdam""", attachments=("06_antwort_ritter_2026-08-20.docx",)),
    mail("10_2026-08-26_mara_fruehere_auskunft.eml", MB, LF,
         "2026-08-26T20:54:00+02:00", "166/26 LF / Die alte Aufstellung habe ich gefunden",
         """Sehr geehrter Herr Dr. Feldkamp,

ich habe die Mail vom 8. Mai 2025 mit Jonas' Schreiben vom 6. Mai wiedergefunden. Er hatte also etwas geschickt, das stimmt. Ich hatte bei unserem ersten Gespräch zu pauschal gesagt, ich hätte keine Auskunft bekommen. Was ich meinte: Kontostände und die versprochenen Unterlagen waren nicht vollständig dabei.

Ich weiß noch, dass wir später einzelne Bilder über das Handy geschickt haben. Ob das genau die Auszüge zu dem verlangten Tag waren, kann ich ohne Nachsehen nicht sagen. Bitte schreiben Sie nicht, ich hätte nie irgendeine Datei bekommen.

Beim Grundstück in Wittbrietzen kenne ich nur die alte Zahl aus der Familie. Ich habe weder einen neuen Makler beauftragt noch das Grundstück selbst vermessen. Ich möchte nicht, dass eine Vermutung von mir nachher als Bewertung in einem Brief steht.

Die Erklärung zum Haushalt bringe ich unterschrieben vorbei. Am Freitag kann ich nach der Arbeit in die Kanzlei kommen.

Mit freundlichen Grüßen
Mara Bergmann""", attachments=("07_angaben_jonas_trennung_2025-05-06.docx",)),
    mail("11_2026-09-08_ursula_schreiben.eml", UB, JB, "2026-09-08T10:22:00+02:00",
         "Brief für Herrn Ritter",
         """Hallo Jonas,

hier ist der Brief von gestern. Frau Neumann hat mir geholfen, ihn am Rechner abzutippen. Lies ihn bitte durch und gib ihn Herrn Ritter so weiter. Die 5.000 Euro von damals sind zurückgezahlt, das soll jetzt nicht wieder als offene Sache auftauchen.

Mit den 380 Euro hilfst Du mir im Monat. Das ist keine Abzahlung und ich habe Dir dafür auch kein Haus versprochen. Mir wäre lieb, wenn das einmal klar ist. Ich will nicht, dass Mara denkt, wir hätten da etwas untereinander geregelt, von dem sie nichts wissen darf.

Wegen der Ostsee habe ich geschrieben, wofür mein Zuschuss gedacht war. Was Ihr zwei am Ende miteinander abrechnen wolltet, weiß ich nicht. Bitte lass die Kinder aus dem Streit darüber heraus.

Liebe Grüße
Mama""", attachments=("12_auskunft_ursula_bergmann_2026-09-07.docx",)),
    mail("12_2026-09-14_mara_sachstand.eml", MB, LF, "2026-09-14T18:46:00+02:00",
         "166/26 LF / Unterlagen für morgen",
         """Sehr geehrter Herr Dr. Feldkamp,

ich bringe den Hausordner morgen wie besprochen zu Frau Albrecht. Ich habe die Seiten nicht neu sortiert, weil ich sonst die Schreiben und die dazugehörigen Auszüge durcheinanderbringe. Die Bestätigung meiner Personalstelle lege ich ebenfalls bei. Dort steht ausdrücklich Angestellte und Entgeltgruppe 14; ich bin keine Beamtin.

Zu Jonas' Bitcoin habe ich nach wie vor nur seine Mail vom Juni und das, was in Herrn Ritters Brief steht. Eine vollständige Handelsübersicht habe ich selbst nicht erhalten. Bei seiner Mutter geht es mir nicht darum, dass sie ohne Hilfe bleiben soll. Mich ärgert, dass wir wegen 420 Euro fürs Kinderlager tagelang schreiben und andere Zahlungen nicht besprechen können.

Gibt es inzwischen eine Antwort auf die noch fehlenden Unterlagen? Ich möchte das Haus nicht unter Zeitdruck verkaufen, bevor überhaupt klar ist, wovon wir ausgehen. Eine Einigung oder irgendeinen Verzicht habe ich Jonas nicht zugesagt.

Mit freundlichen Grüßen
Mara Bergmann"""),
]

CHATS = {
    "13_chat_auszug_trennung_2025-04.txt": """Chat zwischen Mara Bergmann und Jonas Bergmann
Auszug aus dem auf Maras Telefon gespeicherten Verlauf

01.04.2025, 08:12 - Jonas: Ich fahre nachher die letzten Taschen in die Feuerbachstraße. Die Kinder hole ich heute nicht ab, richtig?
01.04.2025, 08:18 - Mara: Richtig. Ich bin nach der Arbeit da. Jule weiß Bescheid, Oskar fragt noch dauernd, wo Du heute schläfst.
01.04.2025, 08:23 - Jonas: In der Wohnung. Sag ihm bitte nicht nur, dass ich arbeiten bin.
01.04.2025, 08:26 - Mara: Mache ich nicht. Wir hatten gesagt, wir erklären es beide noch mal ruhig.
01.04.2025, 17:44 - Jonas: Bin mit den Taschen durch. Im Keller ist noch mein Werkzeugkoffer. Den nehme ich am Wochenende.
01.04.2025, 17:52 - Mara: Bitte sag vorher Bescheid, bevor Du kommst. Ich will nicht, dass wir uns hier dauernd überraschen.
01.04.2025, 18:03 - Jonas: Ja. Den Hausordner lass bitte oben im Schrank. Ich brauche Kopien für die Bank.
02.04.2025, 07:31 - Mara: Kannst Du am Freitag beide von der Schule bzw. Betreuung holen? Ich komme nicht früher weg.
02.04.2025, 07:40 - Jonas: Geht. Schlafsachen bitte mitgeben. Für Oskar fehlt mir noch seine blaue Decke.
02.04.2025, 07:42 - Mara: Packe ich ein. Über das Haus müssen wir extra sprechen, nicht Freitag an der Tür.
03.04.2025, 19:10 - Jonas: Ich habe keine Unterlagen aus Deinem Schreibtisch mitgenommen. Nur meine Papiere und die Sachen fürs Büro.
03.04.2025, 19:18 - Mara: Gut. Dann suche ich den Versicherungsordner noch mal im Keller.
""",
    "14_chat_auszug_ostsee_2025-07.txt": """Chat zwischen Mara Bergmann und Jonas Bergmann
Auszug aus dem auf Maras Telefon gespeicherten Verlauf

02.07.2025, 19:08 - Mara: Für die Unterkunft an der Ostsee waren zuletzt 1.260 Euro fällig. Ich will vor der Reise klären, was wir davon jeweils übernehmen.
02.07.2025, 19:16 - Jonas: Mama hat doch auch was dazugegeben. Das müssen wir mit aufschreiben.
02.07.2025, 19:21 - Mara: Ja, aber sie hat zu mir gesagt für Jule und Oskar. Nicht als Ersatz für Deine Beteiligung.
02.07.2025, 19:28 - Jonas: Das habe ich nicht gesagt. Für mich verringert es die Reisekosten insgesamt.
02.07.2025, 19:30 - Mara: Dann bitte einmal per Mail, ich bin gerade noch beim Abendessen.
05.07.2025, 12:04 - Mara: Deine Mail ist angekommen. Eine komplette Abrechnung haben wir wirklich noch nicht. Das können wir nach der Reise machen, wenn die Belege da sind.
05.07.2025, 12:10 - Jonas: Einverstanden. Aber dann nicht jede Kleinigkeit ohne Beleg dazurechnen.
05.07.2025, 12:18 - Mara: Ich will keine Kassenprüfung. Ich will nicht wieder alles allein zusammenhalten müssen.
07.07.2025, 18:34 - Jonas: Oskar hat noch mal wegen Zusammenwohnen gefragt. Ich habe ihm gesagt, dass die Wohnung bleibt, auch wenn wir den Urlaub zusammen organisieren.
07.07.2025, 18:41 - Mara: Danke. Ich sage ihm dasselbe. Bitte keine Diskussion über Geld vor den beiden.
08.07.2025, 07:50 - Mara: Hast Du Jules Regenjacke jetzt eingepackt?
08.07.2025, 07:56 - Jonas: Ja, liegt oben auf ihrer Tasche.
""",
    "15_chat_auszug_kinderlager_2026-05.txt": """Chat zwischen Mara Bergmann und Jonas Bergmann
Auszug aus dem auf Maras Telefon gespeicherten Verlauf

04.05.2026, 17:06 - Mara: Jules Kinderlager kostet 420 Euro. Kannst Du heute bitte sagen, ob Du Dich beteiligst? Ich muss die Anmeldung abschicken.
04.05.2026, 17:29 - Jonas: Ja, ich beteilige mich. Ich brauche nur den genauen Zahlungstermin, bevor ich etwas zusage, was diese Woche nicht geht.
04.05.2026, 17:32 - Mara: Der Termin steht auf der Anmeldung. Ich schicke sie Dir nachher, bin noch unterwegs.
04.05.2026, 17:37 - Jonas: Danke. Bitte nicht einfach buchen und mir dann am selben Tag schreiben, dass alles sofort raus muss.
04.05.2026, 18:04 - Mara: Ich hatte es letzte Woche schon angesprochen. Es ist mühsam, jedes Mal hinterherzufragen.
05.05.2026, 08:11 - Jonas: Ich hatte letzte Woche den Betrag nicht mehr im Kopf. 420 habe ich jetzt verstanden.
05.05.2026, 08:15 - Mara: Für Deine Mutter gehen jeden Monat 380 automatisch raus. Bei den Kindern wird erst lange diskutiert.
05.05.2026, 08:23 - Jonas: Mama braucht die Hilfe. Das ist kein Gegenargument zum Lager. Bitte vermisch das nicht.
05.05.2026, 08:31 - Mara: Ich will ihr nichts wegnehmen. Ich brauche eine klare Antwort, damit ich planen kann.
06.05.2026, 10:08 - Jonas: Schick mir die Kontoverbindung aus der Anmeldung noch mal lesbar. Auf dem Bild fehlt unten ein Stück.
06.05.2026, 10:19 - Mara: Mache ich zu Hause. Ich schreibe Dir auch dazu, was ich schon erledigt habe, damit wir nichts doppelt zahlen.
""",
}


def set_font(style, size, bold=False):
    style.font.name = "Times New Roman"
    style.font.size = Pt(size)
    style.font.bold = bold
    style.font.color.rgb = RGBColor(0, 0, 0)
    fonts = style.element.get_or_add_rPr().get_or_add_rFonts()
    for attribute in list(fonts.attrib):
        if "theme" in attribute.lower():
            del fonts.attrib[attribute]
    for attribute in ("ascii", "hAnsi", "eastAsia", "cs"):
        fonts.set(qn(f"w:{attribute}"), "Times New Roman")
    for element in style.element.xpath(".//w:pBdr | .//w:rPr/w:spacing | .//w:rPr/w:kern"):
        element.getparent().remove(element)


def stable_docx(document):
    """Fixierte Metadaten und ZIP-Zeitstempel machen den Bau byteidentisch."""
    raw = io.BytesIO()
    document.save(raw)
    out = io.BytesIO()
    with ZipFile(raw) as source, ZipFile(out, "w", ZIP_DEFLATED) as target:
        for name in sorted(source.namelist()):
            info = ZipInfo(name, (2026, 9, 15, 12, 0, 0))
            info.compress_type = ZIP_DEFLATED
            target.writestr(info, source.read(name))
    return out.getvalue()


def build_docx(spec):
    document = Document()
    section = document.sections[0]
    section.page_width = Cm(21)
    section.page_height = Cm(29.7)
    section.top_margin = Inches(0.70)
    section.bottom_margin = Inches(0.70)
    section.left_margin = Inches(0.94)
    section.right_margin = Inches(0.90)
    section.header_distance = Inches(0.28)
    section.footer_distance = Inches(0.30)
    for name in ("Normal", "Title", "Heading 1", "Header", "Footer"):
        set_font(document.styles[name], 11, name in ("Title", "Heading 1"))
    normal = document.styles["Normal"].paragraph_format
    normal.line_spacing = 1.10
    normal.space_after = Pt(7)
    normal.widow_control = True
    title = document.styles["Title"].paragraph_format
    title.space_before = Pt(9)
    title.space_after = Pt(11)
    title.keep_with_next = True
    heading = document.styles["Heading 1"].paragraph_format
    heading.space_before = Pt(7)
    heading.space_after = Pt(11)
    heading.keep_with_next = True

    cp = document.core_properties
    cp.title = spec["title"]
    cp.subject = spec["reference"].replace("\n", " · ")
    cp.author = spec["author"]
    cp.last_modified_by = spec["author"]
    cp.comments = ""
    cp.keywords = ""
    cp.created = STAMP
    cp.modified = STAMP
    cp.revision = 1
    settings = document.settings.element
    lang = document.styles["Normal"].element.get_or_add_rPr()
    language = OxmlElement("w:lang")
    language.set(qn("w:val"), "de-DE")
    lang.append(language)
    compat = settings.find(qn("w:compat"))
    if compat is not None:
        settings.remove(compat)

    paragraph = document.add_paragraph(spec["sender"])
    paragraph.paragraph_format.space_after = Pt(17)
    paragraph.runs[0].bold = True
    paragraph = document.add_paragraph(spec["recipient"])
    paragraph.paragraph_format.space_after = Pt(9)
    paragraph = document.add_paragraph(spec["date"])
    paragraph.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    document.add_paragraph(spec["reference"])
    document.add_paragraph(spec["title"], "Title")
    if spec["salutation"]:
        document.add_paragraph(spec["salutation"])
    for block in spec["paragraphs"]:
        if block == "PAGEBREAK":
            document.add_page_break()
        elif isinstance(block, tuple):
            document.add_paragraph(block[0], "Heading 1")
            document.add_paragraph(block[1])
        else:
            document.add_paragraph(block)
    if spec["closing"]:
        paragraph = document.add_paragraph(spec["closing"])
        paragraph.paragraph_format.keep_with_next = True
        paragraph.paragraph_format.space_after = Pt(12)
    paragraph = document.add_paragraph(spec["signatory"])
    paragraph.paragraph_format.keep_together = True
    paragraph.paragraph_format.space_before = Pt(8)

    footer = section.footer.paragraphs[0]
    footer.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    footer.add_run("Seite ")
    field = OxmlElement("w:fldSimple")
    field.set(qn("w:instr"), "PAGE")
    footer._p.append(field)
    return stable_docx(document)


def message_id(name):
    sender = next(spec["sender"] for spec in EMAILS if spec["name"] == name)
    domain = parseaddr(sender)[1].rsplit("@", 1)[1]
    return f"<{Path(name).stem}@{domain}>"


def build_email(spec, docx):
    message = EmailMessage(policy=policy.SMTP)
    message["From"] = spec["sender"]
    message["To"] = spec["recipient"]
    if spec["cc"]:
        message["Cc"] = spec["cc"]
    message["Date"] = format_datetime(datetime.fromisoformat(spec["date"]))
    message["Message-ID"] = message_id(spec["name"])
    message["Subject"] = spec["subject"]
    if spec["reply"]:
        message["In-Reply-To"] = message_id(spec["reply"])
        message["References"] = message_id(spec["reply"])
    message.set_content(spec["body"].strip() + "\n", charset="utf-8", cte="quoted-printable")
    for name in spec["attachments"]:
        message.add_attachment(docx[name], maintype="application", subtype=DOCX_MIME,
                               filename=name)
    if spec["attachments"]:
        digest = hashlib.sha256(spec["name"].encode()).hexdigest()[:24]
        message.set_boundary(f"=_Bergmann_{digest}")
    return message.as_bytes()


def expected_files():
    docs = {spec["name"]: build_docx(spec) for spec in DOCUMENTS}
    outputs = {AKTEN / name: data for name, data in docs.items()}
    outputs.update({MAILS / spec["name"]: build_email(spec, docs) for spec in EMAILS})
    outputs.update({MAILS / name: text.encode("utf-8") for name, text in CHATS.items()})
    return outputs


def validate(outputs):
    assert len(DOCUMENTS) == 14 and len(EMAILS) == 12 and len(CHATS) == 3
    assert len(outputs) == 29
    words = {}
    for spec in DOCUMENTS:
        path = AKTEN / spec["name"]
        data = outputs[path]
        document = Document(io.BytesIO(data))
        text = "\n".join(p.text for p in document.paragraphs)
        assert spec["title"] in text and spec["date"] in text
        assert spec["signatory"] in text
        assert "§" not in text
        for forbidden in ("Musterantwort", "Lösungsskizze", "KI generiert", "ChatGPT", "Codex"):
            assert forbidden not in text, (path, forbidden)
        assert "Times New Roman" == document.styles["Normal"].font.name
        assert document.styles["Normal"].font.size == Pt(11)
        for section in document.sections:
            assert abs(section.page_width.cm - 21) < 0.01
            assert abs(section.page_height.cm - 29.7) < 0.01
        for name in ("Normal", "Title", "Heading 1"):
            style = document.styles[name]
            assert not style.element.xpath(".//w:pBdr")
            assert not any("theme" in attribute.lower()
                           for fonts in style.element.xpath(".//w:rFonts")
                           for attribute in fonts.attrib)
        words[path.name] = len(text.split())
    for spec in EMAILS:
        parsed = BytesParser(policy=policy.default).parsebytes(outputs[MAILS / spec["name"]])
        assert not parsed.defects, (spec["name"], parsed.defects)
        for key in ("From", "To", "Date", "Subject", "Message-ID", "MIME-Version", "Content-Type"):
            assert parsed[key], (spec["name"], key)
        assert not any(part.defects for part in parsed.walk())
        body = parsed.get_body(preferencelist=("plain",)).get_content()
        assert body.replace("\r\n", "\n").strip() == spec["body"].strip()
        assert len(body.strip()) >= 600, spec["name"]
        assert len(list(parsed.iter_attachments())) == len(spec["attachments"])
        for part in parsed.iter_attachments():
            assert part.get_payload(decode=True) == outputs[AKTEN / part.get_filename()]
    return words


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Prüft byteidentische Reproduzierbarkeit ohne Schreibzugriff.")
    parser.add_argument("--list", action="store_true", help="Listet ausschließlich die erwarteten Aktenstücke.")
    args = parser.parse_args()
    outputs = expected_files()
    words = validate(outputs)
    if args.list:
        for path in outputs:
            print(path.relative_to(ROOT))
        return
    if args.check:
        failures = [str(path.relative_to(ROOT)) for path, data in outputs.items()
                    if not path.exists() or path.read_bytes() != data]
        if failures:
            raise SystemExit("Abweichende oder fehlende Dateien: " + ", ".join(failures))
        print("OK: 29 Dateien byteidentisch; 14 DOCX, 12 EML, 3 TXT; EML-Anlagen geprüft.")
        return
    for directory in (AKTEN, MAILS):
        directory.mkdir(parents=True, exist_ok=True)
    for path, data in outputs.items():
        if not path.exists() or path.read_bytes() != data:
            path.write_bytes(data)
    print(json.dumps({"docx": len(DOCUMENTS), "eml": len(EMAILS), "txt": len(CHATS),
                      "woerter_docx": words}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
