from InstagramAPI import InstagramAPI
import time

if __name__ == "__main__":
    nombre = raw_input("Introduce tu nombre: ")
    contrasena = raw_input("Introduce tu contrasena: ")
    api = InstagramAPI(nombre, contrasena)
    api.login()

    user_id = api.username_id
