# -*- coding: utf8 -*-
'''
Этот модуль заточен под отображение состояния центрального процессора.
Ввиду его отдельности -- его можно втыкать куда угодно. )
'''

from Tkinter import Frame

from pakPC.pakGUI.pakWidgets.modFrmReg import clsFrmReg
from pakPC.pakGUI.pakWidgets.modFrmRegPC import clsFrmRegPC
from pakPC.pakGUI.pakWidgets.modFrmRegBP import clsFrmRegBP

class clsFrmCPU(Frame):
    def __init__(self, root=None):
        Frame.__init__(self, master=root, border=3, relief='sunken')
        self.pack(side='top', fill='x')
        
        # отображаем регистр программной отладки
        self.frmRegBP=clsFrmRegBP(root=self)
        
        # отображаем программный счётчик
        self.frmRegPC=clsFrmRegPC(root=self)
        #self.frmRegA.lblName['text']='RegA'
        
        # отображение регистра А
        self.frmRegA=clsFrmReg(root=self)
        self.frmRegA.lblName['text']='RegA'
