import random
import threading
import time
from queue import Queue


class Table:
    def __init__(self, number):
        self.number = number
        self.guest = None


class Guest(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name

    def run(self):
        pause = random.randint(3, 10)
        time.sleep(pause)

class Cafe:
    def __init__(self, *tables):
        self.tables = tables
        self.queue = Queue()


    def guest_arrival(self, *guests):
    # Перебираем гостей для усаживания
        for current_guest in guests:
    # Поиск количества свободных столов
            counter_free_tables = 0
            for current_table in self.tables:
                if current_table.guest == None:
                    counter_free_tables += 1
    # Поиск свободного стола при наличии свободных
            if counter_free_tables >0:
                for current_table in self.tables:
                    if current_table.guest == None:
                        free_table = current_table
                        break
    # Сажаем гостя за стол
            if counter_free_tables > 0:
                free_table.guest = current_guest
                a = threading.Thread(target=current_guest.run)
                a.start()
                print(f'{current_guest.name} сел(-а) за стол номер {free_table.number}')
    # Создание очереди
            else:
                self.queue.put(current_guest)
                print(f'{current_guest.name} в очереди')

    def check_busy_table(self, *args):
        busy_table = 0
        for current_table in self.tables:
            if current_table.guest != None:
                busy_table += 1
        return busy_table

    def discuss_guests(self):
        busy_table = self.check_busy_table(self)
        status_queue = self.queue.empty()
    # Запуск обслуживания
        while status_queue == False and busy_table != 0:
    # Проверка на окончание приема пищи
            for current_table in self.tables:
                if current_table.guest != None and current_table.guest.is_alive() == False:
                    print(f'{current_table.guest.name} за текущим столом покушал(-а) и ушёл(ушла)')
                    print(f'Стол номер {current_table.number} свободен')
                    current_table.guest = None
                if status_queue == False and busy_table < len(self.tables):
                    if current_table.guest == None:
                        current_table.guest = self.queue.get()
                        print(f'{current_table.guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {current_table.number}')
                        a = threading.Thread(target=current_table.guest.run)
                        a.start()
            busy_table = self.check_busy_table(self)
            status_queue = self.queue.empty()






# Создание столов
tables = [Table(number) for number in range(1, 6)]
# Имена гостей
guests_names = ['Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman', 'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra']
# Создание гостей
guests = [Guest(name) for name in guests_names]
# Заполнение кафе столами
cafe = Cafe(*tables)
# Приём гостей
cafe.guest_arrival(*guests)
# Обслуживание гостей
cafe.discuss_guests()