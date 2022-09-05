#Напишите программу, которая принимает на вход два числа и проверяет, 
# является ли одно число квадратом другого.

#*Примеры:* 

#- 5, 25 -> да
# 4, 16 -> да
#- 25, 5 -> да
#- 8,9 -> нет


#a = int (input("Input first number: "))
#b = int (input ('Input seconf number: '))


#if a**2 == b or b**2 == a:
#    print ('True')
#else:
#    print ('False') 


#2. Напишите программу, которая на вход принимает 5 чисел и находит 
# максимальное из них.

#Примеры:

#- 1, 4, 8, 7, 5 -> 8
#- 78, 55, 36, 90, 2 -> 90

# num1 = int (input("Input first number: "))
# num2 = int (input("Input second number: "))
# num3 = int (input("Input third number: "))
# num4 = int (input("Input forth number: "))
# num5 = int (input("Input fivth number: "))

# list = [num1, num2, num3, num4, num5]
# max = list[0]
# for i in range (len(list)):
#     if list[i] > max:
#         max = list[i]
# print (max)

# list = [int (i) for i in  input().split()]
# max = list[0]
# for i in range (len(list)):
#     if list[i] > max:
#         max = list[i]
# print (max)

# Напишите программу, которая будет на вход принимать число N и выводить числа от -N до N

# *Примеры:* 

# - 5 -> -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5

# n = int (input ('Input number: '))
# for i in range(-n, n +1):
#     print (i, end=', ') #sep - при выводе переходит на следующую строку. 
#                           end=', ' - будет выводить все результаты цикла в строку через запятую и пробул


# 2. Напишите программу, которая будет принимать на вход дробь и показывать первую цифру дробной части числа.

# *Примеры:*

# - 6,78 -> 7
# - 5 -> нет
# - 0,34 -> 3



# num = float( input('Input float number '))
# num2 = num * 10
# num2 %=10
# if num2 == 0:
#     print ('false')
# else:
#     print (int (num2))