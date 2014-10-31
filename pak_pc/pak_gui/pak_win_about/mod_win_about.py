# -*- coding: utf8 -*-
'''
Класс окна "О программе".
'''

from Tkinter import Toplevel, Frame, Button, Label, Text, Scrollbar

class clsWinAbout(Toplevel):
    def __init__(self, root=None):
        def create_self():
            Toplevel.__init__(self)
            self.state('withdrawn')
            self.title(self.lang['win_about_name'])
            self.minsize(380, 200)
        
        def create_frmUp():
            self.frmUp=Frame(self, border=3, relief='groove')
            self.frmUp.pack(fill='both', expand=1, side='top')
            
            self.lblPyPC=Label(self.frmUp, border=3, relief='sunken', text=' pyPC \n'+self.root.res.build, bg='white', fg='red', font='Arial 24 bold')
            self.lblPyPC.pack(side='left', fill='y')
            
            self.lblGit=Label(self.frmUp, text=self.lang['win_about_url'], fg='blue', cursor='hand2')
            self.lblGit.pack(side='bottom', fill='x')
            
            self.scbAbout=Scrollbar(self.frmUp)
            self.scbAbout.pack(side='right', fill='y')
            
            self.txtAbout=Text(self.frmUp, height=12, width=30, font='Courier 9')
            self.txtAbout.pack(fill='both', expand=1, side='left')
            self.txtAbout.insert('end', self.lang['win_about_txt'])
            
            self.scbAbout.config(command=self.txtAbout.yview)
            self.txtAbout.config(yscrollcommand=self.scbAbout.set)
            
        
        def create_frmBtn():
            self.frm_btn=Frame(self, border=3, relief='raised')
            self.frm_btn.pack(side='bottom', fill='x')
            
            self.btn_close_about=Button(self.frm_btn, text=self.lang['win_about_close'], bg='gray', command=self.destroy)
            self.btn_close_about.pack(side='right')
            
            self.btnLicense=Button(self.frm_btn, text=self.lang['win_about_license'], bg='gray', command=self.root.control.show_winLicense)
            self.btnLicense.pack()
        
        self.root=root
        self.lang=root.res.lang_str.lang_dict
        create_self()
        create_frmUp()
        create_frmBtn()
        
        
        
    def show(self):
        self.state('normal')
        # показать поверх всех с фокусом
        self.focus_set()
        self.grab_set()
        self.wait_window()
        
    def destroy(self):
        self.state('withdrawn')
        self.grab_release()
        
    def win_exit(self):
        self.destroy()
