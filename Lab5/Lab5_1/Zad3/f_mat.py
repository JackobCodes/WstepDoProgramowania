# Stwórz dwa pliki w języku Python: f_mat.py oraz ćwiczenia.py. Plik f_mat.py będzie
# zawierał funkcje do wykonywania prostych operacji matematycznych, natomiast
# ćwiczenia.py posłuży do przetestowania tych funkcji.
# W pliku f_mat.py zaimplementuj trzy funkcje:
# • kwadrat(x): funkcja przyjmuje liczbę x i zwraca jej kwadrat,
# • szescian(x): funkcja przyjmuje liczbę x i zwraca jej sześcian,
# • dodaj(a, b): funkcja przyjmuje dwie liczby a i b i zwraca ich sumę.
# •
# W pliku ćwiczenia.py zaimportuj funkcje z modułu f_mat.py na dwa sposoby:
# A. import całego modułu f_mat i wywoływanie funkcji z prefiksem f_mat.
# B. import tylko wybranych funkcji (kwadrat, szescian, dodaj)
# W obu przypadkach wykonaj następujące operacje:
# • oblicz kwadrat liczby 10, wywołując funkcję kwadrat(10).
# • oblicz sześcian liczby 3, wywołując funkcję szescian(3).
# • dodaj liczby 10 i 5, wywołując funkcję dodaj(10, 5).
# Wyświetl wyniki tych operacji na konsoli.

def kwadrat(x):
    return x**2

def szczescian(x):
    return x**3

def dodaj(a, b):
    return a+b
