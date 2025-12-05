# zona de funciones
def capturar_datos():
    numero= int(input("dijite el numero:"))
    return numero
def analisa_datos(num):
    while num!=0:
        
        if num%2==0:
            num="el numero es par"
            return num
        else:
            num="el numero es impar"
            return num
        
def mostrar_mensaje(numero,num):
    mensaje= f"el numero {numero} es {num}"
    return mensaje
def imprimir_mensaje(mensaje):
    print(mensaje)   
    
    
#zona de codigo principal
dato_numero=capturar_datos()
dato_num= analisa_datos(dato_numero)
mensaje=mostrar_mensaje(dato_numero,dato_num)
imprimir_mensaje(mensaje)

        