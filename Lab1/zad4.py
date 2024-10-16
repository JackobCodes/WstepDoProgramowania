# Do zmiennej Cena przypisz cenę produktu równą 39.99 PLN oraz do zmiennej Rabat przypisz
# # wartość 0.2 (rabat 20%). Następnie policz cenę tego produktu po zastosowaniu podanego
# # rabatu. Wynik wydrukuj do konsoli. Zwróć uwagę na odpowiednie formatowanie tekstu w
# # funkcji print() tak, aby końcowa cena produktu została wyświetlona tylko do drugiego
# # miejsca po przecinku.

cena = 39.99
rabat = 0.2

cenaPoRabacie = cena * (1 - rabat)

print(f"Cena produktu po rabacie: {cenaPoRabacie:.2f} PLN")
# Cena produktu po rabacie: 31.99 PLN