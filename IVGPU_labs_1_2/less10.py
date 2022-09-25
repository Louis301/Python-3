import time


def date_difference(my_date, date2=time.strftime("%d-%m-%Y", time.localtime())):
    # Возвращает разницу в секундах между двумя датами формата %d-%m-%Y
    # Если 2-ой параметр не указан, вместо него подставляется текущая дата

    start_time = time.mktime(time.strptime(my_date, "%d-%m-%Y"))
    end_time = time.mktime(time.strptime(date2, "%d-%m-%Y"))

    return abs(end_time - start_time)


# ---------------------------- Точка входа

print(date_difference("03-01-2022", "01-01-2022"))
print(date_difference("01-01-2022", "02-01-2022"))
print(date_difference("16-09-2022"))
