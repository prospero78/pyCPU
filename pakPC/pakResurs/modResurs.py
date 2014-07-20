# -*- coding: utf8 -*-
'''
Класс ресурсов. Содержит всякие полезные штуки для интернационализации, графики и т. д.
'''
class clsRes:
    def __init__(self, root=None, lang='ru', arg=[]):
        self.root=root
        self.lang=lang
        self.arg=arg

        self.pars_arg()
        self.create_res()
        if self.lang=='ru':
            self.create_ru()

    def pars_arg(self):
        if len(self.arg)>1:
            for i in self.arg:
                if ('--help' in i) or ('-h' in i) or ('/h' in i):
                    print '''
Пример запуска: "python main.py --help"
Помощь по ключам командной строки:
    --help (-h)      показать эту справку
    --about (-a)     о программе
                    '''.decode('utf8')
                elif ('--about' in i) or ('-a' in i):
                    print '''
О программе:
    Эта программа представляет собой вымышленный
    (но вполне рабочий) виртуальный компьютер.
    Конечная цель:
        -создать (на сколько это возможно) платформонезависимый компьютер
        -с понятной и простой системой команд, архитектурой
        -дать людям бесплатный инструмент для безопасной работы в этих
            ваших тырнетах
        -наконец-то покончить с дикими вирусами (хотя, хотя.... хотелось бы)
    ------------------
    (A) Valeriy Shipkov, 2014
    (L) GNU GPL v.3
                    '''.decode('utf8')

    def create_res(self):
        self.vers='210' # текущая версия сборки
        self.max_adr=2**16 # максимальный адрес памяти
        self.max_reg_val=2**16 # максимальное значение регистра

        # инициализация биоса
        from modBios import bios
        self.bios=bios

    def create_ru(self):
        self.winMain_name='pyPC    Vers. '+self.vers
        self.winMain_btnExit_name='Выход'
        self.winMain_mbtFile_name='Файл'
        self.winMain_mbtEdit_name='Правка'
        self.winMain_mbtCustom_name='Настройка'
        self.winMain_mbtHelp_name='Справка'
        self.winMain_mbtHelp_help='Справка по программе'
        self.winMain_mbtHelp_about='О программе'
