import psutil
import distro
import subprocess

def Say(w):
    w = 'spd-say -o rhvoice --wait "' + w + '"'
    subprocess.Popen(w, shell=True)

def Cpu():
    cpu_logic = psutil.cpu_count()
    cpu_core = psutil.cpu_count(logical=False)
    cpu_disp = psutil.cpu_times_percent(interval=1).idle
    cpu_freq = round(psutil.cpu_freq().max/1000, 1)
    res = f"O processador possui um total de {cpu_core} núcleos físicos e {cpu_logic} núcloes lógicos com frequência máxima de {cpu_freq} gigahertz, sua utilização total é de {round(100-cpu_disp, 2)} porcento"
    print(res)
    res = res.replace(".", " vírgula ")
    return res

def Ram():
    ram_total = round((psutil.virtual_memory().total)/(1024*1024*1024))
    ram_percent = psutil.virtual_memory().percent
    res = f"O sistema possui um total de {ram_total} Gigabyte de memória RAM, e está utilizando um total de {ram_percent} porcento desta memória"
    print(res)
    res = res.replace(".", " vírgula ")
    return res

def Linux():
    dis = distro.linux_distribution(full_distribution_name=False)
    res = f"O sistema operacional deste computador se chama {dis[0]} e está na versão {dis[1]}"
    print(res)
    res = res.replace(".", " ponto ")
    return res

if __name__ == '__main__':
    Linux()