# Napisz kalkulator, który wyświetli wyniki dodawania, odejmowania, mnożenia, dzielenia i
# potęgowania 2 liczb podanych przez użytkownika.

def kalkulator(a, b):
    print(f"Dodawanie: {a} + {b} = {a + b}")
    print(f"Odejmowanie: {a} - {b} = {a - b}")
    print(f"Mnożenie: {a} * {b} = {a * b}")
    print(f"Dzielenie: {a} / {b} = {a // b if b != 0  else 'Nie można dzielić przez zero!'}")
    print(f"Potęgowanie: {a} ** {b} = {a ** b}")

try:
    a = float(input("Podaj pierwsza liczbę: "))
    b = float(input("Podaj drugą liczbę: "))

    kalkulator(a, b)

except ValueError:
    print("Proszę podać poprawne liczby.")

# Przykład:
# Podaj pierwsza liczbę: 3
# Podaj drugą liczbę: 6
# Dodawanie: 3.0 + 6.0 = 9.0
# Odejmowanie: 3.0 - 6.0 = -3.0
# Mnożenie: 3.0 * 6.0 = 18.0
# Dzielenie: 3.0 / 6.0 = 0.0
# Potęgowanie: 3.0 ** 6.0 = 729.0