# Napisz skrypt, który pobiera długości boków prostokąta, a następnie oblicza jego pole i obwód
# oraz wyświetla wyniki na ekranie.
dlugosc = float(input("Podaj długość prostokąta: "))
szerokosc = float(input("Podaj szerokość prostokąta: "))

pole = dlugosc * szerokosc
obwod = 2 * (dlugosc + szerokosc)

print(f"Pole prostokąta wynosi: {pole}")
print(f"Obwód prostokąta wynosi: {obwod}")

# Przykład:
# Podaj długość prostokąta: 4
# Podaj szerokość prostokąta: 14.6
# Pole prostokąta wynosi: 58.4
# Obwód prostokąta wynosi: 37.2