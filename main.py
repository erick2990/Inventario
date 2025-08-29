import Clientes
import Compras
import Perfiles
import Categorias
import Productos
import Proveedores
import Empleados
import Ventas

#archivo main
class Datos:
    def __init__(self, nombre_em, direccion):
        self.__empresa = nombre_em
        self.__direccion = direccion

    def get_empresa(self):
        return self.__empresa

    def get_direccion(self):
        return self.__direccion

def registrar_empresa():
        nombre_empresa = "Ferreteria"
        direccion = "23 avenida zona 3"
        empresa = Datos(nombre_empresa, direccion)  # guardar los datos de la empresa
        print('Datos guardados correctamente.')
        return empresa #retorna datos de la empresa


def menu_principal(empresa):
        fin_menu = True
        administrador = Perfiles.LoginAdmin() #contiene  el inicio de sesion
        dinamica_admin = Perfiles.EntornoAdmin() #Contiene la dinamica para el menu admin
        gestor_categorias = Categorias.GestionCategorias() #Contiene la dinamica para gestionar las categorias
        gestor_proveedores =  Proveedores.GestionProveedores()
        gestor_productos = Productos.GestionProductos()
        gestor_compras = Compras.GestionCompras()
        gestor_empleados = Empleados.GestionEmpleados()
        gestor_clientes = Clientes.GestionClientes()
        gestor_ventas = Ventas.GestionVentas()

        while fin_menu:
            try:
                print('\n')
                print(f'\t\tSistema de control para la empresa {empresa.get_empresa()} ubicacion: {empresa.get_direccion()}')
                print('\t1. Ingresar como Administrador \n\t2. Ingresar como cajero \n\t3. Ingresar como visitante')
                print('\t4. Salir del programa')
                opcion = int(input('Digite la opción que desea ingresar: '))
                match opcion:
                    case 1:
                        print('Administrador')
                        if administrador.inicio_sesion():
                            print('ACCEDIENDO COMO ADMINISTRADOR....\n')
                            dinamica_admin.menu_admin(gestor_categorias, gestor_proveedores, gestor_productos, gestor_compras, gestor_empleados, gestor_ventas)
                        else:
                            print('Por favor intente más tarde')
                    case 2:
                        print('\nCajero')
                        gestor_ventas.realizar_venta(gestor_clientes, gestor_empleados, gestor_productos)
                    case 3:
                        print('\nVisitante')
                        print('Funcion en construccion')

                    case 4:
                        print('Gracias por usar el sistema')
                        #guardamos todos los datos
                        gestor_clientes.guardar_clientes()
                        gestor_empleados.guardar_empleados()
                        gestor_productos.guardar_productos()
                        gestor_proveedores.guardar_proveedores()
                        gestor_categorias.guardar_categorias()
                        gestor_compras.guardar_compras()
                        gestor_ventas.guardar_ventas()
                        break
                    case _:
                        print('Error por favor ingrese una entrada valida')
            except Exception as e:
                print('Error por favor verifique la entrada del menu principal')

empresa_trabajar = registrar_empresa() #Toma los valores que se ingresan para esta empresa
print('\n\n')
menu_principal(empresa_trabajar) #Se mantiene mientras este en ejecucion






