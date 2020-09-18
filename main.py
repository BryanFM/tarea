from time import sleep
from connection.conn import Conexion
#from classes.alumno import Alumno
from classes.producto import Producto

conn = Conexion('mongodb://localhost:27017', 'tienda')

def menu():
    while True:
        print('Bienvenido al gestor de datos del colegio Perez de Cuellar')
        print('Seleccione la acción que desea realizar: ')
        print('\t1 - Registrar Productos')
        print('\t2 - Ver Productos en stock')
        print('\t3 - Factura')
        print('\t4 - Salir')
        opcion = input("> ")
        if opcion == "1":
            registrar()
        elif opcion == "2":
            ver_stock()
        elif opcion == "3":
            print("\nNo disponible")
        elif opcion == "4":
            print("\nGracias por usar esta aplicación")
            sleep(1)
            quit()

def ver_stock():
    lista_productos_stock = Producto.generar_reporte(conn)
    print(lista_productos_stock)
    pass

def registrar():
    try:
        lista_productos = []
        nro_productos = int(input('Ingrese el nro de productos : '))

        while True:
            for i in range(nro_productos):
                nombre = input(f'Ingrese el nombre del producto n°{i+1} :')
                cantidad = input(f'Ingrese la cantidad para {nombre} :')
                costo = input(f'Ingrese el costo individual {nombre} :')
                #lista_notas = []
                #for n in range(nro_notas):
                #    nota = int(input(f'Ingrese la nota n°{n+1} : '))
                #    lista_notas.append(nota)

                producto = Producto(nombre, cantidad,costo)
                lista_productos.append(producto)

            if lista_productos:
                Producto.ingresar_producto(conn, lista_productos)

            break

    except Exception as e:
        print(f'{str(e)}')
    pass
menu()