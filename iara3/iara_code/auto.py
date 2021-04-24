from datetime import date, time, datetime
import locale
import subprocess
import time
from config import Config
import pc
import luz

locale.setlocale(locale.LC_TIME, "pt_BR.utf8")

def Say(w):
    w = 'spd-say "' + w + '"'
    subprocess.Popen(w, shell=True)

dormir = Config.dormir
dormir = dormir.replace(':', '') + "00"

def Auto():
    print(f"Inicializando sistema automatico de desligamento para as {Config.dormir}")
    while True:
        agora = datetime.now()
        horas = agora.strftime("%H%M%S")
        #print(horas)
        time.sleep(1)
        if (horas == dormir):
            print("Desligamento automático acionado")
            pc.Shut("2")
            luz.Luz("2")


if __name__ == '__main__':
    Auto()