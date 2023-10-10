import tkinter as tk

# Create a function to update the count when the button is clicked
def increment_count():
    global count
    count += 1
    count_label.config(text="Count: " + str(count))

# Create the main application window
app = tk.Tk()
app.title("Counting Button")

# Initialize the count variable
count = 0

# Create a button widget
count_button = tk.Button(app, text="Click Me", command=increment_count)
count_button.pack(pady=30, padx=389)

# Create a label widget to display the count
count_label = tk.Label(app, text="Count: 0")
count_label.pack()

# Start the tkinter main loop
app.mainloop()
