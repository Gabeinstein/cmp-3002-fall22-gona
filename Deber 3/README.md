# Deber 3 Estructura de datos
En este deber se va a tratar los siguientes temas:

* Notación Asintótica para análisis de algoritmos
* Algoritmos de Busqueda: Merge Sort, Quick Sort
* Tiempo de ejecucion de un algoritmo 
* Metodos de recursion

### 1. Merge two sorted lists

1. Assume you have two sorted linked lists. Use **recursion** to merge these lists and return a new sorted list. 

For example:

- Input: 

> L1 = 1 -> 3 -> 5 -> 7 -> null

> L2 = 2 -> 4 -> 6 -> null

- Output:

> L4 = 1 -> 2 -> 3-> 4 -> 5 -> 6 -> 7 -> null

En esta pregunta se creo un metodo que tome las dos listas y comience a recorrerlas con dos punteros de forma recursiva. Lo que se hace es comparar el nodo de ambas listas, el que sea menor se guarda y se realiza la entrada recursiva del siguiente nodo y la otra lista que no se afecto. 

Es importante recalcar que las listas enlazadas estan previamente ordenadas. Esto es fundamental para que funcione el algoritmo.

Si las listas enlazadas no tienen el mismo tamano, cuando la recursividad termina con una lista, simplemente se devuelve el nodo de la que aun no termina ya que estaria ordenada con respecto al resto del algoritmo.

2. Calculate complexity

Al calcular la complejidad, se obtuvo que es lineal siguiendo:

$$O(T) = R*(O(s))$$

donde,

R = n + m porque se recorre los dos arreglos.

O(s) = O(1), complejidad de cada entrada recursiva.

$$O(T) = O(n+m)$$

### 2. Implement quick sort

1. Use the divide and conquer technique to implement the quick sort algorithm studied in class. 

Se implemento QuickSort que es un algoritmo que ordena arreglos dividiendo en 2 subarreglos que tienen la particularidad que el uno son todos los valores menores a un pivote y el segundo todos los mayores. De esta forma se divide recursivamente y finalmente se suma el menor mas el pivote y mas el mayor para entregar el arreglo ordenado.

2. Use a couple of parragraphs to explain the steps of divide and conquer:
    - how/where do you divide?

    Se dividio usando dos sublistas y un pivote. La una lista con valores menores al pivote, y la otra con mayores. De esta forma se reduce el problema.

    - where/what do you conquer?

    Se conquisto el problema cuando al dividir continuamente cada arreglo, se forma una especie de arbol binario en el que se llega a un problema trivial de ordenar 3 valores. 

    - how/what do you combine?
    
    Finalmente, se combina el arreglo menor al pivote. A continuacion se debe colocar el pivote, y por ultimo, el arreglo mayor al pivote. De esta forma el resultado final es el arreglo ordenado.

3. Analyze complexity

Se analizo la complejidad del QuickSort obteniendo que:

$$R = log(n)$$

Debido a la estructura de arbol binario.

$$O(s) = O(n)$$

Ya que existe un for loop que recorre el arreglo entero. Por lo que se obtiene una complejidad total del algoritmo de:

$$O(T) = O(nlog(n))$$

### 3. Compare quick sort and merge sort

1. Generate 1000 random permutations of arrays of integers between 1 to 10000.

Se utiliza la funcion random de Python.

2. Execute merge sort and quick sort for each of the permutations

Se ejecuta los dos algoritmos para 1000 arreglos y se utiliza el decorador de tiempo para calcular el tiempo de ejecucion.

3. Calculate the execution time of these runs, and compare them using the statistics of the measured executed time.

Se uso el calculo del tiempo de ejecucion de ambos algoritmos para observar las graficas. Por un problema en el decorador de tiempo, el QuickSort tenia valores no relevantes mayores a $10^5 [\mu s]$. Por lo que se filtro estos datos y se obtuvo una grafica mucho mas entendible. 

4. Explain the differences. Which algorithm is better? When would you use each?

Finalmente, se comparo ambos algoritmos y se concluyo que QuickSort es mejor algoritmo que MergeSort.

Se concluyo que Merge Sort es util cuando se sabe que el arreglo esta ordenado hasta el pivote.

Quick Sort en cambio es mejor cuando el arreglo se encuentra desordenado randomicamente, como es el caso de la simulacion realizada. 

### 4. Implement factorials with recursion

Recall that a factorial number is defined as:

$k! = k \times (k-1) \times (k-2) \times ... \times 2 \times 1$

For example: $3! = 3 \times 2 \times 1 = 6$

1. Use recursion to implement the factorial

El factorial recursivo se lo realiza retornando k*factorial(k-1), donde k es el valor que buscamos su factorial. 

El caso base es cuando k == 0, que es igual a $0! = 1$.

2. Run your code for numbers between 1 and 10000

No se utilizo el limite superior en 10000 por incapacidad de la computadora en almacenamiento de memoria. Se uso 1000 como cota superior. 

3. Calculate the execution time and plot it. 

Se utilizo decoradores y la misma tecnica para analizar el tiempo de ejecucion.

4. What's the complexity?

R = n ya que se repite n veces la llamada recursiva. 

$O(s) = 1$ porque no existe ningun loop en la complejidad de cada llamada recursiva. 

Por lo tanto:

$$O(T) = O(n)$$

5. Implement memoization to improve the performance of your code

Se utiliza un diccionario de python como memoria cache y se cambia la implementacion. Los cambios son en que si el valor del factorial ya se guardo en la memoria cache, entonces solo retorne esto y no calcule nuevamente. 

6. Measure the runtime when you calculate the factorial for numbers between 1 and 10000.

Una vez mas se utilizo los decoradores de python para calcular el tiempo de ejecucion.

7. What's the complexity of your code using memoization?

Se pudo observar que al usar memoria cache, el algoritmo no realiza las n llamadas recursivas que se indico en la anterior implementacion. Sino que solo entra 2 veces a la misma.

Con respecto a la complejidad de cada llamada recursiva, estos son if clauses que tienen complejidad $O(1)$.

Finalmente, se obtiene que la complejidad total es:

$$O(T) = O(1)$$

8. How does the first implementation and the one with memoization compare?

Se demostro que mejor es la implementacion con memorizacion que sin ya que esta tiene una complejidad constante. Mientras que la implementacion sin memorizacion tiene un comportamiento lineal en su complejidad. 