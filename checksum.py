def checksum(List):
    result = 0
    for num in List:
        result += int(num,2)
    if len(bin(result).split('0b')[1]) > len(num):
        a = bin(result).split('0b')[1][:len(bin(result).split('0b')[1])-len(num)]
        b = bin(result).split('0b')[1][len(bin(result).split('0b')[1])-len(num):]
        check = int(a,2) + int(b,2)
        check = bin(check).split('0b')[1]
    else:
        check = bin(result).split('0b')[1]
    check = check.replace('1','_')
    check = check.replace('0','1')
    check = check.replace('_','0')
    final = ""
    for num in List:
        final += num
    final += check
    return final

#tam = tamanho do checksum
def correcao(palavra, tam):
    check = palavra[len(palavra)-tam:]
    palavra = palavra[:len(palavra)-tam]
    lista = []
    for i in range(tam):
        lista.append(palavra[:tam])
        palavra = palavra[4:]
    soma = 0
    for num in lista:
        soma += int(num,2)
    soma += int(check,2)
    if len(bin(soma).split('0b')[1]) > len(num):
        a = bin(soma).split('0b')[1][:len(bin(soma).split('0b')[1])-len(num)]
        b = bin(soma).split('0b')[1][len(bin(soma).split('0b')[1])-len(num):]
        soma = int(a,2) + int(b,2)
        soma = bin(soma).split('0b')[1]
    else:
        soma = bin(soma).split('0b')[1]
    if(soma.count('1') == len(soma)):
        return True
    else:
        return False


