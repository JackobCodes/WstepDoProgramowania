# Napisz funkcję, która pozwoli obliczyć kwadrat liczby podanej przez użytkownika.
# Zaprezentuj wywołanie funkcji.

def square(x):
    return x ** 2

input_x = int(input('Podaj x: '))
print(f'Kwadrat podanej liczby to: {square(input_x)}')

# Podaj x: 12
# Kwadrat podanej liczby to: 144