lista=[1,2,3,4,5]
def par(numero): #paso un numero y si es par retorna true si no, false
    resultado=(numero % 2) == 0
    return resultado

filtro=filter(par,lista) #filter aplica una funcion a una colección de valores
pares=list(filtro)
print(pares)

#otra manera de expresar una función lambda es
filtro2= filter(lambda numero: (numero %2) == 0,lista)
pares2=list(filtro)
print(pares2)
