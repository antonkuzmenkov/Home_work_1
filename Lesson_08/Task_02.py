# Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
# Проверьте его работу на данных, вводимых пользователем.
# При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.

class VisNull:
    def __init__(self, div, den):
        self.div = div
        self.den = den

    @staticmethod
    def divnull(div, den):
        try:
            return (div / den)
        except:
            return (f"Нельзя")


div = VisNull(2, 20)
print(div.divnull(100, 0))
print(div.divnull(100, 1))