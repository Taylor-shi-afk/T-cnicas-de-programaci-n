import json

# 1. Clase Producto
class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        self.id = id_producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def to_dict(self):
        return {"id": self.id, "nombre": self.nombre, "cantidad": self.cantidad, "precio": self.precio}

    def __str__(self):
        return f"ID: {self.id} | Nombre: {self.nombre} | Stock: {self.cantidad} | Precio: ${self.precio:.2f}"

# 2. Clase Inventario
class Inventario:
    def __init__(self):
        # Uso de Diccionario para búsqueda rápida por ID
        self.productos = {}
        self.archivo = "inventario.json"
        self.cargar_desde_archivo()

    def añadir_producto(self, producto):
        if producto.id in self.productos:
            print("Error: El ID ya existe.")
        else:
            self.productos[producto.id] = producto
            self.guardar_en_archivo()
            print("Producto añadido con éxito.")

    def eliminar_producto(self, id_producto):
        if id_producto in self.productos:
            del self.productos[id_producto]
            self.guardar_en_archivo()
            print("Producto eliminado.")
        else:
            print("Error: ID no encontrado.")

    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        if id_producto in self.productos:
            if cantidad is not None: self.productos[id_producto].cantidad = cantidad
            if precio is not None: self.productos[id_producto].precio = precio
            self.guardar_en_archivo()
            print("Producto actualizado.")
        else:
            print("Error: ID no encontrado.")

    def buscar_por_nombre(self, nombre):
        encontrados = [p for p in self.productos.values() if nombre.lower() in p.nombre.lower()]
        if encontrados:
            for p in encontrados: print(p)
        else:
            print("No se encontraron coincidencias.")

    def mostrar_todo(self):
        if not self.productos:
            print("El inventario está vacío.")
        for p in self.productos.values():
            print(p)

    # 4. Almacenamiento en Archivos (Serialización)
    def guardar_en_archivo(self):
        with open(self.archivo, 'w') as f:
            data = {idx: p.to_dict() for idx, p in self.productos.items()}
            json.dump(data, f, indent=4)

    def cargar_desde_archivo(self):
        try:
            with open(self.archivo, 'r') as f:
                data = json.load(f)
                for item in data.values():
                    self.productos[item['id']] = Producto(item['id'], item['nombre'], item['cantidad'], item['precio'])
        except (FileNotFoundError, json.JSONDecodeError):
            self.productos = {}

# 5. Interfaz de Usuario
def menu():
    inv = Inventario()
    while True:
        print("\n--- SISTEMA DE GESTIÓN DE INVENTARIO ---")
        print("1. Añadir Producto\n2. Eliminar\n3. Actualizar\n4. Buscar\n5. Mostrar Todo\n6. Salir")
        opcion = input("Seleccione: ")

        if opcion == '1':
            idx = input("ID único: ")
            nom = input("Nombre: ")
            cant = int(input("Cantidad: "))
            pre = float(input("Precio: "))
            inv.añadir_producto(Producto(idx, nom, cant, pre))
        elif opcion == '2':
            inv.eliminar_producto(input("ID a eliminar: "))
        elif opcion == '3':
            idx = input("ID: ")
            c = input("Nueva cantidad (enter para omitir): ")
            p = input("Nuevo precio (enter para omitir): ")
            inv.actualizar_producto(idx, int(c) if c else None, float(p) if p else None)
        elif opcion == '4':
            inv.buscar_por_nombre(input("Nombre a buscar: "))
        elif opcion == '5':
            inv.mostrar_todo()
        elif opcion == '6':
            break

if __name__ == "__main__":
    menu()