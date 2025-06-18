import tkinter as tk
from tkinter import messagebox

def calculate():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        op = operator.get()

        if op == '+':
            result = num1 + num2
        elif op == '-':
            result = num1 - num2
        elif op == '*':
            result = num1 * num2
        elif op == '/':
            if num2 == 0:
                raise ZeroDivisionError
            result = num1 / num2
        elif op == '%':
            result = num1 % num2
        else:
            messagebox.showerror("Invalid Operator", "Please select a valid operator.")
            return

        result_label.config(text=f"Result: {round(result, 2)}")

    except ZeroDivisionError:
        messagebox.showerror("Math Error", "Cannot divide by zero.")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numeric values.")

# GUI Setup
app = tk.Tk()
app.title("Basic Calculator")
app.geometry("350x300")
app.resizable(False, False)

tk.Label(app, text="Enter First Number:").pack(pady=5)
entry_num1 = tk.Entry(app, font=("Arial", 12))
entry_num1.pack()

tk.Label(app, text="Enter Second Number:").pack(pady=5)
entry_num2 = tk.Entry(app, font=("Arial", 12))
entry_num2.pack()

tk.Label(app, text="Select Operator:").pack(pady=5)
operator = tk.StringVar(value='+')
op_menu = tk.OptionMenu(app, operator, '+', '-', '*', '/', '%')
op_menu.pack()

tk.Button(app, text="Calculate", command=calculate, font=("Arial", 12)).pack(pady=15)

result_label = tk.Label(app, text="Result: ", font=("Arial", 12))
result_label.pack()

app.mainloop()
