# Wygeneruj wykres kołowy przedstawiający procentowy udział różnych kategorii w całkowitej sprzedaży.

import matplotlib.pyplot as plt

kategorie = ['Art. Spożywcze', 'Elektronka', 'Motoryzacja', 'Art. Chemiczne']
udzial = [50, 1, 28, 5]
plt.pie(udzial, labels=kategorie,
autopct='%1.f%%', startangle=90,
colors=['skyblue', 'lightgreen',
'lightcoral', 'gold'])
plt.title('Udział w kategoriach')
plt.show()