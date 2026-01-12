"""
Descripción del Programa:
Este programa calcula el costo total de un viaje basándose en el destino,
la duración y el gasto diario estimado. También verifica si el costo total
está dentro de un presupuesto máximo definido.
"""


def main():
    # --- Definición de variables (Entradas) ---

    # Tipo de dato: String (Cadena de texto)
    destino_viaje = "París"

    # Tipo de dato: Integer (Entero)
    dias_estadia = 5

    # Tipo de dato: Float (Decimal)
    gasto_diario_promedio = 120.50
    presupuesto_maximo = 550.00

    # --- Procesamiento (Lógica) ---

    # Calculamos el costo total multiplicando días por gasto diario
    costo_total_viaje = dias_estadia * gasto_diario_promedio

    # Tipo de dato: Boolean (Verdadero/Falso)
    # Comprobamos si el costo total es menor o igual al presupuesto
    esta_en_presupuesto = costo_total_viaje <= presupuesto_maximo

    # --- Salidas (Resultados) ---
    print(f"--- Planificación de Viaje a {destino_viaje} ---")
    print(f"Días de estadía: {dias_estadia}")
    print(f"Costo total estimado: ${costo_total_viaje:.2f}")

    # Estructura condicional básica para dar un mensaje final
    if esta_en_presupuesto:
        print("Resultado: ¡El viaje está dentro del presupuesto!")
    else:
        print("Resultado: El viaje excede el presupuesto, necesitas ahorrar más.")


# Ejecutar la función principal
if __name__ == "__main__":
    main()