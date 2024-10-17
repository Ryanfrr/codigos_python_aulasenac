while True:
    nome=str.strip(input("Informe seu nome: "))
    if len (nome) <=3:
        print ("Nome invalido!!")
        continue
    idade=int(input("Informe sua idade: "))
    if idade < 0 or idade > 150:
        print('valor invalido')
        continue
    salario=float(input("Informe seu salario: "))
    if salario < 0:
        print('valor invalido')
        continue
    estado= (input("Informe seu estado civil: "))#ta com erro
    if estado != 's' and  estado != 'c' and  estado != ' v' and  estado != 'd':
        print ("VAlor invaldio!!")
        continue
    sexo= (input("Informe seu sesxo: "))#ta com erro
    if sexo != 'f' and estado != 'm' and  estado != 'o':    
        print ("Valor invalido")
        continue
    break
    
  
