"""Gemeinsame, vollständig fiktive Stammdaten der beiden Bauvergabe-Lebensakten."""
from decimal import Decimal

STAGES = {
    '01-vergabeunterlagen': 'Bauvergabeunterlagen erstellen',
    '02-vergabeverfahren': 'Vergabeverfahren führen',
    '03-bieterarbeit': 'Als Bauunternehmen anbieten',
    '04-rechtsschutz': 'Vergaberechtsschutz bearbeiten',
    '05-nachtragsmanagement': 'Nachträge nach dem Zuschlag bearbeiten',
}
PLUGINS = ['bauvergabe-unterlagen', 'bauvergabe-verfahren', 'bauvergabe-bieter',
           'bauvergabe-rechtsschutz', 'bauvergabe-nachtragsmanagement']
CASES = [
    dict(slug='bauvergabe-klinikum-muenster', short='Klinik',
         title='Klinikum Lindenbogen Münster – Ambulanzneubau und Krankenhausapotheke',
         reference='LBM-2026-01', owner='Klinikum Lindenbogen Münster gGmbH',
         address='Lindenbogen 18, 48155 Münster', city='Münster',
         lead='Dr. Ottilie Knorren', purchaser='Roswitha Klapper',
         engineer='Benedikt Faltenwurf', architect='Faltenwurf Planen GmbH',
         winner='Anselm Klinker Bau GmbH', director='Anselm Klinker',
         rival='Walburga Stein & Sohn GmbH', rival_lead='Walburga Stein',
         counsel='Rechtsanwältin Naila Humpelstiel',
         project_net=40000000, lot_budget=7800000,
         lot='Los 01 – Baugrube, Gründung und Rohbau',
         area=8200, published='2026-10-12', original_deadline='2026-11-16',
         deadline='2026-11-23', notice='2026-12-01', first_award='2026-12-12',
         objection='2026-12-03', refusal='2026-12-04', petition='2026-12-07',
         service='2026-12-08', withdrawal='2026-12-18', new_notice='2027-01-05',
         award='2027-01-18', start='2027-02-01', finish='2027-10-29',
         offer_multiplier='1.00', rival_multiplier='1.04', third_multiplier='1.09',
         issue='Nicht bekannt gemachte regionale Baustellenerfahrung in der Wertung',
         after_issue='Zusätzliche Fundamentvertiefung und verspätete Planfreigabe',
         quantities=[1,13500,4000,2000,4500,650000,18000,3100,8200,2400,2200,1,120,200,90,1],
         prices=[280000,35,28,140,260,2.45,74,190,92,88,64,620000,145,75,960,150000]),
    dict(slug='bauvergabe-wohnhaus-bielefeld', short='Wohnhaus',
         title='Soziales Wohnen Bielefeld – 16 Wohnungen am Quittenhof',
         reference='SWB-QH-2026-02', owner='Soziales Wohnen Bielefeld gGmbH',
         address='Quittenhof 6, 33602 Bielefeld', city='Bielefeld',
         lead='Edeltraud Rumpel', purchaser='Milan Knödler',
         engineer='Friedemann Blechle', architect='Blechle & Yilmaz Planungsgesellschaft mbH',
         winner='Kunigunde Mörtelbau GmbH', director='Kunigunde Mörtel',
         rival='Ferdi Ziegelwerk Bau GmbH', rival_lead='Ferdinand Ziegelwerk',
         counsel='Rechtsanwalt Cem Wunibald Schlotter',
         project_net=8400000, lot_budget=2200000,
         lot='Los 01 – Erdarbeiten und Rohbau',
         area=1900, published='2026-10-19', original_deadline='2026-11-23',
         deadline='2026-11-30', notice='2026-12-08', first_award='2026-12-19',
         objection='2026-12-10', refusal='2026-12-11', petition='2026-12-14',
         service='2026-12-15', withdrawal='2027-01-06', new_notice='2027-01-12',
         award='2027-01-25', start='2027-02-08', finish='2027-08-31',
         offer_multiplier='1.00', rival_multiplier='1.035', third_multiplier='1.075',
         issue='Streit über Referenznachforderung und Eignungsleihe',
         after_issue='Geänderte Brandwand und streitige Bauzeitfolgen',
         quantities=[1,2300,600,450,1100,150000,4200,850,1900,620,500,1,35,60,24,1],
         prices=[85000,32,26,130,250,2.40,70,180,87,82,60,135000,140,72,940,48000]),
]
LV = [
 ('01.01','Baustelleneinrichtung einschließlich Rückbau','psch'),
 ('02.01','Aushub getrennt nach Bauabschnitten; Bodenklasse durch Homogenbereiche ersetzt','m3'),
 ('02.02','Transport unbelasteten Aushubs zur benannten Annahmestelle','m3'),
 ('02.03','Tragschicht aus güteüberwachtem Mineralgemisch','m3'),
 ('03.01','Ortbeton in Gründung, Wänden und Decken nach Bauteilliste','m3'),
 ('03.02','Betonstahl liefern, schneiden, biegen und einbauen','kg'),
 ('03.03','Schalung einschließlich Aussparungen nach freigegebenem Plan','m2'),
 ('04.01','Mauerwerkswände nach Wandtypenliste','m2'),
 ('04.02','Deckenelemente einschließlich Montage nach Statik','m2'),
 ('05.01','Abdichtung erdberührter Bauteile nach Abdichtungskonzept','m2'),
 ('05.02','Perimeterdämmung mit nachgewiesenen Eigenschaften','m2'),
 ('06.01','Baulogistik, Gerüste und temporäre Schutzmaßnahmen','psch'),
 ('06.02','Koordinierte Leitungsdurchführungen nach Durchbruchsliste','St'),
 ('06.03','Fugenabdichtung mit dokumentiertem Systemnachweis','m'),
 ('07.01','Fertigteiltreppen nach freigegebener Treppenliste','St'),
 ('08.01','Bestands- und Revisionsunterlagen sowie vereinbarte Prüfleistungen','psch'),
]

def money(value):
    return f'{Decimal(str(value)):,.2f}'.replace(',', 'X').replace('.', ',').replace('X', '.')

def total(case, multiplier='1'):
    return sum(Decimal(str(q))*Decimal(str(p))*Decimal(multiplier) for q,p in zip(case['quantities'],case['prices'])).quantize(Decimal('.01'))

def case_by_slug(slug):
    return next(c for c in CASES if c['slug']==slug)
