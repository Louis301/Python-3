
def get_text_info(text):
    # Возвращает информацию о строке

    digit_count = 0
    words_count = len(text.split(" "))

    for simbol in text:
        if simbol.isdigit():
            digit_count += 1

    return {'length': len(text), 'words_count': words_count, 'digit_count': digit_count}


# -------------------------- Точка входа

text = input("Введите строку: ")

text_info = get_text_info(text)

for key in text_info.keys():
    print(key, "=>", text_info[key])
