jan = [22,43] 
fev=[32,45]
mar=[25,12]
abr=[45,50]
mai=[18,22]
jun=[11,43]
jul=[46,26]
ago=[10,28]
sete=[9,-1]
out=[34,27]
nov=[6,7.7]
dez=[-1,0]
soma1 = jan+fev+mar+abr+mai+jun + ago+sete+out+nov+dez
mean= sum(soma1) / len (soma1)
soma1.sort()
print(f'media:{mean :.2f}')
print('menor a maior temperatura:',soma1)
soma1.sort(reverse = True)
print('Maior a menor temperatura:',soma1)


