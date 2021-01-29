class OnlyNumberError:
    def __init__(self, *args):
        self.my_list = []

    def my_input(self):

        while True:
            try:
                a = int(input('Введите значения и нажмите Enter - '))
                self.my_list.append(a)
                print(f'Итоговый список - {self.my_list} \n ')
            except:
                print(f"Недопустимое значение. Введите число")
                choice = input(f'Продолжим ввод - "Y" или выход - "STOP"')

                if choice == 'Y' or choice == 'y':
                    print(try_except.my_input())
                elif choice == 'STOP' or choice == 'stop':
                    return f'Вы закончили ввод. Итоговый список {self.my_list}'
                else:
                    return f'Вы вышли'


try_except = OnlyNumberError(1)
print(try_except.my_input())
