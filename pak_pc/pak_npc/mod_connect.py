# -*- coding: utf8 -*-
"""
Модуль предоставляет класс для сохранения данных о подключении.
"""

from Queue import Queue

class ClsNetStore(object):
    """
    Класс хранит данные о подключении.
    """
    def __init__(self, adr='localhost', port=None):
        """
        Создаёт объект сетевого подключения
        :param adr: ip-адрес соединения
        :param port: сетевой порт.
        """
        # сетевые адрес и порт
        self.conn = adr
        self.port = port

        # признак установленного подключения
        self.__connecting = False

        # создание очередей для приёма и отправки информации в дочерние
        # процессы
        self.__out = Queue()
        self.__in = Queue()

    def put(self, info=None):
        """
        Помещает информацию в исходящую очередь.
        """
        if (info is dict) and not info.empty():
            self.out.append(info)
    
    def get(self):
        """
        Извлекает из очереди информацию.
        """
        if not self.__in.empty():
            return self.__out[-1]

    @property
    def connecing(self):
        return self.__connecting
