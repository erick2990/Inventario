from datetime import  datetime

from pcbnew import VECTOR_VECTOR2I


#Archivo ventas

class Venta:
    def __init__(self, id_venta, fecha_venta, id_empleado , nit, productos, total):
        self.__id_venta = id_venta
        self.__fecha_venta = fecha_venta
        self.__id_empleado = id_empleado
        self.__nit = nit
        self.productos = productos
        self.__total = total

    def get_id_venta(self):
        return self.__id_venta

    def __str__(self):
        resumen = (
            f"Venta ID: {self.__id_venta} | Fecha: {self.__fecha_venta}\n"
            f"Empleado ID: {self.__id_empleado} | Cliente NIT: {self.__nit}\n"
            f"Productos vendidos:\n"
        )
        for id_prod, producto in self.productos.items():
            resumen += (
                f"  - {producto.get_nombre_product()} (ID: {id_prod}) | "
                f"Precio: Q{producto.get_precio_venta():.2f} | "
                f"Cantidad: {producto.get_stock()} unidades\n"
            )
        resumen += f"Total de la venta: Q{self.__total:.2f}\n"
        return resumen

class GestionVentas:

    def __init__(self):
        self.diccioanrio_ventas_generales = {}


    def realizar_venta(self, gestor_clientes, gestor_empleados):
        print('Logica de venta')
        id_venta = len(list(self.diccioanrio_ventas_generales)) + 5 #Id de las ventas de forma automatica
        fecha_actual = datetime.now().date()  # guarda la fecha
        print(f'{fecha_actual} \nID Venta: {id_venta} asignado de forma automatica')
        while True:
            try:
                id_vendedor = int(input('Ingrese su ID de cajero: '))
                if gestor_empleados.existencia_valida():
                    print('Acceso Valido...')
                    break
                else:
                    print('Por favor verifique su PIN')

            except  Exception as e:
                print(f'Ocurrio un error en ventas por favor verificar {e}')
        while True:
            try:
                nit = input('NIT cliente:  ')

            except Exception as e:
                print('Ocurrio un error en la asociacion del cliente con la compra')



