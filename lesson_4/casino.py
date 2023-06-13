import random
guess = 0
randnum = random.randint(0,100)
interrupted = False

while guess != randnum:
    try:
        # Не повторять же постоянно больше или меньше
        if not interrupted:
            print(f"Чуть {'меньше' if guess > randnum else 'больше'}")
        else:
            interrupted = False
            
        guess = int(input("Угадаешь? Уверен, что нет. "), 0)

    except KeyboardInterrupt as e:
        answer = input("А ты точно ливнуть хочешь? QwQ ").lower()
        interrupted = True
        
        if answer == "да":
            exit()
        else:
            print("Тогда продолжим AwA")
    except:
        print("Дурак?")
else:
    print("Что-ж, победа.")