# Napisz skrypt, który pobiera od użytkownika drogę pokonaną przez samochód oraz średnie
# spalanie (w litrach na 100 km) i wyświetli informację o przewidywanym zużyciu paliwa oraz o
# szacowanych kosztach podróży (cena paliwa 6.5 zł/l).
#
#   A) Zmodyfikuj skrypt tak, aby długość przejechanej drogi była generowana losowo
#      (liczba całkowita z zakresu ), a użytkownik podawał aktualną cenę paliwa za litr.
#
#   B) Zmodyfikuj zadania 6 tak, aby wyświetlanie wyników wykorzystywało f-string.

import random

droga = random.randint(1, 100)
spalanie = float(input("Podaj średnie spalanie samochodu: "))
cenaPaliwa = float(input("Podaj aktualną cenę paliwa za litr: "))

zuzyciePaliwa = droga * spalanie / 100
kosztyPodrozy = zuzyciePaliwa * cenaPaliwa

print(f"Przejechana droga: {droga} km")
print(f"Przewidywane zużycie paliwa: {zuzyciePaliwa:.2f} litrów")
print(f"Aktualna cena paliwa: {cenaPaliwa} zł/l")
print(f"Szacowane koszty podróży: {kosztyPodrozy:.2f} zł")

# Przykład:
# Podaj średnie spalanie samochodu: 7.8
# Podaj aktualną cenę paliwa za litr: 6.99
# Przejechana droga: 92 km
# Przewidywane zużycie paliwa: 7.18 litrów
# Aktualna cena paliwa: 6.99 zł/l
# Szacowane koszty podróży: 50.16 zł
