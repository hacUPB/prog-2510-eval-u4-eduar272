import csv

with open('ejemplo.csv', 'r') as csvfile:   #usamos el manejador de contexto
    lector = csv.reader(csvfile, delimiter=";") #se utiliza el método reader
    encabezado = next(lector)
    print(encabezado[6])
    for fila in lector:          #con el for se itera sobre el objeto para leer
        print(fila[6])