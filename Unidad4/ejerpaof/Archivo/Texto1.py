nombre = input("Ingrese su nombre:  ")
edad = int(input("Ingrse su edad:  "))
cedula = input("Ingrese su Cédula:  ")

#Abrir un archivo
var_archivo = open("C:\\Users\\B09S202est\\Desktop\\Texto1.txt","w")
var_archivo.write(f"{nombre} con cédula {cedula} tiene {edad} años\n")

var_archivo.close() #Cerrar el archivo
#crear el archivo en el Escritorio