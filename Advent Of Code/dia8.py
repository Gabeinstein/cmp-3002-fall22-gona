A = []
with open('D:/USFQ/OneDrive - Universidad San Francisco de Quito/5. Quinto Semestre/Estructura de Datos/Github/cmp-3002-fall22-gona/Advent Of Code/input8.txt') as file_obj:
    inp = file_obj.readlines()
    for i in range(len(inp)):
        A.append(inp[i].replace('\n',''))

height = len(A)
width = len(A[0])

count = []
y_pos = 0
y_neg = 0
x_pos = 0
x_neg = 0

'''
A.clear()
A.append('30373')
A.append('25512')
A.append('65332')
A.append('33549')
A.append('35390')
height =5
width = 5
'''

for i in range(height):
    for j in range(width):
        if i != 0 and j != 0 and i != height-1 and j != width -1:
            for k in reversed(range(0,i)):
                if int(A[i][j]) <= int(A[k][j]):
                    y_pos = i-k
                    break
                else:
                    y_pos = i
            for k in range(i+1,height):
                if int(A[i][j]) <= int(A[k][j]):
                    y_neg = k-i
                    break
                else:
                    y_neg = height-1-i
            for k in reversed(range(0,j)):
                if int(A[i][j]) <= int(A[i][k]):
                    x_neg = j-k
                    break
                else:
                    x_neg = j
            for k in range(j+1,width):
                if int(A[i][j]) <= int(A[i][k]):
                    x_pos = k-j
                    break
                else:
                    x_pos = width-1-j

            count.append(x_neg*x_pos*y_neg*y_pos)
            
        #elif i == 0 or j == 0 or i == height-1 or j == width -1:
         #   count += 1

max_ = 0
for i in range (len(count)):
    if count[i] >= max_:
        max_ = count[i]
print (max_)