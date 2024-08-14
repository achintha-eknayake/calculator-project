import os
import tkinter as tk
from tkinter import *
from tkinter import colorchooser

#center the created window 
def center_window(window,width=570,height=600):
   x = (window.winfo_screenwidth()//2 -(width // 2))
   y = (window.winfo_screenheight()//2 -(height//2))
   window.geometry(f'{width}x{height}+{x}+{y}')

class WellcomeMessage(tk.Frame):
    def __init__(self,master):
        super().__init__()
        self.master=master
        self.master.title('Wellcome')
        self.configure(bg="#db0b49")
        self.master.resizable(False,False)
        center_window(280,150)
        center_window(self.master,300,150)
        
        self.selected_colour = "#17161b"  # Default colour
        self.create_Widgets()
        self.pack
        self.pack(fill='both',expand=True)

    def get_input(self):
        user_input = self.entry.get()
        if user_input :
            return user_input+"'s"
        else:
            return ""

    def update_label(self, *args):
        self.label_name.config(text=self.entry_var.get(), fg="black")

    def pick_color(self):
        colour_code = colorchooser.askcolor(title='choose colour')
        if colour_code[1]:
            self.selected_colour = colour_code[1]
    def create_Widgets(self):

        self.entry_var =tk.StringVar()
        self.entry_var.trace_add('write',self.update_label)
        self.entry =tk.Entry(self,width=15,font=('Arial',16),textvariable = self.entry_var)
        self.entry.place(x=45,y=60)
        
        self.label_name =tk.Label(self,width=22,height=1,text="Your name ...",font=('arial',10),fg="grey")
        self.label_name.place(x=45,y=20)

        colour_button = tk.Button(self, text='Select colour', command=self.pick_color)
        colour_button.place(x=150, y=100)    
        
        quit_button = tk.Button(self, text='Quit', command=self.master.quit)
        quit_button.place(x=10, y=10)
        quit_button.place(x=270, y=0)
        
        login_button = tk.Button(self, text="Login", width=10)
        login_button.place(x=80, y=60)  # Consistent with place geometry management
        login_button = tk.Button(self, text="Login", width=10, command=self.on_login)
        login_button.place(x=45, y=100)  

    def on_login(self):
        user_input = self.get_input()
        for widget in self.winfo_children():
            widget.destroy()
        self.destroy()
        Calculator(self.master,user_input,self.selected_colour)


class Calculator(tk.Frame):
    def __init__(self,master,user_input,colour):
        super().__init__()
        self.master = master
        self.user_input =user_input
        self.colour = colour
        self.master.title(f"{user_input} Calculator")
        self.master.resizable(False,False)
        self.configure(bg=colour)
        center_window(self.master)
        self.equation =""

root = tk.Tk()
root.eval('tk::PlaceWindow . center')
        self.create_widgets()
        self.pack(fill='both',expand=True)

    def show(self,value):
        self.equation += value
        self.label_result.config(text = self.equation)

    def clear(self):
        self.equation = ""
        self.label_result.config(text=self.equation)
        
    def calculate(self):
        try:
            result = str(eval(self.equation))
            self.label_result.config(text=result)
            self.equation = result  # Allow chaining of calculations
        except Exception as e:
            self.label_result.config(text="Incorrect calculation")
            self.equation = ""


    def create_widgets(self):
        
        self.label_result = tk.Label(self,width=25,height=2,text="",font=("arial",30))
        self.label_result.pack()  # Added placement for the result label

        
        Button(self,text="C", width=5, height=1, font=("arial",30,"bold"), bd=1,fg="#fff",bg="#3697f5",command=lambda: self.clear()).place(x=10,y=100)
        Button(self,text="/", width=5, height=1, font=("arial",30,"bold"), bd=1,fg="#fff",bg="#2a2d36",command=lambda: self.show("/")).place(x=150,y=100)
        Button(self,text="%", width=5, height=1, font=("arial",30,"bold"), bd=1,fg="#fff",bg="#2a2d36",command=lambda: self.show("%")).place(x=290,y=100)
        Button(self,text="*", width=5, height=1, font=("arial",30,"bold"), bd=1,fg="#fff",bg="#2a2d36",command=lambda: self.show("*")).place(x=430,y=100)

        Button(self,text="7", width=5, height=1, font=("arial",30,"bold"), bd=1,fg="#fff",bg="#2a2d36",command=lambda: self.show("7")).place(x=10,y=200)
        Button(self,text="8", width=5, height=1, font=("arial",30,"bold"), bd=1,fg="#fff",bg="#2a2d36",command=lambda: self.show("8")).place(x=150,y=200)
        Button(self,text="9", width=5, height=1, font=("arial",30,"bold"), bd=1,fg="#fff",bg="#2a2d36",command=lambda: self.show("9")).place(x=290,y=200)
        Button(self,text="-", width=5, height=1, font=("arial",30,"bold"), bd=1,fg="#fff",bg="#2a2d36",command=lambda: self.show("-")).place(x=430,y=200)
        
        Button(self,text="4", width=5, height=1, font=("arial",30,"bold"), bd=1,fg="#fff",bg="#2a2d36",command=lambda: self.show("4")).place(x=10,y=300)
        Button(self,text="5", width=5, height=1, font=("arial",30,"bold"), bd=1,fg="#fff",bg="#2a2d36",command=lambda: self.show("5")).place(x=150,y=300)
        Button(self,text="6", width=5, height=1, font=("arial",30,"bold"), bd=1,fg="#fff",bg="#2a2d36",command=lambda: self.show("6")).place(x=290,y=300)
        Button(self,text="+", width=5, height=1, font=("arial",30,"bold"), bd=1,fg="#fff",bg="#2a2d36",command=lambda: self.show("+")).place(x=430,y=300)

# Define the path to the icon file
icon_path = os.path.join(script_dir, "icon.ico")
        Button(self,text="1", width=5, height=1, font=("arial",30,"bold"), bd=1,fg="#fff",bg="#2a2d36",command=lambda: self.show("1")).place(x=10,y=400)
        Button(self,text="2", width=5, height=1, font=("arial",30,"bold"), bd=1,fg="#fff",bg="#2a2d36",command=lambda: self.show("2")).place(x=150,y=400)
        Button(self,text="3", width=5, height=1, font=("arial",30,"bold"), bd=1,fg="#fff",bg="#2a2d36",command=lambda: self.show("3")).place(x=290,y=400)
        Button(self,text="0", width=11, height=1, font=("arial",30,"bold"), bd=1,fg="#fff",bg="#2a2d36",command=lambda: self.show("0")).place(x=10,y=500)

root.iconbitmap(icon_path)
WellcomeMessage(root)
root.mainloop()        Button(self,text=".", width=5, height=1, font=("arial",30,"bold"), bd=1,fg="#fff",bg="#2a2d36",command=lambda: self.show(".")).place(x=290,y=500)
        Button(self,text="=", width=5, height=3, font=("arial",30,"bold"), bd=1,fg="#fff",bg="#fe9037",command=lambda: self.calculate()).place(x=430,y=400)
