def info(num):
    ids = {0: 'Continue',
    1: 'Switching Protocols',
    2: 'Processing',
    3: 'Early Hints'}
    return ids[num]

def success(num):
    codes = {0: 'OK',
   1: 'Created',
   2: 'Accepted',
   3: 'Non-Authoritative Information',
   4: 'No Content',
   5: 'Reset Content',
   6: 'Partial Content',
   7: 'Multi-Status',
   8: 'Already Reported',
   6: 'IM Used'}
    return codes[num]

def redirect(num):
    codes = {0: 'Multiple Choices',
   1: 'Moved Permanently',
   2: 'Moved Temporarily',
   3: 'See Other',
   4: 'Not Modified',
   5: 'Use Proxy',
   6: 'Reserved',
   7: 'Temporary Redirect',
   8: 'Permanent Redirect'}
    return codes[num]

def client_err(num):
    codes = {0: 'Bad Request',
   1: 'Unauthorized',
   2: 'Payment Required',
   3: 'Forbidden',
   4: 'Not Found',
   5: 'Method Not Allowed',
   6: 'Not Acceptable',
   7: 'Proxy Authentication Required',
   8: 'Request Timeout',
   9: 'Conflict',
   10: 'Gone',
   11: 'Length Required',
   12: 'Precondition Failed',
   13: 'Payload Too Large',
   14: 'URI Too Long',
   15: 'Unsupported Media Type',
   16: 'Range Not Satisfiable',
   17: 'Expectation Failed',
   18: "I'm a teapot",
   19: 'Authentication Timeout',
   21: 'Misdirected Request',
   22: 'Unprocessable Entity',
   23: 'Locked',
   24: 'Failed Dependency',
   25: 'Too Early',
   26: 'Upgrade Required',
   28: 'Precondition Required',
   29: 'Too Many Requests',
   31: 'Request Header Fields Too Large',
   49: 'Retry With',
   51: 'Unavailable For Legal Reasons',
   99: 'Client Closed Request'}
    return codes[num]

def server_err(num):
    codes = {0: 'Internal Server Error',
   1: 'Not Implemented',
   2: 'Bad Gateway',
   3: 'Service Unavailable',
   4: 'Gateway Timeout',
   5: 'HTTP Version Not Supported',
   6: 'Variant Also Negotiates',
   7: 'Insufficient Storage',
   8: 'Loop Detected',
   9: 'Bandwidth Limit Exceeded',
   10: 'Not Extended',
   11: 'Network Authentication Required',
   20: 'Unknown Error',
   21: 'Web Server Is Down',
   22: 'Connection Timed Out',
   23: 'Origin Is Unreachable',
   24: 'A Timeout Occurred',
   25: 'SSL Handshake Failed',
   26: 'Invalid SSL Certificate'}
    return codes[num]

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
    case 1:
        print(f"Инфа: {info(tail)}" if tail in possible1 else errmsg)
    case 2:
        print(f"Успешный успех: {success(tail)}" if tail in possible2 else errmsg)
    case 3:
        print(f"Редирект: {redirect(tail)}" if tail in possible3 else errmsg)
    case 4:
        print(f"Ошибка на стороне клиента: {client_err(tail)}" if tail in possible4 else errmsg)
    case 5:
        print(f"Ошибка на стороне сервера: {server_err(tail)}" if tail in possible5 else errmsg)
