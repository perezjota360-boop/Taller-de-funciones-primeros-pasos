# zonq de fuinciones
def capturar_numero():
    numero = int(input("Introduce un número entero: "))
    return numero

def identificar_numero(dato_numero):
        if dato_numero > 0:
            return "positivo"
        elif dato_numero < 0:
            return "negativo"
        else:
            return "cero"
def generar_mensage(numero, dato_numero):       
    mensaje= f"El número {numero} es {dato_numero}."
    return mensaje

def imprimir_mensage(mensage):
    print (mensage)
# zona principal
numero = capturar_numero()
dato_numero = identificar_numero(numero)
mensage = generar_mensage(numero, dato_numero)
imprimir_mensage(mensage)
