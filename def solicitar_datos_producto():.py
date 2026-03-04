def solicitar_datos_producto():
    cantidad = float(input("Ingrese la cantidad de producto: "))
    precio_compra = float(input("Ingrese el precio de compra por unidad: "))
    precio_venta = float(input("Ingrese el precio de venta por unidad: "))
    transporte = float(input("Ingrese el costo de transporte: "))
    impuestos = float(input("Ingrese el valor de impuestos: "))

    return cantidad, precio_compra, precio_venta, transporte, impuestos


def calcular_costos_y_ingresos(cantidad, precio_compra, precio_venta, transporte, impuestos):
    costo_bruto = cantidad * precio_compra
    ingreso = cantidad * precio_venta
    costo_neto = costo_bruto + transporte + impuestos

    return costo_bruto, ingreso, costo_neto


def mostrar_resultados(total_ingresos, utilidad_bruta, utilidad_neta):
    print("\n----- RESULTADOS FINALES -----")
    print(f"Total ingresos: {total_ingresos}")
    print(f"Utilidad bruta: {utilidad_bruta}")
    print(f"Utilidad neta: {utilidad_neta}")


def main():
    total_ingresos = 0
    total_costos_brutos = 0
    total_costos_netos = 0

    while True:
        respuesta = input("\n¿Desea ingresar un producto? (si/no): ").lower()
        if respuesta != "si":
            break

        cantidad, precio_compra, precio_venta, transporte, impuestos = solicitar_datos_producto()

        costo_bruto, ingreso, costo_neto = calcular_costos_y_ingresos(
            cantidad, precio_compra, precio_venta, transporte, impuestos
        )

        total_ingresos += ingreso
        total_costos_brutos += costo_bruto
        total_costos_netos += costo_neto

    utilidad_bruta = total_ingresos - total_costos_brutos
    utilidad_neta = total_ingresos - total_costos_netos

    mostrar_resultados(total_ingresos, utilidad_bruta, utilidad_neta)


if __name__ == "__main__":
    main()