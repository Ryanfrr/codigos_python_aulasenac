valor1 = int(input("Escreva um valor: "))
valor2 = int(input("Escreva um valor: "))
valor3 = int(input("Escreva um valor: "))

if valor1 > valor2 > valor3:
    print("Em ordem crescente:", valor3, valor2, valor1)
elif valor3 > valor2 > valor1:
    print("Em ordem crescente:", valor1, valor2, valor3)
elif valor2 > valor3 > valor1:
    print("Em ordem crescente:", valor1, valor3, valor2)
elif valor1 > valor3 > valor2:
    print("Em ordem crescente:", valor2, valor3, valor1)
elif valor3 > valor1 > valor2:
    print("Em ordem crescente:", valor2, valor1, valor3)
elif valor2 > valor1 > valor3:
    print("Em ordem crescente:", valor3, valor1, valor2)
else: 
    print("Numeros iguais")