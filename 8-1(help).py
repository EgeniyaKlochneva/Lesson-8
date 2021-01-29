import datetime
from time import strptime #Евгений, так и не смогла разобраться с таким вариантом задания. 
#Хотела как то через модуль datetime. Подскажите пожалуйста, что не так я сделала.

class Data:
    def __init__(self, d_m_y):

        self.d_m_y = str(d_m_y)

    @classmethod
    def method_1(cls, d_m_y):
        my_date = []

        for i in d_m_y.split('-'):
            if i != '-':
                my_date.append(i)

        return int(my_date[0]), int(my_date[1]), int(my_date[2])


    @staticmethod
    def method_2(day, month, year):
        correctDate = None
        try:
            newDate = datetime.datetime(day, month, year)
            correctDate = print('Дата введена верно')
        except ValueError:
            correctDate = print('Дата введена некорректно')
        print(str(correctDate))

    def __str__(self):
        return f'{Data.method_1(self.d_m_y)}'


today = Data('29-2-2020')
print(today)
print(Data.method_2(31, 2, 2021))

