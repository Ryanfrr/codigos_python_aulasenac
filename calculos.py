a= 80000
b = 200000

ca = 0.03
cb = 0.015

ano = 0

while a< b:
    a+= a *ca
    b += b * cb
    ano += 1
    print (b,ano,"\n",a,ano)

