def primos(numeros):
    primos = list()
    for numero in numeros:
        primo = True
        for i in range(2, numero):
            if numero % i == 0:
                primo = False
                break
        if primo and numero > 1:
            primos.append(numero)
    return primos


numeros = range(1000)

primos = primos(numeros)

print(primos)