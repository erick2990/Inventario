import getpass
#archivo perfiles

class Admin:
    def __init__(self, usuario, password):
        self.__usuario = usuario
        self.__password = password
    def get_usuario(self):
        return self.__usuario
    def get_password(self):
        return self.__password

class LoginAdmin:
    admin = Admin('Erick', 'Erick2000') #Aqui se instancia un objeto de tipo admin para que pueda iniciarse sesion
    def inicio_sesion(self):
        intentos = 3
        while intentos>0:
            try:
                user = input('Ingrese su usuario: ')
                password =  getpass.getpass('Ingrese su contraseña: ')
                if user == self.admin.get_usuario() and password == self.admin.get_password():
                    print('¡¡Inicio de sesión Exitoso!!')
                    return True
                else:
                    intentos -=1
                    print(f'Le quedan {intentos}')
            except Exception as e:
                print('Error por favor verifique la entrada')
        print('Se terminaron los intentos validos')

class EntornoAdmin:
    print('clase para el admin')

    def menu_admin(self, gestor_categorias, gestor_proveedores, gestor_productos, gestor_compras, gestor_empleados):
        fin_admin = True

        while fin_admin:
            try:
                print('--- Bievenido Administrdor ---')
                print('1. Ingresar Categorías \n2. Ingresar Proveedor \n3. Realizar Compra / Abastecer/ HISTORIAL \n4. Mostrar Categorias')
                print('5. \n6. Modificar producto \n7. Salir')
                opcion = int(input('Seleccione la opción: '))
                match opcion:
                    case 1:
                        gestor_categorias.agregar_categorias()
                    case 2:
                        print('\n')
                        gestor_proveedores.agregar_proveedores(gestor_categorias)
                    case 3:
                        print('\n')
                        if gestor_categorias.diccionario_cat and gestor_proveedores.diccionario_prov:
                            while True:
                                try:
                                    print('1. Ingresar compra de productos NUEVOS \n2. Ingresar compra de productos EXISTENTES\n3. Mostrar compras')
                                    print('\n4. Contratar Trabajadores  \n5. Salir')
                                    opcion_s = int(input('Ingrese la opción a la que desee ingresar: '))
                                    match opcion_s:
                                        case 1:
                                            print('\nIngreso de productos nuevos: ')
                                            gestor_compras.realizar_compra(gestor_productos, gestor_categorias)

                                        case 2:
                                            print('\nAbasecimiento productos: ')
                                            gestor_compras.realizar_abastecimiento(gestor_productos)

                                        case 3:
                                            print('\nHistorial de compras: ')
                                            gestor_compras.mostrar_compras()
                                        case 4:
                                            print('Contrato de personal: ')
                                            gestor_empleados.agregar_empleado() #Aqui se crean los trabajadores
                                        case 5:
                                            print('Regresando a menu admin')
                                            break
                                        case _:
                                            print('Opción invalida - Ingrese un dato correcto')
                                except Exception as e:
                                    print(f'Error por favor verifique el submenu {e}')
                        else:
                            print('Datos vacios no se pueden realizar las compras')
                    case 4:
                        print('\n')
                        gestor_categorias.mostrar_categorias()
                    case 5:
                        print('Empleados')
                    case 6:
                        print('Administrador puede cambiar/ pCompra/pVenta/Stock/proveedor')
                    case 7:
                        print('Saliendo del modo administrador')
                        fin_admin = False
                    case _:
                        print('Opción invalida por favor verifique nuevamente')

            except Exception as e:
                print('Ocurrio un error en el menú de administrador por favor verificar')


