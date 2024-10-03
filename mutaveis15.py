lista = [12,34,23,65,43,11.5,35,9,10,26,45,-1]
mean= sum(lista) / len (lista)
lista.sort()
print('menor a maior temperatura:',lista)
lista.sort(reverse = True)
print('Maior a menor temperatura:',lista)
print(f'media:{mean :.2f}')
