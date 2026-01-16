# Задание 1
def konvert_vremeni(chislo, ot_chego, v_chto):
    if ot_chego == "h":
        sekundi = chislo * 3600
    elif ot_chego == "m":
        sekundi = chislo * 60
    else:
        sekundi = chislo
    
    if v_chto == "h":
        otvet = sekundi / 3600
    elif v_chto == "m":
        otvet = sekundi / 60
    else:
        otvet = sekundi
    
    print(str(otvet) + v_chto)

# Задание 2
def vklad(summa, let):
    if summa < 30000:
        print("Error!")
        return
    
    dop_stavka = summa // 10000 * 0.3
    if dop_stavka > 5:
        dop_stavka = 5
    
    if let <= 3:
        osn_stavka = 3
    elif let <= 6:
        osn_stavka = 5
    else:
        osn_stavka = 2
    
    stavka_vsego = osn_stavka + dop_stavka
    
    vsego_deneg = summa
    god = 0
    while god < let:
        vsego_deneg = vsego_deneg + vsego_deneg * stavka_vsego / 100
        god = god + 1
    
    pribil = vsego_deneg - summa
    print(pribil)

# Задание 3
def prostie_chisla(nachalo, konec):
    if nachalo > konec:
        print("Error!")
        return
    
    spisok = []
    chislo = nachalo
    
    while chislo <= konec:
        if chislo > 1:
            prostoe = True
            delitel = 2
            while delitel < chislo:
                if chislo % delitel == 0:
                    prostoe = False
                    break
                delitel = delitel + 1
            
            if prostoe == True:
                spisok.append(chislo)
        
        chislo = chislo + 1
    
    if len(spisok) == 0:
        print("Нет простых чисел")
    else:
        for x in spisok:
            print(x, end=" ")

# Задание 4
def slozhenie_matric(razmer, matrica1, matrica2):
    if razmer <= 2:
        print("Error!")
        return
    
    otvet = []
    
    i = 0
    while i < razmer:
        stroka = []
        j = 0
        while j < razmer:
            stroka.append(matrica1[i][j] + matrica2[i][j])
            j = j + 1
        otvet.append(stroka)
        i = i + 1
    
    for stroka in otvet:
        for chislo in stroka:
            print(chislo, end=" ")
        print()

# Задание 5
def palindrom(stroka):
    chistaya = ""
    
    for bukva in stroka:
        if bukva != " ":
            chistaya = chistaya + bukva.lower()
    
    pal = True
    dlina = len(chistaya)
    
    i = 0
    while i < dlina // 2:
        if chistaya[i] != chistaya[dlina - 1 - i]:
            pal = False
            break
        i = i + 1
    
    if pal == True:
        print("Да")
    else:
        print("Нет")