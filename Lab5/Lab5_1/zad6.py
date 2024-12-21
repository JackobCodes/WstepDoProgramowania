# Napisz program „sekundnik”, który prze określony przez użytkownika czas będzie wyświetlał
# liczbę sekund pozostałą do końca.

import time

def sekundnik():
    try:
        czas = int(input("Podaj liczbę sekund do odliczenia: "))

        if czas <= 0:
            print("Czas musi być większy od zera!")
            return

        print(f"Rozpoczynam odliczanie {czas} sekund.")

        while czas > 0:
            print(f"Pozostało: {czas} sekund")
            time.sleep(1)
            czas -= 1

        print("Czas minął!")
    except ValueError:
        print("Błąd: Podaj poprawną liczbę całkowitą.")

sekundnik()

# Podaj liczbę sekund do odliczenia: 5
# Rozpoczynam odliczanie 5 sekund.
# Pozostało: 5 sekund
# Pozostało: 4 sekund
# Pozostało: 3 sekund
# Pozostało: 2 sekund
# Pozostało: 1 sekund
# Czas minął!