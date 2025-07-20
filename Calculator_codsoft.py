import tkinter as tk
from tkinter import messagebox

class CalculatorApp:
    def __init__(self,root):
        self.root = root
        root.title("Calculator")
        root.geometry("350x350")
        root.configure(bg= "#b3f3c4")


        self.label1 = tk.Label(root, text="First Number", bg= "#dff9fb",font = ("Times New Roman",12))
        self.label1.place(x=30,y=30)
        self.input1 = tk.Entry(root,font= ("Times New Roman",12) )
        self.input1.place(x=160, y=30)

        self.label2 = tk.Label(root, text="second Number", bg= "#dff9fb",font = ("Times New Roman",12))
        self.label2.place(x=30,y=70)
        self.input2 = tk.Entry(root,font= ("Times New Roman",12) )
        self.input2.place(x=160, y=70)

        self.create_buttons()
        
        self.output = tk.Label(root, text= "", font = ("Times New Roman",12, "bold"),fg= "#E84F8F", bg= "#dff9fb")
        self.output.place(x=30, y=230)
        
    def create_buttons(self):
        btn_area = tk.Frame(self.root,bg= "#dff9fb")
        btn_area.place(x=30, y=130)

        tk.Button(btn_area, text="Add", width=8, font = ("Times New Roman",11,),command=self.do_add).grid(row=0, column=0,padx=5)
        tk.Button(btn_area, text="Subtract", width=8, font = ("Times New Roman",11,),command=self.do_subtract).grid(row=0, column=1,padx=5)
        tk.Button(btn_area, text="Multiply", width=8, font = ("Times New Roman",11,),command=self.do_multiply).grid(row=1, column=0,pady=10)
        tk.Button(btn_area, text="Divide", width=8, font = ("Times New Roman",11,),command=self.do_divide).grid(row=1, column=1,pady=10)

    def read_input(self):
        try:
            number1 = float(self.input1.get())
            number2 = float(self.input2.get())
            return number1,number2
       
        except ValueError:
            messagebox.showwarning("Error","please enter only numbers")
            return None, None
        
    def do_add(self):
        a, b = self.read_input()
        if a is not None:
            self.output.config(text=f"Result: {a+b}")
       
    def do_subtract(self):
        a, b = self.read_input()
        if a is not None:
           self.output.config(text=f"Result: {a-b}")

    def do_multiply(self):
        a, b = self.read_input()
        if a is not None:
           self.output.config(text=f"Result: {a*b}")

    def do_divide(self):
        a, b = self.read_input()
        if a is not None:
            if b == 0:
               messagebox.showwarning("Error", "Cannot divide by zero")
            else:
               self.output.config(text=f"Result: {round(a / b, 3)}")
        
       
if __name__ == "__main__":
    window = tk.Tk()
    app = CalculatorApp(window)
    window.mainloop()
        
        
        