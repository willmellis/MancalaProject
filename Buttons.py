import tkinter as tk

def button_click():

pass

Counters = [
    [4, 4, 4, 4, 4, 4],
    [4, 4, 4, 4, 4, 4]
]


mancalaP1 = 0
manacalaP2 = 0


root = tk.Tk()
root.title("Button Grid")



button_grid = []
for i in range(2):
    row = []
    for j in range(6):
        button = tk.Button(root, text=Counters[i][j], command=button_click, font=("Arial",75))
        button.grid(row=i, column=j, padx=10, pady=10)
        row.append(button)
    button_grid.append(row)







root.mainloop()
