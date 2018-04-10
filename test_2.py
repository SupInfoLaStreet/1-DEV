#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tkinter import *
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



board_graph = [[0] * 10 for i in range(8)]
tab_cord = [[0] * 10 for i in range(8)]
fenetre = Tk()
fenetre.geometry("700x700")
canvas = Canvas(fenetre, width=505, height=400, background='yellow')
add_x, add_y = 0, 0
for i in range(8):
    for j in range(10):
        board_graph[i][j] = canvas.create_rectangle(add_x, add_y, add_x + 50, add_y + 50)
        add_x += 50
    add_x = 0
    add_y += 50

count = 0
for k in range(8):
    for l in range(10):
        count += 1
        tab_cord[k][l] = (canvas.coords(count))

def motion(event):
    if event.x < 505 and event.y <401 and event.y > 0 and event.x > 0:
        count = 0
        for k in range(8):
            for l in range(10):
                count +=1
                if event.x >= tab_cord[k][l][0] and event.x <= tab_cord[k][l][2] and event.y >= tab_cord[k][l][1] and event.y <= tab_cord[k][l][3]:
                    print('Vous avez cliqué sur la case : ' + str(count))
                    count = 0

def graphTranslation(plateau):
    count = 0
    for k in range(8):
        for l in range(10):
            count +=1
            if plateau[k][l] != 0:
                if plateau[k][l] == 1 :
                    canvas.itemconfig(count, fill='red')
                elif plateau[k][l] == 2 :
                    canvas.itemconfig(count, fill='green')
                elif plateau[k][l][0] == 1:
                    w = Label(fenetre, text = '1')
                    print(tab_cord[k][l][0])
                    print(str(tab_cord[k][l][1]) + '\n ----')
                    w.place(x=tab_cord[k][l][0]+110,y=tab_cord[k][l][1]+10)
                elif plateau[k][l][0] == 2:
                    w = Label(fenetre, text = '2')
                    print(tab_cord[k][l][0])
                    print(str(tab_cord[k][l][1]) + '\n ----')
                    w.place(x=tab_cord[k][l][0]+110,y=tab_cord[k][l][1]+10)
                elif plateau[k][l][0] == 3:
                    w = Label(fenetre, text = '3')
                    print(tab_cord[k][l][0])
                    print(str(tab_cord[k][l][1]) + '\n ----')
                    w.place(x=tab_cord[k][l][0]+110,y=tab_cord[k][l][1]+10)
                elif plateau[k][l][0] == 4:
                    w = Label(fenetre, text = '4')
                    print(tab_cord[k][l][0])
                    print(str(tab_cord[k][l][1]) + '\n ----')
                    w.place(x=tab_cord[k][l][0]+110,y=tab_cord[k][l][1]+10)
                elif plateau[k][l][0] == 5:
                    w = Label(fenetre, text = '5')
                    print(tab_cord[k][l][0])
                    print(str(tab_cord[k][l][1]) + '\n ----')
                    w.place(x=tab_cord[k][l][0]+110,y=tab_cord[k][l][1]+10)

def newBoard():
    plateau = [[0] * 10 for i in range(8)]  # creation d'un tableau vide de 0 de longueur n*n
    return plateau

plat = newBoard()
classic(plat)
graphTranslation(plat)
print(tab_cord[2][3][1])
canvas.pack()
fenetre.bind("<Button-1>", motion)
fenetre.mainloop()
#   for i in range()

