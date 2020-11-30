# Tarea 2:

## Algoritmo Genetico

El link de github que contiene este Readme con sus imagenes se encuentra en:
https://github.com/CArielSanchez/CC5114-Redes-Neuronales/tree/master/Tarea2

Integrantes:
- Valentín Espina
- Cristian Sánchez

# Palabra

## Descripción del Problema

El problema consiste en encontrar una palabra oculta usando un algoritmo genético, al cual solo se le informa que tan cerca de la respuesta está.

## Algoritmo Genetico Usado

### Funcionamiento

El algoritmo recibe:
- Tamaño de la poblacion: Donde la población es un cojunto de individuos.
- Tasa de la mutación: Es la probabilidad de mutar un gen de un individuo.
- Fintess: Es la función que indica que tan cerca esta de la respuesta.
- GeneFactory: Es la función que genera un gen aleatoriamente.
- IndividualFactory: Es la función que genera un individuo aleatoriamente.
- MaxIter: Es la máxima epoca que puede alcanzar el algoritmo.
- Selector: Es tipo de selector que se usara para elegir a un individuo.
- TerminationCondition: Es la condición de termino del algoritmo.

El algoritmo itera hasta que se alcanza MaxIter o TerminationCondition, generando nuevos individuos a través de la herencia y la mutacion, de una generacion a otra. Finalmente cuando terminan las iteraciones, el algoritmo entrega el mejor individuo de esa generación en base a su fitness.

### Selector

Para seleccionar a un individuo dentro de una lista de individuos utilizaremos el algoritmo de la ruleta, donde se escoge a un individuo aleatoriamente, donde su probabilidad de ser escogido es directamente proporcional a su fitness, entonces a mayor fitness mayor probabilidad de ser escogido.

### Herencia

Para calcular la herencia entre 2 individuos se elije aleatoriamente una posición para cortar los genes de los 2 individuos, en donde para crear un nuevo individuo, se escoge el primer trozo del primer individuo y el segundo trozo del segundo individuo.

### Mutacion

Para realizar la mutacion de un individuo, se genera un gen aleatoriamente y se intercambia con uno seleccionado (usando la función de seleccion) teniendo en cuenta la tasa de mutacion (mutation rate), para decidir si intercambiarlo o no.


## Instancia del Algoritmo 

## Experimentos

### Fitness vs Epoch

### Epoch vs Popsize

## Conclusión


# Binario

## Descripción del Problema

El problema consiste en encontrar la transformacion binaria de un número, utilizando un algoritmo genético, al cual solo se le informa qué tan cerca esta del número preguntado.

## Algoritmo Genetico Usado



## Instancia del Algoritmo 

## Experimentos

### Fitness vs Epoch

### Epoch vs Popsize

## Conclusión



# Traveling Salesman Problem (TSP)

## Descripción del Problema

El problema consiste en encontrar la combinacion de ciudades que recorridas en aquel orden, la distancia recorrida sea mínima (óptima).

## Algoritmo Genetico Usado

### Herencia

### Mutacion

## Instancia del Algoritmo 

### Clase Ciudad

## Experimentos

### Fitness vs Epoch

### Epoch vs Popsize

## Conclusión




![Normalization](imgs/normalization.png) 



# Librerias

Las librerias utilizadas son: 
- Numpy. Libreria para manejo de matrices y operaciones entre estas. Ademas, de poder inicializar matrices aleatoriamente.

- Random, Libreria para generar números aleatoriamente.

- Sys, Libreria que maneja constantes del sistema.

- Math, Libreria para formulas matemáticas.

- Matplotlib. Libreria grafica para mostrar comparaciones entre datos.

La forma de instalar librerias estan en el archivo [InstallLibraries](InstallLibraries.md)
