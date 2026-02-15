from flask import Flask, request, jsonify, send_from_directory
import os

app = Flask(__name__)
ARCHIVO_MEMORIA = "memoria.txt"

# Crear memoria si no existe
if not os.path.exists(ARCHIVO_MEMORIA):
    open(ARCHIVO_MEMORIA, "w").close()

# Cargar memoria
def cargar_memoria():
    memoria = {}
    with open(ARCHIVO_MEMORIA, "r", encoding="utf-8") as f:
        for linea in f:
            if "|" in linea:
                pregunta, respuesta = linea.strip().split("|", 1)
                memoria[pregunta.lower()] = respuesta
    return memoria

# Guardar nueva pregunta/respuesta
def guardar_memoria(pregunta, respuesta):
    with open(ARCHIVO_MEMORIA, "a", encoding="utf-8") as f:
        f.write(f"{pregunta}|{respuesta}\n")

# Ruta principal
@app.route("/")
def home():
    return send_from_directory(".", "index.html")

# API para preguntar
@app.route("/preguntar", methods=["POST"])
def preguntar():
    data = request.json
    pregunta = data.get("pregunta", "").lower()
    memoria = cargar_memoria()
    respuesta = memoria.get(pregunta)
    if respuesta:
        return jsonify({"respuesta": respuesta})
    else:
        nueva_respuesta = data.get("respuesta")
        if nueva_respuesta:
            guardar_memoria(pregunta, nueva_respuesta)
            return jsonify({"respuesta": f"Aprendido: {nueva_respuesta}"})
        return jsonify({"respuesta": "No sé eso aún."})

if __name__ == "__main__":
    app.run(debug=True)
