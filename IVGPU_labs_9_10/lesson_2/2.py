# Задача 2.
# Программа должна запросить у пользователя следующую информацию:
# 1) имена двух персонажей;
# 2) вид соревнования;
# 3) характеристики персонажей в данном виде деятельности.
# Подготовьте шаблон, в который при рендеринге передастся полученная
# информация. В результате рендеринга должен быть получен текст,
# содержащий имя победителя (побеждает тот, чьи характеристики больше).
# При равенстве вывести соответствующею информацию Сравнение
# характеристик должно происходить в блоке if шаблонизатора.
# Дополнительно:
# Вывод на экран должен быть в формате json или csv. Оба формата
# должны содержать следующие поля:
# 1) имя победителя
# 2) его характеристики
# 3) вид соревнования
# 4) дата проведения соревнования
# Имена полей произвольные.

import os.path
from jinja2 import Template
import csv


class Character:
    def __init__(self, name, competition_type, characteristic, competition_data):
        self.name = name
        self.competition_type = competition_type
        self.characteristic = characteristic
        self.competition_data = competition_data


# ------------------------------------


def get_file_content(path):
    if os.path.isfile(path):
        with open(path, "r", encoding='utf-8') as txt_infile:
            file_content = ''.join(txt_infile.read().splitlines())
    else:
        print("File not exists")

    return file_content


# ------------------------------------

def set_csv_data(characters, path):
    with open(path, mode="w", encoding='utf-8') as csv_outfile:
        file_writer = csv.writer(
            csv_outfile, delimiter=";", lineterminator="\r")

        file_writer.writerow(
            ["Имя победителя", "Вид соревнования", "Дата соревнования", "Характеристика"])

        for char in characters:
            file_writer.writerow(
                [char.name, char.competition_type, char.competition_data, char.characteristic])
    pass


# ------------------------------------
if __name__ == "__main__":

    char_1 = Character("Алексей", "волейбол", 7, '24.10.2022')
    char_2 = Character("Михаил", "волейбол", 10, '24.10.2022')

    # char_1 = Character(
    #   input("Имя: "),
    #   input("Вид соревнования: "),
    #   int(input("Характеристика: ")),
    #   input("Дата соревнования: ")
    # )

    # char_2 = Character(
    #   input("Имя: "),
    #   input("Вид соревнования: "),
    #   int(input("Характеристика: ")),
    #   input("Дата соревнования: ")
    # )

    characters = [char_1, char_2]

    # ============================================================
    msg_template = Template(get_file_content('lesson_2/template.txt'))

    print(msg_template.render(
        c_t=char_1.competition_type, char_1=char_1, char_2=char_2))

    # ============================================================
    print("-----------------------------------")
    set_csv_data(characters, 'lesson_2/characters.csv')

    with open('lesson_2/characters.csv', 'r', encoding="utf-8") as csv_inline:
        print(csv_inline.read())
