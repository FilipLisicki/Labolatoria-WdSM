import math
import matplotlib.pyplot as plt
import time

ziarno = None

def ustawziarno(uzycieziarna=True, wartosc=12468):
    global ziarno
    if uzycieziarna:
        ziarno = wartosc
    else:
        ziarno = int(time.time() * 1000) % 2147483647

def losowa01():
    global ziarno
    a = 16807
    c = 0
    m = 2147483647
    ziarno = (a * ziarno + c) % m
    return ziarno / m

def poisson(lmbd):
    X = -1
    S = 1
    q = math.exp(-lmbd)
    while S > q:
        U = losowa01()
        S = S * U
        X += 1
    return X

def generujpoisson(lmbd, ilosc):
    liczby = []
    for _ in range(ilosc):
        liczby.append(poisson(lmbd))
    return liczby

uzyjziarna = True
wartoscziarna = 12468
lambda_value = 4
ilosc = 10000

ustawziarno(uzyjziarna, wartoscziarna)
dane = generujpoisson(lambda_value, ilosc)

plt.hist(dane, bins=max(dane)-min(dane)+1, density=True)
plt.title("Rozklad Poissona")
plt.xlabel("k")
plt.ylabel("P(k)")
plt.show()