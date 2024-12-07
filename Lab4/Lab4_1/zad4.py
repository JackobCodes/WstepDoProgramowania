# Napisz program, który wczyta od użytkownika zdanie. Wypisz z niego wszystkie litery w kolejności
# alfabetycznej, a następnie wypisze których litera alfabetu nie zawiera.

import string

text = input("Napisz zdanie: ").lower()
letters = sorted(set(filter(str.isalpha, text)))
alphabet = set(string.ascii_lowercase)
missing_letters = sorted(alphabet - set(letters))

print("Litery w zdaniu w kolejności alfabetycznej:")
print(" ".join(letters))

print("Litery, których brakuje w zdaniu:")
print(" ".join(missing_letters))

# Napisz zdanie: Programowanie jest super!
# Litery w zdaniu w kolejności alfabetycznej:
# a e g i j m n o p r s t u w
# Litery, których brakuje w zdaniu:
# b c d f h k l q v x y z