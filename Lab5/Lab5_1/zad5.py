# Napisz program, który przeprowadzi losowanie "Dużego Lotka". Skrypt ma wylosować 6 kul
# spośród liczb 1 do 49. Wygeneruj listę 1 do 49 (range). Poszukaj informacji na temat
# random.sample() i zasymiluj losowanie totolotka.

import random

def duzy_lotek_losowanie():
    liczby = list(range(1, 50))

    wylosowane_liczby = random.sample(liczby, 6)

    print(f"Wylosowane liczby w Dużym Lotku to: {wylosowane_liczby}")

duzy_lotek_losowanie()

# Wylosowane liczby w Dużym Lotku to: [35, 36, 31, 7, 24, 3]
