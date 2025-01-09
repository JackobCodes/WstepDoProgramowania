# Utwórz tablicę wypełnioną zerami 3x3. Wypełnij zaznaczone obszary tablicy jedynkami.

import numpy as np

array_a = np.zeros((3, 3), dtype=int)
array_a[2, :] = 1
print("a) Cały trzeci rząd:\n", array_a)

array_b = np.zeros((3, 3), dtype=int)
array_b[1, 1] = 1
array_b[2, 1] = 1
print("\nb) Rząd 2, kolumna 2 i rząd 3, kolumna 2:\n", array_b)

array_c = np.zeros((3, 3), dtype=int)
array_c[1:, :] = 1
print("\nc) Cały drugi i trzeci rząd:\n", array_c)

array_d = np.zeros((3, 3), dtype=int)
array_d[0, [0, 2]] = 1
array_d[1, [0, 2]] = 1
print("\nd) Rząd 1 kolumna 1 i 3 oraz rząd 2 kolumna 1 i 3:\n", array_d)

array_e = np.zeros((3, 3), dtype=int)
array_e[1, 1:] = 1
array_e[2, 1:] = 1
print("\ne) Rząd 2 kolumna 2 i 3 oraz rząd 3 kolumna 2 i 3:\n", array_e)

# a) Cały trzeci rząd:
#  [[0 0 0]
#  [0 0 0]
#  [1 1 1]]
#
# b) Rząd 2, kolumna 2 i rząd 3, kolumna 2:
#  [[0 0 0]
#  [0 1 0]
#  [0 1 0]]
#
# c) Cały drugi i trzeci rząd:
#  [[0 0 0]
#  [1 1 1]
#  [1 1 1]]
#
# d) Rząd 1 kolumna 1 i 3 oraz rząd 2 kolumna 1 i 3:
#  [[1 0 1]
#  [1 0 1]
#  [0 0 0]]
#
# e) Rząd 2 kolumna 2 i 3 oraz rząd 3 kolumna 2 i 3:
#  [[0 0 0]
#  [0 1 1]
#  [0 1 1]]
