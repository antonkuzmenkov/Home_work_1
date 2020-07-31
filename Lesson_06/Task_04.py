# Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты:
# speed, color, name, is_police (булево). А также методы: go, stop, turn(direction),
# которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar)
# и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.

class Car:
    # atributes
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    # methods
    def go(self):
        return f'{self.name}  start'

    def stop(self):
        return f'{self.name}  stop'

    def turn_right(self):
        return f'{self.name}  turn right'

    def turn_left(self):
        return f'{self.name}  turn left'

    def show_speed(self):
        return f'Correct speed {self.name} is {self.speed}'


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Correct speed of town car {self.name} is {self.speed}')

        if self.speed > 40:
            return f'Speed of {self.name} is higher '
        else:
            return f'Speed of {self.name} is normal'

class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Correct speed of work car {self.name} is {self.speed}')

        if self.speed > 60:
            return f'Speed of {self.name} is higher'


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def police(self):
        if self.is_police:
            return f'{self.name} go to the office'
        else:
            return f'{self.name} patrol the street'


ferrari = SportCar(100, 'black', 'ferrari', False)
hyandai = TownCar(30, 'Yellow', 'hyandai', False)
solaris = WorkCar(70, 'Green', 'solaris', True)
mustang = PoliceCar(110, 'Blue',  'mustang', True)
print(solaris.turn_right())
print(f'When {hyandai.turn_right()}, then {hyandai.stop()}')
print(f'{mustang.go()} with speed exactly {mustang.show_speed()}')
print(f'{ferrari.name} is {ferrari.color}')
print(f'Is {mustang.name} a police? {mustang.is_police}')
