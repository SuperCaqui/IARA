I.A.R.A. Se trata de uma assistente virtual para automação residencial paraense, a qual deve ser executada via NOHUP em um servidor Linux a base de Debian.

Para executar a assistente virtual I.A.R.A. é preciso primeiramente executar o script de instalação "install.sh" a fim de instalar todas as suas dependências.

Depois é preciso editar o arquivo de configuração "config.txt" a fim de adicionar as suas configurações pessoais:

1 - a configuração de mopdo permite que você defina a necessidade de uma resposta inicial [1] ou que o acionamento seja mais direto [0]
2 - Nome do usuário
3 - Pronome de tratamentop prefrido pelo usuário
4 - Endereço MAC da máquina que será ligada por protocolo wake on lan
5 - IP da mesma máquina
6 - Token do bot do telegram a ser utilizado
7 - Token do sistema accuweather
8 - horário de desligamento automático da luz e computador
