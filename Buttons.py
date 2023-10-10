import tkinter as tk

counters = [[4,4,4,4,4,4],[4,4,4,4,4,4]]

def button_click(row, col):
    # Handle button click event here
    value = counters[row][col]
    counters[row][col] = 0
    if row == 0:
        for i in value:
            col =- 1
            counters[row][col] += 1


# Create the main window
root = tk.Tk()
root.title("2x6 Grid of Buttons")

# Create a 2x6 grid of buttons
button_grid = []
for i in range(2):
    row = []
    for j in range(6):
        button = tk.Button(root, text=counters[i][j], command=lambda i=i, j=j: button_click(i, j))
        button.grid(row=i, column=j, padx=10, pady=10)
        row.append(button)
    button_grid.append(row)

# Run the Tkinter main loop
root.mainloop()

