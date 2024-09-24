produto = input("informe o nome do produto: ")
print(produto)
quant =int (input("Quantidade do produto: "))
print(quant)

valor = int(2)
print ("O valor de cada produto é de %s reais"%valor)

descontoi = int(input("Percentual de desconto: "))
print(descontoi)

valorcomp = int(quant*valor)
descontof1 = int(valorcomp* descontoi) / 100
valortotal = (valorcomp - descontof1)

print("Total da compra: ", valortotal)



