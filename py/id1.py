#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Парой называется класс с двумя полями, которые обычно имеют имена first и second.
Требуется реализовать тип данных с помощью такого класса. Во всех заданиях обязательно должны
присутствовать:
метод инициализации __init__ ; (метод должен контролировать значения аргументов на корректность)
ввод с клавиатуры read ;
вывод на экран display .
Реализовать внешнюю функцию с именем make_тип() , где тип — тип реализуемой структуры.
Функция должна получать в качестве аргументов значения для полей структуры и возвращать
структуру требуемого типа. При передаче ошибочных параметров следует выводить сообщение
и заканчивать работу.
Номер варианта необходимо уточнить у преподавателя. В раздел программы, начинающийся
после инструкции if __name__ = '__main__': добавить код, демонстрирующий возможности
разработанного класса.

Вариант 29(9)
9. Поле first — целое положительное число, часы; поле second — целое положительное
число, минуты. Реализовать метод minutes() — приведение времени в минуты.
"""


class MyTime:
    def __init__(self, first=0, second=0):
        if isinstance(first, int) and isinstance(second, int) and first >= 0 and second >= 0:
            self.first = first
            self.second = second
        else:
            raise ValueError

    def read(self):
        try:
            self.first = int(input("Enter hours: "))
            self.second = int(input("Enter minutes: "))
        except:
            print("Error")

    def display(self):
        print(f"First (hours): {self.first}")
        print(f"Second (minutes): {self.second}")

    def minutes(self):
        print(f"Time in minutes: {self.first * 60 + self.second}")


def make_MyTime(first, second):
    return MyTime(first, second)


if __name__ == '__main__':
    mew_time = make_MyTime(4, 23)
    mew_time.display()
    mew_time.minutes()
    mew_time.read()
    mew_time.display()
    mew_time.minutes()
