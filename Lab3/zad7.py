# A)
# Grupa laboratoryjna składa się z n studentów (wartość n podaje użytkownik). Wprowadzamy liczbę
# punktów dla każdego studenta.
# Napisz program, który obliczy średnią liczbę punktów w grupie z wykorzystaniem pętli while.
# WSTĘP DO PROGRAMOWANIA – LAB. 3
# MGR INŻ. ANNA MARCZAKIEWICZ 7
# Zastosuj instrukcje continue w programie tak, aby po podaniu liczby punktów spoza przedziału 0 –
# 100 pomijać dalsze wykonywanie pętli. Sprawdź działanie programu.

# A)
# n = int(input("Podaj liczbę studentów: "))
# suma_punktow = 0
# licznik = 0
#
# while licznik < n:
#     punkty = int(input(f"Podaj liczbę punktów dla studenta {licznik + 1}: "))
#     if punkty < 0 or punkty > 100:
#         print('Liczba punktów spoza przedziału 0-100. Spróbuj ponownie.')
#         continue
#     suma_punktow += punkty
#     licznik += 1
#
# srednia = suma_punktow / n
# print(f"Średnia liczba punktów w grupie: {srednia:.2f}")

# Podaj liczbę studentów: 10
# Podaj liczbę punktów dla studenta 1: 55
# Podaj liczbę punktów dla studenta 2: 42
# Podaj liczbę punktów dla studenta 3: 1
# Podaj liczbę punktów dla studenta 4: 741
# Liczba punktów spoza przedziału 0-100. Spróbuj ponownie.
# Podaj liczbę punktów dla studenta 4: 58
# Podaj liczbę punktów dla studenta 5: 99
# Podaj liczbę punktów dla studenta 6: 100
# Podaj liczbę punktów dla studenta 7: 0
# Podaj liczbę punktów dla studenta 8: -1
# Liczba punktów spoza przedziału 0-100. Spróbuj ponownie.
# Podaj liczbę punktów dla studenta 8: 61
# Podaj liczbę punktów dla studenta 9: 85
# Podaj liczbę punktów dla studenta 10: 19
# Średnia liczba punktów w grupie: 52.00

# B)
# Następnie zmień pętlę na nieskończoną, czyli taką której warunek zawsze jest prawdziwy. Zakończ
# działanie pętli przy użyciu instrukcji break.

# B)

suma_punktow = 0
licznik = 0

while True:
    punkty = int(input(f"Podaj liczbę punktów dla studenta {licznik + 1} (wpisz liczbę spoza przedziału aby zakończyć program): "))
    if punkty < 0 or punkty > 100:
        print('Liczba punktów spoza przedziału 0-100. Koniec pętli.')
        break
    suma_punktow += punkty
    licznik += 1

if licznik > 0:
    srednia = suma_punktow / licznik
    print(f'Średnia liczba punktów w grupie: {srednia:.2f}')
else:
    print('Nie wprowadzono żadnych poprawnych punktów.')

# Podaj liczbę punktów dla studenta 1 (wpisz liczbę spoza przedziału aby zakończyć program): 100
# Podaj liczbę punktów dla studenta 2 (wpisz liczbę spoza przedziału aby zakończyć program): 45
# Podaj liczbę punktów dla studenta 3 (wpisz liczbę spoza przedziału aby zakończyć program): 0
# Podaj liczbę punktów dla studenta 4 (wpisz liczbę spoza przedziału aby zakończyć program): 0
# Podaj liczbę punktów dla studenta 5 (wpisz liczbę spoza przedziału aby zakończyć program): 104
# Liczba punktów spoza przedziału 0-100. Koniec pętli.
# Średnia liczba punktów w grupie: 36.25