# Napisz program, który:
# a. Wczyta (zmienną) imię oraz wyświetli tekst „Witaj” oraz wczytane imię.
# b. Wczyta (zmienną) wiek oraz wyświetli tekst „Twój wiek to:” oraz wczytany wiek.
# c. Wczyta (zmienne) imię i nazwisko i wyświetli inicjały.
# d. Wczyta łańcuch i wyświetli go pięć razy.
# e. Wczyta dwa łańcuchy, a w trzecim łańcuchu zapamięta połączone te dwa łańcuchy.
# f. Wczyta dwa łańcuchy, a w trzecim łańcuchu zapamięta pierwszą połowę pierwszego i drugą połowę
# drugiego.

name = input('Podaj swoje imię: ')
print(f' Witaj {name}')
# Podaj swoje imię: Jakub
#  Witaj Jakub

age = int(input('Podaj swój wiek: '))
print(f'Twój wiek to: {age}')
# Podaj swój wiek: 21
# Twój wiek to: 21

firstName = input('Podaj swoje imię: ')
lastName = input('Podaj swoje nazwisko: ')
print(f'Twoje inicjały to {firstName[0]}.{lastName[0]}.')
# Podaj swoje imię: Jakub
# Podaj swoje nazwisko: Lewicki
# Twoje inicjały to J.L

text = input('Podaj ciąg znaków: ')
print((text + '\n') * 5 )
# Podaj ciąg znaków: Wstep do programowania
# Wstep do programowania
# Wstep do programowania
# Wstep do programowania
# Wstep do programowania
# Wstep do programowania

text1 = input('Podaj pierwszy ciąg znaków: ')
text2 = input('Podaj drugi ciąg znaków: ')

allText = text1 + text2
print(f'Połączony ciąg znaków: {allText}')

half1 = text1[:len(text1) // 2]
half2 = text2[:len(text2) // 2]

allHalftext = half1 + half2
print(f'Połączone połowy: {allHalftext}')

# Podaj pierwszy ciąg znaków: programowanie
# Podaj drugi ciąg znaków: jest super!
# Połączony ciąg znaków: programowaniejest super!
# Połączone połowy: prograjest