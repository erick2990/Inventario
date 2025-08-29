#archivo clientes
class Clientes:
    def __init__(self, nit,nombre, telefono):
        self.__nit = nit
        self.__nombre = nombre
        self.telefono = telefono
        self.compras = {}  # Compras que ha realizado el cliente

    def get_nit(self):
        return self.__nit
    def get_nombre(self):
        return self.__nombre


    def __str__(self):
        resumen = (
            f"Cliente: {self.get_nombre()} | NIT: {self.get_nit()}\n"
            f"Teléfono: {self.telefono}\n"
        )
        if self.compras:
            resumen += f"Compras realizadas: {len(self.compras)}\n"
            for id_compra, compra in self.compras.items():
                resumen += f"  - Compra ID: {id_compra} | Detalles: {compra}\n"
        else:
            resumen += "No ha realizado compras aún.\n"
        return resumen

class GestionClientes:

    def __init__(self):
        self.diccionario_clientes = {}
        self.cargar_clientes()

    def agregar_cliente(self):
        nit = input("Ingrese el NIT del cliente: ")
        if nit in self.diccionario_clientes:
            print("⚠Este NIT ya está registrado.")
            return
        nombre = input("Ingrese el nombre del cliente: ")
        telefono = input("Ingrese el número de teléfono: ")
        cliente_tmp = Clientes(nit, nombre, telefono)
        self.diccionario_clientes[nit] = cliente_tmp
        self.guardar_clientes()
        print("Cliente agregado exitosamente.")

    def cliente_existe(self, nit):
        return nit in self.diccionario_clientes

    def asociar_compra_cliente(self, nit, objeto_comprado):
        if nit in self.diccionario_clientes:
            id_venta = objeto_comprado.get_id_venta()  # o usa un getter si lo tienes
            self.diccionario_clientes[nit].compras[id_venta] = objeto_comprado
            print(f"Compra asociada al cliente {nit}")
        else:
            print("Cliente no encontrado. No se puede asociar la compra.")

    def guardar_clientes(self, archivo="clientes.txt"):
        with open(archivo, "w", encoding="utf-8") as f:
            for nit, cliente in self.diccionario_clientes.items():
                f.write(f"{nit}:{cliente.get_nombre()}:{cliente.get_telefono}\n")

    def cargar_clientes(self, archivo="clientes.txt"):
        try:
            with open(archivo, "r", encoding="utf-8") as f:
                for linea in f:
                    nit, nombre, telefono = linea.strip().split(":")
                    self.diccionario_clientes[nit] = Clientes(nit, nombre, telefono)
        except FileNotFoundError:
            print(" clientes.txt no encontrado. Se creará al guardar.")



