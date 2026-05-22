equipos = [
    ["Nacional", 0, 0, 0, 0, 0, 0],
    ["Millonarios", 0, 0, 0, 0, 0, 0],
    ["America", 0, 0, 0, 0, 0, 0]
]

print("\nEquipos disponibles:")

for equipo in equipos:
    print(equipo[0])
cantidad_partidos = int(input("Ingrese cantidad de partidos: "))

for partido in range(cantidad_partidos):

    print("\nPARTIDO", partido + 1)

    local = input("Equipo local: ")
    goles_local = int(input("Goles local: "))

    visitante = input("Equipo visitante: ")
    goles_visitante = int(input("Goles visitante: "))

    for equipo in equipos:

        if equipo[0] == local:

            equipo[1] += 1
            equipo[4] += goles_local
            equipo[5] += goles_visitante

            if goles_local > goles_visitante:

                equipo[2] += 1
                equipo[6] += 3

            elif goles_local == goles_visitante:

                equipo[3] += 1
                equipo[6] += 1

        if equipo[0] == visitante:

            equipo[1] += 1
            equipo[4] += goles_visitante
            equipo[5] += goles_local

            if goles_visitante > goles_local:

                equipo[2] += 1
                equipo[6] += 3

            elif goles_visitante == goles_local:

                equipo[3] += 1
                equipo[6] += 1

for i in range(len(equipos)):

    for j in range(len(equipos) - 1):

        if equipos[j][6] < equipos[j + 1][6]:

            auxiliar = equipos[j]
            equipos[j] = equipos[j + 1]
            equipos[j + 1] = auxiliar

print("\nTABLA DE POSICIONES")

for equipo in equipos:

    print(
        equipo[0],
        "PJ:", equipo[1],
        "PG:", equipo[2],
        "PE:", equipo[3],
        "GF:", equipo[4],
        "GC:", equipo[5],
        "PTS:", equipo[6]
    )
