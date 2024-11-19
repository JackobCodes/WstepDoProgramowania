# Napisz pętlę nieskończoną, w której użytkownik podaje liczby całkowite. W przypadku liczby ujemnej,
# następuję wyjście z pętli.

while True:
    liczba = int(input("Podaj Liczbę całkowitą (podanie liczby ujemnej kończy program): "))
    if liczba < 0:
        print("Podano liczbę ujemną. Koniec pętli.")
        break
    print(f"Podano liczbę: {liczba}")

# Podaj Liczbę całkowitą (podanie liczby ujemnej kończy program): 13
# Podano liczbę: 13
# Podaj Liczbę całkowitą (podanie liczby ujemnej kończy program): 66
# Podano liczbę: 66
# Podaj Liczbę całkowitą (podanie liczby ujemnej kończy program): -8
# Podano liczbę ujemną. Koniec pętli.