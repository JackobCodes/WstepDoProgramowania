# Utwórz 8-elementową listę składającą się z wartościach będących kolejnymi potęgami liczby 2 - [128 64 32 16 8 4 2 1].
# Na podstawie tej listy utwórz tablice ndarray o nazwie wagi.
# Utwórz drugą 8-elementową tablicę ndarray wypełnioną zerami i jedynkami (losowo) o nazwie liczba_bin.
# Napisz funkcję wartosc_liczby_bin(), która oblicza wartość liczby binarnej na podstawie listy wagi i listy
# liczba_bin. (funkcja konwertuje liczbę binarną na system dziesiętny)

import numpy as np

wagi = np.array([128, 64, 32, 16, 8, 4, 2, 1])

liczba_bin = np.random.randint(0, 2, size=8)

def wartosc_liczby_bin(wagi, liczba_bin):
    return np.sum(wagi * liczba_bin)

wartosc_dziesietna = wartosc_liczby_bin(wagi, liczba_bin)

print("Wagi:", wagi)
print("Liczba binarna:", liczba_bin)
print("Wartość dziesiętna:", wartosc_dziesietna)

# Wagi: [128  64  32  16   8   4   2   1]
# Liczba binarna: [0 0 1 0 1 1 0 0]
# Wartość dziesiętna: 44