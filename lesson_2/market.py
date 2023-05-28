discounts = {100: 0.05, 500: 0.1, 1000: 0.15, 5000: 0.2}

init_price = int(input("Шекели: "))

discount = 0

for x, y in discounts.items():
    discount = float(y) if init_price >= int(x) else discount

print(init_price - init_price * discount)
print("Скидка: " + str(discount * 100) + "%")