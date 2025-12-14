
class InformacionClima:
    """Clase base que representa la información diaria del clima."""
    def __init__(self):
        
        self.__temperaturas = []

    def ingresar_datos(self):
        """Método para ingresar las temperaturas de la semana."""
        dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
        print("--- Ingreso de Datos (Enfoque POO) ---")
        for dia in dias:
            while True:
                try:
                    val = float(input(f"Ingrese temperatura de {dia}: "))
                    self.__temperaturas.append(val)
                    break
                except ValueError:
                    print("Error: Ingrese un número válido.")

    def calcular_promedio_semanal(self):
        """Método para realizar el cálculo del promedio."""
        if not self.__temperaturas:
            return 0
        return sum(self.__temperaturas) / len(self.__temperaturas)


class ReporteClima(InformacionClima):
    def mostrar_resumen(self):
        promedio = self.calcular_promedio_semanal()
        print("\n--- Reporte Final de Clima ---")
        print(f"Promedio calculado: {promedio:.2f}°C")

def ejecutar_programa():

    reporte = ReporteClima()
    reporte.ingresar_datos()
    reporte.mostrar_resumen()

if __name__ == "__main__":
    ejecutar_programa()