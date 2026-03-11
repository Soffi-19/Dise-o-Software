# Dise-o-Software
# Venta de ropa


Me han contratado como desarrollador para una aplicación software para una empresa que permita la administración del registro de la venta de sus prendas de vestir y la gestión de cada una de ellas. La empresa maneja la venta
de camisas y busos oversize. La aplicación debe registrar el precio de cada una de las prendas además de registrar el cálculo de las ventas generadas por día.

 # Aclaraciones
• La aplicación se limita únicamente al cálculo y registro financiero.

• No se contempla la gestión de inventario, entradas de mercancía o existencias (stock).


• El enfoque principal es la relación entre el precio unitario y las unidades vendidas para obtener el recaudo diario.


# Historia de usuario
**Título:** Registro y gestión de ventas de ropa. 

•	**Como:** Dependiente de la Tienda

•	**Quiero:** Ingresar los datos de cada prenda (nombre, precio y registro de ventas)

•	**Para:** Calcular y registrar las ventas generadas por día.

# Descripción
 
El sistema debe registra la venta por día y gestionar el stock de las prendas. 

# Requisitos del Sistema
•	**Registro de Precios:** Configurar el nombre y precio unitario de camisas y busos oversize.

•	**Cálculo de Ventas:** Procesar la operación

    Venta = Precio * Unidades.


•	**Recaudo Diario:** Mostrar el total acumulado de dinero ingresado en el día.

# Criterios de aceptación

* El sistema permite registrar nuevas camisas y busos oversize ingresando su nombre y precio inicial.

* El sistema permite visualizar el total acumulado de dinero (ventas) recaudado durante el día actual.

# Diagrama UML

![Use Case Diagram](https://github.com/user-attachments/assets/edf06edf-aa36-4fc7-9cdd-02742bf8019a)


# Caso de uso extendido
Nombre: Registrar y Gestionar Ventas de Ropa 
Actores: Dependiente de la Tienda 
Propósito: Registrar los datos de las prendas y calcular el total de ventas     diarias.


# Curso de eventos:
1.	El Dependiente ingresa la cantidad de tipos de prendas a registrar (Camisas o Busos Oversize).
2.	Para cada tipo de prenda:
	* El Dependiente ingresa el nombre de la prenda.

    * El Dependiente ingresa el precio unitario.
    * La aplicación almacena los datos de la prenda.

3.	El sistema calcula la venta individual de cada tipo de prenda mediante la operación:

    *	    unidades vendidas × precio unitario.
4.	Acumula cada resultado en una variable que representa el total de ventas generadas por día.
Postcondición: El total de ventas del día ha sido calculado y el stock de prendas ha sido actualizado.

# Diagrama de flujo

![Diagrama de flujo](https://github.com/user-attachments/assets/683bf26d-add8-440d-ba10-b70f5f4805ba)


 # Pseudocódigo
**Inicio** 

    Caracteres: nombresPrendas[50], nombre 
    Real: precios[50], ventasDiarias <- 0, precio, unidades
    Entero: numeroPrendas, i

    Imprimir: ' Configuración de Precios '
    Imprimir: 'Digite el número de tipos de prendas a registrar:'
    Asignar: numeroPrendas

    Para i = 0 hasta numeroPrendas - 1, 1
        Imprimir: 'Nombre de la prenda:'
        Asignar: nombre
        Imprimir: 'Precio unitario de venta:'
        Asignar: precio
        
        nombresPrendas[i] <- nombre
        precios[i] <- precio
    FinPara

    Imprimir: 'Registro de Ventas del Día '
    
    Para i = 0 hasta numeroPrendas - 1, 1
        Imprimir: '¿Cuántas unidades se vendieron de: ' + nombresPrendas[i] + '?'
        Asignar: unidades
        
        ventasDiarias <- ventasDiarias + (unidades * precios[i])
    FinPara
    Imprimir: '-------------------------------------------'
    Imprimir: 'EL TOTAL DE VENTAS DEL DÍA ES: $' + ventasDiarias
    Imprimir: 'Registro financiero finalizado.'
Fin




