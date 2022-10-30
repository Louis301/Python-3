
class Human():
    def __init__(self, surname, name, second_name, age=0, sex="М"):
        self.surname = surname.title()
        self.name = name.title()
        self.second_name = second_name.title()
        self.age = age
        self.sex = sex
        pass

    def get_fio(self):
        print(self.surname + " " +
              self.name[0] + ". " +
              self.second_name[0] + ".")
        pass

    def get_full_info(self):
        print(f"Фамилия: {self.surname}")
        print(f"Имя: {self.name}")
        print(f"Отчество: {self.second_name}")
        print(f"Возраст: {self.age}")
        print(f"Пол: {self.sex}")
        pass


class Student(Human):
    def __init__(self, surname, name, second_name, age=0, sex="М", group=""):
        super().__init__(surname, name, second_name, age, sex)
        self.group = group
        pass

    # use mode "return" to get the string
    def get_full_info(self, mode="print"):
        if mode == "print":
            sep = "\n"
        elif mode == "return":
            sep = ", "

        info = f"Фамилия: {self.surname}" + sep + f"Имя: {self.name}" + sep + f"Отчество: {self.second_name}" + \
            sep + f"Возраст: {self.age}" + sep + \
            f"Пол: {self.sex}" + sep + f"Группа: {self.group}"

        if mode == "print":
            print(info)
        elif mode == "return":
            return info


if __name__ == "__main__":
    #dude = Human("Орлик", "Юрий", "владиславович", 20)
    # dude.get_fio()
    # dude.get_full_info()

    man = Student("kkkkkk", "aaaa", "uuuuuuuuu", 18, "m", "AD-12")
    man.get_full_info("print")
    # print(man.get_full_info("return"))
