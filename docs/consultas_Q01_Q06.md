# A3 - Consultas Q01 a Q06

## Q01 - Iniciativas activas por sector y etapa didáctica

**Actor:** Responsable de la Unidad de Emprendimiento.

**Necesidad:** Consultar las iniciativas que se encuentran activas, filtrándolas por sector y por etapa didáctica.

**Filtros:**
- sector
- etapa
- estado = activa

**Campos de salida:**
- codigo
- nombre
- sector
- etapa
- estado

**Orden:** Por nombre de la iniciativa en orden alfabético.

**Frecuencia estimada:** Diaria.

---

## Q02 - Detalle de una iniciativa con propuesta de valor y atributos específicos

**Actor:** Responsable de la Unidad de Emprendimiento o asesor.

**Necesidad:** Consultar toda la información de una iniciativa específica, incluyendo su propuesta de valor y los atributos particulares según su sector.

**Filtros:**
- codigo de la iniciativa

**Campos de salida:**
- codigo
- nombre
- sector
- etapa
- propuesta_valor
- atributos específicos
- estado

**Orden:** No requiere un orden porque se consulta una sola iniciativa.

**Frecuencia estimada:** Frecuente.

---

## Q03 - Iniciativas de un emprendedor responsable por estado

**Actor:** Responsable de la Unidad de Emprendimiento.

**Necesidad:** Consultar las iniciativas asociadas a un emprendedor responsable y filtrarlas por su estado.

**Filtros:**
- codigo del emprendedor
- estado de la iniciativa

**Campos de salida:**
- codigo de la iniciativa
- nombre
- sector
- etapa
- estado

**Orden:** Por nombre de la iniciativa.

**Frecuencia estimada:** Semanal.

---

## Q04 - Asesorías programadas pendientes por rango de fechas y modalidad

**Actor:** Asesor o responsable de la Unidad de Emprendimiento.

**Necesidad:** Consultar las asesorías que están programadas y pendientes dentro de un rango de fechas y según una modalidad determinada.

**Filtros:**
- estado = programada
- fecha_programada desde
- fecha_programada hasta
- modalidad

**Campos de salida:**
- codigo de la asesoria
- codigo de la iniciativa
- codigo del asesor
- fecha_programada
- modalidad
- estado

**Orden:** Por fecha_programada de la más próxima a la más lejana.

**Frecuencia estimada:** Diaria.

---

## Q05 - Historial de asesorías de una iniciativa

**Actor:** Asesor o responsable de la Unidad de Emprendimiento.

**Necesidad:** Consultar todas las asesorías relacionadas con una iniciativa específica para conocer su historial.

**Filtros:**
- codigo de la iniciativa

**Campos de salida:**
- codigo de la asesoria
- codigo del asesor
- estado
- modalidad
- fecha_programada
- fecha_realizacion
- temas tratados

**Orden:** Por fecha, desde la asesoría más antigua hasta la más reciente.

**Frecuencia estimada:** Frecuente.

---

## Q06 - Cantidad de asesorías realizadas por sector y mes

**Actor:** Responsable de la Unidad de Emprendimiento.

**Necesidad:** Consultar la cantidad de asesorías realizadas agrupadas por sector de la iniciativa y por mes.

**Filtros:**
- estado = realizada
- periodo de fechas

**Campos de salida:**
- sector
- mes
- cantidad de asesorias realizadas

**Orden:** Por mes y sector.

**Frecuencia estimada:** Mensual.

**Decisión sobre el sector:** Para esta consulta se tomará el sector registrado al momento de la asesoría, con el fin de conservar el contexto histórico de la información.