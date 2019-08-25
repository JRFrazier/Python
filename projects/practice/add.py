class Number:
    def __init__(self, number):
        self.number = number

    def __repr__(self):
        return repr(self.number)

    def __add__(self, other):
        return self + other


one = Number(1)

two = Number(2)

print(one.number)


class Employee():
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name
