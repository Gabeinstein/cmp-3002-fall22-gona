A = []
rock = 'A'
paper = 'B'
scissors = 'C'

def result(juego):
    if (juego[2] == 'X'):
        if (juego[0] == 'A'):
            return 'A Z'
        elif (juego[0] == 'B'):
            return 'B X'
        elif (juego[0] == 'C'):
            return 'C Y'

    if (juego[2] == 'Y'):
        if (juego[0] == 'A'):
            return 'A X'
        elif (juego[0] == 'B'):
            return 'B Y'
        elif (juego[0] == 'C'):
            return 'C Z'

    if (juego[2] == 'Z'):
        if (juego[0] == 'A'):
            return 'A Y'
        elif (juego[0] == 'B'):
            return 'B Z'
        elif (juego[0] == 'C'):
            return 'C X'
        

def is_win(juego):
    if (juego == 'A Y'):
        return True
    elif (juego == 'B Z'):
        return True
    elif (juego == 'C X'):
        return True
    else:
        return False

def is_draw(juego):
    if (juego == 'A X'):
        return True
    elif (juego == 'B Y'):
        return True
    elif (juego == 'C Z'):
        return True
    else:
        return False

def is_lose(juego):
    if (juego == 'A Z'):
        return True
    elif (juego == 'B X'):
        return True
    elif (juego == 'C Y'):
        return True
    else:
        return False

sum_plays = 0
sum_choose = 0
sum_total = 0

choose_match = []
with open('D:/USFQ/OneDrive - Universidad San Francisco de Quito/5. Quinto Semestre/Estructura de Datos/Github/cmp-3002-fall22-gona/Advent Of Code/input2.txt') as file_obj:
    inp = file_obj.readlines()
  
    for i in range(len(inp)):

        choose_match.append(result(inp[i]))

        if is_win(choose_match[i].replace('\n','')):
            sum_plays += 6
        if is_draw(choose_match[i].replace('\n','')):
            sum_plays += 3

        #sum_plays += result(inp[i].replace('\n',''))

        if choose_match[i][2] == 'X':
            sum_choose += 1
        if choose_match[i][2] == 'Y':
            sum_choose += 2
        if choose_match[i][2] == 'Z':
            sum_choose += 3
    print(choose_match)
sum_total = sum_plays + sum_choose
print(sum_total)