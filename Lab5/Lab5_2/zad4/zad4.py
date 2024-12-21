# Stwórz DataFrame zawierający dane o pracownikach firmy.
# Dane:
# 1. Numer identyfikacyjny pracownika: 1, 2, 3, 4, 5
# 2. Imię: Anna, Jan, Katarzyna, Tomasz, Michał
# 3. Nazwisko: Kowalska, Nowak, Wiśniewska, Kaczmarek, Zieliński
# 4. Stanowisko: Manager, Programista', Konsultant, Programista, Manager
# 5. Wiek: 35, 28, 40, 30, 45
# 6. Pensja (w PLN): 8000, 4500, 6000, 5500, 7000
#
# Wykonaj poniższe operacje na tych danych:
# a) Wybierz pracowników, którzy mają pensję większą niż 5000 PLN.
# b) Posortuj pracowników według wieku (od najmłodszych do najstarszych).
# c) Zgrupuj pracowników według stanowiska i oblicz średnią pensję w każdej grupie.
# d) Utwórz ramkę danych zawierającą informacje o pracownikach, którzy zmienili stanowisko (np. po
# awansie) i połącz ją z ramką pierwszego terminu na podstawie wspólnego klucza (np. numer
# identyfikacyjny).
# e) Zapisz przygotowany DataFrame do pliku CSV.
# f) Wczytaj dane z pliku CSV i sprawdź, czy wczytanie przebiegło poprawnie.

import pandas as pd

dane = {
    "Numer ID": [1, 2, 3, 4, 5],
    "Imię": ["Anna", "Jan", "Katarzyna", "Tomasz", "Michał"],
    "Nazwisko": ["Kowalska", "Nowak", "Wiśniewska", "Kaczmarek", "Zieliński"],
    "Stanowisko": ["Manager", "Programista", "Konsultant", "Programista", "Manager"],
    "Wiek": [35, 28, 40, 30, 45],
    "Pensja": [8000, 4500, 6000, 5500, 7000],
}

pracownicy = pd.DataFrame(dane)

pracownicy_z_wysoka_pensja = pracownicy[pracownicy["Pensja"] > 5000]

print("a) Pracownicy z pensją większą niż 5000 PLN:")
print(pracownicy_z_wysoka_pensja)

# a) Pracownicy z pensją większą niż 5000 PLN:
#    Numer ID       Imię    Nazwisko   Stanowisko  Wiek  Pensja
# 0         1       Anna    Kowalska      Manager    35    8000
# 2         3  Katarzyna  Wiśniewska   Konsultant    40    6000
# 3         4     Tomasz   Kaczmarek  Programista    30    5500
# 4         5     Michał   Zieliński      Manager    45    7000


pracownicy_posortowani_wedlug_wieku = pracownicy.sort_values(by="Wiek")

print("b) Pracownicy posortowani według wieku:")
print(pracownicy_posortowani_wedlug_wieku)

# b) Pracownicy posortowani według wieku:
#    Numer ID       Imię    Nazwisko   Stanowisko  Wiek  Pensja
# 1         2        Jan       Nowak  Programista    28    4500
# 3         4     Tomasz   Kaczmarek  Programista    30    5500
# 0         1       Anna    Kowalska      Manager    35    8000
# 2         3  Katarzyna  Wiśniewska   Konsultant    40    6000
# 4         5     Michał   Zieliński      Manager    45    7000


srednia_pensja_dla_stanowiska = pracownicy.groupby("Stanowisko")["Pensja"].mean().reset_index()

print("c) Średnia pensja dla każdego stanowiska:")
print(srednia_pensja_dla_stanowiska)

# c) Średnia pensja dla każdego stanowiska:
#     Stanowisko  Pensja
# 0   Konsultant  6000.0
# 1      Manager  7500.0
# 2  Programista  5000.0



nowe_stanowiska = {
    "Numer ID": [2, 4],
    "Nowe Stanowisko": ["Senior Programista", "Lead Programista"],
}
pracownicy_nowe_stanowiska = pd.DataFrame(nowe_stanowiska)
polaczone_dane = pd.merge(pracownicy, pracownicy_nowe_stanowiska, on="Numer ID", how="left")

print("d) Dane z nowymi stanowiskami:")
print(polaczone_dane)

# d) Dane z nowymi stanowiskami:
#    Numer ID       Imię    Nazwisko  ... Wiek  Pensja     Nowe Stanowisko
# 0         1       Anna    Kowalska  ...   35    8000                 NaN
# 1         2        Jan       Nowak  ...   28    4500  Senior Programista
# 2         3  Katarzyna  Wiśniewska  ...   40    6000                 NaN
# 3         4     Tomasz   Kaczmarek  ...   30    5500    Lead Programista
# 4         5     Michał   Zieliński  ...   45    7000                 NaN
#
# [5 rows x 7 columns]


sciezka_do_pliku = "pracownicy.csv"
pracownicy.to_csv(sciezka_do_pliku, index=False)


wczytane_dane = pd.read_csv(sciezka_do_pliku)

print("e) Dane wczytane z pliku CSV:")
print(wczytane_dane)

# e) Dane wczytane z pliku CSV:
#    Numer ID       Imię    Nazwisko   Stanowisko  Wiek  Pensja
# 0         1       Anna    Kowalska      Manager    35    8000
# 1         2        Jan       Nowak  Programista    28    4500
# 2         3  Katarzyna  Wiśniewska   Konsultant    40    6000
# 3         4     Tomasz   Kaczmarek  Programista    30    5500
# 4         5     Michał   Zieliński      Manager    45    7000