# 📚 Sistema Inteligente de Biblioteca en Python

¡Bienvenido al **Sistema de Biblioteca**! Este es un proyecto desarrollado en Python puro diseñado para facilitar la administración del inventario y los usuarios de una biblioteca, utilizando el paradigma de Programación Orientada a Objetos (POO).

---

## ✨ Características y Funciones

El sistema cuenta con un menú interactivo en consola que permite realizar las siguientes acciones de forma intuitiva:

* **📦 Carga Automática:** Si el sistema es nuevo, pre-carga libros y usuarios por defecto automáticamente.
* **💾 Persistencia de Datos:** Toda la actividad se guarda al instante en un archivo `datos_biblioteca.txt`. 
* **🔍 Motor de Búsqueda:** Encuentra libros por su título, autor o categoría.
* **🤝 Gestión de Préstamos:** Permite prestar libros (sacándolos del inventario general) y procesar devoluciones.
* **🛡️ Validaciones:** Protege contra la duplicación de identificadores (ISBN únicos e IDs de usuario únicos).

## 🛠️ Requisitos e Instalación

1.  Asegúrate de tener instalado **Python 3.x**.
2.  Clona o descarga este repositorio en tu computadora.
3.  No necesitas instalar dependencias adicionales; el código utiliza librerías nativas (`os`, `json`).

---