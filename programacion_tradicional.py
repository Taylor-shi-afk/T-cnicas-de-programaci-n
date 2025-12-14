
def ingresar_temperaturas():
    """Función para la entrada de datos de temperaturas diarias."""
    temperaturas = []
    dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

    print("--- Ingreso de Temperaturas (Programación Tradicional) ---")
    for dia in dias:
        while True:
            try:
                temp = float(input(f"Ingrese la temperatura del {dia}: "))
                temperaturas.append(temp)
                break
            except ValueError:
                print("Error: Por favor, ingrese un valor numérico válido.")
    return temperaturas


def calcular_promedio(temperaturas):
    """Función para el cálculo del promedio semanal."""
    if not temperaturas:
        return 0
    return sum(temperaturas) / len(temperaturas)


def main():
    """Función principal para organizar la lógica del programa."""
    datos_clima = ingresar_temperaturas()
    promedio = calcular_promedio(datos_clima)

    print("\n--- Resultados ---")
    print(f"El promedio semanal de temperatura es: {promedio:.2f}°C")


if __name__ == "__main__":
    main()