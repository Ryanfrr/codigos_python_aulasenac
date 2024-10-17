while True:
    valor=int(input("\nEscolha: \n1)Adicção\n2)Subtração\n3)Mult\n4)Divisão:\n0)Sair: \n"))
    if valor == 0:
        print('saindo')
        break
    elif valor == 1: 
        a=float(input("Digite um valor:"))
        b= float(input("Digite um valor:"))
        adc = a + b
        print("Resposta: ",adc)
    elif valor == 2:
        a=float(input("Digite um valor:"))
        b= float(input("Digite um valor:"))
        subt = a -b
        print("Resposta: ",subt)
    elif valor == 3:
        a=float(input("Digite um valor:"))
        b= float(input("Digite um valor:"))
        div = a / b
        print("Resposta: ",div)
    elif valor ==4:
        a=float(input("Digite um valor:"))
        b= float(input("Digite um valor:"))
        mult = a*b
        print("Resposta: ",mult)
    else:
        print('opção invalida')

