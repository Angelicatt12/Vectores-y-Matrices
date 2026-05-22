import random

matriz = []

for i in range(2):  
    fila = []   
    for j in range(2):        
        numero = random.randint(1, 20)
        fila.append(numero)      
    matriz.append(fila)    
print("Matriz:")

for fila in matriz:
    print(fila)  
determinante = (
        matriz[0][0] * matriz[1][1]
        - matriz[0][1] * matriz[1][0]
)

print("Determinante:", determinante)