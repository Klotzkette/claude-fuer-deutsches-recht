#!/usr/bin/env python3
"""Regressionsprüfung: sofortige Erstattung und späterer Rückgriff bleiben getrennt."""
import importlib.util
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location('phishing_gate', ROOT / 'phishing-vorfall-pruefer/scripts/phishing_case_gate.py')
GATE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(GATE)

class RefundSequenceTests(unittest.TestCase):
    def test_negligence_indicators_do_not_block_refund_review(self):
        result = GATE.score_case({'case_name':'Rabenstein','damage_amount':'700',
            'transactions':[{'amount':'700'}], 'authorization_status':'not_authorized',
            'factors':{'tan_shared_by_phone':True,'security_warnings_before':True,
                       'strong_customer_authentication_logged':True,'app_text_clear_amount_recipient':True}})
        self.assertNotEqual(result['traffic_lights']['prozessfreigabe'], 'ROT')
        self.assertEqual(result['refund_review']['path'], 'unverzuegliche_erstattung_pruefen')
        self.assertTrue(result['recourse_review']['separate_from_immediate_refund'])
        self.assertFalse(result['human_release_granted'])

    def test_no_automatic_claim_from_spoofing(self):
        result=GATE.score_case({'factors':{'spoofed_bank_number':True}})
        self.assertNotEqual(result['traffic_lights']['erstattung_dem_grunde'],'GRUEN')
        self.assertEqual(result['refund_review']['path'],'autorisierung_aufklaeren')

    def test_authorized_fraud_is_not_automatically_675u(self):
        result=GATE.score_case({'authorization_status':'authorized'})
        self.assertEqual(result['refund_review']['path'],'andere_anspruchsgrundlage_pruefen')

    def test_third_party_fraud_is_not_payer_fraud_exception(self):
        result=GATE.score_case({'authorization_status':'not_authorized','factors':{'third_party_fraud':True}})
        self.assertEqual(result['refund_review']['fraud_exception_status'],'nicht_belegt')

    def test_written_notification_is_only_a_review_input(self):
        result=GATE.score_case({'authorization_status':'not_authorized',
            'payer_fraud_suspicion':{'reasons':'Bank behauptet Beteiligung; bestritten','evidence':'B1'},
            'authority_notification':{'written':True,'authority':'zuständige Behörde noch prüfen','date':'2026-10-13','evidence':'B2'}})
        self.assertEqual(result['refund_review']['fraud_exception_status'],'begruendung_und_mitteilung_rechtlich_pruefen')
        self.assertFalse(result['human_release_granted'])

    def test_string_false_is_not_treated_as_true(self):
        with self.assertRaises(ValueError): GATE.score_case({'factors':{'spoofed_bank_number':'false'}})

    def test_missing_amounts_remain_unknown(self):
        result=GATE.score_case({})
        self.assertIsNone(result['damage_amount'])
        self.assertIsNone(result['transaction_total'])
        self.assertIsNone(result['damage_matches_transactions'])

    def test_incomplete_transactions_are_not_summed_as_zero(self):
        result=GATE.score_case({'damage_amount':'700','transactions':[{'amount':'700'},{}]})
        self.assertIsNone(result['transaction_total'])
        self.assertIsNone(result['damage_matches_transactions'])

    def test_negative_or_non_numeric_notification_interval_is_rejected(self):
        for value in [-30, 'gestern', True, float('nan')]:
            with self.subTest(value=value),self.assertRaises(ValueError):
                GATE.score_case({'immediate_block_call_minutes':value})

    def test_minutes_do_not_determine_legal_promptness(self):
        result=GATE.score_case({'immediate_block_call_minutes':45})
        self.assertEqual(result['reported_block_call_minutes'],45)
        self.assertFalse(any('zeitnah' in point for point in result['claimant_points']))

    def test_invalid_money_does_not_become_a_claim(self):
        for value in ['-700','NaN','Infinity']:
            with self.subTest(value=value),self.assertRaises(ValueError): GATE.score_case({'damage_amount':value})

if __name__=='__main__': unittest.main()
