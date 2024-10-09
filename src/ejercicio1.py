def calcula_imc(peso, altura):
    '''
    Recibe un peso en kilogramos y una altura en metros
    y devuelve el índice de masa corporal.
    '''
    return peso / (altura * altura)

if __name__ == '__main__':
    peso = float(input("Introzca peso en kilogramos:"))
    altura = float(input("Introduzca altura en metros:"))
    imc = calcula_imc(peso, altura)
    print("El imc es:", imc)

