import socket
from time import time
from checksum import *
from random import choice

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
			ruido = choice([0,1])
			if ruido == 1:
				print("RUIDO")
				pos=choice([0,len(bits)-1])
				if bits[pos]=='1':
					bits = bits[:pos-1] + "01" + bits[pos:]
				else:
					bits = bits[:pos-1] + "10" + bits[pos:]
			bits = bits.encode('utf8')
			self.cliente.send(bits)
			msg = input()
		self.cliente.close()

cli = Cliente()
cli.cria_cliente()
cli.conecta()
cli.enviar()
