﻿# Задача-1: поработайте с переменными, создайте несколько,
# выведите на экран, запросите от пользователя и сохраните в переменную, выведите на экран

age = 26
name = 'Александр'
print('Меня зовут', name, 'и мне', age, 'лет!')
name_2 = input('А как тебя зовут?')
print('Очень приятно,', name_2)

# Задача-2: Запросите от пользователя число, сохраните в переменную,
# прибавьте к числу 2 и выведите результат на экран.
# Если возникла ошибка, прочитайте ее, вспомните урок и постарайтесь устранить ошибку.

number_1 = int(input('Напиши число: '))
print(number_1 + 2)

# Задача-3: Запросите у пользователя его возраст.
# Если ему есть 18 лет, выведите: "Доступ разрешен",
# иначе "Извините, пользование данным ресурсом только с 18 лет"

age_2 = int(input('Привет! Сколько тебе лет? '))
if age_2 >= 18:
    print('Доступ разрешен')
else:
    print('Извините, пользование данным ресурсом только с 18 лет')