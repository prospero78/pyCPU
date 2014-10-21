# -*- coding: utf8 -*-
'''
Класс видеокарты.
Видеокарта приписана жёстко к портам.
Порт:
    0 -- запрос на поддерживаемые режимы (RegA)
    1 -- запрос на установку режима (RegA)

Команды запроса:
1 -- установить режим
    (
'''


class clsVideo:
    def __init__(self, root=None):
        '''
        По умолчанию создаётся один экран в текстовом режиме, монохромный,
        размером 80*40 знакомест (3200 позиций).
        '''
        self.root=root
        self.mode_max=0
        self.mode_current=0
        
        self.command=0
        self.buf=''
#        self.adr={}
#        for i in xrange(0, 3200):
#            self.adr[i]=0
        self.adr=' '*3200 # будет символный экран на 3200 символов.
    
    def fill(self, color='#000'):
        '''
        Заполнение экрана виртуального компьютера заданным цветом.
        '''
        pass
