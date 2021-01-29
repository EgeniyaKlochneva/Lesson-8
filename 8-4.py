class Storage:
    def __init__(self):
        self._dict = {}

    def add_to(self, office_equipment):
        self._dict.setdefault(office_equipment.group_name(), []).append(office_equipment)

    def extract(self, device_name): #Евгений, не могу разобраться почему не работает вывод со склада по имени..
        #крутила крутила...так и не получилось
        if self._dict[device_name]:
            self._dict.setdefault[device_name].pop(0)


class OfficeEquipment:
    def __init__(self, device_name, device_type, work_speed, price):
        self.device_name = device_name
        self.device_type = device_type
        self.work_speed = work_speed
        self.price = int(price)
        self.group = self.__class__.__name__

    try:
        self.price = int(price)
        pass

    except:
        print('Некорректный ввод. Стоимость это число')

    def group_name(self):
        return f'{self.group}'

    def __repr__(self):
        return f'{self.device_name} {self.device_type} {self.work_speed} {self.price}'

class Printer(OfficeEquipment):
    def __init__(self, device_name, device_type, number_of_colors ,work_speed, price):
        OfficeEquipment.__init__(self, device_name, device_type, work_speed, price)
        self.number_of_colors = number_of_colors

    def __str__(self):
        return f'{self.device_name} {self.device_type} {self.number_of_colors}' \
               f'{self.work_speed} {self.price}'



    def action(self):
        return 'Печатает'

class Scanner(OfficeEquipment):
    def __init__(self, device_name, device_type, color_rendering, work_speed, price):
        OfficeEquipment.__init__(self, device_name, device_type, work_speed, price)
        self.color_rendering = color_rendering

    def __str__(self):
        return f'{self.device_name} {self.device_type} {self.color_rendering}' \
               f'{self.work_speed} {self.price}'

    def action(self):
        return 'Сканирует'

class Xerox(OfficeEquipment):
    def __init__(self, device_name, device_type, resource_cylinder, work_speed, price):
        OfficeEquipment.__init__(self, device_name, device_type, work_speed, price)
        self.resource_cylinder = resource_cylinder

    def __str__(self):
        return f'{self.device_name} {self.device_type} {self.resource_cylinder}' \
               f'{self.work_speed} {self.price}'

    def action(self):
        return 'Копирует'


storage = Storage()
printer = Printer("Epson", "струйный", "256 цветов", "30л/м", "ggggg")
storage.add_to(printer)
printer = Printer("HP", "лазерный", "256 цветов", "60л/м", "30000")
storage.add_to(printer)
scanner = Scanner("HP", "планшетный", "256 цветов", "20л/м", "9000")
storage.add_to(scanner)
scanner = Scanner("Samsung", "протяжный", "ч/б", "40л/м", "18000")
storage.add_to(scanner)
xerox = Xerox("Samsung", "цифровой", "60000 копий", "40л/м", "30000")
storage.add_to(xerox)
xerox = Xerox("Xerox", "аналоговый", "40000 копий", "20л/м", "6000")
storage.add_to(xerox)

print(storage._dict)

#storage.extract(printer)
print()
