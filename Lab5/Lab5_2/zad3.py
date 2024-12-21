# Znajdź największy przyrost ludności we wszystkich latach. Wyświetl nazwę kraju, którego dotyczy
# ten przyrost.
# Użyj metody max() do całej DataFrame, z wyłączeniem kolumny „KRAJ”.
# Użyj metody idxmax() aby określić, w którym roku był największy przyrost.
# Ponownie skorzystaj z metody idxmax() w celu znalezienia „indeksu wiersza” w ramach tej kolumny,
# w którym wystąpił największy przyrost.

import pandas as pd

plik_csv = 'demografia.csv'


decimal_separator = ','
missing_values = ['NA', 'n/a', 'NaN']

try:
    dane = pd.read_csv(plik_csv, decimal=decimal_separator, na_values=missing_values)

    dane.set_index('KRAJE', inplace=True)

    przyrost_max = dane.max(axis=1).max()

    indeks_max_przyrostu = dane.max(axis=1).idxmax()

    rok_max_przyrostu = dane.loc[indeks_max_przyrostu].idxmax()

    print(f"Kraj z największym przyrostem ludności: {indeks_max_przyrostu}")
    print(f"Największy przyrost ludności: {przyrost_max}")
    print(f"Rok, w którym był największy przyrost: {rok_max_przyrostu}")

except FileNotFoundError:
    print(f"Plik {plik_csv} nie został znaleziony.")


# Kraj z największym przyrostem ludności: San Marino
# Największy przyrost ludności: 7.23
# Rok, w którym był największy przyrost: 1980