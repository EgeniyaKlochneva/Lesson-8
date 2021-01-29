class ComplexNumber:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        return f'Сумма комплексных чисел равна: {self.a + other.a} + {self.b + other.b} * i'

    def __mul__(self, other):
        return f'Произведение комплексных чисел равно: {self.a * other.a - (self.b * other.b)} + {self.b * other.a} * i'


c_1 = ComplexNumber(2, 1)
c_2 = ComplexNumber(3, 5)
print(c_1 + c_2)
print(c_1 * c_2)
