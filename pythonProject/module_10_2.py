import threading
import time


class Knight(threading.Thread):
    def __init__(self, name, power):
        threading.Thread.__init__(self)
        self.name = name
        self.power = power

    def run(self):
        print(f'{self.name}, на нас напали!')
        day = 1
        for i in range(100, 0, -self.power):
            print(f'{self.name} сражается {day} день(дня)..., осталось {i - self.power} воинов')
            day += 1
            time.sleep(1)
        print(f'{self.name} одержал победу спустя {day-1} дней(дня)!')


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)
first_knight.start()
second_knight.start()
first_knight.join()
second_knight.join()
print('Все битвы закончились!')
