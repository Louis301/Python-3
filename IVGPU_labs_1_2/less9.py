import random
import time


def random_date(start_date, end_date):
    # Возвращает случайную дату 2022-го года

    prop = random.random()
    time_format = "%d-%m-%Y"

    stime = time.mktime(time.strptime(start_date, time_format))
    etime = time.mktime(time.strptime(end_date, time_format))

    ptime = stime + prop * (etime - stime)

    return time.strftime(time_format, time.localtime(ptime))


# ---------------------------- Точка входа

print(random_date("01-01-2022", "01-01-2023"))
print(random_date("01-01-2022", "01-01-2023"))
print(random_date("01-01-2022", "01-01-2023"))
