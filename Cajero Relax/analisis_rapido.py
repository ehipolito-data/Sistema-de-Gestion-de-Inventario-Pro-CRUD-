import pandas as pd

df = pd.read_json('inventario.json')

print("--- TU INVENTARIO COMO DATAFRAME ---")
print(df)

print("\n--- RESUMEN ESTADISTICO ---")
print(df.describe())

df['valor_total_stock'] = df['precio'] * df['stock']

print("\n--- INVENTARIO VALORIZADO ---")
print(df[['nombre', 'precio', 'stock', 'valor_total_stock']])

#stock_bajo = df['stock'] < 5

#print(stock_bajo)
print('\n Elementos con menos de 5 de stock')

stock_bajo = df[df['stock'] < 5] 

print(stock_bajo)

print("\n---ALERTA DE REABASTECIMIENTO (Stock < 5)---")
if not stock_bajo.empty:
    print(stock_bajo[['nombre', 'stock']])
else:
    "Todo en orden, no hay stock bajo"

#Guardamos solo los productos que necesitan reabastecerse

stock_bajo.to_excel('Alerta_Reabastecimiento.xlsx', index=False)
print("\n ¡Archivo 'Alerta_Reabestecimiento.xlsx' generado con éxito!")