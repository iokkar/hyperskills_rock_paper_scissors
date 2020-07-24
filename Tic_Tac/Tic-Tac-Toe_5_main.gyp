board = [' ' for i in range(9)]
matrix = [board[i:i + 3] for i in range(0, len(board), 3)]
numbers = [str(i) for i in range(10)]
i_coords = [str(i) for i in range(1, 4)]
x, y = 0, 0
symb = "O"

# переменныи для проверки статуса
stateGame = 'game'
printState = 'Game not finished'
win_coords = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 4, 7), (2, 5, 8), (3, 6, 9), (1, 5, 9), (3, 5, 7)]

# глобальная переменная для остановки цикла/игры (не тестировалась)
check = False


def print_board():
    print('-' * 9)
    for i in range(len(matrix)):
        print('|', end=' ')
        for j in range(len(matrix[i])):
            print(matrix[i][j], end=' ')
        print('|')
    print('-' * 9)


def check_input():  # нужна интеграция с шт
    global coords, matrix, x, y, symb, check
    check = False

    while check != True:
        coords = input('Enter the coordinates:').split()
        if any([i for i in coords if i not in numbers]) or len(coords) != 2:
            print('You should enter numbers!')
        elif any([i for i in coords if i not in i_coords]):
            print('Coordinates should be from 1 to 3!')
        else:
            x, y = coords
            if matrix[3 - int(y)][int(x) - 1] == ' ' and coords[0] and coords[1] in i_coords:
                if symb == 'O':
                    matrix[3 - int(y)][int(x) - 1] = 'X'
                    symb = 'X'
                    check = True  # скорее всего не срабатывает
                elif symb == 'X':
                    matrix[3 - int(y)][int(x) - 1] = 'O'
                    symb = 'O'
                    check = True
                coords = [int(i) for i in coords]
                x, y = coords
                check_win('X')  # тестирую проверку внутри функции
                check_win('O')
                check_draw()
                break
            else:
                print('This cell is occupied! Choose another one!')


def check_draw():  # из check_state оставил только проверку ничьи
    global stateGame, printState, check
    board = [j for i in matrix for j in i]

    if stateGame == 'game':
        for i in win_coords:
            X = ((board[i[0] - 1]), (board[i[1] - 1]), (board[i[2] - 1])).count('X')
            O = ((board[i[0] - 1]), (board[i[1] - 1]), (board[i[2] - 1])).count('O')
            if ' ' not in board and X <= 3 and O <= 3:  # !=3 заменил на <=3
                stateGame = 'draw'
                printState = 'Draw'
                check = True
    else:
        return


# заменил board на matrix
def check_win(symb):
    global stateGame, printState, check
    board = [j for i in matrix for j in i]
    for i in win_coords:
        if (board[i[0] - 1]) == (board[i[1] - 1]) == (board[i[2] - 1]) == symb:
            stateGame = 'win'
            printState = board[i[0] - 1] + ' wins'
            # тест
            check = True


def game():
    global board, matrix, x, y
    while stateGame == 'game':  # тестовый параметр для проверки
        print_board()
        check_input()
        if stateGame != 'game':
            print_board()
            print(printState)


game()
