import os

ARCHIVO_MEMORIA = "memoria.txt"

# Crear archivo si no existe
if not os.path.exists(ARCHIVO_MEMORIA):
    open(ARCHIVO_MEMORIA, "w").close()

def guardar_en_memoria(texto):
    with open(ARCHIVO_MEMORIA, "a", encoding="utf-8") as f:
        f.write(texto + "\n")

def buscar_en_memoria(pregunta):
    with open(ARCHIVO_MEMORIA, "r", encoding="utf-8") as f:
        lineas = f.readlines()

    for linea in lineas:
        if pregunta.lower() in linea.lower():
            return linea.strip()

    return None

def ia():
    print("Pedus IA iniciada 😎")
    
    while True:
        usuario = input("Tú: ")

        if usuario.lower() == "salir":
            break

        # Buscar respuesta en memoria
        respuesta = buscar_en_memoria(usuario)

        if respuesta:
            print("IA:", respuesta)
        else:
            print("IA: No sé eso aún. Enséñame algo relacionado.")
            nueva_info = input("Escribe la información para aprender: ")
            guardar_en_memoria(nueva_info)
            print("IA: Aprendido ✔")

ia()

