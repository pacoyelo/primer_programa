# primer programa para github

def sumador(numeros):
    suma = 0
    for numero in range (numeros+1):
        suma += numero
    return suma

def mayusculas(palabra):
    for letra in palabra:
        print(letra.upper(), end='')
    print()

def cuadrados(valores):
    cuadrado = 0
    for valor in range (0, valores+1):
        cuadrado += valor**2
    return cuadrado


print(sumador(100))
mayusculas('hola')
print(cuadrados(3))
