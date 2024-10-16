# Narysuj schemat blokowy algorytmu i napisz program rozwiązywania ro wnania
# kwadratowego ax2 + bx + c = 0, gdzie a, b i c są wspo łczynnikami podawanymi przez
# uz ytkownika.

import math

a = float(input("Podaj współczynnik a: "))
b = float(input("Podaj współczynnik b: "))
c = float(input("Podaj współczynnik c: "))

if a == 0:
    if b == 0:
        if c == 0:
            print("Równanie ma nieskończenie wiele rozwiązań.")
        else:
            print("Równanie sprzeczne.")
    else:
        x= -c / b
        print(f"Równanie jest linowe, rozwiązanie to: x = {x:.2f}")
else:
    delta = b**2 - 4*a*c

    if delta > 0:
        x1 = (-b + math.sqrt(delta)) / (2*a)
        x2 = (-b - math.sqrt(delta)) / (2*a)
        print(f"Równanie ma dwa rozwiązanie: x1 = {x1:.2f}, x2 = {x2:.2f}")
    elif delta == 0:
        x = -b / 2*a
        print(f"Równanie ma jedno rozwiązanie: x = {x:.2f}")
    else:
        print("Równanie nie ma rozwiązań")


# Przykład:
# Podaj współczynnik a: 1
# Podaj współczynnik b: -5
# Podaj współczynnik c: 6
# Równanie ma dwa rozwiązanie: x1 = 3.00, x2 = 2.00
