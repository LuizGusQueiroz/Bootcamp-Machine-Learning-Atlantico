def soma_listas_menos_intersecao(lista1, lista2):
    lista3 = list()

    for numero in lista1:
        if not (numero in lista2):
            lista3.append(numero)

    for numero in lista2:
        if not (numero in lista1):
            lista3.append(numero)

    return lista3


lista1 = range(0, 100, 2)
lista2 = range(0, 100, 3)
lista3 = soma_listas_menos_intersecao(lista1, lista2)
print(lista3)
