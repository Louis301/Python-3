class Triangle():

    def __init__(self, a, b, c):
        self.__a = a
        self.__b = b
        self.__c = c
        pass

    def reset_a(self, a):
        if a < self.__b + self.__c:
            self.__a = a
        pass

    def reset_b(self, b):
        if b < self.__a + self.__c:
            self.__b = b
        pass

    def reset_c(self, c):
        if c < self.__a + self.__b:
            self.__c = c
        pass

    def get_perimetr(self):
        print("Perimetr =", self.__a + self.__b + self.__c)
        pass


class NewTriangle():
    protected_attrs = ("a", "b", "c", "protected_attrs")

    def __init__(self, a, b, c):
        self.reset_a(a)
        self.reset_b(b)
        self.reset_c(c)
        pass

    def reset_a(self, a):
        if a and isinstance(a, int):
            super().__setattr__("a", a)
        else:
            raise ValueError("Пустой аргумент А")

    def reset_b(self, b):
        if b and isinstance(b, int):
            super().__setattr__("b", b)
        else:
            raise ValueError("Пустой аргумент B")

    def reset_c(self, c):
        if c and isinstance(c, int):
            super().__setattr__("c", c)
        else:
            raise ValueError("Пустой аргумент C")

    def __setattr__(self, key, value):
        if key in self.protected_attrs:
            raise AttributeError(f"Нельзя установить данный атрибут {key}")
        super().__setattr__(key, value)


class Point():
    x: int


if __name__ == "__main__":

    ins = Point()
    print(ins.y)

    shape = NewTriangle(2, 12, 8)

    print(shape.a)  # Вывод: 2
    # shape.a = 10   # error: "Нельзя установить данный атрибут а"

    shape.reset_a(10)  # Атрибут а успешно изменён на 10
    print(shape.a)  # Вывод: 10
