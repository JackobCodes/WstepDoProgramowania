# Wyświetl wszystkie nazwy funkcji zawartych w modułach: math, tuple, keyword

import math
import keyword

print("\nFunkcje w obiekcie 'math':")
for nazwa in dir(math):
    if callable(getattr(math, nazwa)) and not nazwa.startswith("__"):
        print(nazwa)


print("\nFunkcje w obiekcie 'tuple':")
for nazwa in dir(tuple):
    if callable(getattr(tuple, nazwa)) and not nazwa.startswith("__"):
        print(nazwa)


print("\nFunkcje w module 'keyword':")
for nazwa in dir(keyword):
    if callable(getattr(keyword, nazwa)) and not nazwa.startswith("__"):
        print(nazwa)


# Funkcje w obiekcie 'math':
# acos
# acosh
# asin
# asinh
# atan
# atan2
# atanh
# ceil
# comb
# copysign
# cos
# cosh
# degrees
# dist
# erf
# erfc
# exp
# expm1
# fabs
# factorial
# floor
# fmod
# frexp
# fsum
# gamma
# gcd
# hypot
# isclose
# isfinite
# isinf
# isnan
# isqrt
# lcm
# ldexp
# lgamma
# log
# log10
# log1p
# log2
# modf
# nextafter
# perm
# pow
# prod
# radians
# remainder
# sin
# sinh
# sqrt
# tan
# tanh
# trunc
# ulp
#
# Funkcje w obiekcie 'tuple':
# count
# index
#
# Funkcje w module 'keyword':
# iskeyword
# issoftkeyword