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
    def get_fecha_venta(self):
        return self.__fecha_venta
    def get_id_empleado(self):
        return self.__id_empleado
    def get_nit(self):
        return self.__nit


    def __str__(self):
        resumen = (
            f"Venta ID: {self.get_id_venta()} | Fecha: {self.get_fecha_venta()}\n"
            f"Empleado ID: {self.get_id_empleado()} | Cliente NIT: {self.get_nit()}\n"
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
        self.diccionario_ventas_generales = {}
        self.cargar_ventas()

    def guardar_ventas(self, archivo="ventas.txt"):
        with open(archivo, "w", encoding="utf-8") as f:
            for venta in self.diccionario_ventas_generales.values():
                linea = f"{venta.get_id_venta()}|{venta.get_fecha_venta()}|{venta.get_id_empleado()}|{venta.get_nit()}|{venta.total_venta}"
                for id_prod, prod in venta.productos.items():
                    linea += f"|{id_prod},{prod.get_nombre_product()},{prod.get_precio_venta():.2f},{prod.get_stock()}"
                f.write(linea + "\n")

    def cargar_ventas(self, archivo="ventas.txt"):
        try:
            with open(archivo, "r", encoding="utf-8") as f:
                for linea in f:
                    partes = linea.strip().split("|")
                    id_venta = int(partes[0])
                    fecha = partes[1]
                    id_empleado = int(partes[2])
                    nit = partes[3]
                    total = float(partes[4])
                    venta = Venta(id_venta, fecha, id_empleado, nit)
                    venta.total_venta = total
                    for prod_data in partes[5:]:
                        id_prod, nombre, precio, cantidad = prod_data.split(",")
                        producto = Producto(nombre, int(id_prod), 0, 0, 0, float(precio), int(cantidad))
                        venta.productos[int(id_prod)] = producto
                    self.diccionario_ventas_generales[id_venta] = venta
        except FileNotFoundError:
            print("ventas.txt no encontrado. Se creará al guardar.")

    def mostrar_ventas(self):
        print("\nHistorial de ventas registradas:\n")
        if not self.diccionario_ventas_generales:
            print("No hay ventas registradas aún.\n")
            return

        for id_venta, venta in self.diccionario_ventas_generales.items():
            print(f"Venta #{id_venta}")
            print(venta)
            print("-" * 40)

    def realizar_venta(self, gestor_clientes, gestor_empleados, gestor_productos):
        print('\t\t\tSistema de ventas:')
        id_venta = len(list(self.diccionario_ventas_generales)) + 5 #Id de las ventas de forma automática
        fecha_actual = datetime.now().date()  # guarda la fecha
        print(f'{fecha_actual} \nID Venta: {id_venta} asignado de forma automática')
        while True:
            try:
                id_vendedor = int(input('Ingrese su ID de cajero: '))
                if gestor_empleados.existencia_valida(id_vendedor):
                    print('Acceso Valido...')
                    break
                else:
                    print('Por favor verifique su PIN')
                    return

            except  Exception as e:
                print(f'Ocurrió un error en ventas por favor verificar {e}')
        while True:
            try:
                nit = input('NIT cliente:  ')
                if  gestor_clientes.cliente_existe(nit):  #Si ya existe entonces no agrega nada solo se queda en el nit
                    print('El cliente ya existe!')
                    break

                else:
                    gestor_clientes.agregar_cliente(nit) #si el NIT no existe entonces guarda un nuevo cliente
                    break
            except Exception as e:
                print('Ocurrió un error en la asociación del cliente con la compra')

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

        self.diccionario_ventas_generales[id_venta] = compra_tmp #se guarda la compra en el historial de compras
        gestor_empleados.acreditar_venta(id_vendedor, compra_tmp) #se acredita la venta al empleado correspondiente
        gestor_clientes.asociar_compra_cliente(nit, compra_tmp) #se asocia la compra al cliente que le atendimos
        print("\nVenta registrada exitosamente:")
        print(compra_tmp)






