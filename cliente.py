import socket
from time import time
from checksum import *
from random import choice

class Cliente:

	HOST = ''
	PORT = 5554


	def cria_cliente(self):
		self.cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	def conecta(self):
		self.cliente.connect((self.HOST, self.PORT))
		print('Conexao criada com sucesso')

	def enviar(self):
		while(1):
			print('Digite uma mensagem para enviar ao servidor')
			msg = input()
			texto = msg
			cont = 0
			frame = ""
			salvo = []
			while len(texto)>0:
				#listframes = texto[:4]

				frame = texto[:1]
				texto = texto[1:]
				ruido = choice([0,1])
				salvo.append(frame)
				if ruido == 1:
					print("RUIDO em frame: ", cont)
					pos=choice([0,len(frame)-1])
					if frame[pos]=='1':
						frame = frame[:pos-1] + "0" + frame[pos:]
					else:
						frame = frame[:pos-1] + "1" + frame[pos:]
				#envia check(frame)
				bits = check(frame)
				bits = bits.encode('utf8')
				self.cliente.send(bits)
				self.cliente.settimeout(5)
				confir = self.cliente.recv(2048)
				confir = confir.decode('utf8')
				if confir is not '0':
					cont += 1
				else:
					for x in salvo:
						self.cliente.send(bits)
						self.cliente.settimeout(5)
						confir = self.cliente.recv(2048)
						confir = confir.decode('utf8')
						if confir is '0':
							print("ACK, Frame reenviada com sucesso")
					salvo = []

		self.cliente.close()

cli = Cliente()
cli.cria_cliente()
cli.conecta()
cli.enviar()
