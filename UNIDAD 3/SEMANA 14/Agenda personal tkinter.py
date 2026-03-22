import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkcalendar import DateEntry


class AgendaPersonalApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Agenda Personal")
        self.root.geometry("600x550")
        self.root.configure(padx=20, pady=20)

        # ==========================================
        # CONTENEDORES (Frames)
        # ==========================================
        # Frame para la entrada de datos
        self.frame_entrada = tk.LabelFrame(self.root, text="Detalles del Evento", padx=10, pady=10)
        self.frame_entrada.pack(fill="x", pady=(0, 10))

        # Frame para los botones de acción
        self.frame_botones = tk.Frame(self.root, pady=10)
        self.frame_botones.pack(fill="x")

        # Frame para la visualización de la lista (Treeview)
        self.frame_lista = tk.LabelFrame(self.root, text="Lista de Eventos", padx=10, pady=10)
        self.frame_lista.pack(fill="both", expand=True)

        # ==========================================
        # COMPONENTES DE ENTRADA
        # ==========================================
        # Etiqueta y DatePicker para la Fecha
        tk.Label(self.frame_entrada, text="Fecha:").grid(row=0, column=0, sticky="w", pady=5)
        self.date_picker = DateEntry(self.frame_entrada, width=15, background='darkblue',
                                     foreground='white', borderwidth=2, date_pattern='yyyy-mm-dd')
        self.date_picker.grid(row=0, column=1, padx=10, pady=5, sticky="w")

        # Etiqueta y Entry para la Hora
        tk.Label(self.frame_entrada, text="Hora (HH:MM):").grid(row=1, column=0, sticky="w", pady=5)
        self.entry_hora = tk.Entry(self.frame_entrada, width=18)
        self.entry_hora.grid(row=1, column=1, padx=10, pady=5, sticky="w")

        # Etiqueta y Entry para la Descripción
        tk.Label(self.frame_entrada, text="Descripción:").grid(row=2, column=0, sticky="w", pady=5)
        self.entry_descripcion = tk.Entry(self.frame_entrada, width=40)
        self.entry_descripcion.grid(row=2, column=1, padx=10, pady=5, sticky="w")

        # ==========================================
        # BOTONES DE ACCIÓN
        # ==========================================
        self.btn_agregar = tk.Button(self.frame_botones, text="Agregar Evento", bg="#4CAF50", fg="white",
                                     command=self.agregar_evento)
        self.btn_agregar.pack(side="left", padx=5)

        self.btn_eliminar = tk.Button(self.frame_botones, text="Eliminar Evento Seleccionado", bg="#f44336", fg="white",
                                      command=self.eliminar_evento)
        self.btn_eliminar.pack(side="left", padx=5)

        self.btn_salir = tk.Button(self.frame_botones, text="Salir", bg="#555555", fg="white",
                                   command=self.salir_aplicacion)
        self.btn_salir.pack(side="right", padx=5)

        # ==========================================
        # TREEVIEW (Lista de Eventos)
        # ==========================================
        # Configuración de columnas
        columnas = ("Fecha", "Hora", "Descripción")
        self.tree = ttk.Treeview(self.frame_lista, columns=columnas, show="headings", height=10)

        # Definir los encabezados y anchos de columna
        self.tree.heading("Fecha", text="Fecha")
        self.tree.column("Fecha", width=100, anchor="center")

        self.tree.heading("Hora", text="Hora")
        self.tree.column("Hora", width=100, anchor="center")

        self.tree.heading("Descripción", text="Descripción")
        self.tree.column("Descripción", width=300, anchor="w")

        # Agregar un Scrollbar al Treeview
        scrollbar = ttk.Scrollbar(self.frame_lista, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)

        self.tree.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

    # ==========================================
    # MÉTODOS Y MANEJO DE EVENTOS
    # ==========================================
    def agregar_evento(self):
        """Obtiene los datos de los campos de entrada y los añade al TreeView."""
        fecha = self.date_picker.get()
        hora = self.entry_hora.get().strip()
        descripcion = self.entry_descripcion.get().strip()

        # Validación básica para que no ingresen eventos vacíos
        if not hora or not descripcion:
            messagebox.showwarning("Campos incompletos", "Por favor, ingresa la hora y la descripción del evento.")
            return

        # Insertar los datos en el Treeview
        self.tree.insert("", "end", values=(fecha, hora, descripcion))

        # Limpiar los campos de entrada después de agregar
        self.entry_hora.delete(0, tk.END)
        self.entry_descripcion.delete(0, tk.END)
        self.date_picker.set_date(self.date_picker._date.today())  # Reiniciar a la fecha actual

        messagebox.showinfo("Éxito", "Evento agregado correctamente.")

    def eliminar_evento(self):
        """Elimina el evento seleccionado en el TreeView previa confirmación."""
        seleccion = self.tree.selection()

        if not seleccion:
            messagebox.showwarning("Advertencia", "Por favor, selecciona un evento para eliminar.")
            return

        # Cuadro de diálogo de confirmación (Requisito Opcional cumplido)
        respuesta = messagebox.askyesno("Confirmar Eliminación",
                                        "¿Estás seguro de que deseas eliminar el evento seleccionado?")

        if respuesta:
            for item in seleccion:
                self.tree.delete(item)
            messagebox.showinfo("Eliminado", "Evento eliminado correctamente.")

    def salir_aplicacion(self):
        """Cierra la ventana principal de la aplicación."""
        self.root.destroy()


# ==========================================
# EJECUCIÓN PRINCIPAL
# ==========================================
if __name__ == "__main__":
    # Crear la ventana principal
    ventana_principal = tk.Tk()

    # Instanciar la aplicación
    app = AgendaPersonalApp(ventana_principal)

    # Iniciar el bucle de eventos
    ventana_principal.mainloop()