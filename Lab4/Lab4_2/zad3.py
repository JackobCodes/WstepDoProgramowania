# Napisz funkcję o nazwie powitanie, która przyjmuje dwa argumenty:
# imie – reprezentuje imię osoby, którą chcemy przywitać (domyślna wartość to
# "Użytkowniku").
# jezyk – reprezentuje język, w którym funkcja ma wyświetlić powitanie (domyślna wartość to
# "polski").
# Funkcja powinna działać w następujący sposób:
# Jeśli jezyk to "polski", funkcja powinna wyświetlić powitanie w języku polskim, np. Cześć,
# Anna.
# Jeśli jezyk to "angielski", funkcja powinna wyświetlić powitanie w języku angielskim, np.
# Hello, John.
# Jeśli jezyk to "niemiecki", funkcja powinna wyświetlić powitanie w języku niemieckim, np.
# Guten Morgen, Hans.
# Jeśli jezyk to inna wartość, funkcja powinna wyświetlić domyślne powitanie Witaj, <imie>.
# Zaprezentuj wywołanie funkcji z różnymi parametrami.

def powitanie(imie='Użytkowniku', jezyk='polski'):
    if jezyk == 'polski':
        print(f'Cześć, {imie}')
    elif jezyk == 'angielski':
        print(f'Hello, {imie}')
    elif jezyk == 'niemiecki':
        print(f'Guten Morgen, {imie}')
    else:
        print(f'Witaj, {imie}')

powitanie('Jakub', 'angielski')
# Hello, Jakub

powitanie()
# Cześć, Użytkowniku

powitanie('Ala', 'niemiecki')
# Guten Morgen, Ala
