'''
Задайте список. Напишите программу, которая определит, присутствует ли в заданном списке строк некое число.
'''

sp = [1, 5, 10 , 'ghjk', 3 , 'number', 354, 'gtrt45', 988, 52, 'job30', 7]

try:
    N = int(input('Введите число: '))

    print()
    print(sp)
    print()

    def check(a, lists):
        if a in lists:
            print('Данное число присутствует в списке')
        else:
            print ("Такое чисо отсутствует")

    check(N, sp)
except ValueError:
    print('Должно быть введено число')