class Prenda:
    def __init__(self, nombre, precio, unidades):
        self.nombre = nombre
        self.precio = precio
        self.unidades = unidades
    
    def total_venta(self):
        return self.precio * self.unidades

def main():
    prendas = []
    ventas_totales = 0

    cantidad_prendas = int(input("Digite la cantidad de prendas: "))

    for i in range(cantidad_prendas):
        print(f"Prenda {i + 1}: ")

        nombre = input("Digite el nombre de la prenda: ")
        precio = float(input("Digite el precio de la prenda: "))
        unidades = int(input("Digite las unidades vendidas: "))

        prenda = Prenda(nombre, precio, unidades)
        prendas.append(prenda)

    ventas_totales = sum(
        p.total_venta()
        for p in prendas
    )

    print(f"El total de ventas del día es: {ventas_totales}")

if __name__ == "__main__":
    main()