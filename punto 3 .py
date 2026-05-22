respuestas_correctas = [1, 2, 3, 4, 5, 1]

cantidad_estudiantes = int(input("Ingrese cantidad de estudiantes: "))

suma_matematicas = 0
suma_verbal = 0
suma_total = 0

mejor_puntaje = 0
mejor_credencial = ""

estudiantes = []

for estudiante in range(cantidad_estudiantes):

    print("\nEstudiante", estudiante + 1)

    credencial = input("Ingrese credencial: ")

    respuestas_estudiante = []

    for i in range(6):

        respuesta = int(input(f"Respuesta pregunta {i + 1}: "))
        respuestas_estudiante.append(respuesta)

    puntaje_matematicas = 0
    puntaje_verbal = 0

    for i in range(3):

        if respuestas_estudiante[i] == respuestas_correctas[i]:
            puntaje_matematicas += 1

    for i in range(3, 6):

        if respuestas_estudiante[i] == respuestas_correctas[i]:
            puntaje_verbal += 1

    puntaje_total = puntaje_matematicas + puntaje_verbal

    print("Puntaje matemáticas:", puntaje_matematicas)
    print("Puntaje verbal:", puntaje_verbal)
    print("Puntaje total:", puntaje_total)

    suma_matematicas += puntaje_matematicas
    suma_verbal += puntaje_verbal
    suma_total += puntaje_total

    estudiantes.append([credencial, puntaje_total])

    if puntaje_total > mejor_puntaje:

        mejor_puntaje = puntaje_total
        mejor_credencial = credencial

promedio_matematicas = suma_matematicas / cantidad_estudiantes
promedio_verbal = suma_verbal / cantidad_estudiantes
promedio_total = suma_total / cantidad_estudiantes

print("\nPROMEDIOS")
print("Promedio matemáticas:", promedio_matematicas)
print("Promedio verbal:", promedio_verbal)
print("Promedio total:", promedio_total)

print("\nESTUDIANTES SOBRE EL PROMEDIO")

for estudiante in estudiantes:

    if estudiante[1] >= promedio_total:

        print("Credencial:", estudiante[0])
        print("Puntaje:", estudiante[1])

print("\nMEJOR ESTUDIANTE")
print("Credencial:", mejor_credencial)
print("Mayor puntaje:", mejor_puntaje)
