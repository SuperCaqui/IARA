#!/usr/bin/env python3

import speech_recognition as sr
import subprocess
import sys
import time
import random

import dia_e_hora
import wiki
import luz
from config import Config
import pc

random.seed()

r = sr.Recognizer()

art = ['o', 'a', 'os', 'as', 'um', 'uma', 'uns', 'umas'] # lista de artigos a serem ignorados


def Say(w):
    w = 'spd-say -o rhvoice --wait "' + w + '"'
    subprocess.Popen(w, shell=True)

def Say2(w):
    w = 'spd-say -o rhvoice --wait "' + w + '"'
    subprocess.call(w, shell=True)


def Recog():
    rand = random.randrange(6)
    if rand == 0:
        chan = "Pode dizer"
    elif rand == 1:
        chan = "Diga"
    elif rand == 2:
        chan = "Sim"
    elif rand == 3:
        chan = "O que deseja?"
    elif rand == 4:
        chan = "Sou todo ouvidos"
    elif rand == 5:
        chan = "Estou ouvindo"
    rand = random.randrange(2)
    if rand == 0:
        chan += "," + Config.pronoum + Config.name
    Say2(chan)
    with sr.Microphone() as source:
        #r.adjust_for_ambient_noise(source)
        
        print("Diga algo")
        try:
            audio = r.listen(source, timeout=5)

        except:
            err = "Não entendi"
            print(err)
            Say(err)

    fr = ""
    try:
        fr=r.recognize_google(audio, language="pt-BR") # variável onde é armazenada a frase dita
        fr = fr.lower()
        print("frase: ", fr)
        resul = Faz(fr)
    except:
        resul = "Não entendi"
        print(resul)
    Say(resul)





def Faz(fr):

    res = ""
    l = fr.split() #lista de palavras ditas
    print(l)
    print(len(l))
    l = [i for i in l if i not in art]
    print(l)
    for x in range(0, len(l)):
        print(x, l[x])
        if l[x] in ['horas', 'hora']:
            res = dia_e_hora.Horas()
            break
        elif l[x] in ['data', 'dia'] and not l[x-1] in ['bom']:
            res = dia_e_hora.Dia()
            break
        elif l[x] in ['que', 'quem']:
            if l[x+1] in ['é', 'seria', 'foi']:
                res = wiki.Wiki(l[x+2])
                break
        elif l[x] in ['ligar', 'acender', 'acenda', 'ligue', 'liga', 'acende']:
            if l[x+1] in ['luz', 'luzes', 'lâmpada']:
                res = "Ligando a luz"
                luz.Luz("1")
                break
            elif l[x+1] in ['computador']:
                res = "Ligando o computador"
                pc.Wake()
                break
        elif l[x] in ['desligar', 'desligue', 'apague', 'apagar', 'desliga', 'apaga']:
            if l[x+1] in ['luz', 'luzes', 'lâmpada']:
                res = "Desligando a luz"
                print(res)
                luz.Luz("0")
                break
            elif l[x+1] in ['computador']:
                try:
                    res = "Desligando o computador"
                    print(res)
                    pc.Shut("1")
                except:
                    res = "Impossível conectar"
                    print(res)
                break
            elif l[x+1] in ['sistema']:
                Say("Desligando")
                #sys.exit(0)
                break
        elif l[x] in ['diga', 'repita']:
            fr2 = fr.split(' ', 1)[1]
            Say(fr2)
            res = "Dizendo: " + fr2
            break
        elif l[x] in ['nome', 'nome?']:
            res = "Eu sou Iara, assistente virtual Paraense criada por Gabriel Melém"
            print(res)
            break
        elif l[x] in ['cancelar']:
            try:
                res = "Cancelando desligamento"
                print(res)
                pc.Shut("3")
            except:
                res = "Impossível conectar"
                print(res)
            break
        else:
            res = "Não entendi"
    return res


if __name__ == '__main__':
	Recog()