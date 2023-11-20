import ctypes
class Stack(object):
    """
    Implementation of the stack data structure
    """
    def __init__(self, n):
        self.l = 0
        self.n = n
        self.stack = self._create_stack(self.n)        
    
    def _create_stack(self, n):
        """
        Creates a new stack of capacity n
        """
        return (n * ctypes.py_object)()
    
    def push(self, item):
        """
        Add new item to the stack
        """
        if self.l == self.n:
            print("No more capacity")
        else:
            self.stack[self.l] = item
            self.l += 1

    def pop(self):
        """
        Remove an element from the stack
        """
        # self.l = 0
        # 0 is equivalent to False
        # any number != 0 is True
        if not self.l:
            print('Stack is empty')
        else:
            c = self.stack[self.l-1]
            self.stack[self.l] = ctypes.py_object
            self.l -= 1
            return c

    def top(self):
        """
        Show the top element of the stack
        """
        return self.stack[self.l-1]

    def full(self):
        """
        Is the stack full?
        """
        return self.l == self.n
        # if self.l == self.n:
        #    return True
        # return False

    def empty(self):
        """
        Is the stack empty?
        """
        return self.l == 0
        #if self.l == 0:
        #    return True
        #return False

    def size(self):
        """
        Return size of the stack
        """
        return self.l
temp = []
clean = ''

stacks = []
for i in range(0,9):
    stacks.append(Stack(56))

instructions = []

with open('D:/USFQ/OneDrive - Universidad San Francisco de Quito/5. Quinto Semestre/Estructura de Datos/Github/cmp-3002-fall22-gona/Advent Of Code/input5.txt') as file_obj:
    inp = file_obj.readlines()
    for i in range(0,8):
        j = 1
        while j < 37:
            clean += inp[i][j]
            j += 4
        temp.append(clean)
        clean = ''
    i = 7
    while i > -1:
        for j in range(9):
            if(temp[i][j] != ' '):
                stacks[j].push(temp[i][j])
        i -= 1

    for k in range(10,len(inp)):
        clean = inp[k].replace('move ','')
        clean = clean.replace('\n','')
        clean = clean.replace(' from','')
        clean = clean.replace(' to','')
        instructions.append(clean)

for i in range (len(instructions)):
    num_pops = 0
    stack_from = 0
    stack_to = 0

    num = False
    from_ = False

    temp_str = ''

    for j in range(len(instructions[i])):
        if (instructions[i][j] != ' '):
            temp_str += instructions[i][j]

        if(instructions[i][j] == ' ' and not num and not from_):
            num = True
            num_pops = int(temp_str)
            temp_str = ''
        elif(instructions[i][j] == ' ' and num and not from_):
            from_ = True
            stack_from = int(temp_str)
            temp_str = ''            
    stack_to = int(temp_str)

    #print(str(num_pops)+str(stack_from)+str(stack_to))
    temp_stk = Stack(56)
    for j in range(num_pops):
        temp_stk.push(stacks[stack_from-1].pop())
    for j in range(num_pops):
        stacks[stack_to-1].push(temp_stk.pop())

#print(instructions)

print(stacks[0].pop())
print(stacks[1].pop())
print(stacks[2].pop())
print(stacks[3].pop())
print(stacks[4].pop())
print(stacks[5].pop())
print(stacks[6].pop())
print(stacks[7].pop())
print(stacks[8].pop())



