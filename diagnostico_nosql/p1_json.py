import json

texto = '{"codigo":"INI-001", "activa":true, "intereses":["Validar mercado"]}'

datos = json.loads(texto)

print("Código:", datos["codigo"])
print("Activa:", datos["activa"])
print("Tipo de código:", type(datos["codigo"]).__name__)
print("Tipo de activa:", type(datos["activa"]).__name__)

# Explicación:
# El JSON inicial tenía True, pero en JSON los booleanos se escriben
# como true o false en minúscula.
# También había una coma sobrante después de "Validar mercado".
# Después de corregir estos errores, json.loads puede leer el JSON.