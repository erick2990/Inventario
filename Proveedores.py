#Archivo proveedores
class Proveedor:

    def __init__(self, id_proveedor, nombre_empresa, cel_proveedor, dir_proveedor, correo_proveedor):
        self.__id_proveedor = id_proveedor
        self.__nombre_empresa = nombre_empresa
        self.__cel_proveedor = cel_proveedor
        self.__dir_proveedor = dir_proveedor
        self.__correo_proveedor = correo_proveedor


    def get_id_proveedor(self):
        return self.__id_proveedor
    def get_empresa_proveedor(self):
        return self.__nombre_empresa
    def get_cel_proveedor(self):
        return self.__cel_proveedor
    def get_dir_proveedor(self):
        return self.__dir_proveedor
    def get_correo_proveedor(self):
        return self.__correo_proveedor
    def set_cel_proveedor(self, nuevo_cel):
        self.__cel_proveedor = nuevo_cel
    def set_dir_proveedor(self, nueva_dir):
        self.__dir_proveedor = nueva_dir
    def set_correo_proveedor(self, nuevo_correo):
        self.__correo_proveedor = nuevo_correo

    def __str__(self): #solo se invoca el objeto
        return (
            f'ID: {self.get_id_proveedor()} | Empresa: {self.get_empresa_proveedor()} | '
            f'Celular: {self.get_cel_proveedor()} | Dirección: {self.get_dir_proveedor()} | '
            f'Correo: {self.get_correo_proveedor()}'
        )

class GestionProveedores:

    def __init__(self):
        self.diccionario_prov = {}
        self.cargar_proveedores()

    def mostrar_proveedores(self):
        if not self.diccionario_prov:
            print('NO HAY PROVEEDORES AÚN')
        else:
            for llave, campo in self.diccionario_prov.items():
                print(f'Información: {campo} ')

    def guardar_proveedores(self, archivo="proveedores.txt"):
        with open(archivo, "w", encoding="utf-8") as f:
            for prov in self.diccionario_prov.values():
                f.write(
                    f"{prov.get_id_proveedor()}:{prov.get_empresa_proveedor()}:{prov.get_cel_proveedor()}:"
                    f"{prov.get_dir_proveedor()}:{prov.get_correo_proveedor()}\n"
                )

    def cargar_proveedores(self, archivo="proveedores.txt"):
        try:
            with open(archivo, "r", encoding="utf-8") as f:
                for linea in f:
                    id_prov, nombre, cel, dir, correo = linea.strip().split(":")
                    proveedor = Proveedor(int(id_prov), nombre, cel, dir, correo)
                    self.diccionario_prov[int(id_prov)] = proveedor
        except FileNotFoundError:
            print("proveedores.txt no encontrado. Se creará al guardar.")


    def agregar_proveedores(self, gestor_categorias):
        fin_agregar = True

        while fin_agregar:
            id_proveedor = len(list(self.diccionario_prov))+2
            print(f'ID de proveedor asignado de forma automática: {id_proveedor}')
            nombre = input('Ingrese el nombre de la empresa: ')
            telefono = input('Ingrese el numero de teléfono: ')
            dir = input('Ingrese la dirección: ')
            correo = input('Ingrese el correo: ')
            proveedor_tmp = Proveedor(id_proveedor, nombre, telefono, dir, correo) #Se crea el proveedor
            self.diccionario_prov[id_proveedor] = proveedor_tmp #se agrega al diccionario de proveedores
            print('Proveedor guardado con exito!!!')
            print('\nAsocie el proveedor con la categoria que provee: \n\n')
            gestor_categorias.mostrar_categorias() #muestra las categorias disponibles
            while True:
                print(F'PRESIONE (0) PARA FINALIZAR LA ASIGNACIÓN DE CATEGORIAS AL PROVEEDOR {nombre}')
                cat_asociada = int(input('\nIngrese la categoria que desea asociar con el actual proveedor: '))
                if cat_asociada in gestor_categorias.diccionario_cat.keys(): #se verifica si esta en las llaves
                   categroria_objeto = gestor_categorias.diccionario_cat[cat_asociada]
                   if proveedor_tmp in categroria_objeto.listado_proveedores:
                       print('Esta proveedor ya fue asociado intente con otra categoria')
                   else:
                       categroria_objeto.agregar_proveedor_categoria(proveedor_tmp) #Se envia el objeto proveedor para ser guardado
                       print('¡¡¡Proveedor asociado con éxito!!!\n')
                if cat_asociada== 0:
                    print('Asociaciones terminadas')
                    break

            while True:
                print('\n\n')
                agregar = input('¿DESEA INGRESAR OTRO PROVEEDOR? S/N: ').upper()
                if agregar == "S":
                    break
                elif agregar == "N":
                    print('Registros Guardados')
                    fin_agregar = False
                    break
                else:
                    print('Entrada no valida por favor intentarlo de nuevo')




