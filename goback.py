from checksum import *

def server_msg(frame):
    cont=1
    if correcao(frame):
        cont += 1
        return 0
    else:
        return cont

def client_msg(texto):
    cont=0;
    frame = ""
    salvo = []
    while len(texto)>0:
        frame = texto[:7]
        ruido = choice([0,1])
        salvo.append(frame)
        if ruido == 1:
            print("RUIDO")
            pos=choice([0,len(frame)-1])
            if frame[pos]=='1':
                frame = frame[:pos-1] + "0" + frame[pos:]
            else:
                frame = frame[:pos-1] + "1" + frame[pos:]
        #envia check(frame)
        confir = #espera retorno server
        if confir > 0:
            cont += 1
        else:
            for x in salvo:
                #reenvia check(frame)
            salvo = []
