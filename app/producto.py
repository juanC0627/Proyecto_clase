class Producto(Bodega):

    #constructor

    def __init__(self, nombre, descripcion, precio, stock, categoria, nombre_bodega, ubicacion, capacidad_max):
        super().__init__(nombre_bodega, ubicacion, capacidad_max)
        self.nombre = nombre
        self.descripcion = descripcion
        self.precio = precio
        self.stock = stock
        self.categoria = categoria