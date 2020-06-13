
import math
import random
inicio = 0
fin = 0
paso = 0
azar = []
print('Bien venido')
azar = []
def lista_aleatorea(inicio, fin, paso):
    i = 0
    while i < 5:
            azaroso= random.randrange(inicio, fin, paso)
            azar.append(azaroso)
            i += 1
    else:
        return azar

        


def obtener():
    inicio = int(input('Ingrese el parametro inicio\n'))
    fin = int(input('Ingrese el parametro fin\n'))
    rango = fin - inicio
    cantidad = int(input('Ingrese el parametro paso\n'))
    if rango > 0:
        azar = lista_aleatorea(inicio, fin, paso)
        numero_1 = random.choice(azar)
        numero_2 = random.choice(azar)
        print('Numero 1', numero_1)
        print('Numero 2', numero_2)
        raiz_cuadrada_1 = math.sqrt(numero_1)
        raiz_cuadrada_2 = math.sqrt(numero_2)
        print('Raiz cuadrada de', numero_1, 'es', raiz_cuadrada_1)
        print('Raiz cuadrada de', numero_2, 'es', raiz_cuadrada_2)
        print('Lista random', azar)
    else:
        print('Datos fuera de rango\n')

def contar():
    i = 0
    numero_i = 0
    total = 0
    inicio = 1
    fin = 9
    paso = 1
    azar = lista_aleatorea(inicio, fin+1, paso)
    while i < 5:
        numero_i = azar[i]
        repe = azar.count(numero_i)
        print('El numero', numero_i, 'se repite', repe, 'veces')
        total = total + repe
        if total != 5:
            i += 1
        else:
            if total == 5:
                print(azar)
                break
    else:
        if i == 5:
            print(azar)


def buscar():   # Aún no funciona
    indice = []
    indice_elemento = 0
    indices = []
    i = 0
    numero = 0
    total = 0
    inicio = 1
    fin = 9
    azar = lista_aleatorea(inicio, fin+1, paso)
    print('Elementos generados por azar')
    print(azar)
    elegir = int(input('Número, entonces ubicación 1, Ubicación entonces número 2\n'))
    if elegir == 1:
        while i < 5:
            elemento = int(input('Ingrese el número\n'))
            indice_elemento = azar.index(elemento)
            indices = indices.append(indice_elemento)
            i += 1
            print(indices)
    if elegir == 2:
        while i < 5:
                indice_elemento = int(input('Ingrese indice\n'))
                elemento = azar[indice_elemento]
                i += 1
                print(elemento)
            
    
    



if __name__ == '__main__':
    #lista_aleatorea(inicio, fin, cantidad)
    #obtener()
    #contar()
    buscar()