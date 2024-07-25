import tkinter as tk

class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Calculator")
        self.geometry("220x320")
        self.resizable(0,0)
        self.iconbitmap(r'D:\python programming\logo.ico')
        self.create_widgets()
        
    def create_widgets(self):
        self.display = tk.Entry(self, font=("Arial", 20), justify='right', bd=10, insertwidth=2, width=14, borderwidth=4)
        self.display.grid(row=0, column=0, columnspan=4)

        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
            ('AC', 5, 0)
        ]

        for (text, row, col) in buttons:
            self.create_button(text, row, col)

    def create_button(self, text, row, col):
        button = tk.Button(self, text=text, command=lambda: self.on_button_click(text))
        button.grid(row=row, column=col, ipadx=10, ipady=10, padx=5, pady=5)

    def on_button_click(self, char):
        if char == '=':
            try:
                result = str(eval(self.display.get()))
                self.display.delete(0, tk.END)
                self.display.insert(0, result)
            except Exception as e:
                self.display.delete(0, tk.END)
                self.display.insert(0, "Error")
        elif char == 'AC':
            self.display.delete(0, tk.END)
        elif char in ('+', '-', '*', '/'):
            self.display.insert(tk.END, f' {char} ')
        else:
            self.display.insert(tk.END, char)

if __name__ == "__main__":
    app = Calculator()
    app.mainloop()
