
# ARCHIVO: producto.py

class Producto:
    def __init__(self, id_prod, nombre, cantidad, precio):
        # Constructor que inicializa los atributos
        self.__id = id_prod  # Hacemos los atributos "privados" por convención
        self.__nombre = nombre
        self.__cantidad = cantidad
        self.__precio = precio

    # Getters (Obtenedores)
    def get_id(self):
        return self.__id

    def get_nombre(self):
        return self.__nombre

    def get_cantidad(self):
        return self.__cantidad

    def get_precio(self):
        return self.__precio

    # Setters (Modificadores) - El ID no suele tener setter porque es único
    def set_nombre(self, nombre):
        self.__nombre = nombre

    def set_cantidad(self, cantidad):
        self.__cantidad = cantidad

    def set_precio(self, precio):
        self.__precio = precio

    def __str__(self):
        # Método especial para mostrar la información como texto
        return f"ID: {self.__id} | Nombre: {self.__nombre} | Cant: {self.__cantidad} | Precio: ${self.__precio:.2f}"


# ARCHIVO: main.py (o inventario.py)
# ==========================================
# Si separas los archivos, descomenta la siguiente línea:
# from producto import Producto

class Inventario:
    def __init__(self):
        self.productos = []  # Lista para guardar los objetos Producto

    def aniadir_producto(self, producto):
        # Verificar ID único
        if any(p.get_id() == producto.get_id() for p in self.productos):
            print("Error: Ya existe un producto con ese ID.")
            return
        self.productos.append(producto)
        print("Producto añadido correctamente.")

    def eliminar_producto(self, id_prod):
        for p in self.productos:
            if p.get_id() == id_prod:
                self.productos.remove(p)
                print("Producto eliminado.")
                return
        print("Error: No se encontró el producto.")

    def actualizar_producto(self, id_prod, nueva_cant=None, nuevo_precio=None):
        for p in self.productos:
            if p.get_id() == id_prod:
                if nueva_cant is not None:
                    p.set_cantidad(nueva_cant)
                if nuevo_precio is not None:
                    p.set_precio(nuevo_precio)
                print("Producto actualizado.")
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
    inventario = Inventario()
    while True:
        print("\n--- GESTIÓN DE INVENTARIO (Opción 1) ---")
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
                # Crear objeto (asumiendo que Producto está importado o definido arriba)
                nuevo_prod = Producto(id_prod, nombre, cant, precio)
                inventario.aniadir_producto(nuevo_prod)
            except ValueError:
                print("Error: Cantidad o precio inválidos.")

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
            print("Saliendo...")
            break
        else:
            print("Opción no válida.")


if __name__ == "__main__":
    menu()