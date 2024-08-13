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

    def create_Widgets(self):
        self.quitBotton = tk.Button(self,text='Quit',command=self.quit)
        self.quitBotton.grid()
root = tk.Tk()
root.eval('tk::PlaceWindow . center')
root.iconbitmap("D:\python\calculator project\icon.ico")
WellcomeMessage(root)
root.mainloop()