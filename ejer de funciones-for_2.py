#zona de funciones
def capturar_datos():
    cantidad=int(input("dijite la cantidad de numeros a sumar:"))
    return cantidad
def capturar_datos2(i):
    numero=int(input("dijite el numero:"+ str(i+1)+":"))
    return numero
def analizar_datos(cantidad,suma):
    for i in range(cantidad):
        numero=capturar_datos2(i)
        suma=suma+numero
    return suma
def mostrar_mensaje(suma):
    mensaje=f"la suma total es:"+  str (suma)  
    return mensaje 
def imprimir_mensaje(mensaje):
    print(mensaje)
#zona de condigo principal
dato_cantidad=capturar_datos()
suma=0
suma=analizar_datos(dato_cantidad,suma)
mensaje=mostrar_mensaje(suma)
imprimir_mensaje(mensaje)