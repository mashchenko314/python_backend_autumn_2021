class CustomMeta(type):
    """Реализация пользовательского метакласса, который
     в начале названий всех атрибутов и методов (кроме магических) добавляет префикс "custom_".

    :param type: базовый метакласс
    :type type: type
    """

    def __new__(cls, name, bases, dct):
        attrs = dict((name, 'custom_'+name)
        for name, value in dct.items() if not name.startswith('__'))
        for key in dct.copy():
            if key in attrs:
                value = dct.pop(key)
                dct[attrs[key]] = value
        return type.__new__(cls, name, bases, dct)



class CustomClass(metaclass=CustomMeta):
    """Класс, использующий в качестве базового созданный нами метакласс CustomMeta.
    """
    x = 50

    def __init__(self, val=99):
        self.val = val

    def line(self):
        return 100
