# Napisz program, który wydrukuje do konsoli 10 pierwszych liczb pierwszych rozdzielonych
# przecinkiem tak jak pokazano poniżej.
# Pamiętaj, że liczba pierwsza - to taka liczba naturalna, która ma dokładnie dwa dzielniki naturalne:
# jedynkę i samą siebie.
# W rozwiązaniu użyj pętli while oraz instrukcji break
# Oczekiwany wynik:
# 2,3,5,7,11,13,17,19,23,29


licznik = 0
liczba = 2
wynik = []

while licznik < 10:
    liczba_pierwsza = True
    dzielnik = 2

    while dzielnik < liczba:
        if liczba % dzielnik == 0:
            liczba_pierwsza = False
            break
        dzielnik += 1

    if liczba_pierwsza:
        wynik.append(liczba)
        licznik += 1

    liczba += 1

print(",".join(map(str, wynik)))

# 2,3,5,7,11,13,17,19,23,29