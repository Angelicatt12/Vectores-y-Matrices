numeros = [5, 2, 9, 1, 7]
# i controla las pasadas
for i in range(len(numeros)):
    # j controla las comparaciones
    for j in range(len(numeros) - 1):
        if numeros[j] < numeros[j + 1]:
            auxiliar = numeros[j]
            numeros[j] = numeros[j + 1]
            numeros[j + 1] = auxiliar
print(numeros)
