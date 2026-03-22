# 📅 Aplicación de Agenda Personal

![Python](https://img.shields.io/badge/Python-3.x-blue?style=flat&logo=python)
![Tkinter](https://img.shields.io/badge/GUI-Tkinter-lightgrey?style=flat)
![POO](https://img.shields.io/badge/Paradigma-POO-success?style=flat)

Una aplicación de escritorio intuitiva y fácil de usar desarrollada en Python. Esta herramienta funciona como una agenda personal que permite al usuario programar, visualizar y gestionar sus eventos o tareas diarias a través de una interfaz gráfica (GUI).

El proyecto fue construido aplicando los principios de la **Programación Orientada a Objetos (POO)** para mantener un código limpio, modular y escalable.

---

## ✨ Características Principales

* **Interfaz Gráfica Amigable:** Desarrollada con la biblioteca estándar `Tkinter` de Python, organizada lógicamente mediante contenedores (`Frames`).
* **Selección de Fecha Interactiva:** Integración de un *DatePicker* (calendario desplegable) gracias a la librería `tkcalendar`, facilitando la elección rápida y sin errores de fechas.
* **Visualización en Tabla:** Uso del widget `Treeview` para mostrar todos los eventos programados de forma estructurada (Fecha, Hora, Descripción), incluyendo una barra de desplazamiento vertical.
* **Validación de Datos:** El sistema alerta al usuario si intenta guardar un evento sin haber completado los campos de hora y descripción.
* **Seguridad al Eliminar:** Incorpora un cuadro de diálogo de confirmación antes de eliminar cualquier registro para evitar borrados accidentales.

---

## 🛠️ Requisitos Previos

Para ejecutar esta aplicación, asegúrate de tener instalado lo siguiente en tu sistema:

1.  **Python 3.x:** Puedes descargarlo desde [python.org](https://www.python.org/).
2.  **Librería tkcalendar:** Es necesaria para el funcionamiento del selector de fechas. Puedes instalarla ejecutando el siguiente comando en tu terminal o símbolo del sistema:

    ```bash
    pip install tkcalendar
    ```

---

## 🚀 Instalación y Uso

1.  Clona este repositorio en tu máquina local o descarga el archivo `.py` principal.
    ```bash
    git clone [https://github.com/TU_USUARIO/TU_REPOSITORIO.git](https://github.com/TU_USUARIO/TU_REPOSITORIO.git)
    ```
2.  Abre una terminal y navega hasta el directorio donde guardaste el archivo.
3.  Ejecuta el script principal con Python:
    ```bash
    python agenda_personal.py
    ```
*(Nota: Asegúrate de reemplazar `agenda_personal tkinter.py` por el nombre exacto de tu archivo).*

---

## 📖 Cómo utilizar la Agenda

1.  **Agregar un Evento:**
    * Haz clic en el campo **Fecha** y selecciona el día en el calendario desplegable.
    * Escribe la **Hora** en formato `HH:MM` (ej. 14:30).
    * Escribe una **Descripción** breve de tu tarea o evento.
    * Presiona el botón verde **"Agregar Evento"**.
2.  **Ver Eventos:**
    * Todos los eventos agregados aparecerán automáticamente en la tabla inferior. Puedes usar la barra lateral para desplazarte si tienes muchos registros.
3.  **Eliminar un Evento:**
    * Haz clic sobre la fila del evento que deseas borrar en la tabla.
    * Presiona el botón rojo **"Eliminar Evento Seleccionado"**.
    * Confirma tu decisión en el cuadro de diálogo que aparecerá en pantalla.
4.  **Salir:**
    * Usa el botón **"Salir"** para cerrar la aplicación de manera segura.

---

## 🏗️ Estructura del Código

El programa está encapsulado en una clase principal llamada `AgendaPersonalApp`. Esto permite una mejor gestión del estado de la aplicación:

* `__init__(self, root)`: Configura la ventana principal, los contenedores, las etiquetas, los campos de entrada, los botones y la tabla (`Treeview`).
* `agregar_evento(self)`: Extrae los datos de la interfaz, los valida y los inserta en el `Treeview`.
* `eliminar_evento(self)`: Identifica el ítem seleccionado, solicita confirmación mediante `messagebox` y lo remueve de la lista.
* `salir_aplicacion(self)`: Finaliza el bucle principal de Tkinter y cierra la ventana.

---
