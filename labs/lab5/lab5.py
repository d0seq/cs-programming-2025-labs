# Задание 1
num = [1, 5, 8, 2, 3, 7, 9, 4, 6, 10]
for i in range(len(num)):
    if num[i] == 3:
        num[i] = 30
print(num)

# Задание 2
num = [2, 4, 6, 8, 10]
s = []
for x in num:
    s.append(x * x)
print(s)

# Задание 3
num = [15, 8, 23, 4, 42, 11]
max_num = 0
for x in num:
    if x > max_num:
        max_num = x
result = max_num / len(num)
print(result)

# Задание 4
my_tuple = (5, 2, 8, 1, 9)
try:
    sorted_tuple = tuple(sorted(my_tuple))
    print(sorted_tuple)
except TypeError:
    print(my_tuple)

# Задание 5
products = {"яблоки": 50, "бананы": 30, "виноград": 120, "хлеб": 25}
min_price = min(products, key=products.get)
max_price = max(products, key=products.get)
print(f"Минимальная цена: {min_price} - {products[min_price]}")
print(f"Максимальная цена: {max_price} - {products[max_price]}")

# Задание 6
items = ["a", "b", "c", "d"]
new_dict = {}
for item in items:
    new_dict[item] = item
print(new_dict)

# Задание 7
eng_rus = {"apple": "яблоко", "banana": "банан", "cat": "кошка"}
word = input("Введите русское слово: ")
for eng, rus in eng_rus.items():
    if rus == word:
        print(f"Перевод: {eng}")
        break
else:
    print("Слово не найдено")

# Задание 8

import random

rules = {
    "камень": ["ножницы", "ящерица"],
    "ножницы": ["бумага", "ящерица"], 
    "бумага": ["камень", "спок"],
    "ящерица": ["бумага", "спок"],
    "спок": ["ножницы", "камень"]
}

player = input("Камень, ножницы, бумага, ящерица, спок: ").lower()
computer = random.choice(list(rules.keys()))

print(f"Компьютер: {computer}")

if player == computer:
    print("Ничья!")
elif computer in rules[player]:
    print("Вы победили!")
else:
    print("Компьютер победил!")

# Задание 9
words = ["яблоко", "груша", "банан", "киви", "апельсин", "ананас"]
result_dict = {}
for word in words:
    first = word[0]
    if first not in result_dict:
        result_dict[first] = []
    result_dict[first].append(word)
print(result_dict)

# Задание 10
students = [("Анна", [5, 4, 5]), ("Иван", [3, 4, 4]), ("Мария", [5, 5, 5])]
averages = dict([(name, sum(grades)/len(grades)) for name, grades in students])
best_student = max(averages, key=averages.get)
best_grade = averages[best_student]
print(f"{best_student} имеет наивысший средний балл: {best_grade}")
