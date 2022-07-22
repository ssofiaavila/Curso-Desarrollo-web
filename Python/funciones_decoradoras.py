#es una funcion que se aplica sobre otra funcion

def asteriscos(funcion): #tengo la funcion asteriscos que dentro tiene otra funcion
    def poner_asteriscos():
        print("******************")
        funcion()
        print("******************")
    return poner_asteriscos() #ejecutada la funcion asteriscos, retornará la funcion poner_asteriscos()


def imprimir():
    print("Buen día")



imprimir= asteriscos(imprimir) #estaria redefiniendo la funcion imprimir con una nueva funcion
#si no puedo hacer @imprimir
