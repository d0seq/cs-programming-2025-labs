#Задание 1
unit = {"h": 3600, "m": 60, "s": 1}
def time(x, y, z):
    return x * unit[y] / unit[z]
first = time(4, "h", "m")
second = time(30, "m", "h")
third = time(12, "s", "h")
print(f"{first}m") 
print(f"{second}h")
print(f"{third}h")

#Задание 2
def calculate(x: int, y: int):
    if x < 30000:
        return 0
    total = 0
    base = min(0.3 * (x // 10000), 5)
    for i in range(y):
        if i <= 2: rate = 3
        elif i < 6: rate = 5
        else: rate = 2
        interest = x * ((base + rate) * 0.01)
        total += interest
        x += interest
    return total
first = calculate(30000, 3)
second = calculate(100000, 5)
third = calculate(200000, 8)
print(f"{first}")
print(f"{second}")
print(f"{third}")

#Задание 3
def prime(x):
    if x < 2: return False
    if x == 2: return True
    if x % 2 == 0: return False
    return all(x % i for i in range(3, int(x**0.5) + 1, 2))
def primes(a, b):
    p = [str(x) for x in range(a, b + 1) if prime(x)]
    if not p: return "Error!"
    r = ""
    for i in p:
        r += i + " "
    return r[:-1]
first = primes(1, 10)
second = primes(15, 120)
third = primes(0, 1)
print(f"{first}")
print(f"{second}")
print(f"{third}")

#Задание 4
def matrix(n):
    return [list(map(int, input().split())) for _ in range(n)]
def summa(x, y, z):
    for i in range(n):
        for j in range(n):
            print(x[i][j] + y[i][j], end=" ")
        print()
n = int(input())
first = matrix(n)
second = matrix(n)
if any(len(row) != n for row in first + second):
    print("Error!")
else:
    summa(first, second, n)

#Задание 5
def palindrome(text):
    symbols = " !?,.;:-_'\""
    list = {
        'A': 'a', 'B': 'b', 'C': 'c', 'D': 'd', 'E': 'e', 'F': 'f', 'G': 'g',
        'H': 'h', 'I': 'i', 'J': 'j', 'K': 'k', 'L': 'l', 'M': 'm', 'N': 'n',
        'O': 'o', 'P': 'p', 'Q': 'q', 'R': 'r', 'S': 's', 'T': 't', 'U': 'u',
        'V': 'v', 'W': 'w', 'X': 'x', 'Y': 'y', 'Z': 'z',
        'А': 'а', 'Б': 'б', 'В': 'в', 'Г': 'г', 'Д': 'д', 'Е': 'е', 'Ё': 'ё',
        'Ж': 'ж', 'З': 'з', 'И': 'и', 'Й': 'й', 'К': 'к', 'Л': 'л', 'М': 'м',
        'Н': 'н', 'О': 'о', 'П': 'п', 'Р': 'р', 'С': 'с', 'Т': 'т', 'У': 'у',
        'Ф': 'ф', 'Х': 'х', 'Ц': 'ц', 'Ч': 'ч', 'Ш': 'ш', 'Щ': 'щ', 'Ъ': 'ъ',
        'Ы': 'ы', 'Ь': 'ь', 'Э': 'э', 'Ю': 'ю', 'Я': 'я'
    }
    y = ""
    for x in text:
        if x not in symbols:
            y += list.get(x, x)
    return "Да" if y == y[::-1] else "Нет"
first = palindrome("А роза упала на лапу Азора")
second = palindrome("Borrow or rob")
third = palindrome("Алфавитный порядок")
print(f"{first}") 
print(f"{second}")
print(f"{third}")