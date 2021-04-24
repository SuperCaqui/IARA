class Config:
    f = open("config.txt", "r")

    name = f.readline()
    pronoum = f.readline()
    mac = f.readline()
    ip = f.readline()
    bot_api = f.readline()
    clima_api = f.readline()
    dormir = f.readline()
