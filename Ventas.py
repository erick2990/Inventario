from datetime import  datetime
from Productos import Producto

#Archivo ventas

class Venta:
    def __init__(self, id_venta, fecha_venta, id_empleado , nit):
        self.__id_venta = id_venta
        self.__fecha_venta = fecha_venta
        self.__id_empleado = id_empleado
        self.__nit = nit
        self.productos = {}
        self.total_venta = 0

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
        resumen += f"Total de la venta: Q{self.total_venta:.2f}\n"
        return resumen

class GestionVentas:

    def __init__(self):
        self.diccioanrio_ventas_generales = {}

    def mostrar_ventas(self):
        print("\nHistorial de ventas registradas:\n")
        if not self.diccioanrio_ventas_generales:
            print("No hay ventas registradas aún.")
            return

        for id_venta, venta in self.diccioanrio_ventas_generales.items():
            print(f"Venta #{id_venta}")
            print(venta)
            print("-" * 40)

    def realizar_venta(self, gestor_clientes, gestor_empleados, gestor_productos):
        print('Logica de venta')
        id_venta = len(list(self.diccioanrio_ventas_generales)) + 5 #Id de las ventas de forma automatica
        fecha_actual = datetime.now().date()  # guarda la fecha
        print(f'{fecha_actual} \nID Venta: {id_venta} asignado de forma automatica')
        while True:
            try:
                id_vendedor = int(input('Ingrese su ID de cajero: '))
                if gestor_empleados.existencia_valida(id_vendedor):
                    print('Acceso Valido...')
                    break
                else:
                    print('Por favor verifique su PIN')

            except  Exception as e:
                print(f'Ocurrio un error en ventas por favor verificar {e}')
        while True:
            try:
                nit = input('NIT cliente:  ')
                if  gestor_clientes.existencia_valida(nit):  #Si ya existe entonces no agrega nada solo se queda en el nit
                    print('El cliente ya existe!')
                    break

                else:
                    gestor_clientes.agregar_cliente() #si el NIT no existe entonces gurrda un nuevo clinete
                    break
            except Exception as e:
                print('Ocurrio un error en la asociacion del cliente con la compra')

        compra_tmp = Venta(id_venta, fecha_actual, id_vendedor, nit)

        while True:
            try:
                id_producto = int(input('Ingrese el ID del producto: '))
                if gestor_productos.producto_existe(id_producto):
                    producto = gestor_productos.diccionario_productos[id_producto]
                    print(
                        f"Producto: {producto.get_nombre_product()} | Precio: Q{producto.get_precio_venta():.2f} | Stock disponible: {producto.get_stock()}")

                    cantidad = int(input('Ingrese la cantidad que desea comprar: '))
                    if cantidad > 0 and cantidad <= producto.get_stock():
                        # Crear una copia del producto con la cantidad deseada
                        producto_vendido = Producto(
                            producto.get_nombre_product(),
                            producto.get_id_producto(),
                            producto.get_id_categoria(),
                            producto.get_id_proveedor(),
                            producto.get_precio_compra(),
                            producto.get_precio_venta(),
                            cantidad
                        )
                        # Agregar al objeto Venta
                        compra_tmp.productos[id_producto] = producto_vendido
                        # Calcular subtotal
                        subtotal = producto.get_precio_venta() * cantidad
                        compra_tmp.total_venta += subtotal
                        # Actualizar stock en inventario
                        nuevo_stock = producto.get_stock() - cantidad
                        producto._Producto__stock = nuevo_stock

                        print(f"Producto agregado a la venta. Subtotal: Q{subtotal:.2f}")
                    else:
                        print("Cantidad inválida o insuficiente stock.")
                else:
                    print('Producto no existe. Intente nuevamente.')
            except Exception as e:
                print(f'Error en el escaneo de productos: {e}')

            continuar = input('¿Desea agregar otro producto? S/N: ').upper()
            if continuar == 'N':
                print('Compra finalizada')
                break

        self.diccioanrio_ventas_generales[id_venta] = compra_tmp #se guarda la compra en el historial de compras
        gestor_empleados.acreditar_venta(id_vendedor, compra_tmp) #se acredita la venta al empleado correspondiente
        gestor_clientes.asociar_compra_cliente(nit, compra_tmp) #se asocia la compra al cliente que le atendimos
        print("\nVenta registrada exitosamente:")
        print(compra_tmp)






