def min_max(numeros):
    min = numeros[0]
    max = numeros[0]
    for num in numeros:
        if num > max: max = num
        if num < min: min = num
    return min, max


numeros = [0, 2, 1, 5, 1, 77, -15, 23, -11, 55, 31, -17]
(min, max) = min_max(numeros)
print(f'min:{min}\nmax:{max}')
