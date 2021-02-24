
class Cell:
    def __init__(self, quantity):
        self.quantity = int(quantity)

    def __add__(self, other):
        return self.quantity + other.quantity

    def __sub__(self, other):
        sub = self.quantity - other.quantity
        return sub

    def __mul__(self, other):
        return self.quantity * other.quantity

    def __truediv__(self, other):
        return self.quantity // other.quantity

    def make_order(self, nums):
        return '\n'.join(['*' * self for _ in range(nums // self)]) + '\n' + '*' * (nums % self)
    print(make_order(7, 15))


print(Cell.make_order(5, 12))
print(Cell.make_order(5, 15))
