# -*- coding: utf8 -*-
'''
Класс окна "О программе".
'''

from Tkinter import Toplevel

class clsWinAbout(Toplevel):
    def __init__(self, root=None):
        self.root=root
        Toplevel.__init__(self)
        self.state('withdrawn')
        
    def show(self):
        self.state('normal')
