import os 

nome = input("Nome: ")
idade = int(input("Idade: "))
sexo = input("Sexo: ")

nota1 = float(input("Primeira nota: " )) 
nota2 = float(input("Segunda nota: "))
media = float(nota1 + nota2)/2
os.system("cls")

print("Nome:",nome)
print("idade:",idade)
print("Sexo:",sexo)
(print("Média:",media ))