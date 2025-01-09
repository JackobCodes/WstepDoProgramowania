# Przedstaw dane na wykresie punktowym, gdzie oś X to czas, a oś Y to prędkość chwilowa pojazdu.

import matplotlib.pyplot as plt

czas = [10, 25, 39, 40, 50]
predkosc = [250, 48, 63, 88, 106]
plt.scatter(czas, predkosc, label='Dane')
plt.title('Wykres punktowy')
plt.xlabel('Czas')
plt.ylabel('Prędkość')
plt.legend()
plt.grid(True)
plt.show()