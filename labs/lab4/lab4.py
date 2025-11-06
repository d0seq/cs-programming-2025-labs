#Задание 1
temperature = float (input("введите температуру: "))
if temperature < 20:
    print("Кондиционер включен")
else:
    print("Кондиционер выключен")

#Задание 2
month = int (input ("введите номер месяца: "))
if month in [12, 1, 2]:
    print("Зима")
elif month in [3, 4, 5]:
    print("Весна")
elif month in [6, 7, 8]:
    print("Лето")
elif month in [9, 10, 11]:
    print("Осень")
else:
    print("Ошибка: такого месяца нет")

#Задание 3
try:
    age = int(input("Введите возраст собаки: "))
    if age < 1:
        print("Ошибка: Возраст должен быть не меньше 1")
    elif age > 22:
        print("Ошибка: Возраст должен быть не больше 22")
    else:
        if age <= 2:
            x = age * 10.5
        else:
            x = 21 + (age - 2) * 4 
        print(f"Собачий возраст {age} лет = {x} человеческих лет") 
except ValueError:
    print("Ошибка: введено не число")

#Задание 4
num = int(input("Введите число: "))
if num % 2 == 0 and num % 3 == 0:
    print("Число делится на 6")
else:
    print("Не делится на 6")

#Задание 5
password = input("Введите пароль: ")
m = ""
if len(password) < 8:
    m = m + "слишком короткий, "
if not any(c in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" for c in password):
    m = m + "нет заглавных букв, "
if not any(c in "abcdefghijklmnopqrstuvwxyz" for c in password):
    m = m + "нет строчных букв, "
if not any(c in "0123456789" for c in password):
    m = m + "нет цифр, "
if not any(c in "!@#$%^&*()_+-=[]{}|;:,.<>?/" for c in password):
    m = m + "нет специальных символов, "
if m:
    print("Пароль ненадежный:", m[:-2])
else:
    print("Пароль надежный!")

#Задание 6
year = int(input("Введите текущий год: "))
if year % 4 == 0:
    if year % 100 != 0 or year % 400 == 0:
        print("Високосный год")
    else:
        print("Не високосный год")
else:
    print("Не високосный год")

#Задание 7
a = float(input("Введите первое число: "))
b = float(input("Введите второе число: "))
c = float(input("Введите третье число: "))
if a <= b and a <= c:
    minimum = a
elif b <= a and b <= c:
    minimum = b
else:
    minimum = c
print(f"Наименьшее число: {minimum}")

#Задание 8
summa = float(input("Введите сумму покупки: "))
if summa < 1000:
    sale = 0
elif summa <= 5000:
    sale = 5
elif summa <= 10000:
    sale = 10
else:
    sale = 15
y = summa - sale / 100
print(f"Ваша скидка: {sale}%")
print(f"К оплате: {y} руб.")

#Задание 9
hour = int (input ("Введите какой сейчас час(одно число): "))
if hour in [0, 1, 2, 3, 4, 5]:
    print("Ночь")
elif hour in [6, 7, 8, 9, 10, 11]:
    print("Утро")
elif hour in [12, 13, 14, 15, 16, 17]:
    print("День")
elif hour in [18, 19, 20, 21, 22, 23, 24]:
    print("Вечер")
else:
    print("Ошибка: введите какой сейчас час")

#Задание 10
n = int(input("Введите число: "))
if n < 2:
    print(f"{n} - составное число")
else:
    i = 2
    while i < n:
        if n % i == 0:
            print(f"{n} - составное число")
            i = n
        i = i + 1
    else:
        if n >= 2 and i == n:
            print(f"{n} - простое число")