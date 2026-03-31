import random
import time
import matplotlib.pyplot as plt

ziarno = 12345
lam = 0.5
czas_symulacji = 60
srednia = 8
odchylenie = 2
min_czas = 2
max_czas = 20
liczba_kanalow = 5
dlugosc_kolejki = 3
opoznienie = 1

random.seed(ziarno)

def generuj_pary(lam, czas_symulacji, srednia, odchylenie, min_czas, max_czas):
    pary = []
    t = 0
    while t <= czas_symulacji:
        przyrost = random.expovariate(lam)
        t += przyrost
        while True:
            d = random.gauss(srednia, odchylenie)
            if min_czas <= d <= max_czas:
                break
        pary.append((przyrost, d))
    return pary

pary = generuj_pary(lam, czas_symulacji, srednia, odchylenie, min_czas, max_czas)
tau = [p[0] for p in pary]
delta = [p[1] for p in pary]

kanaly = [None] * liczba_kanalow
kolejka = []

obsluzzone = 0
zablokowane = 0
historia_rho = []
historia_Q = []
historia_W = []

plt.ion()
fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(10, 8))
fig.suptitle("Symulator stacji bazowej")

ax1.set_title("Intensywnosc ruchu rho")
ax1.set_xlim(0, czas_symulacji)
ax1.set_ylim(0, 1)
ax1.set_xlabel("Krok")
ax1.set_ylabel("rho")
linia_rho, = ax1.plot([], [], color="blue")

ax2.set_title("Srednia dlugosc kolejki Q")
ax2.set_xlim(0, czas_symulacji)
ax2.set_ylim(0, dlugosc_kolejki + 1)
ax2.set_xlabel("Krok")
ax2.set_ylabel("Q")
linia_Q, = ax2.plot([], [], color="green")

ax3.set_title("Sredni czas oczekiwania W")
ax3.set_xlim(0, czas_symulacji)
ax3.set_ylim(0, (dlugosc_kolejki + 1) / lam + 1)
ax3.set_xlabel("Krok")
ax3.set_ylabel("W")
linia_W, = ax3.plot([], [], color="red")

plt.tight_layout()

print(f"{'Krok':>4} | {'Nowe':>4} | {'Zajete':>6} | {'Kolejka':>7} | {'rho':>6} | {'Q':>6} | {'W':>6} | {'Obsl.':>5} | {'Zablok.':>7}")
print("-" * 75)

for krok in range(1, czas_symulacji + 1):

    for i in range(liczba_kanalow):
        if kanaly[i] is not None:
            kanaly[i] -= 1
            if kanaly[i] <= 0:
                kanaly[i] = None
                obsluzzone += 1
                if kolejka:
                    kanaly[i] = kolejka.pop(0)

    k = 0
    suma = 0
    for i in range(len(tau)):
        suma += tau[i]
        if suma >= 1:
            k = i + 1
            break
    else:
        k = len(tau)

    nowe = list(zip(tau[:k], delta[:k]))
    tau = tau[k:]
    delta = delta[k:]

    for t, d in nowe:
        wolny = None
        for i in range(liczba_kanalow):
            if kanaly[i] is None:
                wolny = i
                break
        if wolny is not None:
            kanaly[wolny] = d
        elif len(kolejka) < dlugosc_kolejki:
            kolejka.append(d)
        else:
            zablokowane += 1

    zajete = sum(1 for k_ in kanaly if k_ is not None)
    rho = zajete / liczba_kanalow
    Q = len(kolejka)
    W = Q / lam

    historia_rho.append(rho)
    historia_Q.append(Q)
    historia_W.append(W)

    kroki = list(range(1, krok + 1))
    linia_rho.set_data(kroki, historia_rho)
    linia_Q.set_data(kroki, historia_Q)
    linia_W.set_data(kroki, historia_W)
    fig.canvas.draw()
    fig.canvas.flush_events()

    print(f"{krok:>4} | {len(nowe):>4} | {zajete:>6} | {Q:>7} | {rho:>6.2f} | {Q:>6.2f} | {W:>6.2f} | {obsluzzone:>5} | {zablokowane:>7}")

    time.sleep(opoznienie)

plt.ioff()

print("\n--- PODSUMOWANIE ---")
print(f"Czas symulacji:     {czas_symulacji} s")
print(f"Liczba kanalow:     {liczba_kanalow}")
print(f"Dlugosc kolejki:    {dlugosc_kolejki}")
print(f"Lambda:             {lam}")
print(f"Obsluzzone lacznie: {obsluzzone}")
print(f"Zablokowane:        {zablokowane}")
print(f"Srednie rho:        {sum(historia_rho)/len(historia_rho):.3f}")
print(f"Srednie Q:          {sum(historia_Q)/len(historia_Q):.3f}")
print(f"Srednie W:          {sum(historia_W)/len(historia_W):.3f}")

with open("wyniki_symulacji.txt", "w", encoding="utf-8") as f:
    f.write(f"Czas symulacji: {czas_symulacji}\n")
    f.write(f"Liczba kanalow: {liczba_kanalow}\n")
    f.write(f"Dlugosc kolejki: {dlugosc_kolejki}\n")
    f.write(f"Lambda: {lam}\n")
    f.write(f"Srednia rozm: {srednia}\n")
    f.write(f"Odchylenie: {odchylenie}\n")
    f.write(f"Min/Max rozm: {min_czas}/{max_czas}\n")
    f.write("\nKrok\trho\tQ\tW\n")
    for i in range(len(historia_rho)):
        f.write(f"{i+1}\t{historia_rho[i]:.3f}\t{historia_Q[i]:.3f}\t{historia_W[i]:.3f}\n")

print("Wyniki zapisane do: wyniki_symulacji.txt")

plt.show()