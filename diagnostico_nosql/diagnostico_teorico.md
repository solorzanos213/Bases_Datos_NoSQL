# Diagnóstico teórico - Bases de Datos NoSQL

## 1. Tabla, fila y clave primaria
Una tabla es una estructura donde se organizan datos relacionados, por ejemplo una tabla llamada iniciativas.  
Una fila representa un registro específico, por ejemplo una iniciativa llamada EcoEmpaque.  
La clave primaria es un campo que identifica de manera única cada fila, por ejemplo el id de la iniciativa.

## 2. Clave foránea
Una clave foránea sirve para relacionar una tabla con otra.  
Por ejemplo, una iniciativa puede tener un emprendedor_id que haga referencia al id de un emprendedor.

Si una iniciativa hace referencia a un emprendedor que no existe, se genera un problema de integridad porque la relación apunta a un registro inexistente.

## 3. Consulta SELECT
La consulta:

SELECT codigo FROM iniciativas WHERE sector = 'tecnologia';

devuelve los códigos de las iniciativas cuyo sector sea tecnologia.

Esta consulta no modifica los datos, solo los consulta.

## 4. Lista y diccionario en Python
Una lista sirve para guardar varios elementos en una misma estructura.

Un diccionario guarda información usando claves y valores.

Para representar una iniciativa usaría un diccionario porque permite guardar datos como codigo, nombre, sector y estado.

Para representar varias iniciativas usaría una lista de diccionarios.

## 5. Booleanos en JSON
No son equivalentes.

false es un valor booleano.

"false" es una cadena de texto porque está entre comillas.

Aunque visualmente se parezcan, tienen tipos de datos diferentes.

## 6. Campo ausente, null y cadena vacía
Un campo ausente significa que la clave no existe dentro del documento.

Un campo con null significa que la clave existe pero no tiene un valor definido.

Una cadena vacía "" significa que el campo existe y su valor es texto, pero sin contenido.

Ejemplo:

Campo ausente:
{
  "codigo": "INI-001"
}

Campo con null:
{
  "codigo": "INI-001",
  "fecha_realizacion": null
}

Cadena vacía:
{
  "codigo": "INI-001",
  "descripcion": ""
}

## 7. Funciones que retornan datos
Una función que retorna datos permite usar el resultado después en otra parte del programa, por ejemplo guardarlo en una variable o usarlo en otra función.

Una función que solamente imprime muestra el resultado en pantalla, pero no permite reutilizarlo directamente.

## 8. Error al leer un archivo JSON
Antes de cambiar el programa revisaría si el archivo existe, si la ruta es correcta y si la sintaxis del JSON está bien escrita.

También revisaría que use comillas dobles, que los booleanos estén escritos como true o false y que no existan comas adicionales.

## 9. Fechas y formato ISO
2026-10-06T13:00:00Z representa una fecha y hora en formato ISO.

Indica el 6 de octubre de 2026 a las 13:00 horas en UTC.

La Z indica que la hora está expresada en UTC.

Este formato evita ambigüedades que pueden ocurrir con algo como 06/10/26 8:00, porque no siempre queda claro el orden de día, mes, año ni la zona horaria.

## 10. Contraseña publicada en Git
Si una contraseña fue publicada por error en Git, no es suficiente borrarla solamente del archivo actual.

Se debe cambiar o rotar la contraseña, revisar el historial del repositorio y eliminar la información sensible si es necesario.

También se debe agregar el archivo que contiene credenciales al .gitignore y evitar volver a publicar contraseñas o datos sensibles.

## Autoevaluación

Puedo realizar:
Puedo trabajar con estructuras básicas de Python, interpretar consultas SQL sencillas y corregir errores básicos en archivos JSON.

Necesito reforzar:
Necesito reforzar el manejo de relaciones entre tablas, la sintaxis de JSON y los conceptos de bases de datos NoSQL.

Mi primera acción de mejora será:
Repasar los conceptos principales de SQL, JSON y los diferentes modelos de bases de datos NoSQL para comprender mejor las siguientes actividades.