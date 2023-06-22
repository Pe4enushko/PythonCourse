import re

def filter_numstrings(strs):
    toremove = []
    for s in strs:
        if not re.match(r'[1-9]+\.[0-9]*$',s) and not str.isdigit(s) or ' ' in s:
            toremove.append(s)
            print(f'Weird input: {s}. It was removed')
    for x in toremove:
        strs.remove(x)
        
    return strs
try:
    inp = input('Введи числа через пробел (если float - разделитель ".")\n')
except KeyboardInterrupt:
    print('Ну лан')
    
finp = filter_numstrings(str.split(inp.strip(), ' '))
nums = list(map(lambda x: float(x) if '.' in x else int(x, 0),finp))

finalnums = (sorted([x for x in filter(lambda a: a % 2 == 0, nums)])
             + sorted([x for x in filter(lambda a: a % 2 != 0, nums)]))

print(str.join(', ', list(map(str,finalnums))))