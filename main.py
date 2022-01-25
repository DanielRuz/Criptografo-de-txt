import sys
import os
import modulo_criptografo

#Si no recibe parametro desde la terminal, pregunta por el
if (len(sys.argv) == 1):

	nombre_txt = input("Inserte nombre de archivo txt:")
	
else:

	nombre_txt = sys.argv[1]
	

#Verifica que exista el archivo	
if(not os.path.isfile(nombre_txt)):

	print("Nombre no valido")
	sys.exit()
	

#Solicite una opcion
opcion = input("(1) Encriptar \n(2) Desencriptar \nOpcion:")


#La primer opcion encripta el contenido de un txt y lo guarda en otro
if(opcion == '1'):
	
	modulo_criptografo.encriptar_txt(nombre_txt)

#La segunda opcion desencripta el contenido de un txt y lo muestra en la terminal	
elif (opcion == '2'):

	modulo_criptografo.desencriptar_txt(nombre_txt)

#Si se da una opcion diferente, termina el programa	
else:

	print("Opcion no valida")
	sys.exit()		

	
