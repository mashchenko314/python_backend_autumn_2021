class CustomMeta(type):
    """Реализация пользовательского метакласса, который
     в начале названий всех атрибутов и методов (кроме магических) добавляет префикс "custom_".

    :param type: базовый метакласс
    :type type: type
    """

    def __new__(cls, name, bases, dct):
        attrs = dict((name, 'custom_' + name) for name, value in dct.items() if not name.startswith('__') and not name.endswith('__'))
        for key in dct.copy():
            if key in attrs:
                value = dct.pop(key)
                dct[attrs[key]] = value
        return super().__new__(cls, name, bases, dct)
    
    def __call__(cls, *args, **kwargs):
        inst = super().__call__(*args, **kwargs)
        for key in inst.__dict__.copy():
            inst.__dict__['custom_' + key] = inst.__dict__.pop(key)
        return inst


class CustomClass(metaclass=CustomMeta):
    """Класс, использующий в качестве базового созданный нами метакласс CustomMeta.
    """
    x = 50

    def __init__(self, val=99):
        self.val = val

    def line(self):
        return 100
