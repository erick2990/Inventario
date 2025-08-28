#archivo categorias
class Categoria:

    def __init__(self,id_categoria ,nombre_categoria):
        self.__id_categoria = id_categoria
        self.__nombre_categoria = nombre_categoria
        self.listado_proveedores = []

    def get_id_categoria(self):
        return self.__id_categoria
    def get_nombre_categoria(self):
        return self.__nombre_categoria
    def get_listado_proveedores(self):
        return self.listado_proveedores


    def agregar_proveedor_categoria(self, objeto_proveedor):
        print(f'Proveedor {objeto_proveedor}')
        self.listado_proveedores.append(objeto_proveedor) #se guarda unicamente por ID ya que es la llave foranea

    def eliminar_proveedor(self, id_proveedor):
        print(f'Eliminando proveedor {id_proveedor}')
        self.listado_proveedores.remove(id_proveedor)
        print('Proveedor eliminado')

    def __str__(self):
        proveedores = ', '.join(self.listado_proveedores) if self.listado_proveedores else 'Sin proveedores asociados'
        return f'ID: {self.__id_categoria}  Nombre: {self.__nombre_categoria}  Proveedores: {proveedores}'

class GestionCategorias:

    def __init__(self):
        self.diccionario_cat = {}
    def diccionario_categorias(self):
        return self.diccionario_cat
    def diccionario_llaves_categorias(self): #retorna el diccionario como un entero
        return self.diccionario_cat.keys()

    def mostrar_categorias(self):
        for llave, campo in self.diccionario_cat.items():
            print(f'ID CATEGORIA: {llave} NOMBRE CATEGORIA: {campo.get_nombre_categoria()}')
            print(f'LISTADO PROVEEDORES: ')
            for x in campo.get_listado_proveedores():
                print(f'Empresa: {x.get_empresa_proveedor()} ID_PROVEEDOR: {x.get_id_proveedor()} ')
            print('\n')

    def agregar_categorias(self):
        fin_agregar = True

        print('Ingrese todos los datos correspodientes: \n\n')

        while fin_agregar:
            try:

                id_categoria = len(list(self.diccionario_cat)) +1 #El ID que tomara es automatico y empieza en 1
                print(f'ID de categoria automatico: {id_categoria}')
                nombre_categoria = input('Ingrese el nombre de la categoria: ').upper()
                existencia_nombres = [cat.get_nombre_categoria().upper() for cat in self.diccionario_cat.values()] #lista por comprension
                if nombre_categoria in existencia_nombres:
                    print('Este nombre ya existe por favor vuelva a intentarlo') #Esto valida que le nombre no se repita

                else:
                    categoria_tmp = Categoria(id_categoria, nombre_categoria)
                    self.diccionario_cat[id_categoria] = categoria_tmp  # se añade este objeto al diccionario y se guarda
                    print('¡¡Categoria asociada con éxito!!\n')
                    while True:
                        agregar = input('¿Desea ingresar otra categoria? S/N: ').upper()
                        if agregar == "S":
                            break
                        elif agregar == "N":
                            print('Registros Guardados')
                            self.mostrar_categorias()
                            fin_agregar = False
                            break
                        else:
                            print('Entrada no valida por favor intentarlo de nuevo')

            except Exception as e:
                print(f'Error - Por favor verificar agregar categorias {e}')

