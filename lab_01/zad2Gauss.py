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

def gauss(mu, sigma):
    U1 = losowa01()
    U2 = losowa01()
    Z0 = math.sqrt(-2 * math.log(U1)) * math.cos(2 * math.pi * U2)
    Z1 = math.sqrt(-2 * math.log(U1)) * math.sin(2 * math.pi * U2)
    X0 = mu + sigma * Z0
    X1 = mu + sigma * Z1
    return X0, X1

def generujgauss(mu, sigma, ilosc):
    liczby = []
    while len(liczby) < ilosc:
        x0, x1 = gauss(mu, sigma)
        liczby.append(x0)
        if len(liczby) < ilosc:
            liczby.append(x1)
    return liczby

uzyjziarna = True
wartoscziarna = 12468
srednia = 5
odchylenie = 2
ilosc = 10000

ustawziarno(uzyjziarna, wartoscziarna)
dane = generujgauss(srednia, odchylenie, ilosc)

plt.hist(dane, bins=50, density=True)
plt.title(f"Rozkład normalny N({srednia},{odchylenie**2})")
plt.xlabel("x")
plt.ylabel("P(x)")
plt.show()