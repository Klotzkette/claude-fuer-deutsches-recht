# Konfigurations- und Logfile-Auszug BewerberPilot TalentRank 2.4

**System:** BewerberPilot TalentRank 2.4 (Release Candidate)
**Build:** BP-TR-2.4-RC-2026-05-28
**Hosting:** MedData Hosting GmbH, Region EU-Nürnberg, Mandant elbtal-pilot-2026
**Zeitraum Auszug:** 12.05.2026 00:00 Uhr UTC bis 25.05.2026 23:59 Uhr UTC
**Zweck:** Nachweis der technischen Konformitaet (Art. 12 KI-VO, Art. 11 i.V.m. Anhang IV KI-VO).
**Verfasser des Auszugs:** Tim Lange (DevOps, BewerberPilot Score GmbH), 26.05.2026
**Prüfer:** Dr. Caspar Lintorf (Compliance)

---

## 1. Konfigurationsstand (Auszug aus `bp-tr/config/manifest.yaml`)

```yaml
system:
  name: bp-tr
  version: 2.4-rc
  build_id: BP-TR-2.4-RC-2026-05-28
  git_tag: bp-tr-v2.4-rc

runtime:
  hosting:
    provider: MedData Hosting GmbH
    region: EU-DE-Nuernberg
    tenant: elbtal-pilot-2026
  encryption:
    in_transit: TLS-1.3
    at_rest: AES-256-GCM
  mfa: required-all-roles

models:
  extractor:
    name: bp-extractor
    version: 2.4.0
    type: transformer_ner_finetuned
    training_data: D-Train-2024-HR (rev 12)
    bias_test: passed_with_open_items   # vgl. 13_bias_audit_bericht.md
    explainability: feature_attribution_v3
  ranker:
    name: bp-ranker
    version: 2.4.0
    type: gradient_boosted_trees
    feature_set: feat-set-v8
    weights_rev: w-2026-05-18
  summarizer:
    name: lexicore-coordinator
    version: 3.1   # praeziser Patch noch offen
    endpoint: https://eu-dublin.lexicore.example/v1
    no_training_clause: contract-2026-02-14
    safety_filters: standard+pii-mask

bias_controls:
  feature_blocked:
    - photo
    - date_of_birth
    - religion
    - marital_status
    - union_membership
    - political_orientation
    - country_of_origin_explicit
  feature_masked:
    - free_text_indicators_sensitive
    - care_specific_disabilities

human_oversight:
  ui_requires_review: true
  reject_requires_human: true
  override_logging: enabled
  no_auto_reject: true

logging:
  retention_days:
    upload: 720
    scoring: 720
    view: 540
    decision: 720
    override: 720
    export: 720
  fields_redacted_at_rest:
    - mfa_secret
    - api_key
    - candidate_birth_date
```

## 2. Wesentliche Konfigurationsentscheidungen

1. **`no_auto_reject: true`** technisch im UI-Code und im Backend doppelt durchgesetzt. Ein Ablehnungsstatus kann nicht ohne menschliche Eingabe gesetzt werden.
2. **Featureblockliste** umfasst alle nach Art. 10 KI-VO besonders kritischen Merkmale. Eine Liste der maskierten Merkmale wird quartalsweise gereviewt.
3. **GPAI-Endpoint Dublin EU-Region.** Keine Datenübermittlung in Drittländer, über EU-Region-Endpoint vertraglich abgesichert.
4. **MFA-required-all-roles:** kein Recruiter, kein Admin und kein Auditor kann ohne MFA arbeiten.

## 3. Logfile-Auszug (typische Einträge, anonymisiert)

```
[2026-05-12 09:14:22 UTC] INFO   user=recruiter-23 action=login tenant=elbtal-pilot-2026 ip=hash:8a... mfa=true
[2026-05-12 09:18:01 UTC] INFO   user=recruiter-23 action=open_application app_id=APP-2026-04-1102
[2026-05-12 09:18:09 UTC] INFO   user=recruiter-23 action=view_score app_id=APP-2026-04-1102 score=78 must_flag=PASS reason_codes="career_continuity,language_german_native,medical_certificate"
[2026-05-12 09:18:34 UTC] INFO   user=recruiter-23 action=mark_invitation app_id=APP-2026-04-1102
[2026-05-12 09:23:55 UTC] INFO   user=recruiter-23 action=view_score app_id=APP-2026-04-1118 score=41 must_flag=PASS reason_codes="career_continuity,language_proficient_b2"
[2026-05-12 09:24:18 UTC] WARN   user=recruiter-23 action=attempt_reject app_id=APP-2026-04-1118 blocked_reason="reject_requires_human_text_min_15_chars"
[2026-05-12 09:24:51 UTC] INFO   user=recruiter-23 action=reject app_id=APP-2026-04-1118 reason_text="trotz fachlicher Eignung kein freier Slot im Cluster Pflege ab 1.8."
[2026-05-12 09:25:02 UTC] INFO   override.captured=true app_id=APP-2026-04-1118 override_reason="recruiter ablehnt trotz score-mid"
[2026-05-12 11:02:09 UTC] INFO   user=admin-elbtal action=consent_received app_id=APP-2026-04-1118 candidate_consent_ai_processing=opted_in
[2026-05-12 12:14:48 UTC] ALERT  pmm_check id=monthly_acceptance_rate cluster=Pflege rate=0.18 baseline=0.22 status=under_threshold action=manual_review
[2026-05-13 08:00:00 UTC] INFO   nightly.bias_check status=clean drift=0.011 reference_window=last_30d
[2026-05-13 14:33:11 UTC] WARN   summarizer.fallback applied app_id=APP-2026-04-1209 reason="lexicore_timeout" fallback=local_summary
[2026-05-13 14:33:11 UTC] INFO   summarizer.flag candidate_id=hash:c2... reason="multiple_languages_detected" actions=use_german
[2026-05-13 16:22:18 UTC] ERROR  job=export_for_admin job_id=EX-2026-05-13-0001 status=failed reason="missing_consent_for_export"
[2026-05-14 09:00:01 UTC] INFO   system.config_change actor=devops author=tim.lange field=ranker.weights_rev old=w-2026-05-11 new=w-2026-05-18 motivation="hotfix-bias-feedback-from-fairnesslab"
[2026-05-14 09:00:01 UTC] INFO   versions.deployed extractor=2.4.0 ranker=2.4.0 weights_rev=w-2026-05-18 summarizer=lexicore-coordinator@v3.1
[2026-05-14 09:05:11 UTC] INFO   compliance.flag fairnesslab_recommendation_id=FL-2026-088-R2 status=accepted
[2026-05-16 11:42:55 UTC] INFO   candidate_complaint_filed complaint_id=COMP-2026-0411 channel=web_form status=open
[2026-05-18 19:11:02 UTC] WARN   pmm_check id=monthly_acceptance_rate cluster=IT rate=0.31 baseline=0.27 status=above_threshold action=no_action_required note="positive_drift"
[2026-05-20 07:31:00 UTC] INFO   audit.export FairnessLab id=FL-2026-088 status=delivered
[2026-05-22 12:00:00 UTC] INFO   weekly.bias_metric_summary delivered_to=compliance@bewerberpilot.example
[2026-05-23 10:18:45 UTC] WARN   gpai.response.flag app_id=APP-2026-05-0822 issue="possible_hallucination_education" action=request_human_review
[2026-05-24 09:14:12 UTC] INFO   recruiter_override_rate weekly=0.118 baseline=0.090 status=elevated review_due=2026-05-31
[2026-05-25 17:00:00 UTC] INFO   readiness.gate id=gate_2_bias status=open blocker_id=FL-2026-088-R2
```

## 4. Auffälligkeiten und Hinweise

### 4.1 Ablehnungs-Override

Der Logeintrag `[2026-05-12 09:24:18 UTC] WARN user=recruiter-23 action=attempt_reject app_id=APP-2026-04-1118 blocked_reason="reject_requires_human_text_min_15_chars"` zeigt, dass das System eine Ablehnung **erst** zulässt, wenn der Recruiter eine handschriftliche Begründung von mindestens 15 Zeichen eingibt. Dies entspricht dem Konzept "menschliche Aufsicht" gemaess Art. 14 KI-VO.

### 4.2 PMM-Alert

Der ALERT-Eintrag am 12.05.2026 zur "Pflege-Acceptance-Rate" (0.18 unter Baseline 0.22) löst einen Manual-Review aus. Dieser ist im PMM-Plan vorgesehen (TD-12).

### 4.3 LexiCore Fallback

Der WARN-Eintrag am 13.05.2026 zeigt, dass das System bei LexiCore-Timeouts auf ein lokales Modell zurückgreift. Diese Fallback-Logik ist im Konfigurations-Manifest dokumentiert und im UI sichtbar.

### 4.4 GPAI-Hallucination-Flag

Der WARN-Eintrag am 23.05.2026 zeigt, dass eine GPAI-Zusammenfassung als "mögliche Halluzination zu Bildungsangaben" markiert wurde und das System manuelle Pruefung anfordert. Dies entspricht den Massnahmen aus dem Bias-Auditbericht (vgl. 13_bias_audit_bericht.md, Ziffer 4.1).

### 4.5 Override-Rate eskaliert

Am 24.05.2026 wird eine wachsende Recruiter-Override-Rate (0.118 vs. Baseline 0.090) erfasst. Dieser Wert ist im Pilot relevant; ein Review ist für den 31.05.2026 angesetzt.

### 4.6 Readiness-Gate offen

Am 25.05.2026 zeigt das Readiness-Gate "gate_2_bias" als "open" wegen FairnessLab-Empfehlung FL-2026-088-R2. Dies blockiert eine Pilotfreigabe vor Schliessung der Massnahmen.

## 5. Konsistenz mit anderen Aktendokumenten

- **04_daten_governance_bias_test_art_10.md:** Bias-Test-Beobachten-Schwellen sind im Log überprüft.
- **06_human_oversight_logging_art_12_14.md:** Logging-Spezifikation v1.1 ist im Konfigurations-Manifest umgesetzt.
- **10_lueckenliste_massnahmenplan.md:** Lücken Nr. 1 bis 9 sind im Log nachweisbar oder fehlen (Nr. 5 Human-Oversight-Test ist noch offen).
- **13_bias_audit_bericht.md:** Empfehlungen sind im System als "FairnessLab recommendation_id" abrufbar.

## 6. Aufbewahrung

Die Logdateien werden gemaess Konfiguration `logging.retention_days` zwischen 540 und 720 Tagen aufbewahrt. Ein vollständiger Auszug für den Pilotzeitraum wird der Pilotkundin auf Anfrage übergeben.

## 7. Signatur

Tim Lange (DevOps Lead, BewerberPilot Score GmbH), 26.05.2026

Dr. Caspar Lintorf (Compliance Officer), 26.05.2026 (Prüfvermerk: Auszug freigegeben für interne Verwendung)
