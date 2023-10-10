import tkinter as tk

counters = [[0,4,4,4,4,4,4],[4,4,4,4,4,4,0]]

p1 = True
p2 = False


def button_click(row, col):
    # Handle button click event here
    print( row  , col )
    value = counters[row][col]
    counters[row][col] = 0
    button_grid[row][col].config(text=counters[row][col])
    if value > col:
        wrap = value - col
        if row == 0:
            for i in range(value-wrap):
                col -= 1
                counters[row][col] += 1
                button_grid[row][col].config(text=counters[row][col])
            col = 0
            for j in range(wrap):
                counters[1][col] += 1
                button_grid[1][col].config(text=counters[1][col])
                col += 1
        """if row == 1:
            for i in range(value-wrap):
                col += 1
                counters[row][col] += 1
                button_grid[row][col].config(text=counters[row][col])
            for j in range(wrap):
                col = 6
                counters[0][col] += 1
                button_grid[0][6].config(text=counters[0][col])
                col -= 1"""


    print( counters )



# Create the main window
root = tk.Tk()
root.title("2x6 Grid of Buttons")

# Create a 2x6 grid of buttons
button_grid = []
for i in range(2):
    row = []
    for j in range(7):
        button = tk.Button(root, text=counters[i][j], command=lambda i=i, j=j: button_click(i, j),
        height = 2, width = 4, font = ("Times New Roman",70))
        button.grid(row=i, column=j, padx=10, pady=10)
        row.append(button)
    button_grid.append(row)
button_grid[0][0].config(fg="red")
button_grid[1][6].config(fg="blue")

# Run the Tkinter main loop
root.mainloop()

