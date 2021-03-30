#!/bin/bash

echo "Este batch tem por objetivo preparar o sistema para o funcionamento da assistente virtual iara"
if [ "$EUID" -ne 0 ]
    then echo "Execute o arquivo como root"
    exit
fi
cd
apt update -y
apt upgrade -y
apt install -y python3
apt install -y python3-pip
apt install -y git
apt install -y samba-common
apt install -y wget
apt install -y sox
apt install -y swig
apt install -y portaudio19-dev
apt install -y libatlas-base-dev
wget https://www.dropbox.com/s/51aq1vequ9odsi1/rhvoice-leticia-f123_4.6.5_amd64.deb
dpkg -i rhvoice-leticia-f123_4.6.5_amd64.deb
apt install -y -f
yes | pip3 install PyAudio
yes | pip3 install SpeechRecognition
yes | pip3 install pyttsx3
git clone https://github.com/seasalt-ai/snowboy.git .
cd snowboy/
yes | python3 setup.py install
cd
yes | pip3 install wikipedia
yes | pip3 install aiogram
yes | pip3 install wakeonlan
git clone https://github.com/SuperCaqui/IARA.git .
