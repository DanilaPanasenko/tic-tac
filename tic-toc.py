#поле битвы
battl = [1, 2, 3,
         4, 5, 6,
         7, 8, 9]
#победные комбинации
battl_win = [[0, 1, 2],
             [3, 4, 5],
             [6, 7, 8],
             [0, 3, 6],
             [1, 4, 7],
             [2, 5, 8],
             [0, 4, 8],
             [6, 4, 2]]
#вывод поля битвы
def print_battl():
    print(battl[0], battl[1], battl[2], sep= " | ")
    print(battl[3], battl[4], battl[5], sep= " | ")
    print(battl[6], battl[7], battl[8], sep= " | ")
print_battl()
game = True # Активна ли игра
N = 9 # Количество оставшихся ходов
# Функция определяющаяя победителя
def chec_winner():
    for i in battl_win:
        global game
        if battl[i[0]] == 'X' and battl[i[1]] == 'X' and battl[i[2]] == 'X':
            print("Игрок 1 победил ")
            game = False
        elif battl[i[0]] == 'O' and battl[i[1]] == 'O' and battl[i[2]] == 'O':
            print("Игрок 2 победил ")
            game = False
# Функция отвечвающая за ход и замену на символ
def step(number, symbol, player):
    global N
    if battl[number - 1] != 'X' and battl[number - 1] != 'O':
        battl[number - 1] = symbol
        chec_winner()
        print_battl()
        N -= 1
    else:
        print('Ячейка занята')
        c = int(input(f'Игрок {player} введите номер({symbol}): '))
        step(c, symbol, player)
# Основной цикл игры
while game == True:
    if game == True and N > 0:
        a = int(input('Игрок 1 введите номер(X): '))
        step(a, 'X', 1)
    elif N == 0:
        print('Ничья')
        game = False
    if game == True and N > 0:
        b = int(input('Игрок 2 введите номер(O): '))
        step(b, 'O', 2)
    elif N == 0:
        print('Ничья')
        game = False





