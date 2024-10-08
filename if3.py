num1 = int(input("Escreva um número: " ))
num2 = int(input("Escreva um número: "))
if num2 < num1:
        print('Maior número: ', num2)
        print('Menor número: ', num1)
elif num2 > num1:
        print('Maior número: ', num1)
        print('Menor número: ', num2)
else:
        print('Números iguais')