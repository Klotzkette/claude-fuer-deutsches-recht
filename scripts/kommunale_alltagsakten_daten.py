"""Acht getrennte kommunale Alltagsakten; die vier bestehenden Akten bleiben erhalten."""
from kommunale_alltagsakten_verkehr import CASES as VERKEHR
from kommunale_alltagsakten_amt import CASES as AMT

CASES = sorted(VERKEHR + AMT, key=lambda case: case['slug'])
SLUGS = frozenset(case['slug'] for case in CASES)

REVIEW = {
 'akha-wuerzburg-fahrzeugschaden': ('Fahrtzweck, Halter, Fahrer und Anspruchsgegner anhand der Einsatzunterlagen unterscheiden.', 'Reparatur, frühere Beschädigungen, Vorsteuer und einzelne Nebenforderungen getrennt belegen.'),
 'akha-wuerzburg-schwimmbad': ('Betreiber-GmbH, privatrechtlichen Eintritt und konkrete Gefahrenkenntnis zuordnen.', 'Behandlung, Heilungsverlauf und bezifferte Kosten ohne erfundene Dauerfolgen auswerten.'),
 'akha-wuerzburg-baumpflege': ('Ausführung, Absperrung und Aufsicht aus dem konkreten Auftrag ableiten; Verwaltungshelferstellung nicht pauschal unterstellen.', 'Fallenden Ast, beschädigtes Fahrzeug und Reparaturbedarf anhand der zeitnahen Unterlagen abgleichen.'),
 'akha-wuerzburg-schlagloch': ('Straßenklasse, Pflichtenträger, Kontrollen und Erkennbarkeit der konkreten Gefahr klären.', 'Unfallschaden von Vorschaden und ohnehin erforderlicher Reifenbeschaffung abgrenzen.'),
 'akha-wuerzburg-glatteis': ('Genaue Sturzstelle, Art der Verkehrsfläche, Verkehrsbedeutung und erneute Glätte mit dem tatsächlichen Streuablauf verbinden.', 'Zeitnahe Beobachtungen, spätere Erinnerungen und den medizinisch belegten Umfang des Schadens trennen.'),
 'akha-wuerzburg-antragsbearbeitung': ('Vollständigkeit, Zuständigkeit, rechtmäßige Entscheidungsalternative und erfolgversprechenden Primärrechtsschutz konkret prüfen.', 'Entgangenen Gewinn aus Umsätzen, ersparten Aufwendungen und tatsächlich nicht anderweitig nutzbaren Kosten entwickeln.'),
 'akha-wuerzburg-baugenehmigung': ('Bescheid, Rechtsbehelf, Abhilfe und hypothetisch rechtzeitige Genehmigung anhand der Chronologie prüfen.', 'Mietbeginn, Finanzierungskosten und ersparte Aufwendungen ohne Doppelzählung und ohne pauschalen Entschädigungsanspruch abgleichen.'),
 'akha-wuerzburg-abwasseranlage': ('Die Kommune als geschädigte Anspruchstellerin und den Tiefbauer als möglichen Ersatzpflichtigen erkennen.', 'Schäden an der Leitung von Schäden durch austretende Flüssigkeit unterscheiden; Reparatur- und Personalaufwand sowie Vertragslage belegen.'),
}
