# Definición de la Clase Base
class Vehiculo:
    def __init__(self, marca, modelo, costo_dia):
        self.marca = marca
        self.modelo = modelo
        # ENCAPSULACIÓN: El atributo '__costo_dia' es privado (doble guion bajo)
        # Solo se puede acceder o modificar a través de métodos de la clase.
        self.__costo_dia = costo_dia

    # Método público para mostrar información general
    def mostrar_info(self):
        return f"Vehículo: {self.marca} {self.modelo}"

    # Método para calcular alquiler (será sobrescrito para demostrar polimorfismo)
    def calcular_alquiler(self, dias):
        return self.__costo_dia * dias

    # Getter para acceder al atributo privado (parte de la encapsulación)
    def get_costo_dia(self):
        return self.__costo_dia

    # Setter para modificar el atributo privado de forma controlada
    def set_costo_dia(self, nuevo_costo):
        if nuevo_costo > 0:
            self.__costo_dia = nuevo_costo
        else:
            print("El costo debe ser positivo.")

# HERENCIA: La clase AutoDeportivo hereda de la clase Vehiculo
class AutoDeportivo(Vehiculo):
    def __init__(self, marca, modelo, costo_dia, caballos_fuerza):
        # Llamada al constructor de la clase base (super)
        super().__init__(marca, modelo, costo_dia)
        self.caballos_fuerza = caballos_fuerza

    # POLIMORFISMO: Sobreescritura del método 'mostrar_info'
    # Modificamos el comportamiento original para incluir los caballos de fuerza
    def mostrar_info(self):
        info_base = super().mostrar_info()
        return f"{info_base} (Edición Deportiva: {self.caballos_fuerza} HP)"

    # POLIMORFISMO: Sobreescritura de 'calcular_alquiler'
    # Los deportivos tienen un cargo extra del 20% por seguro premium
    def calcular_alquiler(self, dias):
        costo_base = self.get_costo_dia() * dias
        return costo_base * 1.20  # Agrega 20% extra

# --- Bloque Principal de Ejecución ---
if __name__ == "__main__":
    print("--- SISTEMA DE GESTIÓN DE VEHÍCULOS ---\n")

    # Instanciación de objetos (Crear instancias)
    mi_sedan = Vehiculo("Toyota", "Corolla", 50)
    mi_ferrari = AutoDeportivo("Ferrari", "488 Spider", 500, 660)

    # Demostración de Encapsulación y Getters
    # print(mi_sedan.__costo_dia) # Esto daría error porque es privado
    print(f"Costo base del Sedan: ${mi_sedan.get_costo_dia()}")

    # Demostración de Polimorfismo en acción
    vehiculos = [mi_sedan, mi_ferrari]

    for v in vehiculos:
        print("-" * 30)
        print(v.mostrar_info())
        # El mismo método 'calcular_alquiler' actúa diferente según el objeto
        costo_3_dias = v.calcular_alquiler(3)
        print(f"Costo alquiler por 3 días: ${costo_3_dias:.2f}")