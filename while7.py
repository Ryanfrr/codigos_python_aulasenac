
while True:
    valor=int(input("Informe uma nota: "))
    if valor < 0 or valor >10 :
        print('valor invalido')
    elif valor >= 0 and valor <=10:
        print ("valor valido")