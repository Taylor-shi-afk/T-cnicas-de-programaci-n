#Sistema de Reservas de Hotel
#Este programa utiliza la Programación Orientada a Objetos para gestionar reservas.
#Incluye clases para Habitaciones y Clientes, y gestiona la disponibilidad.


class Cliente:
    """Clase que representa a un cliente del hotel."""

    def __init__(self, nombre, documento):
        self.nombre = nombre
        self.documento = documento

    def __str__(self):
        return f"{self.nombre} (ID: {self.documento})"


class Habitacion:
    """Clase que representa una habitación de hotel."""

    def __init__(self, numero, tipo, precio):
        self.numero = numero
        self.tipo = tipo
        self.precio = precio
        self.esta_ocupada = False  # Atributo para controlar el estado

    def reservar(self):
        """Marca la habitación como ocupada si está disponible."""
        if not self.esta_ocupada:
            self.esta_ocupada = True
            return True
        return False

    def liberar(self):
        """Marca la habitación como libre."""
        self.esta_ocupada = False

    def __str__(self):
        estado = "Ocupada" if self.esta_ocupada else "Disponible"
        return f"Habitación {self.numero} ({self.tipo}) - ${self.precio} - [{estado}]"


class SistemaReservas:
    """Clase para gestionar la interacción entre clientes y habitaciones."""

    def __init__(self):
        self.reservas = []

    def realizar_reserva(self, cliente, habitacion):
        """
        Intenta reservar una habitación para un cliente.
        Demuestra la interacción entre objetos.
        """
        print(f"--- Intentando reservar hab. {habitacion.numero} para {cliente.nombre} ---")
        if habitacion.reservar():
            self.reservas.append({"cliente": cliente, "habitacion": habitacion})
            print(f"¡Éxito! Reserva confirmada para {cliente.nombre} en la habitación {habitacion.numero}.")
        else:
            print(f"Error: La habitación {habitacion.numero} ya está ocupada.")

    def mostrar_reservas(self):
        """Muestra todas las reservas activas."""
        print("\n--- Lista de Reservas Activas ---")
        for reserva in self.reservas:
            print(f"Cliente: {reserva['cliente'].nombre} | {reserva['habitacion']}")


# --- Bloque Principal de Ejecución ---
if __name__ == "__main__":
    # 1. Crear objetos (Instancias)
    cliente1 = Cliente("TAYLOR PONCE ", "0928270222")
    cliente2 = Cliente("TATIANA ARMIJOS ", "1150191954")

    habitacion101 = Habitacion(101, "Simple", 50.00)
    habitacion102 = Habitacion(102, "Doble", 80.00)

    # 2. Inicializar sistema
    hotel = SistemaReservas()

    # 3. Interacción de objetos
    # TAYLOR reserva la 101
    hotel.realizar_reserva(cliente1, habitacion101)

    # TATIANA intenta reservar la 101 (debería fallar porque ya está ocupada)
    hotel.realizar_reserva(cliente2, habitacion101)

    # TATIANA reserva la 102
    hotel.realizar_reserva(cliente2, habitacion102)

    # 4. Mostrar estado final
    hotel.mostrar_reservas()