# Задание 1
def time_converter(x, y, z):
    if y == 'h':
        s = x * 3600
    elif y == 'm':
        s = x * 60
    else:
        s = x
    
    if z == 'h':
        r = s / 3600
    elif z == 'm':
        r = s / 60
    else:
        r = s
    
    return f"{r:.2f}{z}"

# Задание 2
def calculate_profit(x, y):
    if x < 30000:
        return "Error!"
    
    a = (x // 10000) * 0.3
    if a > 5:
        a = 5
    
    if y <= 3:
        b = 3
    elif y <= 6:
        b = 5
    else:
        b = 2
    
    c = b + a
    d = x
    
    for _ in range(int(y)):
        d = d * (1 + c/100)
    
    e = d - x
    return f"{e:.2f}"

# Задание 3
def find_primes(x, y):
    if x > y:
        return "Error!"
    
    z = []
    for i in range(x, y + 1):
        if i > 1:
            p = True
            for j in range(2, i):
                if i % j == 0:
                    p = False
                    break
            if p:
                z.append(i)
    
    if not z:
        return "Нет простых чисел"
    else:
        return " ".join(map(str, z))

# Задание 4
def add_matrices(n, m1, m2):
    if n <= 2:
        return "Error!"
    
    r = []
    for i in range(n):
        t = []
        for j in range(n):
            t.append(m1[i][j] + m2[i][j])
        r.append(t)
    
    return r

# Задание 5
def check_palindrome(s):
    t = ""
    for c in s:
        if c != " ":
            t += c.lower()
    
    p = True
    l = len(t)
    for i in range(l // 2):
        if t[i] != t[l - 1 - i]:
            p = False
            break
    
    if p:
        return "Да"
    else:
        return "Нет"