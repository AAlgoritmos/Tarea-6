# Tarea 6

## Grupo 2

María Catalina Ibáñez Piñeres, 201922462
Andrés Felipe Florián Quitián, 202324937

## ¿Cómo ejecutar el programa implementado?

El código funciona con formato de **entrada y salida estándar**. Es decir, recibe cualquier archivo de texto que tenga en la primer línea el número del algoritmo aproximado que se debe correr (1, 2, 3 o 4) y el resto del archivo debe contener por cada línea una pareja de números que representan un eje (los dos vértices conectados), separados por tab.

Puede ejecutar las pruebas corriendo en una terminal de comandos (clásica, no Powershell) el código:
py main.py < test.in > answ.out. Donde py es la referencia de la máquina al intérprete de Python, puede que en lugar de py sea necesario escribir python o python3.

El símbolo "<" redirige el contenido de "test.in" a la entrada estándar.
El símbolo ">" redirige la salida estándar al archivo "answ.out".

Los archivos algorithm_1.py, algorithm_2.py, algorithm_3.py y algorithm_4.py contienen la implementación de los 4 algoritmos aproximados respectivamente y el archivo graph.py contiene una clase SimpleGraph que se utiliza para crear un objeto grafo en los 4 algoritmos.

Se asume que el grafo de entrada es un grafo no dirigido, razón por la cual si en el archivo test.in hay un eje (u,v) cuando se arma la matriz de adyacencias se pone un 1 en la posición u,v y en la posición v,u. 

A continuación, se presentará un caso de ejemplo y salida para el código realizado.

#### Ejemplo de entrada:

4
0   2
2   4
4   1
4   3

#### Ejemplo de salida:

Vertex cover:  {2, 4}
Size:  2
