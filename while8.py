while True:
    valor=(input("Informe seu nome: "))
    senha=(input("Informe sua senha: "))   
    if valor != senha:
        print("Concluido!")
        break
    elif valor == senha :
        print('A senha não pode ser igual ao usuario!!')
        continue
    