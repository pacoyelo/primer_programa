# funcion valor maximo de una lista

def maximo (*numeros):
    max = numeros[0]
    for numero in range(len(numeros)):
        if numeros[numero] > max:
            max = numeros[numero]
    return max

print(maximo(1, 2, 3, 7))