import socket
from wakeonlan import send_magic_packet
from config import Config

def Wake():
    print("Enviando pacote")
    send_magic_packet(Config.mac, ip_address='192.168.0.255',  port=9)

def Shut(n):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(3)
    s.connect(("192.168.0.22", 1234))
    s.send(bytes(n, "utf-8"))
    s.close()