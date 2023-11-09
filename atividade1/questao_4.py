def ordena_tuplas(dados):
    for i in range(len(dados)):
        for j in range(i, len(dados)):
            if dados[i][0] > dados[j][0]:
                dados[i], dados[j] = dados[j], dados[i]
    return dados


dados = [('Luiz', 20), ('Caio', 19), ('Isaack', 22), ('Daniel', 35), ('Alan', 44)]
dados_ordenados = ordena_tuplas(dados)
print(dados_ordenados)
