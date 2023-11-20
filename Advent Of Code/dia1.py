#Dia 1 Advent of code

A = []
suma = 0

with open('D:/USFQ/OneDrive - Universidad San Francisco de Quito/5. Quinto Semestre/Estructura de Datos/Github/cmp-3002-fall22-gona/Advent Of Code/input1.txt') as file_obj:
    inp = file_obj.readlines()
    suma = 0
    for i in range(len(inp)):
        if inp[i] == '\n':
            A.append(suma)
            suma = 0
        else:
            suma = suma + int(inp[i].replace('\n',''))
    A.append(suma)

def insertion_sort(array):
    """
    Insert Sort
    Input: Array of Tuples, length
    Output: Order the Array in order of priority
    """
    for j in range(len(array)):
        temp = array[j] 
        i = j-1
        while i >= 0 and array[i] > temp:
            array[i+1] = array[i]
            i -= 1
        array[i+1] = temp

insertion_sort(A)

print(A[len(A)-1]+A[len(A)-2]+A[len(A)-3])

