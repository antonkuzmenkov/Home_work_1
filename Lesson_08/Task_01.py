# Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки
# формата «день-месяц-год». В рамках класса реализовать два метода. Первый,
# с декоратором @classmethod, должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
# Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
# Проверить работу полученной структуры на реальных данных.

class Data:
    def __init__(self, d_m_y):
        self.d_m_y = str(d_m_y)

    @classmethod
    def a(cls, d_m_y):
        m_date = []

        for i in d_m_y.split():
            if i != '-': m_date.append(i)

        return int(m_date[0]), int(m_date[1]), int(m_date[2])

    @staticmethod
    def b(day, month, year):

        if 1 <= day <= 30:
            if 1 <= month <= 12:
                if 2021 >= year >= 0:
                    return f'Верно'
                else:
                    return f'Измени год'
            else:
                return f'Измени месяц'
        else:
            return f'Измени день'

    def __str__(self):
        return f'Дата {Data.a(self.d_m_y)}'


today = Data('22 - 2 - 2015')
print(today)
print(today.b(13, 13, 2012))
