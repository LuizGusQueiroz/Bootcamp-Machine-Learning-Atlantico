def segundo_maior(numeros):
    if(len(numeros) < 1): return None
    if(len(numeros) == 1): return numeros[0]

    maior     = max(numeros[:2])
    seg_maior = min(numeros[:2])

    for numero in numeros[2:]:
        if numero > maior:
            maior, seg_maior = numero, maior
        elif numero > seg_maior:
            seg_maior = numero

    return seg_maior


numeros = [-1, 9, 1, 2, 7, 3, 1, -19, 20]
seg_maior = segundo_maior(numeros)
print(seg_maior)