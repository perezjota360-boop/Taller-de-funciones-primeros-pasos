#zona de funciones
def capturar_datos(i):
    numero=int(input("dijite el numero:"+ str(i+1)+":"))
    return numero
suma=0
def analizar_datos(suma):
    for i in range(0,10,2):
        numero=capturar_datos(i)
        suma=suma+numero
    return suma
def mostrar_mensaje(suma):
    mensaje=f"la suma total es:"+ str(suma)  
    return mensaje 
def imprimir_mensaje(mensaje):
    print(mensaje)
#zona de condigo principal
dato_suma=analizar_datos(suma)
mensaje=mostrar_mensaje(dato_suma)
imprimir_mensaje(mensaje)