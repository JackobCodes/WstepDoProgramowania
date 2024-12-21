# Napisz program, który:
# A. Wylosuje „Twoją szczęśliwą liczbę”.
# B. Zdefiniuj tablicę, której elementami będą roczniki urodzenia wszystkich osób w grupie.
# Wylosuj szczęśliwy rocznik.

import random

print(f'Twoja szczęśliwa liczba to: {random.randint(1, 100)}')

# Twoja szczęśliwa liczba to: 30


roczniki = [1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007]

print(f'Szęśliwy rocznik to: {random.choice(roczniki)}')

# Szęśliwy rocznik to: 2004
