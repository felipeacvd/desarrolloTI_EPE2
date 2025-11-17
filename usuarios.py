import json
import csv

with open('usuarios.json', 'r', encoding='utf-8') as archivo_json:
    datos = json.load(archivo_json)

print("=== Análisis de Datos de Usuarios ===")
for usuario in datos:
    print(f"Usuario: {usuario['nombre']}")
    print(f" - Cantidad de visitas: {usuario['visitas']}")
    print(f" - Duración promedio: {usuario['duracion_promedio']} minutos")
    print(f" - Contenido más visitado: {usuario['contenido_mas_visitado']}")
    print("---------------------------------------")

with open('usuarios.csv', 'w', newline='', encoding='utf-8') as archivo_csv:
    encabezados = ['id_usuario', 'nombre', 'visitas', 'duracion_promedio', 'contenido_mas_visitado']
    escritor = csv.DictWriter(archivo_csv, fieldnames=encabezados)
    escritor.writeheader()
    escritor.writerows(datos)

print("Archivo 'usuarios.csv' generado correctamente.")