import socket
from time import time
from checksum import *

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
		print('Digite uma mensagem para enviar ao servidor')
		msg = input()
		while msg != '\x18':
			bits = check(msg)
			bits = bits.encode('utf8')
			self.cliente.send(bits)
			msg = input()
		self.cliente.close()

cli = Cliente()
cli.cria_cliente()
cli.conecta()
cli.enviar()
