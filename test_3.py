def possible_next(x,y,plateau,player):
    count = (x*10)+(y+1)
    for i in range(80):
        canvas.itemconfig(i, outline='black', width='0')
    if plateau[x][y] != 5:
        if x==0:
            if plateau[y+1][x] == 0 :
                print('COLOR')
                count = ((x+1) * 10) + (y + 1)
                canvas.itemconfig(count, outline='red', width='2')
            else:
                if plateau[y+1][x] == 1 or plateau[y+1][x] == 2:
                    if plateau[x + 1][y] == player:
                        count = ((x + 1) * 10) + (y + 1)
                        canvas.itemconfig(count, outline='red', width='2')
                elif plateau[x + 1][y][2] == player :
                    count = ((x + 1) * 10) + (y + 1)
                    canvas.itemconfig(count, outline='red', width='2')

            if plateau[y][x-1] == 0 :
                print('COLOR')
                count = (x * 10) + ((y-1) + 1)
                canvas.itemconfig(count, outline='red', width='2')
            else:
                if plateau[y][x-1] == 1 or plateau[y][x-1] == 2:
                    if plateau[y][x-1] == player:
                        count = (x * 10) + ((y - 1) + 1)
                        canvas.itemconfig(count, outline='red', width='2')
                elif plateau[y][x-1][2] == player :
                    count = (x * 10) + ((y - 1) + 1)
                    canvas.itemconfig(count, outline='red', width='2')

            if plateau[y][x+1] == 0 :
                print('COLOR')
                count = (x * 10) + ((y + 1) + 1)
                canvas.itemconfig(count, outline='red', width='2')
            else:
                if plateau[y][x+1] == 1 or plateau[y][x+1] == 2:
                    if plateau[y][x+1] == player:
                        count = (x * 10) + ((y + 1) + 1)
                        canvas.itemconfig(count, outline='red', width='2')
                elif plateau[y][x+1][2] == player :
                    count = (x * 10) + ((y + 1) + 1)
                    canvas.itemconfig(count, outline='red', width='2')
        if y == 0:

            if plateau[y+1][x] == 0 :
                print('COLOR')
                count = ((x+1) * 10) + (y + 1)
                canvas.itemconfig(count, outline='red', width='2')
            else:
                if plateau[y+1][x] == 1 or plateau[y+1][x] == 2:
                    if plateau[x + 1][y] == player:
                        count = ((x + 1) * 10) + (y + 1)
                        canvas.itemconfig(count, outline='red', width='2')
                elif plateau[x + 1][y][2] == player :
                    count = ((x + 1) * 10) + (y + 1)
                    canvas.itemconfig(count, outline='red', width='2')

            if plateau[y-1][x] == 0 :
                print('COLOR')
                count = ((x - 1) * 10) + (y + 1)
                canvas.itemconfig(count, outline='red', width='2')
            else:
                if plateau[y-1][x] == 1 or plateau[y-1][x] == 2:
                    if plateau[y-1][x] == player:
                        count = ((x - 1) * 10) + (y + 1)
                        canvas.itemconfig(count, outline='red', width='2')
                elif plateau[y-1][x][2] == player :
                    count = ((x - 1) * 10) + (y + 1)
                    canvas.itemconfig(count, outline='red', width='2')

            if plateau[y][x+1] == 0 :
                print('COLOR')
                count = (x * 10) + ((y + 1) + 1)
                canvas.itemconfig(count, outline='red', width='2')
            else:
                if plateau[y][x+1] == 1 or plateau[y][x+1] == 2:
                    if plateau[y][x+1] == player:
                        count = (x * 10) + ((y + 1) + 1)
                        canvas.itemconfig(count, outline='red', width='2')
                elif plateau[y][x+1][2] == player :
                    count = (x * 10) + ((y + 1) + 1)
                    canvas.itemconfig(count, outline='red', width='2')

        if x==9:
            if plateau[y-1][x] == 0 :
                print('COLOR')
                count = ((x - 1) * 10) + (y + 1)
                canvas.itemconfig(count, outline='red', width='2')
            else:
                if plateau[y-1][x] == 1 or plateau[y-1][x] == 2:
                    if plateau[y-1][x] == player:
                        count = ((x - 1) * 10) + (y + 1)
                        canvas.itemconfig(count, outline='red', width='2')
                elif plateau[y-1][x][2] == player :
                    count = ((x - 1) * 10) + (y + 1)
                    canvas.itemconfig(count, outline='red', width='2')


            if plateau[y][x-1] == 0 :
                print('COLOR')
                count = (x * 10) + ((y-1) + 1)
                canvas.itemconfig(count, outline='red', width='2')
            else:
                if plateau[y][x-1] == 1 or plateau[y][x-1] == 2:
                    if plateau[y][x-1] == player:
                        count = (x * 10) + ((y - 1) + 1)
                        canvas.itemconfig(count, outline='red', width='2')
                elif plateau[y][x-1][2] == player :
                    count = (x * 10) + ((y - 1) + 1)
                    canvas.itemconfig(count, outline='red', width='2')

            if plateau[y][x+1] == 0 :
                print('COLOR')
                count = (x * 10) + ((y + 1) + 1)
                canvas.itemconfig(count, outline='red', width='2')
            else:
                if plateau[y][x+1] == 1 or plateau[y][x+1] == 2:
                    if plateau[y][x+1] == player:
                        count = (x * 10) + ((y + 1) + 1)
                        canvas.itemconfig(count, outline='red', width='2')
                elif plateau[y][x+1][2] == player :
                    count = (x * 10) + ((y + 1) + 1)
                    canvas.itemconfig(count, outline='red', width='2')
        if y == 7:

            if plateau[y+1][x] == 0 :
                print('COLOR')
                count = ((x+1) * 10) + (y + 1)
                canvas.itemconfig(count, outline='red', width='2')
            else:
                if plateau[y+1][x] == 1 or plateau[y+1][x] == 2:
                    if plateau[x + 1][y] == player:
                        count = ((x + 1) * 10) + (y + 1)
                        canvas.itemconfig(count, outline='red', width='2')
                elif plateau[x + 1][y][2] == player :
                    count = ((x + 1) * 10) + (y + 1)
                    canvas.itemconfig(count, outline='red', width='2')

            if plateau[y-1][x] == 0 :
                print('COLOR')
                count = ((x - 1) * 10) + (y + 1)
                canvas.itemconfig(count, outline='red', width='2')
            else:
                if plateau[y-1][x] == 1 or plateau[y-1][x] == 2:
                    if plateau[y-1][x] == player:
                        count = ((x - 1) * 10) + (y + 1)
                        canvas.itemconfig(count, outline='red', width='2')
                elif plateau[y-1][x][2] == player :
                    count = ((x - 1) * 10) + (y + 1)
                    canvas.itemconfig(count, outline='red', width='2')

            if plateau[x][y - 1] == 0:
                print('COLOR')
                count = (x * 10) + ((y - 1) + 1)
                canvas.itemconfig(count, outline='red', width='2')
            else:
                if plateau[x][y - 1] == 1 or plateau[x][y - 1] == 2:
                    if plateau[x][y - 1] == player:
                        count = (x * 10) + ((y - 1) + 1)
                        canvas.itemconfig(count, outline='red', width='2')
                elif plateau[x][y - 1][2] == player:
                    count = (x * 10) + ((y - 1) + 1)
                    canvas.itemconfig(count, outline='red', width='2')

        else:
            if plateau[y+1][x] == 0 :
                print('COLOR')
                count = ((x+1) * 10) + (y + 1)
                canvas.itemconfig(count, outline='red', width='2')
            else:
                if plateau[y+1][x] == 1 or plateau[y+1][x] == 2:
                    if plateau[x + 1][y] == player:
                        count = ((x + 1) * 10) + (y + 1)
                        canvas.itemconfig(count, outline='red', width='2')
                elif plateau[x + 1][y][2] == player :
                    count = ((x + 1) * 10) + (y + 1)
                    canvas.itemconfig(count, outline='red', width='2')

            if plateau[y-1][x] == 0 :
                print('COLOR')
                count = ((x - 1) * 10) + (y + 1)
                canvas.itemconfig(count, outline='red', width='2')
            else:
                if plateau[y-1][x] == 1 or plateau[y-1][x] == 2:
                    if plateau[y-1][x] == player:
                        count = ((x - 1) * 10) + (y + 1)
                        canvas.itemconfig(count, outline='red', width='2')
                elif plateau[y-1][x][2] == player :
                    count = ((x - 1) * 10) + (y + 1)
                    canvas.itemconfig(count, outline='red', width='2')

            if plateau[x][y - 1] == 0:
                print('COLOR')
                count = (x * 10) + ((y - 1) + 1)
                canvas.itemconfig(count, outline='red', width='2')
            else:
                if plateau[x][y - 1] == 1 or plateau[x][y - 1] == 2:
                    if plateau[x][y - 1] == player:
                        count = (x * 10) + ((y - 1) + 1)
                        canvas.itemconfig(count, outline='red', width='2')
                elif plateau[x][y - 1][2] == player:
                    count = (x * 10) + ((y - 1) + 1)
                    canvas.itemconfig(count, outline='red', width='2')

            if plateau[x][y + 1] == 0:
                print('COLOR')
                count = (x * 10) + ((y + 1) + 1)
                canvas.itemconfig(count, outline='red', width='2')
            else:
                if plateau[x][y + 1] == 1 or plateau[x][y + 1] == 2:
                    if plateau[x][y + 1] == player:
                        count = (x * 10) + ((y + 1) + 1)
                        canvas.itemconfig(count, outline='red', width='2')
                elif plateau[x][y + 1][2] == player:
                    count = (x * 10) + ((y + 1) + 1)
                    canvas.itemconfig(count, outline='red', width='2')
