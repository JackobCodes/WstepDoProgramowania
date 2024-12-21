# Stwórz moduł geometria.py, który będzie zawierał stałą PI oraz dwie funkcje do obliczeń
# geometrycznych:
# 1. obwod_kola(promien) – funkcję, która przyjmuje promień koła i zwraca jego obwód.
# 2. pole_kola(promien) – funkcję, która przyjmuje promień koła i zwraca jego pole.
# Użyj wartości PI = 3.14159 w obu funkcjach.
# Następnie w osobnym pliku (np. obliczenia.py) zaimportuj moduł matematyka i wywołaj
# obie funkcje dla promienia o długości 16. Wypisz wyniki obliczeń na ekranie.

PI = 3.14159

def obwod_kola(promien):
     return 2 * PI * promien

def pole_kola(promien):
    return PI * promien ** 2