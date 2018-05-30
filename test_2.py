#!/usr/bin/env python
# -*- coding: utf-8 -*-
aled_x = 0
aled_y = 0
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


##Var gloable
board_graph = [[0] * 10 for i in range(8)]
tab_cord = [[0] * 10 for i in range(8)]
fenetre = Tk()
var = StringVar()
var.set('hello')
fenetre.geometry("700x700")
canvas = Canvas(fenetre, width=550, height=500, background='yellow')
add_x, add_y = 0, 0
button_move = Button(fenetre, text="Bouger le pion",state = DISABLED)
button_rotate = Button(fenetre, text="Pivoter le pion",state = DISABLED)
label = Label(fenetre, text="Sens :")
text_sens = Label(fenetre, textvariable=var)


#creation du tableau graphique (loop de rectangle)
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

#fonction selection click
def select(x,y,plateau,player):
    print('ALED',x,y)
    if plateau[y][x] != 0 or plateau[y][x] != 1 or plateau[y][x] != 2:
        var.set(str(plateau[y][x][1]))
    possible_next(x,y,plateau,player)
#fonction pour afficher en surbrillance les deplacements possibles (non finie)
def possible_next(x,y,plateau,player):
    count = (x*10)+(y+1)
    print('OMG ',x,y)
    for i in range(80):
        canvas.itemconfig(i, outline='black', width='0')
    if plateau[y][x] != 5:
        if x==0:
            if plateau[y+1][x] == 0 :
                print('COLOR')
                count = ((y+1)*10) + (x+1)
                canvas.itemconfig(count, outline='red', width='2')
            else:
                if plateau[y+1][x] == 1 or plateau[y+1][x] == 2:
                    if plateau[y + 1][x] == player:
                        count = ((y + 1) * 10) + (x + 1)
                        canvas.itemconfig(count, outline='red', width='2')
                elif plateau[y + 1][x][2] == player :
                    count = ((y + 1) * 10) + (x + 1)
                    canvas.itemconfig(count, outline='red', width='2')

            if plateau[y][x+1] == 0 :
                print('COLOR')
                count = ((y) * 10) + (x + 2)
                canvas.itemconfig(count, outline='red', width='2')
            else:
                if plateau[y][x+1] == 1 or plateau[y][x+1] == 2:
                    if plateau[y][x+1] == player:
                        count = ((y) * 10) + (x + 2)
                        canvas.itemconfig(count, outline='red', width='2')
                elif plateau[y][x+1][2] == player :
                    count = ((y) * 10) + (x + 2)
                    canvas.itemconfig(count, outline='red', width='2')
        elif y == 0:

            if plateau[y][x-1] == 0 :
                print('COLOR')
                count = (y * 10) + x
                canvas.itemconfig(count, outline='red', width='2')
            else:
                if plateau[y][x-1] == 1 or plateau[y][x-1] == 2:
                    if plateau[y][x-1] == player:
                        count = (y * 10) + x
                        canvas.itemconfig(count, outline='red', width='2')
                elif plateau[y][x-1][2] == player :
                    count = (y * 10) + x
                    canvas.itemconfig(count, outline='red', width='2')

            if plateau[y-1][x] == 0 :
                print('COLOR')
                count = ((y-1) * 10) + (x+1)
                canvas.itemconfig(count, outline='red', width='2')
            else:
                if plateau[y-1][x] == 1 or plateau[y-1][x] == 2:
                    if plateau[y-1][x] == player:
                        count = ((y - 1) * 10) + (x + 1)
                        canvas.itemconfig(count, outline='red', width='2')
                elif plateau[y-1][x][2] == player :
                    count = ((y - 1) * 10) + (x + 1)
                    canvas.itemconfig(count, outline='red', width='2')

            if plateau[y][x+1] == 0 :
                print('COLOR')
                count = (y* 10) + (x + 2)
                canvas.itemconfig(count, outline='red', width='2')
            else:
                if plateau[y][x+1] == 1 or plateau[y][x+1] == 2:
                    if plateau[y][x+1] == player:
                        count = (y * 10) + (x + 2)
                        canvas.itemconfig(count, outline='red', width='2')
                elif plateau[y][x+1][2] == player :
                    count = (y * 10) + (x + 2)
                    canvas.itemconfig(count, outline='red', width='2')

        elif y==7:
            print('ok')
            if plateau[y - 1][x] == 0:
                print('COLOR 1')
                count = ((y-1) * 10) + (x+1)
                canvas.itemconfig(count, outline='red', width='2')
            else:
                if plateau[y - 1][x] == 1 or plateau[y - 1][x] == 2:
                    if plateau[y - 1][x] == player:
                        count = ((y - 1) * 10) + (x + 1)
                        canvas.itemconfig(count, outline='red', width='2')
                elif plateau[y - 1][x][2] == player:
                    count = ((y - 1) * 10) + (x + 1)
                    canvas.itemconfig(count, outline='red', width='2')


            if plateau[y][x-1] == 0 :
                print('COLOR 2')

                count = ((y) * 10) + x
                canvas.itemconfig(count, outline='red', width='2')
            else:
                if plateau[y][x-1] == 1 or plateau[y][x-1] == 2:
                    if plateau[y][x-1] == player:
                        count = ((y) * 10) + x
                        canvas.itemconfig(count, outline='red', width='2')
                elif plateau[y][x-1][2] == player :
                    count = ((y) * 10) + x
                    canvas.itemconfig(count, outline='red', width='2')

            if plateau[y][x+1] == 0 :
                print('COLOR 3')

                count = ((y) * 10) + (x+2)
                canvas.itemconfig(count, outline='red', width='2')
            else:
                if plateau[y][x+1] == 1 or plateau[y][x+1] == 2:
                    if plateau[y][x+1] == player:
                        count = ((y) * 10) + (x + 2)
                        canvas.itemconfig(count, outline='red', width='2')
                elif plateau[y][x+1][2] == player :
                    count = ((y) * 10) + (x + 2)
                    canvas.itemconfig(count, outline='red', width='2')
        elif x == 9:
            print('OK X')
            if plateau[y + 1][x] == 0:
                print('COLOR')

                count = ((y + 1) * 10) + (x + 1)
                canvas.itemconfig(count, outline='red', width='2')
            else:
                if plateau[y + 1][x] == 1 or plateau[y + 1][x] == 2:
                    if plateau[y + 1][x] == player:
                        count = ((y + 1) * 10) + (x + 1)
                        canvas.itemconfig(count, outline='red', width='2')
                elif plateau[y + 1][x][2] == player:
                    count = ((y + 1) * 10) + (x + 1)
                    canvas.itemconfig(count, outline='red', width='2')

            if plateau[y - 1][x] == 0:
                print('COLOR')
                count = ((y - 1) * 10) + (x + 1)
                canvas.itemconfig(count, outline='red', width='2')
            else:
                if plateau[y - 1][x] == 1 or plateau[y - 1][x] == 2:
                    if plateau[y - 1][x] == player:
                        count = ((y - 1) * 10) + (x + 1)
                        canvas.itemconfig(count, outline='red', width='2')
                elif plateau[y - 1][x][2] == player:
                    count = ((y - 1) * 10) + (x + 1)
                    canvas.itemconfig(count, outline='red', width='2')

            if plateau[y][x-1] == 0 :
                print('COLOR')
                count = (y * 10) + x
                canvas.itemconfig(count, outline='red', width='2')
            else:
                if plateau[y][x-1] == 1 or plateau[y][x-1] == 2:
                    if plateau[y][x-1] == player:
                        count = (y * 10) + x
                        canvas.itemconfig(count, outline='red', width='2')
                elif plateau[y][x-1][2] == player :
                    count = (y * 10) + x
                    canvas.itemconfig(count, outline='red', width='2')

        else:
            if plateau[y + 1][x] == 0:
                print('COLOR')

                count = ((y + 1) * 10) + (x + 1)
                canvas.itemconfig(count, outline='red', width='2')
            else:
                if plateau[y + 1][x] == 1 or plateau[y + 1][x] == 2:
                    if plateau[y + 1][x] == player:
                        count = ((y + 1) * 10) + (x + 1)
                        canvas.itemconfig(count, outline='red', width='2')
                elif plateau[y + 1][x][2] == player:
                    count = ((y + 1) * 10) + (x + 1)
                    canvas.itemconfig(count, outline='red', width='2')

            if plateau[y - 1][x] == 0:
                print('COLOR')
                count = ((y - 1) * 10) + (x + 1)
                canvas.itemconfig(count, outline='red', width='2')
            else:
                if plateau[y - 1][x] == 1 or plateau[y - 1][x] == 2:
                    if plateau[y - 1][x] == player:
                        count = ((y - 1) * 10) + (x + 1)
                        canvas.itemconfig(count, outline='red', width='2')
                elif plateau[y - 1][x][2] == player:
                    count = ((y - 1) * 10) + (x + 1)
                    canvas.itemconfig(count, outline='red', width='2')

            if plateau[y][x-1] == 0 :
                print('COLOR')
                count = (y * 10) + x
                canvas.itemconfig(count, outline='red', width='2')
            else:
                if plateau[y][x-1] == 1 or plateau[y][x-1] == 2:
                    if plateau[y][x-1] == player:
                        count = (y * 10) + x
                        canvas.itemconfig(count, outline='red', width='2')
                elif plateau[y][x-1][2] == player :
                    count = (y * 10) + x
                    canvas.itemconfig(count, outline='red', width='2')

            if plateau[y][x + 1] == 0:
                print('COLOR')
                count = (y * 10) + (x + 2)
                canvas.itemconfig(count, outline='red', width='2')
            else:
                if plateau[y][x + 1] == 1 or plateau[y][x + 1] == 2:
                    if plateau[y][x + 1] == player:
                        count = (y * 10) + (x + 2)
                        canvas.itemconfig(count, outline='red', width='2')
                elif plateau[y][x + 1][2] == player:
                    count = (y * 10) + (x + 2)
                    canvas.itemconfig(count, outline='red', width='2')

#fonction bindé au click (appellée a chaque click)
def motion(event):
    if event.x < 505 and event.y <401 and event.y > 0 and event.x > 0:#Verif du click sur le tableau
        count = 0
        for k in range(8):
            for l in range(10):
                count +=1
                if event.x >= tab_cord[k][l][0] and event.x <= tab_cord[k][l][2] and event.y >= tab_cord[k][l][1] and event.y <= tab_cord[k][l][3]:
                    #Reperage de la case du click
                    print('Vous avez cliqué sur la case : ' + str(count))
                    aled_y = count//10
                    aled_x = (count%10)-1
                    if aled_x+1 == 0:
                        aled_x = 9
                        aled_y -=1
                    print(aled_x,aled_y)
                    count = 0
                    button_rotate['state'] = 'normal'
                    verif(aled_x,aled_y)
                    #RETURN
                    select(aled_x,aled_y,plat,1)
                    display(plat)



#fonction qui transforme le tableau algo en un truck graphiquement potable
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

def verif(var1,var2):
    if var1 != 0:
        print('OK C GUD1')
    if var2 != 0:
        print('OK C GUD2')

def newBoard():
    plateau = [[0] * 10 for i in range(8)]  # creation d'un tableau vide de 0 de longueur n*n
    return plateau

plat = newBoard()
classic(plat)
graphTranslation(plat)
print(tab_cord[2][3][1])
canvas.pack()

fenetre.bind("<Button-1>", motion)

def display(gameBoard):
    for ligne in gameBoard:
        for x in ligne:
            print(x, ' ', end='')
        print('\n')

if aled_x != 0 :
    print('OK C GUD')


button_move.pack()
button_rotate.pack()
label.pack()
text_sens.pack()
fenetre.mainloop()

#   for i in range()

