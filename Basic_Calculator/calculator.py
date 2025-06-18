import tkinter as tk
import math

def click(number):
    entry.insert(tk.END, str(number))

def clear():
    entry.delete(0, tk.END)

def backspace():
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current[:-1])

def square():
    try:
        value = float(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, value ** 2)
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

def square_root():
    try:
        value = float(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, math.sqrt(value))
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

def percentage():
    try:
        value = float(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, value / 100)
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

def evaluate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

def build_calculator():
    welcome_screen.destroy()
    
    root = tk.Tk()
    root.title("Basic Calculator")
    root.geometry("330x520")
    root.configure(bg="#DFFFE0")  # light green

    global entry
    entry = tk.Entry(root, font=("Helvetica", 20), borderwidth=2, relief="solid", justify="right")
    entry.pack(fill="both", padx=10, pady=10, ipady=10)

    button_frame = tk.Frame(root, bg="#DFFFE0")
    button_frame.pack()

    buttons = [
        ('7', 1, 0), ('8', 1, 1), ('9', 1, 2),
        ('4', 2, 0), ('5', 2, 1), ('6', 2, 2),
        ('1', 3, 0), ('2', 3, 1), ('3', 3, 2),
        ('0', 4, 1)
    ]

    ops = [
        ('+', 1, 3), ('-', 2, 3),
        ('*', 3, 3), ('/', 4, 3),
        ('C', 4, 0), ('=', 4, 2),
        ('⌫', 5, 0), ('x²', 5, 1), ('√', 5, 2),
        ('%', 5, 3)
    ]

    for (text, row, col) in buttons + ops:
        if text == "C":
            cmd = clear
        elif text == "=":
            cmd = evaluate
        elif text == "⌫":
            cmd = backspace
        elif text == "√":
            cmd = square_root
        elif text == "x²":
            cmd = square
        elif text == "%":
            cmd = percentage
        else:
            cmd = lambda t=text: click(t)

        tk.Button(button_frame, text=text, font=("Helvetica", 16), width=5, height=2,
                  command=cmd, bg="white").grid(row=row, column=col, padx=5, pady=5)

    root.mainloop()

# Welcome screen
welcome_screen = tk.Tk()
welcome_screen.title("Welcome")
welcome_screen.configure(bg="#DFFFE0")
screen_width = welcome_screen.winfo_screenwidth()
screen_height = welcome_screen.winfo_screenheight()
x = (screen_width // 2) - (300 // 2)
y = (screen_height // 2) - (150 // 2)
welcome_screen.geometry(f"300x150+{x}+{y}")

label = tk.Label(welcome_screen, text="Welcome, User!", font=("Helvetica", 20, "bold"), bg="#DFFFE0")
label.pack(expand=True)

# Show calculator after 2 seconds
welcome_screen.after(2000, build_calculator)
welcome_screen.mainloop()
