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
    def __init__(self):
        self.admin = Admin("Erick", "Erick2000")


    def inicio_sesion(self):
        intentos = 3
        while intentos > 0:
            user = input("Usuario: ")
            password = getpass.getpass("Contraseña: ")
            if user == self.admin.get_usuario() and password == self.admin.get_password():
                print("Inicio de sesión exitoso.")
                return True
            else:
                intentos -= 1
                print(f"Credenciales incorrectas. Intentos restantes: {intentos}")
        print(" Se agotaron los intentos.")
        return False


class EntornoAdmin:

    def menu_admin(self, gestor_categorias, gestor_proveedores, gestor_productos, gestor_compras, gestor_empleados, gestor_ventas):
        fin_admin = True

        while fin_admin:
            try:
                print('\n')
                print('--- Bienvenido Administrador ---')
                print('1. Ingresar Categorías \n2. Ingresar Proveedor \n3. Realizar Compra PRODUCTOS NUEVOS / Abastecer existentes \n4. Historial de compras')
                print('5. Contratar Trabajadores \n6. Mostrar Cajeros \n7. Historial de Ventas\n8. Mostrar Productos \n9. Modificar precios V/C')
                print('10. Salir')
                opcion = int(input('Seleccione la opción: '))
                match opcion:
                    case 1:
                        gestor_categorias.agregar_categorias() #Ingreso de cat
                    case 2:
                        print('Listado de proveedores actuales: ') #Ingreso de proveedores
                        gestor_proveedores.mostrar_proveedores()
                        print('\n')
                        gestor_proveedores.agregar_proveedores(gestor_categorias)
                    case 3: #Compras tanto de nuevo producto como de abastecimiento
                        print('\n')
                        while True:
                            try:
                                print(
                                    '1. Ingresar compra de productos NUEVOS \n2. Ingresar compra de productos EXISTENTES')
                                print('3. Salir')
                                opcion_s = int(input('Ingrese la opción a la que desee ingresar: '))
                                match opcion_s:
                                    case 1:
                                        print('\nIngreso de productos nuevos: ')
                                        gestor_compras.realizar_compra(gestor_productos, gestor_categorias)

                                    case 2:
                                        print('\nAbastecimiento productos: ')
                                        gestor_compras.realizar_abastecimiento(gestor_productos)
                                    case 3:
                                        print('Regresando a menu admin')
                                        break
                                    case _:
                                        print('Opción invalida - Ingrese un dato correcto')
                            except Exception as e:
                                print(f'Error por favor verifique el submenu {e}')
                            print('Datos vacíos no se pueden realizar las compras')
                    case 4:
                        print('\nHistorial de compras: ') #Historial de compras realizadas a proveedores
                        gestor_compras.mostrar_compras()

                    case 5:
                        print('Contrato de personal: ') #Creaciond de los empleados
                        gestor_empleados.agregar_empleado()  # Aquí se crean los trabajadores

                    case 6:
                        print('\n')  # Muestra los empleados actuales
                        gestor_empleados.mostrar_empleados()
                    case 7:
                        print('Historial Ventas: ')
                        gestor_ventas.mostrar_ventas()
                    case 8:
                        print('Productos existentes: ')
                        gestor_productos.mostrar_productos()
                    case 9:
                        print('Modificar precios:')
                        if not gestor_productos.diccionario_productos:
                            print('No hay productos aún')
                        else:
                            gestor_productos.modificar_precio_venta_compra()

                    case 10:
                        print('Saliendo del modo administrador')
                        print('---'*40)
                        fin_admin = False
                    case _:
                        print('Opción invalida por favor verifique nuevamente')

            except Exception as e:
                print('Ocurrió un error en el menú de administrador por favor verificar')

class Invitado:

    def mostrar_productos_invitado(self, gestor_productos):
        gestor_productos.mostrar_productos()

    def mostrar_proveedores_invitado(self, gestor_proveedores):
        gestor_proveedores.mostrar_proveedores()

    def mostrar_categorias_invitado(self, gestor_categorias):
        gestor_categorias.mostrar_categorias()


