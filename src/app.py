import tkinter as tk

class App(tk.Tk):
    def __init__(self,screenname : str,sizey : int = 500, sizex:int = 500):
        super().__init__()

        self.title(screenname)
        self.geometry(newGeometry=self.getCoorCenterWindow(self.winfo_screenheight(),self.winfo_screenwidth(),sizex,sizey))

    def run(self):
        
        self.mainloop()

    @staticmethod
    def getCoorCenterWindow(winfo_screenheight:int,winfo_screenwidth:int, sizex : int, sizey:int)->str:
        x = (winfo_screenwidth // 2) - (sizex // 2)
        y = (winfo_screenheight // 2) - (sizey // 2)
        return f"{sizex}x{sizey}+{x}+{y}"
