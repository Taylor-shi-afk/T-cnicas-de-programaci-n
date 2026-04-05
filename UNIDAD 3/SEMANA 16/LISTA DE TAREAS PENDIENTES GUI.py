import tkinter as tk
from tkinter import messagebox


def agregar_tarea(event=None):
    """Añade la tarea escrita en el Entry al Listbox."""
    tarea = input_tarea.get()
    if tarea.strip():  # Verifica que no esté vacío o solo contenga espacios
        lista_tareas.insert(tk.END, tarea)
        input_tarea.delete(0, tk.END)  # Limpia el campo de entrada
    else:
        messagebox.showwarning("Advertencia", "Por favor, escribe una tarea.")


def completar_tarea(event=None):
    """Marca la tarea seleccionada como completada cambiando su color y texto."""
    try:
        indice = lista_tareas.curselection()[0]
        texto_actual = lista_tareas.get(indice)

        # Evita marcar una tarea que ya está completada
        if not texto_actual.endswith(" ✅ (Completada)"):
            lista_tareas.delete(indice)
            lista_tareas.insert(indice, texto_actual + " ✅ (Completada)")
            # Feedback visual: Cambia el color del texto a gris
            lista_tareas.itemconfig(indice, {'fg': 'gray'})
            # Mantiene la selección para que el usuario no la pierda
            lista_tareas.select_set(indice)
    except IndexError:
        pass  # No se hace nada si no hay ninguna tarea seleccionada


def eliminar_tarea(event=None):
    """Elimina la tarea seleccionada del Listbox."""
    try:
        indice = lista_tareas.curselection()[0]
        lista_tareas.delete(indice)
    except IndexError:
        pass  # No se hace nada si no hay ninguna tarea seleccionada


def cerrar_aplicacion(event=None):
    """Cierra la ventana principal."""
    ventana.destroy()



# Configuración de la Ventana Principal

ventana = tk.Tk()
ventana.title("Gestión de Tareas")
ventana.geometry("450x400")
ventana.config(padx=20, pady=20)


# Elementos de la Interfaz (Widgets)

# Campo de entrada (Entry)
input_tarea = tk.Entry(ventana, width=40, font=("Arial", 12))
input_tarea.pack(pady=(0, 10))

# Marco para los botones
frame_botones = tk.Frame(ventana)
frame_botones.pack(pady=(0, 15))

# Botones con eventos de clic
btn_agregar = tk.Button(frame_botones, text="Añadir Tarea", command=agregar_tarea)
btn_agregar.grid(row=0, column=0, padx=5)

btn_completar = tk.Button(frame_botones, text="Completar", command=completar_tarea)
btn_completar.grid(row=0, column=1, padx=5)

btn_eliminar = tk.Button(frame_botones, text="Eliminar", command=eliminar_tarea)
btn_eliminar.grid(row=0, column=2, padx=5)

# Lista para mostrar las tareas (Listbox)
lista_tareas = tk.Listbox(ventana, width=50, height=15, font=("Arial", 11), selectbackground="#a6a6a6")
lista_tareas.pack()


# Atajos de Teclado (Bindings)

# Tecla "Enter" en el campo de texto para añadir
input_tarea.bind('<Return>', agregar_tarea)

# Teclas "C" o "c" para completar la tarea seleccionada
ventana.bind('<c>', completar_tarea)
ventana.bind('<C>', completar_tarea)

# Tecla "Delete" (Suprimir) o "D"/"d" para eliminar la tarea
ventana.bind('<Delete>', eliminar_tarea)
ventana.bind('<d>', eliminar_tarea)
ventana.bind('<D>', eliminar_tarea)

# Tecla "Escape" para cerrar la aplicación
ventana.bind('<Escape>', cerrar_aplicacion)

# Iniciar el bucle principal de la aplicación
ventana.mainloop()