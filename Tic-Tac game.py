board = [' ' for i in range(9)]
player1 = 'X'
player2 = 'O'


def print_board():
    row1 = '|{}|{}|{}|'.format(board[0], board[1], board[2])
    row2 = '|{}|{}|{}|'.format(board[3], board[4], board[5])
    row3 = '|{}|{}|{}|'.format(board[6], board[7], board[8])
    print(row1)
    print(row2)
    print(row3)


def make_move(position, player):
    board[position] = player


def is_winner(player):
    # горизонтальные строки
    if board[0] == player and board[1] == player and board[2] == player:
        return True
    if board[3] == player and board[4] == player and board[5] == player:
        return True
    if board[6] == player and board[7] == player and board[8] == player:
        return True
    # вертикальные строки
    if board[0] == player and board[3] == player and board[6] == player:
        return True
    if board[1] == player and board[4] == player and board[7] == player:
        return True
    if board[2] == player and board[5] == player and board[8] == player:
        return True
    # диагонали
    if board[0] == player and board[4] == player and board[8] == player:
        return True
    if board[2] == player and board[4] == player and board[6] == player:
        return True
    return False


def play_game():
    print_board()  # выводим доску на экран
    while True:
        # ход игрока 1
        position = int(input('Ход игрока 1 (1-9): ')) - 1
        make_move(position, player1)
        print_board()
        if is_winner(player1):
            print('Игрок 1 победил!')
            break
        # ход игрока 2
        position = int(input('Ход игрока 2 (1-9): ')) - 1
        make_move(position, player2)
        print_board()
        if is_winner(player2):
            print('Игрок 2 победил!')
            break

play_game()
