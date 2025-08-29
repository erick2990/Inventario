#arcivo compras
from datetime import  datetime
from Productos import Producto

class Compra:
    def __init__(self, id_compra, fecha):
        self.__id_compra = id_compra
        self.__fecha =  fecha
        self.diccionario_articulos_comprados = {}

    def get_id_compra(self):
        return self.__id_compra
    def get_fecha(self):
        return self.__fecha

    def __str__(self):
        resumen = f"Compra ID: {self.__id_compra} | Fecha: {self.__fecha}\nArtículos comprados:\n"
        for id_prod, producto in self.diccionario_articulos_comprados.items():
            resumen += f" - {producto.get_nombre_product()} (ID: {id_prod}) | Q{producto.get_precio_venta():.2f} x {producto.get_stock()} unidades\n"
        return resumen

class GestionCompras:
    def __init__(self):
        self.diccionario_historial_compras = {} #Se guardaran todas las compras que se realizan
        self.cargar_compras()

    def mostrar_compras(self):
        for llave, campo in self.diccionario_historial_compras.items():
            print(f'Compra: {llave}')
            print(f'{campo}')

    def guardar_compras(self, archivo="compras.txt"):
        with open(archivo, "w", encoding="utf-8") as f:
            for compra in self.diccionario_historial_compras.values():
                linea = f"{compra.get_id_compra()}|{compra.get_fecha()}"
                for id_prod, prod in compra.diccionario_articulos_comprados.items():
                    linea += f"|{id_prod},{prod.get_nombre_product()},{prod.get_precio_venta():.2f},{prod.get_stock()}"
                f.write(linea + "\n")

    def cargar_compras(self, archivo="compras.txt"):
        try:
            with open(archivo, "r", encoding="utf-8") as f:
                for linea in f:
                    partes = linea.strip().split("|")
                    id_compra = int(partes[0])
                    fecha = partes[1]
                    compra = Compra(id_compra, fecha)
                    for prod_data in partes[2:]:
                        id_prod, nombre, precio, cantidad = prod_data.split(",")
                        producto = Producto(nombre, int(id_prod), 0, 0, 0, float(precio), int(cantidad))
                        compra.diccionario_articulos_comprados[int(id_prod)] = producto
                    self.diccionario_historial_compras[id_compra] = compra
        except FileNotFoundError:
            print("compras.txt no encontrado. Se creará al guardar.")


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