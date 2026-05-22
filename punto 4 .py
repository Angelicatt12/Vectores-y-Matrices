cantidad_vendedores = int(input("Ingrese cantidad de vendedores: "))
cantidad_años = int(input("Ingrese cantidad de años: "))

ventas = []

for i in range(cantidad_vendedores):

    fila = []

    print("\nVendedor", i + 1)

    for j in range(cantidad_años):

        venta = float(input(f"Ingrese ventas del año {j + 1}: "))
        fila.append(venta)

    ventas.append(fila)

print("\nMATRIZ DE VENTAS")

for fila in ventas:
    print(fila)

print("\nTOTAL POR VENDEDOR")

for i in range(cantidad_vendedores):

    total_vendedor = 0

    for j in range(cantidad_años):

        total_vendedor += ventas[i][j]

    print("Vendedor", i + 1, ":", total_vendedor)

print("\nTOTAL POR AÑO")

for j in range(cantidad_años):

    total_anio = 0

    for i in range(cantidad_vendedores):

        total_anio += ventas[i][j]

    print("Año", j + 1, ":", total_anio)

gran_total = 0

for i in range(cantidad_vendedores):

    for j in range(cantidad_años):

        gran_total += ventas[i][j]

print("\nGRAN TOTAL DE LA EMPRESA:", gran_total)
