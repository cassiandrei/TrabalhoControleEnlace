import socket
from checksum import *

class Server:

	HOST = ''
	PORT = 5555

	def cria_server(self):
		self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	def receber(self):
		self.server.bind((self.HOST,self.PORT))
		self.server.listen(5)
		while True:
			print('Esperando conexao')
			self.conexao, self.cliente = self.server.accept()
			print('Conectado por ', self.cliente)
			while True:
				msg = self.conexao.recv(2048)
				if correcao(msg):
					print("Frame verificado com sucesso")
					msg = '0'
					#msg = msg.decode('utf8')
					self.conexao.send(str.encode(msg))
				else:
					print("Frame: com erro")
					msg = "1"
					#msg = msg.decode('utf8')
					self.conexao.send(str.encode(msg))

			print('Fim da conexao com cliente: ', self.cliente)
			self.conexao.close()

serv = Server()
serv.cria_server()
serv.receber()
