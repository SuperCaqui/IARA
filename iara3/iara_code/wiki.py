import wikipedia
import subprocess

wikipedia.set_lang("pt")

def Say(w):
    w = 'spd-say --wait "' + w + '"'
    subprocess.Popen(w, shell=True)


def Wiki(p):
    s = wikipedia.summary(p, 1)
    print(s)

    #engine.say(s)
    #engine.runAndWait()
    #Say(s)
    return s

if __name__ == '__main__':
    s = Wiki("engenharia")
    Say(s)
