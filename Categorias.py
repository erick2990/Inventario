class Categoria:

    def __init__(self, nombre_categoria):
        self.__nombre_categoria = nombre_categoria
        self.listado_proveedores = []


    def agregar_proveedor_categoria(self, id_proveedor, objeto):
        print(f'Proveedor {id_proveedor}')
        print(f'Info proveedor desde el objeto')
