import json
import os


class Libro:
    def __init__(self, titulo, autor, categoria, isbn):
        self._info_inmutable = (autor, titulo)
        self.categoria = categoria
        self.isbn = isbn

    @property
    def autor(self):
        return self._info_inmutable[0]

    @property
    def titulo(self):
        return self._info_inmutable[1]

    def to_dict(self):
        return {"titulo": self.titulo, "autor": self.autor, "categoria": self.categoria, "isbn": self.isbn}

    def __str__(self):
        return f"'{self.titulo}' por {self.autor} (Categoría: {self.categoria}, ISBN: {self.isbn})"


class Usuario:
    def __init__(self, nombre, id_usuario):
        self.nombre = nombre
        self.id_usuario = id_usuario
        self.libros_prestados = []

    def to_dict(self):
        return {
            "nombre": self.nombre,
            "id_usuario": self.id_usuario,
            "libros_prestados": [libro.to_dict() for libro in self.libros_prestados]
        }

    def __str__(self):
        return f"Usuario: {self.nombre} (ID: {self.id_usuario})"


class Biblioteca:
    def __init__(self, archivo_datos="datos_biblioteca.txt"):
        self.libros_disponibles = {}
        self.usuarios = {}
        self.ids_usuarios = set()
        self.archivo_datos = archivo_datos
        self.cargar_datos()

    def cargar_datos_por_defecto(self):
        print("📦 Cargando datos iniciales ...")
        # Libros iniciales
        self.anadir_libro(Libro("El Quijote", "Miguel de Cervantes", "Novela", "ISBN001"), mostrar_mensaje=False)
        self.anadir_libro(Libro("1984", "George Orwell", "Ciencia Ficción", "ISBN002"), mostrar_mensaje=False)
        self.anadir_libro(Libro("Cien años de soledad", "Gabriel García Márquez", "Realismo Mágico", "ISBN003"),
                          mostrar_mensaje=False)
        # Usuarios iniciales
        self.registrar_usuario(Usuario("Taylor", "U100"), mostrar_mensaje=False)
        self.registrar_usuario(Usuario("Kerly", "U200"), mostrar_mensaje=False)
        print("✅ Datos iniciales cargados y listos.")

    def anadir_libro(self, libro, mostrar_mensaje=True):
        if libro.isbn not in self.libros_disponibles:
            self.libros_disponibles[libro.isbn] = libro
            if mostrar_mensaje:
                print(f"✅ Libro añadido: {libro.titulo}")
            self.guardar_datos()
        else:
            if mostrar_mensaje:
                print(f"⚠️ El libro con ISBN {libro.isbn} ya existe.")

    def registrar_usuario(self, usuario, mostrar_mensaje=True):
        if usuario.id_usuario not in self.ids_usuarios:
            self.ids_usuarios.add(usuario.id_usuario)
            self.usuarios[usuario.id_usuario] = usuario
            if mostrar_mensaje:
                print(f"✅ Usuario registrado: {usuario.nombre}")
            self.guardar_datos()
        else:
            if mostrar_mensaje:
                print(f"⚠️ El ID {usuario.id_usuario} ya está en uso.")

    def prestar_libro(self, id_usuario, isbn):
        if id_usuario in self.ids_usuarios and isbn in self.libros_disponibles:
            usuario = self.usuarios[id_usuario]
            libro = self.libros_disponibles.pop(isbn)
            usuario.libros_prestados.append(libro)
            print(f"📖 Libro '{libro.titulo}' prestado a {usuario.nombre}.")
            self.guardar_datos()
        else:
            print("❌ Error: Usuario no encontrado o el libro no está disponible.")

    def devolver_libro(self, id_usuario, isbn):
        if id_usuario in self.ids_usuarios:
            usuario = self.usuarios[id_usuario]
            for libro in usuario.libros_prestados:
                if libro.isbn == isbn:
                    usuario.libros_prestados.remove(libro)
                    self.libros_disponibles[isbn] = libro
                    print(f"🔄 Libro '{libro.titulo}' devuelto por {usuario.nombre}.")
                    self.guardar_datos()
                    return
            print(f"⚠️ {usuario.nombre} no tiene el libro con ISBN {isbn}.")
        else:
            print(f"⚠️ No se encontró el usuario con ID {id_usuario}.")

    def buscar_libros(self, criterio, valor):
        resultados = []
        valor = valor.lower()
        for libro in self.libros_disponibles.values():
            if (criterio == 'titulo' and valor in libro.titulo.lower()) or \
                    (criterio == 'autor' and valor in libro.autor.lower()) or \
                    (criterio == 'categoria' and valor == libro.categoria.lower()):
                resultados.append(libro)
        return resultados

    def guardar_datos(self):
        datos = {
            "libros": {isbn: libro.to_dict() for isbn, libro in self.libros_disponibles.items()},
            "usuarios": {id_user: user.to_dict() for id_user, user in self.usuarios.items()}
        }
        with open(self.archivo_datos, 'w', encoding='utf-8') as archivo:
            json.dump(datos, archivo, indent=4)

    def cargar_datos(self):
        if os.path.exists(self.archivo_datos):
            with open(self.archivo_datos, 'r', encoding='utf-8') as archivo:
                try:
                    datos = json.load(archivo)
                    for isbn, lib_data in datos.get("libros", {}).items():
                        self.libros_disponibles[isbn] = Libro(lib_data['titulo'], lib_data['autor'],
                                                              lib_data['categoria'], lib_data['isbn'])

                    for id_user, user_data in datos.get("usuarios", {}).items():
                        nuevo_usuario = Usuario(user_data['nombre'], user_data['id_usuario'])
                        for lib_prestado in user_data.get('libros_prestados', []):
                            nuevo_usuario.libros_prestados.append(
                                Libro(lib_prestado['titulo'], lib_prestado['autor'], lib_prestado['categoria'],
                                      lib_prestado['isbn']))
                        self.usuarios[id_user] = nuevo_usuario
                        self.ids_usuarios.add(id_user)
                except json.JSONDecodeError:
                    print("⚠️ Archivo de texto vacío o corrupto. Iniciando desde cero.")
                    self.cargar_datos_por_defecto()
        else:
            # Si el archivo no existe, cargamos los datos obligatorios del deber
            self.cargar_datos_por_defecto()


def menu_interactivo():
    mi_biblioteca = Biblioteca()

    while True:
        print("\n" + "=" * 35)
        print(" 📚 SISTEMA DE BIBLIOTECA 📚 ")
        print("=" * 35)
        print("1. Añadir un nuevo libro")
        print("2. Registrar un nuevo usuario")
        print("3. Buscar libros (por título, autor o categoría)")
        print("4. Prestar un libro")
        print("5. Devolver un libro")
        print("6. Ver libros disponibles")
        print("7. Ver usuarios registrados")
        print("8. Salir")

        opcion = input("\nElige una opción (1-8): ")

        if opcion == '1':
            titulo = input("Ingresa el título del libro: ")
            autor = input("Ingresa el autor: ")
            categoria = input("Ingresa la categoría: ")
            isbn = input("Ingresa el ISBN único: ")
            mi_biblioteca.anadir_libro(Libro(titulo, autor, categoria, isbn))

        elif opcion == '2':
            nombre = input("Ingresa el nombre del usuario: ")
            id_usuario = input("Ingresa el ID del usuario: ")
            mi_biblioteca.registrar_usuario(Usuario(nombre, id_usuario))

        elif opcion == '3':
            criterio = input("¿Por qué deseas buscar? (Escribe: titulo, autor o categoria): ").lower()
            if criterio in ['titulo', 'autor', 'categoria']:
                valor = input(f"Ingresa el {criterio} a buscar: ")
                resultados = mi_biblioteca.buscar_libros(criterio, valor)
                print(f"\n--- RESULTADOS DE BÚSQUEDA ---")
                if resultados:
                    for r in resultados:
                        print(f"  > Encontrado: {r}")
                else:
                    print("No se encontraron coincidencias.")
            else:
                print("❌ Criterio no válido. Debes escribir 'titulo', 'autor' o 'categoria'.")

        elif opcion == '4':
            id_usuario = input("Ingresa el ID del usuario: ")
            isbn = input("Ingresa el ISBN del libro a prestar: ")
            mi_biblioteca.prestar_libro(id_usuario, isbn)

        elif opcion == '5':
            id_usuario = input("Ingresa el ID del usuario: ")
            isbn = input("Ingresa el ISBN del libro a devolver: ")
            mi_biblioteca.devolver_libro(id_usuario, isbn)

        elif opcion == '6':
            print("\n--- LIBROS EN EL INVENTARIO ---")
            if not mi_biblioteca.libros_disponibles:
                print("No hay libros disponibles en este momento.")
            else:
                for libro in mi_biblioteca.libros_disponibles.values():
                    print(libro)

        elif opcion == '7':
            print("\n--- USUARIOS REGISTRADOS ---")
            if not mi_biblioteca.usuarios:
                print("No hay usuarios registrados.")
            else:
                for usuario in mi_biblioteca.usuarios.values():
                    print(usuario)
                    if usuario.libros_prestados:
                        print("   📖 Libros en su poder:")
                        for lib in usuario.libros_prestados:
                            print(f"      - {lib.titulo}")

        elif opcion == '8':
            print("Saliendo del sistema... ¡Tus datos están seguros en 'datos_biblioteca.txt'!")
            break
        else:
            print("❌ Opción no válida. Intenta de nuevo.")


if __name__ == "__main__":
    menu_interactivo()