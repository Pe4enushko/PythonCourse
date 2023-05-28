from datetime import date


raw_date = input("Давай сюда свою дату рождения в формате dd/mm/yyyy \n")

date_parts = raw_date.split('/')

try:
    birth_day = date(
        int(date_parts[2]),
        int(date_parts[1]),
        int(date_parts[0]))
except ValueError as e:
    print(e.args[0])
    exit()
    
if birth_day.year > date.today().year:
    print("В следующий раз придёшь - принеси мне сувенир из этого своего будущего")
    exit()

age = date.today().year - birth_day.year

if age > 150:
    confirm = input(
        f"Я конечно всё понимаю, " +
        f"но тебе точно {age} лет? Да/Нет \n")
    if not confirm == "Да":
        print("В следующий раз аккуратнее по клаве стучи")
        exit()
print(
    "Ладно, бери фулл. 18 тебе есть"
    if age >= 18
    else f"Какой фулл? тебе {age}")