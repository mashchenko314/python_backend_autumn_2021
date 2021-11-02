from my_classes.custom_list import CustomList
from my_classes.custom_meta import CustomClass


if __name__ == '__main__':
    a = [1,5,3,7]
    b = CustomList([3,6,7])
    c = CustomList([10, 5, 8, 9, 3])
    print(sum(b))
    print('a = ', type(a), a)
    print('b = ', type(b), b)
    print('c = ', type(c), c)
    print(f'{a} - {b} =', a-b)
    print(f'{a} + {b} =', a+b)
    print(f'{c} + {b} =', c+b)
    print(f'{c} - {b} =', c-b)
    print(f'{b} - {a} =', b-a)
    print(f'{c} == {b}: ', c==b)
    print(f'{c} > {b}: ', c>b)
    print(f'{c} < {b}: ', c<b)


    inst = CustomClass()
    inst.custom_val 
    inst.custom_x
    inst.custom_line()
    
    inst.val #ошибка
    inst.x  # ошибка
    inst.line() # ошибка


    

