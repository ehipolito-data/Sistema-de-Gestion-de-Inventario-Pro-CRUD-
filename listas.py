def cargar_archivo():
    try:
        with open('lista_productos.txt', "r") as file:
            productos = file.read().splitlines()
            return productos
    except FileNotFoundError:
        productos = []

def mostrar_producto(productos):
    for producto in productos:
        print(producto)

def guardar_archivo(productos):
    texto_para_guardar = "\n".join(productos)
    with open ('lista_productos.txt', "w") as file:
        file.write(texto_para_guardar)
        print("Productos guardados correctamente")

def agregar_producto(productos):
    producto_agregar_cliente = input("¿Qué producto deseas agregar?")
    productos.append(producto_agregar_cliente)
    print("Producto agregado correctamente")
    print(productos)

def eliminar_producto(productos):
    try:
        producto_eliminar_cliente = input("¿Qué producto deseas eliminar?")
        productos.remove(producto_eliminar_cliente)
        print("Eliminado correctamente")
        print(productos)
    except:
        print("Este producto no se encuentra en la lista")

def mostrar_menu():
    opcion_menu = input("""
    1. Ver inventario.
    2. Agregar producto.
    3. Eliminar producto.
    4. Guardar y Salir.
    Seleccione una opción: """)
    return opcion_menu

lista = cargar_archivo()

while True:
    opcion_menu = mostrar_menu()
    if opcion_menu == "1": 
        mostrar_producto(lista)
    elif opcion_menu == "2": 
        agregar_producto(lista)
    elif opcion_menu == "3": 
        eliminar_producto(lista)
    elif opcion_menu == "4": 
        guardar_archivo(lista)
        break
    else:
        print("Opción no valida, intenta otra")









