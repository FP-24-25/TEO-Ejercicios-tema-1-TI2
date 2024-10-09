import ejercicio1, ejercicio2

def imprime_estados_nutricionales(pesos_y_alturas):
    '''
    Reciba como parámetro una lista de tuplas, que representan el peso
      y la altura de una serie de personas, y muestre el IMC y el estado 
      nutricional de cada una de ellas. 
    '''
    i = 1
    for persona in pesos_y_alturas:
        imc = ejercicio1.calcula_imc(persona[0], persona[1])
        estado = ejercicio2.calcula_estado_nutricional(persona[0], persona[1])
        print("El IMC de la persona", i, "es", imc, "y su estado nutricional es", estado)
        i += 1 # Es lo mismo que poner i = i + 1

if __name__ == '__main__':
    personas = [
        (60.0, 1.6),
        (75.4, 1.75),
        (87.9, 1.69),
        (45.1, 1.65)
    ]
    imprime_estados_nutricionales(personas)


'''
El IMC es 23.543, y su estado nutricional es Normal.
El IMC es 27.324, y su estado nutricional es Sobrepeso.
'''