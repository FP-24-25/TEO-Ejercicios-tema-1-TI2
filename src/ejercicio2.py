import ejercicio1

def calcula_estado_nutricional(peso, altura):
    imc = ejercicio1.calcula_imc(peso, altura)
    if imc < 18.5:
        return "Bajo peso"
    elif imc < 25:
        return "Normal"
    elif imc < 30:
        return "Sobrepeso"
    else:
        return "Obesidad"

if __name__ == '__main__':
    peso = float(   # ... y luego esto
        input("Introduce tu peso en kg:") # Primero se ejecuta esto...
        )
    altura = float(input("Introduce tu altura en metros:"))

    estado = calcula_estado_nutricional(peso, altura)
    print("Tu estado nutricional es:", estado)