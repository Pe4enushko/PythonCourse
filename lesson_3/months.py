import re

num_filter = re.compile("[0-9]+")

inp = input("С вас месяц ")

# Если чел буквы введёт, то возьму последнюю цифру в строке
if not inp.isdigit():
    print("Я буквы не просил, ну лан. Попробую взять цифры из этого...")
    filtered = num_filter.findall(inp)
    if len(filtered) > 0:
        inp = filtered[-1]
        print(f"Повезло-повезло. Нашлось число {inp}")
    else:
        print("Чисел не нашёл. Давай в следующий раз")
        exit()
    
match int(inp):
    case 1: print("Январь")
    case 2: print("Февраль")
    case 3: print("Март")
    case 4: print("Апрель") 
    case 5: print("Май")
    case 6: print("Июнь")
    case 7: print("Июль")
    case 8: print("Август")
    case 9: print("Сентябрь")
    case 10: print("Октябрь")
    case 11: print("Ноябрь")
    case 12: print("Декабрь")
    case _: print("Я не знать таких месяцев")
    