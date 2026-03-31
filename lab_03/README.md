Lab 03 – Modelowanie systemu M/M/S/S (symulator stacji bazowej)
Opis zadania

W ramach laboratorium zaimplementowano symulator stacji bazowej działający w modelu kolejkowym M/M/S/S. System odwzorowuje działanie komórki sieci mobilnej, w której zgłoszenia napływają zgodnie z rozkładem Poissona, a czas trwania połączeń modelowany jest rozkładem normalnym z ograniczeniami minimalnymi i maksymalnymi.

Symulacja obejmuje generowanie ruchu sieciowego, obsługę kanałów transmisyjnych oraz dynamiczną analizę stanu systemu w czasie. W każdym kroku czasowym (1 sekunda) system aktualizuje stan kanałów, przydziela nowe zgłoszenia oraz oblicza parametry takie jak intensywność ruchu ρ, średnia długość kolejki Q oraz średni czas oczekiwania W. Dodatkowo dane są zapisywane oraz wizualizowane w postaci wykresów.

Zaimplementowane elementy

W projekcie zaimplementowano generator zgłoszeń oparty na rozkładzie Poissona, generator czasu trwania połączeń oparty na rozkładzie Gaussa z ograniczeniami min/max oraz mechanizm symulacji pracy kanałów w czasie rzeczywistym. System obsługuje kolejkę zgłoszeń, przydział zasobów oraz aktualizację stanu systemu w kolejnych krokach czasowych. Dodatkowo obliczane są i monitorowane parametry ρ, Q oraz W.

Parametry symulacji

Symulator wykorzystuje parametry takie jak liczba kanałów S, intensywność ruchu λ, średni czas rozmowy N, odchylenie standardowe σ, minimalny i maksymalny czas rozmowy, długość kolejki oraz czas trwania symulacji.

Działanie programu

Program rozpoczyna od wygenerowania zgłoszeń zgodnie z rozkładem Poissona, a następnie dla każdego zgłoszenia losowany jest czas trwania rozmowy zgodnie z rozkładem normalnym. W kolejnych krokach symulacji system przydziela dostępne kanały, obsługuje aktywne połączenia oraz aktualizuje statystyki. W trakcie działania zapisywane są wartości parametrów systemu oraz generowane są wykresy przedstawiające ich zmiany w czasie.

Wyniki

W wyniku działania programu otrzymuje się wykresy przedstawiające zmiany intensywności ruchu ρ, średniej długości kolejki Q oraz średniego czasu oczekiwania W, a także dane zapisane w pliku dotyczące przebiegu symulacji.

Uruchomienie

Projekt został napisany w Pythonie i uruchamiany w środowisku PyCharm. Wymagane są biblioteki random, time oraz opcjonalnie matplotlib do wizualizacji wyników.
