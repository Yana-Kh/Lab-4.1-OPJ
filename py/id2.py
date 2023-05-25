#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from datetime import datetime

"""
Составить программу с использованием классов и объектов для решения задачи.
Во всех заданиях, помимо указанных в задании операций, обязательно должны быть реализованы следующие методы:
−	метод инициализации __init__ ;
−	ввод с клавиатуры read ;
−	вывод на экран display .
Номер варианта необходимо уточнить у преподавателя. В раздел программы, начинающийся после инструкции
if __name__ = '__main__': добавить код, демонстрирующий возможности разработанного класса.

Вариант 29(14)
14. Создать класс Payment (зарплата). В классе должны быть представлены поля:
фамилия-имя-отчество,
оклад,
год поступления на работу,
процент надбавки,
подоходный налог,
количество отработанных дней в месяце,
количество рабочих дней в месяце,
начисленная и удержанная суммы.

Реализовать методы:
вычисления начисленной суммы,
вычисления удержанной суммы,
вычисления суммы, выдаваемой на руки,
вычисления стажа.

Стаж вычисляется как полное количество лет, прошедших от года поступления на работу, до текущего года.
Начисления представляют собой сумму, начисленную за отработанные дни, и надбавки, то есть доли от первой суммы.
Удержания представляют собой отчисления в пенсионный фонд (1% от начисленной суммы) и подоходный налог.
Подоходный налог составляет 13% от начисленной суммы без отчислений в пенсионный фонд.
"""


class Payment:
    def __init__(self, name, salary, year, perc_allow, worked_days, work_days):
        if isinstance(name, str):
            self.name = name
        else:
            self.name = "not name"
        if isinstance(salary, float) or isinstance(salary, int):
            self.salary = salary
        else:
            self.salary = 0
        if isinstance(year, int) and 2023 >= year >= 0:
            self.year = year
        else:
            self.year = 1700
        if isinstance(perc_allow, float) or isinstance(perc_allow, int):
            self.perc_allow = perc_allow
        else:
            self.perc_allow = 0
        if isinstance(worked_days, int) and 31 >= worked_days >= 1:
            self.worked_days = worked_days
        else:
            self.worked_days = 1
        if isinstance(work_days, int) and 31 >= work_days >= 0:
            self.work_days = work_days
        else:
            self.work_days = 0
        try:
            self.accrued_amount = self.accruedAmount()
            self.income_tax = self.accrued_amount * 0.13
            self.amount_withheld = self.amountWithheld()
        except:
            pass


    def read(self):
        try:
            print("-------------------------------ввод")
            self.name = input("ФИО: ")
            self.salary = float(input("Оклад: "))
            self.year = int(input("Год поступления на работу: "))
            self.perc_allow = float(input("Процент надбавки: "))
            self.worked_days = int(input("Количество отработанных дней в месяце: "))
            self.work_days = int(input("Количество рабочих дней в месяце: "))
            self.accrued_amount = self.accruedAmount()
            self.income_tax = self.accrued_amount * 0.13
            self.amount_withheld = self.amountWithheld()
            print("--------------------------------")
        except:
            print("Error")

    def display(self):
        print("-------------------------------вывод")
        print(f"ФИО: {self.name}")
        print(f"Оклад: {self.salary}")
        print(f"Год поступления на работу: {self.year}")
        print(f"Стаж: {self.experience()}")
        print(f"Процент надбавки: {self.perc_allow}%")
        print(f"Подоходный налог: {self.income_tax:.2f}")
        print(f"Количество отработанных дней в месяце: {self.worked_days}")
        print(f"Количество рабочих дней в месяце: {self.work_days}")
        print(f"Начисленная сумма: {self.accrued_amount:.2f}")
        print(f"Удержанная сумма: {self.amount_withheld:.2f}")
        print(f"Сумма выдаваемая на руки: {self.amountOnHand():.2f}")
        print("--------------------------------")

    def experience(self):
        """
        Стаж
        self.experience =
        """
        return datetime.now().year - self.year

    def accruedAmount(self):
        """
        Начисленная сумма
        self.accrued_amount =
        self.income_tax =
        """
        return self.salary * (1 + self.perc_allow / 100) * (self.worked_days / self.work_days)
        return self.accrued_amount * 0.13

    def amountWithheld(self):
        """
        Удержанная сумма
        self.amount_withheld =
        """
        return self.accrued_amount * 0.01 + self.income_tax

    def amountOnHand(self):
        """
        Сумма выдаваемая на руки
        self.amount_on_hand =
        """
        return self.accrued_amount - self.amount_withheld


if __name__ == '__main__':
    person1 = Payment("Петров Игорь Олегович", 32000.0, 2020, 14.0, 19, 28)
    person1.display()
    person2 = Payment(None, None, None, None, None, None)
    person2.read()
    person2.display()
