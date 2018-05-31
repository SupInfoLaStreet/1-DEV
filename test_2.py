#!/usr/bin/env python
# -*- coding: utf-8 -*-
aled_x = 0
aled_y = 0
global tab_possible_next
tab_possible_next = []
selected = False
from tkinter import *


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
    plateau[3][9] = [4, 'no', 2]
    plateau[4][9] = [4, 'so', 2]
    plateau[3][2] = [4, 'so', 2]
    plateau[4][2] = [4, 'no', 2]
    plateau[2][3] = [4, 'no', 2]
    # Scarab rouge
    plateau[3][4] = [2, 'so', 1]
    plateau[3][5] = [2, 'se', 1]
    # Scarab blanc
    plateau[4][4] = [2, 'se', 2]
    plateau[4][5] = [2, 'so', 2]
    # Camp rouge
    plateau[1][0], plateau[2][0], plateau[5][0], plateau[6][0], plateau[7][0], plateau[0][8], plateau[7][
        8] = 1, 1, 1, 1, 1, 1, 1
    # Camp blanc
    plateau[0][9], plateau[1][9], plateau[2][9], plateau[5][9], plateau[6][9], plateau[0][1], plateau[7][
        1] = 2, 2, 2, 2, 2, 2, 2

def rotate():
    print('ok')
    old_y = test_temp // 10
    old_x = (test_temp % 10) - 1
    if old_x + 1 == 0:
        old_x = 9
        old_y -= 1
    if plat[old_y][old_x][0] == 5:
        print('ok sphinx')
        if plat[old_y][old_x][1] == 's':
            plat[old_y][old_x][1] = 'e'

        elif plat[old_y][old_x][1] == 'e':
            plat[old_y][old_x][1] = 's'

        elif plat[old_y][old_x][1] == 'n':
            plat[old_y][old_x][1] = 'o'

        elif plat[old_y][old_x][1] == 'o':
            plat[old_y][old_x][1] = 'n'
    else:
        button_rotate_horaire.pack()
        button_rotate_anti_horaire.pack()


def rotate_horaire():
    old_y = test_temp // 10
    old_x = (test_temp % 10) - 1
    if old_x + 1 == 0:
        old_x = 9
        old_y -= 1


    if plat[old_y][old_x][1] == 's':
        plat[old_y][old_x][1] = 'o'

    elif plat[old_y][old_x][1] == 'e':
        plat[old_y][old_x][1] = 's'

    elif plat[old_y][old_x][1] == 'n':
        plat[old_y][old_x][1] = 'e'

    elif plat[old_y][old_x][1] == 'o':
        plat[old_y][old_x][1] = 'n'


    elif plat[old_y][old_x][1] == 'no':
        plat[old_y][old_x][1] = 'ne'

    elif plat[old_y][old_x][1] == 'ne':
        plat[old_y][old_x][1] = 'se'

    elif plat[old_y][old_x][1] == 'se':
        plat[old_y][old_x][1] = 'so'

    elif plat[old_y][old_x][1] == 'so':
        plat[old_y][old_x][1] = 'no'

    display(plat)


def rotate_anti_horaire():
    old_y = test_temp // 10
    old_x = (test_temp % 10) - 1
    if old_x + 1 == 0:
        old_x = 9
        old_y -= 1

    if plat[old_y][old_x][1] == 's':
        plat[old_y][old_x][1] = 'e'

    elif plat[old_y][old_x][1] == 'e':
        plat[old_y][old_x][1] = 'n'

    elif plat[old_y][old_x][1] == 'n':
        plat[old_y][old_x][1] = 'o'

    elif plat[old_y][old_x][1] == 'o':
        plat[old_y][old_x][1] = 's'

    elif plat[old_y][old_x][1] == 'no':
        plat[old_y][old_x][1] = 'so'

    elif plat[old_y][old_x][1] == 'ne':
        plat[old_y][old_x][1] = 'no'

    elif plat[old_y][old_x][1] == 'se':
        plat[old_y][old_x][1] = 'ne'

    elif plat[old_y][old_x][1] == 'so':
        plat[old_y][old_x][1] = 'se'

    display(plat)

##Var gloable

def test_select():
    print('OK BUTTON')
    global selected
    selected = True
    print('TABLEAU', tab_possible_next)
    canvas.itemconfig(test_temp, outline='green', width='2')


board_graph = [[0] * 10 for i in range(8)]
tab_cord = [[0] * 10 for i in range(8)]
fenetre = Tk()
var = StringVar()
var.set('hello')
fenetre.geometry("700x700")
canvas = Canvas(fenetre, width=550, height=500, background='yellow')
add_x, add_y = 0, 0
button_move = Button(fenetre, text="Bouger le pion", state=DISABLED, command=test_select)
button_rotate = Button(fenetre, text="Pivoter le pion", state=DISABLED, command=rotate)
button_rotate_horaire = Button(fenetre, text="Pivoter dans le sens horaire",command =rotate_horaire)
button_rotate_anti_horaire = Button(fenetre, text="Pivoter dans le sens antihoraire",command = rotate_anti_horaire)
label = Label(fenetre, text="Sens :")
text_sens = Label(fenetre, textvariable=var)


def selected_move(x, y, plateau, player):
    old_y = test_temp // 10
    old_x = (test_temp % 10) - 1
    new_case = (y * 10) + (x + 1)
    if old_x + 1 == 0:
        old_x = 9
        old_y -= 1

    for i in range(len(tab_possible_next)):
        if new_case == tab_possible_next[i]:
            new_y = tab_possible_next[i] // 10
            new_x = (tab_possible_next[i] % 10) - 1
            if (plateau[new_y][new_x][0] == 3 or plateau[new_y][new_x][0] == 4) and plateau[old_y][old_x][0] == 2 and plateau[new_y][new_x][2] == player:
                temp = plateau[new_y][new_x]
                plateau[new_y][new_x] = plateau[old_y][old_x]
                plateau[old_y][old_x] = temp
                temp = ''
            else:
                print('OK C LA BONNE CASE')
                print('OK NEW X ET Y  :', new_x, new_y, old_x, old_y)
                print('value 1', plateau[new_y][new_x])
                print('value 2', plateau[old_y][old_x])
                plateau[new_y][new_x] = plateau[old_y][old_x]
                plateau[old_y][old_x] = 0
                print('value 1', plateau[new_y][new_x])
                print('value 2', plateau[old_y][old_x])
                graphTranslation(plateau)
                display(plateau)  # creation du tableau graphique (loop de rectangle)
for i in range(8):
    for j in range(10):
        board_graph[i][j] = canvas.create_rectangle(add_x, add_y, add_x + 50, add_y + 50)
        add_x += 52
    add_x = 0
    add_y += 52

count = 0

for k in range(8):
    for l in range(10):
        count += 1
        tab_cord[k][l] = (canvas.coords(count))


# fonction selection click
def select(x, y, plateau, player):
    print('ALED', x, y)
    if plateau[y][x] != 0 and plateau[y][x] != 1 and plateau[y][x] != 2:
        var.set(str(plateau[y][x][1]))
    possible_next(x, y, plateau, player)


# fonction pour afficher en surbrillance les deplacements possibles (non finie)
def possible_next(x, y, plateau, player):
    print(selected)
    count = (x * 10) + (y + 1)
    print('OMG ', x, y)

    if plateau[y][x] != 0 and plateau[y][x] != 1 and plateau[y][x] != 2:
        if plateau[y][x][0] != 5:
            if plateau[y][x][2] == player:
                if x == 0:
                    for i in range(80):
                        canvas.itemconfig(i, outline='black', width='0')
                    global test_temp
                    test_temp = (y * 10) + (x + 1)
                    if plateau[y + 1][x] == 0:
                        print('COLOR')
                        count = ((y + 1) * 10) + (x + 1)
                        canvas.itemconfig(count, outline='red', width='2')
                        button_move['state'] = 'normal'
                        button_rotate['state'] = 'normal'
                        tab_possible_next.append(count)


                    else:
                        if plateau[y + 1][x] == 1 or plateau[y + 1][x] == 2:
                            if plateau[y + 1][x] == player:
                                count = ((y + 1) * 10) + (x + 1)
                                canvas.itemconfig(count, outline='red', width='2')
                                button_move['state'] = 'normal'
                                button_rotate['state'] = 'normal'
                                tab_possible_next.append(count)

                        elif plateau[y][x][0] == 2:
                            if (plateau[y + 1][x][0] == 3 or plateau[y + 1][x][0] == 4) and plateau[y + 1][x][
                                2] == player:
                                count = ((y + 1) * 10) + (x + 1)
                                canvas.itemconfig(count, outline='red', width='2')
                                button_move['state'] = 'normal'
                                button_rotate['state'] = 'normal'
                                tab_possible_next.append(count)

                    if plateau[y - 1][x] == 0:
                        print('COLOR')
                        count = ((y - 1) * 10) + (x + 1)
                        canvas.itemconfig(count, outline='red', width='2')
                        button_move['state'] = 'normal'
                        button_rotate['state'] = 'normal'
                        tab_possible_next.append(count)
                    else:
                        if plateau[y - 1][x] == 1 or plateau[y - 1][x] == 2:
                            if plateau[y - 1][x] == player:
                                count = ((y - 1) * 10) + (x + 1)
                                canvas.itemconfig(count, outline='red', width='2')
                                button_move['state'] = 'normal'
                                button_rotate['state'] = 'normal'
                                tab_possible_next.append(count)
                        elif plateau[y][x][0] == 2:
                            if (plateau[y - 1][x][0] == 3 or plateau[y - 1][x][0] == 4) and plateau[y - 1][x][
                                2] == player:
                                count = ((y - 1) * 10) + (x + 1)
                                canvas.itemconfig(count, outline='red', width='2')
                                button_move['state'] = 'normal'
                                button_rotate['state'] = 'normal'
                                tab_possible_next.append(count)

                    if plateau[y][x + 1] == 0:
                        print('COLOR')
                        count = ((y) * 10) + (x + 2)
                        canvas.itemconfig(count, outline='red', width='2')
                        button_move['state'] = 'normal'
                        button_rotate['state'] = 'normal'
                        tab_possible_next.append(count)
                    else:
                        if plateau[y][x + 1] == 1 or plateau[y][x + 1] == 2:
                            if plateau[y][x + 1] == player:
                                count = ((y) * 10) + (x + 2)
                                canvas.itemconfig(count, outline='red', width='2')
                                button_move['state'] = 'normal'
                                button_rotate['state'] = 'normal'
                                tab_possible_next.append(count)

                        elif plateau[y][x][0] == 2:
                            if (plateau[y][x + 1][0] == 3 or plateau[y][x + 1][0] == 4) and plateau[y][x + 1][
                                2] == player:
                                count = (y * 10) + (x + 2)
                                canvas.itemconfig(count, outline='red', width='2')
                                button_move['state'] = 'normal'
                                button_rotate['state'] = 'normal'
                                tab_possible_next.append(count)
                elif y == 0:
                    for i in range(80):
                        canvas.itemconfig(i, outline='black', width='0')
                    global test_temp
                    test_temp = (y * 10) + (x + 1)
                    if plateau[y][x - 1] == 0:
                        print('COLOR')
                        count = (y * 10) + x
                        canvas.itemconfig(count, outline='red', width='2')
                        button_move['state'] = 'normal'
                        button_rotate['state'] = 'normal'
                        tab_possible_next.append(count)
                    else:
                        if plateau[y][x - 1] == 1 or plateau[y][x - 1] == 2:
                            if plateau[y][x - 1] == player:
                                count = (y * 10) + x
                                canvas.itemconfig(count, outline='red', width='2')
                                button_move['state'] = 'normal'
                                button_rotate['state'] = 'normal'
                                tab_possible_next.append(count)
                        elif plateau[y][x][0] == 2:
                            if (plateau[y][x - 1][0] == 3 or plateau[y][x - 1][0] == 4) and plateau[y][x - 1][
                                2] == player:
                                count = (y * 10) + x
                                canvas.itemconfig(count, outline='red', width='2')
                                button_move['state'] = 'normal'
                                button_rotate['state'] = 'normal'
                                tab_possible_next.append(count)

                    if plateau[y + 1][x] == 0:
                        print('COLOR')
                        count = ((y + 1) * 10) + (x + 1)
                        canvas.itemconfig(count, outline='red', width='2')
                        button_move['state'] = 'normal'
                        button_rotate['state'] = 'normal'
                        tab_possible_next.append(count)
                    else:
                        if plateau[y + 1][x] == 1 or plateau[y + 1][x] == 2:
                            if plateau[y + 1][x] == player:
                                count = ((y + 1) * 10) + (x + 1)
                                canvas.itemconfig(count, outline='red', width='2')
                                button_move['state'] = 'normal'
                                button_rotate['state'] = 'normal'
                                tab_possible_next.append(count)

                        elif plateau[y][x][0] == 2:
                            if (plateau[y + 1][x][0] == 3 or plateau[y + 1][x][0] == 4) and plateau[y + 1][x][
                                2] == player:
                                count = ((y + 1) * 10) + (x + 1)
                                canvas.itemconfig(count, outline='red', width='2')
                                button_move['state'] = 'normal'
                                button_rotate['state'] = 'normal'
                                tab_possible_next.append(count)

                    if plateau[y][x + 1] == 0:
                        print('COLOR')
                        count = (y * 10) + (x + 2)
                        canvas.itemconfig(count, outline='red', width='2')
                        button_move['state'] = 'normal'
                        button_rotate['state'] = 'normal'
                        tab_possible_next.append(count)
                    else:
                        if plateau[y][x + 1] == 1 or plateau[y][x + 1] == 2:
                            if plateau[y][x + 1] == player:
                                count = (y * 10) + (x + 2)
                                canvas.itemconfig(count, outline='red', width='2')
                                button_move['state'] = 'normal'
                                button_rotate['state'] = 'normal'
                                tab_possible_next.append(count)
                        elif plateau[y][x][0] == 2:
                            if (plateau[y][x + 1][0] == 3 or plateau[y][x + 1][0] == 4) and plateau[y][x + 1][
                                2] == player:
                                count = (y * 10) + (x + 2)
                                canvas.itemconfig(count, outline='red', width='2')
                                button_move['state'] = 'normal'
                                button_rotate['state'] = 'normal'
                                tab_possible_next.append(count)

                elif y == 7:
                    for i in range(80):
                        canvas.itemconfig(i, outline='black', width='0')
                    global test_temp
                    test_temp = (y * 10) + (x + 1)
                    print('ok')
                    if plateau[y - 1][x] == 0:
                        print('COLOR 1')
                        count = ((y - 1) * 10) + (x + 1)
                        canvas.itemconfig(count, outline='red', width='2')
                        button_move['state'] = 'normal'
                        button_rotate['state'] = 'normal'
                        tab_possible_next.append(count)
                    else:
                        if plateau[y - 1][x] == 1 or plateau[y - 1][x] == 2:
                            if plateau[y - 1][x] == player:
                                count = ((y - 1) * 10) + (x + 1)
                                canvas.itemconfig(count, outline='red', width='2')
                                button_move['state'] = 'normal'
                                button_rotate['state'] = 'normal'
                                tab_possible_next.append(count)
                        elif plateau[y][x][0] == 2:
                            if (plateau[y - 1][x][0] == 3 or plateau[y - 1][x][0] == 4) and plateau[y - 1][x][
                                2] == player:
                                count = ((y - 1) * 10) + (x + 1)
                                canvas.itemconfig(count, outline='red', width='2')
                                button_move['state'] = 'normal'
                                button_rotate['state'] = 'normal'
                                tab_possible_next.append(count)

                    if plateau[y][x - 1] == 0:
                        print('COLOR 2')

                        count = ((y) * 10) + x
                        canvas.itemconfig(count, outline='red', width='2')
                        button_move['state'] = 'normal'
                        button_rotate['state'] = 'normal'
                        tab_possible_next.append(count)
                    else:
                        if plateau[y][x - 1] == 1 or plateau[y][x - 1] == 2:
                            if plateau[y][x - 1] == player:
                                count = ((y) * 10) + x
                                canvas.itemconfig(count, outline='red', width='2')
                                button_move['state'] = 'normal'
                                button_rotate['state'] = 'normal'
                                tab_possible_next.append(count)
                        elif plateau[y][x][0] == 2:
                            if (plateau[y][x - 1][0] == 3 or plateau[y][x - 1][0] == 4) and plateau[y][x - 1][
                                2] == player:
                                count = (y * 10) + x
                                canvas.itemconfig(count, outline='red', width='2')
                                button_move['state'] = 'normal'
                                button_rotate['state'] = 'normal'
                                tab_possible_next.append(count)

                    if plateau[y][x + 1] == 0:
                        print('COLOR 3')

                        count = ((y) * 10) + (x + 2)
                        canvas.itemconfig(count, outline='red', width='2')
                        button_move['state'] = 'normal'
                        button_rotate['state'] = 'normal'
                        tab_possible_next.append(count)
                    else:
                        if plateau[y][x + 1] == 1 or plateau[y][x + 1] == 2:
                            if plateau[y][x + 1] == player:
                                count = ((y) * 10) + (x + 2)
                                canvas.itemconfig(count, outline='red', width='2')
                                button_move['state'] = 'normal'
                                button_rotate['state'] = 'normal'
                                tab_possible_next.append(count)
                        elif plateau[y][x][0] == 2:
                            if (plateau[y][x + 1][0] == 3 or plateau[y][x + 1][0] == 4) and plateau[y][x + 1][
                                2] == player:
                                count = (y * 10) + (x + 2)
                                canvas.itemconfig(count, outline='red', width='2')
                                button_move['state'] = 'normal'
                                button_rotate['state'] = 'normal'
                                tab_possible_next.append(count)
                elif x == 9:
                    for i in range(80):
                        canvas.itemconfig(i, outline='black', width='0')
                    global test_temp
                    test_temp = (y * 10) + (x + 1)
                    print('OK X')
                    if plateau[y + 1][x] == 0:
                        print('COLOR')

                        count = ((y + 1) * 10) + (x + 1)
                        canvas.itemconfig(count, outline='red', width='2')
                        button_move['state'] = 'normal'
                        button_rotate['state'] = 'normal'
                        tab_possible_next.append(count)
                    else:
                        if plateau[y + 1][x] == 1 or plateau[y + 1][x] == 2:
                            if plateau[y + 1][x] == player:
                                count = ((y + 1) * 10) + (x + 1)
                                canvas.itemconfig(count, outline='red', width='2')
                                button_move['state'] = 'normal'
                                button_rotate['state'] = 'normal'
                                tab_possible_next.append(count)
                        elif plateau[y][x][0] == 2:
                            if (plateau[y + 1][x][0] == 3 or plateau[y + 1][x][0] == 4) and plateau[y + 1][x][
                                2] == player:
                                count = ((y + 1) * 10) + (x + 1)
                                canvas.itemconfig(count, outline='red', width='2')
                                button_move['state'] = 'normal'
                                button_rotate['state'] = 'normal'
                                tab_possible_next.append(count)

                    if plateau[y - 1][x] == 0:
                        print('COLOR')
                        count = ((y - 1) * 10) + (x + 1)
                        canvas.itemconfig(count, outline='red', width='2')
                        button_move['state'] = 'normal'
                        button_rotate['state'] = 'normal'
                        tab_possible_next.append(count)
                    else:
                        if plateau[y - 1][x] == 1 or plateau[y - 1][x] == 2:
                            if plateau[y - 1][x] == player:
                                count = ((y - 1) * 10) + (x + 1)
                                canvas.itemconfig(count, outline='red', width='2')
                                button_move['state'] = 'normal'
                                button_rotate['state'] = 'normal'
                                tab_possible_next.append(count)
                        elif plateau[y][x][0] == 2:
                            if (plateau[y - 1][x][0] == 3 or plateau[y - 1][x][0] == 4) and plateau[y - 1][x][
                                2] == player:
                                count = ((y - 1) * 10) + (x + 1)
                                canvas.itemconfig(count, outline='red', width='2')
                                button_move['state'] = 'normal'
                                button_rotate['state'] = 'normal'
                                tab_possible_next.append(count)

                    if plateau[y][x - 1] == 0:
                        print('COLOR')
                        count = (y * 10) + x
                        canvas.itemconfig(count, outline='red', width='2')
                        button_move['state'] = 'normal'
                        button_rotate['state'] = 'normal'
                        tab_possible_next.append(count)
                    else:
                        if plateau[y][x - 1] == 1 or plateau[y][x - 1] == 2:
                            if plateau[y][x - 1] == player:
                                count = (y * 10) + x
                                canvas.itemconfig(count, outline='red', width='2')
                                button_move['state'] = 'normal'
                                button_rotate['state'] = 'normal'
                                tab_possible_next.append(count)
                        elif plateau[y][x][0] == 2:
                            if (plateau[y][x - 1][0] == 3 or plateau[y][x - 1][0] == 4) and plateau[y][x - 1][
                                2] == player:
                                count = (y * 10) + x
                                canvas.itemconfig(count, outline='red', width='2')
                                button_move['state'] = 'normal'
                                button_rotate['state'] = 'normal'
                                tab_possible_next.append(count)

                else:
                    for i in range(80):
                        canvas.itemconfig(i, outline='black', width='0')
                    global test_temp
                    test_temp = (y * 10) + (x + 1)
                    if plateau[y + 1][x] == 0:
                        print('COLOR')

                        count = ((y + 1) * 10) + (x + 1)
                        canvas.itemconfig(count, outline='red', width='2')
                        button_move['state'] = 'normal'
                        button_rotate['state'] = 'normal'
                        tab_possible_next.append(count)
                    else:
                        if plateau[y + 1][x] == 1 or plateau[y + 1][x] == 2:
                            if plateau[y + 1][x] == player:
                                count = ((y + 1) * 10) + (x + 1)
                                canvas.itemconfig(count, outline='red', width='2')
                                button_move['state'] = 'normal'
                                button_rotate['state'] = 'normal'
                                tab_possible_next.append(count)
                        elif plateau[y][x][0] == 2:
                            if (plateau[y + 1][x][0] == 3 or plateau[y + 1][x][0] == 4) and plateau[y + 1][x][
                                2] == player:
                                count = ((y + 1) * 10) + (x + 1)
                                canvas.itemconfig(count, outline='red', width='2')
                                button_move['state'] = 'normal'
                                button_rotate['state'] = 'normal'
                                tab_possible_next.append(count)

                    if plateau[y - 1][x] == 0:
                        print('COLOR')
                        count = ((y - 1) * 10) + (x + 1)
                        canvas.itemconfig(count, outline='red', width='2')
                        button_move['state'] = 'normal'
                        button_rotate['state'] = 'normal'
                        tab_possible_next.append(count)
                    else:
                        if plateau[y - 1][x] == 1 or plateau[y - 1][x] == 2:
                            if plateau[y - 1][x] == player:
                                count = ((y - 1) * 10) + (x + 1)
                                canvas.itemconfig(count, outline='red', width='2')
                                button_move['state'] = 'normal'
                                button_rotate['state'] = 'normal'
                                tab_possible_next.append(count)
                        elif plateau[y][x][0] == 2:
                            if (plateau[y - 1][x][0] == 3 or plateau[y - 1][x][0] == 4) and plateau[y - 1][x][
                                2] == player:
                                count = ((y - 1) * 10) + (x + 1)
                                canvas.itemconfig(count, outline='red', width='2')
                                button_move['state'] = 'normal'
                                button_rotate['state'] = 'normal'
                                tab_possible_next.append(count)

                    if plateau[y][x - 1] == 0:
                        print('COLOR')
                        count = (y * 10) + x
                        canvas.itemconfig(count, outline='red', width='2')
                        button_move['state'] = 'normal'
                        button_rotate['state'] = 'normal'
                        tab_possible_next.append(count)
                    else:
                        if plateau[y][x - 1] == 1 or plateau[y][x - 1] == 2:
                            if plateau[y][x - 1] == player:
                                count = (y * 10) + x
                                canvas.itemconfig(count, outline='red', width='2')
                                button_move['state'] = 'normal'
                                button_rotate['state'] = 'normal'
                                tab_possible_next.append(count)
                        elif plateau[y][x][0] == 2:
                            if (plateau[y][x - 1][0] == 3 or plateau[y][x - 1][0] == 4) and plateau[y][x - 1][
                                2] == player:
                                count = (y * 10) + x
                                canvas.itemconfig(count, outline='red', width='2')
                                button_move['state'] = 'normal'
                                button_rotate['state'] = 'normal'
                                tab_possible_next.append(count)

                    if plateau[y][x + 1] == 0:
                        print('COLOR')
                        count = (y * 10) + (x + 2)
                        canvas.itemconfig(count, outline='red', width='2')
                        button_move['state'] = 'normal'
                        button_rotate['state'] = 'normal'
                        tab_possible_next.append(count)
                    else:
                        if plateau[y][x + 1] == 1 or plateau[y][x + 1] == 2:
                            if plateau[y][x + 1] == player:
                                count = (y * 10) + (x + 2)
                                canvas.itemconfig(count, outline='red', width='2')
                                button_move['state'] = 'normal'
                                button_rotate['state'] = 'normal'
                                tab_possible_next.append(count)
                            elif plateau[y][x][0] == 2:
                                if (plateau[y][x + 1][0] == 3 or plateau[y][x + 1][0] == 4) and plateau[y][x + 1][
                                    2] == player:
                                    count = (y * 10) + (x + 2)
                                    canvas.itemconfig(count, outline='red', width='2')
                                    button_move['state'] = 'normal'
                                    button_rotate['state'] = 'normal'
                                    tab_possible_next.append(count)
            else:
                button_move['state'] = 'disabled'
                button_rotate['state'] = 'disabled'

    else:
        button_move['state'] = 'disabled'


def shoot(player, plateau):

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
                        if plateau[i][j][0] == 5 and plateau[i][j][2] == player:
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
                        print('Le player ' + str(plateau[x_init][k][2]) + ' a perdu')
                        inProgess = False
                        game = False
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
                        print('Le player ' + str(plateau[x_init][k][2]) + ' a perdu')
                        inProgess = False
                        game = False
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

                        elif plateau[k][y_init][1] == 'e':
                            plateau[k][y_init] = 0
                            aled = False
                            inProgess = False
                            x_init = k
                        elif plateau[k][y_init][1] == 'o':
                            plateau[k][y_init] = 0
                            aled = False
                            inProgess = False
                            x_init = k

                        elif plateau[k][y_init][1] == 's':
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
                        print('Le player ' + str(plateau[x_init][k][2]) + ' a perdu')
                        inProgess = False
                        game = False
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
                        print('ok 3 ')
                        print(plateau[x_init][k])
                        if plateau[x_init][k][1] == 'n':
                            print('ok n')
                            plateau[x_init][k] = 0
                            aled = False
                            inProgess = False
                            y_init = k
                        elif plateau[x_init][k][1] == 'e':
                            print('ok e')
                            print('absorbed')
                            aled = False
                            inProgess = False
                            y_init = k

                        elif plateau[x_init][k][1] == 'o':
                            print('ok o')
                            plateau[x_init][k] = 0
                            aled = False
                            inProgess = False
                            y_init = k

                        elif plateau[x_init][k][1] == 's':
                            print('ok s')
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
                        print('Le player ' + str(plateau[x_init][k][2]) + ' a perdu')
                        inProgess=False
                        game = False
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
                        elif plateau[x_init][k][1] == 'e':
                           plateau[x_init][k] = 0
                           inProgess = False
                           aled = False
                           y_init = k

                        elif plateau[x_init][k][1] == 'o':
                            print('absorbed')
                            aled = False
                            inProgess = False
                            y_init = k

                        elif plateau[x_init][k][1] == 's':
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
                            print('DETRUIS TOI')
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

# fonction bindé au click (appellée a chaque click)
def motion(event):
    if event.x < 505 and event.y < 401 and event.y > 0 and event.x > 0:  # Verif du click sur le tableau
        count = 0
        for k in range(8):
            for l in range(10):
                count += 1
                if event.x >= tab_cord[k][l][0] and event.x <= tab_cord[k][l][2] and event.y >= tab_cord[k][l][
                    1] and event.y <= tab_cord[k][l][3]:
                    # Reperage de la case du click
                    print('Vous avez cliqué sur la case : ' + str(count))
                    aled_y = count // 10
                    aled_x = (count % 10) - 1
                    if aled_x + 1 == 0:
                        aled_x = 9
                        aled_y -= 1
                    print(aled_x, aled_y)
                    count = 0
                    # RETURN
                    if selected == False:
                        select(aled_x, aled_y, plat, 1)
                    else:
                        selected_move(aled_x, aled_y, plat, 1)

                    shoot(1,plat)

# fonction qui transforme le tableau algo en un truck graphiquement potable
def graphTranslation(plateau):
    count = 0
    for k in range(8):
        for l in range(10):
            count += 1
            if plateau[k][l] != 0:
                if plateau[k][l] == 1:
                    canvas.itemconfig(count, fill='red')
                elif plateau[k][l] == 2:
                    canvas.itemconfig(count, fill='green')
                elif plateau[k][l][0] == 1:
                    w = Label(fenetre, text='1')
                    print(tab_cord[k][l][0])
                    print(str(tab_cord[k][l][1]) + '\n ----')
                    w.place(x=tab_cord[k][l][0] + 110, y=tab_cord[k][l][1] + 10)
                elif plateau[k][l][0] == 2:
                    w = Label(fenetre, text='2')
                    print(tab_cord[k][l][0])
                    print(str(tab_cord[k][l][1]) + '\n ----')
                    w.place(x=tab_cord[k][l][0] + 110, y=tab_cord[k][l][1] + 10)
                elif plateau[k][l][0] == 3:
                    w = Label(fenetre, text='3')
                    print(tab_cord[k][l][0])
                    print(str(tab_cord[k][l][1]) + '\n ----')
                    w.place(x=tab_cord[k][l][0] + 110, y=tab_cord[k][l][1] + 10)
                elif plateau[k][l][0] == 4:
                    w = Label(fenetre, text='4')
                    print(tab_cord[k][l][0])
                    print(str(tab_cord[k][l][1]) + '\n ----')
                    w.place(x=tab_cord[k][l][0] + 110, y=tab_cord[k][l][1] + 10)
                elif plateau[k][l][0] == 5:
                    w = Label(fenetre, text='5')
                    print(tab_cord[k][l][0])
                    print(str(tab_cord[k][l][1]) + '\n ----')
                    w.place(x=tab_cord[k][l][0] + 110, y=tab_cord[k][l][1] + 10)


def newBoard():
    plateau = [[0] * 10 for i in range(8)]  # creation d'un tableau vide de 0 de longueur n*n
    return plateau

plat = newBoard()
classic(plat)
graphTranslation(plat)
print(tab_cord[2][3][1])
canvas.pack()

fenetre.bind("<Button-1>", motion)

if aled_x != 0:
    print('OK C GUD')

button_move.pack()
button_rotate.pack()
label.pack()
text_sens.pack()
fenetre.mainloop()

#   for i in range()
