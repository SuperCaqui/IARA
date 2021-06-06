import socket
import time

def Luz(data):
	host = socket.gethostname()   # get local machine name
	print('Host:', host)
	port = 8080  # Make sure it's within the > 1024 $$ <65535 range

	s = socket.socket()
	s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)	
	s.bind(('', port))
  	
	s.listen(1)
	print('Ouvindo...')

	client_socket, adress = s.accept()
	client_socket2, adress2 = s.accept()
	time.sleep(0.5)
	print("Conexão de: " + str(adress))
	print('client_socket: ', client_socket)
	print("Conexão de: " + str(adress2))
	print('client_socket: ', client_socket2)

	data = data.upper()
	data = data + '\r'
	print('Enviando...')
	client_socket.send(data.encode('utf-8'))
	client_socket2.send(data.encode('utf-8'))
	print('Encerrando conexão')
	client_socket.close()
	client_socket2.close()


if __name__ == '__main__':
	Luz("4")
