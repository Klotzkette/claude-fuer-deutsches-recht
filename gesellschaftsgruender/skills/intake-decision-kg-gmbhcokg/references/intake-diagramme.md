# 1. Intake-Diagramme

Die Diagramme visualisieren den bereits erhobenen Gründungsfall. Sie werden nur geöffnet, wenn eine grafische Entscheidungsdarstellung benötigt wird.

## Gesamt(Mermaid)

```mermaid
flowchart TD
 Start([Mandant fragt Gruendung an]) --> Intake[Gruender-Intake-Formular]

 Intake --> Q1{Anzahl Gruender?}
 Q1 -->|1| Solo[Solo-Gruender-Pfad]
 Q1 -->|2-3| StandardPath[Standard-Pfad]
 Q1 -->|4+| ComplexPath[Komplex-Pfad mit SHA]

 Solo --> Q2a{Kapital verfuegbar?}
 Q2a -->|< 5.000 EUR| UG_Pfad[UG-Pfad]
 Q2a -->|5.000 - 25.000 EUR| Q2b{Investor geplant?}
 Q2a -->|>= 25.000 EUR| GmbH_Pfad[GmbH-Pfad]

 Q2b -->|Ja| GmbH_Pfad
 Q2b -->|Nein| UG_Empfehlung[UG empfohlen]

 StandardPath --> Q3{Investor in 12 Monaten?}
 Q3 -->|Ja| ClassShares_jetzt[Class-Shares schon bei Gruendung]
 Q3 -->|Nein| ClassShares_spaeter[Class-Shares spaeter einfuehren]
 Q3 -->|Unklar| GenehmigtesKapital_jetzt[Genehmigtes Kapital vorsehen]

 ComplexPath --> ClassShares_jetzt

 ClassShares_jetzt --> SHA_Modul[SHA-Modul triggern]
 ClassShares_spaeter --> Satzung_Modul[Satzung-Modul triggern]
 GenehmigtesKapital_jetzt --> Satzung_Modul

 SHA_Modul --> Vesting{Vesting für Gruender?}
 Vesting -->|Ja| VestingKlausel[Vesting-Klausel SHA]
 Vesting -->|Nein| Stoppschild_Vesting[Warnung: Bad-Leaver-Risiko]

 VestingKlausel --> StimmBindung[Stimmbindungs-Klausel SHA]
 StimmBindung --> Notar[Notar-Vorbereitung]
 Satzung_Modul --> Notar
 UG_Pfad --> Notar
 UG_Empfehlung --> Notar

 Notar --> SV_Check{GF-Sozialversicherung?}
 SV_Check -->|Solo-GF| SV_frei[SV-frei]
 SV_Check -->|Mehrheits-GF| SV_frei
 SV_Check -->|Minderheits-GF| SV_Sperrminoritaet{Echte Sperrminoritaet in Satzung?}

 SV_Sperrminoritaet -->|Ja in Satzung| SV_frei
 SV_Sperrminoritaet -->|Nur in SHA| SV_pflichtig_Warnung[WARNUNG: BSG-Linie - SHA-Stimmbindung reicht nicht]
 SV_Sperrminoritaet -->|Keine| SV_pflichtig[SV-pflichtig]

 SV_frei --> Statusfeststellung[Statusfeststellung Paragraf 7a SGB IV beantragen]
 SV_pflichtig_Warnung --> Statusfeststellung
 SV_pflichtig --> Statusfeststellung

 Statusfeststellung --> HR_Anmeldung[Handelsregister-Anmeldung]
 HR_Anmeldung --> Behörden[Gewerbe Finanzamt IHK BG TraFinG]
 Behörden --> Compliance[Erste 100 Tage GF-Pflichten]
 Compliance --> Ende([Operatives Geschaeft])
```

## Detail-Diagramm: Class-Shares-Modul

```mermaid
flowchart TD
 Start([Class-Shares-Modul]) --> Q1{Anzahl Klassen?}
 Q1 -->|1 nur Common| Klasse1[Standard-Satzung]
 Q1 -->|2 Common + B| Klasse2[Series-A-Struktur]
 Q1 -->|3+ Common A B C| Klasse3[Multi-Class-Struktur]

 Klasse2 --> Q2{Investor-Schutz}
 Q2 -->|Liquidation Preference| LiqPref[Klausel 6 Liquidation Preference]
 Q2 -->|Anti-Dilution| AntiDil[Klausel 7 Anti-Dilution]
 Q2 -->|Veto-Rechte| Veto[Sondervetorechte]

 LiqPref --> Q3{Participating oder non-participating?}
 Q3 -->|non-participating| LiqPref_NP[Beste Praxis bei Tech-Startup]
 Q3 -->|participating| LiqPref_Warnung[WARNUNG: Bei mittelmäßigem Exit Vorteil Investor erheblich]

 AntiDil --> Q4{Methode?}
 Q4 -->|Weighted Average broad-based| AntiDil_WA[Standard empfohlen]
 Q4 -->|Full Ratchet| AntiDil_FR[Aggressiv nur bei riskanten Investments]

 Veto --> Q5{Reichweite}
 Q5 -->|Spezifische Themen| Veto_OK[Klausel 2 Golden Share angepasst]
 Q5 -->|Alle Beschluesse| Veto_Sittenwidrig[WARNUNG Sittenwidrigkeit Paragraf 138 BGB]
```

## Detail-Diagramm: SV-Status-Prüfung

```mermaid
flowchart TD
 Start([SV-Status-Pruefung]) --> Q1{Ist der GF zugleich Gesellschafter?}
 Q1 -->|Nein - Fremd-GF| Fremd[Fremd-GF]
 Q1 -->|Ja| Q2{Anteilshoehe?}

 Fremd --> SV_pflichtig[SV-pflichtig BSG-Linie]

 Q2 -->|>= 50 Prozent| Mehrheit[Mehrheits-GF]
 Q2 -->|< 50 Prozent| Q3{Sperrminoritaet?}

 Mehrheit --> SV_frei[SV-frei BSG-Linie]

 Q3 -->|Ja in Satzung| Q4{Sperrminoritaet umfassend?}
 Q3 -->|Nur in SHA-Stimmbindung| SV_pflichtig_SHA[SV-pflichtig BSG 11.11.2015]
 Q3 -->|Keine| SV_pflichtig

 Q4 -->|Ja| SV_frei
 Q4 -->|Nur teilweise| SV_pruefen[Im Einzelfall pruefen]

 SV_pflichtig --> Statusfeststellung[Paragraf 7a SGB IV beantragen]
 SV_pflichtig_SHA --> Statusfeststellung
 SV_frei --> Statusfeststellung
 SV_pruefen --> Statusfeststellung

 Statusfeststellung --> Lohnabrechnung[Lohnabrechnung entsprechend einrichten]
```

## Detail-Diagramm: Streit-Eskalations-Pfad

```mermaid
flowchart TD
 Start([Streitiger Gesellschafterbeschluss]) --> Q1{Beschluss bereits gefasst?}
 Q1 -->|Nein| Pravention[Praevention: SHA-Stimmbindung pruefen Beirat anrufen]
 Q1 -->|Ja| Q2{Bei HR eingereicht?}

 Q2 -->|Nein| Q3{Eilbeduerftigkeit gegeben?}
 Q2 -->|Ja| Sofort_eA[Einstweilige Verfuegung LG + Anmeldungs-Sperre Registergericht binnen 48h]

 Q3 -->|Ja| Sofort_eA
 Q3 -->|Nein| Anfechtungsklage[Anfechtungsklage binnen 1 Monat]

 Sofort_eA --> Q4{Verfuegung erlassen?}
 Q4 -->|Ja| Hauptverfahren[Hauptverfahren Anfechtungsklage]
 Q4 -->|Nein| Q5{Beschwerde?}
 Q5 -->|Ja| OLG[OLG-Beschwerde]
 Q5 -->|Nein| Hauptverfahren

 Anfechtungsklage --> Hauptverfahren
 OLG --> Hauptverfahren

 Hauptverfahren --> Beirat[Schlichtungs-Pflicht Beirat einhalten]
 Beirat --> Q6{Beirat Vergleich vorgeschlagen?}
 Q6 -->|Ja| Q7{Annahme?}
 Q6 -->|Nein| Verfahren_weiter[LG entscheidet]

 Q7 -->|Ja| Vergleich[Vergleich Klagerückname]
 Q7 -->|Nein| Verfahren_weiter

 Verfahren_weiter --> Urteil[Urteil und ggf. Berufung]
 Pravention --> Vergleich
```
