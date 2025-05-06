'''''
from random import randint

lista =[]
for i in range(100):
    lista.append(randint(50, 90))
conjunto = set(lista)
'''''
from random import randint

lista1 = []
lista2 = []
for i in range(100):
    lista1.append(randint(0, 100))
    lista2.append(randint(50, 150))

conjunto1= set(lista1)
conjunto2 = set(lista2)

interseccion = conjunto1.intersection(conjunto2)
diferencia = conjunto1.difference(conjunto2)

list1 = list(interseccion)
list2 = list(diferencia)

print(f"iguales elementos {list1}")
print(f"diferentes elementos {list2}")