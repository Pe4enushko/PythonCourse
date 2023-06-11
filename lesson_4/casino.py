import random
guess = 0
randnum = random.randint(0,100)
while guess != randnum:
    try:
        guess = int(input("Угадаешь? Уверен, что нет. "), 0)
    except:
        print("Дурак?")
else:
    print("Ле....")