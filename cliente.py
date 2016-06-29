import socket
from time import time
import checksum

class Cliente:

	HOST = ''
	PORT = 5000


	def cria_cliente(self):
		self.cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	def conecta(self):
		#try:
		self.cliente.connect((self.HOST, self.PORT))
		print('Conexao criada com sucesso')
		#except ConnectRefusedError:
		#print("Nao foi possivel fazer a conexão")
		#self.cliente.settimeout(3)

	def enviar(self):
		#funcao CRC,CHECKSUM CASSIANO
		print('Digite uma mensagem para enviar ao servidor')
		msg = input()
		msg = msg.encode('utf8')
		while msg != '\x18':
			#oi
			checksum(msg)
			self.cliente.send(msg)
			msg = input()
			msg = msg.encode('utf8')
		self.cliente.close()	

	def receber(self):
		#funcao de checagem 
		self.cliente.recv(min())

cli = Cliente()
cli.cria_cliente()
cli.conecta()
cli.enviar()
