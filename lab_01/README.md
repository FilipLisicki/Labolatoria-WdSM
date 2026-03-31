Lab 01 – Teoretyczne podstawy i algorytmy generowania zdarzeń (ruchu)
Co zostało zrealizowane

W ramach laboratorium zapoznałem się z teorią generowania liczb losowych oraz pseudolosowych i ich zastosowaniem w symulacjach. Omówione zostały generatory liczb o różnych rozkładach statystycznych, w tym rozkładzie równomiernym, Poissona oraz normalnym (Gaussa).

Zaimplementowałem generator liczb pseudolosowych typu LCG (Linear Congruential Generator), który stanowi podstawę do dalszych obliczeń probabilistycznych.

Na jego podstawie przygotowałem:

generator rozkładu normalnego (Boxa-Mullera),
generator rozkładu Poissona,
możliwość pracy z ziarnem (seed) oraz bez ziarna (losowo inicjalizowany generator),
wizualizację wyników w postaci histogramów.

Kod został napisany w języku Python i uruchamiany w środowisku PyCharm.

Uruchomienie

Projekt uruchamiany w Pythonie (np. PyCharm).
Wymagane biblioteki: math, matplotlib, time.

Po uruchomieniu program generuje dane i wyświetla histogramy rozkładów.
