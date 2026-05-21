# Metodo para convertirun texto en mayuscula
texto_minuscula:str="hola"
print(texto_minuscula.upper())
# Metodo para convertir un texto en mainusculas
texto_mayuscula:str="HOLASSSSS"
print(texto_mayuscula.lower())
# Metodo para convertir sola la primera letra en mayuscula
texto:str="buenos dias"
print(texto.capitalize())
# Metodo para convertir la primera letra de cada palabra en mayuscula como un titulo
print(texto.title())

#Metodo par quitar espacios
texto_espacios:str="        osos           "
print(texto_espacios)
#Este metodo quita los espacios que estan a la deecha e izquierda. si deseamos quitar solo los espacios de la izquierda usamos el metodo lstrip() y si deseamos quitar los espacios solo de la derecha usamos rstrip()
print(texto_espacios.strip())

# Metodo para buscar un caracter o conjunto de caracteres
# Find retorna el indicedonde comienza el texto a buscar si el texto no se encuentra retornara -1
parrafo:str="mi mama me ama yo amo ami mama de lucas"
print(parrafo.find("lucas"))
print(parrafo[35:])

# Metodo para remplazar una parte de texto
texto_incorrecto:str="gianfranco es malo" 
print(texto_incorrecto.replace("malo","bueno"))

#(Metodo) operador binario de existencia 
# este operador verifica si cierto texto existe o no dentro de otra retorna True si existe y False si no 
vocales:str="aeiouAEIOU"
print("A" in vocales)

#averiguar que son y cuales son los operador unarios, binarios y ternarios.

not False

# Ternario
# valor_si_verdado if condicion else valor_si_falso
print("es verdad" if 20>18 else "es falso")

## realizar un programa que nos pida la contraseña si la contraseña es correcta el usuario podra ingresar caso contrario le dara un mensaje de contraseña incorrecta

password_user:str=input("ingresa tu contraseña:")
print("bienvenido al sistema" if password_user=="hola1234" else "contraseña incorrecta")