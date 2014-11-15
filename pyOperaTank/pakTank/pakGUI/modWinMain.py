# -*- coding: utf8 -*-
"""
Инициализация пакета для танковой графики.
"""

from Tkinter import Tk, Frame

from pakTank.pakGUI.modFrmButton import clsFrmButton
from pakTank.pakGUI.modFrmLeft import clsFrmLeft
from pakTank.pakGUI.modFrmRight import clsFrmRight

class clsWinMain(Tk):
    """
    Класс обеспечивает графику пользователя.
    """
    def __init__(self, clb=None):
        Tk.__init__(self)
        self.title('Калькулятор танков     ===build. 009===')
        self.minsize(320, 240)
        self.frmButton = clsFrmButton(root=self)
        self.frmLeft = clsFrmLeft(root=self, clb=clb)
        self.frmRight = clsFrmRight(root=self, clb=clb)
        #self.after(1000, self.update_sound)
        #self.mainloop()
        
    def update_sound(self):
        print 'aaa'
        self.after(1000, self.update_sound)
