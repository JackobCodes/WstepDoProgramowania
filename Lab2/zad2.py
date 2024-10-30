# Napisz program porządkowania trzech liczb x, y i z. Od najmniejszej do największej, bez użycia
# wbudowanych funkcji


x = float(input('Podaj liczbę x: '))
y = float(input('Podaj liczbę y: '))
z = float(input('Podaj liczbę z: '))

if x <= y and x <= z:
    if y <= z:
        print(f'Kolejność liczb od najmniejszej do największej: x = {x}, y = {y}, z = {z}')
    else:
        print(f'Kolejność liczb od najmniejszej do największej: x = {x}, z = {z}, y = {y}')
elif y <= x and y <= z:
    if x <= z:
        print(f'Kolejność liczb od najmniejszej do największej: y = {y}, x = {x}, z = {z}')
    else:
        print(f'Kolejność liczb od najmniejszej do największej: y = {y}, z = {z}, x = {x}')
else:
    if x <= y:
        print(f'Kolejność liczb od najmniejszej do największej: z = {z}, x = {x}, y = {y}')
    else:
        print(f'Kolejność liczb od najmniejszej do największej: z = {z}, y = {y}, x = {x}')



# Przykład:
# Podaj liczbę x: 355.66
# Podaj liczbę y: 64.3
# Podaj liczbę z: 33
# Kolejność liczb od najmniejszej do największej: z = 33.0, y = 64.3, x = 355.66
