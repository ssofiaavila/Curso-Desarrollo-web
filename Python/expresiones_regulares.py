import re

texto= "Argentina campeón" #texto en el que buscaré
patron="Argentina" #patron que tengo que buscar en la cadena
encontrado=re.seach(patron,texto) #encontrado almacenará si existe el patrón
if encontrado:
    print("Patron {} encontrado en el texto".format(patron))
else:
    print("Patron {} no encontrado".format(patron))
