class Producto:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock 

    def __str__(self):
        return f"Producto: {self.nombre} | Precio: {self.precio:.2f} | Stock: {self.stock}"
    
    def to_dict(self):
        return {
            "nombre": self.nombre,
            "precio": self.precio,
            "stock": self.stock
        }

    def vender(self, cantidad):
        if cantidad <= self.stock:
            self.stock -= cantidad
            print(f"Venta exitosa: {cantidad} {self.nombre}(s) vendidos.")
        else:
            print(f"Error: no hay suficiente stock de {self.nombre}.")
    
    def aplicar_descuento(self, porcentaje):
        self.precio -= self.precio * (porcentaje / 100)
        print(f"Se aplicó el descuento de {porcentaje}%")


#mis_juguetes = [Producto("Buzz", 600, 5), Producto("Woody", 500, 10)]

#for juguete in mis_juguetes:
    #print(juguete)

