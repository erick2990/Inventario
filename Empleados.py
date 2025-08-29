#Archivo empleados
class Empleados:
    def __init__(self, id_empleado, nombre, telefono, direccion, correo):
        self.__id_empleado = id_empleado
        self.__nombre = nombre
        self.telefono = telefono
        self.direccion = direccion
        self.correo = correo
        self.ventas = {} #Este empleado tendra un record de ventas que ha realizado

    def get_id_empleado(self):
        return self.__id_empleado
    def get_nombre_empleado(self):
        return self.__nombre


    def __str__(self):
        resumen = (
            f"Empleado: {self.get_nombre_empleado()} | ID: {self.get_id_empleado()}\n"
            f"Teléfono: {self.telefono} | Dirección: {self.direccion} | Correo: {self.correo}\n"
        )
        if self.ventas:
            resumen += f"Ventas realizadas: {len(self.ventas)}\n"
            for id_venta, venta in self.ventas.items():
                resumen += f"  - Venta ID: {id_venta} | Detalles: {venta}\n"
        else:
            resumen += "No ha realizado ventas aún.\n"
        return resumen

class GestionEmpleados:

    def __init__(self):
        self.diccionario_empleados = {}
        self.cargar_empleados()


    def agregar_empleado(self):
        print('\t\tIngrese los datos adecuados para el nuevo trabajador: ')
        id_empleado = len(list(self.diccionario_empleados)) + 2
        nombre = input('Nombre: ')
        print(f'El ID: {id_empleado}  se asignara al trabajador: {nombre}')
        telefono = input('Teléfono: ')
        direccion = input('Dirección: ')
        correo = input('Correo electrónico: ')
        empleado_tmp = Empleados(id_empleado, nombre, telefono, direccion, correo)
        self.diccionario_empleados[id_empleado] = empleado_tmp #se guarda el empleado introducido en el diccionario de empelados
        self.guardar_empleados()
        print('¡¡Empleado guardado de forma exitosa!!')

    def existencia_valida(self, id_vendedor):
        # Metodo que retorna True si el id es correcto para la asociacion de la venta
        return id_vendedor in self.diccionario_empleados

    def acreditar_venta(self, id_empleado, objeto_venta):
        if id_empleado in self.diccionario_empleados:
            id_venta = objeto_venta.get_id_venta()  # Getter de la venta asociada para asociar el objeto con ese mismo ID
            self.diccionario_empleados[id_empleado].ventas[id_venta] = objeto_venta
            print(f" Venta acreditada al empleado {id_empleado}")
        else:
            print("Empleado no encontrado.")

    def guardar_empleados(self, archivo="empleados.txt"):
        with open(archivo, "w", encoding="utf-8") as f:
            for id_empleado, emp in self.diccionario_empleados.items():
                f.write(
                    f"{id_empleado}:{emp.get_nombre_empleado()}:{emp._Empleados__telefono}:{emp.direccion}:{emp.correo}\n")

    def cargar_empleados(self, archivo="empleados.txt"):
        try:
            with open(archivo, "r", encoding="utf-8") as f:
                for linea in f:
                    id_empleado, nombre, telefono, direccion, correo = linea.strip().split(":")
                    self.diccionario_empleados[int(id_empleado)] = Empleados(int(id_empleado), nombre, telefono,
                                                                             direccion, correo)
        except FileNotFoundError:
            print("empleados.txt no encontrado. Se creará al guardar.")






