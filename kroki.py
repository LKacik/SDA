lista1 = [12,23]
lista2 = [24,34]

listaN1 = [1,2,2,3]
listaN2 = [2,4,3,4]


while listaN1[0] != listaN2[0]:
    listaN1[0] += 1
licznik1 = listaN1[0] - 1
#print(licznik1)

while listaN1[1] != listaN2[1]:
    listaN1[1] += 1
licznik2 = listaN1[1] - 2
#print(licznik2)

while listaN1[2] != listaN2[2]:
   listaN1[2] +=1
licznik3 = listaN1[2] - 2
#print(licznik3)

while listaN1[3] != listaN2[3]:
    listaN1[3] +=1
licznik4 = listaN1[3] - 3
#print(licznik4)

licznik = licznik1 + licznik2 + licznik3 + licznik4

print(f"Ilość  ruchów wynosi: {licznik}, ({licznik1}, {licznik2}, {licznik3}, {licznik4})")
