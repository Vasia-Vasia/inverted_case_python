def invert_case(text):
    result = ''
    for symbol in text:
        if symbol == symbol.lower():
            result = result + symbol.upper()
        else:
            result = result + symbol.lower()
    return result

# Проверка

text = 'Hello, World!'
print(invert_case(text))
