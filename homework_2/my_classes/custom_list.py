from itertools import zip_longest

class CustomList(list):
    """Реализация пользовательского списка.
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __add__(self, other):
        buffer = []
        try:
            for i,j in zip_longest(self, other, fillvalue=0):
                buffer.append(i+j)
        except TypeError:
            print('Невозможно выполнить сложение из-за различия типов слагаемых.')
            return None
        else:
            return CustomList(buffer)

    def __radd__(self, other):
        buffer = []
        try:
            for i, j in zip_longest(other, self, fillvalue=0):
                buffer.append(i + j)
        except TypeError:
            print('Невозможно выполнить сложение из-за различия типов слагаемых.')
            return None
        else:
            return CustomList(buffer)

    def __sub__(self, other):
        buffer = []
        for i,j in zip_longest(self, other, fillvalue=0):
            buffer.append(i-j)
        return CustomList(buffer)

    def __rsub__(self, other):
        buffer = []
        for i,j in zip_longest(other, self, fillvalue=0):
            buffer.append(i-j)
        return CustomList(buffer)

    def  __lt__(self, other): # x < y
        return sum(self) < sum(other)

    def __le__(self, other): # x ≤ y
        return sum(self) <= sum(other)

    def __eq__(self, other): #x == y
        return sum(self) == sum(other)

    def __ne__(self, other): #x != y
        return sum(self) != sum(other)

    def __gt__(self, other): # x > y
        return sum(self) > sum(other)

    def __ge__(self, other): # x ≥ y
        return sum(self) >= sum(other)
