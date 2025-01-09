# Utwórz macierz o wymiarach 5x5 wypełnioną początkowo zerami. Na każdym brzegu macierzy
# ustaw jedynki (góra, dół, lewo, prawo). Napisz funkcję zamieniającą zera na jedynki i odwrotnie.

import numpy as np

matrix = np.zeros((5, 5), dtype=int)

matrix[0, :] = 1
matrix[-1, :] = 1
matrix[:, 0] = 1
matrix[:, -1] = 1

print("Początkowa macierz:")
print(matrix)

def toggle_zeros_ones(matrix):
    return np.where(matrix == 0, 1, 0)

toggled_matrix = toggle_zeros_ones(matrix)

print("\nMacierz po zamianie zer na jedynki i odwrotnie:")
print(toggled_matrix)

# Początkowa macierz:
# [[1 1 1 1 1]
#  [1 0 0 0 1]
#  [1 0 0 0 1]
#  [1 0 0 0 1]
#  [1 1 1 1 1]]
#
# Macierz po zamianie zer na jedynki i odwrotnie:
# [[0 0 0 0 0]
#  [0 1 1 1 0]
#  [0 1 1 1 0]
#  [0 1 1 1 0]
#  [0 0 0 0 0]]
