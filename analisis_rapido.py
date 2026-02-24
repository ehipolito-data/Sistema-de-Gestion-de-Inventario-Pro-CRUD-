import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_json('inventario.json')

def analisis_inventario(df):
    print("--- TU INVENTARIO COMO DATAFRAME ---")
    print(df)
    print("\n--- RESUMEN ESTADISTICO ---")
    print(df.describe())
    df['valor_total_stock'] = df['precio'] * df['stock']
    print("\n--- INVENTARIO VALORIZADO ---")
    print(df[['nombre', 'precio', 'stock', 'valor_total_stock']])

def bajos_stock(df):
    stock_bajo = df[df['stock'] < 5] 
    return stock_bajo

def negativo_precio (df):
    precio_negativo = df[df['precio'] <= 0]
    return precio_negativo

def negativo_stock(df):
    stock_negativo = df[df['stock'] < 0]
    return stock_negativo

def normalizar_datos(df):
    print('Limpieza y normalización de datos')

    #Quitamos espacios en blanco al inicio y al final
    df['nombre'] = df['nombre'].str.strip()

    #Ponemos todo en mayúscula para que no haya duplicados por letras
    df['nombre'] = df['nombre'].str.upper()

    #Verficamos si hay duplicados despúes de limpiar
    duplicados = df.duplicated(subset=['nombre']).sum()
    if duplicados > 0:
        print(f"¡Atención! Se encontraron {duplicados} nombres duplicados.")
        df = df.groupby('nombre').agg({'precio': 'mean', 'stock': 'sum'}).reset_index()
        print("Duplicados fusionados automáticamente. ")
    return df

def validar_datos(df):
    
    total_inicial = len(df)

    precios_negativos = negativo_precio(df)
    stocks_negativos = negativo_stock(df)

    df = df[df['precio'] > 0]   
    df = df[df['stock'] >= 0]

    if not precios_negativos.empty:
        print("Se encontraron productos con precio negativo")
        print(precios_negativos)
    if not stocks_negativos.empty:
        print("Se encontraron productos con stock negativo")
        print(stocks_negativos)

    total_final = len(df)
    eliminados = total_inicial - total_final

    if eliminados > 0:
        print(f"Se han eliminado {eliminados} registros con datos invalidos.")
    else:
        print("Todos los datos son válidos.")

    return df


def reabestecimiento_mostrar(df):
    stock_bajo = bajos_stock(df)
    print("\n---ALERTA DE REABASTECIMIENTO (Stock < 5)---")
    if not stock_bajo.empty:
        print(stock_bajo[['nombre', 'stock']])
    else:
        "Todo en orden, no hay stock bajo"

def exportar_excel(df):
    stock_bajo = bajos_stock(df)
    #Guardamos solo los productos que necesitan reabastecerse
    stock_bajo.to_excel('Alerta_Reabastecimiento.xlsx', index=False)
    print("\n ¡Archivo 'Alerta_Reabestecimiento.xlsx' generado con éxito!")

def simular_inflacion(df, porcentaje=10):
    print(f"\n---Simulación: Incremento por inflación ({porcentaje}%) ---")
    df_sim = df.copy()
    df_sim['precio_inflado'] = df_sim['precio'] * (1 + (porcentaje / 100))
    df_sim['valor_proyectado'] = df_sim['precio_inflado'] * df_sim['stock']

    total_actual = (df['precio'] * df['stock']).sum()
    total_proyectado = df_sim['valor_proyectado'].sum()

    print(f"Valor actual: ${total_actual:,.2f}")
    print(f"Valor proyectado: ${total_proyectado:,.2f}")
    print(f"Incremento patrimonial: ${total_proyectado - total_actual:,.2f}")
    return df_sim

def clasificar_inventario(df):
    print("\n --- SEGMENTACIÓN DE INVENTARIO ---")
    def nivel_stock(cantidad):
        if cantidad < 5: return 'CRÍTICO'
        if cantidad <= 20: return 'NORMAL'
        return 'EXCEDENTE'

    df['estado'] = df['stock'].apply(nivel_stock)
    print(df[['nombre', 'stock', 'estado']])

def graficar_stock(df):
    print("\n ---GENERANDO GRÁFICA DE STOCK---")
    
    #Definimos los colores basados en el stock
    colores = []
    for s in df['stock']:
        if s < 5: colores.append('red') #Crítico
        elif s <= 20: colores.append('orange') #Normal
        else: colores.append('green')

    plt.figure(figsize=(10, 6))
    plt.bar(df['nombre'], df['stock'], color=colores, edgecolor='black')

    # Algunas personalizaciones del diseño
    plt.title('Niveles de Inventario por Producto', fontsize=14)
    plt.xlabel('Productos', fontsize=12)
    plt.ylabel('Unidades en Stock', fontsize=12)
    plt.xticks(rotation=45) #Rotamos los nombre para que se lean bien
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout() #Ajusta los margenes automaticamente

    #En lugar de mostrarla (que a veces falla en servidores), la guardamos

    plt.savefig('reporte_stock_colores.png')
    print("¡Gráfica guardada exitosamente como 'reporte_stock_colores.png'!")

def guardar_inventario_limpio(df, nombre_archivo):
    df_final = normalizar_datos(df)
    df_final = validar_datos(df_final)
    df_final.to_json(nombre_archivo, orient='records', indent=4)
    print(f"Se exportó correctamente el archivo {nombre_archivo}")
    clasificar_inventario(df_final)
    graficar_stock(df_final)

    #--- RESUMEN EJECUTIVO (KPIs) ---
    total_productos = len(df_final)
    valor_total = (df_final['precio'] * df_final['stock']).sum()
    stock_total = df_final['stock'].sum()

    print("RESUMEN DEL INVENTARIO")
    print(f"Total de productos distintos: {total_productos}")
    print(f"Total de productos en almacen: {stock_total}")
    print(f"Valor total del patrimonio {valor_total:,.2f}")

guardar_inventario_limpio(df, 'df_limpio.json')