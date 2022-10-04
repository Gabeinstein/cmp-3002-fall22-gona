# Deber 1 Estructura de datos
En este deber se va a tratar los siguientes temas:

* Notación Asisntótica
* Estructura de datos: Array
* Tiempo de ejecucion de un algoritmo 

Pregunta 1:

## 1. Assume we implemented an algorithm that has complexity approximately $n*log(n)$ . How much faster is this implementation compared to one of complexity $n^2$? 

En esta pregunta se comparó las dos funciones y se busca un numero $c$ que indique cuanto más rápido es el mejor algoritmo con respecto al otro.

En primer lugar, se graficó para tener una idea de cuál función es más rápida.

Luego, se buscó un número c que iguale las dos funciones y este representa el factor de rapidez que existe entre las dos.

Finalmente, este número encontrado es cuanto más rápida es la función con respecto a la otra.

## 2. The runtime of an algorithm is captured in the following table:

### As precissely as possible, estimate the function that describes the growth of the runtime

En esta segunda pregrunta, el objetivo es graficar la función que describe los arreglos dados. 

Posteriormente, se identifica la tendencia de crecimiento de la gráfica. 

Luego se busca los coeficientes que describen esa función y finalmente se grafica las dos funciones para determinar si la aproximación es buena. 

## 3. By estimating the number of operations as a function of $n$, estimate the complexity of the following function

En la pregunta 3, se da un algoritmo el cual se debe buscar la complejidad. 

En primer lugar, se identifica cada linea de código el número de veces que se repite y el número de operaciones elementales.
Las operaciones elementales son read y write.

Con cada loop se usa la notación sigma de la sumatoria para representar el número de operaciones que realiza.

Finalmente, se obtiene la complejidad del algoritmo representada en notación Big-O.

## 4. From class, remember the code we use to get the sum of the first $n$ positive integers:

def sum1(n):
    total = 0
    for i in range(1, n+1):
        total += i
    return total

Now consider a different function that does the same thing.

def sum2(n): 
    total = n*(n+1)//2
    return total

1. Run the two functions and make sure that they return the same outputs. Use $n = 5, 8, 103, 527$

2. Use Python time library to estimate the runtime for inputs of $n = [1, 10, 10^2, 10^3, 10^4, 10^5, 10^6, 10^7, 10^8, 10^9] $

3. Plot the runtime as a function of  for both functions in the same figure.
    * Use different line colors and markers to help distinguish between the two curves.

4. Analytically estime the runtime functions for the functions sum1 and sum2. Call them $T_1(n)$ and $T_2(n)$. 
    * Note that the times obtained in your computer will be different to the ones shown in class since the speed and memory of the computers used to run the code are likely different.

5. How long will it take to run the code for $n=10^{100}$ using sum1 and sum2? What are your main impressions about the difference?

**Hint**: Use and modify the code from the slides to get and plot the runtime

En el primer literal se utiliza un for loop y arreglos para comparar si los resultados de los dos algoritmos son los mismos.

Posteriormente, se usa decoradores de Python para obtener el resultado del tiempo que demoró en ejecutar cada algoritmo. Para esto se usa el decorador que devuelve un vector con el resultado en el primer índice y el tiempo de ejecución en el segundo índice.

Luego, se grafica los dos algoritmos en forma logarítmica para que se aprecien los cambios. 

Se calcula la complejidad de cada algoritmo contando el número de operaciones existentes.

Finalmente, se estima el tiempo que tarda el computador para una operación de $n = 10^100$ con cada algoritmo.

## 5. Prove that the running time of an algorithm is $\Theta(g(n))$ if and only if its worst-case running time is $O(g(n))$ and its best-case running time is $\Omega(g(n))$

Se escribe la definición de: $\Theta(g(n))$, $O(g(n))$ y $\Omega(g(n))$.

Posteriormente, se opera con las cotas inferiores y superiores hasta llegar a la prueba que buscamos. 

Finalmente, se repite el proceso iniciando desde la prueba que buscamos hasta llegar a las definiciones dadas, por lo que de esta forma se logra que la prueba sea si y solo si. 

Una vez que se cumplan ambos sentidos del enunciado, el problema queda resuelto.


## 6. Sort the following functions in decreasing order of asymptotic complexity $O(f(n))$:

* $f_1(n) = \sqrt{n}$
* $f_2(n) = n^3$
* $f_3(n) = \binom{n}{4}$
* $f_4(n) = \sum_{i=2}^{n}(i-1)$

En primer lugar, se grafica cada función para tener una idea de cuales son más rápidas que otras. Una vez encontrado se ordena desde la función con mayor complejidad hasta la que tiene menor complejidad, en orden descendente. 

## 7. Implement the methods of the class Array that deal with deletion of elements. Consider the 3 cases we considered in class.

Se utiliza la clase Array definida en clase. Y se crea 3 nuevos métodos. 

Delete_tail borra el último item agregado al Arreglo.

Delete_head borra el primer item del array desplazando un puesto a todos los datos y dejando el último valor en None.

Delete borra el elemento en el índice dado y desplaza los elementos que están después de ese índice dejando el último valor en None.  