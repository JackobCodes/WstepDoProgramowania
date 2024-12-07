# Napisz funkcję, która na podstawie podanej wagi i wzrostu oblicza i zwraca wskaźnik BMI, a
# następnie informuje użytkownika w jakim jest zakresie.
# *Wskaźnika Body Mass Index (BMI) oblicza się na podstawie dwóch danych: wzrostu i
# aktualna masa ciała.
# Należy podzielić wagę wyrażoną w kilogramach przez wzrost podniesiony do kwadratu,
# wyrażony w metrach, czyli w skrócie BMI = kg / m2.
# Uzyskany wynik należy porównać z zakresami wartości BMI. Klasyfikacja BMI dla osób
# dorosłych wygląda następująco:
# • niedowaga – BMI poniżej 18,5. Tutaj rozróżnia się trzy podkategorie,
# • pożądana masa ciała – BMI od 18,5 do 24,9,
# • nadwaga – BMI od 25 do 29,9,
# • otyłość – BMI powyżej 30. Obecnie wyróżnia się otyłość I stopnia – od 30 do 34,9, II
# stopnia – od 35 do 39,9, oraz III stopnia – powyżej 40.

def bmi(waga, wzrost):
    wynik_bmi = waga / wzrost ** 2
    wynik_bmi = round(wynik_bmi, 2)
    if wynik_bmi < 18.5:
        print(f'Twoje BMI wynosi: {wynik_bmi}, Niedowaga')
    elif wynik_bmi >= 18.5 and wynik_bmi < 25:
        print(f'Twoje BMI wynosi: {wynik_bmi}, Pożądna masa ciała')
    elif wynik_bmi >= 25 and wynik_bmi < 30:
        print(f'Twoje BMI wynosi: {wynik_bmi}, Nadwaga')
    elif wynik_bmi >= 30:
        if wynik_bmi >= 30 and wynik_bmi <= 35:
            print(f'Twoje BMI wynosi: {wynik_bmi}, Otyłość I stopnia')
        elif wynik_bmi >= 35 and wynik_bmi <= 40:
            print(f'Twoje BMI wynosi: {wynik_bmi}, Otyłość II stopnia')
        elif wynik_bmi >= 40:
            print(f'Twoje BMI wynosi: {wynik_bmi}, Otyłość III stopnia')


podana_waga = float(input('Podaj swoją wagę: '))
podany_wzrost = float(input('Podaj swój wzrost w metrach: '))
bmi(podana_waga, podany_wzrost)

# Podaj swoją wagę: 80.6
# Podaj swój wzrost w metrach: 1.84
# Twoje BMI wynosi: 23.81, Pożądna masa ciała