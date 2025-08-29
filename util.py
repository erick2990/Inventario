class Util:
    @staticmethod
    def ordenados(diccionario, clave_func):
        lista = list(diccionario.values())
        if len(lista) <= 1:
            return lista

        pivote = clave_func(lista[0])
        menores = [x for x in lista[1:] if clave_func(x) < pivote]
        iguales = [x for x in lista if clave_func(x) == pivote]
        mayores = [x for x in lista[1:] if clave_func(x) > pivote]

        return (
            Util.ordenados({i: obj for i, obj in enumerate(menores)}, clave_func)
            + iguales +
            Util.ordenados({i: obj for i, obj in enumerate(mayores)}, clave_func)
        )

    def buscar_productos_por_coincidencia(productos, texto_buscado):
        resultados = [] #Se guarda en una lista de productos que coinciden
        texto_buscado = texto_buscado.lower().strip() #Se convierte el texto que se quiere buscar
        for producto in productos.values(): #Se recorre el diccionario
            nombre = producto.get_nombre_product().lower() #Se asigna el nombre del tmp y se compara al buscado
            if texto_buscado in nombre:
                resultados.append(producto) #Se añade al listado de coincidencias el objeto como tal
        return resultados #Retorna la lista


