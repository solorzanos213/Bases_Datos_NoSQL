# Registro del entorno

## Sistema operativo
Windows

## Versiones
- Python: 3.14.6
- Git: 2.51.0.windows.2
- mongosh: 2.5.5
- MongoDB Server: pendiente por verificar

## Base de datos
emprendimiento_sena_lab

## Usuario
aprendiz_nosql

## Observaciones
Las versiones de Python, Git y mongosh fueron verificadas desde la terminal de VS Code.
La versión del servidor MongoDB se registrará después de establecer la conexión.

Predicción:
Se creará un segundo documento con el identificador ASE-DEMO-002.
La iniciativa cambiará a INI-DEMO-002, con nombre Sabores Locales
y sector alimentos.

Los tipos de datos se conservarán:
- _id: cadena
- emprendedor_alias: cadena
- iniciativa: subdocumento
- temas: arreglo
- modalidad: cadena
- estado: cadena
- requiere_seguimiento: booleano
- fecha_programada: Date
- fecha_realizacion: null

El conteo del documento ASE-DEMO-002 debe ser 1.
## Resultado de la segunda prueba

La ejecución creó correctamente el documento ASE-DEMO-002.

Los campos modificados fueron:
- _id: ASE-DEMO-002
- emprendedor_alias: Emprendedor ficticio 02
- iniciativa.codigo: INI-DEMO-002
- iniciativa.nombre: Sabores Locales
- iniciativa.sector: alimentos

Los demás campos conservaron el mismo tipo de dato:
- temas: arreglo
- modalidad: cadena
- estado: cadena
- requiere_seguimiento: booleano
- fecha_programada: Date
- fecha_realizacion: null

El conteo del documento ASE-DEMO-002 fue 1.

## Resultado de la segunda prueba

La ejecución creó correctamente el documento ASE-DEMO-002.

Los campos modificados fueron:
- _id: ASE-DEMO-002
- emprendedor_alias: Emprendedor ficticio 02
- iniciativa.codigo: INI-DEMO-002
- iniciativa.nombre: Sabores Locales
- iniciativa.sector: alimentos

Los demás campos conservaron el mismo tipo de dato:
- temas: arreglo
- modalidad: cadena
- estado: cadena
- requiere_seguimiento: booleano
- fecha_programada: Date
- fecha_realizacion: null

El conteo del documento ASE-DEMO-002 fue 1.

La predicción se cumplió correctamente.