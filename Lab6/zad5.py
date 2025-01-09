# Utwórz losową macierz o wymiarach 5x5. Znajdź największy i najmniejszy element. (patrz tab4_2d;
# metoda max(), min())
# Wypisz największe elementy w każdym z wierszy (axis = 1) i w każdej z kolumn (axis = 0).
# Policz sumę wartości w poszczególnych wierszach.

import numpy as np

tab4_2d = np.random.rand(5, 5)

max_element = tab4_2d.max()
min_element = tab4_2d.min()

max_in_rows = tab4_2d.max(axis=1)

max_in_columns = tab4_2d.max(axis=0)

row_sums = tab4_2d.sum(axis=1)

print("Macierz 5x5:")
print(tab4_2d)
print("\nNajwiększy element:", max_element)
print("Najmniejszy element:", min_element)
print("\nNajwiększe elementy w każdym wierszu:", max_in_rows)
print("Największe elementy w każdej kolumnie:", max_in_columns)
print("\nSuma wartości w poszczególnych wierszach:", row_sums)


# Macierz 5x5:
# [[0.35003321 0.60757344 0.18599083 0.86403814 0.25718658]
#  [0.08821365 0.171635   0.95286993 0.84867388 0.3370805 ]
#  [0.6368679  0.99368874 0.0248451  0.44062966 0.41892782]
#  [0.79485357 0.33374414 0.83186615 0.03742338 0.51247749]
#  [0.45722835 0.19083602 0.34808233 0.52665387 0.64229983]]
#
# Największy element: 0.9936887434885948
# Najmniejszy element: 0.024845101148734505
#
# Największe elementy w każdym wierszu: [0.86403814 0.95286993 0.99368874 0.83186615 0.64229983]
# Największe elementy w każdej kolumnie: [0.79485357 0.99368874 0.95286993 0.86403814 0.64229983]
#
# Suma wartości w poszczególnych wierszach: [2.2648222  2.39847296 2.51495922 2.51036472 2.1651004 ]