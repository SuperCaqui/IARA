import socket
from wakeonlan import send_magic_packet
from config import Config

def Wake():
    print("Enviando pacote")
    mac = Config.mac.rstrip("\n")
    send_magic_packet(mac, ip_address='192.168.0.255',  port=9)

def Shut(n):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(3)
    ip = Config.ip.rstrip("\n")
    s.connect((ip, 1234))
    s.send(bytes(n, "utf-8"))
    s.close()

if __name__ == '__main__':
    Shut("0")