# Wczytaj plik demografia.csv, a następnie go wyświetl.
# Dodaj do funkcji read_csv() decimal oraz na_values
# Podpowiedź: na_values=['NA', 'n/a', 'NaN']: Definiuje listę wartości, które powinny być traktowane
# jako brakujące (NA). Można dostosować listę zgodnie z plikiem.

import pandas as pd

plik_csv = 'demografia.csv'

decimal_separator = ','
missing_values = ['NA', 'n/a', 'NaN']

try:
    dane = pd.read_csv(plik_csv, decimal=decimal_separator, na_values=missing_values)
    print("Zawartość pliku demografia.csv:")
    print(dane)
except FileNotFoundError:
    print(f"Plik {plik_csv} nie został znaleziony.")


# Zawartość pliku demografia.csv:
#                  KRAJE   1965   1970   1980  ...  2010a   2015   2020   2022
# 0          Armenia       3.15   2.22   1.45  ...   0.41  -0.40   0.12      .
# 1          Austria       0.63   0.32   0.10  ...   0.35   1.34   0.36   1.40
# 2      Azerbejdżan       2.85   2.12   1.50  ...   1.26   1.17   0.52  -0.29
# 3           Belgia       0.75  -0.10   0.08  ...   0.10   0.65   0.28   1.17
# 4         Białoruś       1.14   0.94   0.74  ...   0.01   0.18      .      .
# 5         Bułgaria       0.65   0.60   0.34  ...  -0.78  -0.67  -0.50  -5.72
# 6        Chorwacja       0.69   0.40   0.06  ...  -0.31  -0.82  -0.54  -0.30
# 7             Cypr       0.81   0.80   1.14  ...   0.16   0.15   0.90   1.77
# 8           Czechy       0.47   0.21   0.20  ...   0.25   0.15  -1.86   2.96
# 9            Dania       0.81   0.69   0.03  ...   0.47   0.84   0.30   1.01
# 10         Estonia       0.97   1.24   0.68  ...   0.00   0.08   0.08   2.56
# 11       Finlandia       0.27  -0.35   0.34  ...   0.44   0.28   0.15   0.28
# 12         Francja       0.72   0.96   0.55  ...   0.55   0.27   0.25   0.29
# 13          Grecja       0.52   0.28   1.15  ...   0.18  -0.69  -0.34  -0.63
# 14          Gruzja       1.23   1.15   0.83  ...   0.74  -0.24   0.32   1.29
# 15       Hiszpania       1.04   1.56   1.05  ...   0.36  -0.02   0.14   1.32
# 16        Holandia       1.34   1.24   0.83  ...   0.49   0.46   0.39   1.25
# 17        Irlandia       0.31   0.94   1.17  ...   0.29   1.03   0.86   2.65
# 18        Islandia       1.73   0.49   1.07  ...   0.26   1.04   1.28   3.06
# 19           Litwa       1.20   1.32   0.53  ...  -2.57  -1.13   0.06   1.83
# 20      Luksemburg       0.90   0.40   0.38  ...   1.93   2.33   1.38   2.39
# 21           Łotwa       0.96   0.62   0.23  ...  -0.84  -0.87  -0.76   0.39
# 22           Malta          .   0.10   0.98  ...   0.78   2.41   0.30   4.05
# 23          Niemcy       0.98  -0.26   0.28  ...  -0.06   1.20  -0.01   1.35
# 24        Norwegia       0.78   0.65   0.33  ...   1.27   0.85   0.44   1.17
# 25          Polska       0.67  -0.04   0.90  ...   0.09  -0.10  -0.31  -2.39
# 26      Portugalia      -0.67  -0.40   1.08  ...  -0.01  -0.32   0.02   1.11
# 27           Rosja       0.69   0.48   0.51  ...   0.66      .      .      .
# 28         Rumunia       0.54   1.09   0.67  ...  -0.23  -0.56  -0.66   0.05
# 29       San Marino      1.14   2.29   7.23  ...      .   0.66      .   0.34
# 30        Słowacja       0.95   0.75   0.83  ...   0.19   0.09   0.03  -0.11
# 31        Słowenia       1.33   0.69   0.87  ...   0.16   0.06   0.63   0.46
# 32      Szwajcaria       0.93   0.39   0.50  ...   1.03   1.08   0.75   0.85
# 33         Szwecja       1.00   0.96   0.18  ...   0.80   1.06   0.50   0.66
# 34         Ukraina       0.92   0.82   0.36  ...  -0.40  -0.40  -0.75      .
# 35           Węgry       0.25   0.29  -0.04  ...  -0.29  -0.25  -0.40  -0.95
# 36  Wielka Brytania      0.60   0.42   0.10  ...   0.66   0.81      .      .
# 37          Włochy       0.79   0.51   0.16  ...   0.74  -0.21  -0.68  -0.30
#
# [38 rows x 12 columns]