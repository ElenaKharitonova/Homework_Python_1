# Задача 4. Напишите программу, которая на вход принимает число (N), а на выходе показывает все чётные числа от 1 до N.
# 5 -> 2, 4
# 8 -> 2, 4, 6, 8

number=input('Введите натуральное число больше 1=> ')
number=int(number)
if number<=1:
    print('Вы ввели число меньше 1')
else:
    count = 2
    while count<=number:
        print(f'{count} ')
        count += 2