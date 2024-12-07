# Załóżmy, że pracujesz nad systemem wojskowym dotyczącym planowania operacji wojskowych.
# Podana jest poniższa krotka:
# stopnie = (
#  "Szeregowy",
#  "Kapral",
#  "Sierżancie",
#  "Porucznik",
#  "Kapitan",
#  "Major",
#  "Pułkownik",
# )
# Wykonaj poniższe kroki:
# - wyznacz liczbę wszystkich stopni wojskowych i przypisz do zmiennej ilość_stopnii,
# -znajdź indeks krotki dla elementu "Major" i przypisz do zmiennej Major_index,
# -sprawdź, czy wartość "Pułkownik" znajduje się w krotce stopnie i przypisz do zmiennej
# Pułkownik_wstepowanie.
# W wydrukuj otrzymane zmienne do konsoli w podanej kolejności.

stopnie = (
 "Szeregowy",
 "Kapral",
 "Sierżancie",
 "Porucznik",
 "Kapitan",
 "Major",
 "Pułkownik",
)
ilosc_stopnii = len(stopnie)
major_index = stopnie.index('Major')
pulkownik_wstepowanie = 'Pułkownik' in stopnie

print(f'Ilość stopni wojskowych w krotce wynosi: {ilosc_stopnii}, index stopnia Major w krotce wynosi: {major_index}, czy stopień Półkownik występuje w krotce? {pulkownik_wstepowanie} ')
# Ilość stopni wojskowych w krotce wynosi: 7, index stopnia Major w krotce wynosi: 5, czy stopień Półkownik występuje w krotce? True
