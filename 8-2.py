class ZeroError(Exception):
    def __init__(self, b):
        self.b = b


def func():
    try:
        a = int(input("Введите а: "))
        b = int(input("Введите b: "))
        if int(b) == 0:
            raise ZeroError("Error")
        else:
            y = a / b
            return y

    except ValueError:
        return 'Вы ввели не число'

    except ZeroError:
        print("На ноль делить нельзя")


print(func())
