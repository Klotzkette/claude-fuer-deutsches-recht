#!/usr/bin/env python3
"""Grenzfälle der Kalenderrechnung; keine Prüfung der Rechtswahl durch diese Tests."""
import copy,importlib.util,json,subprocess,sys,tempfile,unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
SPEC=importlib.util.spec_from_file_location('fristen',ROOT/'ki-native-kanzlei/scripts/fristen.py')
f=importlib.util.module_from_spec(SPEC);SPEC.loader.exec_module(f)

def fixture(**profile):
    p={'norm':'Explizites Testprofil §§187–193 BGB','rule_source':'https://www.gesetze-im-internet.de/bgb/__188.html','trigger_source':'Testdatum, kein echter Zugang','rule_verified':True,'mode':'event','trigger':'2026-01-31','amount':1,'unit':'months','end_adjustment':'none','adjustment_basis':'Testprofil ohne Verschiebung'}
    p.update(profile)
    return {'schema_version':1,'matter_id':'DEMO-FRIST','profile':p,'calendar':{'place':'Synthetischer Testort','source':'Synthetischer Kalender; nicht zur Mandatsverwendung','valid_from':'2024-01-01','valid_to':'2029-12-31','verified':True,'holidays':[{'date':'2026-04-03','name':'Karfreitag'},{'date':'2026-04-06','name':'Ostermontag'},{'date':'2026-12-25','name':'Weihnachten I'},{'date':'2026-12-26','name':'Weihnachten II'}]}}

class CalendarTests(unittest.TestCase):
    def test_calendar_semantics(self):
        cases=[({'trigger':'2026-01-31'},'2026-02-28'),({'trigger':'2028-01-31'},'2028-02-29'),({'trigger':'2026-01-31','mode':'start'},'2026-02-28'),({'trigger':'2026-01-30','mode':'start'},'2026-02-28'),({'trigger':'2026-01-28','mode':'start'},'2026-02-27'),({'trigger':'2026-03-01','mode':'start'},'2026-03-31'),({'trigger':'2026-10-07','unit':'days','amount':1},'2026-10-08'),({'trigger':'2026-10-07','unit':'days','amount':1,'mode':'start'},'2026-10-07'),({'trigger':'2026-10-07','unit':'weeks','amount':2},'2026-10-21'),({'trigger':'2026-10-07','unit':'weeks','amount':2,'mode':'start'},'2026-10-20'),({'trigger':'2024-02-29','unit':'years'},'2025-02-28'),({'trigger':'2024-02-29','unit':'years','mode':'start'},'2025-02-28'),({'trigger':'2026-12-20','unit':'months'},'2027-01-20'),({'trigger':'2026-01-31','end_adjustment':'next_working_day'},'2026-03-02'),({'trigger':'2026-03-20','unit':'weeks','amount':2,'end_adjustment':'next_working_day'},'2026-04-07'),({'trigger':'2026-12-11','unit':'weeks','amount':2,'end_adjustment':'next_working_day'},'2026-12-28')]
        for args,expected in cases:
            with self.subTest(args=args):self.assertEqual(f.calculate(fixture(**args))['end'],expected)
    def test_no_assumed_monday_shift(self):
        self.assertEqual(f.calculate(fixture(trigger='2026-03-20',unit='weeks',amount=2))['end'],'2026-04-03')
    def test_fixed(self):
        x=fixture(mode='fixed',trigger='2026-04-03',end_adjustment='next_working_day');x['profile'].pop('amount');x['profile'].pop('unit')
        r=f.calculate(x);self.assertEqual(r['end'],'2026-04-07');self.assertEqual(len(r['shifted_days']),4)
    def test_workdays_need_definition(self):
        x=fixture(trigger='2026-04-02',unit='working_days',amount=2,weekdays=[0,1,2,3,4],working_day_definition='Test: Montag bis Freitag ohne Feiertage')
        self.assertEqual(f.calculate(x)['end'],'2026-04-08')
        x['profile']['weekdays']=[0,1,2,3,4,5]
        self.assertEqual(f.calculate(x)['end'],'2026-04-07')
        del x['profile']['working_day_definition']
        with self.assertRaises(ValueError):f.calculate(x)
    def test_long_year_does_not_mean_365(self):
        self.assertEqual(f.calculate(fixture(trigger='2027-03-01',unit='years'))['end'],'2028-03-01')
    def test_calendar_coverage_no_silent_rollover(self):
        x=fixture(trigger='2029-12-31');self.assertRaises(ValueError,f.calculate,x)
    def test_calendar_rejects_unverified(self):
        x=fixture();x['calendar']['verified']=False;self.assertRaises(ValueError,f.calculate,x)
    def test_rule_rejects_unverified(self):
        x=fixture();x['profile']['rule_verified']=False;self.assertRaises(ValueError,f.calculate,x)
    def test_bad_amounts(self):
        for n in [True,False,0,-1,1.5,'2',None,36601]:
            with self.subTest(n=n):self.assertRaises(ValueError,f.calculate,fixture(amount=n))
    def test_bad_profile(self):
        for kv in [{'mode':'auto'},{'unit':'halfmonths'},{'end_adjustment':'auto'},{'trigger':'31.01.2026'},{'trigger':'2026-02-30'},{'rule_source':''},{'trigger_source':'x\ny'}]:
            with self.subTest(kv=kv):self.assertRaises(ValueError,f.calculate,fixture(**kv))
    def test_unknown_rules_not_ignored(self):
        for key in ['suspensions','restart','service_presumption','appeal_type','whatever']:
            x=fixture();x[key]=[];self.assertRaises(ValueError,f.calculate,x)
        x=fixture();x['profile']['hearing_time']='12:00';self.assertRaises(ValueError,f.calculate,x)
    def test_duplicate_holiday(self):
        x=fixture();x['calendar']['holidays']*=2;self.assertRaises(ValueError,f.calculate,x)
    def test_schema_boolean_not_version(self):
        x=fixture();x['schema_version']=True;self.assertRaises(ValueError,f.calculate,x)
    def test_input_immutable_and_hash_stable(self):
        x=fixture();old=copy.deepcopy(x);a=f.calculate(x);b=f.calculate(x)
        self.assertEqual(x,old);self.assertEqual(a,b);self.assertEqual(len(a['input_sha256']),64);self.assertFalse(a['calendar_written']);self.assertFalse(a['reminder_created'])
    def test_hours_dst_and_excluded_days(self):
        cases=[('2026-03-28T12:00:00+01:00',24,'elapsed','2026-03-29T13:00:00+02:00'),('2026-10-24T12:00:00+02:00',24,'elapsed','2026-10-25T11:00:00+01:00'),('2026-04-02T16:00:00+02:00',24,'exclude_nonworking_days','2026-04-07T16:00:00+02:00'),('2026-10-02T16:00:00+02:00',8,'exclude_nonworking_days','2026-10-03T00:00:00+02:00'),('2026-10-02T16:00:00+02:00',9,'exclude_nonworking_days','2026-10-05T01:00:00+02:00')]
        for trigger,amount,rule,expected in cases:
            x=fixture(mode='hours',trigger=trigger,amount=amount,zone='Europe/Berlin',hour_rule=rule);x['profile'].pop('unit')
            with self.subTest(trigger=trigger,rule=rule):self.assertEqual(f.calculate(x)['end'],expected)
    def test_hours_ambiguous_requires_explicit_valid_offset(self):
        for trigger in ['2026-03-29T02:30:00+01:00','2026-03-29T02:30:00+02:00','2026-10-25T02:30:00','2026-07-01T08:00:00+01:00']:
            x=fixture(mode='hours',trigger=trigger,zone='Europe/Berlin',hour_rule='elapsed');x['profile'].pop('unit')
            with self.subTest(trigger=trigger):self.assertRaises(ValueError,f.calculate,x)
    def test_hours_both_folds_valid(self):
        for off,expected in [('+02:00','2026-10-25T02:30:00+01:00'),('+01:00','2026-10-25T03:30:00+01:00')]:
            x=fixture(mode='hours',trigger='2026-10-25T02:30:00'+off,zone='Europe/Berlin',hour_rule='elapsed');x['profile'].pop('unit')
            self.assertEqual(f.calculate(x)['end'],expected)
    def test_cli_no_overwrite_and_readable_audit(self):
        with tempfile.TemporaryDirectory() as td:
            d=Path(td);inp=d/'input.json';inp.write_text(json.dumps(fixture()));out=d/'run';cmd=[sys.executable,str(ROOT/'ki-native-kanzlei/scripts/fristen.py'),'--data',str(inp),'--out',str(out)]
            a=subprocess.run(cmd,capture_output=True,text=True);self.assertEqual(a.returncode,0,a.stderr)
            original=(out/'fristenvermerk.json').read_bytes();self.assertIn('2026-02-28',(out/'fristenvermerk.md').read_text())
            b=subprocess.run(cmd,capture_output=True,text=True);self.assertEqual(b.returncode,2);self.assertEqual((out/'fristenvermerk.json').read_bytes(),original)
if __name__=='__main__':unittest.main(verbosity=2)
