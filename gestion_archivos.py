
class GestorDeArchivo:
    def __init__(self, nombre_archivo):
        """
        Constructor (__init__): Se ejecuta al crear el objeto.
        Aquí inicializamos los atributos y abrimos el archivo en modo escritura.
        """
        self.nombre_archivo = nombre_archivo
        print(f"--> Constructor: Creando el objeto y abriendo el archivo '{self.nombre_archivo}'.")
        # Simulamos la apertura de un archivo para escribir datos
        self.archivo = open(self.nombre_archivo, 'w')

    def guardar_dato(self, dato):
        """
        Método simple para escribir información en el archivo.
        """
        if self.archivo:
            self.archivo.write(dato + '\n')
            print(f"    [Info]: Guardando '{dato}' en el archivo.")

    def __del__(self):
        """
        Destructor (__del__): Se ejecuta cuando el objeto está a punto de ser destruido.
        Es CRÍTICO aquí cerrar el archivo para evitar pérdida de datos o consumo de memoria.
        """
        if self.archivo:
            self.archivo.close()
        print(
            f"--> Destructor: El objeto ha sido eliminado y el archivo '{self.nombre_archivo}' se cerró correctamente.")


# Bloque principal de ejecución
if __name__ == "__main__":
    print("--- Inicio del Programa ---")

    # 1. Creación del objeto (Se llama a __init__)
    gestor = GestorDeArchivo("notas_clase.txt")

    # 2. Uso del objeto
    gestor.guardar_dato("Aprendiendo constructores")
    gestor.guardar_dato("Aprendiendo destructores")

    print("--- Fin del bloque de uso ---")

    # 3. Eliminación manual del objeto para forzar la demostración del destructor
    # Nota: Python lo haría automáticamente al final, pero 'del' lo hace visible ahora.
    del gestor

    print("--- Fin del Programa ---")