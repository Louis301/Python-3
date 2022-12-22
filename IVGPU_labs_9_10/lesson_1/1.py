# Задача 1.
# Создайте текстовый файл (шаблон), содержащий следующее:
# «Приветствую тебя, {{ user_name }}! Очень рад тебя видеть! С нашей
# последней встречи прошло {{ time }} лет… Прими этот {{ item }} и
# садись {{ place }}»
# Ваша программа во время запуска должна запросить соответствующие
# данные у пользователя через консоль. Затем заполнить данный шаблон этими
# данными и вывести отрендеренный текст в консоль.
# Дополнительно:
# Подготовьте файл ответов в формате json. При наличии этого файла
# программа не будет запрашивать у пользователя данные, а должная считать их
# из этого файла.

from jinja2 import Template
import os.path
import json

# ------------------------------------


def get_file_content(path):
    if os.path.isfile(path):
        with open(path, "r", encoding='utf-8') as txt_infile:
            file_content = txt_infile.read()
    else:
        print("File not exists")

    return file_content


# ------------------------------------

def get_final_msg(json_answers_path, msg_template):

    if os.path.isfile(json_answers_path):
        with open('answers.json', "r", encoding='utf-8') as json_infile:
            answers = json.load(json_infile)
            for answer in answers['data']:
                user_name = answer["Имя"]
                time = answer["Срок"]
                item = answer["Предмет"]
                place = answer["Место"]
    else:
        user_name = input("Имя: ")
        time = input("Срок: ")
        item = input("Предмет: ")
        place = input("Место: ")

    return msg_template.render(u_n=user_name, t=time, i=item, p=place)


# ------------------------------------
if __name__ == "__main__":

    tm = Template(get_file_content('lesson_1/template.txt'))

    print(get_final_msg('answers.json', tm))
