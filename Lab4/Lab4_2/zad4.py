# Napisz funkcję, obliczającą średnią z listy liczb. Zaprezentuj wywołanie funkcji.

def srednia():
    lista = [1, 5, 75, 74, 83, 12, 64]
    srednia_liczb = sum(lista) / len(lista)
    return srednia_liczb

print(srednia())
# 44.857142857142854