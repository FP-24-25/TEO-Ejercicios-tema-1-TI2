def lee_numeros(n):
    '''
    Lee n números enteros del teclado y los devuelve
    almacenados en una lista. 
    '''
    lista = []
    for _ in range(n):
        numero = int(input("Introduce un número:"))
        lista.append(numero)
    return lista

if __name__ == '__main__':
    cantidad_numeros = int(input("Cuántos números quieres leer?"))
    numeros = lee_numeros(cantidad_numeros)
    print("Esta es la lista obtenida:", numeros)

    mayor = max(numeros)
    print("El mayor de la lista es", mayor)

    media = sum(numeros) / len(numeros)
    print("La media es", media)

    contador = 0
    for numero in numeros:
        if numero % 2 == 0:
            contador += 1
    print("Hay", contador, "números pares.")

    numeros_mayores_10 = []
    for numero in numeros:
        if numero > 10:
            numeros_mayores_10.append(numero)
    print("Números mayores a 10:", numeros_mayores_10)


    