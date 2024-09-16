# module_1_6.py
my_dict = {"Luda": 1985, "Nata": 1992, "Roma": 1980}  # создания списка ключ-значение
print("Dict:", my_dict)# вывод словаря  на экран
print("Existing value:", my_dict["Luda"])# вывод одного значения по ключу
print("Not existing value:", my_dict.get("Kirill")) # вывод отсутствующего ключа
my_dict.update({"lily": 1976, "Sasha": 1985}) # добавление нового списка
print("Deleted value:", my_dict["Nata"]) # удаление элемента
del(my_dict["Nata"])
print("Modified dictionary:", my_dict) # вывод словаря  на экран
#
my_set = {1, 2, 3, 4.5, "кoмпот", True, (1, 1, 1), 2, 4.5,} # создание множества
print("Set:", my_set) # вывод множества на экран
my_set.add(9) # добавление одно элемента множества
my_set.add(8.6) # добавление 2-го элемента множества
my_set.remove(4.5) # удаление элементаиз множества
print("Modified set:", my_set) # вывод на экран



