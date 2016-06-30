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
		while(1):
			print('Digite uma mensagem para enviar ao servidor')
			msg = input()
			texto = msg
			cont = 0
			conterro = []
			cont3=0
			frame = ""
			salvo = []
			ERRO=False
			while len(texto)>0:
				listframes = texto[:8]
				texto = texto[8:]
				cont3=cont
				for frame in listframes:
					salvo.append(frame)
					ruido = choice([0,1])
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
					print("Frame:", cont, "Enviado")
					confir = self.cliente.recv(2048)
					confir = confir.decode('utf8')
					if confir is '0':
						cont += 1
					else:
						conterro.append(cont)
						cont += 1
						ERRO=True
				if ERRO:
					cont2=conterro[0]
					for frame in salvo:
						if cont3 >= cont2:
							#envia check(frame)
							bits = check(frame)
							bits = bits.encode('utf8')
							self.cliente.send(bits)
							self.cliente.settimeout(5)
							print("Frame:", cont3, "reenviado")
							confir = self.cliente.recv(2048)
							confir = confir.decode('utf8')
						cont3 += 1
					salvo=[]
					conterro=[]
					ERRO=False
		self.cliente.close()

cli = Cliente()
cli.cria_cliente()
cli.conecta()
cli.enviar()
