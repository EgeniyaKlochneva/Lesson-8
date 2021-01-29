class Data:
    def __init__(self, d_m_y):
        self.d_m_y = str(d_m_y)

    @classmethod
    def method_1(cls, d_m_y):
        new_date = []

        for i in d_m_y.split('-'):
            if i != '-':
                new_date.append(i)

        return int(new_date[0]), int(new_date[1]), int(new_date[2])

    @staticmethod
    def method_2(day, month, year):

        if 1 <= day <= 31:
            if 1 <= month <= 12:
                if 2021 >= year >= 0:
                    return f'Дата введена верно'
                else:
                    return f'Некорректно введен год'
            else:
                return f'Некорректно введен месяц'
        else:
            return f'Некорректно введен день'

    def __str__(self):
        return f'Текущая дата {Data.method_1(self.d_m_y)}'


d = Data('28-1-2021')
print(d)
print(Data.method_2(28, 1, 2023))
print(d.method_2(28, 28, 2020))
print(Data.method_2(28, 1, 2021))
print(Data.method_1('28-01-2021'))
print(d.method_1('28-01-2021'))
