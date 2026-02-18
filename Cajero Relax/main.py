from gestor_datos import cargar_datos, guardar_datos
from modelos import Producto

def mostrar_inventario(lista):
    total = 0
    for producto in lista:
        print(f'El producto {producto.nombre} cuesta {producto.precio} y hay {producto.stock} en existencia')
        total += producto.precio * producto.stock
    print(f"El total de todos los productos en stock es {total}")

def buscar_producto(lista):
    nombre_buscado = input("Ingresa el nombre a buscar: ")
    encontrado = False
    for producto in lista:
        if producto.nombre == nombre_buscado:
            print(f'El producto {producto.nombre} cuesta {producto.precio} y hay {producto.stock} en existencia')
            encontrado = True
            break
    
    if not encontrado:
            print(f"Lo siento, {nombre_buscado} no está en el inventario")


def pedir_precio():
    while True:
        try:
            precio = float(input(f"Ingresa el precio del producto: "))
            return precio
        except ValueError:
            print("ERROR: El precio debe de ser un número. Intenta de nuevo.")

def pedir_stock():
    while True:
        try:
            stock = int(input(f"¿Cuantas unidades tenemos de este producto?: "))
            return stock
        except ValueError:
            print("ERROR: El stock debe de ser un número. Intenta de nuevo.")

def agregar_producto(lista):
    nombre_producto = input("Ingresa el nombre del producto: ")
    precio = pedir_precio()
    stock = pedir_stock()
    nuevo_producto = Producto(nombre_producto, precio, stock)
    lista.append(nuevo_producto)
    print("Producto agregado correctamente")


def realizar_venta(lista):
    nombre_vendido = input("¿Qué producto deseas vender?")
    encontrado = False
    for producto in lista:
        if producto.nombre == nombre_vendido:
            while True:
                try:
                    cantidad = int(input(f"¿Cuántas unidades de {nombre_vendido} deseas vender?: "))
                    if cantidad < 0: 
                        print("No puedes vender cantidades negativas.")
                        continue 
                    producto.vender(cantidad)
                    encontrado = True
                    return 
                except ValueError:
                    print("Por favor ingresa un número entero positivo para realizar la venta")

    if not encontrado:
        print(f"El producto {nombre_vendido} no está disponible o no existe")

def actualizar_precio(lista):
    nombre_buscado = input("Ingresa el nombre del producto al cual desea actualizarle el precio: ")
    encontrado = False
    for producto in lista:
        if producto.nombre == nombre_buscado:
            precio_actualizado = pedir_precio()
            producto.precio = precio_actualizado
            print(f"Se ha actualizado correctamente el precio de {producto.nombre} en ${producto.precio}")
            encontrado = True
            return    
    if not encontrado:
            print(f"Lo siento, {nombre_buscado} no está en el inventario")
            
def eliminar_producto(lista):
    producto_buscado = input("¿Cuál es el producto que deseas eliminar?: ")
    for producto in lista:
        if producto_buscado == producto.nombre:
            confirmar = input(f"¿Estas seguro que quieres eliminar el producto {producto.nombre}? (s/n): ")
            if confirmar.lower() == 's':
                lista.remove(producto)
                print("Producto eliminado correctamente")
                return
            else:
                print("Se ha cancelado la operación")
                return
    print("Producto no encontrado")

def mostrar_menu():
    opcion_menu = input("""
    1. Ver inventario.
    2. Buscar producto.
    3. Agregar nuevo producto.                    
    4. Vender producto.
    5. Actualizar precio.
    6. Eliminar producto.
    7. Guardar y salir.
    Seleccione una opción: """)
    return opcion_menu

inventario = cargar_datos("inventario.json")
for producto in inventario:
    print(producto)

while True:
    opcion_menu = mostrar_menu()
    if opcion_menu == "1": 
        mostrar_inventario(inventario)
    elif opcion_menu == "2": 
        buscar_producto(inventario)
    elif opcion_menu == "3":  
        agregar_producto(inventario)
    elif opcion_menu == "4": 
        realizar_venta(inventario)
    elif opcion_menu == "5": 
        actualizar_precio(inventario)
    elif opcion_menu == "6": 
        eliminar_producto(inventario)
    elif opcion_menu == "7": 
        guardar_datos(inventario, "inventario.json")
        break
    else:
        print("Opción no valida, intenta otra")