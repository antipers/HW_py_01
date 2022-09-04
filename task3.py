# Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0
# и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).

# Пример:

# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

point_x = int(input("Введите координату точки Х--> "))
point_y = int(input("Введите координату точки Y--> "))

if (point_x > 0 and point_y > 0):
    print("Это плоскость 1")
elif (point_x < 0 and point_y > 0):
    print("Это плоскость 2")
elif (point_x < 0 and point_y < 0):
    print("Это плоскость 3")
elif (point_x > 0 and point_y < 0):
    print("Это плоскость 4")
elif (point_x == 0) and (point_y == 0):
    print("Введите другие значения")
elif (point_x == 0) and (point_y != 0):
    print("Точка находится на оси Y")
elif (point_x != 0) and (point_y == 0):
    print("Точка находится на оси X")
