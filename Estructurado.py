prendas = []
precios = []
unidades_vendidas = []

cantidad_prendas = int(input("Digite la cantidad de prendas: "))

for i in range(cantidad_prendas):
    print(f"Prenda {i + 1}:")
    
    prenda = input("Digite el nombre de la prenda: ")
    precio = float(input("Digite el precio de la prenda: "))
    unidades = int(input("Digite las unidades vendidas: "))
    
    prendas.append(prenda)
    precios.append(precio)
    unidades_vendidas.append(unidades)

ventas_totales = 0

for i in range(cantidad_prendas):
    ventas_totales = ventas_totales + (precios[i] * unidades_vendidas[i])

print("El total de ventas del día es:", ventas_totales)