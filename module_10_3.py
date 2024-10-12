# Блокировки и обработка ошибок
# Задача "Банковские операции"
from threading import Lock, Thread
from random import randint
from time import sleep

lock = Lock()

class Bank:
    def __init__(self, balance):
        self.balance = balance
        print(f'Входящий баланс: {self.balance}')
        print('------------------------------------------')

    def deposit(self):
        for i in range(100):
            credit = randint(50, 500)
            self.balance += credit
            if self.balance >= 000 and lock.locked():
                lock.release()
            print(f'Пополнение: {credit:4}      Баланс: {self.balance:5}')
            sleep(0.001)

    def take(self):
        for i in range(100):
            debet = randint(50, 500)
            print(f'\nЗапрос на  {debet:5}')
            if debet <= self.balance:
                self.balance -= debet
                print(f'Снятие:     {debet:4}      Баланс: {self.balance:5}')
            else:
                print('Запрос отклонён, недостаточно средств.')
                lock.acquire()


bk = Bank(randint(0, 500))

# Т.к. методы принимают self, в потоки нужно передать сам объект класса Bank
th1 = Thread(target=Bank.deposit, args=(bk,))
th2 = Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()
print('-----------------------------------')
print(f'Итоговый баланс: {bk.balance}')
