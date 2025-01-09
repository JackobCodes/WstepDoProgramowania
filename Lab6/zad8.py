# Stwórz macierz o wymiarach 5x5 o losowych wartościach, a następnie wybierz elementy, które
# są większe niż 20 i wypisz ich liczbę. Policz średnią dla całejtablicy.

import numpy as np

matrix = np.random.randint(0, 51, (5, 5))

print("Macierz 5x5 z losowymi wartościami:")
print(matrix)

elements_greater_than_20 = matrix[matrix > 20]

count_greater_than_20 = elements_greater_than_20.size

average = matrix.mean()

print("\nElementy większe niż 20:")
print(elements_greater_than_20)
print(f"\nLiczba elementów większych niż 20: {count_greater_than_20}")
print(f"Średnia dla całej tablicy: {average:.2f}")

# Macierz 5x5 z losowymi wartościami:
# [[27  5 16  5  2]
#  [43  3  4 48  9]
#  [44 26 28 19 49]
#  [22 33  5 13 12]
#  [27 12 23 16 34]]
#
# Elementy większe niż 20:
# [27 43 48 44 26 28 49 22 33 27 23 34]
#
# Liczba elementów większych niż 20: 12
# Średnia dla całej tablicy: 21.00