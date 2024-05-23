# lista
nomes = ['Alex', 'Simone', 'Bernardo' , 'César' , 'Alexandra']

# ordenando a lista, usando a função sort()
nomes.sort() # sort(reverse=True) para decrescente

# exibe a lista na tela
print(nomes) # imprimir tudo
print(nomes[0]) # imprimir a 1ª posição(inicia com 0)

# exibe a lista um em embaixo do outro
for nome in nomes:
    print(nome)

# outra forma
for i in range(len(nomes)): #O len conta o total de posições
    print(f'{i + 1}º nome da lista: {nomes[i]}.')

