try:
    with open ('saldo.txt', 'r') as file:
        monto_cajero = int(file.read()) 
except (FileNotFoundError, ValueError):
    monto_cajero = 0
    with open('saldo.txt', 'w') as file:
        file.write("0")
    
intentos = 0
intentos_restantes = 3
#Este contraseña tan simplona no representa la robustez que debe tener un sistema en la vida real JAJAJA
pin_maestro = "1234"

def cajero():
    global monto_cajero
    global intentos 
    global intentos_restantes

    while intentos < 3:

        contraseña = input("Ingresa tu contraseña para usar este cajero, por favor")
        if contraseña == pin_maestro:
            print("¡Bievenido!")
            while True:
                monto = int(input("Ingresa la cantidad a ingresar o retirar, por favor"))
                if monto > 0:
                    print("La cantidad se agregó con éxito")
                    monto_cajero += monto
                    print("La cantidad en tu cuenta ahora es, ", monto_cajero)  
                elif monto < 0 :
                    if monto < monto_cajero:
                        print("Se retiró con éxito la cantidad")
                        monto_cajero += monto
                        print("La cantidad en tu cuenta ahora es, ", monto_cajero)  
                    else:
                        print("no puedes retirar más de la cantidad que tienes disponible")
                else:
                    print("este valor no es válido")    
                    break
                with open ('saldo.txt', 'w') as file:
                    file.write(str(monto_cajero))
                respuesta = input("Escribe 'salir' para terminar:")
                if respuesta == "salir":
                    break
        else:
            intentos_restantes -= 1
            intentos += 1
            print(f"Acceso denegado, te quedan {intentos_restantes} intentos")
cajero()