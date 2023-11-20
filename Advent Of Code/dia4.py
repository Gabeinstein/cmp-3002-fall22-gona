elf1_inf = []
elf1_sup = []
elf2_inf = []
elf2_sup = []

state1 = False
state2 = False

class Node:
    """
    Implementation of a node
    """
    def __init__(self, val=None):
        self.val = val
        self.next_node = None
    
    def set_next_node(self, next_node):
        self.next_node = next_node

class Singly_linked_list:
    """
    Implementation of a singly linked list
    """
    def __init__(self, head_node=None):
        """
        Head Node initialization
        Preset: head_node = None
        """
        self.head_node = head_node

    def list_traversed(self):
        """
        List Traversed
        Print all the sigle linked list
        """
        node = self.head_node
        while node:
            print(node.val)
            node = node.next_node
    
    def insert_head(self, new_node):
        """
        Insert Head
        Inserts a node in the first place of the list
        """
        # insert to the head
        # A -> B -> null
        # R -> A -> B -> null 
        new_node.set_next_node(self.head_node)
        self.head_node = new_node
        
    def insert_tail(self, new_node):
        """
        Insert Tail
        Inserts a node at the end of the list where the node.next_node = None.
        """
        # insert to the tail
        # A -> B -> null
        # A -> B -> R -> null 
        if not self.head_node:
            self.head_node = new_node
        else: 
            node = self.head_node
            prev = self.head_node
            while node:
                prev = node
                node = node.next_node
            prev.set_next_node(new_node)
        
    def insert_middle(self, new_node, value):
        """
        Insert Middle
        Inserts a node at next node of a specific value at the list.
        If not found -> insert_tail()
        """
        # insert in the middle
        # A -> B -> C -> null
        # A -> B -> R -> C -> null
        node = self.head_node
        #Changed case not val found
        while node:
            if node.val == value :  #Prevents None has no attribute 'val'
                break
            node = node.next_node
        if node:
            new_node.set_next_node(node.next_node)
            node.set_next_node(new_node)
        else:
            self.insert_tail(new_node)

    def delete_head(self):
        """
        Delete head
        Deletes first node of the list.
        If None -> pass
        """
        #delete value
        # A -> B -> C -> None
        # B -> C -> None
        if self.head_node: 
            node = self.head_node
            self.head_node = node.next_node
            node.val = 0    #Delete data for security
            node.next_node = None   #Delete pointer for security

    def delete_tail(self):
        """
        Delete tail
        Deletes last node of the list.
        """
        #delete value
        # A -> B -> C -> None
        # A -> B -> None
        if self.head_node:
            node = self.head_node
            prev = self.head_node
            while node.next_node:
                prev = node
                node = node.next_node
            prev.set_next_node(None)

    def delete(self,value):
        """
        Delete
        Deletes a node at a specific value of the list.
        If not found -> pass
        If firts -> Changes the head node
        """
        #delete value
        # A -> B -> C -> None
        # A -> C -> None
        node = self.head_node
        prev = None
        while node:
            if node.val == value :
                break
            prev = node
            node = node.next_node
        if node:
            if not prev:    #Prevent head node error. None has no attribute 'set_next_node'
                self.head_node = node.next_node
                node.next_node = None
            else:
                prev.set_next_node(node.next_node)
                node.next_node = None

with open('D:/USFQ/OneDrive - Universidad San Francisco de Quito/5. Quinto Semestre/Estructura de Datos/Github/cmp-3002-fall22-gona/Advent Of Code/input4.txt') as file_obj:
    inp = file_obj.readlines()
    for i in range(len(inp)):
        temp = ''
        for j in range(len(inp[i])):
            temp += inp[i][j]
            if state1 == False and state2 == False and inp[i][j] == '-':
                elf1_inf.append(temp[0:len(temp)-1])
                temp = ''
                state1 = True
                state2 = False

            if state1 == True and state2 == False and inp[i][j] == ',':
                elf1_sup.append(temp[0:len(temp)-1])
                temp = ''
                state1 = False
                state2 = True

            if state1 == False and state2 == True and inp[i][j] == '-':
                elf2_inf.append(temp[0:len(temp)-1])
                temp = ''
                state1 = True
                state2 = True
            
            if state1 == True and state2 == True and (inp[i][j] == '\n' or (j == len(inp[len(inp)-1])-1 and i == len(inp)-1)):
                elf2_sup.append(temp.replace('\n',''))
                temp = ''
                state1 = False
                state2 = False
                break
    
#print(len(elf2_sup))
#print(elf2_sup)

#print ("")

#print(elf2_inf)
#print(elf2_sup)

conteo = 0

for i in range(len(elf1_inf)):
    elf1inf = False
    elf1sup = False
    elf2inf = False
    elf2sup = False

    if int(elf1_inf[i]) <= int(elf2_inf[i]):
        elf1inf = True
    if int(elf1_inf[i]) >= int(elf2_inf[i]):
        elf2inf = True
    if int(elf1_sup[i]) >= int(elf2_sup[i]):
        elf1sup = True
    if int(elf1_sup[i]) <= int(elf2_sup[i]):
        elf2sup = True

    if elf1inf and elf1sup and elf2inf and elf2sup:
        conteo += 1
    elif elf1inf == True and elf1sup == True:
        conteo += 1
    elif elf2inf == True and elf2sup == True:
        conteo += 1

print(conteo)


list1 = []
list2 = []

for i in range(len(elf1_inf)):
    list1.append(Singly_linked_list(Node(int(elf1_inf[i]))))
    for j in range(int(elf1_inf[i])+1,int(elf1_sup[i])+1):
        list1[i].insert_tail(Node(j))

for i in range(len(elf2_inf)):
    list2.append(Singly_linked_list(Node(int(elf2_inf[i]))))
    for j in range(int(elf2_inf[i])+1,int(elf2_sup[i])+1):
        list2[i].insert_tail(Node(j))



def intersection(L1,L2):
    node1 = L1.head_node
    node2 = L2.head_node
    
    while node1:
        while node2:
            if (node1.val == node2.val):
                return node1.val
            node2 = node2.next_node
        node2 = L2.head_node
        node1 = node1.next_node
    
    return None

count = 0
for i in range(len(list1)):
    if (intersection(list1[i],list2[i])):
        count += 1

print(count)

#print(intersection(list1[44],list2[44]))
#list1[44].list_traversed()
#list2[44].list_traversed()
