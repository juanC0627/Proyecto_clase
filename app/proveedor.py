class Proveedor(Bodega):

    #constructor

    def __init__(self, nombre_proveedor, direccion, telefono, lista_prod, nombre_bodega, ubicacion, capacidad_max):
        super().__init__(nombre_bodega, ubicacion, capacidad_max)
        self.nombre_proveedor = nombre_proveedor
        self.direccion = direccion
        self.telefono = telefono
        self.lista_prod = lista_prod
        