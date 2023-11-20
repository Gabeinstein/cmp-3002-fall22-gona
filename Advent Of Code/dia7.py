class TreeNode:
    def __init__(self, name=None,dir_ = False, size = 0, child=[],parent = None):
        self.name = name
        self.is_dir = dir_
        self.size = size
        self.child = child
        self.parent = parent

def calculate_memory(root):
    memory = 0
    if len(root.child) == 0:
        return root
   
    for i in range (len(root.child)):
        if len(root.child[i].child) == 0:
            memory += calculate_memory(root.child[i]).size
        else:
            calculate_memory(root.child[i])
            memory += root.child[i].size
    root.size = memory

def sum_memory(root):
    memory = []
    last_dir = False
    for i in range(len(root.child)):
        if root.child[i].is_dir:
            last_dir = False
            break
        else:
            last_dir = True
    if root.is_dir and last_dir:
        return root.size

    for i in range (len(root.child)):
        if root.child[i].is_dir:
            memory.append(sum_memory(root.child[i]))
    memory.append(root.size)
    return memory

def del_min(root):
    suma = 0
    last_dir = False
    for i in range(len(root.child)):
        if root.child[i].is_dir:
            last_dir = False
            break
        else:
            last_dir = True
    if root.is_dir and last_dir:
        return root.size

    for i in range(len(root.child)):
        if root.child[i].is_dir:
            temp = del_min(root.child[i])
            if temp != None:
                suma += temp
            if suma >= 30000000:
                return suma
    return None

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

A = []
with open('D:/USFQ/OneDrive - Universidad San Francisco de Quito/5. Quinto Semestre/Estructura de Datos/Github/cmp-3002-fall22-gona/Advent Of Code/input7.txt') as file_obj:
    inp = file_obj.readlines()
    for i in range(len(inp)):
        A.append(inp[i].replace('\n',''))

    root = TreeNode('/',True,0,[],None)
    node = root
    ls = False
    
    for i in range(len(A)):
        if A[i][0:5] == '$ cd ':
            temp = A[i][5:len(A[i])]
            ls = False
            
            if (temp == '/'):
                node = root
            elif(temp == '..'):
                node = node.parent
            else:
                for j in range(len(node.child)):
                    temp_node = node.child[j]
                    if temp_node.name == temp:
                        node = temp_node
                        break
            
        if A[i] == '$ ls':
            ls = True

        if ls:
            if (A[i][0] == 'd'):
                temp_node = TreeNode(A[i][4:len(A[i])],True,0,[],node)
                node.child.append(temp_node)
            elif(A[i][0] != '$'):
                temp = ''
                temp_node = TreeNode(None,False,0,[],node)
                for j in range (len(A[i])):
                    temp += A[i][j]
                    if A[i][j] == ' ':
                        temp_node.size = int(temp.replace(' ',''))
                        temp = ''
                    if j == len(A[i])-1:
                        temp_node.name = temp
                node.child.append(temp_node)

    calculate_memory(root)

    #for i in range(len(root.child)):
    #  print(root.child[i].size) 
    print(sum_memory(root))
    #res = res.replace('  ', ' ')
    print(del_min(root))
    '''
    temp = ''
    sum_ = 0
    for i in range (len(res)):
        temp += res[i]
        if res[i] == ' ':
            temp = temp.replace(' ', '')
            num = int(temp)
            if num <= 100000:
                sum_ += num
            temp = ''

    memorias = []

    for i in range (len(res)):
        temp += res[i]
        if res[i] == ' ':
            temp = temp.replace(' ', '')
            memorias.append(int(temp))
            temp = ''

    insertion_sort(memorias)

    memory_need = 30000000
    for i in range (len(memorias)):
        if memorias[i]>= memory_need:
            print (memorias[i])
            break
    '''