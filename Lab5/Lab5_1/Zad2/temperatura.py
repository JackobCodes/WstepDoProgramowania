# Stwórz moduł temperatura.py, który będzie zawierał trzy funkcje do przeliczania
# temperatur:
# 1. c_to_f(celsius) – funkcję, która przelicza temperaturę z Celsjusza na Fahrenheita z
# wzoru:
# 2. f_to_c(fahrenheit) – funkcję, która przelicza temperaturę z Fahrenheita na
# Celsjusza z wzoru:
# 3. c_to_k, która przelicza temperaturę z Celsjusza na Kelwiny wiedząc, że do temperatury w
# stopniach Celsiusa należy dodać 273.15 aby otrzymać temperaturę w stopniach Kelwina.
# Następnie w osobnym pliku (np. pogoda.py) zaimportuj moduł temperatura i użyj obu
# funkcji do przeliczenia temperatur:
# • 21 stopni Celsjusza na Fahrenheita.
# • 89 stopni Fahrenheita na Celsjusza.
# • 35 stopni Celsjusza na Kelwiny.
# Wyświetl wyniki na ekranie.


def c_to_f(celsius):
    return celsius * 9/5 + 32

def f_to_c(fahrenheit):
    return (fahrenheit - 32) * 5/9

def c_to_k(celsius):
    return celsius + 273.15