class Producto:
    def __init__(self, nombre, id_producto, id_categoria, id_proveedor, precio_compra, precio_venta, stock):
        self.__nombre =  nombre
        self.__id_producto = id_producto
        self.__id_categoria = id_categoria
        self.__id_proveedor = id_proveedor
        self.__precio_compra = precio_compra
        self.__precio_venta = precio_venta
        self.__ganancia = (precio_venta - precio_compra) * stock
        self.__stock = stock

    def get_nombre_product(self):
        return self.__nombre
    def get_id_producto(self):
        return self.__id_producto
    def get_id_categoria(self):
        return self.__id_categoria
    def get_id_proveedor(self):
        return self.__id_proveedor
    def get_precio_venta(self):
        return self.__precio_venta
    def get_precio_compra(self):
        return self.__precio_compra
    def get_stock(self):
        return self.__stock

    def set_precio_compra(self, nuevo_precio_compra):
        if nuevo_precio_compra>0:
            self.__precio_compra = nuevo_precio_compra
            print('¡Cambio de precio de compra exitoso!')
        else:
            print('Valor no valido')
    def set_precio_venta(self, nuevo_precio_venta):
        if nuevo_precio_venta>self.__precio_compra:
            self.__precio_venta = nuevo_precio_venta
            print('¡Cambio de precio de venta exitoso!')
        else:
            print('El precio de venta debe ser mayor para obtener ganancias')
    def set_stock(self, nuevo_stock):
        if nuevo_stock>0:
            self.__stock = nuevo_stock
        else:
            print('El stock debe ser mayor a 0')

    def __str__(self):
        return (
            f'Producto: {self.__nombre} | ID: {self.__id_producto} | '
            f'Categoría: {self.__id_categoria} | Proveedor: {self.__id_proveedor} | '
            f'Compra: Q{self.__precio_compra:.2f} | Venta: Q{self.__precio_venta:.2f} | '
            f'Ganancia: Q{self.__ganancia:.2f} | Stock: {self.__stock} unidades'
        )


class GestionProductos:

    def __init__(self):
        self.diccionario_productos = {}

    def mostrar_productos(self):
        if not self.diccionario_productos:
            print('Diccionario vació')

        for llave, campo in self.diccionario_productos.items():
            print(f'ID Producto: {llave}')
            print(f'{campo}')


    #metodo para añadir productos nuevos o empezar de 0
    #el gesto de categorias es el vinculo para unir los ID de la categoria y los ID de los proveedores
    def agregar_productos(self, gestor_categorias):

        global id_proveedor_categoria
        fin_agregar_p = True
        productos_nuevos = {} #Este diccionario sirve para enviar a las compras
        print('\t\tAñadir productos nuevos al inventario\n\n')
        while fin_agregar_p:
            print('\t\tINGRESE LOS DATOS CORRESPONDIENTES DEL PRODUCTO:')
            nombre_producto = input('Ingrese el nombre: ')      #nombre producto
            id_producto = len(list(self.diccionario_productos)) + 20 #El Id del producto se creara de forma automatica
            print(f'El ID del producto {nombre_producto} es: {id_producto}')
            while True:
                try:
                    precio_compra = float(input('Ingrese el precio de compra: Q.')) #Precio compra
                    if precio_compra > 0:
                        break
                    else:
                        print('Ingrese un precio mayor a Q.0')
                except Exception as e:
                    print('Ocurrió un error en el ingreso de precio compra - inténtelo nuevamente')
            while True:
                try:
                    precio_venta = float(input('Ingrese el precio de venta: Q.')) #precio venta
                    if precio_venta > precio_compra :
                        break
                    else:
                        print('Ingrese un precio mayor al precio de compra, ya que se deben obtener ganancias')
                except Exception as e:
                    print(f'Ocurrió un error en el ingreso de precio venta - inténtelo nuevamente {e}')
            while True:
                try:
                    stock = int(input('Ingrese las unidades de producto comprado: ')) #stock
                    if stock>0:
                        break
                    else:
                        print('El stock debe ser mayor a 0 unidades')
                except Exception as e:
                    print(f'Ocurrió un error en el ingreso de stock - inténtelo nuevamente {e}')


            print('\nSe desplegara el listado de categorias y respectivos proveedores, ingrese el ID de cada uno según se indique')
            gestor_categorias.mostrar_categorias() #Despliegue de categorias y proveedores
            while True:
                try:
                    id_categoria_producto = int(input('Ingrese el ID de la categoria: '))
                    if id_categoria_producto in gestor_categorias.diccionario_cat.keys():
                        buscar = True
                        while buscar:
                            try:
                                id_proveedor_categoria = int(input(f'Ingrese el ID del proveedor de la categoria {id_categoria_producto}: '))
                                proveedores_asociados = gestor_categorias.diccionario_cat[id_categoria_producto].listado_proveedores #se devuelve como lista
                                proveedor_valido = False
                                for x in proveedores_asociados:
                                    if id_proveedor_categoria == x.get_id_proveedor():
                                        proveedor_valido = True
                                        break
                                if proveedor_valido:
                                    buscar = False
                                else:
                                    print('El ID ingresado no corresponde a un proveedor asociado a esta categoría.')

                            except Exception as e:
                                print(f'Ocurrió un error en asociar proveedor por favor verifique {e}')
                        break #termina el while principal
                    else:
                        print('El ID de la categoria que intenta asociar no existe por favor verifique la entrada')
                except Exception as e:
                    print(f'Ocurrió un error por favor verifique la entrada {e}')
            #Se instancia el objeto
            producto_tmp = Producto(nombre_producto, id_producto, id_categoria_producto, id_proveedor_categoria, precio_compra, precio_venta, stock)
            self.diccionario_productos[id_producto] = producto_tmp #se guarda el producto en el diccionario general
            productos_nuevos[id_producto] = producto_tmp #Se guarda en el diccionario de retorno
            while True:
                print('\n\n')
                agregar = input('¿Desea ingresar otro Producto? S/N: ').upper()
                if agregar == "S":
                    break
                elif agregar == "N":
                    print('Registros Guardados')
                    fin_agregar_p= False
                    return productos_nuevos
                else:
                    print('Entrada no valida por favor intentarlo de nuevo')

    def abastecer(self):
        print('\nAbastecimiento de productos existentes\n')

        if not self.diccionario_productos:
            print('No hay productos registrados para abastecer.')
            return

        self.mostrar_productos()

        while True:
            try:
                id_producto = int(input('\nIngrese el ID del producto que desea abastecer: '))
                if id_producto in self.diccionario_productos:
                    producto = self.diccionario_productos[id_producto]
                    print(
                        f'Producto seleccionado: {producto.get_nombre_product()} | Stock actual: {producto.get_stock()} unidades')

                    while True:
                        try:
                            cantidad = int(input('Ingrese la cantidad que se sumara al stock: '))
                            if cantidad > 0:
                                nuevo_stock = producto.get_stock() + cantidad
                                producto.set_stock(nuevo_stock)
                                print(f'Stock actualizado. Nuevo stock: {nuevo_stock} unidades.')
                                break
                            else:
                                print('La cantidad debe ser mayor a 0.')
                        except Exception as e:
                            print(f'Error al ingresar cantidad. Detalle: {e}')
                else:
                    print('El ID ingresado no corresponde a ningún producto.')
            except Exception as e:
                print(f' Error al ingresar el ID. Detalle: {e}')

            continuar = input('\n¿Desea abastecer otro producto? S/N: ').upper()
            if continuar == 'N':
                print('Abastecimiento finalizado.')
                break
            elif continuar != 'S':
                print('Entrada no válida. Se asumirá que no desea continuar.')
                break
