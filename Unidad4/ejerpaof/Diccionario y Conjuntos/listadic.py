# Lista global para almacenar los diccionarios de personas
personas = []

def agregar_persona(nombre:str, edad:str, ciudad:str):
    persona = {
        'nombre': nombre,
        'edad': edad,
        'ciudad': ciudad
    }

    personas.append(persona)
    print(f"Diciionario: {personas[0]}")
    print(f"personas: {personas[1]["nombre"]}")    



def main():
    name = input("Ingrese el nombre:  ")
    age = int(input("Ingrese la edad:  "))
    city = input("Ingrese la ciudad:  ")

    agregar_persona(name, age, city)
    agregar_persona("Juan", 18, "Medellín")
    print(f"Diciionario: {personas[0]}")
    print(f"personas: {personas[1]["nombre"]}")

    for usuario in personas:
        if usuario["eadad"] > 18: #sirve para imprimir datos que tienen cosas en comun, separandolos por caracteriticas especificas de cada uno, sirve para manejar basesde datos grandes  
            print(usuario["nombre"])

if __name__== "__main__":
    pass