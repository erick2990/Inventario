import Perfiles
import Categorias
import Proveedores

class Datos:
    def __init__(self, nombre_em, direccion):
        self.__empresa = nombre_em
        self.__direccion = direccion

    def get_empresa(self):
        return self.__empresa

    def get_direccion(self):
        return self.__direccion

def registrar_empresa():
     while True:
         print('\t\t\tBienvenido al sistema de inventarios')
         nombre_empresa = input('Ingrese el nombre de la empresa: ')
         if nombre_empresa == "":
            print(' Por favor ingrese un nombre válido.')
            continue
         direccion = input('Ingrese la dirección de la empresa: ')
         if direccion == "":
            print('Por favor ingrese una dirección válida.')
            continue
         empresa = Datos(nombre_empresa, direccion)  # guardar los datos de la empresa
         print('Datos guardados correctamente.')
         return empresa #retorna datos de la empresa


def menu_principal(empresa):
        fin_menu = True
        administrador = Perfiles.LoginAdmin() #contiene  el inicio de sesion
        dinamica_admin = Perfiles.EntornoAdmin() #Contiene la dinamica para el menu admin
        gestor_categorias = Categorias.GestionCategorias() #Contiene la dinamica para gestionar las categorias
        gestor_proveedores =  Proveedores.GestionProveedores()

        while fin_menu:
            try:
                print(f'\t\tSistema de control para la empresa {empresa.get_empresa()} ubicacion: {empresa.get_direccion()}')
                print('1. Ingresar como Administrador \n2. Ingresar como cajero \n3. Ingresar como visitante')
                print('4. Salir del programa')
                opcion  =int(input('Digite la opcion que desea ingresar: '))
                match opcion:
                    case 1:
                        print('Administrador')
                        if administrador.inicio_sesion():
                            print('ACCEDIENDO COMO ADMINISTRADOR....\n')
                            dinamica_admin.menu_admin(gestor_categorias, gestor_proveedores)
                        else:
                            print('Por favor intente más tarde')
                    case 2:
                        print('Cajero')
                    case 3:
                        print('Visitante')
                    case 4:
                        print('Gracias por usar el sistema')
                        fin_menu = False
                    case _:
                        print('Error por favor ingrese una entrada valida')
            except Exception as e:
                print('Error por favor verifique la entrada del menu principal')

empresa_trabajar = registrar_empresa() #Toma los valores que se ingresan para esta empresa
menu_principal(empresa_trabajar) #Se mantiene mientras este en ejecucion






