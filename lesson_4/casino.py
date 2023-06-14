import random
guess = 0
randnum = random.randint(0,100)
firstRound = True

while guess != randnum:
    try:
        if not firstRound:
            print(f"Чуть {'меньше' if guess > randnum else 'больше'}")
        guess = int(input("Угадаешь? Уверен, что нет. "), 0)
        firstRound = False
    except KeyboardInterrupt as e:
        answer = input("А ты точно ливнуть хочешь? QwQ ").lower()
       
        if answer == "да":
            exit()
        else:
            print("Тогда продолжим AwA")
    except:
        print("Дурак?")
else:
    print("Что-ж, победа.")