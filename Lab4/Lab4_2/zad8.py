# A. Napisz funkcję o zmiennej liczbie parametrów, która wyświetla wartości parametrów na ekranie.
# B. Zmodyfikuj funkcję tak, aby znajdowała i zwracała wartość maksymalną.
# *Użyj parametru *args, który łączy wszystkie dodatkowe (nadmiarowe) argumenty pozycyjne,
# niebędące słowami kluczowymi podczas wywoływania funkcji, w krotkę.
# W Pythonie *args pozwala funkcji przyjmować zmienną liczbę argumentów pozycyjnych, które są
# przekazywane jako krotka (tuple). Dzięki temu można przekazać dowolną liczbę dodatkowych
# argumentów do funkcji bez konieczności definiowania ich z góry.

def wypisz_parametry(*args):
    for arg in args:
        print(arg)

wypisz_parametry(3, 5, 7, 2, 8, 1)

# 3
# 5
# 7
# 2
# 8
# 1


def znajdz_max(*args):
    if args:
        return max(args)
    return None

wynik = znajdz_max(3, 5, 7, 2, 8, 1)
print(f"Największa wartość: {wynik}")

# Największa wartość: 8
