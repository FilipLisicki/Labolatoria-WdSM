ziarno = 12468

def losowa01():
    global ziarno
    a = 16807
    c = 0
    m = 2147483647
    ziarno = (a * ziarno + c) % m
    return ziarno / m

def generujtablice(ilosc):
    liczby = []
    for _ in range(ilosc):
        liczby.append(losowa01())
    return liczby

tablica = generujtablice(10)
print(tablica)