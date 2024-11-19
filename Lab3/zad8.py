# Wyświetl z łańcucha tekst ="Python jest super" znaki o indeksach:
# • Zerowym
# • Ostatnim
# • Co drugi, zaczynając od zerowego
# • Co trzeci zaczynając od pierwszego
# • Od dziesiątego do ostatniego
# • Wyświetl od końca do początku

tekst = 'Python jest super'

print('Zerowy znak:', tekst[0])
print('Ostatni znak:', tekst[-1])
print('Co drugi znak od zerowego:', tekst[::2])
print('Co trzeci znak od pierwszego:', tekst[1::3])
print('Od dziesiątego do ostatniego:', tekst[10:])
print('Od końca do początku:', tekst[::-1])

# Zerowy znak: P
# Ostatni znak: r
# Co drugi znak od zerowego: Pto etspr
# Co trzeci znak od pierwszego: yojtur
# Od dziesiątego do ostatniego: t super
# Od końca do początku: repus tsej nohtyP