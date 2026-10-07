# Bases de Datos NoSQL - Semana 1

## Descripción

Este proyecto corresponde a la Semana 1 de la guía de aprendizaje de Bases de Datos NoSQL.

El caso trabajado está basado en una Unidad de Emprendimiento del SENA, donde se busca organizar información relacionada con emprendedores, iniciativas y asesorías.

Durante esta semana se realizaron actividades de diagnóstico, comparación de modelos NoSQL, definición de consultas, reglas del caso y una primera conexión con MongoDB Atlas.

## Actividades realizadas

### A1 - Diagnóstico
Se resolvieron preguntas teóricas sobre:
- SQL
- Python
- JSON
- claves primarias y foráneas
- tipos de datos
- manejo básico de errores

También se realizaron tres ejercicios prácticos:
- Corrección y lectura de JSON
- Filtrado de registros con Python
- Consulta de relaciones con SQL

### A2 - Comparación de modelos NoSQL
Se analizaron los siguientes modelos:
- MongoDB - documental
- Redis - clave-valor
- Cassandra - familias de columnas
- Neo4j - grafos

### A3 - Consultas y reglas
Se definieron las consultas Q01 a Q06 relacionadas con:
- iniciativas activas
- detalle de iniciativas
- iniciativas por emprendedor
- asesorías programadas
- historial de asesorías
- cantidad de asesorías realizadas

También se definieron reglas funcionales del caso.

### A4 - MongoDB
Se realizó la conexión a MongoDB Atlas mediante mongosh.

Se creó la base de datos:

emprendimiento_sena_lab

Se utilizó la colección:

asesorias_demo

Se realizaron pruebas con los documentos:
- ASE-DEMO-001
- ASE-DEMO-002

Se verificaron tipos de datos como:
- cadenas
- booleanos
- arreglos
- subdocumentos
- Date
- null

## Estructura del proyecto

- diagnostico_nosql/: ejercicios del diagnóstico
- docs/: matrices, consultas y reglas
- scripts/: scripts de MongoDB
- evidencias/: resultados de ejecución
- entorno.md: información del entorno de trabajo
- README.md: descripción general del proyecto

## Herramientas utilizadas

- Visual Studio Code
- Python 3.14.6
- Git 2.51.0
- mongosh 2.5.5
- MongoDB Server 8.0.34
- MongoDB Atlas

## Ejecución del script

Para ejecutar el script de exploración se utiliza:

```bash
mongosh "mongodb+srv://TU_CLUSTER.mongodb.net/" --apiVersion 1 --username TU_USUARIO --file scripts/01_explorar.js

.env
secrets/
.venv/
__pycache__/
