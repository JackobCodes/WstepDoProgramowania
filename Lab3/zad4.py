# Zamówiłeś w restauracji z grupą x przyjaciół, n potraw (liczbę zamówionych dań i liczbę gości, za
# każdym razem wskazuje użytkownik), następnie dla każdej potrawy podajesz jej cenę.
# Korzystając z pętli while napisz program, który pozwoli obliczyć średnią cenę zamówionej potrawy.
# Podziel sprawiedliwe rachunek miedzy wszystkich gości.

liczba_gosci = int(input("Podaj liczbę gości: "))
liczba_dan = int(input("Podaj liczbę zamówionych potraw: "))

suma_cen = 0
licznik = 0

while licznik < liczba_dan:
    cena = float(input(f"Podaj cenę potrawy {licznik + 1}: "))
    suma_cen += cena
    licznik += 1

srednia_cena = suma_cen / liczba_dan

rachunek_osoba = suma_cen / liczba_gosci

print('\nPodsumowanie:')
print(f"Średnia cena potrawy: {srednia_cena:.2f} zł")
print(f"Każda osoba powinna zapłacić: {rachunek_osoba:.2f} zł")

# Podaj liczbę gości: 5
# Podaj liczbę zamówionych potraw: 7
# Podaj cenę potrawy 1: 25
# Podaj cenę potrawy 2: 77
# Podaj cenę potrawy 3: 13
# Podaj cenę potrawy 4: 53
# Podaj cenę potrawy 5: 86
# Podaj cenę potrawy 6: 23
# Podaj cenę potrawy 7: 111
#
# Podsumowanie:
# Średnia cena potrawy: 55.43 zł
# Każda osoba powinna zapłacić: 77.60 zł