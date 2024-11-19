# Napisz program, który będzie kontrolować zużycie paliwa w samolocie. Przed rozpoczęciem każdej
# jednostki czasu wydrukuj do konsoli informację o pozostałych jednostkach paliwa. Gdy paliwo
# zostanie wyczerpane, wydrukuj do konsoli informacje 'Konie lotu.'.
# Masz do dyspozycji następujące dane.:
# • ilość paliwa w samolocie w litrach
# • ilość paliwa zużywanego na sekundę w litrach
# • czas lotu w sekunadach
# Wartości początkowe:
# • paliwo = 100
# • paliwo_zużyte_na_s = 10
# • czas = 0


paliwo = 100
paliwo_zuzyt_na_s = 10
czas = 0

while paliwo > 0:
    print(f'Pozostała ilość paliwa: {paliwo}l, czas lotu: {czas}')
    paliwo -= paliwo_zuzyt_na_s
    czas += 1
else:
    print(f'Koniec lotu. Lot trwał: {czas} sekund')


# Pozostała ilość paliwa: 100l, czas lotu: 0
# Pozostała ilość paliwa: 90l, czas lotu: 1
# Pozostała ilość paliwa: 80l, czas lotu: 2
# Pozostała ilość paliwa: 70l, czas lotu: 3
# Pozostała ilość paliwa: 60l, czas lotu: 4
# Pozostała ilość paliwa: 50l, czas lotu: 5
# Pozostała ilość paliwa: 40l, czas lotu: 6
# Pozostała ilość paliwa: 30l, czas lotu: 7
# Pozostała ilość paliwa: 20l, czas lotu: 8
# Pozostała ilość paliwa: 10l, czas lotu: 9
# Koniec lotu. Lot trwał: 10 sekund
