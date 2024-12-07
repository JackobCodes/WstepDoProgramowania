# Stwórz listę z imionami 4 osób.
# a. Posortuj ją alfabetycznie i wyświetl,
# b. Dodaj na końcu dwie osoby i pobierz ostatnią z nich poleceniem pop().
# c. Na pozycji 3 dodaj jeszcze jedną osobę.
# d. Odwróć kolejność na liście i zdubluj ją.

Imiona = ['Jakub', 'Marian', 'Ania', 'Oliwia']

print(f'Posortowana lista alfabetycznie: {sorted(Imiona)}')
# Posortowana lista alfabetycznie: ['Ania', 'Jakub', 'Marian', 'Oliwia']

Imiona.append('Mariusz')
Imiona.append('Weronika')
usuniecie = Imiona.pop()
print(f'Dodanie dwóch osób do listy {Imiona}, oraz usunięcie ostatniej osoby z listy {usuniecie}')
# Dodanie dwóch osób do listy ['Jakub', 'Marian', 'Ania', 'Oliwia', 'Mariusz'], oraz usunięcie ostatniej osoby z listy Weronika

Imiona.insert(2,'Adrian')
print(f'Dodanie nowej osoby na trzeciej pozycji: {Imiona}')
# Dodanie nowej osoby na trzeciej pozycji: ['Jakub', 'Marian', 'Adrian', 'Ania', 'Oliwia', 'Mariusz']

Imiona.reverse()
zdublowanie = Imiona*2
print(f'Odwrócenie listy i zdublowanie jej: {zdublowanie}')
# Odwrócenie listy i zdublowanie jej: ['Mariusz', 'Oliwia', 'Ania', 'Adrian', 'Marian', 'Jakub', 'Mariusz', 'Oliwia', 'Ania', 'Adrian', 'Marian', 'Jakub']