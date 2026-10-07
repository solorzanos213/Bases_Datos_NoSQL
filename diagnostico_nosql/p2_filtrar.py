iniciativas = [
    {"codigo": "INI-001", "sector": "tecnologia", "pendiente": True},
    {"codigo": "INI-002", "sector": "alimentos", "pendiente": True},
    {"codigo": "INI-003", "sector": "tecnologia", "pendiente": False},
    {"codigo": "INI-004", "sector": "tecnologia"}
]


def seleccionar_pendientes(registros, sector):
    resultados = []

    for iniciativa in registros:
        if iniciativa.get("sector") == sector and iniciativa.get("pendiente") is True:
            resultados.append(iniciativa["codigo"])

    return resultados


# Prueba con resultados
print("Tecnología:", seleccionar_pendientes(iniciativas, "tecnologia"))

# Prueba sin resultados
print("Economía circular:", seleccionar_pendientes(iniciativas, "economia_circular"))


# Explicación:
# Si el campo pendiente no existe, .get("pendiente") devuelve None.
# Por eso la iniciativa no se selecciona.
# No se debe confundir True con "True", porque True es booleano
# y "True" es una cadena de texto.