from datetime import date

def calcula_dia_semana(fecha):
    nombres_dias_semana = ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]
    dia_semana = fecha.weekday()
    return nombres_dias_semana[dia_semana]

if __name__ == '__main__':
    dia = int(input("Cuál es el día de tu fecha de nacimiento?"))
    mes = int(input("Cuál es el mes de tu fecha de nacimiento?"))
    año = int(input("Cuál es el año de tu fecha de nacimiento?"))

    fecha_nacimiento = date(año, mes, dia)
    dia_semana = calcula_dia_semana(fecha_nacimiento)
    print("Naciste un", dia_semana)
