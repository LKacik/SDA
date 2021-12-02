import string
alfabet = string.ascii_letters
lista = []
przesuniecie = 2
for r in alfabet:
    lista.append(r)
# print(lista)
def szyfrCezar(haslo):
    for h in haslo:
        if h in lista:
            zmienna = lista.index(h) - przesuniecie
            print(lista[zmienna], end='')
szyfrCezar("Dom")