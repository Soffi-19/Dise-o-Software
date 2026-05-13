def main():

    prendas = []

    cantidad_prendas = int(input("Digite la cantidad de prendas: "))

    for i in range(cantidad_prendas):
        print(f"Prenda {i + 1}:")

        nombre = input("Digite el nombre de la prenda: ")
        precio = float(input("Digite el precio de la prenda: "))
        unidades = int(input("Digite las unidades vendidas: "))

        prenda = {
            "nombre": nombre,
            "precio": precio,
            "unidades": unidades
        }

        prendas.append(prenda)

    ventas_totales = 0

    for p in prendas:
        ventas_totales += p["precio"] * p["unidades"]

    print("El total de ventas del día es:", ventas_totales)

if __name__ == "__main__":
    main()