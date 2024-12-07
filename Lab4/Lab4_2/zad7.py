# Napisz funkcję rekurencyjną obliczania potęgę n’tego stopnia liczby a, wartości dla
# argumentów funkcji podaje użytkownik.

def potega(a, n):
    if n == 0:
        return 1
    elif n < 0:
        return 1 / potega(a, -n)
    else:
        return a * potega(a, n - 1)

podana_wartosc_a = int(input("Podaj wartosc a: "))
podana_wartosc_n = int(input("Podaj wartosc n: "))
wynik = potega(podana_wartosc_a, podana_wartosc_n)
print(f"Wynik: {wynik}")

# Podaj wartosc a: 5
# Podaj wartosc n: 4
# Wynik: 625