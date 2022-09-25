
print("Сколько будет 2 * 2?")
print("Выберите вариант ответа:")

print("  1. Восемь")
print("  2. Четыре")
print("  3. Не скажу")
print("  4. Тринадцать")
print("  5. Три")

answer = int(input("Номер ответа = "))

if answer == 2:
    print("\033[32m{0}".format("Правильно"))
else:
    print("\033[31m{0}\033[37m".format("Не правильно"))

    # question_answer = {
    #     "Сколько будет 2 * 2: ": "4",
    #     "Столица Франции: ": "Париж",
    #     "Первый президент США: ": "Джордж Вашингтон",
    #     "Трёхногий клавишный инструмент: ": "рояль",
    #     "Вольфганг ... Моцарт. Заполните пропуск: ": "Амадей"
    # }

    # my_answers = []

    # for question in question_answer.keys():
    #     my_answers.append(input(question).lower().strip())

    # print("----------------------")

    # i = 0

    # for answer in question_answer.values():
    #     if my_answers[i] in answer.lower().strip():
    #         print("Вопрос {0} - \033[32m{1}\033[37m".format(i + 1, "ОК"))
    #     else:
    #         print(
    #             "Вопрос {0} - \033[31m{1}\033[37m".format(i + 1, "Неправильно"), end="")
    #         print(" => Ответ:", answer)
    #     i += 1

    # print("----------------------")
