# Napisz funkcję, która oblicza pole trójkąta o boku a, b ,c. Pamiętaj o zabezpieczeniu funkcji przed
# błędnymi danymi i wyjątkami. Użyj wzoru Herona.
# * Do obliczenia pola trójkąta o bokach a, b, c można użyć wzoru Herona:
# gdzie s to połowa obwodu trójkąta (tzw. Półobwód):
# Do sprawdzenia poprawności danych wprowadzanych przez użytkownika zastosuj strukturę
# Try & Except
# try:
# # Kod, który potencjalnie może wywołać wyjątek
# except ExceptionType:
# # Kod do wykonania, jeśli wystąpi wyjątek typu ExceptionType

import math

def pole_trojkata(a, b, c):
    try:
        if a <= 0 or b <= 0 or c <= 0:
            raise ValueError("Boki trójkąta muszą być większe od zera.")

        if a + b <= c or a + c <= b or b + c <= a:
            raise ValueError("Boki trójkąta nie spełniają warunków istnienia trójkąta.")

        s = (a + b + c) / 2

        pole = math.sqrt(s * (s - a) * (s - b) * (s - c))

        return round(pole, 2)

    except ValueError as e:
        return f"Błąd: {e}"
    except Exception as e:
        return f"Wystąpił nieoczekiwany błąd: {e}"


try:
    a = float(input("Podaj długość pierwszego boku trójkąta: "))
    b = float(input("Podaj długość drugiego boku trójkąta: "))
    c = float(input("Podaj długość trzeciego boku trójkąta: "))

    wynik = pole_trojkata(a, b, c)
    print(f"Pole trójkąta wynosi: {wynik}")
except ValueError:
    print("Podano niepoprawną wartość. Użyj liczb.")

# Podaj długość pierwszego boku trójkąta: 12
# Podaj długość drugiego boku trójkąta: 5
# Podaj długość trzeciego boku trójkąta: 9
# Pole trójkąta wynosi: 20.4
