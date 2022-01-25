import cryptocode

#Encripta el contenido de un archivo txt y lo guarda en otro
def encriptar_txt(nombre_txt):

	#Lee el contenido del txt
	archivo_txt = open(nombre_txt,'r')
	contenido_txt = archivo_txt.read()
	archivo_txt.close()
	
	#Encripta el contenido con palabra clave
	contenido_encriptado = cryptocode.encrypt(contenido_txt,"codigoencriptador")
	
	#Guarda el contenido encriptado en un txt
	output_txt = open("encrypt_" + nombre_txt, 'w')
	output_txt.write(contenido_encriptado)
	output_txt.close()
	
#Desencripta el contenido de un txt y lo muestra en pantalla	
def desencriptar_txt(nombre_txt):

	#Lee el contenido del txt
	archivo_txt = open(nombre_txt,'r')
	contenido_txt = archivo_txt.read()
	archivo_txt.close()
		
	#Desencripta el contenido	
	contenido_desencriptado = cryptocode.decrypt(contenido_txt,"codigoencriptador")	
	
	#Lo muestra en pantalla
	print(contenido_desencriptado)
	
	
	
