import calculator
import tkinter as tk
import os

def main():
    root = tk.Tk()
    root.eval('tk::PlaceWindow . center')
    

    script_dir = os.path.dirname(os.path.abspath(__file__))
    icon_path = os.path.join(script_dir, "icon.ico")
    root.iconbitmap(icon_path)

    app=calculator.WellcomeMessage(root)
    root.mainloop()

if __name__ == "__main__":
    main()