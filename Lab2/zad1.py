# Napisz prosty program, który na podstawie podanej przez Studenta liczby zdobytych punktów,
# poinformuje go o rezultacie egzaminu.
# Każdy Student, który zdobył powyżej 80 punktów zalicza egzamin w terminie 0
# Studenci którzy otrzymali liczbę punków z przedziału 50-80, mogą poprawić jego wynik.
# Studenci, którzy zdobyli poniżej 50 punktów, muszą go poprawić.

x = float(input('Podaj liczbę zdobytych puntków: '))

if x > 80:
    print(f'Zaliczyłeś egzamin w terminie 0 z liczbą puntków: {x}')
elif 50 <= x <= 80:
    print(f'Zaliczyłeś egzamin z liczbą puntków {x}. Jeżeli wynik Cię nie satysfakcjonuje możesz go poprawić.')
else:
    print(f'Niestety nie zaliczyłeś egzaminu. Twoja liczba punktów wynosi: {x}.')


# Przykład:
# Podaj liczbę zdobytych puntków: 56
# Zaliczyłeś egzamin z liczbą puntków 56.0. Jeżeli wynik Cię nie satysfakcjonuje możesz go poprawić.
