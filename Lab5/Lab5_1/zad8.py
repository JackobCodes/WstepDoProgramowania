# Sprawdź czy słowa: for, print, break, done, bad, są słowami kluczowymi

import keyword

słowa = ["for", "print", "break", "done", "bad"]

for słowo in słowa:
    if keyword.iskeyword(słowo):
        print(f"{słowo} jest słowem kluczowym.")
    else:
        print(f"{słowo} nie jest słowem kluczowym.")

# for jest słowem kluczowym.
# print nie jest słowem kluczowym.
# break jest słowem kluczowym.
# done nie jest słowem kluczowym.
# bad nie jest słowem kluczowym.