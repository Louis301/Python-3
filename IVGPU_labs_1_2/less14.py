
import random


def get_upper(string_list):
    return str(string_list[random.randint(0, len(string_list)-1)]).upper()

# ---------------------- Точка входа


my_strings = [
    "First",
    "Second",
    "Big Foot",
    "Das boot",
    "Smoll string",
]

print(get_upper(my_strings))
print(get_upper(my_strings))
print(get_upper(my_strings))
print(get_upper(my_strings))
print(get_upper(my_strings))
