code = input("Кидаю запрос... (код дайте в ответе)")

# Ага, реюз кода из задания про месяцы месяцев uwu
if not code.isdigit():
    print("Я буквы не просил, ну лан. Попробую взять цифры из этого...")
    filtered = num_filter.findall(inp)
    if len(filtered) > 0:
        inp = filtered[-1]
        print(f"Повезло-повезло. Нашлось число {inp}")
    else:
        print("Чисел не нашёл. Давай в следующий раз")
        exit()

possible1 = list(range(0, 4))
possible2 = list(range(0, 9)) + [26]
possible3 = list(range(0, 9))
possible4 = list(range(0, 30)) + [31, 49, 51, 99]
possible5 = list(range(0, 27))

errmsg = "Такого кода не знаю, сорян"
tail = int(code[1:])
match int(code[0]):
    case 1: print("Информативно" if tail in possible1 else errmsg)
    case 2: print("Успешный успех" if tail in possible2 else errmsg)
    case 3: print("Редирект" if tail in possible3 else errmsg)
    case 4: print("Ошибка на стороне клиента" if tail in possible4 else errmsg)
    case 5: print("Ошибка на стороне сервера" if tail in possible5 else errmsg)