def daw(txt, i, words_count):
    if(words_count <= 0):
        return txt
    selected_word = get_selected_word_index(txt, i)
    words = txt.split(' ')
    final_words = words[:selected_word] + words[selected_word + words_count:]
    return str.join(' ', final_words)

def get_selected_word_index(txt, cursor_position):
    txt_before = txt[:cursor_position]
    left_words_count = len(txt_before.split(' '))
    if len(txt) >= cursor_position:
        return left_words_count
    return left_words_count - 1
    
# test
inp = input('Дай мне 3 аргумента через запятую: текст, позицию, кол-во слов ')
args = inp.split(',')
print(daw(args[0], int(args[1].strip(),0), int(args[2].strip(),0)))