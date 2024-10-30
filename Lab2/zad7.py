# Podana jest poniższa zmienna przechowująca ciąg znaków - hasło:
# Hasło = 'pk47!jy0893'

# Sprawdź, czy podane hasło ma wymaganą długość 11 znaków oraz zwiera znak specjalny '!'. Jeżeli tak,
# wydrukuj do konsoli „Hasło jest poprawne”, w przeciwnym razie „Hasło jest nie poprawne”.


Hasło = 'pk47!jy0893'

if len(Hasło) >= 11 and '!' in Hasło:
    print('Hasło jest poprawne')
else:
    print('Hasło jest nie poprawne')

# Odpowiedź:
# Hasło jest poprawne