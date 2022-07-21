lista=[2,4,6,8,10]
print(lista)
lista.pop() #elimina el ultimo elemento de la lista#
lista.pop(0) #elimina el elemento del indice indicado
print(lista)

lista.reverse() #invierte el orden de la lista
print(lista)

lista.sort()
print(lista)

#formar listas anidadas o lo podría ver como una matriz
anidada=[0,lista]
print(anidada)
elemento= anidada[1][1]
print(elemento)


#crear una lista con otra lista
matriz={[1,2,3],[4,5,6],[7,8,9]}
lista_nueva= [elemento[0] for elemento in matriz] #por cada elemento de la posicion 0 de la matriz
print(lista_nueva)
