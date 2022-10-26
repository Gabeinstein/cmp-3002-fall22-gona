# Deber 2 Estructura de datos
En este deber se va a tratar los siguientes temas:

* Notación Asintótica para análisis de algoritmos
* Estructura de datos: Stacks, Singly linked list, Queue, PriorityQueue, Doubly linked list.
* Tiempo de ejecucion de un algoritmo 

### Pregunta 1

## 1. Implement the class `Stacks` and all its methods using singly linked lists. Analyze the runtime and memory complexity, and compare with what we studied in class

En primer lugar se debe importar la clase Singly Linked List realizada en clase con los métodos: set_next_node(), list_traversed(), insert_head(), insert_tail(), insert_middle(new_node, value), delete_head(), delete_tail(), delete(value).

La estructura de datos Stack sigue la idea FILO y tiene los siguientes métodos que se definirán la implementación a continuación.
* Push(item): Se verifica si el Stack está lleno, si no lo está se realiza insert_head(Node(item)) y se aumenta en 1 a self.l. Sino aparece un ValueError.
* Pop(): Si el stack no está vacío se realiza un delete_head() se disminuye en 1 self.l y se retorna este valor. 
* Top(): Devuelve el head_node.val de la lista enlazada, la cual representa el top value del stack.
* Full(): Retorna true si self.l == self.n, indicando que el stack está lleno.
* Empty(): Retorna true si el stack está vacío.
* Size(): Retorna el self.l.

Finalmente, se calcula las complejidades asintóticas de cada método del Stack y se compara con la implementación creada en clase.

### Pregunta 2

## 2. Write a method part of the linked list class that will reverse the linked list. Your implementation should visit each node in the list only one time, and should use $O(1)$ of extra memory.


> For example, if the list is:

> A -> B -> C -> D -> null

> The method must return:

> D -> C -> B -> A -> null

Se crea un método perteneciente a la clase Singly_linked_list llamado reverse(). Utilizando las referencias de cada nodo en la lista se intercambia la referencia del node.next_node con la del nodo previo. Por lo tanto, se cambia el sentido de la lista sin necesidad de mover los datos o de recorrer la lista más de una vez. 

### Pregunta 3

## 3. Implement the class Queue using stacks. 

> a. Analyze the runtime and memory complexity, and compare with what we implemented in class.

> b. Implement a few test cases that would allow you to measure the difference in runtime of the `dequeue` method. (Hint: what is the worst case, so that dequeue of the stack implementation is greater than the implementation we did in class?)

En el literal a) se realiza la implementación de Queue usando stacks. Esta es una estructura de datos que sigue la idea FIFO. Para esta implementación se va a usar dos stacks, el primero para realizar el enqueue de los datos y el segundo para el dequeue. 

La estructura de datos Queue tiene los siguientes métodos que se definirán a continuación.
* Enqueue(item): Se verifica si el Stack está lleno, si no lo está hace push en el stack enqueue y se aumenta en 1 a self.l. Sino aparece un ValueError.
* Dequeue(): Si el stack dequeue esta vacío se pasa todos los datos del stack del enqueue al dequeue, se disminuye en 1 self.l y se retorna este valor. Si no es este el caso se realiza el pop en el stack del dequeue. 
* First(): Devuelve el valor que se ingresó primero con la función top() del stack analizando si este valor se encuentra en el enqueue o stack o en el dequeue stack.
* Full(): Retorna true si self.l == self.n, indicando que el stack está lleno.
* Empty(): Retorna true si el stack está vacío.
* Size(): Retorna el self.l.

La función enqueue únicamente realiza push en el stack designado para los enqueues. Mientras que la función dequeue verifica si el stack de dequeue está vacío para pasar los datos desde el stack de enqueue al dequeue, esta operación tiene complejidad $O(n)$. Por otro lado, si el stack de dequeue no está vacío, unicamente se realiza un pop en este stack, lo cual tiene complejidad $O(1)$. Por lo tanto, se denomina amortiación de la complejidad del método dequeue.

Esta implementación es diferente a la realizada en clase, ya que en ella para cada dequeue se realiza el traspaso de los datos del stack enqueue al stack de dequeue. Por lo que siempre, su complejidad es $O(n)$.

Para el literal b) se realiza algunas pruebas para medir los mejores y peores casos en tiempo de ejecución entre los dos métodos de implementación. 

En síntesis, el peor caso es cuando se almacena datos con enqueue y luego se quiere eliminarlos con el dequeue. Esto tiene un coste $O(n)$ para el primer dequeue y $O(1)$ para el resto. Mientras que si se realiza enqueue y dequeue alternado estamos en el mejor caso y su complejidad sería $O(1)$ por cada operación. Sin embargo, mediante el experimento realizado se dertermina que la implementación de la clase Queue con stacks es mucho más eficiente. 

### 4. Complete the PriorityQueue class, so that when we call `dequeue`, the element with the highest priority will be returned. Analyze the complexity of runtime and memory of the `enqueue` and `dequeue` methods.

Utilizando la clase PriorityQueue hecha en clase, se completa su implementación para obtener las funciones dequeue o deleteMin y enqueue o insert. 

La estructura de datos PriorityQueue usa una tupla cuyo primer valor es la prioridad del dato y su segundo valor el dato. Para ello es necesario realizar un algoritmo de ordenamiento, como el utilizado insertion sort, para ordenar los datos dependiedo de la prioridad. 

A continuación se detalla cada función miembro:

* Insert(item): Se verifica si el Stack está lleno, si no lo está añade en el actual índice vacío del stack el item y se aumenta en 1 a self.l. Sino aparece un ValueError.
* deleteMin(): En primer lugar ordena el arreglo con insertion sort, el primer valor será el que se va a eliminar. Cada valor se mueve al índice previo, disminuye 1 el self.l y se retorna el valor eliminado. 
* getMin(): Si la PriorityQueue no está vacía, realiza insertion sort y devuelve la tupla en el primer índice del arreglo.
* decreaseKey(item): Modifica la prioridad de la tupla del valor buscado, siempre que esta prioridad sea menor a la anterior. 

Finalmente, se analiza la complejidad de dequeue y enqueue, obteniendo $O(n^2)$ para dequeue en tiempo de ejecución y $O(1)$ para enqueue. La complejdad en memoria para ambos casos es $O(1)$.

### 5. A given linked-list (singly or doubly) represents an integer number. For example, 345 is represented by the singly-linked list 3 -> 4 ->5. Write a Python program that does the following:

1. Receives three integers A, B and C as inputs. Assume that the three number have the same number of digits.

2. Transform the numbers to their corresponding linked lists

3. Implement the sum of the three numbers. The result A + B + C must be stored in a linked list. 

4. Print the result by traversing the list. 

5. Run your program for numbers with 1 to 100 digits, and capture the runtime. Use these number to estimate the complexity of the runtime.
    - Hint: write a small function that uses `randint()` to generate a number of a given number of digits 
6. Analitically estimate the runtime complexity and compare with the one obtained in (5).

En primer lugar se importa la clase Doubly linked list realizada en clase. Se define una función fuera de la lista llamada to_linked_list(A) que transforma el número A en lista enlazada. 

Posteriormente, se implementa una función suma que ingrese 3 números, se los transforme a lista enlazada y se realize la suma de las listas enlazadas. Esta función retorna la lista enlazada resultante y se realiza un list traverse para mostrar en pantalla el resultado.

En el literal 5 se utilizó el decorador para calcular tiempo de ejecución en la función sum_3() y se realizó un código importando la librería random el cual se escribe el número de dígitos que se quiere experimentar con la función creada. Esto insertará como argumento, valores randómicos con el número de dígitos indicados y se calculará el tiempo de ejecución del algoritmo.

Finalmente, observando el gráfico se estima la complejidad del mismo y posteriormente se calcula analíticamente dicha complejidad. 
