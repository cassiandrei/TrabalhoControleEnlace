import socket
from time import time
from checksum import *
from random import choice

class Cliente:

	HOST = ''
	PORT = 5555


	def cria_cliente(self):
		self.cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	def conecta(self):
		self.cliente.connect((self.HOST, self.PORT))
		print('Conexao criada com sucesso')

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
			self.cliente.settimeout(5)
			msg = self.cliente.recv(2048)
			msg = msg.decode('utf8')
			print("Mensagem recebida: " + msg)
			msg = input()
		self.cliente.close()

cli = Cliente()
cli.cria_cliente()
cli.conecta()
cli.enviar()
