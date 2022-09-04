# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

# Пример:

# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

from math import sqrt


point_x_a = float(input("Введите точку Xa--> "))
point_y_a = float(input("Введите точку Ya--> "))
point_x_b = float(input("Введите точку Xb--> "))
point_y_b = float(input("Введите точку Yb--> "))

distance = sqrt(((point_x_b - point_x_a)**2) + ((point_y_b - point_y_a)**2))
print(round(distance,2))