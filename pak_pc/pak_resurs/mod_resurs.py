# -*- coding: utf8 -*-
"""
Класс ресурсов. Содержит всякие полезные штуки для интернационализации,
графики и т. д.
"""


class ClsRes(object):
    """
    Класс создаёт все необходимые ресурсы в программе.
    """

    def __init__(self, root=None, lang='ru', arg=None):
        """
        Создаёт класс ресурсов
        :param root: ссылка на себя
        :param lang:  строка языка
        :param arg: аргументы командной строки
        :return:
        """
        self.__root = root
        self.__lang = lang
        self.arg = arg
        self.build = '0.1390'  # текущая версия сборки

        fread = open('./pak_pc/pak_resurs/txt/GNU_GPL_v3_eng.txt', 'r')
        lic_eng = fread.read()
        fread.close()

        self.pars_arg()
        if self.lang == 'ru':
            from pak_pc.pak_resurs.mod_lang_ru import ClsLangRu

            self.lang_str = ClsLangRu(lang=self.__lang)

        self.lang_str.lang_dict['win_license_origin'] = lic_eng

    @property
    def lang(self):
        """
        Свойство хранит в себе значение языка.
        """
        return self.__lang

    @lang.setter
    def lang(self, lang='ru'):
        """
        Устанавливает текущий язык программы.
        """
        self.__lang = lang

    def pars_arg(self):
        """
        Осуществляет парсинг аргументов передаваемых при запуске
        программы.
        """
        if len(self.arg) > 1:
            for i in self.arg:
                if ('--help' in i) or ('-h' in i) or ('/h' in i):
                    print '''
Пример запуска: "python main.py --help"
Помощь по ключам командной строки:
    --help (-h)      показать эту справку
    --about (-a)     о программе
                    '''.decode('utf8')
                elif ('--about' in i) or ('-a' in i):
                    print '''pyPC build. ''' + self.build + '''
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
