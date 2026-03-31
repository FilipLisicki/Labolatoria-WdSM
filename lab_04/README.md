Lab 03 – Modelowanie systemu M/M/S/S (symulator stacji bazowej)
Opis zadania

W ramach laboratorium zaimplementowano kompletny symulator stacji bazowej działający w modelu kolejkowym M/M/S/S. System odwzorowuje działanie komórki sieci mobilnej, w której zgłoszenia napływają zgodnie z rozkładem Poissona, a czas trwania połączeń generowany jest na podstawie rozkładu normalnego z ograniczeniami minimalnymi i maksymalnymi.

Symulacja uwzględnia pracę wielu kanałów transmisyjnych, obsługę kolejki zgłoszeń oraz mechanizm blokowania połączeń w przypadku braku dostępnych zasobów. System działa w trybie krokowym (1 krok = 1 sekunda), aktualizując stan kanałów, kolejki oraz statystyki pracy systemu.

Zaimplementowane elementy

W projekcie zaimplementowano generator ruchu sieciowego oparty na rozkładzie Poissona, generator czasu trwania rozmów oparty na rozkładzie Gaussa oraz mechanizm przydziału zasobów w systemie wielokanałowym. Dodatkowo uwzględniono obsługę kolejki o ograniczonej długości oraz blokowanie zgłoszeń w przypadku jej przepełnienia. Symulacja umożliwia analizę pracy systemu w czasie rzeczywistym wraz z wizualizacją wyników.

Parametry symulacji

Symulator wykorzystuje następujące parametry: intensywność napływu zgłoszeń λ, średni czas rozmowy, odchylenie standardowe, minimalny i maksymalny czas rozmowy, liczbę kanałów transmisyjnych, długość kolejki oraz czas trwania symulacji. Dodatkowo używane jest ziarno generatora losowego zapewniające powtarzalność wyników.

Działanie programu

Program generuje zgłoszenia oraz czasy ich obsługi, a następnie w kolejnych krokach czasowych przydziela dostępne kanały lub umieszcza zgłoszenia w kolejce. W przypadku braku zasobów zgłoszenia są blokowane. W każdym kroku obliczane są parametry systemu, takie jak intensywność ruchu ρ, długość kolejki Q oraz średni czas oczekiwania W. Wyniki są prezentowane na wykresach oraz w formie tabelarycznej w konsoli.

Wyniki

Wyniki działania programu obejmują wykresy zmian parametrów ρ, Q oraz W w czasie symulacji, a także szczegółową tabelę wartości dla każdego kroku. Dodatkowo generowany jest plik tekstowy wyniki_symulacji.txt, zawierający parametry symulacji oraz przebieg wartości w czasie.

Na podstawie przykładowych danych zaobserwowano okresowe przeciążenie systemu (ρ ≈ 1) oraz występowanie blokad i zapełnianie kolejki przy ograniczonej liczbie kanałów.

Uruchomienie

Projekt napisany w Pythonie i uruchamiany w środowisku PyCharm. Wymagane biblioteki: random, time oraz matplotlib. Po uruchomieniu program generuje wykresy oraz zapisuje wyniki do pliku tekstowego.
