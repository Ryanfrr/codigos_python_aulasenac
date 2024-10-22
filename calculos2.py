a= float(input ("Informe uma população: "))
b = float(input ("Informe uma população: "))

ca = float(input ("Informe a porcentagem: "))
cb = float(input ("Informe a porcentagem: "))
ano = 0
while a< b:
    a+= a *ca
    b += b * cb
    ano += 1
    print (ano)