txt = 'OwO\n'

print(1)
print(txt*10)

print(2)
print(str.join('',[txt for x in range(10)]))

print(3)
i = 0
while i < 10: 
    print(txt, end='')
    i+=1