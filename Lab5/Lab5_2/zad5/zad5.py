# Stwórz DataFrame z danymi studentów (nr_albumu, imię, nazwisko, oceny z
# kolokwium), Następnie:
# a. Wybierz studentów, którzy mają ocenę większą niż 4.
# b. Posortuj studentów według wieku.
# c. Zgrupuj studentów według ocen i oblicz średnią wieku w każdej grupie.
# d. Utwórz ramkę danych protokołu ocen z poprawy a następnie połacz ją z ramką
# pierwszego terminu na podstawie wspólnego klucza (jakiego?).
# e. Zapisz przygotowany DataFrame do pliku CSV.
# f. Wczytaj dane z pliku CSV i sprawdź poprawność wczytania.
# g. Dodaj nowego studenta do istniejącego DataFrame.
# h. Znajdź unikalne wartości w kolumnie z ocenami.
# i. Sprawdź, ile studentów ma ocenę równą 5
# Dane:
# 1. Nr_albumu: 1, 2, 3, 4, 5
# 2. Imię: Anna, Jan, Katarzyna, Tomasz, Michał
# 3. Nazwisko: Kowalska, Nowak, Wiśniewska, Kaczmarek, Zieliński
# 4. Ocena: 4.5, 3.0, 5.0, 4.0, 2.5,
# 5. WiekS: [22, 21, 24, 23, 25]

import pandas as pd

nr_albumu = [1, 2, 3, 4, 5]
imiona = ['Anna', 'Jan', 'Katarzyna', 'Tomasz', 'Michał']
nazwiska = ['Kowalska', 'Nowak', 'Wiśniewska', 'Kaczmarek', 'Zieliński']
oceny = [4.5, 3.0, 5.0, 4.0, 2.5]
wiek = [22, 21, 24, 23, 25]

studenci = pd.DataFrame({
    'Nr_albumu': nr_albumu,
    'Imię': imiona,
    'Nazwisko': nazwiska,
    'Ocena': oceny,
    'Wiek': wiek
})

studenci_ocena_wieksza_niz_4 = studenci[studenci['Ocena'] > 4]
print("Studenci z oceną większą niż 4:")
print(studenci_ocena_wieksza_niz_4)

# Studenci z oceną większą niż 4:
#    Nr_albumu       Imię    Nazwisko  Ocena  Wiek
# 0          1       Anna    Kowalska    4.5    22
# 2          3  Katarzyna  Wiśniewska    5.0    24


studenci_posortowani_wiek = studenci.sort_values(by='Wiek')
print("Studenci posortowani według wieku:")
print(studenci_posortowani_wiek)

# Studenci posortowani według wieku:
#    Nr_albumu       Imię    Nazwisko  Ocena  Wiek
# 1          2        Jan       Nowak    3.0    21
# 0          1       Anna    Kowalska    4.5    22
# 3          4     Tomasz   Kaczmarek    4.0    23
# 2          3  Katarzyna  Wiśniewska    5.0    24
# 4          5     Michał   Zieliński    2.5    25


srednia_wiek_wedlug_ocen = studenci.groupby('Ocena')['Wiek'].mean()
print("Średnia wieku według ocen:")
print(srednia_wiek_wedlug_ocen)

# Średnia wieku według ocen:
# Ocena
# 2.5    25.0
# 3.0    21.0
# 4.0    23.0
# 4.5    22.0
# 5.0    24.0
# Name: Wiek, dtype: float64


oceny_poprawa = pd.DataFrame({
    'Nr_albumu': [1, 2, 3, 4, 5],
    'Ocena_poprawa': [5.0, 3.5, 5.0, 4.5, 3.0]
})
studenci_polaczeni = pd.merge(studenci, oceny_poprawa, on='Nr_albumu')
print("Studenci po połączeniu z ocenami poprawy:")
print(studenci_polaczeni)

# Studenci po połączeniu z ocenami poprawy:
#    Nr_albumu       Imię    Nazwisko  Ocena  Wiek  Ocena_poprawa
# 0          1       Anna    Kowalska    4.5    22            5.0
# 1          2        Jan       Nowak    3.0    21            3.5
# 2          3  Katarzyna  Wiśniewska    5.0    24            5.0
# 3          4     Tomasz   Kaczmarek    4.0    23            4.5
# 4          5     Michał   Zieliński    2.5    25            3.0


sciezka_csv = 'studenci.csv'
studenci_polaczeni.to_csv(sciezka_csv, index=False)
print(f"Dane zapisane do pliku: {sciezka_csv}")

# Dane zapisane do pliku: studenci.csv


wczytane_dane = pd.read_csv(sciezka_csv)
print("Wczytane dane z pliku CSV:")
print(wczytane_dane)

# Wczytane dane z pliku CSV:
#    Nr_albumu       Imię    Nazwisko  Ocena  Wiek  Ocena_poprawa
# 0          1       Anna    Kowalska    4.5    22            5.0
# 1          2        Jan       Nowak    3.0    21            3.5
# 2          3  Katarzyna  Wiśniewska    5.0    24            5.0
# 3          4     Tomasz   Kaczmarek    4.0    23            4.5
# 4          5     Michał   Zieliński    2.5    25            3.0


nowy_student = pd.DataFrame({
    'Nr_albumu': [6],
    'Imię': ['Paweł'],
    'Nazwisko': ['Kowal'],
    'Ocena': [3.5],
    'Wiek': [20]
})
studenci_rozszerzeni = pd.concat([studenci, nowy_student], ignore_index=True)
print("Dodano nowego studenta:")
print(studenci_rozszerzeni)

# Dodano nowego studenta:
#    Nr_albumu       Imię    Nazwisko  Ocena  Wiek
# 0          1       Anna    Kowalska    4.5    22
# 1          2        Jan       Nowak    3.0    21
# 2          3  Katarzyna  Wiśniewska    5.0    24
# 3          4     Tomasz   Kaczmarek    4.0    23
# 4          5     Michał   Zieliński    2.5    25
# 5          6      Paweł       Kowal    3.5    20


unikalne_oceny = studenci['Ocena'].unique()
print("Unikalne wartości w kolumnie z ocenami:")
print(unikalne_oceny)

# Unikalne wartości w kolumnie z ocenami:
# [4.5 3.  5.  4.  2.5]


liczba_studentow_ocena_5 = len(studenci[studenci['Ocena'] == 5.0])
print("Liczba studentów z oceną równą 5:")
print(liczba_studentow_ocena_5)

# Liczba studentów z oceną równą 5:
# 1