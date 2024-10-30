# Napisz skrypt w Pythonie, który sprawdza, czy litera wprowadzona przez użytkownika jest duża
# czy mała

x = input('Podaj jedną literkę: ')

if len(x) == 1 and x.isalpha():
    if x.isupper():
        print(f'Wprowadzona literka {x} jest duża')
    else:
        print(f'Wprowadzona literka {x} jest mała')
else:
    print(f'Proszę wprowadzić dokładnie jedną literkę.')

# Przykład:
# Podaj jedną literkę: A
# Wprowadzona literka A jest duża