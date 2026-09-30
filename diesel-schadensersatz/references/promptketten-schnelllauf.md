# Promptketten-Schnelllauf

Verbindlicher Ausführungsvertrag für alle 21 Diesel-Skills. Er gilt modellneutral für Opus 5 und Fable 5: Tempo entsteht durch Auswahl, begrenzten Kontext und geprüfte Wiederverwendung, nie durch den Verlust von Tatsachen, Fundstellen, Fristen, Rechtsankern oder Stopps.

## 1. Laufprinzip

Jeder Lauf hat genau ein verantwortliches Arbeitsprodukt und genau einen federführenden Skill. Höchstens zwei wirklich unabhängige Vorprüfungen dürfen parallel laufen; abhängige Arbeit bleibt sequenziell. Bereits belegte Inhalte werden nicht neu hergeleitet. Eine Frage wird nur gestellt, wenn ohne ihre Antwort kein gekennzeichnetes Zwischenergebnis möglich ist.

Geladen werden nur:

1. dieser stabile Vertrag,
2. der aktive Skill,
3. der skillbezogene Arbeitsstand,
4. höchstens eine wirklich benötigte Fachreferenz.

Der Host begrenzt statischen Kontext auf 48.000 Bytes, den skillbezogenen `model_state` auf 48.000 Bytes, den Auftrag auf 4.000 Bytes und alles zusammen auf 100.000 Bytes. Der vollständige kanonische Zustand darf 512.000 Bytes umfassen und bleibt außerhalb des Providerkontexts erhalten.

### Verlustfreie Nachladung

Eine Projektion ist referenziell geschlossen: Ein sichtbares Gate, ein Blocker oder Konflikt wird zusammen mit allen referenzierten Fakten, Blockern, Konflikten und Rechtsankern geliefert. Passt das Bündel nicht, wird das ganze Objekt ausgelassen; es bleiben keine losen Basis-IDs.

Das Retrieval-Manifest bindet `fall_id`, Skill, kanonischen State-SHA-256, den Hash des vollständigen skillbezogenen Zustands sowie die ausgelassenen IDs. Nur die Host-Funktion `retrieve_state_items(fall_id, state_sha256, skill, item_type, ids)` darf aus exakt demselben aktuellen, nichtterminalen SQLite-Head nachladen. Sie prüft Hash, Payload, Skill-Scope, Typ, eindeutige IDs und Antwortgröße. Ist der Stand nicht publiziert oder inzwischen stale, stoppt der Modelllauf mit Publikations-Handoff. Ein Funktionsname oder Modelloutput allein ist keine Nachladung.

## 2. Laufprofile und Router

- `SCHNELL`: Intake, Sortierung, Beleglücken, einfache Rechnung, Korrespondenz und klarer Folgeauftrag.
- `TIEF`: Anspruchswahl, zweifelhafte Betroffenheit, Verjährung, tragende Rechtsprechung, Klage, Replik, Rechtsmittel oder erheblicher Vergleich.
- `VERSAND`: nur fachlich freigegebene Endfassung; Skill 21 baut das Paket, Skill 16 übermittelt es erst danach über eine privilegierte Produktionsschnittstelle.

Ein neuer oder ungeordneter Eingang startet mit Skill 01. Skill 02 klärt Vertrag, Zahlung und Belege; 03 Chronologie, Zugang und Fristen; 04 Fahrzeug, Motor, Rückruf und Maßnahme. Sind diese Punkte schon belastbar erfasst, startet der verlangte Fachskill direkt. Ein Rücksprung erfolgt nur, wenn die Lücke das Ergebnis tatsächlich ändern kann.

Skill 05 behandelt eine konkrete technische Einrichtung oder Updatefrage, 06 Anspruchstriage, 07 Verjährung/Hemmung, 08 Bezifferung. Die gerichtliche Kette bleibt `13 → 14|15 → 21 → 16`; nach Erwiderung folgt `17 → 21 → 16`. Titel/Kosten starten mit 19, Vergleich mit 18, Finanzierung mit 12, DMS-/E-Akte-Auftrag mit 20. Rote Gates bleiben in jedem Direkteinstieg wirksam.

Der ausdrücklich verlangte Fachskill wird nicht durch Stichwortsuche überschrieben. Negierte, zitierte, bedingte, vergangene oder nur vorbereitende Versandformulierungen öffnen niemals Skill 16. Freitext und Standalone-CLI autorisieren keine irreversible Handlung.

## 3. Kanonischer Arbeitsstand

Maschinenlesbare Stände erfüllen `assets/schemas/arbeitsstand.schema.json` (`schema_version=2.0.0`). Quelle der Wahrheit ist der feste SQLite-Runtime-Store des Hosts, nicht eine beliebig erneut gelesene Datei. Pro `fall_id` existiert genau ein Head mit exakten Payload-Bytes und SHA-256.

Revision 1 hat keinen Vorgänger. Ab Revision 2 müssen unmittelbare Vorgängerdatei, deren Byte-Hash, Revisionssprung, Fall-ID und `delta` exakt passen. Vor jeder Publikation parst der Host die tatsächlichen Bytes erneut, validiert vollständiges Schema und Vorgänger und führt dann ein kurzes Compare-and-Swap aus. Stimmen erwarteter und kanonischer Head nicht überein, wird nichts geschrieben. Ein terminaler Stand wird nie fortgesetzt.

Der Arbeitsstand bewahrt Fallkern, Tatsachen mit stabilen IDs und Fundstellen, Konflikte, bereichsbezogene Blocker, sieben Gates, Rechtsstand, Completion-Historie, Versandfreigabe, aktiven/nächsten Skill, Abschluss und Delta. Revisionen entfernen keine vorhandene Tatsache. `erledigte_skills` ist append-only; frühere Läufe werden weder geändert noch umgeordnet.

Ein Completion-Lauf enthält `skill`, eindeutige `run_id`, `supersedes`, `reuse_status`, Resultat-, Auftrags- und optionalen externen Eingabehash, `result_refs`, `completion_sha256`, Zeitstempel und gegebenenfalls Rechtsstanddatum. Der erste Lauf eines Skills setzt `supersedes=null`, jeder weitere zeigt auf dessen unmittelbar vorherigen Lauf. Der Host hängt genau einen Lauf an; Kandidat, Endstand und Vorgänger werden an der Commit-Grenze erneut aus ihren Bytes validiert und gemeinsam atomar publiziert. Nur Skill 21 darf dabei vor dem Append die reservierten Hostfelder `connector_namespace` und `action_id` von `null` auf ihre gebundenen Endwerte setzen.

`completion_sha256` ist der kanonische Objekthash aus Skill, Lauf-ID, Vorgänger-Lauf, Resultat-, Auftrags- und Eingabehash sowie Ergebnisreferenzen. Das Modell erfindet keine Prüfsumme. Ohne Hostprüfung bleibt `reuse_status=ausstehend` und die unbestätigten Hashes bleiben `null`.

Eine Ergebnisreferenz zeigt auf eine integrierte Fakten-ID oder ein vorhandenes Artefakt mit echtem SHA-256 und relativem, punktsegmentfreiem Pfad unter der expliziten Artefaktwurzel. Absolute Pfade, Traversal und Symlinks sind unzulässig. Dokumentproduzierende Skills benötigen ein Artefakt; eine DMS-ID allein ist kein prüfbarer Beleg.

Wiederverwendung ist nur zulässig, wenn Skill-State, normalisierter Auftrag, externer Eingabehash, Rechtsstand und alle Resultrefs erneut passen. Neue Datei, relevanter Widerspruch, geänderter Rechtsanker oder nicht auffindbares Artefakt öffnet einen neuen Lauf; der alte bleibt erhalten.

## 4. Fach- und Rechtsqualität

Tatsachenstatus lautet `belegt`, `streitig`, `offen` oder `verworfen`. Belegt ist nur, was eine prüfbare Fundstelle trägt. Konflikte werden nicht still aufgelöst. Gate-Status lautet `gruen`, `gelb`, `rot` oder `nicht_relevant`; ein grünes Gate braucht passende Basis-IDs. Blocker sperren nur ihren Scope.

Der lokale Rechtskorpus dient der Auswahl, nicht der automatischen Zitierfreigabe. Vor einer tragenden externen Aussage werden Volltext, Datum, Aktenzeichen, Randnummer, Entscheidungsstatus und Folgeentwicklung an amtlicher HTTPS-Quelle geprüft. Anhängige Verfahren sind keine Sachentscheidung. Der Arbeitsstand führt zusammen höchstens sechs Entscheidungs- und Normanker; jeder nennt `registry_id`, amtliche URL und `gilt_fuer_skills`. Für externe Skills ist ein Live-Prüfstand höchstens 45 Tage alt.

Ein Quellenpaket enthält höchstens zwei höchstrichterliche Anker, zwei technisch vergleichbare Instanzentscheidungen, eine erhebliche Gegenlinie und einen Statusanker. Neue Rechtsprechung ändert nur betroffene Anker und davon abhängige Gates, nicht die Falltatsachen.

Vor externer Verwendung wird die konkrete Fassung einmal vollständig geprüft: Fakten/Beträge/Daten/FIN/Anlagen, Norm und Rechtsprechung, Frist/Zuständigkeit/Antrag, stärkstes Gegenargument, Dokumentstand und Freigabe. Eine spätere Inhaltsänderung entwertet die betroffenen Prüfpunkte.

## 5. Versandgrenze

Skill 21 bindet ein freigegebenes Paket geschlossen an `status,paket_fingerprint_sha256,freigabe_revision,recipient_id,connector_namespace,action_id`. Der Host setzt `connector_namespace` ausschließlich als produktionsautorisierte Domäne `bea-egvp:prod:tenant`. Fall, Revision, Paket, Empfänger und Namespace fließen in die deterministische Action-ID ein. Test-, Sandbox-, andere Provider-, Umgebungs- oder Tenantgrenzen dürfen den Produktionspfad nicht öffnen.

Skill 16 verlangt zusätzlich explizites `confirm_submit`, positiven tatsächlichen Versandauftrag, aktuellen kanonischen Head und einen vom Host injizierten Dispatcher sowie Receipt-Verifier. Beide melden denselben Namespace und `production_authorized=true`; eine Stringbehauptung `prod` allein genügt nicht.

Der Host reserviert die Action-ID einmalig im selben Runtime-Store. Phasen sind `reserved → executing → completed` oder vor jeder Ausführung `reserved → cancelled`. Während `reserved`/`executing` bleibt der Fall-Head eingefroren. Stornierung braucht eine außerhalb der Schreibtransaktion eingeholte, an Action-ID und Claim-Hash gebundene menschliche Autorisierung; danach prüft eine kurze Transaktion, dass der Claim noch unverändert `reserved` ist. `executing` wird nie lokal freigegeben.

Nach Absturz fragt der Host zuerst dieselbe Action-ID beim identischen Connector ab. `submitted` wird versöhnt, `unknown` blockiert. Nur autoritatives `not_found` erlaubt nach erneuter kurzer Prüfung von Claim, Phase, Namespace und unverändertem Head einen idempotenten Retry. Paket-, Empfänger- oder Namespacewechsel geht zurück an Skill 21 und erzeugt eine neue Action-ID.

Ein Skill-16-Abschluss braucht zwei gehashte Artefakte: unveränderten Originalbeleg des beA-/EGVP-Connectors und signierte Connector-Attestierung. Diese bindet geschlossen `schema_version,status,action_type,action_id,package_sha256,recipient_id,submitted_at,issuer,audience,key_id,connector_namespace,source_receipt_sha256,attestation_signature`; Status `eingereicht`, Typ `gerichtliche_einreichung`, Originalbeleg-Hash, Namespace und Action-ID müssen exakt passen. Nur der produktionsautorisierte injizierte Vertrauensanker prüft die Signatur. Lokale JSON-Datei, selbst behaupteter Receipt oder CLI-Flag ist kein Eingangsbeweis; der Status bleibt `EINGANG_UNGEKLAERT`.

## 6. Verständliche Ausgabe

Die erste Aussage nennt Ergebnis oder konkreten Engpass. Danach folgen ausformuliertes Arbeitsprodukt, wesentliche Belege, Gegenargument/Risiko und genau ein nächster Schritt. Keine interne Gedankenkette, Pfeilgerippe, Platzhalterprosa oder wiederholte generische Selbstkontrolle.

Tabellen sind kein Standard. Sie werden nur bei mindestens drei vergleichbaren, wirklich befüllten Körperzeilen verwendet, etwa für Zahlungen, Fristen, Schadensrechnung, Einwendungen oder Anlagen. Kopf- und Trennzeile zählen nicht. Ein einzelner Befund, eine Fallbeschreibung und rechtliche Würdigung gehören in vollständige Absätze oder kurze Listen.

Eine Textübergabe nennt Ziel, Fallkern, belegte/streitige/offene Tatsachen mit IDs und Fundstellen, Konflikte und Gates, verifizierte Rechtsanker, neue Erkenntnisse sowie genau einen aktiven oder nächsten Skill. Sie darf Formulierungen kürzen, aber nie IDs, Fundstellen, Beträge, Daten, FIN, Fristen, Konflikte, Gate-Status, Entscheidungsstatus oder Verwendungsgrenzen entfernen.

Opus 5 erhält keine generischen Doppelprüfungen. Fable 5 wird ausdrücklich auf vorhandene Belege, begrenzten Scope und den einen nächsten Schritt festgelegt. Beide erhalten vollständige Sätze, denselben fachlichen Zustand und dieselben Stopps.
