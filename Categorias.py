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
        self.listado_proveedores.append(objeto_proveedor) #se guarda unicamente por ID ya que es la llave foranea

    def eliminar_proveedor(self, id_proveedor):
        print(f'Eliminando proveedor {id_proveedor}')
        self.listado_proveedores.remove(id_proveedor)
        print('Proveedor eliminado')

    def __str__(self):
        proveedores = ', '.join(self.listado_proveedores) if self.listado_proveedores else 'Sin proveedores asociados'
        return f'ID: {self.get_id_categoria()}  Nombre: {self.get_nombre_categoria()}  Proveedores: {proveedores}'

class GestionCategorias:

    def __init__(self, gestor_proveedores):
        self.diccionario_cat = {}
        self.cargar_categorias(gestor_proveedores)


    def guardar_categorias(self, archivo="categorias.txt"):
        with open(archivo, "w", encoding="utf-8") as f:
            for id_cat, cat in self.diccionario_cat.items():
                proveedores_ids = [str(p.get_id_proveedor()) for p in cat.get_listado_proveedores()]
                f.write(f"{id_cat}:{cat.get_nombre_categoria()}:{','.join(proveedores_ids)}\n")

    def cargar_categorias(self, gestor_proveedores, archivo="categorias.txt"): #este metodo de cargar es distinto porque se inica desde proveedores porque puede provenir desde alli
        try:
            with open(archivo, "r", encoding="utf-8") as f:
                for linea in f:
                    id_cat, nombre, proveedores_str = linea.strip().split(":")
                    categoria = Categoria(int(id_cat), nombre)
                    if proveedores_str:
                        for pid in proveedores_str.split(","):
                            pid_int = int(pid)
                            if pid_int in gestor_proveedores.diccionario_prov:
                                proveedor_obj = gestor_proveedores.diccionario_prov[pid_int]
                                categoria.agregar_proveedor_categoria(proveedor_obj)
                    self.diccionario_cat[int(id_cat)] = categoria
        except FileNotFoundError:
            print("categorias.txt no encontrado. Se creará al guardar.")

    def mostrar_categorias(self):
        if not self.diccionario_cat:
            print('NO HAY CATEGORIAS AÚN')

        else:
            for llave, campo in self.diccionario_cat.items():
                print(f'ID CATEGORIA: {llave} NOMBRE CATEGORIA: {campo.get_nombre_categoria()}')
                print(f'LISTADO PROVEEDORES: ')
                for x in campo.get_listado_proveedores():
                    print(f'Empresa: {x.get_empresa_proveedor()} ID_PROVEEDOR: {x.get_id_proveedor()} ')
                print('\n')

    def agregar_categorias(self):
        fin_agregar = True

        print('Ingrese todos los datos correspondientes: \n\n')

        while fin_agregar:
            try:
                print('\n')
                print('\t\t\tINRGRESE 0 PARA CANCELAR EL PROCESO')
                id_categoria = len(list(self.diccionario_cat)) +1 #El ID que tomara es por defecto y empieza en 1
                print(f'ID de categoria automático: {id_categoria}')
                nombre_categoria = input('Ingrese el nombre de la categoria: ').upper()
                if int(nombre_categoria) == 0:
                    print('Regresando...')
                    break
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
                print(f'Error - Por favor verificar agregar categorías {e}')

