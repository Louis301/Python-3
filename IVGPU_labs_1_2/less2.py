last_name = input("Фамилия: ")
first_name = input("Имя: ")
patronymic = input("Отчество: ")

print("{0} {1}.{2}.".format(
    last_name.title(), first_name[0].upper(), patronymic[0].upper()))
