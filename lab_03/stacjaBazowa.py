import random
import time

ziarno = 12345
lam = 0.5
czas_symulacji = 60
srednia = 8
odchylenie = 2
min_czas = 2
max_czas = 20
opoznienie = 1

random.seed(ziarno)

def generuj_pary(lam, czas_symulacji, srednia, odchylenie, min_czas, max_czas):
    pary = []
    t = 0
    while t <= czas_symulacji:
        t += random.expovariate(lam)
        while True:
            d = random.gauss(srednia, odchylenie)
            if min_czas <= d <= max_czas:
                break
        pary.append((t, d))
    return pary

pary = generuj_pary(lam, czas_symulacji, srednia, odchylenie, min_czas, max_czas)
tau = [p[0] for p in pary]
delta = [p[1] for p in pary]

for krok in range(1, czas_symulacji + 1):

    k = 0
    suma = 0
    for i in range(len(tau)):
        suma += tau[i]
        k += 1
        if suma >= 1:
            break

    nowe = list(zip(tau[:k], delta[:k]))

    print("Krok:", krok, "  k =", k, "  nowe zgloszenia:")
    for t, d in nowe:
        print("   tau =", round(t, 2), "  delta =", round(d, 2))

    tau = tau[k:]
    delta = delta[k:]

    time.sleep(opoznienie)