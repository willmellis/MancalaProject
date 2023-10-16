import tkinter as tk

#creates the values of the pits in the mancala board
counters = [[0,4,4,4,4,4,4],[4,4,4,4,4,4,0]]

player = True

def actions0(row,col):
    global player
    if row == 1:
        player = not player
        return
    value = counters[row][col]
    counters[row][col] = 0
    button_grid[row][col].config(text=counters[row][col])
    if value > col and row == 0:  # if the value (number of stones) is grater then the index of the colum and the row == 0
        wrap = value - col
        for i in range(value - wrap):  # the for loop runs while i is <=value-wrap
            col -= 1
            counters[row][col] += 1
            button_grid[row][col].config(text=counters[row][col])
        # col = 0
        for j in range(wrap):  # while j is <=wrap, the code below will run
            counters[1][col] += 1
            button_grid[1][col].config(text=counters[1][col])
            col += 1
    if value <= col and row == 0:  # if value <= the colum index and row == 0 the code below will run
        for c in range(value):  # while a <= value, the code below will run
            col -= 1
            counters[row][col] += 1
            button_grid[row][col].config(text=counters[row][col])

def actions1(row,col):
    global player
    if row == 0:
        player = not player
        return
    value = counters[row][col]
    counters[row][col] = 0
    button_grid[row][col].config(text=counters[row][col])
    if value > 6 - col and row == 1:  # if the value is larger then 6 - the index of the colum and the row == 1
        wrap = value - (6 - col)
        for a in range(6 - col):  # while a <= 6-col the code below will run
            col += 1
            counters[row][col] += 1
            button_grid[row][col].config(text=counters[row][col])
        # col = 6
        for b in range(wrap):  # while b is <=wrap, the code below will run
            counters[0][col] += 1
            button_grid[0][col].config(text=counters[0][col])
            col -= 1
    if value <= 6 - col and row == 1:  # if the value is <= the index of the colum and the row = 0, the code below will run
        for d in range(value):  # while a is <= value, the code below will run
            col += 1
            counters[row][col] += 1
            button_grid[row][col].config(text=counters[row][col])

#this method determines what modifications are made to the board after a player clicks on a pit of their choice.
#The modifications depends on what happens during the move, and what happens after. (i.e if a player lands in an empty pit)
def button_click(row, col):
    global player
    if player == True:
        actions0(row,col)
    elif player == False:
        actions1(row,col)
    player = not player
print( counters )


#This code will create the window for the mancala game itself
root = tk.Tk()
root.title("Mancala Game")

#This code will create the mancala board as it is seen when the program runs
#the board will be 2x7 (2x6 including the 2 mancalas, one on each side)
button_grid = []
for i in range(2):#while i <= 2(the number of rows), the code below will run
    row = []
    for j in range(7):#while j <= 7(the number of colums), the code below will run
        button = tk.Button(root, text=counters[i][j], command=lambda i=i, j=j: button_click(i, j),
        height = 2, width = 4, font = ("Times New Roman",70))
        button.grid(row=i, column=j, padx=10, pady=10)
        row.append(button)
    button_grid.append(row)
button_grid[0][0].config(fg="red")
button_grid[1][6].config(fg="blue")


#used to run tkinter
root.mainloop()

