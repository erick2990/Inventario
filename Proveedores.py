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
    def set_cel_proveedor(self, nuevo_cel):
        self.__cel_proveedor = nuevo_cel
    def set_dir_proveedor(self, nueva_dir):
        self.__dir_proveedor = nueva_dir
    def set_correo_proveedor(self, nuevo_correo):
        self.__correo_proveedor = nuevo_correo

    def __str__(self): #solo se invoca el objeto
        return (
            f'ID: {self.__id_proveedor} | Empresa: {self.__nombre_empresa} | '
            f'Celular: {self.__cel_proveedor} | Dirección: {self.__dir_proveedor} | '
            f'Correo: {self.__correo_proveedor}'
        )

class GestionProveedores:

    def __init__(self):
        self.diccionario_prov = {}
    def diccionario_proveedores(self):
        return self.diccionario_prov

    def mostrar_proveedores(self):
        for llave, campo in self.diccionario_prov.items():
            print(f'ID: {llave}  Información: {campo} ')


    def agregar_proveedores(self, gestor_categorias):
        fin_agregar = True

        while fin_agregar:
            id_proveedor = len(list(self.diccionario_prov))+2
            print(f'ID de proveedor asignado de forma automatica: {id_proveedor}')
            nombre = input('Ingrese el nombre de la empresa: ')
            telefono = input('Ingrese el numero de teléfono: ')
            dir = input('Ingrese la dirección: ')
            correo = input('Ingrese el correo: ')
            proveedor_tmp = Proveedor(id_proveedor, nombre, telefono, dir, correo) #Se crea el proveedor
            self.diccionario_prov[id_proveedor] = proveedor_tmp #se agrega al diccionario de proveedores

            print('Asocie el proveedor con la categoria que provee: \n\n')
            gestor_categorias.mostrar_categorias() #muestra las categorias disponibles
            while True:
                print('Presione 0 para finalizar la asociación')
                cat_asociada = int(input('\nIngrese la categoria que desea asociar: '))
                if cat_asociada in gestor_categorias.diccionario_cat.keys(): #se verifica si esta en las llaves
                   categroria_objeto = gestor_categorias.diccionario_cat[cat_asociada]
                   if proveedor_tmp in categroria_objeto.listado_proveedores:
                       print('Esta proveedor ya fue asociado intente con otra categoria')
                   else:
                       categroria_objeto.agregar_proveedor_categoria(proveedor_tmp) #Se envia el objeto proveedor para ser guardado
                       print('¡¡¡Proveedor asociado con exito!!!\n')
                if cat_asociada== "0":
                    print('Asociasiones temrinadas')
                    break
                else:
                    print('Esta categoria no existe por favor verifique')
            while True:
                agregar = input('¿Desea ingresar otra Proveedor? S/N: ').upper()
                if agregar == "S":
                    break
                elif agregar == "N":
                    print('Registros Guardados')
                    fin_agregar = False
                    break
                else:
                    print('Entrada no valida por favor intentarlo de nuevo')




