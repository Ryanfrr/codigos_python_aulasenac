maca= int(input("Quantas maças você vai comprar?: "))
if maca >=12:
    valor = 0.25
    total = maca*valor
    print(f"Valor da compra:  {total:.2f}")
else:
    valor = 0.30
    total = maca*valor
    print(f"Valor da compra: {total:.2f}")