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

print(sumador(100))
mayusculas('hola')