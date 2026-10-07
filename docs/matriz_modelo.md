# A2 - Comparación de modelos NoSQL

| Caso | Modelo propuesto | Razón vinculada a una consulta | Límite o costo | Alternativa |
|---|---|---|---|---|
| Iniciativas de varios sectores | Documental - MongoDB | Permite guardar iniciativas con campos diferentes según el sector y consultar fácilmente por sector, estado o etapa. | Si se diseña mal, puede haber duplicación de datos o documentos muy diferentes entre sí. | SQL, si la estructura fuera muy estable y las relaciones fueran más importantes que la flexibilidad. |
| Sesiones temporales | Clave-valor - Redis | Permite consultar rápidamente una sesión mediante una clave y manejar datos que vencen después de cierto tiempo. | No es la mejor opción para relaciones complejas o consultas muy elaboradas entre varios datos. | MongoDB o SQL si se necesitara guardar más información histórica de las sesiones. |
| Recorridos de relaciones | Grafos - Neo4j | Facilita recorrer relaciones entre emprendedores, mentores y habilidades, por ejemplo encontrar qué mentor tiene determinada habilidad y con qué emprendedores se relaciona. | Puede ser innecesario para sistemas donde las relaciones son simples y no se necesitan recorridos complejos. | SQL, usando tablas relacionadas y claves foráneas. |
| Lecturas por dispositivo y periodo | Familias de columnas - Cassandra | Está orientada a manejar grandes cantidades de datos distribuidos y consultas previamente definidas, como lecturas de sensores por dispositivo y periodo. | El modelo debe diseñarse pensando desde el inicio en las consultas que se van a realizar. | MongoDB o SQL si la cantidad de datos fuera pequeña o mediana. |

## Situación en la que conservaría SQL

Conservaría una base de datos SQL si el sistema tuviera una estructura de datos muy estable y necesitara mantener relaciones estrictas entre varias entidades.

Por ejemplo, si cada iniciativa tuviera siempre los mismos campos y fuera necesario garantizar relaciones entre emprendedores, iniciativas y asesorías mediante claves primarias y foráneas, una base de datos relacional podría ser una buena opción.

## Justificación individual

Considero que para el caso de las iniciativas de emprendimiento MongoDB es una opción adecuada porque los proyectos pueden pertenecer a diferentes sectores y no todos necesitan exactamente los mismos atributos. Esto permite manejar una estructura flexible sin obligar a que todas las iniciativas tengan los mismos campos.