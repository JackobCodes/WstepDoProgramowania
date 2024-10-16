# Narysuj schemat blokowy algorytmu i napisz program rozwiązywania ro wnania
# liniowego ax + b = 0 , gdzie a i b są wspo łczynnikami podawanymi przez uz ytkownika

a = float(input("Podaj współczynnik a: "))
b = float(input("Podaj współczynnik b: "))

if a == 0:
    if b == 0:
        print("Równanie ma nieskończenie wiele rozwiązań.")
    else:
        print("Równanie nie ma rozwiązań.")
else:
    x = -b / a
    print(f"Rozwiązanie równania ax + b = 0: x = {x:.2f}")

# Przykład:
# Podaj współczynnik a: 6
# Podaj współczynnik b: -75
# Rozwiązanie równania ax + b = 0: x = 12.50