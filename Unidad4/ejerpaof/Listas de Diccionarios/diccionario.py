'''
frase = "la deteccion de cuerpos extraños"
palabras = frase.lower().split()
print(palabras)
frecuencia = {}

for palabra in palabras:
    if palabra in frecuencia:
        frecuencia[palabra] += 1
    else:
        frecuencia[palabra] = 1

print(frecuencia)  # {'hola': 2, 'mundo': 1, 'python': 1}
'''
usuarios = {
    "user1": {"nombre": "Ana", "edad": 25},
    "user2": {"nombre": "Luis", "edad": 30}
}

print(usuarios["user1"]["edad"])

user3 = {}
nombre = input("Porfavor ingrese su nombre:  ")
edad = int(input("Porfavo ringrese su edad:  ")) 
user3["nombre"] = nombre
user3["edad"] = edad
print(user3)
usuarios["user3"] = user3
print(usuarios)