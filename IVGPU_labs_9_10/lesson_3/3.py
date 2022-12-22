# В прошлой работе Вы получили список городов в формате json или csv.
# Необходимо сделать шаблон в формате html. Шаблон необходимо заполнить
# данными из Ваших файлов и сохранить как result.html.
# «добавление стилей в самом html документе или подключение файла css
# для более приятного отображения – приветствуется»
# Дополнительно:
# Ваша программа должна перед рендерингом запросить наименьшее
# количество население города для помещения его в шаблон. То есть города, чье
# население ниже установленной планки не должны присутствовать в
# result.html. Фильтрация должна быть в заложена в шаблон.


from jinja2 import Template
import json
import os.path


class City:
    def __init__(self, index, region_type, region, name, population):
        self.name = name

        try:
            self.population = int(population)
        except ValueError:
            self.population = 0

        self.region = region
        self.index = int(index)
        self.region_type = region_type

    def print(self):
        print("name", self.name)
        print("population", self.population)
        print("region", self.region)
        print("index", self.index)
        print("region_type", self.region_type)
        pass

# ------------------------------------


def get_json_content(path):
    cities_list = list()
    with open(path, "r", encoding='utf-8') as json_infile:
        cities = json.load(json_infile)
        for city in cities['data']:
            cities_list.append(City(
                city["Индекс"], city["Тип региона"], city["Регион"], city["Город"], city["Население"]))
    return cities_list

# ------------------------------------


def get_txt_content(path):
    if os.path.isfile(path):
        with open(path, "r", encoding='utf-8') as txt_infile:
            txt_content = ''.join(txt_infile.read().splitlines())
    else:
        print("File not exists")

    return txt_content


def set_html_content(path, content):
    with open(path, "w", encoding='utf-8') as html_file:
        html_file.write(content)
    pass


# ------------------------------------
if __name__ == "__main__":

    # 1. получаем список городов в формате json
    cities_list = get_json_content("lesson_3/Cities.json")

    # 2. Считываем шаблон
    msg_template = Template(get_txt_content("lesson_3/template.txt"))

    # 3. Запрашиваем наименьшее население (фильтрация должна быть в шаблоне)
    smallest_population = int(input("Предел населения: "))

    # 4. Рендерим шаблон
    html_text = msg_template.render(
        cities=cities_list, s_p=smallest_population)

    # 5. Генерируем веб-страницу
    set_html_content("lesson_3/index.html", html_text)
