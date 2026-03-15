# Gestor de Información Básica 🖥️

Esta es una aplicación de interfaz gráfica de usuario (GUI) desarrollada en Python utilizando la librería `tkinter`. El propósito de esta herramienta es permitir a los usuarios interactuar con datos de manera visual, facilitando el ingreso, visualización y eliminación de información mediante una interfaz intuitiva.

## 🎯 Objetivos del Proyecto

- Implementar una interfaz gráfica funcional utilizando componentes básicos (etiquetas, botones, campos de texto y listas).
- Aplicar el paradigma de Programación Orientada a Objetos (POO) para estructurar el código de manera limpia y escalable.
- Manejar eventos de usuario (clics) y validación de datos en tiempo real.

## ⚙️ Funcionalidad y Características

La aplicación cuenta con las siguientes características interactivas:
- **Entrada de Texto (`Entry`):** Permite al usuario escribir nuevos datos.
- **Botón "Agregar":** Captura la información ingresada y la añade a la lista principal. Incluye una validación que muestra una advertencia (`messagebox`) si el usuario intenta agregar un campo vacío.
- **Botón "Limpiar":** Tiene una doble función:
  1. Borra cualquier texto que esté actualmente escrito en el campo de entrada.
  2. Si el usuario selecciona un elemento específico dentro de la lista, este botón elimina ese registro exacto.
- **Lista de Datos (`Listbox`):** Muestra de forma organizada toda la información que ha sido agregada por el usuario.

## 🛠️ Tecnologías Utilizadas

- **Lenguaje:** Python 3.x
- **Librería GUI:** `tkinter` (incluida en la biblioteca estándar de Python)

## 🚀 Instrucciones de Ejecución

Para probar esta aplicación en tu entorno local, sigue estos pasos:

1. Asegúrate de tener Python instalado en tu sistema.
2. Clona este repositorio o descarga el archivo fuente `Aplicación_GUI.py`.
3. Abre una terminal y navega hasta el directorio donde se encuentra el archivo.
4. Ejecuta el script con el siguiente comando:
   ```bash
   python app_gui.py