p_archivo_datos = open("texto2.txt","r")
archivo_imc = open("Imc.txt","a")
for i in range(5):
    peso = int(p_archivo_datos.readline())
    estatura = float(p_archivo_datos.readline())
    imc = peso/estatura^2
    archivo_imc.write(str(imc)+"\n")
p_archivo_datos.close()
archivo_imc.close()