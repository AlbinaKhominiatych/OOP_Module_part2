# перевантаження методів
class StringManipulator:
    def concatenate(self, a, b):
        return a + b

    def concatenate(self, a, b):
        return str(a) + str(b)


calc = StringManipulator()
print(calc.concatenate(2, 3))
print(calc.concatenate("2", "3"))
