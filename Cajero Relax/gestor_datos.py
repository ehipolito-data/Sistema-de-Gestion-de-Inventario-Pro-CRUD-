import json
from modelos import Producto

def cargar_datos(archivo):
    try:
        with open(archivo, 'r') as file:
            datos_json = json.load(file)
            lista_objetos = []
            for d in datos_json:
                nuevo_obj = Producto(d["nombre"], d["precio"], d["stock"])
                lista_objetos.append(nuevo_obj)
            return lista_objetos
    except FileNotFoundError:
        return []

def guardar_datos(lista, archivo):

    lista_diccionarios = [obj.to_dict() for obj in lista] 

    with open(archivo, 'w') as file:
        json.dump(lista_diccionarios, file, indent=4)
    print("Base de datos actualizada.")