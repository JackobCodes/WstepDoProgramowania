# Stwórz wykres słupkowy przedstawiający ilość sprzedanych produktów w różnych kategoriach.

import matplotlib.pyplot as plt

kategorie = ['Art. Spożywcze', 'Elektronka', 'Motoryzacja', 'Art. Chemiczne']
wartosci = [1000, 250, 150, 350]
plt.bar(kategorie, wartosci)
plt.show()