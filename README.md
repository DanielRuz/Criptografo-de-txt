# Criptografo-de-txt

Programa en python que es capaz de encriptar y desencriptar el contenido de un archivo txt. Los mensajes se encriptan con la palabra clave codigoencriptador.

## Instalación de dependencias

El programa solo usa una dependencia que no es estandar en python. Por tanto, se puede instalar con la instrucción:

`pip3 install -r requiriments.txt`

## Manual de uso

Para correr el programa es suficiente con la instrucción:

`python3 Main.py`

O bien, insertando el nombre del txt a encriptar o desencriptar desde la línea de comando:

`ṕython3 Main.py quijote.txt`

Si el nombre del archivo txt no es recibido desde la línea de comando, se solicita en la ejecucción del programa. Posteriormente, se deberá seleccionar la opción de encriptar o desencriptar según sea el caso.

Los mensajes encriptados se guardaran en un archivo txt con la palabra encrypt_ mas el nombre del txt que se usó como parámetro.

Los mensajes desencriptados se muestran en pantalla. Si no se introduce un mensaje encriptado para esta opción, se retornará False.
