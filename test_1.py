def newBoard():
    plateau = [[0] * 10 for i in range(8)]  # creation d'un tableau vide de 0 de longueur n*n
    return plateau


def display(gameBoard):
    for ligne in gameBoard:
        for x in ligne:
            print(x, ' ', end='')
        print('\n')


def classic(plateau):
    # Sphinx rouge
    plateau[0][0] = [5, 's', 1]
    # Sphinx blanc
    plateau[7][9] = [5, 'n', 2]
    # Anubis rouge
    plateau[0][4] = [3, 's', 1]
    plateau[0][6] = [3, 's', 1]
    # Anubis blanc
    plateau[7][3] = [3, 'n', 2]
    plateau[7][5] = [3, 'n', 2]
    # Pharaoh rouge
    plateau[0][5] = [1, 's', 1]
    # Pharaoh blanc
    plateau[7][4] = [1, 'n', 2]
    # Pyramid rouge
    plateau[1][2] = [4, 'so', 1]
    plateau[0][7] = [4, 'se', 1]
    plateau[3][0] = [4, 'ne', 1]
    plateau[4][0] = [4, 'se', 1]
    plateau[3][7] = [4, 'se', 1]
    plateau[4][7] = [4, 'ne', 1]
    plateau[5][6] = [4, 'se', 1]
    # Pyramid blanc
    plateau[6][7] = [4, 'ne', 2]
    plateau[7][2] = [4, 'no', 2]
    plateau[3][9] = [4, 'so', 2]
    plateau[4][9] = [4, 'no', 2]
    plateau[3][2] = [4, 'so', 2]
    plateau[4][2] = [4, 'no', 2]
    plateau[2][3] = [4, 'no', 2]
    # Scarab rouge
    plateau[3][4] = [2, 'no', 1]
    plateau[3][5] = [2, 'ne', 1]
    # Scarab blanc
    plateau[4][4] = [2, 'so', 2]
    plateau[4][5] = [2, 'se', 2]
    # Camp rouge
    plateau[1][0], plateau[2][0], plateau[5][0], plateau[6][0], plateau[7][0], plateau[0][8], plateau[7][
        8] = 1, 1, 1, 1, 1, 1, 1
    # Camp blanc
    plateau[0][9], plateau[1][9], plateau[2][9], plateau[5][9], plateau[6][9], plateau[0][1], plateau[7][
        1] = 2, 2, 2, 2, 2, 2, 2


def rotation(joueur, plateau):
    x = eval(input('Choisir ligne')) - 1
    y = eval(input('Choisir colonne')) - 1
    while plateau[x][y] != 1 and plateau[x][y] != 2 and plateau[x][y] != 0 and plateau[x][y][2] != joueur:
        x = eval(input('Choisir ligne')) - 1
        y = eval(input('Choisir colonne')) - 1

    rotate = eval(input('1 pour rotate horaire, 2 pr anti horaire'))
    while rotate != 1 and rotate != 2:
        rotate = eval(input('1 pour rotate horaire, 2 pr anti horaire'))
    if plateau[x][y][1] == 'no':
        if rotate == 1:
            plateau[x][y][1] = 'ne'
        else:
            plateau[x][y][1] = 'so'
    elif plateau[x][y][1] == 'ne':
        if rotate == 1:
            plateau[x][y][1] = 'se'
        else:
            plateau[x][y][1] = 'no'
    elif plateau[x][y][1] == 'se':
        if rotate == 1:
            plateau[x][y][1] = 'so'
        else:
            plateau[x][y][1] = 'ne'
    elif plateau[x][y][1] == 'so':
        if rotate == 1:
            plateau[x][y][1] = 'no'
        else:
            plateau[x][y][1] = 'se'


def shoot(joueur, plateau):

    dir = ''
    x_init = ''
    y_init = ''
    count = 0
    inProgess = True
    while inProgess:
        if count == 0:
            for i in range(8):
                for j in range(10):
                    if plateau[i][j] != 0 and plateau[i][j] != 1 and plateau[i][j] != 2:
                        if plateau[i][j][0] == 5 and plateau[i][j][2] == joueur:
                            dir = plateau[i][j][1]
                            x_init = i
                            y_init = j
                            count = 1

        if dir == 'n':
            k=x_init
            aled = True
            while aled == True:
                k = k-1
                if k == -1:
                    aled = False
                    inProgess = False
                    break;
                if plateau[k][y_init] != 1 and plateau[k][y_init] != 2 and plateau[k][y_init] != 0:
                    if plateau[k][y_init][0] == 1:
                        print('rt ta perdu')
                        inProgess = False
                    elif plateau[k][y_init][0] == 2:
                        if plateau[k][y_init][1] == 'no':
                            dir = 'e'
                            aled = False
                            x_init = k
                        elif plateau[k][y_init][1] == 'ne':
                            dir = 'o'
                            aled = False
                            x_init = k
                        elif plateau[k][y_init][1] == 'se':
                            dir = 'e'
                            aled = False
                            x_init = k
                        elif plateau[k][y_init][1] == 'so':
                            dir = 'o'
                            aled = False
                            x_init = k

                    elif plateau[k][y_init][0] == 3:
                        if plateau[k][y_init][1] == 'n':
                            plateau[k][y_init] = 0
                            aled = False
                            inProgess = False
                            x_init = k
                        if plateau[k][y_init][1] == 'e':
                            plateau[k][y_init] = 0
                            aled = False
                            inProgess = False
                            x_init = k

                        if plateau[k][y_init][1] == 'o':
                            plateau[k][y_init] = 0
                            aled = False
                            inProgess = False
                            x_init = k

                        if plateau[k][y_init][1] == 's':
                            print('absorbed')
                            aled = False
                            inProgess = False
                            x_init = k

                    elif plateau[k][y_init][0] == 4:
                        if plateau[k][y_init][1] == 'no':
                            plateau[k][y_init] = 0
                            aled = False
                            inProgess = False
                            x_init = k
                        elif plateau[k][y_init][1] == 'ne':
                            plateau[k][y_init] = 0
                            aled = False
                            inProgess = False
                            x_init = k
                        elif plateau[k][y_init][1] == 'se':
                            dir = 'e'
                            aled = False
                            x_init = k
                        elif plateau[k][y_init][1] == 'so':
                            dir = 'o'
                            aled = False
                            x_init = k

                    elif plateau[k][y_init][0] == 5:
                        print('absorbed')
                        aled = False
                        inProgess = False
                        x_init = k
        if dir == 's':
            k = x_init
            aled = True
            while aled == True:
                k = k+1
                if k == 8:
                    print('PUTINNNNNNNNNNNNN')
                    aled=False
                    inProgess = False
                    break;

                if plateau[k][y_init] != 1 and plateau[k][y_init] != 2 and plateau[k][y_init] != 0:
                    if plateau[k][y_init][0] == 1:
                        print('rt ta perdu')
                        inProgess = False
                    elif plateau[k][y_init][0] == 2:
                        if plateau[k][y_init][1] == 'no':
                            dir = 'o'
                            aled = False
                            x_init = k
                        elif plateau[k][y_init][1] == 'ne':
                            dir = 'e'
                            aled = False
                            x_init = k
                        elif plateau[k][y_init][1] == 'se':
                            dir = 'o'
                            aled = False
                            x_init = k
                        elif plateau[k][y_init][1] == 'so':
                            dir = 'e'
                            aled = False
                            x_init = k

                    elif plateau[k][y_init][0] == 3:
                        if plateau[k][y_init][1] == 'n':
                            print('absorbed')
                            aled = False
                            inProgess = False
                            x_init = k

                        if plateau[k][y_init][1] == 'e':
                            plateau[k][y_init] = 0
                            aled = False
                            inProgess = False
                            x_init = k
                        if plateau[k][y_init][1] == 'o':
                            plateau[k][y_init] = 0
                            aled = False
                            inProgess = False
                            x_init = k

                        if plateau[k][y_init][1] == 's':
                            plateau[k][y_init] = 0
                            aled = False
                            inProgess = False
                            x_init = k

                    elif plateau[k][y_init][0] == 4:
                        if plateau[k][y_init][1] == 'no':
                            dir = 'o'
                            aled = False
                            x_init = k
                        elif plateau[k][y_init][1] == 'ne':
                            dir = 'e'
                            aled = False
                            x_init = k
                        elif plateau[k][y_init][1] == 'se':
                            plateau[k][y_init] = 0
                            inProgess = False
                            aled = False
                            x_init = k
                        elif plateau[k][y_init][1] == 'so':
                            plateau[k][y_init] = 0
                            aled = False
                            inProgess = False
                            x_init = k

                    elif plateau[k][y_init][0] == 5:
                        print('absorbed')
                        aled = False
                        inProgess = False
                        x_init = k

        if dir == 'o':
            k = y_init
            aled = True
            while aled == True:
                k = k-1
                if k == -1:
                    aled=False
                    inProgess = False
                    break;

                if plateau[x_init][k] != 1 and plateau[x_init][k] != 2 and plateau[x_init][k] != 0:
                    if plateau[x_init][k][0] == 1:
                        print('rt ta perdu')
                        inProgess = False
                    elif plateau[x_init][k][0] == 2:
                        if plateau[x_init][k][1] == 'no':
                            dir = 's'
                            aled = False
                            y_init = k
                        elif plateau[x_init][k][1] == 'ne':
                            dir = 'n'
                            aled = False
                            y_init = k
                        elif plateau[x_init][k][1] == 'se':
                            dir = 's'
                            aled = False
                            y_init = k
                        elif plateau[x_init][k][1] == 'so':
                            dir = 'n'
                            aled = False
                            y_init = k

                    elif plateau[x_init][k][0] == 3:
                        if plateau[x_init][k][1] == 'n':
                            plateau[x_init][k] = 0
                            aled = False
                            inProgess = False
                            y_init = k
                        if plateau[x_init][k][1] == 'e':
                            print('absorbed')
                            aled = False
                            inProgess = False
                            y_init = k

                        if plateau[x_init][k][1] == 'o':
                            plateau[x_init][k] = 0
                            aled = False
                            inProgess = False
                            y_init = k

                        if plateau[x_init][k][1] == 's':
                            plateau[x_init][k] = 0
                            aled = False
                            inProgess = False
                            y_init = k

                    elif plateau[x_init][k][0] == 4:
                        if plateau[x_init][k][1] == 'no':
                            plateau[x_init][k] = 0
                            aled = False
                            inProgess = False
                            y_init = k
                        elif plateau[x_init][k][1] == 'ne':
                            dir = 'n'
                            aled = False
                            y_init = k
                        elif plateau[x_init][k][1] == 'se':
                            dir = 's'
                            aled = False
                            y_init = k
                        elif plateau[x_init][k][1] == 'so':
                            plateau[x_init][k] = 0
                            aled = False
                            inProgess = False
                            y_init = k

                    elif plateau[x_init][k][0] == 5:
                        print('absorbed')
                        aled = False
                        inProgess = False
                        y_init = k

        if dir == 'e':
            k = y_init
            aled = True
            while aled == True:
                k = k+1
                if k == 10:
                    inProgess = False
                    aled=False
                    break;

                if plateau[x_init][k] != 1 and plateau[x_init][k] != 2 and plateau[x_init][k] != 0:
                    if plateau[x_init][k][0] == 1:
                        print('rt ta perdu')
                        inProgess=False
                    elif plateau[x_init][k][0] == 2:
                        if plateau[x_init][k][1] == 'no':
                            dir = 'n'
                            aled = False
                            y_init = k
                        elif plateau[x_init][k][1] == 'ne':
                            dir = 's'
                            aled = False
                            y_init = k
                        elif plateau[x_init][k][1] == 'se':
                            dir = 'n'
                            aled = False
                            y_init = k
                        elif plateau[x_init][k][1] == 'so':
                            dir = 's'
                            aled = False
                            y_init = k

                    elif plateau[x_init][k][0] == 3:
                        if plateau[x_init][k][1] == 'n':
                            plateau[x_init][k] = 0
                            aled = False
                            inProgess = False
                            y_init = k
                        if plateau[x_init][k][1] == 'e':
                           plateau[x_init][k] = 0
                           inProgess = False
                           aled = False
                           y_init = k

                        if plateau[x_init][k][1] == 'o':
                            print('absorbed')
                            aled = False
                            inProgess = False
                            y_init = k

                        if plateau[x_init][k][1] == 's':
                            plateau[x_init][k] = 0
                            aled = False
                            inProgess = False
                            y_init = k

                    elif plateau[x_init][k][0] == 4:
                        if plateau[x_init][k][1] == 'no':
                            dir = 'n'
                            aled = False
                            y_init = k
                        elif plateau[x_init][k][1] == 'ne':
                            plateau[x_init][k] = 0
                            aled = False
                            inProgess = False
                            y_init = k
                        elif plateau[x_init][k][1] == 'se':
                            plateau[x_init][k] = 0
                            aled = False
                            inProgess = False
                            y_init = k
                        elif plateau[x_init][k][1] == 'so':
                            dir = 's'
                            aled = False
                            y_init = k
                    elif plateau[x_init][k][0] == 5:
                        print('absorbed')
                        aled = False
                        inProgess = False
                        y_init = k


    print(dir, x_init, y_init)


def play(joueur, plateau):
    rotation(joueur, plateau)
    shoot(joueur,plateau)


def jeux():
    joueur = 1
    plateau = newBoard()
    classic(plateau)
    display(plateau)
    play(joueur,plateau)
    display(plateau)
jeux()
