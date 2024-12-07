# Napisz funkcję rekurencyjną, która poda n-ty wyraz ciągu Fibonacciego.
# *Ciąg Fibonacciego to sekwencja liczb, w której każdy wyraz (od trzeciego wzwyż) jest sumą
# dwóch poprzednich wyrazów. Formuła rekurencyjna dla n-tego wyrazu ciągu Fibonacciego
# jest następująca.

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

n = int(input("Podaj numer wyrazu ciągu Fibonacciego: "))
wynik = fibonacci(n)
print(f"{n}-ty wyraz ciągu Fibonacciego to: {wynik}")

# Podaj numer wyrazu ciągu Fibonacciego: 5
# 5-ty wyraz ciągu Fibonacciego to: 5