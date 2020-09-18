import os
import datetime
from datetime import date
from datetime import datetime
class Producto:
    def __init__(self, nombre, cantidad, costo):
        self.nombre = nombre
        self.cantidad = cantidad
        self.costo = costo

    @staticmethod
    def ingresar_producto(conn, data):
        productos = []
        for i in data:
            insert = {
                'producto': i.nombre,
                'cantidad': int(i.cantidad),
                'costo': i.costo
            }
            productos.append(insert)

        if productos:
            conn.insertar_registros('productos', productos)

    @staticmethod
    def generar_reporte(conn):
        productos = conn.obtener_registros('productos',{
            "cantidad" : {
                "$gt" : 1
            }
        })
        if(len(productos) == 0):
            return "No hay productos disponibles"
            pass
        try:
            #fecha_actual = datetime.today().strftime("%d_%m_%Y-%H_%M_%S")
            file = open(f'productos_enStock.txt', 'w')
            fila_productos = ''
            n = 1
            for i in productos:
                fila_productos += f'N° {i["_id"]}, Nombre: {i["producto"]}, Cantidad: {i["cantidad"]}, Costo: {i["costo"]}\n'
                n += 1
            file.write(fila_productos)
            #print(f'Se genero el reporte de productos: reporteProductos_{fecha_actual}.txt')
            return fila_productos
        except Exception as e:
            print(f'{str(e)}')
        finally:
            if file:
                file.close()
