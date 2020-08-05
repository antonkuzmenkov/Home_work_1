# 4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
# А также класс «Оргтехника», который будет базовым для классов-наследников.
# Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс). В базовом классе определить параметры,
# общие для приведенных типов. В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.

class OfficeStaff:
    printer_count = 0
    table_count = 0
    all_staff = {}
    def __init__(self,name,model,year,cost):
        self.name = name
        self.model = model
        self.year = year
        self.cost = cost


    def Ask(self):
        print(f'It\'s {self.name} model {self.model} buy in {self.year} cost {self.cost}')
        ??????