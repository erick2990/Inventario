import getpass

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
                password =  getpass.getpass('Ingrese su contraseña')
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

    def menu_admin(self):
        fin_admin = True
        while fin_admin:
            try:
                print('--- Bievenido Administrdor ---')
                print('1.Ingresar Categorías 2.Ingresar Proveedor \n3. Realizar Compra \n4. Historial Compras')
                print('5. Modificar producto \n6. Salir')
                opcion = int(input('Seleccione la opción: '))
                match opcion:
                    case 1:
                        print('Ingreso categorias como unica tarea')
                    case 2:
                        print('Ingreso de proveedor modo manual')
                    case 3:
                        print('Compra ingresando id producto/categoria/proveedor(nuevo/existente)')
                    case 4:
                        print('Historial de compras')
                    case 5:
                        print('Administrador puede cambiar/ pCompra/pVenta/Stock/proveedor')
                    case 6:
                        print('Saliendo del modo administrador')
                        fin_admin = False
                    case _:
                        print('Opción invalida por favor verifique nuevamente')

            except Exception as e:
                print('Ocurrio un error en el menú de administrador por favor verificar')


