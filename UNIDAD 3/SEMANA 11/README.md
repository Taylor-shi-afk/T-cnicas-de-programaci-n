# 📦 Sistema Avanzado de Gestión de Inventario

Este proyecto implementa una solución robusta para el control de productos en una tienda, utilizando principios de **Programación Orientada a Objetos (POO)** y persistencia de datos.

---

## 🛠️ Detalles Técnicos y Decisiones de Diseño

### 1. Gestión de Inventario mediante Colecciones
Para este programa, se ha seleccionado un **Diccionario (`dict`)** como la colección principal. La clave es el `ID` del producto y el valor es la instancia de la clase `Producto`.

* 🚀 **Eficiencia:** El uso de diccionarios permite que la búsqueda y eliminación de productos por ID sea extremadamente rápida, con una complejidad de tiempo promedio de $O(1)$.
* 🛡️ **Integridad de Datos:** Al usar el ID como clave, se garantiza automáticamente la **unicidad**, evitando registros duplicados.
* 🔍 **Iteración:** Para funciones de reporte o búsqueda por nombre, se emplea el método `.values()`, facilitando un recorrido lineal eficiente de la colección.

### 2. Persistencia y Almacenamiento en Archivos
Se implementó la **Serialización JSON** para asegurar que la información no se pierda al cerrar la aplicación:

> **Proceso de Guardado:** El método `guardar_en_archivo` transforma el diccionario de objetos en un formato `.json`. Esto mantiene una estructura jerárquica clara y legible.

> **Proceso de Carga:** Al ejecutar el sistema, se realiza una **deserialización**, reconstruyendo los objetos de la clase `Producto` a partir del archivo de texto, cargándolos de nuevo en la memoria RAM.

---