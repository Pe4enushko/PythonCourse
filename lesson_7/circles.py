import math


valtype = input('Вам радиус или диаметр? ')
try:
    val = float(input('Значение в студию '))
except:
    print('Не надо дядя')

match valtype:
    case v if v in ['радиус', 'r']:
        print(f'''Длина окружности: {2*val*math.pi}
Площадь: {math.pi*(val**2)}''')
    case v if v in ['диаметр', 'd']:
        print(f'''Длина окружности: {val*math.pi}
Площадь: {math.pi*((val/2)**2)}''')
    case _: print('Не понял')