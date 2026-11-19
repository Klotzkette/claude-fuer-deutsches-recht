"""Fallbezogene Nachlieferungen zu den fünf priorisierten Schulungsakten."""
import csv
import hashlib
import io
from datetime import datetime
from email import policy
from email.message import EmailMessage
from email.parser import BytesParser
from pathlib import Path

# Die Zuordnung zur vorhandenen Nachricht bewahrt Vorgangsbezug und Korrespondenzpartner.
LIEFERUNGEN = {
    "apothekenrecht-retaxation-kuehlkette-bremen": (
        "07", "2026-07-03T11:12:00+02:00", "Tour HB-K2 – Messstellen und Übergabe",
        "13_zuordnung_transportprotokoll", """Beigefügt ist der Auszug aus dem Schichtbuch der Tour HB-K2. Unsere Disposition hat die Gerätenummern mit dem Rücknahmeschein der Box K-99218 verglichen. FZ-1182 war am Türholm des Fahrzeugs befestigt. Die Anzeige dort konnte der Fahrer beim Entladen sehen. NL-44018 lag im Deckelfach der Box. Wir haben keinen Fühler an einer einzelnen Packung angebracht.

Das Fahrerterminal hat die Übergabe beim Scannen der Box gebucht. Die Zeile zur Rücknahme stammt von der abendlichen Tour und bezeichnet nur die leere Box. Das erklärt, warum deren Nummer nach der Auslieferung ein zweites Mal auftaucht. Für den Zeitraum nach der Übergabe liegen uns keine Messungen des Wareninneren vor. Können Sie bitte den betreffenden Wareneingang mit dem Papierbeleg aus dem roten Tagesordner zusammenführen?

Maren Voß, Qualitätssicherung""",
        "Zeit am 20.02.2026;Vorgang;Gerät oder Gebinde;Beleg;Feststellung\n05:41;Packplatz;K-99218 / NL-44018;P-502;Deckelfach bestückt und Siegel 98117 geschlossen\n07:18;Erster Halt;FZ-1182;Türkontakt 01;Türzone 9,1 Grad\n07:18;Messintervall;NL-44018;Messreihe 177;Box 7,8 Grad\n07:31;Empfang;K-99218;Scan HB-07-31;Siegel 98117 abgezeichnet\n17:26;Leergutrücknahme;K-99218;L-118;ohne Arzneimittel übernommen",
        "Dispositionsauszug zu Außenfühler und Boxlogger", "Antwort des Großhandels zu Messorten, Siegel und Ende der Transportmessung"),
    "krankenhausrecht-md-intensivabrechnung-halle": (
        "08", "2026-05-19T08:37:00+02:00", "Kiste 14 – Scanlauf und Empfängerjournal",
        "13_journal_scanauftrag", """Die Rechtsabteilung hat mich gefragt, was im ersten Export tatsächlich sichtbar war. Ich habe die Objektkennung des Tagesbogens mit dem Auftrag im Scanjournal abgeglichen. Beim ersten Einzug lief das Profil „Aufnahme einseitig“. Der Bedienvermerk nennt eine Heftklammer. Im Journal steht keine persönliche Bestätigung, dass jemand die Rückseite angesehen hat.

Gestern haben wir Vorder- und Rückseite neu erfasst. Auf der Rückseite sind zwei Handzeichen lesbar. Der Transport ins interne Archiv wurde quittiert. Die letzte Zeile ist der Eingang beim Medizincontrolling. Für eine spätere Weitergabe an den MD haben wir hier keine Quittung. Bitte geben Sie bei Ihrer Suche neben der Fallnummer auch die beiden Objektkennungen an, sonst liefert die Trefferliste nur die neuere Fassung.

Kathrin Kühne, Zentralarchiv""",
        "Zeit;Fall;Objekt;Vorgang;Seiten;Ziel\n2026-02-02 10:13;260112-88341;S17-001;Einzugprofil einseitig;1;Archiv ALT\n2026-05-18 15:35;260112-88341;K-03-14-7;Fach geöffnet;2;Arbeitsplatz 04\n2026-05-18 15:51;260112-88341;S17-002;Duplexscan;2;Archiv REV\n2026-05-18 16:12;260112-88341;S17-002;interne Zustellung;2;Medizincontrolling",
        "Journal der beiden Scanläufe für den Tagesbogen vom 17. Januar", "Rückfrage zu Seitenzahl, Objektkennung und Eingangsnachweis"),
    "eu-prozessrecht-beihilfe-nichtigkeitsklage-leipzig": (
        "07", "2026-07-07T09:18:00+02:00", "Matter 61-2026 – Ablageabgleich vor der Nachreichung",
        "13_versandordner_kontrolle", """Ich habe den gesperrten Versandordner vom 26. Juni mit der heute früh übernommenen Arbeitskopie verglichen. Der Export enthält sichtbare Dateinamen und Seitenzahlen. Bei der Kanzlei hieß das Gutachten schon A.9. Auf Seite zwei des damals mitgesandten Verzeichnisses trägt dieselbe Bezeichnung noch die Nummer A.8. Bitte prüfen Sie den konkreten Verweis auf Seite 31, bevor Sie das Verzeichnis freigeben.

Bei A.12 war die nicht vertrauliche PDF bereits unter neuem Namen gespeichert. Im Sichtfenster auf Seite sechs sind weiterhin zwei Kundenzeilen lesbar. Die Arbeitskopie vom 7. Juli ersetzt diese Seite. Sie liegt bei mir zur Gegenlese. Die Quittung vom 26. Juni gehört ausschließlich zum damaligen Versand. Können Sie den Eingang des neuen Registerauszugs bei der Mandantin erfragen? Ich kann ihn im Arbeitsordner noch nicht zuordnen.

Felix""",
        "Stand;Ordner;Kennung;Gegenstand;Kontrollstelle\n26.06.2026;versandt;A.8;Bankangebote;22 Seiten\n26.06.2026;versandt;A.9;Gutachten Harenberg;41 Seiten / Verzeichnis verweist auf A.8\n26.06.2026;versandt;A.12-nv;Kundenpreise;Sichtprüfung Seite 6 offen\n07.07.2026;Arbeitskopie;A.12-nv-r2;Ersatzseite importiert;Zweitlesung ausstehend\n07.07.2026;Arbeitskopie;A.2;Registerauszug;Beschaffung bei Mandantin",
        "Abgleich von versandtem Verzeichnis und späterer Arbeitskopie", "Kanzleirückfrage zu Anlagenbezeichnung, Gegenlese und Registerauszug"),
    "gesellschaftsrecht-treuepflicht-kapitalerhoehung-ulm": (
        "08", "2026-05-29T10:05:00+02:00", "Kapitalrunde – zwei getrennte Spalten für die Besprechung",
        "14_varianten_nennbetraege", """Beim Abgleich unserer Unterlagen ist mir aufgefallen, dass in der Tabelle die 23,75 Prozent aus meinem Alternativangebot neben den 81,25 Prozent aus dem Beschluss stehen. So hat es keine gemeinsame Verteilung gegeben. Ich habe für Ihren Besprechungsordner die jeweiligen Nennbeträge getrennt. Der bisherige Anteil meines Vaters bleibt in beiden Spalten bei 200.000 Euro.

Die zweite Spalte mit meinem Beitrag von 300.000 Euro ist eine Gegenrechnung. Sie setzt voraus, dass das Familienkontor für den Rest zugelassen wird. Ich habe das Geld angeboten, aber aus dieser Aufstellung folgt weder, dass ich gezeichnet habe, noch dass meine Zahlung verbucht wurde. Den Stand der Registeranmeldung kann ich selbst nicht sehen. Bitte bringen Sie für unser Gespräch auch die Fassung der Niederschrift mit, in der meine Bitte um eine längere Bezugsfrist protokolliert ist.

Anna""",
        "Beteiligter;Alt EUR;Neu laut Beschluss EUR;Ende Beschluss EUR;Neu bei Teilzulassung EUR;Ende Alternative EUR\nViktor Brenner;200000;0;200000;0;200000\nDr. Anna Brenner;175000;0;175000;300000;475000\nFamilienkontor Brenner KG;125000;1500000;1625000;1200000;1325000",
        "Getrennte Nennbetragsrechnungen für Beschluss und Alternativangebot", "Mandantenmail zur Herkunft der gemischten Prozentangaben"),
    "wirtschaftsprueferrecht-unabhaengigkeit-hamburg": (
        "07", "2026-06-10T14:26:00+02:00", "Nordwerft – welche Einträge stammen von meinem Zugang?",
        "13_arbeitsplatz_abgleich", """Ich habe im Beisein von Frau Oltmann die mir vorgelegten Zeilen mit meinem damaligen Kalender verglichen. Am 3. September hatte ich den Rücklauf der Elbe Bank im Team angefragt. Der Kommentar in der Liste ist meiner. Am 11. September habe ich einen Vergleich der Covenant-Spalte kommentiert. Eine Unterschrift unter das Arbeitspapier oder eine Freigabe ist daraus nicht abzulesen.

Die Zahl 17 kommt aus dem Bericht über die Objektaufrufe. Darin erscheint ein Dokument erneut, wenn ich es nach dem Wechsel aus der Bankliste wieder öffne. Ich kann heute nicht mehr sagen, welche einzelne Seite ich bei jedem Aufruf gelesen habe. Mein Erinnerungseintrag wurde heute gefertigt. Für die zeitliche Einordnung bleiben das alte Portaljournal und das Ticket über die Entziehung der Rechte maßgeblich. Bitte legen Sie die vorgelegte Auswahl zu meinem Vermerk, damit klar ist, auf welche Zeilen sich meine Antwort bezieht.

Lena Brandt""",
        "Zeit;Objekt;Anzeige im Portal;Quelle;Reichweite\n2025-08-29 08:07;FIN-4.7 v12;geöffnet;Portaljournal;Dauer nicht erfasst\n2025-09-03 14:42;Bankbestätigungen v18;Kommentar;Historie;Rücklauf Elbe Bank fehlt\n2025-09-11 09:16;FIN-4.7 v19;Kommentar;Historie;Abgleich Covenant-Spalte\n2025-09-12 16:05;Mandat Nordwerft;Rechte entzogen;Ticket IND-25-4471;Zeit des Vollzugs",
        "Protokollauszug der der Mitarbeiterin vorgelegten vier Ereignisse", "Datierte Stellungnahme der Prüfungsmanagerin zu zwei Kommentaren"),
}


def write_nachlieferung(directory):
    nummer, zeit, betreff, stamm, inhalt, tabelle, tabellentitel, mailtitel = LIEFERUNGEN[directory.name]
    vorlage = BytesParser(policy=policy.default).parsebytes(next(directory.glob(nummer + "_*.eml")).read_bytes())
    mail = EmailMessage(policy=policy.SMTP)
    mail["From"] = vorlage["From"]
    if directory.name == "gesellschaftsrecht-treuepflicht-kapitalerhoehung-ulm":
        # Anna schreibt ihrem Anwalt, der das ursprüngliche Finanzierungsangebot in Kopie erhielt.
        mail["To"] = next(address for address in vorlage["Cc"].addresses
                          if address.addr_spec == "m.rupp@rupp-eberlein.de")
    else:
        mail["To"] = vorlage["To"]
    mail["Date"] = datetime.fromisoformat(zeit)
    mail["Subject"] = betreff
    mail["In-Reply-To"] = vorlage["Message-ID"]
    mail["References"] = vorlage["Message-ID"]
    mail["Message-ID"] = "<" + stamm + "." + directory.name + "@aktenpost.example>"
    mail.set_content(inhalt + "\n")
    export = io.StringIO(newline="")
    csv.writer(export, delimiter=";").writerows(csv.reader(tabelle.splitlines(), delimiter=";"))
    daten = export.getvalue().encode("utf-8")
    anlage = directory / (stamm + ".csv")
    anlage.write_bytes(daten)
    mail.add_attachment(daten, maintype="text", subtype="csv", filename=anlage.name,
                        params={"charset": "utf-8"})
    mail.set_boundary("aktenpost-" + hashlib.sha256(daten).hexdigest()[:24])
    post = directory / (str(int(stamm[:2])+1) + "_korrespondenz_nachlieferung.eml")
    post.write_bytes(mail.as_bytes())
    readme = directory / "README.md"
    text = readme.read_text()
    rows = f"| `{anlage.name}` | {tabellentitel} |\n| `{post.name}` | {mailtitel} |\n"
    if rows not in text:
        readme.write_text(text.replace("\n## Bearbeitung", rows + "\n## Bearbeitung"))


if __name__ == "__main__":
    for slug in LIEFERUNGEN:
        write_nachlieferung(Path(__file__).resolve().parents[1] / "testakten" / slug)
