# Napisz funkcję, która otrzymuje dwa obiekty iterowalne (sekwencje) i zwraca listę wspólnych
# dla obu obiektów wartości.
# *Wykorzystaj konwersję do zbiorów podanych sekwencji oraz operację
# przecięcia wiedząc, że operator & dla zbiorów zwraca przecięcie, czyli elementy występujące
# w obu zbiorach.

def wspolne_wartosci(sekwencja1, sekwecnja2):
    zbior1 = set(sekwencja1)
    zbior2 = set(sekwencja2)
    wspolne = zbior1 & zbior2
    return list(wspolne)

sekwencja1 = [1, 2, 3, 4, 5]
sekwencja2 = [4, 5, 6, 7, 8]
wynik = wspolne_wartosci(sekwencja1, sekwencja2)
print(f"Wspólne wartości: {wynik}")

# Wspólne wartości: [4, 5]
