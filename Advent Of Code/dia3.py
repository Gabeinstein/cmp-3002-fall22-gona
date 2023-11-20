
pocket1 = []
pocket2 = []
repeat = []
repeat3 = []

with open('D:/USFQ/OneDrive - Universidad San Francisco de Quito/5. Quinto Semestre/Estructura de Datos/Github/cmp-3002-fall22-gona/Advent Of Code/input3.txt') as file_obj:
    inp = file_obj.readlines()
    i = 0
    while i < len(inp):
        found = False
        for j in range(len(inp[i].replace('\n', ''))):
            for k in range(len(inp[i+1].replace('\n', ''))):
                for m in range(len(inp[i+2].replace('\n', ''))):
                    if (inp[i][j] == inp [i+1][k]) and (inp[i+1][k] == inp[i+2][m]):
                        repeat3.append(inp[i][j])
                        found = True
                        break
                if found:
                    break
            if found:
                break

        i += 3


    for i in range (len(inp)):
        pocket1.append((inp[i][0:((len(inp[i])//2))]).replace('\n', ''))
        pocket2.append((inp[i][(len(inp[i])//2):len(inp[i])-1]).replace('\n', ''))

        found = False

        for j in range (len(pocket1[i])):
            for k in range(len(pocket2[i])):
                if (pocket1[i][j] == pocket2[i][k]):
                    repeat.append(pocket1[i][j])
                    found = True
                    break
            
            if found:
                break


print(pocket1[0]+pocket2[0])
print(pocket1[1]+pocket2[1])
print(pocket1[2]+pocket2[2])
print(" ")
print(repeat3[0])

print(ord('M')-38)

priorities = []

for i in range(len(repeat3)):
    if ord(repeat3[i]) > 90:
        priorities.append(ord(repeat3[i])-96)
    if ord(repeat3[i]) <= 90:
        priorities.append(ord(repeat3[i])-38)
sum_total = 0
for i in range(len(priorities)):
    sum_total += priorities[i]
    
print(sum_total)
