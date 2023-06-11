import functools
while True:
    try:
        num = int(input("Ну тип число "),0)
        break
    except:
        num = int(input("Я сказал, число "),0)
        break

print("Факториал:", functools.reduce(lambda a,b: a*b, range(1,num+1)))