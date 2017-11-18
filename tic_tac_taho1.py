import random
import sys
from colorsys import *



def header():
    
    print("\033[1;32m               _____ _           _____               _____     _           \033[1;m")
    print("\033[1;32m              |_   _(_)         |_   _|             |_   _|   | |           \033[1;m")
    print("\033[1;32m                | |  _  ___ ______| | __ _  ___ ______| | __ _| |__   ___   \033[1;m")
    print("\033[1;32m                | | | |/ __|______| |/ _` |/ __|______| |/ _` | '_ \ / _ \   \033[1;m")
    print("\033[1;32m                | | | | (__       | | (_| | (__       | | (_| | | | | (_) |  \033[1;m")
    print("\033[1;32m                \_/ |_|\___|      \_/\__,_|\___|      \_/\__,_|_| |_|\___/    \033[1;m")
    print("\033[1;32m                                                                               \033[1;m")
    print("\033[1;32m                                                                          \033[1;m")
    print("\033[1;32m                 _____                _           _   _            \033[1;m")
    print("\033[1;32m                /  __ \              | |         | | | |            \033[1;m")
    print("\033[1;32m                | /  \/_ __ ___  __ _| |_ ___  __| | | |__  _   _   \033[1;m")
    print("\033[1;32m                | |   | '__/ _ \/ _` | __/ _ \/ _` | | '_ \| | | |    \033[1;m")
    print("\033[1;32m                | \__/| | |  __| (_| | ||  __| (_| | | |_) | |_| |    \033[1;m")
    print("\033[1;32m                 \____|_|  \___|\__,_|\__\___|\__,_| |_.__/ \__, |    \033[1;m")
    print("\033[1;32m                                                             __/ |    \033[1;m")
    print("\033[1;32m                                                            |___/      \033[1;m")
    print("\033[1;32m                ______            _     _                   _  ___  ___      _  \033[1;m")
    print("\033[1;32m                |  _  \          (_)   | |                 | | |  \/  |     | |      \033[1;m")
    print("\033[1;32m                | | | |__ ___   ___  __| |   __ _ _ __   __| | | .  . | __ _| |_ ___ \033[1;m")
    print("\033[1;32m                | | | / _` \ \ / | |/ _` |  / _` | '_ \ / _` | | |\/| |/ _` | __/ _ \ \033[1;m")
    print("\033[1;32m                | |/ | (_| |\ V /| | (_| | | (_| | | | | (_| | | |  | | (_| | ||  __/ \033[1;m")
    print("\033[1;32m                |___/ \__,_| \_/ |_|\__,_|  \__,_|_| |_|\__,_| \_|  |_/\__,_|\__\___| \033[1;m")


def check_board(board, s):
    return board[6] == s and board[7] == s and board[8] == s or \
        board[3] == s and board[4] == s and board[5] == s or \
        board[0] == s and board[1] == s and board[2] == s or \
        board[6] == s and board[3] == s and board[0] == s or \
        board[7] == s and board[4] == s and board[1] == s or \
        board[8] == s and board[5] == s and board[2] == s or \
        board[6] == s and board[4] == s and board[2] == s or \
        board[8] == s and board[4] == s and board[0] == s


def help():
    print('TIC TAC TOE HELP')
    show(["1", "2", "3", "4", "5", "6", "7", "8", "9"])
    print('REMEMBER,AFTER EACH ROUND PLAYERS SWAP POSITION.')
    print('SECOND PLAYER GOES FIRST,FIRST GOES SECOND AND SO ON.')


def getchar():
    import sys
    import tty
    import termios
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        return sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)

def show(board):
    print('\n\033[1;35m|-----------|\033[1;m')
    print('\033[1;35m|\033[1;m', board[6], '\033[1;35m|\033[1;m', board[7], '\033[1;35m|\033[1;m', board[8], '\033[1;35m|\033[1;m')
    print('\033[1;35m|-----------|\033[1;m')
    print('\033[1;35m|\033[1;m', board[3], '\033[1;35m|\033[1;m', board[4], '\033[1;35m|\033[1;m', board[5], '\033[1;35m|\033[1;m')
    print('\033[1;35m|-----------|\033[1;m')
    print('\033[1;35m|\033[1;m', board[0], '\033[1;35m|\033[1;m', board[1], '\033[1;35m|\033[1;m', board[2], '\033[1;35m|\033[1;m')
    print('\033[1;35m|-----------|\033[1;m\n')


def choose_name():
    ply1 = None
    ply2 = None
    while ply1 == ply2:
        ply1 = input("Your name: ")
        ply2 = input("Your name: ")
        if ply1 == ply2:
            print('Try different name!')
    for i in range(1, 2):
        sorszam = (random.randrange(2) + 1)
        if sorszam == 1:
            print('\n' + ply1 + ' goes first!')
        else:
            temp = ply1
            ply1 = ply2
            ply2 = temp
            print('\n' + ply1 + ' goes first!')
    print('\n' + ply1 + '  vs  ' + ply2)
    return [ply1, ply2]


def block_cond(board, s):
    for i in range(0, 9, 3):
        if board[i] == s and board[i + 1] == s and board[i + 2] == ' ':
            return i + 2
        if board[i] == ' ' and board[i + 1] == s and board[i + 2] == s:
            return i
    for i in range(0, 3):
        if board[i] == s and board[i + 3] == s and board[i + 6] == ' ':
            return i + 6
        if board[i] == ' ' and board[i + 3] == s and board[i + 6] == s:
            return i
    if board[0] == s and board[4] == s and board[8] == ' ':
        return 8
    if board[0] == ' ' and board[4] == s and board[8] == s:
        return 0
    if board[2] == s and board[4] == s and board[6] == ' ':
        return 6
    if board[2] == ' ' and board[4] == s and board[6] == s:
        return 2
    if board[0] == s and board[6] == s and board[3] == ' ':
        return 3
    if board[5] == ' ' and board[2] == s and board[8] == s:
        return 5
    if board[6] == s and board[8] == s and board[7] == ' ':
        return 7
    if board[1] == ' ' and board[2] == s and board[0] == s:
        return 1
    return -1


def choose_nameai():
    ply1 = None
    ply2 = None
    while ply1 == ply2:
        ply1 = input("Your name: ")
        ply2 = str("Pisti")
        if ply1 == ply2:
            print('Try different name!')
    print('\n' + ply1 + '  vs  ' + ply2)
    return [ply1, ply2]


def first_playermove(board):
    while True:
        print("Please select a spot")
        choice = getchar()
        try:
            choice = int(choice)
        except:
            print("thats not a number")
            continue
        if board[choice - 1] != 'X' and board[choice - 1] != 'O':
            board[choice - 1] = 'X'
            return False
        else:
            print("this spot is taken")
        show(board)


def second_playermove(board):
    while True:
        print("Please select a spot")
        choice = getchar()
        try:
            choice = int(choice)
        except:
            print("thats not a number")
            continue
        if board[choice - 1] != 'X' and board[choice - 1] != 'O':
            board[choice - 1] = 'O'
            return False
        else:
            print("this spot is taken")
        show(board)


def gameai(board):

    if board[4] == " ":
        board[4] = 'O'
        return 'O'
    ai_win = block_cond(board, "O")
    ai_move = block_cond(board, "X")

    if ai_win != -1:
        board[ai_win] = "O"
        return
    elif ai_move != -1:
        board[ai_move] = "O"
        return

    else:
        while True:
            corner_moves= [0,2,6,8]
            move = random.choice(corner_moves)
            if board[move] != 'X' and board[move] != 'O':
                board[move] = 'O'
                return False
            else:
                continue
            show(board)


def game_pvp():
    p1, p2 = choose_name()
    xwinner = 0
    owinner = 0
    tie = 0
    while True:
        print('\nPress any key to start or "q" to quit or "h" for help: ')
        board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
        ex = getchar()
        if ex == "q":
            break
        if ex == "h":
            help()
            continue
        owin = False
        xwin = False
        roundend = 0
        while roundend < 1:
            nextplayer = 0
            while nextplayer < 1:
                show(board)
                first_playermove(board)
                show(board)
                nextplayer += 1
                if check_board(board, "X"):
                    show(board)
                    roundend += 1
                    xwinner += 1
                    print("\nX wins")
                    print(p1 + " wins:%d " % (xwinner) + '\n' + p2 +
                          " wins:%d " % (owinner) + '\n' + "Tie:%d" % (tie))
                    xwin = True
                    temp = p1
                    p1 = p2
                    p2 = temp
                    temp2 = xwinner
                    xwinner = owinner
                    owinner = temp2
                    break
            if xwin == True:
                break
                show(board)
            if " " not in board:
                tie += 1
                print("\nTie")
                print(p1 + " wins:%d " % (xwinner) + '\n' + p2 + " wins:%d " %
                      (owinner) + '\n' + "Tie:%d" % (tie))
                break
            while nextplayer == 1:
                show(board)
                second_playermove(board)
                show(board)
                nextplayer -= 1
                if check_board(board, "O"):
                    show(board)
                    roundend += 1
                    owinner += 1
                    print("\nO wins")
                    print(p1 + " wins:%d " % (xwinner) + '\n' + p2 +
                          " wins:%d " % (owinner) + '\n' + "Tie:%d" % (tie))
                    owin = True
                    temp = p1
                    p1 = p2
                    p2 = temp
                    temp2 = owinner
                    owinner = xwinner
                    xwinner = temp2
                    break
            if owin == True:
                break
                show(board)
            if " " not in board:
                tie += 1
                print("\nTie")
                print(p1 + " wins:%d " % (xwinner) + '\n' + p2 + " wins:%d " %
                      (owinner) + '\n' + "Tie:%d" % (tie))
                temp = p1
                p1 = p2
                p2 = temp
                break


def game_comp():
    p1, p2 = choose_nameai()
    xwinner = 0
    owinner = 0
    tie = 0
    while True:
        print('\nPress any key to start or "q" to quit or "h" for help: ')
        board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
        ex = getchar()
        if ex == "q":
            break
        if ex == "h":
            help()
            continue
        owin = False
        xwin = False
        while True:
            show(board)
            first_playermove(board)
            if check_board(board, "X"):
                show(board)
                xwinner += 1
                print(p1 + " wins:%d " % (xwinner) + '\n' + p2 + " wins:%d " %
                      (owinner) + '\n' + "Tie:%d" % (tie))
                xwin = True
                break
            elif " " not in board:
                tie += 1
                print("\nTie")
                print(p1 + " wins:%d " % (xwinner) + '\n' + p2 + " wins:%d " %
                      (owinner) + '\n' + "Tie:%d" % (tie))
                show(board)
                break
            show(board)
            gameai(board)
            if check_board(board, "O"):
                show(board)
                owinner += 1
                print(p1 + " wins:%d " % (xwinner) + '\n' + p2 + " wins:%d " %
                      (owinner) + '\n' + "Tie:%d" % (tie))
                owin = True
                break
            if " " not in board:
                tie += 1
                print("\nTie")
                print(p1 + " wins:%d " % (xwinner) + '\n' + p2 + " wins:%d " %
                      (owinner) + '\n' + "Tie:%d" % (tie))
                show(board)
                break


header()
while True:
    k = input("\n2player or ai or q for exit: ")
    if k == "2player":
        game_pvp()
    elif k == "ai":
        game_comp()
    elif k == "q":
        break
    else:
        print("Please make sure you type the correct word!")
        continue