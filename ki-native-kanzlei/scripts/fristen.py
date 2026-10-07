#!/usr/bin/env python3
"""Nachvollziehbare Kalenderrechnung nach ausdrücklich gewähltem Rechtsprofil.

Keine automatische Rechtswahl, Zugangsfiktion, Hemmung, Feiertagsrecherche oder
Kalendersynchronisation. Python >=3.10, nur Standardbibliothek.
"""
import argparse,calendar,hashlib,json,re,sys
from datetime import date,datetime,time,timedelta,timezone
from pathlib import Path
from zoneinfo import ZoneInfo,ZoneInfoNotFoundError


def text(obj,key):
    v=obj.get(key)
    if not isinstance(v,str) or not v.strip() or any(ord(c)<32 for c in v):
        raise ValueError(f'{key}: eindeutiger einzeiliger Text erforderlich')
    return v


def day(value):
    if not isinstance(value,str) or not re.fullmatch(r'\d{4}-\d{2}-\d{2}',value):
        raise ValueError('Datum muss YYYY-MM-DD sein')
    return date.fromisoformat(value)


def integer(value,label,maximum=36600):
    if type(value) is not int or not 1<=value<=maximum:
        raise ValueError(f'{label}: ganze Zahl von 1 bis {maximum} erforderlich')
    return value


class CourtCalendar:
    """Bereitgestellte Feiertage; das Programm prüft keine Kalender-Vollständigkeit."""
    def __init__(self,data):
        if set(data)-{'place','source','valid_from','valid_to','verified','holidays'}:raise ValueError('Nicht unterstützte Kalenderfelder')
        self.place=text(data,'place');self.source=text(data,'source')
        self.first=day(text(data,'valid_from'));self.last=day(text(data,'valid_to'))
        if self.first>self.last:raise ValueError('Kalenderzeitraum widersprüchlich')
        if data.get('verified') is not True:raise ValueError('Kalender muss für Ort und Zeitraum ausdrücklich geprüft sein')
        self.holidays={}
        if not isinstance(data.get('holidays'),list):raise ValueError('holidays: explizite Liste erforderlich')
        for row in data['holidays']:
            if not isinstance(row,dict) or set(row)!={'date','name'}:raise ValueError('Feiertag benötigt genau date und name')
            d=day(text(row,'date'));name=text(row,'name');self.check(d)
            if d in self.holidays:raise ValueError('Doppeltes Feiertagsdatum')
            self.holidays[d]=name

    def check(self,d):
        if not self.first<=d<=self.last:raise ValueError(f'Kalender deckt {d} nicht ab; weiteren Zeitraum amtlich prüfen')

    def reason(self,d,weekdays=(0,1,2,3,4)):
        self.check(d)
        if d in self.holidays:return self.holidays[d]
        if d.weekday() not in weekdays:return ['Montag','Dienstag','Mittwoch','Donnerstag','Freitag','Samstag','Sonntag'][d.weekday()]
        return None


def month_end(trigger,months,beginning):
    """§188 II/III: fehlender maßgebender Endtag -> letzter Tag, nicht vorletzter."""
    index=trigger.year*12+trigger.month-1+months
    year,month=divmod(index,12);month+=1
    if not 1<=year<=9999:raise ValueError('Enddatum außerhalb unterstützter Jahre')
    last=calendar.monthrange(year,month)[1]
    if trigger.day>last:
        return date(year,month,last),'Maßgebender Tag fehlt im Endmonat: letzter Kalendertag (§188 Absatz3 BGB bei gewählter Anwendbarkeit)'
    end=date(year,month,trigger.day)
    if beginning:end-=timedelta(days=1)
    return end,'Kalenderdatum des Endmonats; bei Anfangsfrist dessen Vortag'


def aware(raw,zone):
    text({'timestamp':raw},'timestamp')
    value=datetime.fromisoformat(raw)
    if value.tzinfo is None or value.utcoffset() is None:raise ValueError('Stundenfrist benötigt ISO-Zeitstempel mit explizitem UTC-Offset')
    local=value.astimezone(zone)
    if local.replace(tzinfo=None)!=value.replace(tzinfo=None) or local.utcoffset()!=value.utcoffset():
        raise ValueError('Zeitpunkt/Offset passt nicht zur angegebenen Zeitzone (Sommerzeit prüfen)')
    return local


def hours_end(trigger,amount,rule,cal,zone,trace):
    cursor=trigger.astimezone(timezone.utc);remaining=amount*3600
    if rule=='elapsed':
        end=(cursor+timedelta(seconds=remaining)).astimezone(zone)
        d=trigger.date()
        while d<=end.date():cal.check(d);d+=timedelta(days=1)
        trace.append('Reale verstrichene Stunden in UTC gerechnet; Wochenenden/Feiertage laufen mit')
        return end
    if rule!='exclude_nonworking_days':raise ValueError('hour_rule: elapsed oder exclude_nonworking_days erforderlich')
    while remaining:
        local=cursor.astimezone(zone);d=local.date();reason=cal.reason(d)
        boundary=datetime.combine(d+timedelta(days=1),time.min,zone).astimezone(timezone.utc)
        if reason:
            trace.append(f'{d}: {reason} bei gewählter Stundenregel nicht mitgerechnet');cursor=boundary;continue
        available=int((boundary-cursor).total_seconds())
        used=min(available,remaining);cursor+=timedelta(seconds=used);remaining-=used
    end=cursor.astimezone(zone)
    # Midnight exactly is the boundary at the end of the preceding counted day.
    cal.check(end.date() if end.timetz().replace(tzinfo=None)!=time.min else end.date()-timedelta(days=1))
    trace.append('Nur Zeitanteile der ausdrücklich zugelassenen Tage gezählt; 00:00 ist die Grenze zum Folgetag')
    return end


def calculate(data):
    if not isinstance(data,dict):raise ValueError('Eingabe muss ein Objekt sein')
    if type(data.get('schema_version')) is not int or data.get('schema_version')!=1:raise ValueError('schema_version=1 erforderlich')
    if not isinstance(data.get('profile'),dict) or not isinstance(data.get('calendar'),dict):raise ValueError('profile und calendar erforderlich')
    for forbidden in ('suspensions','restart','service_presumption','appeal_type'):
        if forbidden in data:raise ValueError(f'{forbidden}: rechtlicher Sonderfall ist nicht automatisch implementiert; eigenes Profil/gesonderte Berechnung')
    extra=set(data)-{'schema_version','matter_id','profile','calendar'}
    if extra:raise ValueError('Nicht unterstützte Eingabefelder: '+', '.join(sorted(extra)))
    p=data['profile'];case=text(data,'matter_id');norm=text(p,'norm');source=text(p,'rule_source');evidence=text(p,'trigger_source')
    if p.get('rule_verified') is not True:raise ValueError('Rechtswahl muss vor der Rechnung ausdrücklich geprüft sein')
    cal=CourtCalendar(data['calendar']);mode=text(p,'mode');adjust=text(p,'end_adjustment');adjustment_norm=text(p,'adjustment_basis')
    if adjust not in ('none','next_working_day'):raise ValueError('end_adjustment: none oder next_working_day erforderlich')
    common={'norm','rule_source','trigger_source','rule_verified','mode','trigger','end_adjustment','adjustment_basis'}
    if mode in ('event','start'):
        allowed=common|{'amount','unit'}
        if p.get('unit')=='working_days':allowed|={'weekdays','working_day_definition'}
    elif mode=='hours':allowed=common|{'amount','zone','hour_rule'}
    else:allowed=common
    if set(p)-allowed:raise ValueError('Nicht unterstützte Profilfelder: '+', '.join(sorted(set(p)-allowed)))
    trace=[f'Rechtsprofil: {norm}; Quelle: {source}',f'Auslöserbeleg: {evidence}',f'Kalenderort: {cal.place}; Quelle: {cal.source}']
    movement=[]
    result={'matter_id':case,'legal_rule':norm,'rule_source':source,'trigger_source':evidence,
            'calendar_place':cal.place,'calendar_source':cal.source,'calendar_verified_by_input':True,
            'status':'Kalenderrechnung aus vorgegebenem Rechtsprofil; rechtliche Endkontrolle bleibt erforderlich',
            'calendar_written':False,'reminder_created':False}
    if mode=='hours':
        if adjust!='none':raise ValueError('Stundenfristen verwenden hour_rule, keine zusätzliche pauschale Tagesverschiebung')
        try:zone=ZoneInfo(text(p,'zone'))
        except ZoneInfoNotFoundError as e:raise ValueError('IANA-Zeitzone fehlt im System') from e
        start=aware(text(p,'trigger'),zone);cal.check(start.date());amount=integer(p.get('amount'),'amount',87840)
        end=hours_end(start,amount,text(p,'hour_rule'),cal,zone,trace)
        result.update(begin=start.isoformat(),unadjusted_end=end.isoformat(),end=end.isoformat(),end_boundary='exakter Zeitpunkt')
    else:
        if mode not in ('event','start','fixed'):raise ValueError('mode: event, start, fixed oder hours erforderlich')
        trigger=day(text(p,'trigger'));cal.check(trigger);begin=trigger+timedelta(days=1) if mode=='event' else trigger
        if mode=='fixed':
            raw=trigger;trace.append('Festes Datum unmittelbar aus Vorgabe übernommen; keine Zugangsfiktion gerechnet')
        else:
            amount=integer(p.get('amount'),'amount');unit=text(p,'unit')
            trace.append(f'{mode}: Auslösertag {trigger}; rechnerischer erster Tag {begin}')
            if unit=='days':raw=trigger+timedelta(days=amount-(mode=='start'))
            elif unit=='weeks':raw=trigger+timedelta(days=amount*7-(mode=='start'))
            elif unit in ('months','years'):
                raw,note=month_end(trigger,amount*(12 if unit=='years' else 1),mode=='start');trace.append(note)
            elif unit=='working_days':
                weekdays=p.get('weekdays');text(p,'working_day_definition')
                if not isinstance(weekdays,list) or not weekdays or any(type(d)is not int or d not in range(7) for d in weekdays) or len(set(weekdays))!=len(weekdays):
                    raise ValueError('weekdays: eindeutige erlaubte Wochentage als 0=Montag bis6=Sonntag erforderlich')
                raw=begin;count=0
                while count<amount:
                    reason=cal.reason(raw,weekdays)
                    if not reason:count+=1
                    else:trace.append(f'{raw}: {reason} nicht als definierter Werktag gezählt')
                    if count<amount:raw+=timedelta(days=1)
            else:raise ValueError('unit: days, weeks, months, years oder working_days erforderlich')
        cal.check(raw);end=raw
        if adjust=='next_working_day':
            while (reason:=cal.reason(end)):
                movement.append({'date':end.isoformat(),'reason':reason});end+=timedelta(days=1)
            trace.append(f'Endverschiebung aufgrund {adjustment_norm}: {len(movement)} Tag(e)')
        else:trace.append(f'Keine Endverschiebung: {adjustment_norm}')
        result.update(begin=begin.isoformat(),unadjusted_end=raw.isoformat(),end=end.isoformat(),end_boundary='Ablauf dieses Tages (24:00), soweit das vorgegebene Rechtsprofil dies trägt')
    result['shifted_days']=movement;result['steps']=trace
    result['input_sha256']=hashlib.sha256(json.dumps(data,ensure_ascii=False,sort_keys=True,separators=(',',':'),allow_nan=False).encode()).hexdigest()
    return result


def markdown(r):
    lines=['# Fristenberechnung', '',f"Mandat: {r['matter_id']}", '',f"**Errechnetes Ende: {r['end']}** – {r['end_boundary']}", '',r['status'],'', '## 1. Grundlage','',f"Norm: {r['legal_rule']}",f"Normquelle: {r['rule_source']}",f"Auslöser: {r['trigger_source']}",f"Kalender: {r['calendar_place']} – {r['calendar_source']}", '', '## 2. Rechenschritte','']
    lines += [f'{i}. {s}' for i,s in enumerate(r['steps'],1)]
    lines += ['', '## 3. Ergebnis und Kontrolle','',f"Beginn: {r['begin']}. Unverschobenes Ende: {r['unadjusted_end']}. Ergebnis: {r['end']}.", 'Zugang, Rechtswahl, örtliche Kalender-Vollständigkeit, zulässigen Übermittlungsweg und Sonderregeln vor Übernahme in den Kanzleikalender unabhängig kontrollieren. Keine Kalendereintragung oder Erinnerung wurde ausgelöst.', '',f"Eingabe-SHA256: {r['input_sha256']}",'']
    return '\n'.join(lines)


def main():
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--data',required=True,type=Path);parser.add_argument('--out',type=Path)
    args=parser.parse_args()
    try:
        data=json.loads(args.data.read_text());result=calculate(data)
        if args.out:
            # Each calculation is a new immutable output directory; never overwrite a prior deadline.
            args.out.mkdir(parents=True,exist_ok=False)
            (args.out/'fristenvermerk.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
            (args.out/'fristenvermerk.md').write_text(markdown(result))
        print(json.dumps(result,ensure_ascii=False,indent=2));return 0
    except (ValueError,KeyError,TypeError,OverflowError,OSError) as e:
        print(f'Fristenrechnung abgebrochen: {e}',file=sys.stderr);return 2
if __name__=='__main__':raise SystemExit(main())
