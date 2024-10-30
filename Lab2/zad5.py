# a)
# Odczytaj podany plik notwania_gieldowe.txt zawierający dane dotyczące notowań kilku spółek.
# Wydrukuj każdą linię do konsoli.
# b)
# Dopisz do pliku notwania_gieldowe.txt, w kolejnej linii dane dotyczące nowej spółki: ALR, 113.
# Wydrukuj każdą linię ponownie do konsoli.

with open('notowania_gieldowe.txt', 'a') as file:
    file.write('\nALR, 113')
with open('notowania_gieldowe.txt', 'r') as file:
    for line in file:
        print(line, end='')

# Odpowiedź podpunkt a:
# KGHM, 123
# Tauron, 150
# Orange, 45
# PGE, 24
# PKN Orlen, 70
# PKO BP,56

# Odpowiedź podpunkt b:
# KGHM, 123
# Tauron, 150
# Orange, 45
# PGE, 24
# PKN Orlen, 70
# PKO BP,56
#
# ALR, 113