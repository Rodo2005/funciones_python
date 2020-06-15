#!/usr/bin/env python
'''
Bucles [Python]
Ejercicios de práctica
---------------------------
Autor: Inove Coding School
Version: 1.1

Descripcion:
Programa creado para que practiquen los conocimietos
adquiridos durante la semana
'''

__author__ = "Inove Coding School"
__email__ = "alumnos@inove.com.ar"
__version__ = "1.1"


def ej1():
    print('Comencemos a crear lo nuestro!')

    '''
    Cree un nuevo archivo el cual será su módulo que utilizará
    para resolver todos los ejercicios de está guía.
    En el módulo implemente todas las funciones que le fueron
    solicitadas en "ejercicios_clase":
    - promedio
    - lista_aleatoria
    - ordenar
    - contar
    - buscar

    Importe el módulo a este programa/documento para su uso
    en el resto de los ejercicios
    ''''''


InoveTools
---------------------------
Autor: Rodolfo
Version: 1.0
Descripcion:
Módulo con algunas de las funciones que ejemplifican
las herramientas desarrolladas en este curso.
'''

__author__ = "Rodolfo"
__email__ = "alumnos@inove.com.ar"
__version__ = "1.0"

import math  
import random
import statistics

'''
def promedio():
    longitud = len(numeros)
    if longitud > 0:
        minimo = min(numeros)
        maximo = max(numeros)
        suma = minimo + maximo
        promedio = suma / 2
        print(promedio)
    elif longitud == 0:
        print('No se puede obtener el promedio de una lista vacia\n')
'''

def promedio(numeros):
    
    suma = 0
    longitud = len(numeros)
    if longitud > 0:
        for longitud in numeros:
            suma = suma + longitud
        promedio = suma / longitud
        print('Suma: ', suma)
        print('Promedio:', promedio)
        return promedio
    elif longitud == 0:
        print('Lista vacia')


inicio = 0
fin = 0
cantidad = 0
azar = []
numeros = []
paso = 1


def lista_aleatorea(inicio, fin, paso, muestras):
    i = 0
    while i < muestras:
            azaroso = random.randrange(inicio, fin, paso)
            numeros.append(azaroso)
            i += 1
    else:
        print('Lista:', numeros)
        return numeros

            
def obtener():
    inicio = int(input('Ingrese el parametro inicio\n'))
    fin = int(input('Ingrese el parametro fin\n'))
    rango = fin - inicio
    paso = int(input('Ingrese el parametro paso\n'))
    muestras = int(input('Ingreses la cantidad de muestras\n'))
    if muestras > 0:
        azar = lista_aleatorea(inicio, fin, paso, muestras)
        #numero_1 = random.choice(azar)
        #numero_2 = random.choice(azar)
        #print('Numero 1', numero_1)
        #print('Numero 2', numero_2)
        #raiz_cuadrada_1 = math.sqrt(numero_1)
        #raiz_cuadrada_2 = math.sqrt(numero_2)
        #print('Raiz cuadrada de', numero_1, 'es', raiz_cuadrada_1)
        #print('Raiz cuadrada de', numero_2, 'es', raiz_cuadrada_2)
        print('Lista random', azar)
    else:
        print('Datos fuera de rango\n')


# numeros = []

def ordenar(numeros):
    numeros.sort(reverse=True)
    numeros_ordenados = numeros
    return numeros_ordenados


def crear_lista():
    numeros = []
    cuantos = 0
    cuantos = int(input('Cuantos numero desea ordenar\n'))
    i = 0
    while i < cuantos:
        numero = int(input('Ingresar numero\n'))
        numeros.append(numero)
        i += 1
    ordenar(numeros)
    print(numeros)


def contar():
    i = 0
    numero = 0
    total = 0
    inicio = 1
    fin = 9
    paso = 1
    cantidad = 5
    azar = lista_aleatorea(inicio, fin+1, paso)
    while i < cantidad:
        numero = azar[i]
        repe = azar.count(numero)
        print('El numero', numero, 'se repite', repe, 'veces')
        total = total + repe
        if total != cantidad:
            i += 1
        else:
            if total == cantidad:
                print(azar)
                break
    else:
        if i == cantidad:
            print(azar)


    inicio = 1
    fin = 9
    paso = 1

def buscar():
    cantida_numeros = 5
    i = 1
    j = 0
    lista_repe = []
    indice_num = []
    azar = lista_aleatorea(inicio, fin, paso)
    for i in range(1, 10):
        j = 0
        indice_num = []
        while j < cantida_numeros:
            numero = azar[j]
            if i == numero:
                indice_num.insert(j, azar.index(numero))
                j += 1
            elif i != numero:
                j += 1
        if j == cantida_numeros:
            repeticiones = len(indice_num)
            while repeticiones!= 0:
                lista_repe.append(i)
                lista_repe.append(repeticiones)
                break
                
    if i == 9:            
        k = 0
        while k < 7:
            print('El numero', lista_repe[k], 'aparece', lista_repe[k+1], 'veces')
            #print('En posicion', indice_num[i])
            k += 2


#if __name__ == '__main__':
    #promedio(numeros)
    #lista_aleatorea()
    #obtener()
    #ordenar()
    #crear_lista()
    #contar()
    #buscar()




def ej2():
    print("Jugando a los dados")

    '''
    Un dado común tiene 6 caras, 6 resultados posibles
    1 - 2 - 3 - 4 - 5 - 6

    Utilice la función "lista_aleatoria" para generar
    5 tiros de dados (una lista de 5 con resultados posibles
    de un dado)

    1)
    Utilice la función "ordenar" para ordenar la lista
    de números generados.
    Imprimir en pantalla la lista ordenada

    2)
    Importe el modulo "random" a este programa/documento
    Luego llame al método "shuffle" del módulo "random"
    para volver a mezclar la lista de tiros de dados.

    3)
    Utilice el método "sample" del módulo "random"
    para obtener al hazar 3 valores de la lista
    de números.
    Imprima en pantalla dicha lista de 3 valores.
    '''

def azaroso():
    inicio = 1
    fin = 6
    paso = 1
    muestras = 0
    numeros = []
    tres = []
    #muestras = int(input('Cantidad de muestras: \n'))
    numeros = lista_aleatorea(inicio, fin, paso, muestras)
    numeros_ordenados = ordenar(numeros)
    print('Numeros ordenados: \n', numeros_ordenados)
    random.shuffle(numeros_ordenados)
    tres = random.sample(numeros_ordenados, 3)
    print('Tres numeros:\n', tres)


if __name__ == '__main__':
    azaroso()





def ej3():
    print("Dominando la recursividad")

    '''
    En este ejercicio se deberá plantear el calculo del
    factorial de un número utilizando recursividad
    Primero veamos a que nos referimos con el factorial
    de un número, por ejemplo el factorial (!) de 5 sería:
    --> 5! = 5 * 4 * 3 * 2 * 1
    Mientras que el factorial de 4 sería:
    --> 4! = 4 * 3 * 2 * 1
    Tambíen se podría decir que el factorial de 5 es:
    --> 5! = 5 * 4!
    Es decir, el factorial de 5 (5!) es igual a 5 * factorial de 4 (4!)
    Pueden ver más ejemplos y de que se trata el factorial en el
    siguiente link:
    https://www.disfrutalasmatematicas.com/numeros/factorial.html

    El objetivo es calcular el factorial utilizando recursividad,
    como pueden ver en el ejemplo anterior calcular el factorial de 5
    requiere además calcular el factorial de 4, y calcular el factorial de 4
    requiere calcular el factorial de 3:
    --> 4! = 4 * 3 * 2 * 1
    --> 4! = 4 * 3!
    --> 3! = 3 * 2 * 1
    --> 3! = 3 * 2!

    Les dejamos este ejercicio para que lo piensen, lo pueden dejar para el final
    Cualquier duda nos escriben en el Campus
    '''

def factorial():


    numero = int(input('Ingrese un numero entero para calcular su factorial: \n'))
    if numero > 0:
        i = numero -1
        factorial = numero 
        while i > 1:
            factorial = factorial * i
            i -= 1
        print('El factorial de', numero, 'es', factorial)
    elif numero <= 0:
        print('No existe el factorial de un numero negativo o cero\n')


if __name__ == '__main__':
    factorial()


def ej4():
    print("Un pequeño paso en la estadística, un gran paso en Python")

    '''
    Lo primero que se solicita es utilizar la función "lista_aleatoria"
    para generar una lista de 20 elementos, en un rango del 0 al 100 inclusive
    A continuación se solicitará que calcule el desvío estandar
    del la lista de números generaods.

    Para calcular el desvió estandar deberá aprovechar la función
    de "promedio", que en estadística al promedio se lo llama "media"
    Deberá calcular la sumatoria de la diferencia de todos los elementos
    de la lista respecto a la "media", dividirlo por la cantidad de elementos
    y calcular la raiz cuadrada.

    Les dejamos una página en donde explica el paso a paso del cálculo
    para que vayan viendo:
    https://es.khanacademy.org/math/probability/data-distributions-a1/summarizing-spread-distributions/a/calculating-standard-deviation-step-by-step

    El objetivo de este ejercicio es que practiquen la implementación
    matemática de algorítmos.

    Sugerencias:
    1 - Utilizar la función "promedio" para calcular la media
    2 - Para realizar la diferencia entre cada elemento de la lista
        y el promedio utilizar un bucle "for" e ir acumulando el valor
        en una variable "sumatoria".
        Cada valor de diferencia calculada debe aplicarse el módulo "abs"
        (método en math) antes de incorporar dicha diferencia a la variable
        acumulada "sumatoria"
    3 - Utiliza el método "len" para obtener cuantos elementos
        hay en la lista "N".
    4 - Calcular la raiz cuadrada con el método de math correspondiente.

    '''
    # Mi implementación de desvió estandar a continuación:
import statistics


def desvio_estandar():
    paso = 1
    inicio = int(input('En que valor comienza\n'))
    fin = int(input('En que valor termina\n'))
    muestras = int(input('Cuantas muestras desea se realicen\n'))
    numeros = lista_aleatorea(inicio, fin, paso, muestras)
    prom = promedio(numeros)
    sumar = 0
    potencia = 0
    for i in numeros:
        potencia = (i - prom) * (i - prom)
        sumar = sumar + potencia
    s = math.sqrt(sumar / (len(numeros)) - 1)
    print('La desviacion estandar es:', s)
    print('')

    #  Estas proximas cuatro lineas nos dan datos aproximados
    #  a los calculos hechos sin la libreria 'statistics' para
    #  el calculo de valores estadisticos

    media_arit = statistics.mean(numeros)
    print(media_arit)
    desv_estandar = statistics.stdev(numeros)
    print(desv_estandar)


    


if __name__ == '__main__':
    #lista_aleatorea(inicio, fin, paso)
    promedio(numeros)
    desvio_estandar()

    '''
    Ahora que han terminado, importe el módulo "statistics" y realice
    los mismos calculos utilizando los metodos del módulo para verificar
    sus resultados
    1 - Utilice el método mean() para contrastar nuestro método "promedio"
    2 - Utilice el método stdev() para contrastar nuestro función desvio_estandar
    '''





def ej5():
    print("Ahora sí! buena suerte :)")

    '''
    Este ejercicio representa ya un problema que forma parte de un juego
    Lo que se desea realizar es una parte del juego "la generala".

    Deberá realizar una lista para guardar 5 dados, guardar los números
    sacados en esa tirada de de dados (son 5 números del 1 al 6)

    1) El jugador tira la dados y sacar 5 números aleatorios, puede usar
    la función de "lista_aleatoria" para generar dichos números.

    2) Luego debe analizar los 5 números y ver cual es el número que
    más se repitio entre los 5 dados (debe usar la función max con
    la key de list.count)

    3) Una vez reconocido el número más repetido entre los 5, debe
    guardar en una lista aparte con esos números.
    Si por ejemplo salió 4-4-2-1-4, debe quedarse con esos tres "4"
    Debe extrarlos de la lista, quedándole dos listas separadas
    dados_guardados = [4,4,4]
    dados_para_tirar= [2,1]
    Utilice el método "pop" para extraer elementos de una lista
    y el método "append" para agregar nuevos.
    Puede utilizar la función creada "buscar" para encontrar
    los índices del número que desea extraer.

    4) Debe volver a tira los dados, generar nuevos
    números aleatorios para aquellos dados reservados para
    tirar (dados_para_tirar). Es decir, que si tengo 2 elementos
    en mi lista de "dados_para_tirar", debo generar dos números
    aleatorios nuevos.
    Otra opción es generar una "lista_generica" nueva y reemplazar
    los "dados_para_tirar".

    5) Luego de tirar nuevamente los datos, por ejemplo digamos
    que salieron los números: 4-1
    Debo volver a quedarme con el "4" ya que es el número que estoy
    buscando.
    Sino salió el "4" vuelvo a tirar todos los dados.
    Si salió un "4" me lo quedo y lo sacó de la lista y lo guardo
    en "dados_guardados".

    5) Debe repetir este proceso hasta que en su lista de "dados
    guardados" tenga "generala", es decir, 5 números iguales.

    '''
def generala():
    i = 1
    k = 0
    mayor_cantidad = []
    dados_guardados = []
    mas_cantidad = 0
    paso = 1
    inicio = 1
    fin = 6
    muestras = 5
    verdad = False
    #inicio = int(input('En que valor comienza\n'))
    #fin = int(input('En que valor termina\n'))
    #muestras = int(input('Cuantas muestras desea se realicen\n'))
    while muestras > 0: 
        numeros = lista_aleatorea(inicio, fin, paso, muestras)
        k += 1
        if muestras < 5:
            verdad = True
        if verdad == False:
            mas_cantidad = max(numeros, key=numeros.count)
            cuantos = numeros.count(mas_cantidad)
            while i < cuantos + 1:
                ubicacion = numeros.index(mas_cantidad)
                dados_guardados.append(numeros.pop(ubicacion))
                i += 1
            muestras = len(numeros)
        elif verdad == True:
            if mas_cantidad in numeros:
                cuantos = numeros.count(mas_cantidad)
                i = 1
                while i < cuantos + 1:
                    ubicacion = numeros.index(mas_cantidad)
                    dados_guardados.append(numeros.pop(ubicacion))
                    i += 1
                muestras = len(numeros)
    else:
        print('GENERALA', k, 'veces se tuvieron que tirar los dados') 

if __name__ == '__main__':
    print("Ejercicios de práctica")
    #ej1()
    #ej2()
    #ej3()
    #ej4()
    #ej5()
