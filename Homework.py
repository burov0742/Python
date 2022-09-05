# Task #1
#  Напишите программу, которая принимает на вход цифру, 
# обозначающую день недели, и проверяет, является ли этот день выходным.
# Пример:
# - 6 -> да
# - 7 -> да
# - 1 -> нет

# a = int (input ('Input number day of the week: '))

# if 6 <= a <= 7:
#     print('This is the weekend')
# else:
#     print('This is not the weekend')

# Task #2
# Напишите программу для. проверки истинности утверждения 
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.


# Task #3
# Напишите программу, которая принимает на вход координаты точки (X и Y), 
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).
# Пример:
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

# x = int (input('Input x coordinate: '))
# y = int (input('Input y coordinate: '))

# if x == 0 and y == 0:
#     print ('Center')
    
# else:
#     if x == 0:
#         print ('Point on X line')
#     elif y == 0:
#         print ('Point on Y line')
#     elif x > 0 and y > 0:
#         print ('Firth quarter')
#     elif x < 0 and y > 0:
#         print('Second quarter')
#     elif x < 0 and y < 0:
#         print ('Third quarter')
#     elif x > 0 and y <0:
#         print ('Fourth quarter')


# Task #4
# Напишите программу, которая по заданному номеру четверти, 
# показывает диапазон возможных координат точек в этой четверти (x и y)

# a = int (input ('Input number of quarter (1-4): '))

# if 1 <= a <= 4:

#     if a == 1:
#         print('X > 0 and Y > 0')
#     elif a == 2:
#         print ('X < 0 and Y > 0')
#     elif a == 3:
#         print ('X <0 and Y < 0')
#     elif a == 4:
#         print ('X > 0 and Y < 0')
# else:
#     print ('Please input correct number of quarter')


# Task #5
# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21


