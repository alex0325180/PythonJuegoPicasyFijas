from random import randint

def __generar_secreto__(cantidad): #Se genera un numero aleatorio sin repeticion
    secreto = []
    while True:
        d = randint(0, 9)
        if d not in secreto:
            secreto.append(d)
        if len(secreto) == cantidad:
            break
    return secreto

def __validar_numero__(numero): #Se valida que cada digito del numero sea diferente
    if len(numero) == 1:
        return True
    else:
        if numero[0] in numero[1:]:
            return False
        else: 
            return __validar_numero__(numero[1:])

def __validar_longitud__(numero,longitud): #Se revisa la longitud del numero
    if len(numero) == longitud:
        return __validar_numero__(numero)
    else:
        return False
