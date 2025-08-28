from datetime import  datetime

class Compra:
    def __init__(self, id_compra, fecha):
        self.__id_compra = id_compra
        self.__fecha =  fecha
        self.diccionario_articulos_comprados = {}

    def __str__(self):
        resumen = f"Compra ID: {self.__id_compra} | Fecha: {self.__fecha}\nArtículos comprados:\n"
        for id_prod, producto in self.diccionario_articulos_comprados.items():
            resumen += f" - {producto.get_nombre_product()} (ID: {id_prod}) | Q{producto.get_precio_venta():.2f} x {producto.get_stock()} unidades\n"
        return resumen

class GestionCompras:
    def __init__(self):
        self.diccionario_historial_compras = {} #Se guardaran todas las compras que se realizan

    def mostrar_compras(self):
        for llave, campo in self.diccionario_historial_compras.items():
            print(f'Compra: {llave}')
            print(f'{campo}')


    #Aqui se realizan la dinamica de la compra
    def realizar_compra(self, gestor_productos, gestor_categorias):
        print('Aqui la dinamica de la compra')
        id_compra = len(list(self.diccionario_historial_compras)) + 30 #Aqui le asigna de forma atumatica el ID
        fecha_actual  = datetime.now().date() #guarda la fecha
        productos_comprados = gestor_productos.agregar_productos(gestor_categorias)

        #Se crea el objeto y para guardar los productos ingresados
        compra_tmp = Compra(id_compra, fecha_actual)
        compra_tmp.diccionario_articulos_comprados = productos_comprados #aqui se guardan solo los productos comprados
        self.diccionario_historial_compras[id_compra] = compra_tmp #Se guarda la compra en el diccionario de compras

    def realizar_abastecimiento(self, gestor_productos):
        print('Aqui la dinamica de la compra')
        id_compra = len(list(self.diccionario_historial_compras)) + 30  # Aqui le asigna de forma atumatica el ID
        fecha_actual = datetime.now().date()  # guarda la fecha
        productos_abastecidos = gestor_productos.abastecer() #Diccionario de articulos abastecidos

        # Se crea el objeto y para guardar los productos ingresados
        compra_tmp = Compra(id_compra, fecha_actual)
        compra_tmp.diccionario_articulos_comprados = productos_abastecidos  # aqui se guardan solo los productos abastecidos
        self.diccionario_historial_compras[id_compra] = compra_tmp  # Se guarda la compra en el diccionario de compras