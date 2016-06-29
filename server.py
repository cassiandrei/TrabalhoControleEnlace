import socket
from checksum import *

class Server:

	HOST = ''
	PORT = 5000

	def cria_server(self):
		self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	def receber(self):
		self.server.bind((self.HOST,self.PORT))
		self.server.listen(1)
		while True:
			print('Esperando conexao')
			conexao, cliente = self.server.accept()
			print('Conectado por ', cliente)
			while True:
				msg = conexao.recv(1024)
				if not msg: break
				if correcao(msg):
					print("Mensagem recebida sem erros!")
				else:
					break
				print(cliente, 'Enviou a mensagem: ', msg)
			print('Fim da conexao com cliente: ', cliente)
			conexao.close()

serv = Server()
serv.cria_server()
serv.receber()
