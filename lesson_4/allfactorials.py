import functools
    
factorials = []

def save_factorial(num):
    return functools.reduce(lambda a,b: a*b, range(1,num+1))

# Мой оверинжинеринг, чтобы узнать максимальное нужное число для факториала, чтобы не спамить потом
maxnum = 1
calibration = 1000
while calibration > 1:
    calibration /= maxnum
    maxnum += 1

# Заполняемся факториалами 
a = list(map(save_factorial ,range(1, maxnum)))

for f in a:
    if f <= 1000:
        st = ''
        for x in range(1, a.index(f) + 2):
            st += f'{x}*'
        print(f"{f} = {st[:-1]}")
