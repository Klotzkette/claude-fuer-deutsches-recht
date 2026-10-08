from pathlib import Path
import subprocess,json
root=Path('/tmp/kk338-unabhaengig-fach')
plugin=Path('/Users/klotzkette/Desktop/Codex Projects/legal-work/ki-kanzlei-glaettung-20261008/ki-native-kanzlei')
log=[]
def call(helper,*args):
 cmd=['python3',str(plugin/'scripts'/helper),*map(str,args)]
 p=subprocess.run(cmd,capture_output=True,text=True)
 log.append({'argv':cmd,'returncode':p.returncode,'stdout':p.stdout,'stderr':p.stderr})
 (root/'helferaufrufe.json').write_text(json.dumps(log,ensure_ascii=False,indent=2))
 if p.returncode: raise RuntimeError(p.stderr)
 return p.stdout
for n,person in [(1,'RAin Ada Ahrens'),(2,'RA Bertram Brecht')]:
 a=root/f'Fall{n}'
 inputs=a/'Eingaben';inputs.mkdir(exist_ok=True)
 data={'matter_id':f'FACH-{n}-20261008','client':'[GmbH, Firma noch offen]','subject':'Handaktenherausgabe und Cloudzugang' if n==1 else 'Honorarergänzung für neuen Lizenzvertragsentwurf'}
 f=inputs/'mandat.json';f.write_text(json.dumps(data,ensure_ascii=False,indent=2))
 call('kanzlei.py','init','--akte',a,'--data',f)
 call('mandatslauf.py','init','--akte',a,'--matter-id',data['matter_id'],'--stufe','2')
 call('mandatslauf.py','phase','--akte',a,'--phase','sacharbeit','--grund','Prüfvermerk und ausformulierter Entwurf im ausdrücklich beauftragten internen Probelauf erstellt.')
 products=[('berufsrechtsvermerk' if n==1 else 'honorarstand','Pruefvermerk.md','anwaltsberufsrecht-pruefen' if n==1 else 'honorar-budget-vereinbaren'),('mandantenbrief' if n==1 else 'vertrag','Antwortschreiben.md' if n==1 else 'Honorarergaenzung.md','mandantenkommunikation' if n==1 else 'honorar-budget-vereinbaren')]
 for pid,file,skill in products:
  call('mandatslauf.py','product','--akte',a,'--id',pid,'--pfad','01_Bearbeitung/'+file,'--skill',skill,'--zustand','entwurf')
 call('mandatslauf.py','phase','--akte',a,'--phase','kommunikation' if n==1 else 'abrechnung','--grund','Antwortentwurf und Berechtigungsprüfung offen.' if n==1 else 'Honorarergänzung ausgearbeitet; Parteienannahme offen.','--nebenlauf')
 for gate,pid,note in [('G1',products[0][0],'Übergang, Vollmacht und Mandantenentscheidung ungeklärt.' if n==1 else 'Auftragserweiterung und Honorarannahme noch zu bestätigen.'),('G3',products[1][0],'Es besteht kein Versandauftrag; Entwurf zur fachlichen Durchsicht.')]+([('G6',products[0][0],'Cloudvertrag, Empfängerrollen, Drittlandsupport und Unterauftragnehmer ungeklärt; kein Upload.')] if n==1 else []):
  call('mandatslauf.py','gate','--akte',a,'--gate',gate,'--aktion','oeffnen','--person',person,'--bezug',pid,'--notiz',note)
 irrelevant={'G2':'Es liegt kein konkreter Fristauslöser oder Rechenvermerk vor; Restfristenprüfung als offene Frage geführt.','G4':'Kein ausgabefähiger Rechnungsbetrag und kein Auftrag zur Rechnungsausgabe.','G5':'Keine Zahlung, Verrechnung oder Auszahlung beauftragt.','G7':'Kein konkreter Meldeanlass bekannt.','G8':'Mandatsende und Löschung sind nicht beauftragt und nicht festgestellt.'}
 if n==2: irrelevant['G6']='Für diesen internen Entwurf ist kein externer Aktenzugang beauftragt.'
 for gate,note in irrelevant.items():
  call('mandatslauf.py','gate','--akte',a,'--gate',gate,'--aktion','nicht-erforderlich','--person',person,'--notiz',note)
 questions=(['Wie lautet die verifizierte Erklärung der vertretungsberechtigten GmbH zu Übergang, Empfänger und Umfang; liegt die Empfangsvollmacht vor?','Welche Fristen und unentbehrlichen Unterlagen ergeben sich aus Originalakte und führendem Kalender?','Wer ist Cloudvertragspartner; welche Unterauftragnehmer, Zugriffsorte, Geheimnisschutzverträge und Drittlandmechanismen sind belegt?','Ist die offene Honorarnote der GmbH geschuldet, fällig und nach den Umständen zurückbehaltungsfähig?'] if n==1 else ['Wie lauten vollständige Ursprungsvereinbarung, Lizenzgegenstand, Vertragspartner und Vertretungsdaten?','Wurde die Monatsklausel als AGB gestellt oder tatsächlich ausgehandelt?','Wann haben beide Parteien welche endgültige Nachtragsfassung in Textform angenommen?','Welche Leistungen sind vor Annahme bereits erbracht und welche gesetzliche Gebührenbasis greift hierfür?'])+['Welche Honorargrundlage gilt für diese konkrete Prüfung; welche tatsächlichen anwaltlichen Minuten, Leistungsdaten und Abrechenbarkeit sind bestätigt?']
 for q in questions: call('mandatslauf.py','question','--akte',a,'--text',q)
 # Der Auftrag enthält keine bestätigte Dauer und keinen verifizierten Steuerfall.
 # Deshalb keine terms-, time-, manual-fee- oder payment-Buchung.
 call('kanzlei.py','draft','--akte',a)
 (a/'00_Mandat'/'journalstatus.txt').write_text(call('kanzlei.py','status','--akte',a))
 (a/'00_Mandat'/'laufstatus.txt').write_text(call('mandatslauf.py','status','--akte',a))
 (a/'00_Mandat'/'naechster_schritt.txt').write_text(call('mandatslauf.py','next','--akte',a))
 print(f'Fall{n}: Stufe 2, Produkte {len(products)}, Helferaufrufe erfolgreich.')
print(f'{len(log)} erfolgreiche Helferaufrufe protokolliert.')
