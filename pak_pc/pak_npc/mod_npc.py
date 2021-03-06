# -*- coding: utf8 -*-
"""
Модуль предоставляющий класс для работы хост-процесса с
множеством процессов по сети. Это будет
универсальное и переносимое решение.
"""

import socket
from threading import Thread
from time import sleep
from pak_pc.pak_npc.mod_connect import ClsNetStore

#--- определение сетевых подключений ---
HOST_VIDEO = "" # localhost

# порт, на который должно прийти подключение от видеокарты.
PORT_VIDEO = 58633

class ClsNPC(Thread):
    """
    Класс обеспечивает взаимодействие различных частей python и cython
    кода через различные процессы.
    Использование мультипроцессинга напрямую вызывает дикие проблемы.
    """
    def __init__(self):
        """
        обеспечивает инициализацию класса сетевых межпроцессорных
        взаимодействий
        :return: возвращает ссылку на себя.
        """

        Thread.__init__(self)
        self.video = ClsNetStore()
        self.cpu = ClsNetStore()

    def run(self):
        """
        Метод исполняется при запуске отдельного потока.
        Метод зациклен.
        """

        def get_video_connect():
            """
            Устанавливает соединение видеокарты.
            """

            # --- создание сервера для подключения
            srv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            #srv.settimeout(5)

            #--- запуск сервера ---
            srv.bind((HOST_VIDEO, PORT_VIDEO))
            # сколько можно одновременно получить подключений на порт
            srv.listen(1)
            # ждём когда подкючится клиент видеокарты
            self.video.conn, self.video.adr = srv.accept()
            net_data = self.video.conn.recv(1024) # получить данные
            print 'conn data =', net_data
            srv.close()
            self.video.conn.close()

        def get_cpu_connect():
            """
            Устанавливает соединение с ЦП.
            """
            pass

        def send_info():
            """
            Отправляет сообщения из очередей сообщений.
            """
            pass

        def get_info():
            """
            Получает сообщения по сети и ставит в очередь обработки.
            """

        # --- получить подключение от видеокарты ---
        get_video_connect()
        # --- получить подключение от ЦП ---
        get_cpu_connect()
        #--- счётчик циклов и цикл
        count_loop = 0

        # получить имя системы и счётчик циклов
        print 'Name = ', self.getName(), count_loop
        print "Слушаю порт".decode('utf8'), PORT_VIDEO

        while 1:
            get_info()
            send_info()
            sleep(1)
            count_loop += 1

if __name__ == '__main__':
    APP = ClsNPC()
    APP.start()
