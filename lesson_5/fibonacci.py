import sys
def safe_int_input(text = ""):
    while True:
        try:
            return int(input(text),0)
        except:
            print("Неее, мне число надо")

def get_next_fibonacci(nums = []):
    '''Generates numbers using a nums list. To reset counting - enter a blank list as argument'''
    # min 2 numbers first two are always 0 and 1
    if len(nums) < 1:
        nums.append(0)
        return 0
    elif len(nums) < 2:
        nums.append(1)
        return 1
    res = sum(nums[-2:])
    nums.append(res)
    return res
    
def generate_fibonacci(count):
    result = [] 
    for i in range(count):
        result.append(get_next_fibonacci())
    return result


try:
    if len(sys.argv) == 2:
        try:
            count = int(sys.argv[1],0)
        except:
            print("Нам такого не надо. Давай ещё раз")
    
    if not 'count' in locals():
        count = safe_int_input("Сколько чисел Фиббоначи хотим? ")
    if count > 600:
        confirm = input("\nА может не надо так много? Гляди то и дело питон вылетит O /\\ O \nПовторно введи число, если точно не хочешь менять ").lower()
        if confirm != str(count):
            count = safe_int_input("Вот теперь точно назови число. Второй раз останавливать не буду ")
            
    nums = generate_fibonacci(count)
    
    print(f'Числа: {nums}')
    print(f"Сумма: {sum(nums)}")
except KeyboardInterrupt:
    print("Ну лан, в следующий раз")
    exit()