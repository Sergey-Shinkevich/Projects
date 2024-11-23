import threading
import time
import random


class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()


    def deposit(self):
        for i in range(100):
            poplnenie = random.randint(50, 500)
            self.balance += poplnenie
            if self.balance >= 500 and self.lock.locked() == True:
                self.lock.release()
            print(f'Пополнение: {poplnenie}. Баланс: {self.balance}')
            time.sleep(0.001)

    def take(self):
        for i in range(100):
            snyatie = random.randint(50, 500)
            print(f'Запрос на {snyatie}')
            if snyatie <= self.balance:
                self.balance -= snyatie
                print(f'Снятие {snyatie}. Баланс: {self.balance}')
            else:
                print('Запрос отклонён, недостаточно средств ')
                self.lock.acquire()


bk = Bank()
th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))
th1.start()
th2.start()
th1.join()
th2.join()
print(f'Итоговый баланс: {bk.balance}')

