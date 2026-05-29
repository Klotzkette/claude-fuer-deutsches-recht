# Risikomanagementregister Art. 9 KI-VO

Stand: 15.05.2026

| Risiko-ID | Risiko | Betroffene | Schwere | Eintritt | Maßnahme | Status |
|---|---|---|---|---|---|---|
| R-01 | Diskriminierende Benachteiligung wegen unbalancierter Trainingsdaten | Bewerbende | Hoch | Mittel | Bias-Test nach Stellenfamilie, Geschlecht, Alterssurrogaten, Sprachmustern | Gelb |
| R-02 | Automatisierte faktische Ablehnung durch Rangfolge | Bewerbende | Hoch | Mittel | UI-Sperre, Entscheidung erst nach menschlicher Prüfung, Auditlog | Grün/Gelb |
| R-03 | Unzulässige Verarbeitung besonderer Kategorien | Bewerbende | Hoch | Niedrig/Mittel | Maskierung sensibler Angaben, Nichtverwendung im Score | Gelb |
| R-04 | Halluzinierte Zusammenfassung durch GPAI-Komponente | Bewerbende, Recruiter | Mittel | Mittel | Quellenanker, Unsicherheitshinweis, menschliche Prüfung | Gelb |
| R-05 | Fehlende Nachvollziehbarkeit des Scores | Bewerbende, Betreiber | Hoch | Mittel | Erklärmerkmale, Versionsprotokoll, technische Dokumentation | Gelb |
| R-06 | Zweckentfremdung zur Beschäftigtenbewertung | Beschäftigte | Hoch | Niedrig | Vertragsverbot, technische Tenant-Konfiguration, Monitoring | Grün/Gelb |
| R-07 | Cyberangriff auf Bewerbungsdaten | Bewerbende | Hoch | Niedrig | EU-Hosting, Verschlüsselung, MFA, Pen-Test | Grün |
| R-08 | Unzureichende Betreiberanweisung | Betreiber, Bewerbende | Mittel | Mittel | Gebrauchsanweisung und Schulung vor Pilot | Gelb |

## Bewertung

Der Risikomanagementprozess ist eingerichtet, aber noch nicht vollständig geschlossen. Insbesondere R-01, R-03, R-04 und R-05 blockieren eine finale Konformitätsbescheinigung, solange Testberichte und Freigaben nicht vollständig vorliegen.

## Review-Zyklus

- Vor jedem Major Release.
- Bei neuem Stellencluster.
- Bei Änderung der GPAI-Komponente.
- Bei Beschwerden oder auffälligen Ablehnungsquoten.
- Mindestens quartalsweise im ersten Pilotjahr.
