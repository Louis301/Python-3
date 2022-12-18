# Задача 2.

# Даны два файла (в Moodle) формата csv и json, содержащие разные
# списки городов, их население, регион и индекс. Данные из файлов необходимо
# соединить таким образом, чтобы они содержали только уникальные значения.
# Для этого создайте класс City, у которого будут реализованы методы __hash__
# и __er__. Поместите экземпляры класса в коллекцию, при правильно
# реализованных вышеуказанных методов коллекция будет содержать только
# уникальные города.
# Новый список городов необходимо сохранить в форматы CSV и JSON.
# Используйте собственные функции преобразований.

# Дополнительно:
# Перед сохранением данных в файл отсортируйте список по численности
# населения.


import json
import csv


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

    def __eq__(self, other):
        return self.index == other.index

    def __hash__(self):
        return self.index

    def print(self):
        print("name", self.name)
        print("population", self.population)
        print("region", self.region)
        print("index", self.index)
        print("region_type", self.region_type)
        pass

# -----------------------------------------------------------------


def get_files_data():
    cities_set = set()

    with open('Города.json', "r", encoding='utf-8') as json_infile:
        cities = json.load(json_infile)
        for city in cities['data']:
            cities_set.add(City(
                city["Индекс"], city["Тип региона"], city["Регион"], city["Город"], city["Население"]))
    json_infile.close()

    with open("Города.csv", encoding='utf-8') as csv_infile:
        file_reader = csv.reader(csv_infile, delimiter=",")
        count = 0
        for row in file_reader:
            if count > 0:
                cities_set.add(
                    City(row[0], row[1], row[2], row[3], row[4]))
            count += 1
    csv_infile.close()

    return frozenset(cities_set)

# -----------------------------------------------------------------


def sort_key(s):
    return s.population


# -----------------------------------------------------------------

def set_json_data(cities_list_sorted):
    data = {}
    data['cities'] = []

    for city in cities_list_sorted:
        data['cities'].append({
            "Индекс": city.index,
            "Тип региона":  city.region_type,
            "Регион": city.region,
            "Город": city.name,
            "Население": city.population,
        })

    with open('Cities.json', 'w', encoding='utf-8') as json_outfile:
        json_outfile.write(json.dumps(data, ensure_ascii=False))
    json_outfile.close()
    pass

# -----------------------------------------------------------------


def set_csv_data(cities_list_sorted):
    with open("Cities.csv", mode="w", encoding='utf-8') as csv_outfile:
        file_writer = csv.writer(
            csv_outfile, delimiter=",", lineterminator="\r")

        file_writer.writerow(
            ["Индекс", "Тип региона", "Регион", "Город", "Население"])

        for city in cities_list_sorted:
            file_writer.writerow(
                [city.index, city.region_type, city.region, city.name, city.population])
    csv_outfile.close()
    pass


# -----------------------------------------------------------------
if __name__ == "__main__":

    # Объединяем списки городов из json и csv в одну коллекцию
    cities_frosenset = get_files_data()

    # Cортирует список по `population` в естественном порядке
    cities_list_sorted = sorted(cities_frosenset, key=sort_key)

    # Создаёт файл json с отсортированным списком городов
    set_json_data(cities_list_sorted)

    # Создаёт файл csv с отсортированным списком городов
    set_csv_data(cities_list_sorted)
