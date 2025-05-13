base_datos = {
    "admin": "password",
    "eduardo": "drill272",
    "zaza": "dad",
    "hi": "hello",
    "silk": "song"
}


#def login(usuario:str, contraseña:str):
#if usuario in base_datos:
#    if contraseña == base_datos[usuario]:
#         print("Ingreso exitoso.")
#          return True
#       else:
#            print("Contraseña inaválida.")
#             return False
#      else:
#           print("Usuario no resgistrado")
#            return False

def main():
    user = input("Ingrese su nombre de usuario: ")
    password = input("Ingrese su contraseña: ")
    resultado = login(user, password)
    
    contador = 0
    while resultado == False:
        user = input("Ingrese su nombre de usuario: ")
        password = input("Ingrese su contraseña: ")
        resultado = login(user, password)
        if resultado == False:
            contador += 1
        elif contador == 3:
            print("Límite de intentos alcanzados.")
            break
       



if __name__ == "__main__":
    main()