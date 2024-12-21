# Znajdź kraj, w którym odnotowano największy przyrost ludności w roku 2022.
# Użyj metody idxmax(), która zwraca indeks pierwszego wystąpienia maksymalnej wartości w serii lub
# ramce danych.
# Podpowiedź: skipna: domyślnie ustawiony na True, co oznacza, że wartości NaN są pomijane podczas
# obliczeń. Jeśli ustawisz go na False, uwzględni również wartości NaN.

import pandas as pd

plik_csv = 'demografia.csv'


decimal_separator = ','
missing_values = ['NA', 'n/a', 'NaN']

try:
    dane = pd.read_csv(plik_csv, decimal=decimal_separator, na_values=missing_values)

    dane.set_index('KRAJE', inplace=True)

    if '2022' in dane.columns:
        indeks_max = dane['2022'].idxmax(skipna=True)
        kraj_max = indeks_max  # Nazwa kraju
        przyrost_max = dane.loc[indeks_max, '2022']

        print(f"Kraj z największym przyrostem ludności w 2022 roku: {kraj_max}")
        print(f"Wartość przyrostu: {przyrost_max}")
    else:
        print("Kolumna '2022' nie została znaleziona w danych.")
except FileNotFoundError:
    print(f"Plik {plik_csv} nie został znaleziony.")

# Kraj z największym przyrostem ludności w 2022 roku: Malta
# Wartość przyrostu: 4.05