import os


class Alumno:
    def __init__(self, nombre, notas):
        self.nombre = nombre
        self.notas = notas

    @staticmethod
    def ingresar_alumnos(conn, data):
        alumnos = []
        for i in data:
            lista_notas = i.notas
            promedio = sum(lista_notas) / len(lista_notas)
            insert = {
                'alumno': i.nombre,
                'notas': lista_notas,
                'min_nota': min(lista_notas),
                'max_notas': max(lista_notas),
                'promedio': promedio
            }
            alumnos.append(insert)

        if alumnos:
            conn.insertar_registros('alumnos', alumnos)

    @staticmethod
    def generar_reporte(conn):
        alumnos = conn.obtener_registros('alumnos')
        try:
            file = open('alumnos.txt', 'w')
            fila_alumnos = ''
            n = 1
            for i in alumnos:
                fila_alumnos += f'Nro {n}, Nombre: {i["alumno"]}, Notas: {i["notas"]}, Nota Minima: {i["min_nota"]}, Nota Maxima: {i["max_notas"]}, Promedio: {i["promedio"]}\n'
                n += 1
            file.write(fila_alumnos)
            print('Se genero reporte de alumnos')
        except Exception as e:
            print(f'{str(e)}')
        finally:
            if file:
                file.close()
