# Utwórz listę: Moja_lista=[1, 17, 3, 5, 3, 4, 86, 90, 2, 21], przetestuj działanie wszystkich
# zaprezentowanych operacji na listach, a ich wynik wyświetl w konsoli.

Moja_lista = [1, 17, 3, 5, 3, 4, 86, 90, 2, 21]

print(f'Pierwszy element listy: {Moja_lista[0]}')
# Pierwszy element listy: 1

print(f'Ostatni element listy: {Moja_lista[-1]}')
# Ostatni element listy: 21

print(f'Długość listy: {len(Moja_lista)}')
# Długość listy: 10

print(f'Największa wartość z listy: {max(Moja_lista)}')
# Największa wartość z listy: 90

print(f'Najmniejsza wartość z listy: {min(Moja_lista)}')
# Najmniejsza wartość z listy: 1

print(f'Posortowane wartości z listy: {sorted(Moja_lista)}')
# Posortowane wartości z listy: [1, 2, 3, 3, 4, 5, 17, 21, 86, 90]

print(f'Suma wartości elementów z listy: {sum(Moja_lista)}')
# Suma wartości elementów z listy: 232

Moja_lista.append(6)
print(f'Dodanie kolejnego elementu na końcu listy: {Moja_lista}')
# Dodanie kolejnego elementu na końcu listy: [1, 17, 3, 5, 3, 4, 86, 90, 2, 21, 6]

Moja_lista.insert(4,5)
print(f'Dodanie nowego elementu listy w indesie 4 oraz przesunięcie reszty elementów o jeden index: {Moja_lista}')
# Dodanie nowego elementu listy w indesie 4 oraz przesunięcie reszty elementów o jeden index: [1, 17, 3, 5, 5, 3, 4, 86, 90, 2, 21, 6]

print(f'Zwrócenie ostatniego elementu z listy z jednoczesnym usunięciem go z niej: {Moja_lista.pop()}')
# Zwrócenie ostatniego elementu z listy z jednoczesnym usunięciem go z niej: 6

Moja_lista.reverse()
print(f'Odwrócenie kolejności elementów listy {Moja_lista}')
# Odwrócenie kolejności elementów listy [21, 2, 90, 86, 4, 3, 5, 5, 3, 17, 1]

Moja_lista2 = Moja_lista*5
print(f'Pięciokrotne powrtórzenie wartości z listy w nowej liście: {Moja_lista2}')
# Pięciokrotne powrtórzenie wartości z listy w nowej liście: [21, 2, 90, 86, 4, 3, 5, 5, 3, 17, 1, 21, 2, 90, 86, 4, 3, 5, 5, 3, 17, 1, 21, 2, 90, 86, 4, 3, 5, 5, 3, 17, 1, 21, 2, 90, 86, 4, 3, 5, 5, 3, 17, 1, 21, 2, 90, 86, 4, 3, 5, 5, 3, 17, 1]

print(f'Wycinek listy: od początku do elementu 5: {Moja_lista[:5]}')
# Wycinek listy: od początku do elementu 5: [21, 2, 90, 86, 4]

print(f'Wycinek listy: od elementu o indeksie 6 do końca: {Moja_lista[6:]}')
# Wycinek listy: od elementu o indeksie 6 do końca: [5, 5, 3, 17, 1]

print(f'Wycinek listy: dany zakres elementów 3-6 z krokiem 2 {Moja_lista[3:6:2]}')
# Wycinek listy: dany zakres elementów 3-6 z krokiem 2 [86, 3]

print(f'Odwrócenie listy {Moja_lista[::1]}')
# Odwrócenie listy [21, 2, 90, 86, 4, 3, 5, 5, 3, 17, 1]