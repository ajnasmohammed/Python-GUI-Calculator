import tkinter as tk

# --- handlers --------------------------------------------------------------
def click(label):
    """
    Called when a button is pressed.
    'label' is the button label (string): a digit, operator, '=', or 'C'.
    """
    current = box.get()

    if label == "=":
        # evaluate current expression
        try:
            result = eval(current)    # caution: eval on user input
            box.delete(0, tk.END)
            box.insert(tk.END, str(result))
        except Exception:
            box.delete(0, tk.END)
            box.insert(tk.END, "Error")

    elif label == "C":
        box.delete(0, tk.END)

    else:
        # add label text to the right of the display
        box.insert(tk.END, label)


# --- main window -----------------------------------------------------------
window = tk.Tk()
window.title("Calculator")
window.geometry("360x420")
window.resizable(False, False)

# Entry widget (display)
box = tk.Entry(window, font=("Arial", 24), justify="right")
box.pack(fill=tk.X, padx=10, pady=10, ipady=10)

# Frame to hold buttons
btn_frame = tk.Frame(window)
btn_frame.pack(padx=10, pady=(0,10))

# Buttons to create (4 columns x 5 rows layout)
button_labels = [
    "7", "8", "9", "+",
    "4", "5", "6", "-",
    "1", "2", "3", "*",
    "C", "0", "=", "/"
]

# Create and grid the buttons
for i, label in enumerate(button_labels):
    b = tk.Button(
        btn_frame,
        text=label,
        font=("Arial", 16),
        width=5,
        height=2,
        command=lambda x=label: click(x)
    )
    row = i // 4
    col = i % 4
    b.grid(row=row, column=col, padx=6, pady=6)

# Start the GUI loop
window.mainloop()

