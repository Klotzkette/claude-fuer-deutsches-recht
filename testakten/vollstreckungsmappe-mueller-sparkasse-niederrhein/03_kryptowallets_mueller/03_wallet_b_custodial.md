# Wallet B custodial - Forderungspfaendung gegen Bitpanda

## Rechtliche Einordnung

Wer Krypto bei einem regulierten Krypto-Verwahrer wie Bitpanda haelt, hat einen **schuldrechtlichen Herausgabe- und Auszahlungsanspruch** gegen den Verwahrer. Das ist eine geldwerte Forderung im Sinne der Paragrafen 829, 835 ZPO. Konsequenz: ganz **klassische Forderungspfaendung mittels PfUEB**, kein Sachpfaendungsantrag.

Drittschuldnerin: Bitpanda GmbH, Stella-Klein-Loew-Weg 17, 1020 Wien. Bitpanda hat eine deutsche Tochter (Bitpanda Asset Management GmbH, Frankfurt) mit BaFin-Erlaubnis Paragraf 1 Abs. 1a Satz 2 Nr. 6 KWG; rechtlich ist aber die Wiener GmbH Vertragspartnerin des Kunden. Daraus folgt der Auslandsbezug, der die Vollstreckung deutlich aufwendiger macht.

## Anwendbare Skills

- `zv-pfueb-mieter-finanzamt` (Forderungspfaendung gegen sonstige Drittschuldner; Bitpanda ist weder Bank im Sinne der Skill-Schubladen Bank/Lohn, sondern ein "sonstiger" Drittschuldner)
- `zv-elektronische-zustellung-2027` (Bitpanda hat in Deutschland eBO bereits eroeffnet; Zustellung in Wien laeuft separat ueber EU-Zustellungs-VO)
- `zv-abwehr-schuldner` aus Schuldnersicht
- `zv-vermoegensauskunft-gv` (Quelle der Daten)

## Vollstreckungsweg

Drei Varianten:

### Variante 1 - PfUEB an deutsche Tochter

Die Bitpanda Asset Management GmbH Frankfurt ist Empfangsbevollmaechtigte der Mutter fuer aufsichtsrechtliche Zwecke. Eine direkte Inanspruchnahme als Drittschuldnerin scheitert daran, dass nicht sie, sondern die Wiener GmbH Vertragspartnerin ist. Ein PfUEB an die deutsche Tochter waere unwirksam (es fehlt der "Anspruch des Schuldners gegen die Drittschuldnerin"). Nicht weiterverfolgen.

### Variante 2 - PfUEB an Bitpanda Wien, Zustellung nach EU-Zustellungs-VO

Beim Vollstreckungsgericht AG Krefeld einen PfUEB beantragen, Drittschuldnerin Bitpanda GmbH Wien. Zustellung nach EU-Zustellungs-VO 2020/1784: das deutsche Vollstreckungsgericht ist Uebermittlungsbehoerde; Empfangsbehoerde in Oesterreich ist regelmaessig das Bezirksgericht am Sitz der Drittschuldnerin (BG Innere Stadt Wien). Zeitfenster ca. 6-12 Wochen.

Vorteil: Forderung wird gepfaendet einschliesslich aller Coins und Fiat.
Nachteil: bis zur Zustellung kann der Schuldner umbuchen.

### Variante 3 - Europaeische Kontenpfaendung (EuKtPVO 655/2014)

EuKtPVO ist zugeschnitten auf Bankkonten. Bitpanda ist Krypto-Verwahrer, nicht Bank im Sinne des Art. 4 Nr. 2 EuKtPVO (Kreditinstitut nach RL 2013/36/EU). Daher fuer Krypto-Bestaende nicht einschlaegig. Fuer die 22.000 EUR Fiat-Guthaben *koennte* es greifen, soweit Bitpanda ueber Partnerbank eine Zahlungsdienstleistung im Sinne der EuKtPVO erbringt - der Streit ist offen. **Pragmatisch: Variante 2 + nationaler Eilantrag** in Oesterreich (Sicherheitsverfuegung Paragraf 379 oest. EO) als parallelen Sicherungsschritt durch oesterreichischen Korrespondenzanwalt.

## Empfohlene Mechanik (Variante 2 plus Begleitmassnahmen)

1. PfUEB-Antrag AG Krefeld - Drittschuldnerin Bitpanda GmbH, Wien.
2. Pfaendungsgegenstand: gesamter gegenwaertiger Bestand und kuenftige Eingaenge auf der Kundenbeziehung 5598-77821-MUE (BTC, USDC, EUR Fiat, alle weiteren Vermoegenswerte).
3. Hilfsweise Umrechnung in EUR zum jeweiligen Tageskurs nach Aufforderung der Glaeubigerin.
4. Zustellung nach EU-Zustellungs-VO 2020/1784 ueber das Vollstreckungsgericht.
5. **Begleitend**: oesterreichischer Korrespondenzanwalt schickt Vorabinformation an Bitpanda und beantragt Sicherheitsverfuegung Paragraf 379 oest. EO (10 Tage).
6. Erklaerung Paragraf 840 ZPO: deutsche Bitpanda-Asset-Management-GmbH soll Auskunft geben - das ist aber freiwillig.

## Erloes und Risiken

| Position | Wert / Risiko |
| --- | --- |
| Marktwert per 22.4.2026 | rd. 42.000 EUR |
| Volatilitaetsrisiko BTC/USDC | 15-25 Prozent |
| Zeitrisiko Zustellung Wien | 6-12 Wochen, in denen der Schuldner abziehen koennte |
| Geldwaesche-Vermerk | bei Auszahlung an die Glaeubigerin wird Bitpanda KYC/AML-Pruefung wiederholen |

## Zeitschiene

| Datum | Schritt |
| --- | --- |
| 27.5.2026 | PfUEB-Antrag AG Krefeld + Eilantrag Wien |
| 5.6.2026 | EuKtPVO-Pruefung verworfen, Variante 2 final |
| 10.7.2026 | Zustellung Bitpanda nach EU-Zustellungs-VO |
| 24.7.2026 | Drittschuldnererklaerung |
| 31.7.2026 | Auszahlung EUR-Erloes auf Verfahrenskonto |
