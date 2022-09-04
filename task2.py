# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

x = int(input("Введите первое число--> "))
y = int(input("Введите второе число--> "))
z = int(input("Введите третье число--> "))
left_statement = not (x or  y or  z) 
right_statement = (not x) and (not y) and (not z)
answer = left_statement == right_statement
if answer == True:
    print ("True")
else:
    print ("False")        