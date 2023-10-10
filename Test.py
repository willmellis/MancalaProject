import tkinter as tk


def button_click(row, col):
    global Counters, mancalaP1, mancalaP2
    stones = Counters[row][col]
    Counters[row][col] = 0

    # Distribute stones to adjacent pits
    while stones > 0:
        col += 1
        if col == 6:
            row = 1 - row
            col = 0
        Counters[row][col] += 1
        stones -= 1

    # Update button labels
    update_buttons()


def update_buttons():
    global Counters, mancalaP1, mancalaP2
    for i in range(2):
        for j in range(6):
            button_grid[i][j]["text"] = Counters[i][j]

    # Update Mancala counts
    mancala_label_P1["text"] = f"Player 1 Mancala: {mancalaP1}"
    mancala_label_P2["text"] = f"Player 2 Mancala: {mancalaP2}"


Counters = [
    [4, 4, 4, 4, 4, 4],
    [4, 4, 4, 4, 4, 4]
]
mancalaP1 = 0
mancalaP2 = 0

# Create the main window
root = tk.Tk()
root.title("Mancala Game")

count_label = tk.Label(root, text="Mancala Game")
count_label.pack()

# Create labels for Mancala counts
mancala_label_P1 = tk.Label(root, text=f"Player 1 Mancala: {mancalaP1}")
mancala_label_P1.pack()
mancala_label_P2 = tk.Label(root, text=f"Player 2 Mancala: {mancalaP2}")
mancala_label_P2.pack()

# Create a 2x6 grid of buttons
button_grid = []
for i in range(2):
    row = []
    for j in range(6):
        button = tk.Button(root, text=Counters[i][j], command=lambda i=i, j=j: button_click(i, j), font=("Arial", 20))
        button.grid(row=i, column=j, padx=10, pady=10)
        row.append(button)
    button_grid.append(row)

# Run the Tkinter main loop
root.mainloop()
