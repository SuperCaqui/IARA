from datetime import date, time, datetime
import locale
import subprocess

locale.setlocale(locale.LC_TIME, "pt_BR.utf8")

def Say(w):
    w = 'spd-say "' + w + '"'
    subprocess.Popen(w, shell=True)

def Dia():
    hoje = date.today()
    # Textual month, day and year	
    dia = hoje.strftime("hoje é dia %d de %B de %Y")
    print(dia)
    
    #engine.say(dia)
    #engine.runAndWait()
    return dia

def Horas():
    agora = datetime.now()
    horas = agora.strftime("%H horas")
    if horas[0] in  ['0']:
        horas = horas[1:]
    horas = "São " + horas
    horas2 = agora.strftime("%M minutos")
    if horas2[0] in  ['0']:
        horas2 = horas2[1:]
    if horas2[0] not in ['0']:
        horas += " e " + horas2
    print(horas)

    #engine.say(horas)
    #engine.runAndWait()
    return horas

if __name__ == '__main__':
    s = Horas()
    Say(s)
