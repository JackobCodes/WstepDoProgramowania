# Napisz programy, które:
# • Wczyta (zmienną) imię oraz wyświetli tekst „Witaj” oraz wczytane imię.
# • Wczyta (zmienną) wiek oraz wyświetli tekst „Twój wiek to: ” oraz wczytany
# wiek.
# • Wczyta (zmienne) imię i nazwisko i wyświetli inicjały.
# • Wczyta łańcuch i wyświetli go pięć razy.
# • Wczyta dwa łańcuchy, a w trzecim łańcuchu zapamięta połączone te dwa
# łańcuchy.
# • Wczyta dwa łańcuchy, a w trzecim łańcuchu zapamięta pierwszą połowę

imie = input('Podaj swoje imię: ')
print(f'Witaj {imie}')

wiek = int(input('Podaj swój wiek: '))
print(f"Twój wiek to: {wiek}")

nazwisko = input('Podaj swoje nazwisko: ')
print(f'Twoje inicjały to: {imie[0].upper()}.{nazwisko[0].upper()}.')

lancuch = input("Podaj jakiś łańcuch znaków: ")
print((lancuch + '\n') * 5)

lancuch1 = input('Podaj pierwszy łańcuch znaków: ')
lancuch2 = input('Podaj drugi łańcuch znaków: ')

polaczony_lancuch = lancuch1 + lancuch2
print(f'Połączony łańcuch: {polaczony_lancuch}')

polowa1 = lancuch1[:len(lancuch1) // 2]
polowa2 = lancuch2[:len(lancuch2) // 2]

polaczona_polowa = polowa1 + polowa2
print(f'Połączone połowy: {polaczona_polowa}')

# Podaj swoje imię: Jakub
# Witaj Jakub
#
# Podaj swój wiek: 21
# Twój wiek to: 21
#
# Podaj swoje nazwisko: Lewicki
# Twoje inicjały to: J.L.
#
# Podaj jakiś łańcuch znaków: Zadanie na laboratorium Wstęp do programowania
# Zadanie na laboratorium Wstęp do programowania
# Zadanie na laboratorium Wstęp do programowania
# Zadanie na laboratorium Wstęp do programowania
# Zadanie na laboratorium Wstęp do programowania
# Zadanie na laboratorium Wstęp do programowania
#
# Podaj pierwszy łańcuch znaków: Wstęp do programowania
# Podaj drugi łańcuch znaków: WSIZ
#
# Połączony łańcuch: Wstęp do programowaniaWSIZ
# Połączone połowy: Wstęp do prWS