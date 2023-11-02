

import tkinter as tk
#needed this to make the updating text labels
from tkinter import ttk, StringVar

#creates the values of the pits in the mancala board
counters = [[4,4,4,4,4,4,4],[4,4,4,4,4,4,4]]

#!moved all of this to the top of your code. The computer will read seqeuntially!
#!the first thing you want to do is create your gui and variables so you can use them later on!
#!didn't change your math at all, just creating the labels!

#This code will create the window for the mancala game itself
root = tk.Tk()
root.title("Mancala Game")

#created two updating labels to keep track of scores
counterLabel1 = StringVar()
counterLabel2 = StringVar()
counterLabel1.set("0")
counterLabel2.set("0")

#adds both labels to the gui
label1 = ttk.Label(root, textvariable = counterLabel1, font = ("Times New Roman",70))
label1.grid(row=2, column=2)
label2 = ttk.Label(root, textvariable = counterLabel2, font = ("Times New Roman",70))
label2.grid(row=2, column=4)

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
for i in range(7): #changing the colors of the board
   button_grid[0][i].config(fg="red")
   button_grid[1][i].config(fg="blue")

player = True
counter1 = 0
counter2 = 0

def actions0(row,col): #all actions done in the first row are controlled here
   global player
   global counter1
   if row == 1: #if the row being modified is the bottom row, player = not player
       player = not player
       return
   value = counters[row][col]
   counters[row][col] = 0
   tempcol = col
   button_grid[row][col].config(text=0)
   if value <= col:  # if value <= the colum index and row == 0 the code below will run
       row = 0
       for c in range(value):  # while a <= value, the code below will run
           col -= 1
           #print("col",col)
           counters[0][col] += 1
           button_grid[0][col].config(text=counters[0][col])
       #print(row,col)
   print(counters)
   if value > tempcol and row == 0:  # if the value (number of stones) is grater then the index of the colum and the row == 0
       wrap = value - col
       alr = wrap - 7
       #print("wrap =",wrap,"  alr =",alr)
       for i in range(value - wrap):  # the for loop runs while i is <=value-wrap
           col -= 1
           counters[0][col] += 1
           button_grid[0][col].config(text=counters[0][col])
       if wrap > 6:
           wrap -= alr
           #print("NEW wrap =",wrap,"  alr =",alr)
       for j in range(wrap): # while j is <=wrap, the code below will run
           row = 1
           counters[1][col] += 1
           button_grid[1][col].config(text=counters[1][col])
           col += 1
       if alr > 0: #if alr > 0 double wrap on the top row
           for f in range(alr): #traverse the board
               col -= 1
               counters[0][col] += 1
               button_grid[row][col].config(text=counters[0][col])
       col -=1
   #print(row,col)
   #conditions to make the game interesting
   if counters[row][col] == 1: #if you land on an empty space, go again and you get the stones from across the board
       player = not player
       counter1 += counters[1][col]
       #updates player 1's score in label
       counterLabel1.set(str(counter1))
   if counters[row][col] == 3: #if you land on a pit with 3 stones, it becomes zero an you get +3
       counters[row][col] = 0
       button_grid[row][col].config(text=counters[row][col])
       counter1 += 3
       #updates player 1's score in label
       counterLabel1.set(str(counter1))
   if counter1 >= 20:
       counterLabel1.set("You Win!")

def actions1(row,col):
   global player
   global counter2
   if row == 0:
       player = not player
       return
   value = counters[row][col]
   counters[row][col] = 0
   tempcol2 = col
   button_grid[row][col].config(text=counters[row][col])
   if value <= 6 - col and row == 1: # if the value is <= the index of the colum and the row = 0, the code below will run
       row = 1
       for d in range(value): # while a is <= value, the code below will run
           col += 1
           counters[row][col] += 1
           button_grid[row][col].config(text=counters[row][col])
       #print(row,col)
   if value > 6-tempcol2 and row == 1:  # if the value (number of stones) is grater then the index of the column and the row == 0
       wrap = value - (6 - col)
       alr = wrap - 7
       row = 0
       runRow = 6 - col
       for i in range(runRow):  # the for loop runs while i is <= runRow
           col += 1
           counters[1][col] += 1
           button_grid[1][col].config(text=counters[1][col])
       # col = 0
       if wrap > 6:
           wrap -= alr
           #print("NEW wrap =",wrap,"  alr =",alr)
       for j in range(wrap):  # while j is <=wrap, the code below will run
           counters[0][col] += 1
           button_grid[0][col].config(text=counters[0][col])
           col -= 1
       if alr > 0:
           for f in range(alr):
               col += 1
               counters[1][col] += 1
               button_grid[1][col].config(text=counters[1][col])
       col += 1
   print(row, col)
   if counters[row][col] == 1:
       player = not player
       counter2 += counters[1][col]
       button_grid[0][col].config(text=counters[0][col])
       #updates player 2's score in label
       counterLabel2.set(str(counter2))
   if counters[row][col] == 3:
       counters[row][col] = 0
       button_grid[row][col].config(text=counters[row][col])
       counter2 += 3
       #updates player 2's score in label
       counterLabel2.set(str(counter2))
   if counter2 >= 20:
       counterLabel2.set("You Win!")
#this method determines what modifications are made to the board after a player clicks on a pit of their choice.
#The modifications depends on what happens during the move, and what happens after. (i.e if a player lands in an empty pit)
def button_click(row, col):
   global player
   global counterLabel1
   global counterLabel2
   if player == True:
       actions0(row,col)
   elif player == False:
       actions1(row,col)
   player = not player
#print( counters )

# Start the tkinter main loop
root.mainloop()