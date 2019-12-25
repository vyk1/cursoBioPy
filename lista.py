lista = [3, 2, 1, 5, 99, 1, 33, 3]

# com função
# sort = sorted(lista)
# print (sort)

for i in range(len(lista)):
    menor = i

    for j in range(i+1, len(lista)):
        if lista[j] < lista[menor]:
            menor = j

    if lista[i] != lista[menor]:
        aux = lista[i]
        lista[i] = lista[menor]
        lista[menor] = aux

print (lista)
