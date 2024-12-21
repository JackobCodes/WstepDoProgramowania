# Napisz skrypt, która obliczy ile dni upłynęło od ostatnich
# laboratoriów oraz ile czasu zostało do kolokwium (17.12.2024).
# Niech wynik wyświetli się w
# przystępny sposób z nazwą miesiąca

from datetime import datetime

def oblicz_czas():
    ostatnie_laboratoria = input("Podaj datę ostatnich laboratoriów (RRRR-MM-DD): ")

    try:
        data_laboratoriow = datetime.strptime(ostatnie_laboratoria, "%Y-%m-%d").date()
        dzisiaj = datetime.now().date()

        data_kolokwium = datetime(2024, 12, 17).date()

        dni_od_laboratoriow = (dzisiaj - data_laboratoriow).days
        dni_do_kolokwium = (data_kolokwium - dzisiaj).days

        print(f"Od ostatnich laboratoriów ({data_laboratoriow.strftime('%d %B %Y')}) minęło: {dni_od_laboratoriow} dni.")
        print(f"Do kolokwium ({data_kolokwium.strftime('%d %B %Y')}) zostało: {dni_do_kolokwium} dni.")

    except ValueError:
        print("Błąd: Wprowadź datę w poprawnym formacie RRRR-MM-DD.")


oblicz_czas()

# Podaj datę ostatnich laboratoriów (RRRR-MM-DD): 2024-12-14
# Od ostatnich laboratoriów (14 December 2024) minęło: 3 dni.
# Do kolokwium (17 December 2024) zostało: 0 dni.