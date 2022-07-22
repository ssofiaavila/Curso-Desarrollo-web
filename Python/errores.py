fichero= open("datos.txt","w") #w o r indica si hago una lectura o escritura
fichero.write("Datos para fichero")
fichero.close()

fichero2=open("datos2.txt","r") #error porque quiero leer un fichero que no existe
fichero2.write("Datos para fichero")
fichero2.close()

#para evitar excepcion deberia
try: #intenta
    fichero2=open("datos2.txt","r")
    fichero2.write("Datos para fichero")
    fichero2.close()
except: #ejecutará esto en caso de error
    print("Error, el fichero no existe")
else: #si no surve error, ejecutará esto
    print("Tratamiento para fichero correcto")
finally: #se ejecuta en todos los casos
    print("Continua el programa")
