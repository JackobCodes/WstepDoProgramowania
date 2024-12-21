# Zdefiniuj 10cio elementową krotkę(tuple), której elementy są losowane z przedziału
# podanego przez użytkownika. Oblicz średnią geometryczną krotki.
# Aby obliczyć średnią geometryczną, możemy użyć wzoru:
# , gdzie n to liczba elementów w krotce, a a1,a2,…an to elementy krotki.

import random
import math

def srednia_geometryczna(liczby):
    iloczyn = 1
    for liczba in liczby:
        iloczyn *= liczba
    return math.pow(iloczyn, 1 / len(liczby))

dolna_granica = int(input("Podaj dolną granicę przedziału: "))
gorna_granica = int(input("Podaj górną granicę przedziału: "))

if dolna_granica > gorna_granica:
    dolna_granica, gorna_granica = gorna_granica, dolna_granica

krotka = tuple(random.randint(dolna_granica, gorna_granica) for _ in range(10))

srednia_geom = srednia_geometryczna(krotka)

print(f"Wygenerowana krotka: {krotka}")
print(f"Średnia geometryczna krotki: {srednia_geom:.2f}")

# Podaj dolną granicę przedziału: 45
# Podaj górną granicę przedziału: 6
# Wygenerowana krotka: (44, 39, 6, 41, 41, 12, 14, 45, 41, 20)
# Średnia geometryczna krotki: 25.30