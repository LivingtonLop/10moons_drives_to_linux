import tkinter as tk

from src.widgets.tablet_connection_status import TabletConnectionStatus
from src.widgets.tablet_press_diagram import TabletPressDiagram
from src.widgets.tablet_panel_draw import TabletPanelDraw

from src.conect_usb import Observer


class App(tk.Tk):
    def __init__(self,screenname : str,sizey : int = 500, sizex:int = 1000):
        super().__init__()

        self.title(screenname)
        self.geometry(newGeometry=self.getCoorCenterWindow(self.winfo_screenheight(),self.winfo_screenwidth(),sizex,sizey))
        #connection
        self.usb_event = Observer()
        #widgets
        self.tcs = TabletConnectionStatus(root=self)
        self.status_tablet : bool = False
        self.tpd = TabletPressDiagram(root=self)
        self.tpdd = TabletPanelDraw(root=self)

    def run(self):
        self.tcs.show()
        self.tcs.logic(status= self.status_tablet)

        self.tpd.create_cuadricule(self.tpd.canva,20)
        self.tpd.show()

        self.tpdd.show() #ya se ejecuta uwu

        self.mainloop()

    def event(self):
        pass

    @staticmethod
    def getCoorCenterWindow(winfo_screenheight:int,winfo_screenwidth:int, sizex : int, sizey:int)->str:
        x = (winfo_screenwidth // 2) - (sizex // 2)
        y = (winfo_screenheight // 2) - (sizey // 2)
        return f"{sizex}x{sizey}+{x}+{y}"
