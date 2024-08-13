import os
import tkinter as tk
from tkinter import *
 
def center_window(width=570,height=600):
   x = (root.winfo_screenwidth()//2 -(width // 2))
   y = (root.winfo_screenheight()//2 -(height//2))
   root.geometry(f'{width}x{height}+{x}+{y}')

class WellcomeMessage(tk.Frame):
    def __init__(self,master):
        super().__init__()
        self.master=master
        self.master.title('Wellcome')
        self.master.resizable(False,False)
        center_window(280,150)
        
        self.create_Widgets()
        self.pack

    def create_Widgets(self):
        quit_button = tk.Button(self, text='Quit', command=self.master.quit)
        quit_button.place(x=10, y=10)
        
        login_button = tk.Button(self, text="Login", width=10)
        login_button.place(x=80, y=60)  # Consistent with place geometry management


root = tk.Tk()
root.eval('tk::PlaceWindow . center')
script_dir = os.path.dirname(os.path.abspath(__file__))

# Define the path to the icon file
icon_path = os.path.join(script_dir, "icon.ico")

root.iconbitmap(icon_path)
WellcomeMessage(root)
root.mainloop()