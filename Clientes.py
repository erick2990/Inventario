class Cliente:
    def __init__(self):
        self.clientes = {}
        self.cargar_clientes()

    def cargar_clientes(self):
        try:
            with open("clientes.txt", "r", encoding="utf-8") as archivo:
                for linea in archivo:
                    linea = linea.strip()
                    if linea :
                        nit, nombre, direccion, telefono, correo = linea.split(":")
                        self.clientes[nit] = {
                            "Nombre": nombre,
                            "Direccion": direccion,
                            "Telefono": telefono,
                            "Correo": correo
                        }
            print("Clientes importados desde clientes.txt")
        except FileNotFoundError:
            print("No existe el archivo clientes.txt, se creará uno nuevo al guardar.")

    def guardar_clientes(self):
        with open("clientes.txt", "w", encoding="utf-8") as archivo:
            for nit, datos in self.clientes.items():
                archivo.write(f"{nit}:{datos['Nombre']}:{datos['Direccion']}:{datos['Telefono']}:{datos['Correo']}\n")

    def agregar_cliente(self, nit, nombre, direccion, telefono, correo):
        self.clientes[nit] = {
            "Nombre": nombre,
            "Direccion": direccion,
            "Telefono": telefono,
            "Correo": correo
        }
        self.guardar_clientes()
        print(f"Cliente con NIT {nit} agregado y guardado correctamente.")

    def mostrar_todos(self):
        if self.clientes:
            print("\nLista de clientes:")
            for nit, datos in self.clientes.items():
                print(f"\nNIT: {nit}")
                for clave, valor in datos.items():
                    print(f"{clave}: {valor}")
        else:
            print("No hay clientes registrados.")


clientes = Clientes()

while True:
    print("\n--- Menú ---")
    print("1. Agregar cliente")
    print("2. Mostrar todos los clientes")
    print("3. Salir")

    opcion = input("Elige una opción: ")

    if opcion == "1":
        nit = input("NIT: ")
        nombre = input("Nombre: ")
        direccion = input("Dirección: ")
        telefono = input("Teléfono: ")
        correo = input("Correo: ")
        clientes.agregar_cliente(nit, nombre, direccion, telefono, correo)

    elif opcion == "2":
        clientes.mostrar_todos()

    elif opcion == "3":
        print("Saliendo del programa...")
        break

    else:
        print("Opción inválida, intenta de nuevo.")