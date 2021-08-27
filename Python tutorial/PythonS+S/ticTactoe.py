import random


def display_board(board):
    print('\n' * 5)
    for x in range(5):
        if x % 2:
            print("_ _ _")
        else:
            if x == 0:
                print(f"{board[7]}|{board[8]}|{board[9]}")
            elif x == 2:
                print(f"{board[4]}|{board[5]}|{board[6]}")
            else:
                print(f"{board[1]}|{board[2]}|{board[3]}")


#
test_board = ['#', 'X', 'O', 'X', 'O', 'X', 'O', 'X', '1', 'X']


# display_board(test_board)
def player_input(p1, p2):
    x = ''
    while x != "X" and x != "O":
        x = input(f"{p1} your Choose X or O: ").upper()

    return {p1: "X", p2: "O"} if x == "X" else {p1: "O", p2: "X"}


def player_name():
    p1 = input("Enter first player's name: ")
    p2 = input("Enter second player's name: ")
    return p1, p2


def place_marker(board, marker, position):
    board[position] = marker
    return board


def win_check(board, mark):
    nor = False
    lineStr = ''
    for line in range(3, 10, 3):
        for place in range(0, 3):
            lineStr += board[line - place]

        # print(lineStr)
        if lineStr == mark * 3:
            return True
        else:
            lineStr = ''
    for line in range(0, 3):
        for place in range(1, 8, 3):
            lineStr += board[line + place]
        # print(lineStr)
        if (lineStr == mark * 3):
            return True;
        else:
            lineStr = ''

    return ((board[7] == mark and board[5] == mark and board[3] == mark) or
            (board[9] == mark and board[5] == mark and board[1] == mark))


def choose_first(p1, p2):
    rand = random.randint(1, 2)
    print(rand)
    print(f"{p1} Go First" if rand == 1 else f"{p2} Go First")

    return rand


def space_check(board, position):
    return board[position] == 'X' or board[position] == "O"


def full_board_check(board):
    return ' ' in board


def player_choice(board, player):
    position = 0

    # while position not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not space_check(board, position):
    #     position = int(input('Choose your next position: (1-9) '))
    while True:
        position = int(input(f"{player} choose you move: "))
        if position not in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
            print("Please choose between 1-9")
        elif space_check(board, position):
            print(f"{position} is taken")
        else:

            return position


# player_choice(test_board)
# display_board(test_board)

def replay():
    return input("Replay ? (y/n)").lower().startswith('y')


print('Welcome to Tic Tac Toe!')
p1, p2 = player_name()

while True:
    board = [x for x in "0123456789"]
    display_board(board)
    print("How to play:")
    print("You have to input the number you want to replace")

    dictPlayer = player_input(p1, p2)
    # print(dictPlayer, board)
    board = list(map(lambda x: ' ', board))

    first = choose_first(p1, p2)

    display_board(board)

    for i in range(9):
        if first == 1:

            board = place_marker(board, dictPlayer[p1], player_choice(board, p1))
            display_board(board)
            first = 2
            if win_check(board, dictPlayer[p1]):
                print(f"{p1} has won!!!!!!!!!!!!!")
                break
        else:
            board = place_marker(board, dictPlayer[p2], player_choice(board, p2))
            display_board(board)
            first = 1
            if win_check(board, dictPlayer[p2]):
                print(f"{p2} has won!!!!!!!!!!!")
                break
    else:
        print("Draw!!!!!!")

    if not replay():
        break
