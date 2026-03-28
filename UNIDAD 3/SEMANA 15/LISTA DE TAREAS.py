import tkinter as tk
from tkinter import messagebox


#
# LÓGICA DE LA APLICACIÓN Y MANEJO DE EVENTOS
#

def agregar_tarea(event=None):
    """
    Añade una nueva tarea a la lista.
    El parámetro 'event' permite que la función responda tanto al botón como a la tecla Enter.
    """
    tarea = entrada_tarea.get().strip()  # Obtiene el texto y elimina espacios en blanco extras
    if tarea:
        # Se inserta la tarea al final de la lista
        lista_tareas.insert(tk.END, tarea)
        # Se limpia el campo de entrada
        entrada_tarea.delete(0, tk.END)
    else:
        # Muestra una advertencia si el campo está vacío
        messagebox.showwarning("Campo vacío", "Por favor, escribe una tarea antes de añadirla.")


def marcar_completada(event=None):
    """
    Marca la tarea seleccionada como completada cambiando su apariencia visual.
    También responde al evento de doble clic.
    """
    try:
        # Obtiene el índice de la tarea seleccionada
        indice_seleccionado = lista_tareas.curselection()[0]
        tarea_actual = lista_tareas.get(indice_seleccionado)

        # Verifica que no esté ya marcada para evitar duplicar el prefijo
        if not tarea_actual.startswith("✓ "):
            tarea_completada = f"✓ {tarea_actual}"

            # Reemplaza el texto en la lista
            lista_tareas.delete(indice_seleccionado)
            lista_tareas.insert(indice_seleccionado, tarea_completada)

            # Cambia visualmente el estado (letra gris para indicar que está completada)
            lista_tareas.itemconfig(indice_seleccionado, {'fg': 'gray'})

    except IndexError:
        messagebox.showwarning("Sin selección", "Por favor, selecciona una tarea de la lista para completarla.")


def eliminar_tarea():
    """
    Elimina la tarea seleccionada actualmente en el Listbox.
    """
    try:
        indice_seleccionado = lista_tareas.curselection()[0]
        lista_tareas.delete(indice_seleccionado)
    except IndexError:
        messagebox.showwarning("Sin selección", "Por favor, selecciona una tarea para eliminar.")


# ==========================================
# CONFIGURACIÓN DE LA INTERFAZ GRÁFICA (GUI)
# ==========================================

# 1. Crear la ventana principal
ventana = tk.Tk()
ventana.title("Gestor de Lista de Tareas")
ventana.geometry("400x450")
ventana.config(padx=20, pady=20)

# 2. Componentes de Entrada
frame_entrada = tk.Frame(ventana)
frame_entrada.pack(pady=10, fill=tk.X)

entrada_tarea = tk.Entry(frame_entrada, font=("Arial", 12))
entrada_tarea.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 10))

# Enlazar la tecla "Enter" al campo de entrada para añadir tareas
entrada_tarea.bind("<Return>", agregar_tarea)

btn_anadir = tk.Button(frame_entrada, text="Añadir Tarea", bg="#4CAF50", fg="white", command=agregar_tarea)
btn_anadir.pack(side=tk.RIGHT)

# 3. Componente de Lista (Listbox)
frame_lista = tk.Frame(ventana)
frame_lista.pack(pady=10, fill=tk.BOTH, expand=True)

# Añadir una barra de desplazamiento (Scrollbar) para listas largas
scrollbar = tk.Scrollbar(frame_lista)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

lista_tareas = tk.Listbox(frame_lista, font=("Arial", 12), selectbackground="#a6a6a6", yscrollcommand=scrollbar.set)
lista_tareas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
scrollbar.config(command=lista_tareas.yview)

# Evento opcional: Doble clic izquierdo para marcar como completada
lista_tareas.bind("<Double-Button-1>", marcar_completada)

# 4. Componentes de Acción (Botones inferiores)
frame_botones = tk.Frame(ventana)
frame_botones.pack(pady=10, fill=tk.X)

btn_completar = tk.Button(frame_botones, text="Marcar como Completada", bg="#2196F3", fg="white",
                          command=marcar_completada)
btn_completar.pack(side=tk.LEFT, expand=True, fill=tk.X, padx=(0, 5))

btn_eliminar = tk.Button(frame_botones, text="Eliminar Tarea", bg="#f44336", fg="white", command=eliminar_tarea)
btn_eliminar.pack(side=tk.RIGHT, expand=True, fill=tk.X, padx=(5, 0))

# Iniciar el bucle principal de la aplicación
ventana.mainloop()