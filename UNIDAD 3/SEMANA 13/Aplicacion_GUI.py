import tkinter as tk
from tkinter import messagebox


class AplicacionGUI:
    def __init__(self, root):
        """
        Inicializa la ventana principal y todos los componentes de la interfaz.
        """
        self.root = root
        # Requisito: Ventana principal con un título descriptivo
        self.root.title("Gestor de Información Básica")
        self.root.geometry("400x450")
        self.root.config(padx=20, pady=20)

        # Requisito: Diseño de la Interfaz (Etiquetas, Botones, Campos, Lista)

        # Etiqueta (Label)
        self.lbl_instruccion = tk.Label(root, text="Ingrese un nuevo dato:", font=("Arial", 10))
        self.lbl_instruccion.pack(anchor="w", pady=(0, 5))

        # Campo de texto (Entry)
        self.entrada_dato = tk.Entry(root, width=40, font=("Arial", 10))
        self.entrada_dato.pack(fill="x", pady=(0, 15))

        # Frame para organizar los botones en línea horizontal
        self.frame_botones = tk.Frame(root)
        self.frame_botones.pack(pady=(0, 15))

        # Requisito: Funcionalidad - Botón "Agregar"
        self.btn_agregar = tk.Button(self.frame_botones, text="Agregar", width=12, bg="#4CAF50", fg="white",
                                     command=self.agregar_dato)
        self.btn_agregar.pack(side=tk.LEFT, padx=10)

        # Requisito: Funcionalidad - Botón "Limpiar"
        self.btn_limpiar = tk.Button(self.frame_botones, text="Limpiar", width=12, bg="#f44336", fg="white",
                                     command=self.limpiar_datos)
        self.btn_limpiar.pack(side=tk.LEFT, padx=10)

        # Etiqueta para la lista
        self.lbl_lista = tk.Label(root, text="Datos registrados:", font=("Arial", 10))
        self.lbl_lista.pack(anchor="w", pady=(10, 5))

        # Requisito: Lista para mostrar datos (Listbox)
        self.lista_datos = tk.Listbox(root, width=50, height=12, font=("Arial", 10))
        self.lista_datos.pack(fill="both", expand=True)

    #  Requisito: Eventos y Lógica de Funcionalidad

    def agregar_dato(self):
        """
        Captura el texto del campo de entrada y lo añade a la lista.
        Muestra una advertencia si el campo está vacío.
        """
        # Se obtiene la información ingresada
        dato = self.entrada_dato.get()

        # Validar que el usuario no ingrese texto en blanco
        if dato.strip():
            self.lista_datos.insert(tk.END, dato)  # Se agrega a la lista
            self.entrada_dato.delete(0, tk.END)  # Se limpia el campo de texto automáticamente
        else:
            # Manejo de error si el campo está vacío
            messagebox.showwarning("Advertencia", "El campo de texto está vacío. Ingrese un dato.")

    def limpiar_datos(self):
        """
        Borra la información ingresada en el campo de texto o el elemento
        seleccionado por el usuario en la lista.
        """
        # Limpiar el campo de texto siempre
        self.entrada_dato.delete(0, tk.END)

        # Obtener el índice del elemento seleccionado en la lista (si lo hay)
        seleccion = self.lista_datos.curselection()
        if seleccion:
            # Borrar el elemento seleccionado
            self.lista_datos.delete(seleccion)


# Bloque principal de ejecución
if __name__ == "__main__":
    # Crear la ventana principal de Tkinter
    ventana_principal = tk.Tk()

    # Instanciar la aplicación
    app = AplicacionGUI(ventana_principal)

    # Iniciar el bucle de eventos (mantiene la ventana abierta)
    ventana_principal.mainloop()