# ARCHIVO: gestion_inventario.py (Contiene tanto Producto como Inventario y el Menú)
import os


class Producto:
    def __init__(self, id_prod, nombre, cantidad, precio):
        self.__id = id_prod
        self.__nombre = nombre
        self.__cantidad = cantidad
        self.__precio = precio

    # Getters
    def get_id(self):
        return self.__id

    def get_nombre(self):
        return self.__nombre

    def get_cantidad(self):
        return self.__cantidad

    def get_precio(self):
        return self.__precio

    # Setters
    def set_nombre(self, nombre):
        self.__nombre = nombre

    def set_cantidad(self, cantidad):
        self.__cantidad = cantidad

    def set_precio(self, precio):
        self.__precio = precio

    def __str__(self):
        return f"ID: {self.__id} | Nombre: {self.__nombre} | Cant: {self.__cantidad} | Precio: ${self.__precio:.2f}"


class Inventario:
    def __init__(self, archivo="inventario.txt"):
        self.productos = []
        self.archivo = archivo
        # Requisito 2: Cargar automáticamente los productos al iniciar
        self.cargar_desde_archivo()

    def cargar_desde_archivo(self):
        """Lee el archivo de texto y reconstruye el inventario."""
        try:
            with open(self.archivo, 'r') as f:
                for linea in f:
                    # Separamos los datos por comas (formato CSV simple)
                    datos = linea.strip().split(',')
                    if len(datos) == 4:
                        id_prod, nombre, cant, precio = datos
                        prod = Producto(id_prod, nombre, int(cant), float(precio))
                        self.productos.append(prod)
            print(f"--> Éxito: Inventario cargado desde '{self.archivo}'.")

        # Requisito 3: Manejo de Excepciones (FileNotFoundError y PermissionError)
        except FileNotFoundError:
            print(f"--> Aviso: El archivo '{self.archivo}' no existe. Creando uno nuevo...")
            # Si no existe, creamos un archivo vacío
            try:
                open(self.archivo, 'a').close()
            except PermissionError:
                print(f"--> Error: No hay permisos para crear el archivo en esta ruta.")
        except PermissionError:
            print(f"--> Error: No tienes permisos para leer el archivo '{self.archivo}'.")
        except Exception as e:
            print(f"--> Error inesperado al cargar el archivo: {e}")

    def guardar_en_archivo(self):
        """Guarda todos los productos actuales en el archivo de texto."""
        try:
            with open(self.archivo, 'w') as f:
                for p in self.productos:
                    # Guardamos cada producto en una nueva línea separado por comas
                    linea = f"{p.get_id()},{p.get_nombre()},{p.get_cantidad()},{p.get_precio()}\n"
                    f.write(linea)
            # Requisito 4: Notificar al usuario el éxito de la operación de archivo
            print(f"--> Éxito: Cambios guardados en el archivo '{self.archivo}'.")
        except PermissionError:
            print(
                f"--> Error crítico: No tienes permisos para escribir en el archivo '{self.archivo}'. Los cambios no se guardaron.")
        except Exception as e:
            print(f"--> Error inesperado al guardar en el archivo: {e}")

    # Requisito 1: Reflejar modificaciones en el archivo
    def aniadir_producto(self, producto):
        if any(p.get_id() == producto.get_id() for p in self.productos):
            print("Error: Ya existe un producto con ese ID.")
            return
        self.productos.append(producto)
        print("Producto añadido correctamente en memoria.")
        self.guardar_en_archivo()  # Actualiza el txt

    def eliminar_producto(self, id_prod):
        for p in self.productos:
            if p.get_id() == id_prod:
                self.productos.remove(p)
                print("Producto eliminado de memoria.")
                self.guardar_en_archivo()  # Actualiza el txt
                return
        print("Error: No se encontró el producto.")

    def actualizar_producto(self, id_prod, nueva_cant=None, nuevo_precio=None):
        for p in self.productos:
            if p.get_id() == id_prod:
                if nueva_cant is not None:
                    p.set_cantidad(nueva_cant)
                if nuevo_precio is not None:
                    p.set_precio(nuevo_precio)
                print("Producto actualizado en memoria.")
                self.guardar_en_archivo()  # Actualiza el txt
                return
        print("Error: Producto no encontrado.")

    def buscar_por_nombre(self, nombre):
        encontrados = [p for p in self.productos if nombre.lower() in p.get_nombre().lower()]
        if encontrados:
            for p in encontrados:
                print(p)
        else:
            print("No se encontraron productos con ese nombre.")

    def mostrar_todos(self):
        if not self.productos:
            print("El inventario está vacío.")
        else:
            for p in self.productos:
                print(p)


def menu():
    print("\nIniciando sistema...")
    inventario = Inventario()

    while True:
        print("\n--- GESTIÓN DE INVENTARIO MEJORADO ---")
        print("1. Añadir producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Buscar por nombre")
        print("5. Mostrar todos")
        print("6. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            id_prod = input("Ingrese ID único: ")
            nombre = input("Ingrese nombre: ")
            try:
                cant = int(input("Ingrese cantidad: "))
                precio = float(input("Ingrese precio: "))
                nuevo_prod = Producto(id_prod, nombre, cant, precio)
                inventario.aniadir_producto(nuevo_prod)
            except ValueError:
                print("Error: Cantidad o precio inválidos. Deben ser números.")

        elif opcion == '2':
            id_prod = input("Ingrese ID a eliminar: ")
            inventario.eliminar_producto(id_prod)

        elif opcion == '3':
            id_prod = input("Ingrese ID a actualizar: ")
            try:
                cant = input("Nueva cantidad (enter para dejar igual): ")
                precio = input("Nuevo precio (enter para dejar igual): ")
                c = int(cant) if cant else None
                p = float(precio) if precio else None
                inventario.actualizar_producto(id_prod, c, p)
            except ValueError:
                print("Error: Datos numéricos incorrectos.")

        elif opcion == '4':
            nombre = input("Ingrese nombre a buscar: ")
            inventario.buscar_por_nombre(nombre)

        elif opcion == '5':
            inventario.mostrar_todos()

        elif opcion == '6':
            print("Saliendo del sistema de inventario...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")


if __name__ == "__main__":
    menu()