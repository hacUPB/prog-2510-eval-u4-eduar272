#Abrir archivo
p_archivo_datos = open("texto2.txt", "r")
peso = p_archivo_datos.readline()
estatura = p_archivo_datos.readline()

print(peso)
print(estatura)

p_archivo_datos.close()