def check(value):
    is_equal = False
    for i in range(len(value)):
        for j in range(len(value)):
            if i != j and value[i] != value[j]:
                is_equal = False
            elif i != j and value[i] == value[j]:
                is_equal = True
                break
        if is_equal:
            break
    return is_equal

with open('D:/USFQ/OneDrive - Universidad San Francisco de Quito/5. Quinto Semestre/Estructura de Datos/Github/cmp-3002-fall22-gona/Advent Of Code/input6.txt') as file_obj:
    inp = file_obj.readlines()
    count = 0
    cache = ''

    for i in range(len(inp[0])-13):
        cache = inp[0][i:i+14]
        if not check(cache):
            count = i+14
            break
    print(count)

    