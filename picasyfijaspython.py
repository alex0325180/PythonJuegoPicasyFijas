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
def __puntaje__(a):
    f = open("archivo.txt","r")
    menor=1000
    puntajes = []
    for i in f:
        i = i.rstrip()
        if not i.startswith(a):
            continue
        score = i.split(",")
        puntajes.append(score)
        puntaje = int(score[1])
        if(menor > puntaje):
            menor = puntaje
    for j in puntajes:
        menor=str(menor)
        if (j[1]==menor):
            print ("El mejor en ",a," digitos es:",j[3]," con ",j[1]," intentos")
    
    


def __comprobar__(
    intentos,numero,
    entrada): #Comienza el juego de picas y fijas
    resultado = ""
    for i in range(intentos):
            fijas = 0
            picas = 0
            if intentos == 1:
                resultado = "perdiste "
                print(resultado)
                intent = 0
                return [len(numero),intent, resultado]
            else:
                for i in range(len(entrada)):
                    if numero[i] == entrada[i]:
                        fijas = fijas + 1
                    elif numero[i] in entrada:
                        picas = picas + 1
                if fijas == len(entrada):
                    resultado = "ganaste"
                    print(resultado)
                    intent = 11 - intentos
                    return [len(numero),intent, resultado]
                intentos= intentos-1
                print("tienes ", fijas, "fijas y tienes ", picas, "picas\n intentos restantes: "
                ,intentos)
                while True:
                    entrada = [int(x) for x in input("Ingrese un numero: ")]
                    if __validar_longitud__(entrada,len(numero)) == True:
                        break           
                    try:
                        e = __validar_longitud__(entrada,len(numero))
                        if e == False:
                            quit()
                    except:
                        print("Ingrese un numero valido")
                        continue
                
    
cifras = 0
intentos = 0
